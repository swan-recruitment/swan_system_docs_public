# 📝 Work Order: Swan Recruitment – Contractor Portal (swan-contractor-portal)
**Backlinks:** [Master WO (Full)](work_order_master__FULL.md) · [Work Orders Index](work_orders_index.md)

**Last updated:** 2025-09-27  

## 🎯 Objective
Deliver a secure, user‑friendly **Contractor Portal** where contractors can log in, upload timesheets and invoices, and track the status of their submissions.  
This is the **primary interface** for contractors within the Swan system.

**Non‑goals (MVP):**
- Payment reconciliation logic (handled in Finance/Reconciliation modules)
- Full contractor CRM (handled in ERP / Control Tower)

---

## 🔑 Status Keys
🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred  

**Status:** 🟡 Drafted

---

## 1) Project & Environments Setup
- [ ] Repo: `swan-contractor-portal`
- [ ] Framework: **Vite + React + Tailwind**
- [ ] Environments: `dev`, `staging`, `prod`
- [ ] Firebase Hosting setup (multi‑channel: preview, staging, production)
- [ ] Config management (environment variables, secrets)

Deliverable: **Baseline portal running on dev URL.**

---

## 2) Authentication & Authorization
- [ ] Firebase Auth integration (email/password, optional Google login)
- [ ] Claims model:
  - `contractor` — restricted access to own timesheets/invoices
  - `staff` — internal view for support/admin
- [ ] Emulator testing for Auth flows
- [ ] Logout, password reset, account recovery flows

Deliverable: **Secure login with role enforcement.**

---

## 3) Upload Workflows
- [ ] **Timesheet upload**
  - File types: `.xlsx`, `.csv`, `.pdf`
  - Stored in Firebase Storage under `/timesheets/{contractorId}/{period}/`
  - Metadata in Firestore (`timesheets` collection)
- [ ] **Invoice upload**
  - File types: `.pdf`
  - Stored in `/invoices/{contractorId}/{invoiceNo}/`
  - Metadata in Firestore (`invoices` collection)
- [ ] **Expense upload (Phase 2+)**
- [ ] Standard naming conventions applied
- [ ] Error handling for invalid formats or size limits

Deliverable: **Contractor uploads land in storage + metadata DB.**

---

## 4) Status Dashboard
- [ ] Contractor can see submission statuses:
  - `Submitted` → `Accepted` → `Processed` → `Paid`
- [ ] Backed by Realtime Database nodes:
  - `/timesheetStatus/{contractorId}`
  - `/invoiceStatus/{contractorId}`
- [ ] Live updates (onSnapshot / onValue subscriptions)
- [ ] Error indicators if sync fails

Deliverable: **Live status panel visible in portal.**

---

## 5) Data Binding & Security Rules
### Firestore Schema
- `contractors` — profile, linked auth uid
- `contracts` — metadata only (read‑only to contractor)
- `timesheets` — contractor uploads, metadata, status
- `invoices` — invoice metadata, link to client/contract

### Security
- Contractor: R/W self timesheets + invoices only
- Staff: read/write broader scope for support
- Storage rules aligned with Firestore ACLs

Deliverable: **Rules deployed + emulator tests passing.**

---

## 6) UI/UX
- [ ] Responsive design (desktop + mobile)
- [ ] Clear navigation: Dashboard · Uploads · History · Account
- [ ] Accessibility: WCAG AA compliance
- [ ] Error banners & retry for failed uploads
- [ ] Branding with Swan Recruitment identity

Deliverable: **Functional MVP UI with branding + accessibility.**

---

## 7) Testing
- [ ] **Unit tests** (Jest) for components
- [ ] **Integration tests** with Firebase Emulator Suite
- [ ] **E2E tests** (Cypress/Playwright) for login + upload + status flow
- [ ] Edge cases: large files, invalid types, offline mode

Deliverable: **CI tests running green.**

---

## 8) Deployment & CI/CD
- [ ] GitHub Actions workflow:
  - Lint + unit tests
  - Build portal
  - Deploy to Firebase Hosting (preview on PR, staging on merge, prod on tag)
- [ ] Version tagging for portal releases

Deliverable: **Automated deployments + preview URLs.**

---

## 9) Observability & Audit
- [ ] Client‑side error logging (Sentry or Firebase Crashlytics)
- [ ] Upload failures logged to Firestore `uploadErrors`
- [ ] Emit **Control Tower events**: contractor upload received, errors, retries
- [ ] Metrics: average upload size, failures, retries

Deliverable: **Audit trail + metrics for CT + ops.**

---

## 10) Milestones
**Phase 1 — Init**  
- Repo scaffolded, Firebase Hosting live (Hello World)  

