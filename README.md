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
