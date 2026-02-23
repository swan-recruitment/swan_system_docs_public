# 🧭 Work Order: Swan Recruitment — Control Tower (CT)
**Backlinks:** [Master WO (Full)](work_order_master__FULL.md) · [Work Orders Index](work_orders_index.md)

**Last updated:** 2025-09-26  
**Backlink:** [Work Orders Index](work_orders_index.md)

---

## 1) Objective
Deliver a **single orchestration & observability layer** that:  
- Aggregates **health**, **events**, and **runs** from all subsystems (Backend, Portal, Website, Finance, Desktop, GitHub/CI).  
- Provides **operational controls** (safe triggers), **daily/weekly reporting**, and **audit**.  
- Exposes a **small REST API** for internal tooling and a pragmatic **UI** (optional MVP: stats + tables).

**Non-goals (MVP):**
- Replacing subsystem UIs or Firebase Console.
- Deep analytics BI (beyond operational roll-ups).

---

## 2) Scope & Success Criteria
### In-scope (MVP)
- Event ingestion (push Webhooks + pull Polling) with **Idempotency**, retries, and DLQ.
- Health model: `systems` with status, last heartbeat, error count, SLOs.
- Runs model: durable audit of triggers/batches with correlation IDs.
- Triggers (limited, safe-listed): e.g., regenerate contract pack, backfill finance export.
- Reports: daily digest (email/Slack-ready text), weekly health trend.
- REST API: `/health`, `/events`, `/runs`, `/systems`, `/reports/daily`.
- RBAC: roles `owner`, `maintainer`, `operator`, `viewer`.
- Observability: structured logs + metrics; dashboards spec.

### Out-of-scope (MVP)
- Real-time streaming UI; advanced anomaly detection; multi-tenant.

**Definition of Done (MVP):**
- SLOs defined and measured; CT shows **Green/Amber/Red** per system.  
- Trigger actions are **audited** and **idempotent**.  
- Daily digest file is generated and archived; emailed/slacked manually or via future hook.  
- API documented with **OpenAPI** and protected with **service tokens**.

---

## 3) Architecture Overview
```mermaid
flowchart TD
  subgraph Producers
    P1[Portal] --> E((CT API))
    P2[Backend / Functions] --> E
    P3[Finance Integrations] --> E
    P4[Desktop Manager] --> E
    P5[GitHub Actions] --> E
  end
  E --> Q[Event Router (in-CT)]
  Q --> R[(Runs DB)]
  Q --> S[(Systems DB)]
  Q --> D[DLQ / Retries]
  subgraph CT
    API[CT REST API]
    SVC[Schedulers & Reporters]
    UI[(CT UI)]
  end
  R -. audit .- UI
  S -. health .- UI
  SVC --> R
  SVC --> S
```

**Runtime:** Python (FastAPI) for API + schedulers; Firestore for `runs`, `events`, `systems`; optional small React UI or Desktop embed.  
**Auth:** Firebase Auth (service accounts for producers) + **HMAC** for webhooks.  
**Resilience:** Exponential backoff, DLQ, idempotency keys, pagination & rate-limit guards.

---

## 4) Data Model (Canonical)

### 4.1 `events` (append-only)
- `eventId` (string, ksuid/uuid) — **idempotency key**  
- `type` (string) — see **Event Taxonomy**  
- `ts` (ISO8601) — producer timestamp  
- `source` (enum) — `portal|backend|finance|desktop|github|website`  
- `correlationId` (string) — links to a `run` when applicable  
- `payload` (object, redacted)  
- `ingest` (object) — `{receivedAt, attempt, status}`

### 4.2 `runs` (durable audit)
- `runId` (string) — stable ID across retries  
- `trigger` (string) — e.g., `desktop.trigger.contract`  
- `initiator` (string) — user/service id  
- `inputs` (object) — parameters (redacted fields masked)  
- `status` (enum) — `queued|running|success|failed|cancelled`  
- `metrics` (object) — counts, durations, amounts  
- `logs` (array) — structured log refs (Storage)  
- `createdAt`, `updatedAt`, `endedAt`

