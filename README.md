# Swan System Docs 📚

## What is this repository?

This is the **Swan System Docs** repository — the **umbrella documentation repo** for all Swan projects.  
It centralises documentation that spans across multiple implementation repos, including:

- **Work Orders** — detailed project delivery instructions  
- **Plans** — phased rollout strategies and refactor plans  
- **SOPs** — standard operating procedures (system, operational, compliance, workflow)  
- **Schemas & Configs** — shared data definitions and examples  
- **Visuals & Diagrams** — process flows, ERP maps, and system diagrams  
- **Quick Guides & FAQs** — onboarding and reference material

Unlike the code repos (e.g. `swan-control-tower`, `swan-firebase-backend`), this repo’s purpose is **documentation-first**.  
It acts as the **umbrella index** for the Swan ecosystem.

---

## 🚀 Purpose

Swan Recruitment is building a **custom ERP system** to unify candidate sourcing, contract generation, contractor management, finance, and reporting.
This repo organizes all **project documentation** into clear sections that align with the **Control Tower** (#CTM) for orchestration and delivery.

---

## 📂 Repository Structure
- **swan_system_docs/**
  - **docs/**
    - **_agentchat/** → internal assistant notes/prompts and collaboration scratchpad.
    - **_audit/** → QA checks, validation output, and review notes.
    - **_faq/** → quick answers to common questions.
    - **control_tower/** → Control Tower subsystem docs.
    - **design/** → design specs, templates, component details.
    - **diagrams/** → flow diagrams, module maps, sequences, architecture.
    - **labels/** → label definitions.
    - **lifecycles/** → lifecycle/state definitions.
    - **plans/** → phase plans (1–8) + master index.
    - **quickguides/** → step-by-step contributor guides.
    - **schemas/** → canonical schema docs.
    - **scripts/** → utility scripts and automation.
    - **security/** → security policies and procedures.
    - **sop/** → standard operating procedures.
    - **tasks/** → task breakdowns.
    - **templates/** → templates for work orders/docs/issues.
    - **work-orders/** → subsystem work orders (Firebase, Control Tower, Website, etc.).
    - **workflows/** → workflow descriptions and supporting docs.

  - **.github/** → CI workflows, issue/PR templates, CODEOWNERS, validation rules.
  - **schemas/** → system-wide schema definitions (outside `docs/`).
  - **.gitignore** → ignore rules.
  - **lychee.toml** → link checker config for `lychee`.

  - **Top-level files**
    - **CONTRIBUTING.md** → contribution guidelines.
    - **INDEX.md** → documentation index.
    - **commit_plan_master_sync.md** → Master Sync (governance + merged work order).
    - **labels_import_instructions.md** → label setup for GitHub issues/PRs.
    - **work_order_master.md** → canonical master work order across subsystems.


---

## 🌴 Repo Tree 

    swan_system_docs/
    ├─ .github/
    │  ├─ ISSUE_TEMPLATE/
    │  │  ├─ config.yml
    │  │  ├─ phase_1_2.yml
    │  │  ├─ phase_3.yml
    │  │  ├─ phase_4.yml
    │  │  ├─ phase_5.yml
    │  │  ├─ phase_6.yml
    │  │  ├─ phase_7.yml
    │  │  ├─ phase_8.yml
    │  │  ├─ phase_closeout.yml
    │  │  ├─ phase_delivery.yml
    │  │  ├─ phase_kickoff.yml
    │  │  └─ phase_qa.yml
    │  ├─ workflows/
    │  │  ├─ docs_linkcheck.yml
    │  │  ├─ docs-link-check.yml
    │  │  └─ phase_issue_guardian.yml
    │  ├─ CODEOWNERS
    │  ├─ labels.json
    │  ├─ lychee.toml
    │  └─ pull_request_template.md
    ├─ docs/
    │  ├─ _agentchat_/
    │  │  ├─ audit
    │  │  └─ level_one
    │  ├─ _audit/
    │  │  ├─ content_level_review
    │  │  ├─ risk_register.md
    │  │  └─ summary_audit_system_docs.md
    │  ├─ _faq_/
    │  │  ├─ data_security
    │  │  ├─ data_workflows
    │  │  ├─ labels_import_instructions.md
    │  │  ├─ what_is_a_readme
    │  │  ├─ what_is_contributing
    │  │  ├─ what_is_json_label
    │  │  └─ what_is_the_ct_doing
    │  ├─ control_tower/
    │  │  ├─ schemas/
    │  │  │  ├─ event.schema.json
    │  │  │  ├─ run.schema.json
    │  │  │  └─ systems.schema.json
    │  │  ├─ config.example.yaml
    │  │  ├─ dashboards_spec.md
    │  │  └─ README.md
    │  ├─ design/
    │  │  ├─ openapi/
    │  │  │  └─ control_tower.yaml
    │  │  ├─ updates/
    │  │  │  └─ chat_updates_summary.md
    │  │  ├─ control_tower_vision.md
    │  │  ├─ design_spec_template.md
    │  │  ├─ design_specs_index.md
    │  │  ├─ desktop_manager_vision.md
    │  │  ├─ erp_repo_structure.md
    │  │  ├─ event_taxonomy.md
    │  │  ├─ field_lineage.md
    │  │  ├─ swan_erp_system_architecture.md
    │  │  ├─ vision_index.md
    │  │  └─ work_orders_index.mmd
    │  ├─ diagrams/
    │  │  ├─ contractor-onboarding/
    │  │  │  ├─ 03_timesheet_invoice_submission/
    │  │  │  │  └─ 03_timesheet_invoice_submission.mmd
    │  │  │  ├─ 04_timesheet_invoice_entry/
    │  │  │  │  └─ 04_timesheet_invoice_entry.mmd
    │  │  │  ├─ 05_sales_invoice_generation/
    │  │  │  │  └─ 05_sales_invoice_generation.mmd
    │  │  │  ├─ 06_payroll_accounts/
    │  │  │  │  └─ 06_payroll_accounts.mmd
    │  │  │  └─ 07_reporting_analytics/
    │  │  │     └─ 07_reporting_analytics.mmd
    │  │  ├─ erp-flow-diagram/
    │  │  │  ├─ erp-flow-diagram.png
    │  │  │  ├─ README
    │  │  │  ├─ swan_erp_flow_diagram.html
    │  │  │  ├─ swan_erp_flow_diagram.md
    │  │  │  └─ swan_erp_flow_diagram.mmd
    │  │  ├─ erp-module-map/
    │  │  │  ├─ erp-module-map.png
    │  │  │  ├─ README
    │  │  │  ├─ swan_erp_module_map.html
    │  │  │  ├─ swan_erp_module_map.md
    │  │  │  └─ swan_erp_module_map.mmd
    │  │  ├─ erp-sequence-contract-generator/
    │  │  │  ├─ erp-sequence_contract
    │  │  │  ├─ README
    │  │  │  ├─ sequence_diagram_contract_generator_flow.png
    │  │  │  ├─ swan_erp_sequence_contract.html
    │  │  │  ├─ swan_erp_sequence_contract.md
    │  │  │  └─ swan_erp_sequence_contract.mmd
    │  │  ├─ canonical_data_rules.md
    │  │  ├─ governance_flow.md
    │  │  ├─ mvp_e2e_flow_contractor_portal
    │  │  ├─ README.md
    │  │  └─ visual_docs_index.md
    │  ├─ labels/
    │  │  └─ labels.json
    │  ├─ lifecycles/
    │  │  └─ contractor-lifecycle-automation/
    │  │     └─ sop_ATS_to_payment
    │  ├─ plans/
    │  │  ├─ schema/
    │  │  │  └─ phase_index.schema.json
    │  │  ├─ chatgpt_commands_v3_plan.md
    │  │  ├─ cloud_functions_refactor_plan.md
    │  │  ├─ phase_1_2_plan.md
    │  │  ├─ phase_3_plan.md
    │  │  ├─ phase_4_plan.md
    │  │  ├─ phase_5_plan.md
    │  │  ├─ phase_6_plan.md
    │  │  ├─ phase_7_control_tower_workflow.md
    │  │  ├─ phase_7_plan.md
    │  │  ├─ phase_8_plan.md
    │  │  └─ phase_plans_index.md
    │  ├─ quickguides/
    │  │  ├─ BEGINNERS_GUIDE_GIT.md
    │  │  ├─ commands_cheatsheet_functional.md
    │  │  └─ commands_cheatsheet_styled.md
    │  ├─ schemas/
    │  │  ├─ common/
    │  │  │  └─ common.json
    │  │  └─ PII_POLICY.md
    │  ├─ scripts/
    │  │  ├─ control_tower/
    │  │  │  └─ generate_daily_digest.py
    │  │  ├─ plans/
    │  │  │  ├─ merge_phase_plans.py
    │  │  │  └─ validate_phase_index.py
    │  │  └─ docs_guardian.py
    │  ├─ security/
    │  │  ├─ gdpr_retention.md
    │  │  └─ secrets_policy.md
    │  ├─ sop/
    │  │  ├─ compliance/
    │  │  │  ├─ instances/
    │  │  │  ├─ templates/
    │  │  │  │  └─ sop_compliance_procedure.md
    │  │  │  └─ README.md
    │  │  ├─ emergency/
    │  │  │  ├─ instances/
    │  │  │  ├─ templates/
    │  │  │  │  └─ sop_emergency_procedure.md
    │  │  │  └─ README.md
    │  │  ├─ operational/
    │  │  │  ├─ instances/
    │  │  │  ├─ templates/
    │  │  │  │  └─ sop_operational_procedure.md
    │  │  │  └─ README.md
    │  │  ├─ system/
    │  │  │  ├─ instances/
    │  │  │  ├─ templates/
    │  │  │  │  └─ sop_system_procedure.md
    │  │  │  └─ README.md
    │  │  ├─ workflow/
    │  │  │  ├─ instances/
    │  │  │  │  └─ contractor_onboarding/
    │  │  │  │     ├─ 01_contract_creation/
    │  │  │  │     │  ├─ data/
    │  │  │  │     │  │  └─ data_flow_mapping.md
    │  │  │  │     │  ├─ exceptions/
    │  │  │  │     │  │  └─ exceptions.md
    │  │  │  │     │  ├─ people/
    │  │  │  │     │  │  └─ raci.md
    │  │  │  │     │  ├─ performance/
    │  │  │  │     │  │  └─ metrics_kpi.md
    │  │  │  │     │  ├─ process/
    │  │  │  │     │  │  └─ workflow_step.md
    │  │  │  │     │  ├─ risk/
    │  │  │  │     │  │  └─ risk_control.md
    │  │  │  │     │  ├─ visuals/
    │  │  │  │     │  │  └─ visual_map.md
    │  │  │  │     │  └─ README.md
    │  │  │  │     ├─ 02_portal_account/
    │  │  │  │     │  ├─ data/
    │  │  │  │     │  │  └─ data_flow_mapping.md
    │  │  │  │     │  ├─ exceptions/
    │  │  │  │     │  │  └─ exceptions.md
    │  │  │  │     │  ├─ people/
    │  │  │  │     │  │  └─ raci.md
    │  │  │  │     │  ├─ performance/
    │  │  │  │     │  │  └─ metrics_kpi.md
    │  │  │  │     │  ├─ process/
    │  │  │  │     │  │  └─ workflow_step.md
    │  │  │  │     │  ├─ risk/
    │  │  │  │     │  │  └─ risk_control.md
    │  │  │  │     │  ├─ visuals/
    │  │  │  │     │  │  └─ visual_map.md
    │  │  │  │     │  └─ README.md
    │  │  │  │     ├─ 03_timesheet_invoice_submission/
    │  │  │  │     │  ├─ data/
    │  │  │  │     │  │  └─ data_flow_mapping.md
    │  │  │  │     │  ├─ exceptions/
    │  │  │  │     │  │  └─ exceptions.md
    │  │  │  │     │  ├─ people/
    │  │  │  │     │  │  └─ raci.md
    │  │  │  │     │  ├─ performance/
    │  │  │  │     │  │  └─ metrics_kpi.md
    │  │  │  │     │  ├─ process/
    │  │  │  │     │  │  └─ workflow_step.md
    │  │  │  │     │  ├─ risk/
    │  │  │  │     │  │  └─ risk_control.md
    │  │  │  │     │  ├─ visuals/
    │  │  │  │     │  │  └─ visual_map.md
    │  │  │  │     │  └─ README.md
    │  │  │  │     ├─ 04_timesheet_invoice_entry/
    │  │  │  │     │  ├─ data/
    │  │  │  │     │  │  └─ data_flow_mapping.md
    │  │  │  │     │  ├─ exceptions/
    │  │  │  │     │  │  └─ exceptions.md
    │  │  │  │     │  ├─ people/
    │  │  │  │     │  │  └─ raci.md
    │  │  │  │     │  ├─ performance/
    │  │  │  │     │  │  └─ metrics_kpi.md
    │  │  │  │     │  ├─ process/
    │  │  │  │     │  │  └─ workflow_step.md
    │  │  │  │     │  ├─ risk/
    │  │  │  │     │  │  └─ risk_control.md
    │  │  │  │     │  ├─ visuals/
    │  │  │  │     │  │  └─ visual_map.md
    │  │  │  │     │  └─ README.md
    │  │  │  │     ├─ 05_sales_invoice_generation/
    │  │  │  │     │  ├─ data/
    │  │  │  │     │  │  └─ data_flow_mapping.md
    │  │  │  │     │  ├─ exceptions/
    │  │  │  │     │  │  └─ exceptions.md
    │  │  │  │     │  ├─ people/
    │  │  │  │     │  │  └─ raci.md
    │  │  │  │     │  ├─ performance/
    │  │  │  │     │  │  └─ metrics_kpi.md
    │  │  │  │     │  ├─ process/
    │  │  │  │     │  │  └─ workflow_step.md
    │  │  │  │     │  ├─ risk/
    │  │  │  │     │  │  └─ risk_control.md
    │  │  │  │     │  ├─ visuals/
    │  │  │  │     │  │  └─ visual_map.md
    │  │  │  │     │  └─ README.md
    │  │  │  │     ├─ 06_payroll_accounts/
    │  │  │  │     │  ├─ data/
    │  │  │  │     │  │  └─ data_flow_mapping.md
    │  │  │  │     │  ├─ exceptions/
    │  │  │  │     │  │  └─ exceptions.md
    │  │  │  │     │  ├─ people/
    │  │  │  │     │  │  └─ raci.md
    │  │  │  │     │  ├─ performance/
    │  │  │  │     │  │  └─ metrics_kpi.md
    │  │  │  │     │  ├─ process/
    │  │  │  │     │  │  └─ workflow_step.md
    │  │  │  │     │  ├─ risk/
    │  │  │  │     │  │  └─ risk_control.md
    │  │  │  │     │  ├─ visuals/
    │  │  │  │     │  │  └─ visual_map.md
    │  │  │  │     │  └─ README.md
    │  │  │  │     ├─ 07_reporting_analytics/
    │  │  │  │     │  ├─ data/
    │  │  │  │     │  │  └─ data_flow_mapping.md
    │  │  │  │     │  ├─ exceptions/
    │  │  │  │     │  │  └─ exceptions.md
    │  │  │  │     │  ├─ people/
    │  │  │  │     │  │  └─ raci.md
    │  │  │  │     │  ├─ performance/
    │  │  │  │     │  │  └─ metrics_kpi.md
    │  │  │  │     │  ├─ process/
    │  │  │  │     │  │  └─ workflow_step.md
    │  │  │  │     │  ├─ risk/
    │  │  │  │     │  │  └─ risk_control.md
    │  │  │  │     │  ├─ visuals/
    │  │  │  │     │  │  └─ visual_map.md
    │  │  │  │     │  └─ README.md
    │  │  │  │     ├─ DELTA_README.md
    │  │  │  │     └─ README.md
    │  │  │  ├─ templates/
    │  │  │  │  ├─ sop_data_flow_mapping.md
    │  │  │  │  ├─ sop_exceptions.md
    │  │  │  │  ├─ sop_metrics_kpi.md
    │  │  │  │  ├─ sop_risk_control.md
    │  │  │  │  ├─ sop_roles_responsibility.md
    │  │  │  │  ├─ sop_visual_map.md
    │  │  │  │  └─ sop_workflow_step.md
    │  │  │  └─ README.md
    │  │  ├─ docs_audit_process.md
    │  │  ├─ docs_update_process.md
    │  │  ├─ file_standards_sop.md
    │  │  ├─ INSTANCE_INDEX.md
    │  │  ├─ mvp_stub_packaging.md
    │  │  ├─ README.md
    │  │  ├─ schema_lifecycle.md
    │  │  └─ TEMPLATE_INDEX.md
    │  ├─ tasks/
    │  │  ├─ sop_joborders/
    │  │  │  ├─ joborder_sop_fleshing_checklist.md
    │  │  │  └─ joborder_sop_fleshing.md
    │  │  ├─ backlog.md
    │  │  ├─ ct_quality_jobs.md
    │  │  ├─ joborder_sop_fleshing_checklist.md
    │  │  ├─ joborder_sop_fleshing.md
    │  │  ├─ progress_dashboard.md
    │  │  └─ tracker.json
    │  ├─ templates/
    │  │  └─ README_TEMPLATE.md
    │  ├─ work-orders/
    │  │  ├─ project_delivery_workorders_plan.md
    │  │  ├─ work_order_contractor_portal.md
    │  │  ├─ work_order_control_tower.md
    │  │  ├─ work_order_desktop_manager.md
    │  │  ├─ work_order_excel_migration.md
    │  │  ├─ work_order_finance_integration.md
    │  │  ├─ work_order_firebase_backend.md
    │  │  ├─ work_order_github_setup.md
    │  │  ├─ work_order_phase_issue_templates.md
    │  │  ├─ work_order_phase_plan_detail_integration.md
    │  │  ├─ work_order_system_docs_audit.md
    │  │  ├─ work_order_visuals.md
    │  │  ├─ work_order_website.md
    │  │  └─ work_orders_index.md
    │  ├─ workflows/
    │  │  └─ contractor_workflow.md
    │  ├─ commit_plan_master_sync.md
    │  ├─ CONTRIBUTING.md
    │  ├─ INDEX.md
    │  └─ work_order_master.md
    ├─ schemas/
    │  └─ common/
    │     └─ common.json
    ├─ .gitignore
    ├─ CONTRIBUTING.md
    ├─ INDEX.md
    ├─ lychee.toml
    └─ README.md


---

## 📅 Roadmap & Phase Plans

Project is delivered in **8 phases**, tracked in `/swan_system_docs/docs/plans/`.

🔑 Start here: [Phase Plans Index](/swan_system_docs/docs/plans/phase_plans_index.md)

Status keys:
- 🟡 Drafted
- 🟦 In Progress
- ✅ Approved
- ⏸ Deferred

---

## 🗂️ Work Orders

Subsystem-level execution docs live in `/swan_system_docs/docs/work_orders/`.
Each maps back to a phase in the plan and the [Work Order Master](/swan_system_docs/docs/work_order_master.md).

Examples:
- [Firebase Backend](/swan_system_docs/docs/work_orders/work_order_firebase_backend.md) (Phase 3 – Backend Core)
- [Control Tower](/swan_system_docs/docs/work_orders/work_order_control_tower.md) (Phase 4 – Monitoring & Orchestration)
- [Contractor Portal](/swan_system_docs/docs/work_orders/work_order_contractor_portal.md)
- [Website](/swan_system_docs/docs/work-orders/work_order_website.md)

👉 Full index: [Work Order Master](/swan_system_docs/docs/work_order_master.md)

---

## 🏗️ Architecture & Diagrams

System-level architecture and visuals live in `/swan_system_docs/docs/diagrams/`.

- [ERP System Architecture](/swan_system_docs/docs/diagrams/swan_erp_system_architecture.md)
- ERP Flow Diagram (`/swan_system_docs/docs/diagrams/erp-flow-diagram/`)
- ERP Module Map (`/swan_system_docs/docs/diagrams/erp-module-map/`)
- Contract Generator Sequence (`/swan_system_docs/docs/diagrams/erp-sequence-contract-generator/`)

👉 Visual index: [Visual Docs Index](docs/diagrams/visual_docs_index.md)

---

## 🧭 Control Tower Integration

This repo aligns with the **Swan Control Tower** (#CTM), which manages:
- Phase orchestration
- Work order execution
- Version tracking
- System health checks

📌 **Rules**:
- All subsystem docs must link to both their **phase plan** and the **work order master**.
- Status markers (🟡/🟦/✅/⏸) must be updated before merge.
- Diagrams should include both source (`.drawio`/`.mmd`) and export (`.svg`/`.png`).

---

## 📊 Status Dashboard (lightweight)

> **Note:** This is a **convenience snapshot** for at-a-glance status.
> The **source of truth** remains in [Work Order Master](/swan_system_docs/docs/work_order_master.md).
> Keep this list small and high-signal.

| Subsystem                | Phase | Work Order Link                                                                          |  Status  |
|-------------------------|:-----:|-------------------------------------------------------------------------------------------|----------|
| Firebase Backend        |   3   | /swan_system_docs/docs/work_orders/work_order_firebase_backend.md                         | 🟡 Drafted |
| Control Tower           |   4   | /swan_system_docs/docs/work_orders/work_order_control_tower.md                            | 🟡 Drafted |
| Contractor Portal       |   –   | /swan_system_docs/docs/work_orders/work_order_contractor_portal.md                        | 🟡 Drafted |
| Website                 |   –   | /swan_system_docs/docs/work_orders/work_order_website.md                                  | 🟡 Drafted |

> Tip: When a subsystem progresses, update **Work Order Master** first, then mirror the key change here.

---


---

## 🧠 Vision & Strategy

For big‑picture direction and long‑term evolution of the Control Tower, see the **Control Tower Vision** document.  
It expands the MVP into operational orchestration, advanced monitoring/reporting, and intelligent automation with governance.

- Scope: goals, personas, architecture (Mermaid), component design
- Orchestration: job chaining, retries, approvals, RBAC, audit
- Observability: events/runs, KPIs/SLOs, anomaly detection
- Intelligence: predictive maintenance, recommendation engine, AI validation
- Ops: notifications, escalation, environments, CI/CD, risks, testing, runbooks

📄 **Read:** [Control Tower Vision](/swan_system_docs/docs/design/control_tower_vision.md)

## 🤝 Contributing

See [CONTRIBUTING.md](/swan_system_docs/docs/CONTRIBUTING.md) for contribution guidelines.
Use [labels_import_instructions.md](/swan_system_docs/docs/labels_import_instructions.md) to set up GitHub labels.

---

## 📌 Quick Links

- [Phase Plans Index](/swan_system_docs/docs/plans/phase_plans_index.md)
- [Work Order Master](/swan_system_docs/docs/work_order_master.md)
- [ERP System Architecture](/swan_system_docs/docs/diagrams/swan_erp_system_architecture.md)
- [Visual Docs Index](/swan_system_docs/docs/diagrams/visual_docs_index.md)
---

## 🛠 ERP Source Code

This documentation hub is complemented by the **swan-erp** repository, which contains the ERP source code and development setup.

👉 [swan-erp repo](../swan-erp)


# 📘 Swan ERP Documentation

Welcome to the documentation hub for the Swan ERP system.  
This directory contains SOPs (Standard Operating Procedures), visual diagrams, and related job orders for maintaining and improving the system.

---

## 📂 Contents

### 1. SOPs (Standard Operating Procedures)
All SOP templates and instances are organized into families:  
- [SOP Master Index](./sop/README.md)  
- [Template Index](./sop/TEMPLATE_INDEX.md)  

Families included:  
- Workflow SOPs  
- System SOPs  
- Operational SOPs  
- Compliance & Audit SOPs  
- Emergency & Exception SOPs  

---

### 2. Diagrams
Visual representations of workflows, systems, and data flows.  
- [Diagram Standards & Naming](./diagrams/README.md)  

---

### 3. Tasks & Job Orders
Job orders track documentation tasks and SOP development work.  
- [SOP Job Orders](./tasks/sop_joborders/)  

---

## 📑 Usage

1. Start with the **SOP Master Index** to choose the right SOP family.  
2. Use **Template Index** for quick navigation of available templates.  
3. Link SOPs to **Diagrams** for clarity.  
4. Track active work in **Job Orders**.  

---

## 🔗 Related Resources

- [System Documentation (Repo Root)](../README.md)  
- [ERP Source Code](../)  
