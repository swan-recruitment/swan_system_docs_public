# 📝 Work Order: Swan Recruitment – Phase Issue Templates (System‑wide)

**Last updated:** 2025-09-26

## 🎯 Objective
Design, enforce, and continuously validate **Phase Issue Templates** used to plan and track delivery phases across all Swan repos.  
These templates guarantee that every phase has **clear objectives, dependencies, entry/exit criteria, risks, KPIs, tasks, and approvals**, and that links to **Phase Plans / Work Orders / Vision Docs** are correct.  
The workflow includes **automatic validation & link checks in CI**, **label/owner governance**, and **Control Tower visibility**.

**Non‑goals (MVP)**
- General “bug/feature/chore” templates (covered separately)
- PR templates (handled by GitHub Setup WO)
- Complex automation beyond validation and link checking (future)

---

## 🔑 Status Keys
🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred  
**Status:** 🟡 Drafted

---

## 1) Scope & Roles
### 1.1 Applies To
- All repos in the Swan org that manage delivery phases (docs, backend, portal, website, finance, desktop).

### 1.2 Roles
| Role | Responsibility |
|---|---|
| **Owner** (Ben) | Approves templates, final sign‑off on closeout |
| **Maintainers** | Review new/changed templates, CODEOWNERS for `.github/ISSUE_TEMPLATE` |
| **Contributors** | Use templates as written; no bypassing required fields |
| **CT Maintainers** | Keep CT linkages and dashboards in sync |

---

## 2) Directory & File Layout
```
.github/
  ISSUE_TEMPLATE/
    phase_kickoff.yml
    phase_delivery.yml
    phase_qa.yml
    phase_closeout.yml
docs/
  labels/labels.json            # canonical labels & colours
  plans/phase_plans_index.md    # already exists
  work_orders/work_orders_index.md
```
- **Canonical Source:** `swan_system_docs` (templates copied or org‑defaulted).

---

## 3) Label Taxonomy (Canonical)
```json
[
  {
    "name": "phase",
    "color": "6f42c1",
    "description": "Work is a phase of delivery"
  },
  {
    "name": "ct-track",
    "color": "0e8a16",
    "description": "Visible in Control Tower"
  },
  {
    "name": "kickoff",
    "color": "0366d6",
    "description": "Phase kickoff"
  },
  {
    "name": "delivery",
    "color": "0052cc",
    "description": "Phase delivery/execution"
  },
  {
    "name": "qa",
    "color": "5319e7",
    "description": "Phase QA/verification"
  },
  {
    "name": "closeout",
    "color": "1d76db",
    "description": "Phase closeout"
  },
  {
    "name": "blocked",
    "color": "b60205",
    "description": "Blocked by dependency or risk"
  },
  {
    "name": "risk",
    "color": "d93f0b",
    "description": "Material risk exists"
  },
  {
    "name": "needs-approval",
    "color": "ededed",
    "description": "Requires owner approval"
  }
]
```
> Store as `docs/labels/labels.json`. Repos should sync these labels (name+color+description).

---

## 4) Issue Forms – Templates (Authoritative)
> The 4 forms below are **GitHub Issue Forms** with required fields and validation.  
> They render markdown headings inside the issue body to aid link checking and audits.

### 4.1 Phase Kickoff
```yaml
name: "Phase: Kickoff"
description: "Start a delivery phase with objectives, dependencies, and entry/exit criteria."
title: "[Kickoff] <Project/Subsystem> – <Short name>"
labels: ["phase", "ct-track", "kickoff"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        ## Objectives
        Clearly state what this phase will deliver.
  - type: textarea
    id: objectives
    attributes:
      label: Objectives
      description: High-level outcomes and the definition of done for this phase.
      placeholder: >
        e.g., Deliver MVP of Contractor Portal uploads; health endpoints in CT; basic metrics.
    validations:
      required: true
  - type: textarea
    id: dependencies
    attributes:
      label: Dependencies
      description: Upstream/downstream dependencies (work orders, repos, external systems).
      placeholder: >
        e.g., Firebase functions for uploads; CT health endpoint; GA4 property
    validations:
      required: true
  - type: textarea
    id: entry_criteria
    attributes:
      label: Entry Criteria
      description: Preconditions to begin this phase.
      placeholder: >
        e.g., Repo scaffolded, branch protections on, env secrets available.
    validations:
      required: true
  - type: textarea
    id: exit_criteria
    attributes:
      label: Exit Criteria
      description: What must be true to call this phase complete.
      placeholder: >
        e.g., Acceptance criteria met, CI green, docs updated, owner sign-off.
    validations:
      required: true
  - type: textarea
    id: risks
    attributes:
      label: Risks & Mitigations
      placeholder: >
        e.g., Missing secrets -> mitigate with Secret Manager; perf risk -> Lighthouse in CI.
  - type: textarea
    id: kpis
    attributes:
      label: KPIs / Success Measures
      placeholder: >
        e.g., CI pass rate >= 90%, Time-to-close <= 14 days.
  - type: textarea
    id: links
    attributes:
      label: Links
      description: Phase Plan, Work Orders, Vision Docs, designs, diagrams.
      placeholder: >
        e.g., Phase plan item, WO links, CT dashboard URL.
    validations:
      required: true
  - type: checkboxes
    id: tasks
    attributes:
      label: Tasks
      options:
        - label: "Tasks drafted"
          required: true
        - label: "Risks reviewed"
          required: false
        - label: "Stakeholders notified"
          required: false
  - type: input
    id: approvals
    attributes:
      label: Approvals
      description: "Who must approve phase closeout (e.g., @ben-pitman)."
    validations:
      required: true

```

