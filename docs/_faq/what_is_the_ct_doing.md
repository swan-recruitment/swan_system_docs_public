Awesome—here’s a deep, design-level walkthrough of the Control Tower (CT) work you now have in the repo, expanding every highlight and turning the smoke test into a concrete, step-by-step runbook.

---

# 1) Architecture & Data Model (deep dive)

## 1.1 High-level components

* **Producers**: Portal, Backend (Firebase Functions), Finance Integration, Desktop Manager, Website, GitHub Actions.
* **CT API (FastAPI)**: Receives events (`POST /events`), exposes read endpoints (`/health`, `/systems`, `/events`, `/runs`), and executes allow-listed triggers (`/triggers/{name}`).
* **Event Router (in-CT)**: Validates HMAC, enforces idempotency, persists to `events` collection, fans out to:

  * **Runs DB** (`runs`): Durable audit for staff- or system-initiated operations.
  * **Systems DB** (`systems`): State for health dashboards & SLOs.
  * **DLQ / Retries**: Backoff queue for transient failures (e.g., Firestore write, downstream not ready).
* **Schedulers/Reporters**: Time-based jobs, e.g., 08:00 Europe/London daily digest.
* **UI (optional)**: Thin tables/cards built later; not required for MVP.

## 1.2 Idempotency, retries, DLQ, HMAC

* **Idempotency**: Every event must carry a unique `eventId`. CT rejects a duplicate `eventId` with a deterministic 200/202 “duplicate/accepted” outcome (so producers can safely retry without creating duplicates).
* **Retries**: Transient CT write failures (e.g., Firestore hiccups) retry with exponential backoff (e.g., 1s, 2s, 4s, … capped). After N attempts, the payload goes to **DLQ** with context (error, attempt, next review).
* **DLQ**: Durable store (FireStore+Storage) with a small UI or CLI to replay or tombstone items.
* **HMAC verification**: Producers include `X-CT-Signature: sha256=<hex>` over the **raw request body** using a shared secret (rotated quarterly). CT recomputes and compares; if mismatch → 401.

## 1.3 Canonical collections (Firestore)

### `events` (append-only)

* **Purpose**: Immutable record of happenings across systems.
* **Core fields**:
  `eventId`, `type`, `ts`, `source`, `correlationId`, `payload`, `ingest{receivedAt, attempt, status}`
* **Notes**:

  * `correlationId` ties events to a `runId` when the event is a consequence of a trigger/backfill.
  * `payload` is **redacted** (see redaction rules below).
  * Indexes: by `ts`, `source`, and `type` (compound where helpful).

### `runs` (durable audit)

* **Purpose**: Everything CT *does* on purpose (e.g., triggers, backfills).
* **Core fields**:
  `runId`, `trigger`, `initiator`, `inputs`, `status`, `metrics`, `logs[]`, `createdAt/updatedAt/endedAt`
* **Notes**:

  * `logs[]` can be pointers to Storage objects for larger outputs.
  * `metrics` captures measurable results (processed N invoices, duration ms, etc).

### `systems` (health + SLOs)

* **Purpose**: Latest health status for top-level systems.
* **Core fields**:
  `systemId`, `status (green|amber|red|unknown)`, `lastHeartbeat`, `errors24h`, `slo{…}`, `notes`
* **Derived**: Status often computed from recent events + SLO policy.

---

# 2) Event Taxonomy v1 + Redaction Rules

## 2.1 Taxonomy (examples + when to emit)

| Type                        | Source  | When to emit                                       | Example payload (before redaction)                                                               |
| --------------------------- | ------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `desktop.trigger.contract`  | desktop | Staff triggers contract pack regen                 | `{ "contractorId":"C123", "contractId":"K456" }`                                                 |
| `excel.timesheet.ingested`  | backend | Legacy Excel → Python pipeline ingests a timesheet | `{ "contractorId":"C123","period":"2025-W36","items":[...],"totalHours":37.5 }`                  |
| `finance.invoice.generated` | finance | Invoice PDF created                                | `{ "invoiceId":"INV-2025-0912","period":"2025-09","total":1234.56,"vat":246.91 }`                |
| `finance.payment.webhook`   | finance | Payment provider webhook                           | `{ "invoiceId":"INV-2025-0912","statusFrom":"pending","statusTo":"paid" }`                       |
| `backend.fn.error`          | backend | Function error (uncaught or severe)                | `{ "fnName":"timesheetParse","severity":"high","stackRef":"gs://.../log.txt" }`                  |
| `portal.upload.received`    | portal  | Contractor uploads file                            | `{ "contractorId":"C123","fileRef":"gs://.../upload.pdf" }`                                      |
| `website.form.submitted`    | website | Contact form submitted                             | `{ "formId":"lead-123","captchaScore":0.91 }`                                                    |
| `ci.workflow.failed`        | github  | Protected branch CI fails                          | `{ "repo":"swan-portal","runId":1234567,"job":"build","url":"https://github.com/.../runs/..." }` |

## 2.2 Redaction rules (applied **before** storing in `payload`)

