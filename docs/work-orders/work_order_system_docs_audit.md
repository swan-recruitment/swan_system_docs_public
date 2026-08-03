# 🧭 Work Order – System Docs Audit

**Backlinks:** [Work Orders Index](work_orders_index.md) · [Work Order Master](../work_order_master.md)  
**Last updated:** 2025-09-28  

---

## 1) Objective
Audit the `swan_system_docs` repository to ensure **completeness, consistency, and readiness** as the single source of truth (SSOT) for Swan ERP documentation.  

---

## 📑 Sections
1. Objective  
2. Scope & Success Criteria  
3. Folder Audits  
4. Risks & Mitigations  
5. Acceptance Criteria  
6. Priority Guide  
7. Governance Rules Audit  



## 2) Scope & Success Criteria
- Cover all folders and files under `/docs/`.  
- Identify **current role**, **findings**, and **needs & next steps**.  
- Produce actionable **checklists** for each section.  

**Definition of Done:**  
- All folders reviewed.  
- Checklists exist for every section.  
- Gaps and placeholders logged.  

---

## 3) Folder Audits

### 3.1 `_agentchat_`
**Current Role:** Proto experiments, audit/level_one notes.  
**Needs & Next Steps:**  
- [ ] Confirm purpose of `_agentchat_/audit` vs `_agentchat_/level_one`.  
- [ ] Decide if to merge into `/audit/` or formalise as experimental.  

### 3.2 `_audit_`
**Current Role:** Content-level review material.  
**Needs & Next Steps:**  
- [ ] Clarify ownership: who maintains review?  
- [ ] Migrate findings into main audit WO.  

### 3.3 `_faq_`
**Current Role:** Quick-ref docs (data security, workflows, labels, CT explanation).  
**Needs & Next Steps:**  
- [ ] Review for duplication with `sop/`.  
- [ ] Ensure linked from `INDEX.md`.  
- [ ] Expand CT FAQ into Control Tower README.  

### 3.4 `control_tower/`
**Current Role:** Configs, schemas, dashboards, cheat sheets.  
**Needs & Next Steps:**  
- [ ] Expand README into index.  
- [ ] Link schemas to validators.  
- [ ] Flesh out dashboards spec.  
- [ ] Add runbooks & escalation SOPs.  
- [ ] Merge Best Practices SOPs.  


### 3.5 `design/`
**Current Role:** Vision docs, architecture, taxonomy, lineage, OpenAPI, design specs.

**Findings:**
- Strong backbone: vision, architecture, taxonomy, lineage all present.
- `design_specs_index.md` tracks subsystem design specs with status markers (🟡/🟦/✅/⏸️).
- Some specs listed but missing (contract generator, status sync, auth roles).
- OpenAPI spec may not yet be validated against WO API definitions.
- Cross-linking with Phase Plans is not consistent.

**Needs & Next Steps:**
- [ ] Cross-link `design_specs_index.md` with Phase Plans.
- [ ] Validate `openapi/control_tower.yaml` against Control Tower WO API section.
- [ ] Ensure `event_taxonomy.md` + `field_lineage.md` flow into schemas.
- [ ] Fill missing design specs (contract generator, status sync, auth roles).
- [ ] Add design spec for Finance Integration.
- [ ] Confirm `updates/chat_updates_summary.md` is reconciled with Control Tower glossary.



### 3.6 `diagrams/`
**Current Role:** Visual ERP flows, module maps, contract generator sequences, contractor onboarding lifecycle, governance, canonical data rules.

**Findings:**
- Well-structured: each major ERP view has its own subfolder with multiple formats (.mmd, .md, .html, .png).
- `visual_docs_index.md` provides governance with completion/status tracking.
- Some diagrams referenced in `index.md` (e.g., roadmap timeline) are missing here.
- Governance flow exists but not cross-linked.
- READMEs in diagram subfolders are inconsistent (some present, some missing).
- Contractor onboarding diagrams are scattered; no consolidated index.

**Needs & Next Steps:**
- [ ] Standardise subfolder READMEs (scope, source `.mmd`, outputs).
- [ ] Ensure all diagrams are listed in `visual_docs_index.md`.
- [ ] Add missing diagrams referenced in `index.md` (roadmap timeline, etc.).
- [ ] Cross-link `governance_flow.md` with Phase Plans + Control Tower docs.
- [ ] Consolidate contractor onboarding diagrams under a single index.
- [ ] Confirm MVP E2E flow contractor portal diagram is complete.


