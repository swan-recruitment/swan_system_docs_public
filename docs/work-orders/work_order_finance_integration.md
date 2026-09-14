# 📝 Work Order: Swan Recruitment – Finance Integration (swan-accounts-integration)

**Last updated:** 2025-09-26
**Backlinks:** [Master WO (Full)](work_order_master__FULL.md) · [Work Orders Index](work_orders_index.md)

## 🎯 Objective
Deliver a secure, reliable **Finance Integration layer** that syncs approved invoices from the ERP into the accounting platform, brings **payment status** back into Firebase/Portal, and produces **reconciliation** outputs for finance review.  
*MVP focuses on automated invoice export and payment visibility; advanced BI dashboards live in Control Tower/Reporting.*

**Non‑goals (MVP)**
- Deep BI dashboards (handled by Control Tower/Reporting)
- Direct contractor payments or payouts (future scope)
- Complex multi‑currency rules (assume single currency initially)

---

## 🔑 Status Keys
🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred  

**Status:** 🟡 Drafted

---

## 1) Project & Environments Setup
- [ ] Repository: `swan-accounts-integration`
- [ ] Language/stack: **Node.js (TypeScript)** or **Python** (pick based on chosen provider SDK support)
- [ ] Environments: `sandbox` (vendor test), `staging`, `production`
- [ ] Baseline structure:
  - `src/` – integration logic
  - `tests/` – unit/integration tests
  - `.gitignore` – exclude `node_modules` / `__pycache__` / `/secrets`
  - `README.md` – project overview
- [ ] Secrets:
  - `.env.*` files (never committed)
  - GitHub Actions → **Repository Secrets**
  - Local **/secrets** folder (gitignored)

**Deliverable:** Empty integration repo with environment scaffolding and secrets policy.

---

## 2) Accounting API Integration
- [ ] **Select provider** (e.g., Xero / QuickBooks / Sage) and enable **sandbox** account
- [ ] **Credentials**: OAuth client/secret (or API key) stored securely; token refresh handled
- [ ] **SDK vs REST**:
  - Prefer official SDK; fall back to REST with typed clients
- [ ] **Error handling & idempotency**:
  - Retries with backoff; **idempotency keys** for create/update API calls
  - Pagination/rate‑limit awareness
- [ ] **Attachments** & PDFs: upload invoice PDFs where supported
- [ ] **Webhooks** (if provider supports) vs scheduled polling

**Deliverable:** Proven connectivity to sandbox account with a smoke test (ping + auth + simple list call).

---

## 3) Data Contracts & Field Mapping
Define deterministic mappings between ERP/Firebase entities and the accounting API.

**Invoice mapping (excerpt)**
| ERP (Firestore) | Accounts API | Notes |
|---|---|---|
| `invoiceId` | `external_id` / `reference` | used for idempotency & traceability |
| `contractorId` | `contact_id` | link to contractor/customer account |
| `client` | `customer` | customer record in accounts |
| `lines[].description` | `line_items[].description` | sanitized text |
| `lines[].hours` × `rate` | `line_items[].amount` | VAT rules applied |
| `vatRate` | `tax_rate` | default VAT rate (configurable) |
| `issuedAt` | `issue_date` | ISO date |
| `pdfUrl` | `attachments[]` | optional attachment upload |

**Status mapping (excerpt)**
| Accounts API | ERP/Portal |
|---|---|
| `DRAFT` | *Submitted* |
| `AUTHORISED` | *Accepted* |
| `PAID` | *Paid* |
| `VOID` | *Cancelled* |

**Deliverable:** `docs/mappings.md` with complete field map + examples.

---

## 4) Invoicing Workflow (Export → Accounts)
- [ ] Source **approved** invoices from Firestore
- [ ] Transform to provider schema; compute VAT; attach PDF (if present)
- [ ] **Create/Upsert** invoice in accounts system (use idempotency with `invoiceId`)
- [ ] Persist returned **accountsInvoiceId** + links back to Firestore
- [ ] Update Realtime DB for Portal status (e.g., *Accepted*)
- [ ] Emit **Control Tower** event (`finance.invoice.exported`)

**Deliverable:** End‑to‑end pipeline that exports ERP invoices into accounting and returns persistent IDs.

---

## 5) Payment Status Sync (Accounts → ERP/Portal)
- [ ] Prefer **webhook** subscription for payments; otherwise schedule **polling** (e.g., every 30–60 min)
- [ ] Map partial/full payments; handle credit notes
- [ ] Update Firestore + Realtime DB status to *Paid* / *Partially Paid*
- [ ] Emit **Control Tower** event (`finance.payment.synced`)
- [ ] Latency target (sandbox): updates visible in ≤ 15 min

**Deliverable:** Contractors see **live payment updates** in the Portal; staff can audit status in ERP/CT.