### 4.2 Phase Delivery
```yaml
name: "Phase: Delivery"
description: "Track execution of the phase; ensure audit trail and CT visibility."
title: "[Delivery] <Project/Subsystem> – <Short name>"
labels: ["phase", "ct-track", "delivery"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        ## Objectives
        Ensure the delivery work aligns to the Kickoff's objectives.
  - type: textarea
    id: scope
    attributes:
      label: Scope Updates (if any)
      description: List scope changes since Kickoff (if changed).
  - type: textarea
    id: progress
    attributes:
      label: Progress Summary
      description: Summarise work to date; include links to key PRs/issues.
    validations:
      required: true
  - type: textarea
    id: blockers
    attributes:
      label: Blockers
      description: Dependencies or risks causing delay; add `blocked` label if applicable.
  - type: textarea
    id: metrics
    attributes:
      label: Metrics / Evidence
      description: CI pass rates, perf numbers, adoption metrics, etc.
  - type: textarea
    id: links
    attributes:
      label: Links (Updated)
      description: Additional links since Kickoff (designs, CT views, dashboards).
  - type: checkboxes
    id: tasks
    attributes:
      label: Tasks
      options:
        - label: "CI green"
          required: true
        - label: "Docs updated"
          required: true
        - label: "Owner updated"
          required: false

```

### 4.3 Phase QA / Verification
```yaml
name: "Phase: QA / Verification"
description: "Formalise verification: tests, acceptance, and sign-off readiness."
title: "[QA] <Project/Subsystem> – <Short name>"
labels: ["phase", "ct-track", "qa"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        ## Objectives
        Confirm the phase meets acceptance criteria.
  - type: textarea
    id: test_plan
    attributes:
      label: Test Plan
      description: Link or outline the test plan: unit, integration, E2E, security, perf.
      placeholder: >
        e.g., Emulator tests pass; Lighthouse scores; redaction tests; parity tests.
    validations:
      required: true
  - type: textarea
    id: results
    attributes:
      label: Results & Evidence
      description: Summarise results, attach screenshots or logs, link CI runs.
    validations:
      required: true
  - type: checkboxes
    id: acceptance
    attributes:
      label: Acceptance Checks
      options:
        - label: "Acceptance criteria met"
          required: true
        - label: "Risks re-evaluated"
          required: true
        - label: "Docs updated"
          required: true

```

### 4.4 Phase Closeout
```yaml
name: "Phase: Closeout"
description: "Conclude the phase with approvals, lessons learned, and roll-forward notes."
title: "[Closeout] <Project/Subsystem> – <Short name>"
labels: ["phase", "ct-track", "closeout"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        ## Objectives
        Capture approvals, lessons, and ensure clean handover.
  - type: textarea
    id: outcomes
    attributes:
      label: Outcomes
      description: What was delivered vs original objectives.
    validations:
      required: true
  - type: textarea
    id: lessons
    attributes:
      label: Lessons Learned / Follow-ups
      description: What should we change next time? Any technical debt opened?
  - type: input
    id: approvals
    attributes:
      label: Approvals
      description: Who approved closeout (usernames or names).
    validations:
      required: true
  - type: checkboxes
    id: housekeeping
    attributes:
      label: Housekeeping
      options:
        - label: "CT dashboard updated"
          required: true
        - label: "Docs finalised"
          required: true
        - label: "Risks closed or rolled forward"
          required: true

```

---

## 5) Governance & Enforcement
- **CODEOWNERS** (per repo): gate changes to `.github/ISSUE_TEMPLATE/*` by Owners/Maintainers.
- **Required Sections**: enforced via `validations.required: true` in forms.
- **Backlinks**: every issue must link Phase Plan + WO; validated by CI link checker.
- **Approvals**: `Approvals` field must name approver(s); closeout requires Owner check.

---

## 6) CI Workflows (Validation + Link Check)
Add the following workflow in each repo using the templates (or as org default):