### 3.7 `labels/`
**Current Role:** GitHub labels config.  
**Needs & Next Steps:**  
- [ ] Ensure `labels.json` matches `.github/labels.json`.  
- [ ] Update with current workflow labels.  

### 3.8 `lifecycles/`
**Current Role:** Contractor lifecycle automation SOPs.  
**Needs & Next Steps:**  
- [ ] Validate `sop_ATS_to_payment` is complete.  
- [ ] Link lifecycle SOPs to workflow SOP family.  


### 3.9 `plans/`
**Current Role:** Phase 1–8 docs, workflow-specific plans, schema for validation.

**Findings:**
- Governance model is strong: index with objectives, dependencies, entry/exit criteria, KPIs, visuals, specs, and status markers.
- All 8 phases represented, plus extras (CT workflow, chatgpt_commands_v3_plan, cloud_functions_refactor_plan).
- Schema (`phase_index.schema.json`) exists, but validation status unknown.
- Plans are **outdated** in places — may not reflect current repo or architecture state.

**Needs & Next Steps:**
- [ ] Validate `schema/phase_index.schema.json` against all phase plans.
- [ ] Ensure each phase plan links to its Work Orders.
- [ ] Update status markers (🟡/🟦/✅/⏸) consistently.
- [ ] Merge `chatgpt_commands_v3_plan.md` + `cloud_functions_refactor_plan.md` into formal phase structure.
- [ ] Expand KPIs and risks for phases still in draft.
- [ ] Cross-link visuals (from diagrams) and specs (from design) systematically.
- [ ] **Conduct full audit of each phase plan’s content:**
  - Check if objectives, dependencies, KPIs, risks are still relevant.
  - Align with current repo structure and updated Work Orders.
  - Flag outdated assumptions (esp. Firebase, CI/CD, Finance integrations).
  - Recommend consolidation or retirement of obsolete plans.


### 3.10 `quickguides/`
**Current Role:** ChatGPT command cheat sheets.  
**Needs & Next Steps:**  
- [ ] Decide scope: dev-only, or system-wide inclusion.  
- [ ] Move under `/sop/operational/` if formalised.  

### 3.11 `schemas/`
**Current Role:** Shared schemas + PII policy.  
**Needs & Next Steps:**  
- [ ] Fill in `common/common.json`.  
- [ ] Flesh out `PII_POLICY.md` with concrete redaction rules.  
- [ ] Cross-link to canonical data rules.  


### 3.12 `scripts/`
**Current Role:** Governance automation — consistency checks, phase plan validation, daily digest generation.

**Findings:**
- Covers governance automation: `docs_guardian.py`, `validate_phase_index.py`, `merge_phase_plans.py`, `generate_daily_digest.py`.
- Well-aligned with repo governance model (plans, CT, docs consistency).
- Gaps:
  - No usage docs (when/how to run, dependencies).
  - No automated tests for correctness.
  - Dependencies (Python version, modules) undocumented.
  - Not yet integrated into CI.

**Needs & Next Steps:**
- [ ] Add usage docs (in `/sop/system/` or a new `/docs/scripts/README.md`).
- [ ] Ensure all scripts have unit tests or test cases.
- [ ] Document runtime dependencies (Python version, libraries).
- [ ] Integrate key scripts (`docs_guardian.py`, `validate_phase_index.py`) into CI workflows.
- [ ] Link `generate_daily_digest.py` to Control Tower WO acceptance criteria.



### 3.13 `security/`
**Current Role:** Compliance docs covering GDPR data retention and secrets management.

**Findings:**
- Contains `gdpr_retention.md` and `secrets_policy.md`.
- Provides foundation for data retention/deletion (GDPR) and secrets management.
- Gaps:
  - No explicit access control (RBAC) or audit logging coverage.
  - Not cross-referenced with SOP compliance family.
  - No linkage with Control Tower event logging or PII redaction policies.
  - Policies are static — not integrated into CI or monitoring.

**Needs & Next Steps:**
- [ ] Expand `secrets_policy.md` with rotation cadence, owner responsibilities, and tooling references.
- [ ] Add access control / RBAC policy (tie to Control Tower & API).
- [ ] Add audit logging & monitoring policy (link to Control Tower observability).
- [ ] Cross-reference GDPR/Secrets policies with SOP compliance family.
- [ ] Add section on incident response (tie into Emergency SOP family).
- [ ] Automate policy lint/checks (e.g., extend `docs_guardian.py` for compliance validation).


