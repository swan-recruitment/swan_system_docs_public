# 🗂️ Tasks Backlog

**Created:** 2025-09-26

## Open Tasks
- [ ] Add **Makefile** targets for Phase Plans tooling (`phase-merge`, `phase-validate`) — 2025-09-26


## Backlog Additions (Control Tower Next Tweaks)

### 1. Spectral Lint for OpenAPI
- **Goal**: Prevent drift between the Control Tower API spec and implementation.
- **Tasks**:
  - Add `.spectral.yaml` ruleset with base rules (info/license, tags, operationId, response schemas).
  - GitHub Action job: `spectral lint docs/design/openapi/control_tower.yaml` on every PR.
  - Ensure CI blocks merge if lint fails.

### 2. CT UI Scaffold Checklist
- **Goal**: Provide a minimal UI for CT to visualise health and events.
- **Tasks**:
  - React/Vite skeleton consuming `/systems`, `/events`, `/runs` endpoints.
  - Render **Executive Status cards** with G/A/R and last heartbeat.
  - Render **Events table** (paginated).
  - Leave CSS minimal; goal is wireframe-level MVP.

### 3. Replay Tool for DLQ Items
- **Goal**: Recover safely from transient failures in event ingestion.
- **Tasks**:
  - CLI or Python script to list DLQ items from Firestore/Storage.
  - Replay item into `/events` with a new `eventId`.
  - Restrict to safe event types (configurable allowlist).
  - Audit replay actions into `runs` for traceability.


### 2025-09-27 — Documentation Maintenance Tasks
1. **Add Backlinks to all WOs**  
   - Add a “Backlinks” line at the top of every Work Order pointing to:  
     - Master WO (Full) and Work Orders Index.  
   - Files: all items in `docs/work_orders/`.
2. **Auto-update Index Timestamps**  
   - Script to refresh “Last Updated” for each WO in `work_orders_index.md` based on file mtime.  
   - Integrate as a CI pre-commit or PR check.
3. **CI Rule: Enforce Canonical Data Block**  
   - Lint that each WO contains the “📏 Canonical Data Rules (Swan)” section.  
   - Fail PR if missing.


## 2025-09-27 — Programme Backlog (Prioritised)

> Source: “Top 10 next moves” + gold-standard checklist. Use these to track progress. Create a PR per item using the existing templates.

### P1 — Immediate
- [ ] **Event Schemas (machine-checkable)** — Add JSON Schemas for core events under `docs/schemas/events/` + validator + CI.  
      Files: `docs/schemas/events/*.schema.json`, `scripts/validate_events.(js|py)`  
      Owners: _TBD_ · Links: [Event Taxonomy](../design/event_taxonomy.md)
- [ ] **Phase 1 Plan (real content)** — Objectives, milestones, owners, entry/exit criteria, dependencies, acceptance tests.  
      Files: `../plans/phase_1_plan.md` · Owners: _TBD_
- [ ] **Finance Mapping (field-by-field)** — Swan↔Finance map, `invoice_number` contract, reconciliation examples, error taxonomy.  
      Files: `../design/finance_mapping.md` · Owners: _TBD_

### P2 — Near-term
- [ ] **CT Dashboards Spec** — Widgets, KPIs/SLOs, thresholds, queries, alert routing.  
      Files: `../design/ct_dashboards.md` · Owners: _TBD_ · Links: [ct_quality_jobs.md](ct_quality_jobs.md)
- [ ] **Portal Intake Hardening** — Validation Matrix + anti-dup rules + examples.  
      Files: `../work_orders/work_order_contractor_portal.md`, `../examples/portal/` · Owners: _TBD_
- [ ] **Migration Runbook (Excel→Firebase)** — Batch adapters, alias enforcement, dry-run/verify/commit, rollback, QA checklist.  
      Files: `../work_orders/work_order_excel_migration.md` · Owners: _TBD_

### P3 — Soon
- [ ] **Desktop Manager — POC Plan** — Choose Tauri, module boundaries, packaging, update channels; map to spike scripts.  
      Files: `../work_orders/work_order_desktop_manager.md`, `../../spikes/desktop_manager/` · Owners: _TBD_
- [ ] **CT Quality Jobs Runbook** — Cron schedules, storage, dashboard placements, alerts, DLQ replay procedure.  
      Files: `ct_quality_jobs.md` · Owners: _TBD_

### P4 — Later
- [ ] **Website WO Deepening** — IA/sitemap, content model, SEO/perf budget, a11y checklist, CDN/hosting.  
      Files: `../work_orders/work_order_website.md` · Owners: _TBD_
- [ ] **Repo Ops Polish** — Branch protection, CODEOWNERS update, CONTRIBUTING.md.  
      Files: `/CODEOWNERS`, `../../CONTRIBUTING.md` · Owners: _TBD_

---

### Gold-Standard Hygiene (cross-cutting)
- [ ] **CONTRIBUTING.md** — naming, event/version rules, preview, CI checks.  
- [ ] **GLOSSARY.md** — invoice vs contractor invoice, reconciliation, pack, run, pointer.  
- [ ] **ADRs** — `docs/design/ADR/0001-…md` for important decisions.