* Strip or hash PII: names, emails, phone numbers, bank details, NI numbers.
* Replace document contents with pointers: keep `Storage` refs and metadata, not file bytes.
* For financial data, keep **totals** and **invoice IDs**, but drop line-item PII if any.
* For errors, keep `stackRef`/`logRef` instead of full stack traces in the event record.

**Result**: `payload` remains useful for dashboards/analytics and safe to share internally.

---

# 3) API Surface (how to call it, what it returns)

> OpenAPI file is in `docs/design/openapi/control_tower.yaml`

## 3.1 `POST /events` — Ingest an event

* **Headers**:

  * `Authorization: Bearer <SERVICE_TOKEN>`
  * `X-CT-Signature: sha256=<hex>` (HMAC over raw JSON)
  * `Content-Type: application/json`
* **Body (min required)**:

  ```json
  {
    "eventId": "evt_01J9Z4...",
    "type": "finance.invoice.generated",
    "ts": "2025-09-27T12:03:00Z",
    "source": "finance",
    "payload": { "invoiceId":"INV-2025-0912","period":"2025-09","total":1234.56 }
  }
  ```
* **Responses**:

  * `202 Accepted` — event recorded (or recognized as duplicate idempotently)
  * `401 Unauthorized` — bad token or HMAC
  * `422 Unprocessable Entity` — missing fields or bad types (schema mismatch)
* **Idempotency behavior**: same `eventId` → same response semantics (no duplicates).

## 3.2 `GET /events` — Query events

* **Query params**: `source`, `type`, `from`, `to`, (optionally paging parameters later).
* **Auth**: `maintainer`+.
* **Use**: dashboards, CT UI tables, troubleshooting.

## 3.3 `GET /health` & `GET /systems`

* **`/health`**: aggregate + per system snapshot (computed status).
* **`/systems`**: raw system docs with SLO evaluation details.

## 3.4 `POST /triggers/{name}`

* **Allow-list** only (e.g., `contract.regenerate`, `finance.export.backfill`, `portal.notify.retry`).
* **Auth**: `operator`+.
* **Body**: trigger-specific inputs (validated), e.g. `{ "contractId":"K456" }`.
* **Returns**: `202 Accepted` + `{ "runId": "run_..." }`.
* **Side-effects**: Creates a `runs` record, may emit derived `events` as things happen.

## 3.5 `GET /runs/{runId}`

* **Use**: drilldown for a specific operation (status, metrics, links to logs and correlated events).

## 3.6 `GET /reports/daily`

* **Returns**: JSON/Markdown digest (also archived in Storage).
* **Schedule**: generated at **08:00 Europe/London** (configurable).

---

# 4) SLOs, Alerts & Dashboards (how they’re measured and shown)

## 4.1 SLOs (targets & computation)

* **Event intake latency p95 ≤ 5m**

  * Compute `ingest.receivedAt - ts` for window (24h rolling). P95 under 5m = **Green**, 5–10m **Amber**, >10m **Red**.
* **Run success rate ≥ 99% (7d rolling)**

  * `runs` with `status=success` / total (excluding `cancelled`).
* **Heartbeat**: no gap > 15m in business hours

  * Expect at least one `events` heartbeat or known activity; otherwise degrade to **Amber/Red**.

## 4.2 Alerts

* **Function errors**: if `backend.fn.error` >= 3 in 10 minutes **and** severity `high` → alert (email/pager).
* **Stuck runs**: `status=running` beyond SLA → alert in digest + optional immediate.
* **DLQ depth**: over N items for > 30 min → alert.

## 4.3 Dashboards blueprint (what you’ll build)

* **Executive Status**: cards per system (G/A/R) + overall green%.
* **Event Stream**: timeline & filters by `source`, `type`, time range.
* **Runs**: success rate, duration P50/P95, failure reasons (bar chart).
* **Finance**: invoices generated vs paid (30d), average days-to-pay.
* **CI**: workflows failed per repo (7d), drill into latest failed job.
* **Exceptions**: DLQ depth over time, retries trend, top error signatures.

---

# 5) Security: RBAC, tokens, redaction, immutability, retention

## 5.1 RBAC (roles → permissions)

* **owner**: everything (`*`)
* **maintainer**: read events/runs/systems, execute triggers
* **operator**: execute triggers + read
* **viewer**: read events/runs/systems

## 5.2 Tokens & rotation

* **Bearer tokens** per producer (scoped; rate-limited).
* **Rotation**: Quarterly. Store in Secret Manager; never in repo. Keep 1 overlap window.

## 5.3 HMAC

* **Secret** env var (e.g., `CT_WEBHOOK_SECRET`).
* **Signature**: `sha256` HMAC of **raw body**. Compare using constant-time equality.

## 5.4 PII redaction (again because it’s key)

* Redact at **source** when feasible; otherwise CT middleware strips PII fields and stores a pointer to Storage (for auditors only).

## 5.5 Audit immutability

* `events` and `runs` are append-only.
* Corrections are new events (e.g., `event.corrected`) with references to originals.

