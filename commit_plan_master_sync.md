# Commit Plan — Master Sync (Governance + Merged Work Order)

This plan describes how to commit and ship the prepared **swan_system_docs** bundle containing:
- The **merged** `docs/work_order_master.md` (canonical content + Governance Update v2).
- Governance assets in `.github/` (issue templates, **pull_request_template.md**, **labels.json**).
- Docs additions: **CONTRIBUTING.md**, **labels_import_instructions.md**.
- Existing diagrams, phase plans, work orders, and indexes.

---

## 1) Branch & Scope

**Branch name:**  
`governance/master-sync-visuals-and-templates`

**Scope:**  
- Replace `docs/work_order_master.md` with the *merged* canonical version.  
- Ensure `.github/` contains Issue Templates, PR template, and `labels.json`.  
- Ensure `/docs/` contains `CONTRIBUTING.md` and `labels_import_instructions.md`.  
- Keep diagrams (flow, ERD, sequence, module map) present in `.md`/`.mmd`/`.html` formats.  
- Keep Phase Plans, Work Orders, and indexes as in bundle.

---

## 2) Atomic Commits (Conventional Commits)

1. `chore(repo): add .github labels.json and PR template`  
2. `docs(contributing): add detailed contributor guide and labels import how-to`  
3. `docs(work-orders): merge canonical master with governance update`  
4. `docs(diagrams): ensure flow, ERD, sequence, module map exist in md/mmd/html`  
5. `docs(plans): keep indices and phase plans in place`  

> Prefer atomic commits for clearer review history. If you want a single commit, use the combined message in section 3.

---

## 3) Commands (example workflow)

```bash
# Ensure you are in the repo root and on main
git checkout -b governance/master-sync-visuals-and-templates

# Unpack the prepared bundle (update the filename/path as needed)
unzip swan_system_docs-structure-updated.zip -d .

# Stage and commit in logical chunks (or as one commit if preferred)
git add .
git commit -m "chore(repo): add .github labels.json and PR template"
git commit -m "docs(contributing): add detailed contributor guide and labels import how-to"
git commit -m "docs(work-orders): merge canonical master with governance update"
git commit -m "docs(diagrams): ensure flow, ERD, sequence, module map exist in md/mmd/html"
git commit -m "docs(plans): keep indices and phase plans in place"

git push -u origin governance/master-sync-visuals-and-templates
```

**Single-commit alternative:**
```bash
git add .
git commit -m "docs: sync master work order + governance assets; add PR template, labels.json, CONTRIBUTING, diagram indexes"
git push -u origin governance/master-sync-visuals-and-templates
```

---

## 4) Open the PR

**Title:** `Master sync: governance assets + merged work order`  
**Labels:** `governance`, `plan`, `needs-review`  
**Link Issues:** If there’s a Phase issue open, add `Closes #<issue>`  
**Reviewers:** Docs/Planning lead (@ben.pitman) and affected area leads (Visuals/Backend)

---

## 5) PR Checklist (map to template)

- [ ] Files changed listed (work orders, .github, docs, diagrams)  
- [ ] Cross-links updated in: **Design Specs Index / Phase Plans Index / Visual Docs Index / Master WO**  
- [ ] DoD met for governance (PR template present, labels.json present, CONTRIBUTING present)  
- [ ] Risks & mitigations stated (low risk; easy rollback)  
- [ ] CI checks pass (markdown lint, link check, optional Mermaid validation)  
- [ ] Screenshots attached for any diagram changes (optional)

---

## 6) Post‑Merge Follow‑ups

1. **Seed labels** from `.github/labels.json` using `/docs/labels_import_instructions.md`.  
2. **Verify templates**:  
   - Open “New issue” → confirm Phase forms appear.  
   - Open “New PR” → confirm PR template loads.  
3. **Create Phase issue** for the next work item (e.g., Deployment Diagram) using the phase form.  
4. Add to **Project board** if in use.

---

## 7) Rollback Plan

If something looks off after merge:
- Use GitHub’s **Revert** button on the PR to auto-open a rollback PR, **or**  
- Identify the merge commit SHA and run:
  ```bash
  git revert <merge_commit_sha>
  git push
  ```

This preserves history while removing the undesired changes.

---

## 8) Appendix: What’s in the Bundle

- `.github/`  
  - `ISSUE_TEMPLATE/` (phase_1_2.yml … phase_8.yml, config.yml)  
  - `pull_request_template.md`  
  - `labels.json`  
- `docs/`  
  - `CONTRIBUTING.md`  
  - `labels_import_instructions.md`  
  - `work_order_master.md` (merged)  
  - `design/` (indexes/templates)  
  - `diagrams/` (flow, ERD, sequence, module map in md/mmd/html; PNG placeholders)  
  - `plans/` (phase plans + index)  
  - `work_orders/` (all WOs, including visuals + governance)  

---

**Owner:** @ben.pitman  
**Last updated:** 1758914837.0699844