---

## 6) Reconciliation
- [ ] Build reconciliation jobs (Python Pandas or Node) to compare **ERP invoices** vs **Accounts payments**
- [ ] **Exception queue** for mismatches (amount/date/customer)
- [ ] Reports:
  - **Weekly aging** (30/60/90) and **Monthly** summary
  - Export CSV/Excel/PDF for staff review; archive to Drive
- [ ] Emit **Control Tower** report events; optional Slack/email digest to finance

**Deliverable:** Automated reconciliation outputs with clear **exception handling**.

---

## 7) Security & Compliance
- [ ] **Secrets**: env vars + provider secret stores; rotate regularly
- [ ] **PII**: minimize; redact logs; no PII in error messages
- [ ] **Audit**: structured logs for all outbound/inbound calls (requestId, invoiceId, result)
- [ ] **Access**: least privilege API keys; scoped OAuth; IP allowlists if available
- [ ] **Retention**: logs N=180 days, reports N=365 days (archive thereafter)
- [ ] **GDPR**: consent + data subject rights respected for any personal data

**Deliverable:** Documented security model; periodic review checklist.

---

## 8) Observability & Control Tower Hooks
- [ ] Emit CT events with **runId**, **status**, **duration**, **counts**
- [ ] **Dashboards**: exports per day, failures, payment sync latency
- [ ] **Alerts**: export failure, webhook errors, reconciliation exceptions > threshold
- [ ] **Daily digest**: summary to ops/finance channels

**Deliverable:** Operations can **see, alert, and summarise** finance health centrally.

---

## 9) CI/CD & Deployment
- [ ] GitHub Actions:
  - Lint + unit tests
  - **Sandbox integration tests** (mock provider if no sandbox)
  - Build/package & deploy (Cloud Functions / container)
- [ ] Promotion: sandbox → staging → production with approvals
- [ ] Rollback: last known good artifact; config‑driven endpoints

**Deliverable:** Automated, repeatable deploys with environment promotion gates.

---

## 10) Milestones
**Phase 1 — Init**
- Repo created; provider selected; sandbox connectivity proven

**Phase 2 — Invoicing**
- Export pipeline live; ERP ↔ accounts IDs persisted

**Phase 3 — Payments**
- Payments webhook/polling updates statuses in ERP/Portal

**Phase 4 — Reconciliation**
- Scheduled reports with exception queue + exports

**Phase 5 — CI/CD**
- Tests + automated pipeline for build/deploy & promotion

---

## 11) Acceptance Criteria (MVP)
- [ ] A known **approved invoice** reaches the accounts system with correct VAT/lines
- [ ] Accounting ID stored back on the ERP invoice; duplicate exports avoided (idempotency)
- [ ] **Payment** on that invoice reflects back to *Paid* in ERP/Portal
- [ ] Reconciliation job produces a **weekly aging** report and flags exceptions
- [ ] CI runs unit + sandbox integration tests; deploys to **staging** on merge
- [ ] Security review checklist completed (secrets, PII, logs)

---

## 12) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| API rate limits / pagination | M | M | Backoff + cursors; nightly full sync job |
| Schema drift in provider | M | M | Contract tests; tight version pinning |
| Webhook reliability | M | H | Retries + dead‑letter; fallback polling |
| VAT/rounding discrepancies | L | M | Shared helper; unit tests for totals |
| Timezone/date mishaps | M | M | All times ISO UTC; display TZ in Portal |
| PII in logs | L | H | Redaction middleware; log reviews |
| Credential leakage | L | H | Store in Secrets; rotate; least privilege |

---

## 13) Related Documents
- [Work Order Master](../work_order_master.md)  
- [Phase Plans Index](../plans/phase_plans_index.md)  
- [Firebase Backend Work Order](work_order_firebase_backend.md)  
- [Contractor Portal Work Order](work_order_contractor_portal.md)  
- [Control Tower Work Order](work_order_control_tower.md)  
- [Vision Docs Index](../design/vision_index.md)

---

> Notes: This expands your original Finance Integration WO (setup, provider selection, invoicing, payments, reconciliation, security, CI/CD, milestones) into an **execution‑ready** plan with field mappings, idempotency, CT hooks, and acceptance criteria.
---

### 📏 Canonical Data Rules (Swan)
- Use **snake_case** field names; FKs end with **`_id`**.
- Money uses `{ "amount_minor": int, "currency": "GBP" }` (no floats).
- Dates = `*_date` (date) and `*_at` (datetime, ISO-8601).
- Import common types from **[`docs/schemas/common/common.json`](../schemas/common/common.json)**.
- Follow **PII redaction** policy in **[`docs/schemas/PII_POLICY.md`](../schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`docs/design/field_lineage.md`](../design/field_lineage.md)**.
