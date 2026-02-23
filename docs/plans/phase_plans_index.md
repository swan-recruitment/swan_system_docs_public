# 📅 Phase Plans Index — Detailed (Swan Recruitment ERP)

This expanded index adds **objectives, dependencies, entry/exit criteria, risks/mitigations, KPIs, and linked visuals/specs** for each phase.  
Use it as the single pane of glass for planning + delivery tracking.

> Status keys: 🟡 Drafted · 🟦 In Progress · ✅ Approved · ⏸ Deferred

---

## Phase 1–2: Foundations + Backend Core
**Files:** `phase_1_2_plan.md`  
**Linked visuals:** `swan_erp_flow_diagram.md`, `swan_erp_erd.md`  
**Key work orders:** `work_order_master.md`, `work_order_github_setup.md`, `work_order_firebase_backend.md`  
**Critical design specs:** DB Schema (`docs/design/db_schema.md`), Auth Roles (`docs/design/auth_roles_claims.md`), Contract Generator (`docs/design/contract_generator.md`), Status Sync (`docs/design/status_sync.md`)

**Objective**  
Stand up the org/repo infrastructure and deliver a secure Firebase backend (Firestore + Realtime DB + Functions + Auth) as the project hub.

**Dependencies**  
None (first phase).

**Entry criteria**  
– Org created; repos initialized; planning docs in place.  
– Service accounts available for Firebase.

**Exit criteria (Definition of Done)**  
– Firestore/Realtime schemas created with baseline **security rules**.  
– **Emulator Suite** tests for Functions pass.  
– Contract Generator webhook flow verified end‑to‑end with sample payloads.  
– CI/CD deploys Functions on `main` merges.

**Risks & mitigations**  
– *Auth complexity*: start with least‑privilege rules + unit tests.  
– *Webhook payload drift*: enforce JSON schema validation; contract tests.  
– *Data model churn*: lock ERD v1 and change via PR only.

**KPIs / Acceptance tests**  
– 100% passing emulator tests; ≥1 staging deploy.  
– Contract document generated within < 5s of webhook.  
– Unauthorized reads/writes blocked by rules tests.

---

## Phase 3: Desktop App + Excel Migration
**Files:** `phase_3_plan.md`  
**Linked visuals:** `swan_erp_flow_diagram.md`  
**Key work orders:** `work_order_desktop_app.md`, `work_order_excel_migration.md`  
**Critical design specs:** Timesheet Entry, Invoice Entry, Invoice Generation, Reporting

**Objective**  
Build **swan‑desktop‑manager** and replace legacy Excel/VBA workflows with Python modules integrated to Firebase.

**Dependencies**  
Phase 1–2 schemas, rules, and Functions in place.

**Entry criteria**  
– Firebase Admin access + emulator config.  
– VBA macros exported and mapped.

**Exit criteria (Definition of Done)**  
– Timesheet & Invoice entry live in app; data stored in Firestore.  
– Invoice generation to PDF/Excel validated against legacy outputs.  
– Installer (.exe) built; user guide published.

**Risks & mitigations**  
– *GUI complexity*: prioritize core flows; defer polish.  
– *Parity gaps with Excel*: side‑by‑side tests; golden datasets.

**KPIs / Acceptance tests**  
– ≥95% parity vs legacy outputs; zero critical defects in UAT.  
– Staff complete a full week’s processing using the app only.

---

## Phase 4: Contractor Portal + Website
**Files:** `phase_4_plan.md`  
**Linked visuals:** `swan_erp_flow_diagram.md`  
**Key work orders:** `work_order_contractor_portal.md`, `work_order_website.md`  
**Critical design specs:** Portal Uploads, Status Dashboard, Auth UI, Hosting, SEO

**Objective**  
Deliver portal uploads (timesheets, invoices, expenses) with real‑time status and a branded public website with portal entry.

**Dependencies**  
Phase 2 rules + Realtime sync online.

**Entry criteria**  
– Auth roles/claims enforced; Storage rules drafted.  
– Status nodes present in Realtime DB.

**Exit criteria (Definition of Done)**  
– Uploads to Storage + metadata in Firestore; statuses update in real time.  
– Website live with contact form via Cloud Function; GA4 active.  
– CI/CD to Hosting for portal & website (staging + prod).

**Risks & mitigations**  
– *PII & file security*: strict Storage/Firestore rules; client‑side size/type checks.  
– *Contractor adoption*: clear UX, upload receipts, help content.

**KPIs / Acceptance tests**  
– 100% of test contractors can register, upload, and see status within 10s.  
– Core Web Vitals at least “Good” on homepage.

---