### 4.3 `systems` (health & SLOs)
- `systemId` (string) — e.g., `portal`, `backend`, `finance`  
- `status` (enum) — `green|amber|red|unknown`  
- `lastHeartbeat` (ts)  
- `errors24h` (int)  
- `slo` (object) — per-system SLOs with thresholds  
- `notes` (string)  

> JSON Schemas provided in `/docs/control_tower/schemas/`.

---

## 5) Event Taxonomy (v1)
| Type | When it fires | Key fields |
|---|---|---|
| `desktop.trigger.contract` | Staff triggers contract pack regeneration | contractorId, contractId |
| `excel.timesheet.ingested` | Timesheet parsed + stored | contractorId, period, items |
| `finance.invoice.generated` | Invoice PDF generated | invoiceId, period, total, vat |
| `finance.payment.webhook` | Payment status webhook received | invoiceId, statusBefore→After |
| `backend.fn.error` | Uncaught error in function | fnName, stackRef, severity |
| `portal.upload.received` | Contractor file uploaded | contractorId, fileRef |
| `website.form.submitted` | Client/contractor contact form | formId, captchaScore |
| `ci.workflow.failed` | GitHub CI failed on protected branch | repo, runId, job, url |

**Rules:**
- All events include `eventId`, `ts`, `source`, and **redaction policy** on PII.  
- HMAC signature header: `X-CT-Signature: sha256={hex}` over raw body, per secret key.  
- Idempotency: server rejects duplicates on `{eventId}`; producers must retry on `5xx` with same ID.

---

## 6) API (OpenAPI in repo)
Primary endpoints (documented in `docs/design/openapi/control_tower.yaml`):

- `GET /health` — overall + per-system health.  
- `POST /events` — authenticated producer ingest (HMAC + token).  
- `GET /events` — list/query (role: maintainer).  
- `POST /triggers/{name}` — execute an allowed trigger; returns `runId`.  
- `GET /runs/{runId}` — status & metrics.  
- `GET /systems` — list, with SLO evaluation.  
- `GET /reports/daily` — current daily digest (JSON/markdown).

**Auth & RBAC:**
- Header `Authorization: Bearer <token>` (service token) + optional Firebase user context.  
- Roles: `owner`, `maintainer`, `operator`, `viewer`.  
- Rate limits (per key): default `60/min`, burst `120`.

---

## 7) SLOs & Alerts (MVP targets)
- **Event intake latency** p95 ≤ **5m**.  
- **Run success rate** ≥ **99%** (rolling 7d).  
- **System heartbeat** no gaps > **15m** during business hours.  
- **Alerting:**  
  - Pager/Email on `backend.fn.error` severity ≥ `high` (>3 in 10m).  
  - Daily digest at 08:00 Europe/London summarising: new events count, failures, CI fails, payments updated.

---

## 8) Dashboards (spec in repo)
See `docs/control_tower/dashboards_spec.md` — define cards, charts, and queries:

- **Executive status** — per-system G/A/R, last update.  
- **Event stream** — timeline + filters.  
- **Runs** — success rate, durations, failure reasons.  
- **Finance** — invoices generated vs paid (last 30d).  
- **CI** — workflows failed by repo (last 7d).  
- **Exceptions** — DLQ depth, retries, top error types.

---

## 9) Triggers (allowlist)
| Trigger | Description | Inputs | Guards |
|---|---|---|---|
| `contract.regenerate` | Rebuild contract pack | `contractId` | idempotency, role ≥ operator |
| `finance.export.backfill` | Re-push invoices to accounts API | `fromDate` | rate limit; finance window |
| `portal.notify.retry` | Re-send notification | `uploadId` | exponential backoff |

All triggers:
- Emit a `run` with correlation to any emitted events.  
- Are retried with backoff; ensure **exactly-once** effects in targets.

---

## 10) Security & Compliance
- **AuthN**: service tokens stored in secret manager; keys rotated quarterly.  
- **AuthZ**: RBAC enforced in API; triggers require `operator+`.  
- **PII**: redact payloads at source; store references to Storage where needed.  
- **Audit**: every trigger/run write is immutable; edits only append notes.  
- **Backups**: daily export of `events/runs/systems` to Storage (30/180/365 days tiers).