## 5.6 Backups & retention

* `events`: 180d
* `runs`: 365d
* `systems`: 90d
* Daily export to Storage; periodic coldline if needed.

---

# 6) Milestones, Acceptance, Risks—expanded

## Phase 1 — Foundations

* **Deliver**: OpenAPI stub, schemas for `events/runs/systems`, Firestore collections, HMAC verify, idempotency check.
* **Exit**: Can `POST /events` (202 Accepted) and `GET /events` returns it; `GET /health` responds.

## Phase 2 — Health & Runs

* **Deliver**: `systems` heartbeat evaluation; `/runs/{runId}` with metrics, structured logs to Storage.
* **Exit**: Triggered action produces a `run` and correlated `events`; `/systems` shows computed statuses.

## Phase 3 — Triggers & Digest

* **Deliver**: Allow-list triggers operational; daily digest generator emits Markdown and archives it.
* **Exit**: Operator can safely run `contract.regenerate`; digest visible at 08:00 Europe/London.

## Phase 4 — Dashboards & SLOs

* **Deliver**: Implement dashboard blueprint (UI or report), SLO thresholds & alerts configured.
* **Exit**: Executive Status and key charts deployed; alerts tuned.

### Acceptance Criteria (condensed)

* Schemas live; HMAC & idempotency enforced.
* ≥ 3 producers integrated (backend, finance, CI).
* Daily digest generated & archived.
* Triggers audit to `runs` with metrics.
* SLOs computed; dashboards render.
* OpenAPI published; smoke tests green.

### Risks & Mitigations

* **Drift**: weekly taxonomy review + CI checks.
* **Alert fatigue**: dedupe & severity thresholds; digest for non-critical.
* **Auth gaps**: secret manager + rotation; minimal scopes.
* **Duplicates**: idempotency + DLQ with replay controls.

---

# 7) Concrete Smoke Test Plan (commands you can run)

> These are example commands once the API is implemented and running locally or in a dev environment.

## 7.1 Compute an HMAC and send an event (shell)

```bash
BODY='{"eventId":"evt_demo_001","type":"finance.invoice.generated","ts":"2025-09-27T10:00:00Z","source":"finance","payload":{"invoiceId":"INV-2025-0912","period":"2025-09","total":1234.56}}'
SECRET="replace-with-CT_WEBHOOK_SECRET"
SIG=$(printf '%s' "$BODY" | openssl dgst -sha256 -hmac "$SECRET" -binary | xxd -p -c 256)

curl -i https://ct.dev.swan/events \
  -H "Authorization: Bearer DEV_TOKEN_FINANCE" \
  -H "X-CT-Signature: sha256=$SIG" \
  -H "Content-Type: application/json" \
  -d "$BODY"
# Expect: HTTP/1.1 202 Accepted
```

* **Repeat the same request** → expect **202 Accepted** again (idempotent) and **no duplicate** in `events`.

## 7.2 List events

```bash
curl -s "https://ct.dev.swan/events?source=finance&type=finance.invoice.generated&from=2025-09-27T00:00:00Z" \
  -H "Authorization: Bearer DEV_TOKEN_MAINTAINER" | jq .
# Expect: array with the event above
```

## 7.3 Execute a trigger (allow-listed)

```bash
curl -s -X POST https://ct.dev.swan/triggers/contract.regenerate \
  -H "Authorization: Bearer DEV_TOKEN_OPERATOR" \
  -H "Content-Type: application/json" \
  -d '{"contractId":"K456"}' | jq .
# Expect: { "runId": "run_..." }
```

Then:

```bash
curl -s https://ct.dev.swan/runs/run_... \
  -H "Authorization: Bearer DEV_TOKEN_MAINTAINER" | jq .
# Expect: status, metrics (e.g., documentsGenerated), links to logs/events
```

## 7.4 Generate/read daily digest (placeholder script in repo)

```bash
python scripts/control_tower/generate_daily_digest.py
# Prints markdown to stdout; in real CT, archive to Storage & expose via /reports/daily
```

---

# 8) Where things live in your repo

* **WO**: `docs/work_orders/work_order_control_tower__MERGED.md`
* **OpenAPI**: `docs/design/openapi/control_tower.yaml`
* **Schemas**: `docs/control_tower/schemas/{event,run,systems}.schema.json`
* **Dashboards spec**: `docs/control_tower/dashboards_spec.md`
* **Config example**: `docs/control_tower/config.example.yaml`
* **Digest helper**: `scripts/control_tower/generate_daily_digest.py`

---

# 9) Optional next tweaks (quick wins)

* **Spectral lint in CI** for the OpenAPI (catches schema drift, undocumented endpoints).
* **CT UI scaffold**: a minimal React page (table of events, cards for systems, run drilldown) backed by the endpoints above.
* **Replay tool** for DLQ items: small script to re-submit failed events with a new `eventId`.

If you want, I can add (a) a `spectral.yaml` and a GitHub Action to lint `control_tower.yaml`, and/or (b) a UI scaffold checklist so you can bootstrap the first dashboard page quickly.
