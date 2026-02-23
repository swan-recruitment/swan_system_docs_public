# Contributing Guide – Swan Recruitment ERP Docs & Planning

Welcome! This repository hosts the **planning system** for the Swan ERP: work orders, phase plans, design specs, and visual documentation.  
This guide explains **how to propose work, track phases, update diagrams/specs, and raise PRs** using the conventions we’ve set up.

---

## 0) Repository Scope

- **This repo is docs-first**: plans, specs, diagrams, issue/PR templates, governance.
- Source code lives in the implementation repos (e.g., `swan-firebase-backend`, `swan-desktop-manager`, etc.).
- Changes here should improve **clarity, traceability, and quality gates** for the whole program.

---

## 1) Folder Structure (docs-first)

```
/docs
  /plans                  # Phase plans 1–8 + index files
  /design                 # Design Specs + index + template
  /work_orders            # Work Orders (active + archive/)
  /diagrams               # Mermaid diagrams .md + .mmd + .html
.github
  /ISSUE_TEMPLATE         # Phase Issue Forms (yml)
  pull_request_template.md (optional)
CONTRIBUTING.md
```

**Required formats for diagrams:** every diagram must exist in **all 3** forms:
- `*.md` → renders natively on GitHub  
- `*.mmd` → raw Mermaid source (easy to edit/import)  
- `*.html` → standalone preview (Mermaid CDN)

When you add or edit a diagram, also update **`/docs/design/design_specs_index.md`** and **`/docs/plans/phase_plans_index.md`** so cross-links stay accurate.

---

## 2) Issues → Using Phase Templates

Use the **Phase Issue Forms** in `.github/ISSUE_TEMPLATE/` to create or track work for a phase.

**Open a new issue** → choose the relevant **Phase** form:
- Phase 1–2 (Foundations + Backend Core)
- Phase 3 (Desktop + Excel Migration)
- … through Phase 8 (Final Rollout & Continuous Improvement)

Each form collects:
- **Objective** – what the phase should deliver (business + technical)
- **Dependencies** – preconditions to start
- **Entry Criteria** – must be true before work begins
- **Exit Criteria (Definition of Done)** – how we confirm the phase is complete
- **Risks & Mitigations**
- **KPIs / Acceptance Tests**
- **Linked Files** – phase plans, specs, visuals
- **Tasks** – a checklist for execution
- **Approvals** – who signs off

**Labels** are automatically applied (e.g., `phase-3`, `planning`). You can add more from the taxonomy below.

---

## 3) Labels – Taxonomy

Apply labels consistently so dashboards stay useful:

**Phase** (always one): `phase-1-2`, `phase-3`, `phase-4`, `phase-5`, `phase-6`, `phase-7`, `phase-8`  
**Type**: `work-order`, `design-spec`, `diagram`, `plan`, `governance`  
**Status**: `draft`, `in-progress`, `blocked`, `needs-review`, `approved`, `deferred`  
**Priority**: `p1`, `p2`, `p3`  
**Area** (optional): `backend`, `desktop`, `portal`, `website`, `finance`, `control-tower`

> Tip: Keep **one Phase label** per issue to avoid clutter.

---

## 4) Work Orders – Authoring & Updating

Work Orders live in `/docs/work_orders/` and should follow this structure:

- **Objective** – short problem statement
- **Scope** – what’s in/out
- **Inputs** – files or decisions needed
- **Deliverables / DoD** – “what done looks like”
- **Steps** – ordered tasks
- **Risks & Mitigations**
- **Acceptance Criteria / KPIs**
- **Ownership** – assignee + reviewers

### Special Work Orders (governance)
- `work_order_visuals.md` – now **MANDATORY** to include the **Deployment Diagram**.
- `work_order_phase_plan_detail_integration.md` – merges the detailed phase index into the canonical one.
- `work_order_phase_issue_templates.md` – issue forms (templates created; CONTRIBUTING doc closes this WO).

When a WO is completed, move it to `/docs/work_orders/archive/` and update **`work_order_master.md`**.

---

## 5) Diagrams – Standards & Workflow

**Where:** `/docs/diagrams/`  
**Formats:** `.md`, `.mmd`, `.html` (all three required)

**Mermaid types used here:**
- `flowchart` – system & module flows
- `erDiagram` – Firestore + Realtime DB schema
- `sequenceDiagram` – step-by-step workflows
- `flowchart` (module map) – app/service interactions
- *(optional)* **Deployment** – repos → CI/CD → hosting

**When updating diagrams:**
1. Edit the `.mmd` or `.md` (Mermaid block).
2. Regenerate `.html` (copy the standard HTML shell with Mermaid CDN).
3. Update references in:
   - `/docs/design/design_specs_index.md`
   - `/docs/plans/phase_plans_index.md`
   - `/docs/work_orders/work_order_visuals.md` (if relevant)