---

## 11) CI/CD
- Lint/tests on PR; OpenAPI lint (`spectral`).  
- Build & deploy CT API (Cloud Run/Functions) with version tags.  
- Seed dashboards from spec file.  
- E2E smoke: send sample `POST /events` (HMAC) and read back via `GET /events` as `maintainer`.

---

## 12) Milestones & Exit Criteria
**Phase 1 — Foundations**  
- Schemas committed, OpenAPI drafted, basic storage created.  
- Exit: can ingest an event and list it.

**Phase 2 — Health & Runs**  
- Systems heartbeat + runs auditing live.  
- Exit: run shows in UI/API with metrics.

**Phase 3 — Triggers & Digest**  
- Allowlist triggers wired; daily digest generated and archived.  
- Exit: operator can run `contract.regenerate` safely.

**Phase 4 — Dashboards & SLOs**  
- Dashboards spec implemented; alert thresholds tuned.  
- Exit: SLOs computed; executive status view live.

---

## 13) Acceptance Criteria (MVP)
- [ ] `events`, `runs`, `systems` schemas implemented and validated.  
- [ ] HMAC verification for `/events`; idempotency enforced.  
- [ ] At least **3 producers** integrated (backend, finance, CI).  
- [ ] **Daily digest** produced at 08:00 Europe/London and archived.  
- [ ] Triggers audit to `runs` with success/failure and metrics.  
- [ ] Dashboards render spec’d charts; SLOs computed.  
- [ ] OpenAPI published in repo; endpoints exercised by smoke tests.

---

## 14) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Drift between subsystems & CT | M | M | Event taxonomy ownership; weekly review |
| Alert fatigue | M | M | Tune thresholds; dedupe; digest for non-critical |
| Auth gaps / token leakage | L | H | Secret manager + rotation; principle of least privilege |
| Duplicate events | M | M | Idempotency keys + HMAC + DLQ |
| Backfill impacts providers | L | M | Rate-limited triggers + windows |

---

## 15) Related Documents
- [Work Orders Index](work_orders_index.md)  
- [Phase Plans Index](../plans/phase_plans_index.md)  
- [Desktop Manager WO](work_order_desktop_manager.md) · [Finance Integration WO](work_order_finance_integration.md) · [Portal WO](work_order_contractor_portal.md) · [Website WO](work_order_website.md) · [Firebase Backend WO](work_order_firebase_backend.md)  
- [Visuals WO](work_order_visuals.md)

---

> Notes: This WO provides **schemas, API, event taxonomy, dashboards spec, SLOs, and security** so CT can be implemented with confidence and audited over time.
---
---

## Event Taxonomy
Use the standard CT events defined in [Event Taxonomy](../design/event_taxonomy.md).

**Core events used by this work order:**  
- `backend.parsed` / `backend.transform.applied` / `backend.fn.error` (processing)  
- `artifact.pointer.written` (artifact pointers)  
- `ct.run.started` / `ct.run.completed` (orchestration)

**Payload rules:** IDs-only, pointers not bytes, Money in minor units, ISO timestamps, **no PII**.


### 📏 Canonical Data Rules (Swan)
- Use **snake_case** field names; FKs end with **`_id`**.
- Money uses `{ "amount_minor": int, "currency": "GBP" }` (no floats).
- Dates = `*_date` (date) and `*_at` (datetime, ISO-8601).
- Import common types from **[`docs/schemas/common/common.json`](../schemas/common/common.json)**.
- Follow **PII redaction** policy in **[`docs/schemas/PII_POLICY.md`](../docs/schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`docs/design/field_lineage.md`](../docs/design/field_lineage.md)**.


## 16) Needs & Next Steps (Audit 2025-09-28)
- [ ] Expand CT README to index configs/schemas/dashboards.
- [ ] Add schema validation tooling (JS/Python) linked to fixtures.
- [ ] Flesh out dashboards spec with metric definitions + update frequency.
- [ ] Define dashboard automation (Firestore/Storage integration).
- [ ] Draft CT runbooks: escalation, recovery, troubleshooting.
- [ ] Merge Best Practices SOPs into CT docs.
