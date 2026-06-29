# 📝 Work Order: Swan Recruitment – GitHub Setup (swan-git-project)

**Last updated:** 2025-09-27  
**Backlinks:** [Master WO (Full)](work_order_master__FULL.md) · [Work Orders Index](work_orders_index.md)

## 🎯 Objective
Establish a **secure, consistent GitHub organization** for Swan Recruitment that supports all subprojects, enforces best practices, and integrates into the **Control Tower** for visibility and governance.  

**Non‑goals (MVP):**
- Advanced CI/CD pipelines (handled per project)  
- Long‑term GitOps or infra‑as‑code repos (future scope)  
- External contributor access (initially staff only)

---

## 🔑 Status Keys
🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred  

**Status:** 🟡 Drafted

---

## 1) GitHub Organization Setup
- [ ] Create/verify org: `swancms`  
- [ ] Enforce **SSO** (if available) + **2FA mandatory** for all members  
- [ ] Teams: `Owners`, `Maintainers`, `Developers`, `Viewers`  
- [ ] Role assignments:  
  - Owners = Directors / Core Maintainers  
  - Developers = project contributors  
  - Viewers = read‑only staff (finance, admin)  
- [ ] Org‑wide defaults: LICENSE, CONTRIBUTING.md, SECURITY.md

**Deliverable:** Org visible, secure, and ready for repos.

---

## 2) Repository Standards
- [ ] Repo naming convention: `swan‑<subproject>`  
- [ ] Default branch: `main`  
- [ ] Protections:  
  - Require PRs for merges  
  - Require 1+ reviewer approvals  
  - Disallow force pushes  
- [ ] Templates:  
  - `.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`  
  - `CODEOWNERS` per repo  
- [ ] LICENSE: Apache‑2.0 (or agreed policy) applied across all repos

**Deliverable:** Consistent, professional repos.

---

## 3) Branching & Workflow
- [ ] **Commit messages**: Conventional Commits (e.g., `feat: …`, `fix: …`, `docs: …`)  
- [ ] **Branches**:  
  - `main` = production  
  - `dev` = staging / integration  
  - `feat/*`, `fix/*`, `chore/*` = feature branches  
- [ ] **PRs**: linked to issues; description + checklist required  
- [ ] **Reviews**: at least 1 review; CODEOWNERS enforced  
- [ ] **Tags**: semantic versioning (`vX.Y.Z`)

**Deliverable:** Documented, enforced Git workflow.

---

## 4) CI/CD Seeds
- [ ] Enable **GitHub Actions** org‑wide  
- [ ] Shared starter workflows:  
  - Lint + test  
  - Build + deploy stubs  
  - Docs Guardian CI for system repos  
- [ ] Artifact storage in releases  
- [ ] Matrix ready (Node, Python) for Swan subprojects

**Deliverable:** All repos start with baseline CI.

---

## 5) Security & Compliance
- [ ] Enable **Dependabot** for deps + security updates  
- [ ] Enable **Secret scanning** + push protection  
- [ ] Configure branch protection rules across repos  
- [ ] Security.md with disclosure policy  
- [ ] Regular access review: inactive users removed

**Deliverable:** Secure GitHub footprint.

---

## 6) Observability & Control Tower Hooks
- [ ] Maintain **repo registry** in CT (list + metadata)  
- [ ] Sync status: last commit, open issues, PRs  
- [ ] Hook CI pass/fail status into CT dashboard  
- [ ] Alerts for failing CI or unprotected repos

**Deliverable:** GitHub status visible in Control Tower.

---

## 7) Milestones
**Phase 1 — Org Setup**  
- Org created, 2FA enforced, teams/roles set

**Phase 2 — Repo Standards**  
- Repos renamed, LICENSE applied, branch protections set

**Phase 3 — Workflow**  
- Commit/branching/PR rules in place; CODEOWNERS applied

**Phase 4 — CI/CD Seeds**  
- GitHub Actions templates live; baseline checks enabled

**Phase 5 — CT Hooks**  
- Repo registry & CI status visible in CT

---

## 8) Acceptance Criteria (MVP)
- [ ] All staff accounts with 2FA enforced  
- [ ] All repos follow `swan-` naming convention  
- [ ] LICENSE, README, CONTRIBUTING, SECURITY present in each repo  
- [ ] PRs require review; no direct pushes to main  
- [ ] GitHub Actions run on PR + push  
- [ ] CT dashboard shows repo list + CI status

---

## 9) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Orphaned repos / rogue standards | M | M | Regular audits; enforce CODEOWNERS |
| Missed branch protections | L | H | Baseline automation via Actions or CT audit |
| Secrets leakage in code | M | H | Secret scanning + staff training |
| Staff bypass of 2FA | L | H | Org‑level enforcement; no exceptions |
| Inconsistent licenses | L | M | Apply org‑wide default LICENSE |

---

## 10) Related Documents
- [Work Orders Index](work_orders_index.md)  
- [Work Order Master](work_order_master.md)  
- [SOP PR Guide](../sop/swan_open_pr_guide.md)  
- [Control Tower Work Order](work_order_control_tower.md)  
- [Phase Plans Index](../plans/phase_plans_index.md)  

---

> Notes: Expanded from the original GitHub Setup WO. Now covers org setup, repo standards, workflow, CI/CD seeds, security, observability, milestones, acceptance criteria, and risk management. This ensures Swan’s GitHub usage is professional, consistent, and visible in CT.
---

### 📏 Canonical Data Rules (Swan)
- Use **snake_case** field names; FKs end with **`_id`**.
- Money uses `{ "amount_minor": int, "currency": "GBP" }` (no floats).
- Dates = `*_date` (date) and `*_at` (datetime, ISO-8601).
- Import common types from **[`../schemas/common/common.json`](../schemas/common/common.json)**.
- Follow **PII redaction** policy in **[`../schemas/PII_POLICY.md`](../schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`../design/field_lineage.md`](../design/field_lineage.md)**.