**Phase 2 — Auth & Uploads**  
- Login live; timesheet + invoice uploads functional  

**Phase 3 — Status Dashboard**  
- Real‑time updates wired; contractor can track submissions  

**Phase 4 — Security & UX Polish**  
- Rules hardened; UI branded; accessibility compliance  

**Phase 5 — CI/CD + Observability**  
- Automated deploy; error logging; CT events integrated  

*(Phase 6+: Expenses, contractor profile updates, richer dashboards)*

---

## 11) Acceptance Criteria (MVP)
- [ ] Contractor can log in and securely upload timesheet + invoice
- [ ] Files stored with correct naming + ACLs
- [ ] Status dashboard reflects backend updates in real time
- [ ] Staff can support via role override
- [ ] CI pipeline builds + deploys portal to staging/prod

---

## 12) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Upload of malicious files | M | H | File type/size validation; AV scan option |
| Storage cost growth | M | M | Lifecycle rules; archive policies |
| Contractor confusion on errors | H | M | UX: clear banners + retry |
| Rule misconfig → data leak | L | H | Rule tests + staging rollout |

---

## 13) Related Documents
- [Work Order Master](work_order_master.md)  
- [Phase Plans Index](../plans/phase_plans_index.md) — Phase 2 (Portal Core)  
- [Firebase Backend Work Order](work_order_firebase_backend.md)  
- [Control Tower Work Order](work_order_control_tower.md)  
- [Vision Docs Index](../design/vision_index.md)

---
---
---

## This Work Order Emits / Consumes (Event Taxonomy)
See [Event Taxonomy](../design/event_taxonomy.md) for full definitions and payload rules (IDs only, pointers not bytes, Money in minor units, ISO timestamps, **no PII**).

**Emits (Portal):**
- `portal.uploaded` — file/form received (metadata only).
- `portal.validated` — schema & format checks passed.
- `artifact.pointer.written` — when Portal writes a Drive pointer via Backend.
- `backend.fn.error` — surfaced by Backend for Portal-originated failures (with `correlation_id`).

**Consumes (Portal):**
- `ct.run.started` / `ct.run.completed` — optional UX progress if Portal displays status.
- `finance.payment.reconciled` — optional state reflection in contractor view (read-only).

**Notes:**
- Do not include PII in any event payloads; pass PII via secure Firestore documents only.


### 📏 Canonical Data Rules (Swan)
- Use **snake_case** field names; FKs end with **`_id`**.
- Money uses `{ "amount_minor": int, "currency": "GBP" }` (no floats).
- Dates = `*_date` (date) and `*_at` (datetime, ISO-8601).
- Import common types from **[`docs/schemas/common/common.json`](../schemas/common/common.json)**.
- Follow **PII redaction** policy in **[`docs/schemas/PII_POLICY.md`](../docs/schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`docs/design/field_lineage.md`](../docs/design/field_lineage.md)**.

---

## Appendix A — Detailed Design & Flows (Contractor Portal)

**Last updated:** 2025-09-27

### A1. Forms & Uploads
- **Timesheet form**: week picker, daily hours, project/client selector (filtered by contractor_id), file attach (PDF).
- **Contractor invoice upload**: file dropzone (PDF), metadata (period start/end), optional notes.
- **Validation**: client-side (schema, file type/size); server-side (canonical names, alias map normalization).

### A2. Intake Pipeline
1. **Client-side validation** → block obvious issues, show actionable errors.
2. **POST /ingest** (Backend) → returns `upload_id`, `correlation_id`.
3. **Write pointer** to Drive (Backend) → emit `artifact.pointer.written` (IDs only).
4. **Create/patch** Firestore doc (timesheet/invoice) with pointer & metadata.
5. **Emit events**: `portal.uploaded` → `portal.validated` → `backend.parsed`.

### A3. Security & PII
- Do not include PII in events or query params.
- Files go to Drive; only **Drive URL + checksum** in Firestore + events.
- Rate limiting + reCAPTCHA (invisible) on public endpoints.

### A4. Error Handling
- 4xx: schema/format → UX shows field-level errors.
- 5xx/transient: retry with backoff; retain in local queue for 15 min.
- Emit `backend.fn.error` with `correlation_id` (no PII).

### A5. Acceptance Criteria
- [ ] Upload of valid timesheet produces Firestore doc + Drive pointer in < 5s.
- [ ] Invalid schema gets field-level errors; no Firestore write occurs.
- [ ] Events chain present (uploaded, validated, parsed) with matching `correlation_id`.
- [ ] Accessibility: keyboard-nav, labels, error role announcements.