```yaml
name: Phase Issue Guardian

on:
  issues:
    types: [opened, edited]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Link check (lychee)
        uses: lycheeverse/lychee-action@v1
        with:
          args: --no-progress --verbose --max-concurrency 4 --accept 200,206,429 -- github-issue://${{ github.repository }}#${{ github.event.issue.number }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Basic body heuristics
        uses: actions/github-script@v7
        with:
          script: |
            const body = context.payload.issue.body || "";
            const mustContain = [
              "## Objectives",
              "## Dependencies",
              "## Entry Criteria",
              "## Exit Criteria",
              "## Risks & Mitigations",
              "## KPIs / Success Measures",
              "## Tasks",
              "## Approvals"
            ];
            const missing = mustContain.filter(h => !body.includes(h));
            if (missing.length) {
              core.setFailed(`Phase issue missing sections: ${missing.join(", ")}`);
            }
```

> Rationale: **Issue Forms** already enforce required fields, but this adds a **defense‑in‑depth** check and ensures headings exist for human readability.

---

## 7) Control Tower Integration
- **Discovery**: CT periodically lists issues with label `phase` + `ct-track` via GitHub API.
- **Fields** tracked: repo, number, title, status, assignees, labels, milestone, created/updated/closed timestamps.
- **Rollups**: open/in‑progress/closed counts per repo & per phase type.
- **Alerts**: issues stuck > N days in `🟦 In Progress` or missing Approvals on closeout.
- **Daily Digest**: summary of phase movements.

---

## 8) Adoption & Training
- Short Loom/video or README section showing **how to open a Phase Issue**.
- One‑pager cheat sheet: required sections, examples, and “how approval works”.
- Add **Quick Create** links to GitHub new‑issue pages for each template.

---

## 9) Migration & Rollout
1. Commit templates + labels to `swan_system_docs` (canonical).  
2. Roll out as **org defaults** or copy to each repo.  
3. Enable **Phase Issue Guardian** workflow.  
4. Run a **labels sync** (manual or script) to apply canonical labels.  
5. Announce new process; link to cheat sheet.  
6. Audit in 2 weeks: ensure all new phases use forms; fix drift.

---

## 10) Metrics & KPIs
- **Template Coverage**: % of phase issues created via forms (target ≥ 95%).
- **Validation Pass Rate**: % of issues passing CI checks first time (≥ 90%).
- **Lead Time per Phase**: created → closed, by template type.
- **Escapes**: # of issues missing Approvals at close (target = 0).
- **Broken Links**: count per week (target = 0 after week 2).

---

## 11) Milestones
**Phase 1 — Authoring**  
- Templates + labels in canonical repo; CODEOWNERS set

**Phase 2 — Validation**  
- CI link check + heuristics live and green on sandbox

**Phase 3 — Rollout**  
- Templates present in all target repos; labels synced

**Phase 4 — CT Visibility**  
- CT shows counts + stuck alerts; daily digest active

**Phase 5 — Training & Audit**  
- Cheat sheet shared; 2‑week adoption audit complete

---

## 12) Acceptance Criteria (MVP)
- [ ] All four templates available under `.github/ISSUE_TEMPLATE/` in target repos
- [ ] CI fails issues missing required sections or with broken links
- [ ] Labels (`phase`, `ct-track`, `kickoff`, `delivery`, `qa`, `closeout`) exist and auto‑apply
- [ ] CT can list phase issues and produce counts by status/type
- [ ] At least one real Phase Issue per template created and validated

---

## 13) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Contributors bypass templates | M | M | Branch protection, CODEOWNERS, training |
| Label drift across repos | M | M | Canonical `labels.json` + periodic sync |
| Link checker false positives | M | L | Allowlist internal links; tune lychee args |
| Template fatigue | M | M | Keep forms concise; pre‑fill examples |
| CT polling limits | L | M | Cache results; schedule respectfully |

---

## 14) Maintenance
- Quarterly review of forms + labels; update versions
- Re‑run labels sync when taxonomy changes
- Monitor KPIs; adjust validation rules if needed

---

## 15) Related Documents
- [Work Orders Index](work_orders_index.md)  
- [Phase Plans Index](../plans/phase_plans_index.md)  
- [Work Order – GitHub Setup](work_order_github_setup__MERGED.md)  
- [Work Order – Control Tower](work_order_control_tower.md)  
- [CONTRIBUTING.md](../contributing.md) • [PR Template](../.github/PULL_REQUEST_TEMPLATE.md)

---

> **Notes:** This WO ships **ready‑to‑use forms**, a **CI workflow**, and a **label taxonomy**. It defines governance, CT integration, adoption metrics, and a concrete rollout plan so that phase issues become reliable, comparable units of execution across the org.
