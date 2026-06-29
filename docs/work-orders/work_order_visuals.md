# 📝 Work Order: Swan Recruitment – Visuals (Architecture & Process Diagrams)

**Last updated:** 2025-09-26

**Repo:** `swan_system_docs`  
**Location:** `/docs/work_orders/work_order_visuals.md` 

## 🎯 Objective
Create and maintain a **complete, consistent set of system visuals** that explain Swan’s platform from business flow through deployment. Ensure visuals are **versioned, linkable, and renderable** in docs and CI, and cross‑linked to Phase Plans and Work Orders.

**Non‑goals (MVP)**
- Live infra dashboards (CT covers operational views)
- Pixel‑perfect UI design system (handled in Website/Design System work)

---

## 🔑 Status Keys
🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred  
**Status:** 🟡 Drafted

---

## 1) Directory Layout & Naming
```
docs/
  design/
    visuals/
      flow/
      erd/
      modules/
      sequence/
      deployment/
    design_specs_index.md           # optional
  work_orders/work_orders_index.md
  plans/phase_plans_index.md
```

**File naming pattern** (all diagrams provide these formats):
- Base name: `swan_<type>_<topic>` (e.g., `swan_flow_erp`, `swan_erd_core`, `swan_modules_map`, `swan_sequence_contract`, `swan_deployment_platform`)
- Required formats per diagram:
  - `*.mmd` (Mermaid source) **required**
  - `*.md` (readme with context + legend) **required**
  - `*.html` (standalone render) **required**
  - `*.png` or `*.svg` (browsable image) **recommended**

---

## 2) Required Diagram Set (Deliverables)

### 2.1 Business / Process Flow
**Purpose:** End‑to‑end contractor→invoice→payment journey and staff interventions.  
**Files:** `design/visuals/flow/swan_flow_erp.(mmd|md|html|png)`  
**Content checklist:**
- Contractor onboarding → timesheet → approval → invoicing → finance → payment
- Systems swimlanes (Portal, Firebase, Finance Integration, CT, Desktop, Website)
- Decision nodes for approvals/exception queues

### 2.2 Entity‑Relationship Diagram (ERD)
**Purpose:** Data model for contracts, contractors, clients, invoices, timesheets.  
**Files:** `design/visuals/erd/swan_erd_core.(mmd|md|html|png)`  
**Content checklist:**
- Key entities & relationships (1‑N, M‑N), cardinalities, IDs
- Notes for derived fields and indexing/queries

### 2.3 Module Interaction Map
**Purpose:** High‑level boxes‑and‑arrows of subsystems and their APIs.  
**Files:** `design/visuals/modules/swan_modules_map.(mmd|md|html|png)`  
**Content checklist:**
- Firebase Backend, Contractor Portal, Website, Desktop Manager, Finance Integration, Control Tower
- Interfaces: REST, Firestore, RTDB, Webhooks, Storage
- Directional flow + frequency labels (sync/async)

### 2.4 Sequence Diagram (Contract lifecycle)
**Purpose:** Time‑ordered interactions for a representative flow.  
**Files:** `design/visuals/sequence/swan_sequence_contract.(mmd|md|html|png)`  
**Content checklist:**
- Actors: Contractor, Portal, Firebase Functions, Finance Integration, Accounts API, CT
- Messages: submit, validate, export, payment webhook/poll, status update
- Error/alt paths noted (e.g., webhook failure → polling fallback)

### 2.5 Deployment Diagram (**new & required**)
**Purpose:** Show repos → CI → hosting → runtime environments.  
**Files:** `design/visuals/deployment/swan_deployment_platform.(mmd|md|html|png)`  
**Content checklist:**
- Repos (swan‑portal, swan‑backend, swan‑finance, swan‑desktop, website, system‑docs)
- CI/CD (GitHub Actions), environments (dev/staging/prod), hosting (Firebase/Functions/Hosting), Desktop packaging
- Secrets, permissions, and monitoring touchpoints (CT)

---

## 3) Tooling & Rendering
- **Authoring:** Mermaid (`.mmd`) as the canonical source.  
- **Local preview:** VS Code Mermaid or web preview.  
- **Exporting:** `mmdc` (Mermaid CLI) to output `.png/.svg` and `.html`.  
- **Docs embedding:** reference images in `.md` and link to `.html` for zoomable view.

> Optional: PlantUML allowed for ERD/Sequence if needed; keep Mermaid as the canonical format wherever possible.

---

## 4) Governance & Cross‑Links
- Each diagram must include a **front‑matter or header** in the `.md` with:
  - **Scope/Intent**, **Last updated**, and **Related links** (Work Orders, Phase Plans, Vision Docs, CT views).
- **Backlinks** from relevant WOs/Plans to the diagram’s `.md` page.
- Add entries to a **Visuals Index** (if you keep one), and ensure Work Orders Index & Phase Plans reference visuals where relevant.

---

## 5) Workflow (Step‑by‑Step)
1. Draft Mermaid in the correct folder (`flow/`, `erd/`, `modules/`, `sequence/`, `deployment/`).  
2. Create a matching `.md` file with context, assumptions, and a small legend.  
3. Export `.html` and one image format.  
4. Cross‑link from **Phase Plans** and **Work Orders**.  
5. Open PR; reviewers check content, consistency, and links.  
6. Upon merge, ensure **Docs Link Check** CI is green (runs on `docs/**`).

---

## 6) Quality & Review Checklist
- ✅ Diagram matches current architecture/flows (no stale components).  
- ✅ Mermaid parses and renders; no syntax errors.  
- ✅ At least one **image** and one **HTML** export opens correctly.  
- ✅ Links from `.md` resolve (WOs, Plans, CT).  
- ✅ Diagrams share consistent naming, fonts, and legends.  
- ✅ Deployment diagram includes CI/CD, environments, and monitoring.

---

## 7) Acceptance Criteria (MVP)
- [ ] All five required diagrams exist with `.mmd`, `.md`, `.html` (image recommended).  
- [ ] All diagrams are **cross‑linked** from relevant Work Orders and Phase Plans.  
- [ ] **Docs Link Check** CI passes with **0 broken links**.  
- [ ] A reviewer (Owner/Maintainer) signs off that visuals reflect the current design.  

---

## 8) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Diagrams drift out of date | M | H | Quarterly review; change alongside code/WO updates |
| Broken links in docs | M | M | CI link check (Lychee) on PR & nightly |
| Multiple formats fall out of sync | M | M | Always regenerate exports on change; PR checklist |
| Tooling variance (PlantUML vs Mermaid) | M | L | Prefer Mermaid; note any alternates in `.md` |

---

## 9) Maintenance
- **Quarterly visual audit** (calendar event).  
- Regenerate exports when `.mmd` changes.  
- Keep deployment diagram aligned with CI/CD or hosting changes.  
- Update cross‑links when files move (search/replace + CI check).

---

## 10) Related Documents
- [Work Orders Index](work_orders_index.md)  
- [Phase Plans Index](../plans/phase_plans_index.md)  
- [Control Tower WO](work_order_control_tower.md)  
- [Website WO](work_order_website__MERGED.md) · [Firebase WO](work_order_firebase_backend.md) · [Portal WO](work_order_contractor_portal.md) · [Finance WO](work_order_finance_integration__MERGED.md) · [Desktop Manager WO](work_order_desktop_manager__MERGED.md)

---

> Notes: This merged WO standardises **what diagrams we produce, where they live, how they’re rendered**, and how they tie back to plans and work orders. It adds a **Deployment Diagram** as a first‑class deliverable to make infra clear to stakeholders.