### 3.14 `sop/`
**Current Role:** Families: compliance, emergency, operational, system, workflow. Root-level SOPs also exist.

**Findings:**
- Very comprehensive structure: families, templates, instances, indexes.
- Contractor onboarding workflow SOPs are deeply detailed (data, risks, KPIs, exceptions, roles).
- Strong framework: systematic and extensible (families + templates).
- Gaps:
  - Many templates exist but instances are incomplete across families (compliance, emergency, operational, system).
  - `INSTANCE_INDEX.md` is empty or partial.
  - Some root-level SOPs (e.g., `docs_audit_process.md`, `docs_update_process.md`, `file_standards_sop.md`, `schema_lifecycle.md`, `mvp_stub_packaging.md`) are **orphans** — not placed in a family folder.
  - SOP-joborder linkage exists (`/tasks/sop_joborders/`) but needs reconciliation with actual instance progress.

**Needs & Next Steps:**
- [ ] Populate SOP instances for **compliance, emergency, operational, system** families.
- [ ] Complete `INSTANCE_INDEX.md` so all SOPs are discoverable.
- [ ] Link `docs_update_process.md` and `docs_audit_process.md` into SOP governance cycle.
- [ ] Integrate `mvp_stub_packaging.md` as either a SOP instance or reference doc.
- [ ] Reconcile SOP job orders (`/tasks/sop_joborders/`) with actual family progress.
- [ ] Ensure each workflow SOP (01–07) has complete instances (some are missing visuals/KPIs/exceptions).
- [ ] Standardise naming across templates and instances for easier automation.
- [ ] **Rehouse orphan SOPs** into correct families (system, operational, compliance, or new family if needed).
- [ ] For each orphan SOP, create a folder with `/templates/` and `/instances/` to match family structure.
- [ ] Update `INSTANCE_INDEX.md` and Phase Plans/Work Orders to cross-link these SOPs properly.



### 3.15 `tasks/`
**Current Role:** Documentation improvement tasks, SOP joborders, backlog, progress dashboards, JSON tracker.

**Findings:**
- Functions as a task/project tracker for documentation improvements.
- Includes SOP-specific joborders (`sop_joborders/`).
- `progress_dashboard.md` provides a lightweight status view.
- `tracker.json` suggests machine-readable task tracking (possibly automation).
- Backlog (`backlog.md`) contains technical improvements (phase plan tooling, CT API spec linting).
- Gaps:
  - Backlog may overlap with audit WO checklists (duplication risk).
  - No clear linkage between backlog tasks and phase plans/work orders.
  - SOP joborders don’t appear linked back to `INSTANCE_INDEX.md`.
  - Progress dashboard looks manual, not integrated with CI.

**Needs & Next Steps:**
- [ ] Reconcile backlog items with audit WO priorities (avoid duplication).
- [ ] Ensure all tasks map to Phase Plans or Work Orders.
- [ ] Link `sop_joborders/` to `INSTANCE_INDEX.md` in SOP.
- [ ] Automate `progress_dashboard.md` updates (e.g., GitHub Actions).
- [ ] Expand `tracker.json` into a schema-driven tracker for cross-repo tasks.
- [ ] Clarify whether `ct_quality_jobs.md` is a placeholder or actionable.



### 3.16 `templates/`
**Current Role:** Repository boilerplate templates (currently only README template).

**Findings:**
- Contains only `README_TEMPLATE.md`, useful for repo-level consistency.
- Strong starting point, references ERP system architecture.
- Gaps:
  - No templates for SOPs, Phase Plans, or Work Orders.
  - No CONTRIBUTING template (guides exist but not standardised here).
  - No visibility for `.github/` issue/PR templates within this folder.
  - No style guide for Markdown templates.

**Needs & Next Steps:**
- [ ] Extend template library: add SOP templates, Phase Plan templates, Work Order templates.
- [ ] Add CONTRIBUTING template to standardise contributor guides across repos.
- [ ] Ensure `.github/` issue/PR templates are linked from here for visibility.
- [ ] Create style guide for Markdown templates (headings, status markers, links).
- [ ] Ensure templates are referenced in SOP families (esp. system & operational).



### 3.17 `work-orders/`
**Current Role:** Subsystem work orders, project delivery plan, and index governance.

