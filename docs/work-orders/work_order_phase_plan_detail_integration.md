# 📝 Work Order: Swan Recruitment – Phase Plan Detail Integration

**Last updated:** 2025-09-26

## 🎯 Objective
Create a **single authoritative Phase Plans Index** by merging the expanded content into the canonical `phase_plans_index.md`, normalising structure, fixing cross-links, and wiring governance/CI so it **stays correct** over time. This WO implements a repeatable process, validation scripts, and CI to prevent drift.

**Non‑goals (MVP)**
- Rewriting individual Phase Plan documents’ content (beyond normalising headings/links)
- Building dashboards (those surface via Control Tower once links are stable)

---

## 🔑 Status Keys
🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred  

**Status:** 🟡 Drafted

---

## 1) Inputs & Current State
- Source of truth (expanded): `docs/plans/phase_plans_index_detailed.md`
- Canonical (to be replaced): `docs/plans/phase_plans_index.md`
- Phase plans: `docs/plans/phase_1_2_plan.md` … `docs/plans/phase_8_plan.md`
- Visuals: `swan_erp_flow_diagram.*`, `swan_erp_erd.*`, `swan_erp_sequence_contract.*`, `swan_erp_module_map.*`

> This WO formalises the merge/replace process described in the existing “Phase Plan Detail Integration” brief and its v2 update (scope, steps, risks, and acceptance).

---

## 2) Directory Layout
```
docs/
  plans/
    phase_plans_index.md              # ← canonical after this WO
    phase_plans_index_detailed.md     # ← archived copy (history only)
    phase_1_2_plan.md
    phase_3_plan.md
    ...
    schema/
      phase_index.schema.json         # JSON schema for optional export/validation
scripts/
  plans/
    merge_phase_plans.py              # performs merge+normalisation+report
    validate_phase_index.py           # structural checks / headings / links summary
.github/
  workflows/
    docs_linkcheck.yml                # nightly + PR link checking for docs/
.lychee.toml                           # link-check config
```

---

## 3) Canonical Structure (per Phase section)
Every phase block in the index must contain these headings exactly (for readability + automation):

1. **Objectives**  
2. **Dependencies**  
3. **Entry Criteria**  
4. **Exit Criteria**  
5. **Risks & Mitigations**  
6. **KPIs / Success Measures**  
7. **Links** (Work Orders, Vision/Design Specs, Visuals, CT views)

> Scripts/CI validate that each phase subsection includes all seven headings.

---

## 4) Data Model & CT Mapping (excerpt)
If the index is exported to JSON for Control Tower ingestion, each phase item uses:

```json
{
  "id": "phase_3",
  "title": "Phase 3 — Backend Core",
  "status": "🟦 In Progress",
  "objectives": ["..."],
  "dependencies": ["../work_orders/work_order_firebase_backend.md", "..."],
  "entry_criteria": ["..."],
  "exit_criteria": ["..."],
  "risks": [{"item":"...", "level":"M", "mitigation":"..."}],
  "kpis": ["..."],
  "links": [
    {"type":"work_order","href":"../work_orders/work_order_control_tower.md"},
    {"type":"visual","href":"../design/visuals/swan_erp_flow_diagram.png"}
  ]
}
```

See `docs/plans/schema/phase_index.schema.json` for the full optional schema.

---

## 5) Process & Steps (detailed)
1. **Gap analysis** — Compare `phase_plans_index_detailed.md` → `phase_plans_index.md`. Identify missing sections, broken links, and heading mismatches.
2. **Merge** — Replace canonical file contents with detailed version while **normalising headings** to the seven-section structure.
3. **Normalise links** — Ensure all relative links are consistent (prefer relative `../` paths within `docs/` and kebab-case filenames).
4. **Append governance** — Add Status Keys legend and Maintenance section at bottom of canonical index.
5. **Validate** — Run `scripts/plans/validate_phase_index.py` to check headings and emit a report of missing sections or link anomalies.
6. **Link check** — CI workflow `docs_linkcheck.yml` runs **Lychee** to verify all hyperlinks inside `docs/` (on PR + nightly).
7. **Archive** — Move the previously detailed file to `phase_plans_index_detailed.md` and annotate that canonical is the source of truth.
8. **PR & Review** — Open PR, request review from Backend/Portal leads; merge when green.
9. **CT tie‑in** (optional) — Export JSON and confirm CT can ingest the structured model (fields above).

---

## 6) Tooling Deliverables
### 6.1 Merge tool
`python scripts/plans/merge_phase_plans.py --detailed docs/plans/phase_plans_index_detailed.md --canonical docs/plans/phase_plans_index.md --archive`

**What it does:**
- Copies detailed → canonical, preserves front‑matter if present
- Ensures all phase sections contain the seven headings (injects empty ones if missing)
- Normalises relative links and heading levels
- Writes a **merge report** to stdout (counts, added headings, fixed links)

### 6.2 Validator
`python scripts/plans/validate_phase_index.py docs/plans/phase_plans_index.md`

**Checks:**
- Presence of the seven required headings for each phase
- Collects all links and prints a summary list (CI link checker verifies reachability)
- Emits non‑zero exit code if required sections are missing

### 6.3 CI — Docs Link Check
Runs on PRs and nightly to scan `docs/` with Lychee (link checker). Configured via `.lychee.toml`.

---

## 7) Acceptance Criteria (MVP)
- [ ] `phase_plans_index.md` **fully matches** expanded detail; headings normalised
- [ ] **0 broken links** in `docs/` (CI green)
- [ ] Each phase section includes **all seven** required headings
- [ ] Archived detailed file present for history; canonical marked as source of truth
- [ ] PR merged with approvals from Backend + Portal leads

---

## 8) KPIs
- **Link health:** 0 broken links week over week
- **Completeness:** 100% phases include all headings
- **Review velocity:** PR cycle time ≤ 2 working days

---

## 9) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Drift reappears over time | M | M | CI link check + validator; quarterly review |
| Broken cross‑links after renames | M | M | Relative links + Lychee + PR checks |
| Inconsistent heading levels | M | L | Normaliser enforces h2/h3 levels |
| CT ingestion mismatch | L | M | JSON export + schema validation before CT import |

---

## 10) Maintenance
- Add a **quarterly docs audit** to the calendar
- Keep `.lychee.toml` allowlist tuned (e.g., private repo links)
- When adding new phases, ensure the seven headings and cross‑links are present **before** merging

---

## 11) Related Documents
- [Work Orders Index](../work_orders/work_orders_index.md)  
- [Vision Docs Index](../design/vision_index.md)  
- [Design Specs Index](../design/design_specs_index.md) *(if present)*  
- [Work Order – Control Tower](../work_orders/work_order_control_tower.md)

---

> Notes: This WO operationalises the consolidation plan and adds scripts + CI so your phase index remains complete, consistent, and link‑healthy over time.
