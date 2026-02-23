# 📝 Work Order: Swan Recruitment – Firebase Backend (swan-firebase-backend)
**Backlinks:** [Master WO (Full)](work_order_master__FULL.md) · [Work Orders Index](work_orders_index.md)

**Last updated:** 2025-09-26

## 🎯 Objective
Build and maintain the **Firebase Backend** that powers Swan’s ERP: onboarding, contract generation, portal sync, exports for finance, and orchestration hooks for the **Control Tower**.

**Non‑goals (MVP):**
- Full finance BI (handled later via Reporting/CT layers)
- Owning long‑term system-of-record data (CT/ERP handle visibility; finance owns accounting SoR)

---

## 🔑 Status Keys
- 🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred

**Status:** 🟡 Drafted

---

## 1) Project & Environments Setup
- [ ] Repo: `swan-firebase-backend`
- [ ] Firebase project created/linked to Swan account; billing enabled if needed
- [ ] Environments: `dev`, `staging`, `prod`
- [ ] Tooling installed (Windows‑first):
  - [ ] Firebase CLI  
        ```powershell
        npm install -g firebase-tools
        firebase login
        ```
  - [ ] Node 18+
  - [ ] PowerShell scripts in `/tools` (optional)

- [ ] Initialize Firebase in repo  
  ```powershell
  firebase init
  ```

- [ ] Baseline files
  - [ ] `firebase.json`, `.firebaserc`
  - [ ] `/functions/` (TypeScript/JS), `/firestore.rules`, `/storage.rules`
  - [ ] `.github/workflows/deploy.yml` (CI)

---

## 2) Data Model & Security
### 2.1 Firestore Collections (MVP)
- `contracts` — contract docs metadata (contractorId, client, status, file refs, issuedAt)
- `contractors` — profile, auth linkage, status
- `timesheets` — period, hours, approvals, file refs
- `invoices` — invoiceNo, period, amounts, client, export status
- `users` — staff/admin metadata, role claims cache (mirrors Auth claims)

### 2.2 Realtime DB Nodes (for live UI)
- `/timesheetStatus/{contractorId}`
- `/invoiceStatus/{contractorId}`

### 2.3 Security Rules
- [ ] Firestore: least‑privilege rules; staff vs contractor paths
- [ ] RTDB: contractor can read/write only self status nodes
- [ ] Storage: per‑folder ACL (e.g., `/contracts/`, `/timesheets/`, `/invoices/`)

Deliverable: **Schema + initial rules** committed.

---

## 3) Cloud Functions (MVP)
### 3.1 Webhooks & Orchestration
- [ ] **CATSone “Candidate Placed” webhook** → parse payload → enqueue New Starter flow
- [ ] **New Starter Flow steps:**
  - [ ] Parse contractor/client/contract terms
  - [ ] **Generate contract Word docs**
  - [ ] Upload docs to CATSone (link on contractor record)
  - [ ] Generate **starter CSV**
  - [ ] Upload CSV to **Google Drive** (for timesheet Excel process)
  - [ ] Emit events to Control Tower (runId, status, timings)

### 3.2 Timesheets & Invoices
- [ ] Handle **timesheet/invoice uploads** from Contractor Portal
- [ ] Validate & persist to Firestore + Storage
- [ ] Update RTDB status nodes
- [ ] Emit CT events

### 3.3 Utilities
- [ ] **Document naming** conventions applied everywhere
- [ ] **Audit logging** on every function with correlationId
- [ ] Health endpoint(s) for CT

Run locally via Emulators; deploy functions when ready:
```powershell
firebase deploy --only functions
```

Deliverable: **First function set** deployed and verified in `dev`.

---

## 4) Authentication & Authorization
- [ ] Enable Firebase Auth (email/password; optional Google SSO)
- [ ] Roles (claims):
  - **contractor** – portal access only
  - **staff** – internal tools (desktop app) & admin UIs
- [ ] Function to **attach role claims** post‑onboarding
- [ ] Rule tests verifying access boundaries

Deliverable: **Secure login + role claims** integrated.

---

## 5) Integrations
- [ ] **CATSone** — webhook receiver; document upload; contractor record linkage
- [ ] **Google Drive** — CSV/contract archives, folder standards
- [ ] **Contractor Portal** — upload webhooks; status feeds
- [ ] **Control Tower (CT)** — health checks; run events; job result metadata
- [ ] **Desktop Manager** — secure API for manual triggers

Deliverable: **Integration map** documented; endpoints stabilized.

---

## 6) Observability & Audit
- [ ] Structured logs with correlationId (requestId/runId)
- [ ] Persist **Run** and **Event** documents for 90 days (extendable)
- [ ] Basic KPI counters (e.g., starter flow durations, failure rates)
- [ ] CT notifications for failures / digest summaries (Phase 2)

Deliverable: **Queryable audit trail** + minimal KPIs.

---

## 7) CI/CD (GitHub Actions)
- [ ] Pipeline in `.github/workflows/deploy.yml`:
  - Lint & unit tests
  - **Emulator Suite tests** (Firestore/RTDB/Functions/Auth)
  - Guard rails (no secrets in logs)
  - Deploy to `dev` on PR merge; manual promotion to `staging`/`prod`

Deliverable: **Automated deploy** with emulator coverage.

---

## 8) Milestones
**Phase 1 — Project Init**
- Firebase project created; CLI + Emulators configured

**Phase 2 — Schema & Rules**
- Firestore/RTDB structure defined; base rules applied

**Phase 3 — Functions**
- Webhook + contract generator; status sync functions live

**Phase 4 — Auth**
- Auth enabled; role claims logic implemented

**Phase 5 — CI/CD**
- Actions pipeline running; gated deploys

*(Further phases: Pub/Sub/Eventarc, batch processing, GraphQL, banking/finance API bridges)*

---

## 9) Acceptance Criteria (MVP)
- [ ] New Starter flow runs end‑to‑end, producing docs + CSV and Drive upload
- [ ] Contractor uploads (timesheet/invoice) land with correct ACLs + statuses
- [ ] Auth roles enforced in rules & tested
- [ ] CT can read health + receives run events
- [ ] CI runs emulator tests and deploys safely

---

## 10) Risks & Mitigations (excerpt)
| Risk | Likelihood | Impact | Mitigation |
|---|:--:|:--:|---|
| Webhook payload variance | M | M | JSON schemas + strict parsing + tests |
| Secrets leakage in logs | L | H | Redaction middleware; CI checks |
| Rule misconfig → data exposure | L | H | Rule tests + staged rollouts |
| Over‑reliance on sync ops | M | M | Queueing/async (Eventarc/Pub/Sub) in Phase 2 |

---

## 11) Related Documents
- [Work Order Master](work_order_master.md)
- [Phase Plans Index](../plans/phase_plans_index.md) — Phase 3 (Backend Core)
- [Control Tower Work Order](work_order_control_tower.md)
- [Control Tower Vision](../design/control_tower_vision.md)
- [Vision Docs Index](../design/vision_index.md)
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
- Follow **PII redaction** policy in **[`docs/schemas/PII_POLICY.md`](../schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`docs/design/field_lineage.md`](../design/field_lineage.md)**.