**Findings:**
- Strong structure: each subsystem (Portal, Control Tower, Desktop, Finance, Firebase, Website) has its own WO.
- `project_delivery_workorders_plan.md` provides orchestration at project-delivery level.
- `work_orders_index.md` includes governance metadata (review dates, owner, audit cycle).
- Gaps:
  - `work_order_system_docs_audit.md` must be reflected here (new addition).
  - Some subsystem WOs are strong (Control Tower) but others remain draft or incomplete (e.g., Excel migration, GitHub setup).
  - Not all WOs clearly link back to Phase Plans.
  - Status markers (🟡/🟦/✅/⏸) not consistently applied across WOs.
  - Duplication risk between `work_order_phase_plan_detail_integration.md` and Phase Plan index.

**Needs & Next Steps:**
- [ ] Add `work_order_system_docs_audit.md` into index (✅ ensure linkage is complete).
- [ ] Ensure all subsystem WOs link to relevant Phase Plans.
- [ ] Apply status markers (🟡/🟦/✅/⏸) across all WOs for clarity.
- [ ] Standardise WO headers (objective, scope, success criteria, risks).
- [ ] Consolidate duplication (phase detail vs phase index).
- [ ] Schedule WO reviews in sync with Phase Plans (use governance metadata).
- [ ] Expand weaker/draft WOs (e.g., Excel migration, GitHub setup).



### 3.18 `workflows/`
**Current Role:** End-to-end workflow documentation (currently contractor workflow).

**Findings:**
- `contractor_workflow.md` describes the full lifecycle: ATS (CATSone) → Contract Creation → Portal → Finance → Reporting.
- Provides a narrative view of Swan ERP’s contractor process.
- Complements workflow SOPs in `/docs/sop/workflow/`.
- Gaps:
  - Not cross-linked to workflow SOPs (01–07).
  - No references to diagrams in `/docs/diagrams/contractor-onboarding/`.
  - No backlinks to related Work Orders (Contractor Portal, Finance, Control Tower).
  - Lacks governance metadata (owner, review cycle, status markers).
  - Structure differs from other WO/SOP docs (missing objectives/scope/criteria).

**Needs & Next Steps:**
- [ ] Cross-link `contractor_workflow.md` with workflow SOPs (01–07).
- [ ] Reference diagrams in `/docs/diagrams/contractor-onboarding/`.
- [ ] Add backlinks to Work Orders (Contractor Portal, Finance, Control Tower).
- [ ] Add governance metadata (owner, last reviewed, next audit).
- [ ] Standardise structure: include objectives, scope, success criteria.
- [ ] Consider merging with SOP workflow family index for single source of truth.



### 3.19 Root Docs
**Current Role:** Repo-level governance and navigation docs.

**Findings:**
- `README.md` defines repo purpose (Swan SSOT).
- `INDEX.md` serves as a navigation hub.
- `CONTRIBUTING.md` sets contributor guidelines.
- `work_order_master.md` aggregates subsystem work orders.
- `commit_plan_master_sync.md` governs commit syncing.
- Strong foundation overall, with repo-level governance in place.
- Gaps:
  - README could link directly to Phase Plans, Design, SOPs.
  - INDEX may not be fully updated (needs refresh as repo expands).
  - CONTRIBUTING may not align with `.github/labels.json` and PR templates.
  - Master WO doesn’t yet reflect the new Audit WO.
  - Commit sync process not tied into CI.

**Needs & Next Steps:**
- [ ] Update README with quick links to Phase Plans, Design, SOPs.
- [ ] Refresh INDEX.md with all new folders (lifecycles, quickguides, audit, etc.).
- [ ] Ensure CONTRIBUTING.md matches `.github/labels.json` + PR templates.
- [ ] Add Audit WO (`work_order_system_docs_audit.md`) to Work Order Master.
- [ ] Link commit_plan_master_sync.md to automation (GitHub Actions).
- [ ] Add governance metadata (owner, review cycle) to README + INDEX.


---

---

## 4) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Docs drift across folders | M | H | Audit WO + phase review cadence |
| SOP families incomplete | H | M | Use joborders in `/docs/tasks` to drive completion |
| Placeholders left unfilled | M | M | Checklist sign-off before phase exit; docs_guardian.py checks |
| Duplication (FAQ vs SOP) | M | L | Merge under SOP families; retire duplicates |

---