4. Note the change in the PR (see PR guidelines).

---

## 6) Design Specs – Standards

**Location:** `/docs/design/`  
**Index:** `design_specs_index.md`  
**Template:** `_template.md` (Overview, Inputs/Outputs, Architecture & Flow, Technology, Risks, Testing)

**Must-have specs (examples):**
- Contract Generator, Status Sync, Auth Roles & Claims, DB Schema (Phase 2)
- Desktop Timesheet/Invoice Modules, Reporting (Phase 3)
- Portal Uploads + Status Dashboard (Phase 4)
- Finance Automation + Payment Sync + Reconciliation (Phase 5)
- Control Tower components (Phase 7)

Each spec should link to **relevant diagrams** (Flow, ERD, Sequence, Module Map) and have **clear DoD** and **UAT checkpoints**.

---

## 7) Phase Plans – Standards

**Location:** `/docs/plans/`  
- Use `phase_plans_index.md` and (expanded) `phase_plans_index_detailed.md` as **authoritative** references.
- Each phase plan file (e.g., `phase_5_plan.md`) includes **objectives, actions, deliverables** and should link to:
  - Relevant **work orders**
  - **Design specs**
  - **Diagrams**

**Entry/Exit Criteria** and **KPIs** are **mandatory** in the index and/or the individual phase file.

---

## 8) Pull Requests – Workflow

**Branch naming:**

```
feature/phase-3-desktop-timesheets
docs/phase-5-finance-reconciliation
diagram/phase-2-erd-v1
governance/issue-templates
fix/links-design-index
```

**Commit messages (Conventional Commits recommended):**

```
docs(plans): add KPIs and risks to phase 4
chore(templates): add phase-5 issue form
feat(diagrams): add module interaction map
fix(index): repair broken link to sequence diagram
```

**PR checklist (minimum):**
- Purpose & summary of change
- Files affected (plans/specs/diagrams/work orders)
- Cross-link updates (indexes updated?)
- Screenshots for diagrams (optional)
- Risks & mitigations (if any)
- Reviewers tagged

**Link issues/PRs:** use GitHub keywords to auto-close: `Closes #123`, `Fixes #456`.

**Approvals:** at least one reviewer from the relevant area (Backend, Desktop, Portal, Finance, Control Tower).

---

## 9) Quality Gates (CI suggestions)

It’s recommended to enable these actions in this repo:

- **Markdown lint** (e.g., `markdownlint-cli`)  
- **Broken link check** (e.g., `lychee` or `markdown-link-check`)  
- **Mermaid validation** (basic – ensure code blocks compile; optional)  
- **Spell check** (optional)

PRs that fail quality checks should be marked `needs-review` until corrected.

---

## 10) Security & Secrets (Docs repo)

- Do **not** commit secrets or API keys.  
- For code repos, use **GitHub Actions Secrets** and `.env` files excluded by `.gitignore`.
- Redact PII in example payloads (CATSone, invoices, etc.).

---

## 11) Triage & Lifecycle

**New** → **In Planning** → **In Progress** → **In Review** → **Approved** → **Done** → *(Archive if WO)*

- Keep the **Phase issue** open for the full phase; reference multiple PRs as needed.
- Update labels as the issue progresses (e.g., `draft` → `in-progress` → `needs-review` → `approved`).
- Use **milestones** or **Projects** to track phases across repos.

---

## 12) Frequently Used Links (filenames)

- **Phase Plans Index:** `/docs/plans/phase_plans_index.md` (+ `_detailed.md`)  
- **Design Specs Index:** `/docs/design/design_specs_index.md`  
- **Visual Docs Index:** `/docs/diagrams/visual_docs_index.md` (or `/docs/visual_docs_index.md` if kept at root)  
- **Work Order Master:** `/docs/work_orders/work_order_master.md`  
- **Visuals Work Order:** `/docs/work_orders/work_order_visuals.md`

---

## 13) What “Good” Looks Like (Example)

- You update the **ERD** to add `payments` collection.  
- You commit three files in `/docs/diagrams/`: `swan_erp_erd.md` + `.mmd` + `.html`.  
- You edit **Design Specs Index** to reference the ERD.  
- You edit **Phase Plans Index (detailed)** to reflect the schema change in Phase 2.  
- You raise a PR with description, risks, and screenshots.  
- CI passes (lint + links). Reviewer approves → merge.

---

## 14) Contacts & Ownership

- **Docs/Planning lead:** `@ben.pitman`  
- **Area leads:** assign per phase/area in PRs (Backend, Desktop, Portal, Website, Finance, Control Tower)

If in doubt, open a Phase Issue using the appropriate template and tag the relevant lead(s).

---

Thanks for keeping Swan ERP documentation **clear, consistent, and auditable**.  
Good documentation makes delivery easier—and safer.