## Phase 5: Finance Integration (Accounting API + Reconciliation)
**Files:** `phase_5_plan.md`  
**Linked visuals:** `swan_erp_module_map.md`  
**Key work orders:** `work_order_finance_integration.md`  
**Critical design specs:** Invoice Automation, Payment Status Sync, Reconciliation Engine

**Objective**  
Automate client invoicing and payment sync with the accounting platform; provide reconciliation reports.

**Dependencies**  
Approved invoice records from Desktop App; stable Firestore schema.

**Entry criteria**  
– Sandbox account + API keys (least‑privilege).  
– Sample client invoice mappings defined.

**Exit criteria (Definition of Done)**  
– Client invoices created via API; IDs stored back in Firestore.  
– Payment statuses synced into Realtime DB for portal.  
– Reconciliation report generated and exported (CSV/Excel/PDF).

**Risks & mitigations**  
– *API rate/quotas*: queued jobs + exponential backoff.  
– *Rounding/tax logic*: unit tests per client; config tables.

**KPIs / Acceptance tests**  
– 100% of approved invoices exported within < 15 min SLA.  
– Reconciliation variance = £0 on golden dataset.

---

## Phase 6: Excel Migration Cutover & Final Testing
**Files:** `phase_6_plan.md`  
**Linked visuals:** `swan_erp_flow_diagram.md`  
**Key work orders:** `work_order_excel_migration.md` (+ Testing/Validation WO if split)  
**Critical design specs:** Final Test Suite, Cutover Plan, Archival Strategy

**Objective**  
Retire Excel/VBA with a controlled cutover and comprehensive validation/UAT.

**Dependencies**  
Phases 3–5 features stable.

**Entry criteria**  
– Historical data export plan approved.  
– UAT sign‑off criteria defined.

**Exit criteria (Definition of Done)**  
– Parallel run 2–4 weeks complete; variances addressed.  
– Excel entry frozen; archival completed and documented.  
– First live billing cycle completed end‑to‑end on new stack.

**Risks & mitigations**  
– *Edge‑case discrepancies*: defect triage with rollback playbook.  
– *Change management*: training sessions; quick‑ref guides.

**KPIs / Acceptance tests**  
– Zero P1 defects during first live cycle.  
– Staff satisfaction ≥ 8/10 in post‑cutover survey.

---

## Phase 7: Control Tower (Monitoring + Orchestration)
**Files:** `phase_7_plan.md`  
**Linked visuals:** `swan_erp_module_map.md`  
**Key work orders:** `work_order_control_tower.md`  
**Critical design specs:** Health Monitor, Manual Triggers API, Alerts/Notifications, Version Dashboard

**Objective**  
Centralize observability and control of workflows, versions, and alerts.

**Dependencies**  
Earlier phases deployed; metrics/logs accessible.

**Entry criteria**  
– Slack/email endpoints ready; service accounts scoped.  
– Health checks defined per component.

**Exit criteria (Definition of Do ne)**  
– Live dashboard of components (Functions, Hosting, Portal, Desktop heartbeat).  
– Manual triggers secured with RBAC + audit logs.  
– Alerts firing with runbooks linked.

**Risks & mitigations**  
– *Signal noise*: alert tuning thresholds; dedup rules.  
– *Access risk*: enforce least‑privilege and approval gates.

**KPIs / Acceptance tests**  
– MTTR < 30 min for simulated failures.  
– < 5% false‑positive alert rate over a month.

---

## Phase 8: Final Rollout & Continuous Improvement
**Files:** `phase_8_plan.md`  
**Linked visuals:** (Optional) Deployment Diagram  
**Key work orders:** Rollout & Onboarding, Continuous Improvement  
**Critical design specs:** Training & Onboarding, Feedback Loop, Continuous Deployment

**Objective**  
Onboard all users, institutionalize CI/CD + feedback loops, and operate the system.

**Dependencies**  
All prior phases live.

**Entry criteria**  
– Training materials ready; support rota set.  
– Issue labels/triage workflow in GitHub Projects.

**Exit criteria (Definition of Done)**  
– All staff/contractors onboarded; legacy fully retired.  
– Quarterly review cadence and backlog grooming established.  
– CI/CD green across repos for 30 consecutive days.

**Risks & mitigations**  
– *Adoption lag*: targeted coaching; office hours.  
– *Backlog sprawl*: strict triage SLAs; owner per epic.

**KPIs / Acceptance tests**  
– 90% of portal submissions processed within SLA.  
– NPS ≥ 8/10 from staff after two months.

---

## Maintenance
– Keep this index updated per phase via PR.  
– Only change ERD/rules via reviewed PRs.  
– Link all new/updated visuals and specs as they ship.