## 5) Acceptance Criteria
- [ ] All folder audits completed & documented.  
- [ ] Gaps logged as checklists.  
- [ ] New WO committed to repo and linked from Master & Index.

---

## 6) Priority Guide (Audit 2025-09-28)

### 🚨 Immediate (High Value / High Risk if delayed)
1. **Control Tower Docs**
   - Expand README into index (link config, schemas, dashboards).
   - Link schemas to validators.
   - Flesh out dashboards spec (metrics, update cadence).
   - Draft runbooks & escalation SOPs.

2. **Schemas**
   - Fill in `common/common.json`.
   - Flesh out `PII_POLICY.md`.
   - Cross-link to canonical data rules.

3. **Plans**
   - Validate `phase_index.schema.json`.
   - Ensure each phase links to Work Orders.
   - Update status markers (🟡/🟦/✅/⏸).

### 📅 Near-term (Supports workflows, but less urgent)
4. **Design Docs**
   - Cross-link design index with phase plans.
   - Validate OpenAPI spec against WO API.
   - Ensure taxonomy + lineage flow into schemas.

5. **Diagrams**
   - Standardise READMEs + exports.
   - Align diagrams with design docs + phase plans.
   - Confirm MVP E2E flow completeness.

6. **SOP Families (`/sop/`)**
   - Populate instances from templates.
   - Ensure job orders in `/tasks/sop_joborders/` track progress.
   - Link workflow SOPs to lifecycle + diagrams.

7. **Scripts**
   - Add usage docs in `/sop/system/`.
   - Ensure unit tests + dependency notes.

### 🕒 Later (Housekeeping / polish)
8. **_faq_**
   - Merge duplicates into SOP families.
   - Ensure INDEX.md references correct FAQ.

9. **Security**
   - Expand to include access control + role mapping.

10. **Tasks & Templates**
    - Groom backlog.
    - Add templates for SOPs, plans, WOs.

11. **Labels**
    - Ensure `labels.json` matches `.github/labels.json`.

12. **Misc Root Docs**
    - Confirm commit sync process.
    - Ensure CONTRIBUTING.md aligns with labels.json.


## 7) Governance Rules Audit

**Current State:**  
Governance scaffolding already exists in Swan System Docs but is fragmented.

### ✅ In Place
- **Governance Metadata:** Present in `work_orders_index.md` (Last Reviewed, Owner, Next Audit Due, Quarterly Review).
- **Audit Process:** Defined in `docs_audit_process.md` and `docs_update_process.md` (SOPs).
- **Risk Handling:** Risks documented in workflow SOPs (`risk_control.md`) and Phase Plans.
- **Automation:** Scripts like `docs_guardian.py` and `validate_phase_index.py` exist for consistency checks.
- **Template Use:** Workflow SOPs use strict template/instance system; `README_TEMPLATE.md` provides repo consistency.

### ⚠️ Partial Coverage
- **Governance Metadata:** Not consistently applied across SOPs, Phase Plans, Root Docs, or Workflows.
- **Audit Process:** Defined in SOPs, but not universally referenced (Audit WO was not tied in previously).
- **Risk Register:** Risks exist in multiple places but not unified into one central register.
- **Automation Hooks:** Scripts exist but not integrated into CI workflows.
- **Archival/Legacy Handling:** Old plans (e.g., `chatgpt_commands_v3_plan.md`) not marked or archived.

### 🚨 Missing
- **Visual Governance Dashboard:** No Red/Amber/Green auto-summary of governance health.
- **Contributor Experience:** CONTRIBUTING.md does not reference governance cycles, audit cadence, or audit WO.

**Needs & Next Steps:**
- [ ] Apply governance metadata (Last Reviewed, Owner, Next Audit) consistently to SOPs, Plans, Root Docs, Workflows.
- [ ] Reference Audit WO in governance SOPs (`docs_audit_process.md`, `docs_update_process.md`).
- [ ] Create a central `risk_register.md` under `/docs/_audit/` to consolidate risks across Plans, SOPs, WOs.
- [ ] Integrate `docs_guardian.py` and `validate_phase_index.py` into CI workflows for automated enforcement.
- [ ] Mark/archive outdated plans (move to `/docs/_archive/` if retired).
- [ ] Develop a Visual Governance Dashboard (RAG view) sourced from Audit WO + Phase Plans.
- [ ] Expand CONTRIBUTING.md to include governance roles, audit cycles, and links to Audit WO + Summary.

---
