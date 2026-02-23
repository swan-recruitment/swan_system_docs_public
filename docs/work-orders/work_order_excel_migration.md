# 📝 Work Order: Swan Recruitment – Excel Migration (swan-excel-tools)

**Last updated:** 2025-09-26
**Backlinks:** [Master WO (Full)](work_order_master__FULL.md) · [Work Orders Index](work_orders_index.md)

## 🎯 Objective
Manage and **migrate legacy Excel/VBA workflows** (timesheet & invoice entry, VBA macros, templates) into **modern Python workflows** embedded in the **Desktop Manager**, with data persisted in Firebase and fully observable via the Control Tower.

**Non‑goals (MVP)**
- Building a full BI/reporting suite (lives in Control Tower/Reporting)
- Multi‑tenant template designer (support 1–2 standard templates first)
- Replacing the Contractor Portal upload flows (Portal remains contractor‑facing)

---

## 🔑 Status Keys
🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred  

**Status:** 🟡 Drafted

---

## 1) Project & Environments Setup
- [ ] Repository: `swan-excel-tools`
- [ ] Folders:
  - `vba/` — legacy macros exported as `.bas`
  - `templates/` — Excel/Word/HTML templates used by legacy flows
  - `docs/` — migration notes, field maps, template guides
  - `samples/` — anonymised sample inputs/outputs for tests
- [ ] `.gitignore` for temp files (`~$*.xls*`, `.DS_Store`, `/secrets`)
- [ ] `README.md` with purpose, structure, and local run instructions

**Deliverable:** Repo created with legacy VBA + templates consolidated and documented.  

---

## 2) Legacy System Capture & Documentation
- [ ] Export **all VBA modules** (`.bas`, `.cls`) and save under `vba/`
- [ ] For each macro:
  - Purpose, inputs, outputs, side‑effects
  - Dependencies (linked sheets, file paths, naming conventions)
  - Known quirks (date parsing, locale formatting, rounding)
- [ ] Inventory **templates**: filename, version, owner, usage
- [ ] Map **Excel/Sheet fields → ERP/Firebase model**

**Deliverable:** Comprehensive legacy documentation + field/logic map.

---

## 3) Target Architecture & Data Contracts
- **Runtime**: Python modules invoked from **Desktop Manager**
- **Persistence**: Firestore/Storage for records and generated artifacts
- **Events**: CT events for job start/finish/error (correlationId, runId)
- **Contracts**:
  - Timesheet: contractorId, period, hours/days, approvals, attachments
  - Invoice: invoiceId, period, lines (desc, qty, rate, VAT), totals, attachments
  - Templates: versioned artifacts with checksum and owner

**Deliverable:** `docs/mappings.md` covering Excel→Python→Firestore/Storage mapping.

---

## 4) Python Replacement Design
- [ ] Identify flows to move into **Desktop Manager**:
  - Timesheet entry helper (staff‑side tooling)
  - Invoice entry helper
  - Invoice document generation (PDF/XLSX) for clients
- [ ] Modules:
  - `src/timesheets/` — parse, validate, normalise, persist
  - `src/invoices/` — line build, VAT rules, totals, persist
  - `src/templates/` — rendering (XLSX/HTML→PDF) with versioning
- [ ] Libraries (suggested):
  - `pandas`, `openpyxl`/`xlsxwriter` for Excel I/O
  - `python-docx` or HTML→PDF (WeasyPrint/wkhtmltopdf) for PDFs
  - `pydantic` for schemas & strict validation

**Deliverable:** Design notes + module skeletons with typed interfaces.

---

## 5) Implementation – Timesheets
- [ ] Parse legacy Excel timesheets (openpyxl) → normalised Python model
- [ ] Validate (date ranges, totals, missing fields)
- [ ] Persist to Firestore (`timesheets`) + upload raw file to Storage
- [ ] Set RTDB status (`/timesheetStatus/{contractorId}`) for Portal
- [ ] Emit CT event `excel.timesheet.ingested` with run metrics
- [ ] Export parity file (optional) for verification

**Deliverable:** Timesheets fully processed by Python path, matching legacy results.

---

## 6) Implementation – Invoices
- [ ] Build invoices from legacy inputs (or staff form) using Python
- [ ] Apply VAT rules; compute totals with **shared rounding helper**
- [ ] Generate **client‑facing PDF** (HTML→PDF or DOCX→PDF pipeline)
- [ ] Persist invoice to Firestore (`invoices`) + upload PDF to Storage
- [ ] Emit CT event `excel.invoice.generated`
- [ ] (If needed) push to **Finance Integration** queue for accounts export

**Deliverable:** Invoices generated and ready for finance export.

---

## 7) Templates & Naming Conventions
- [ ] Introduce **template registry** (JSON/YAML) with:
  - templateId, version, lastChangedBy, checksum
  - applicable client(s), sample data link
- [ ] Enforce naming:
  - Timesheet: `TS_{contractorId}_{YYYY-WW}.xlsx`
  - Invoice: `INV_{invoiceId}_{YYYY-MM}.pdf`
- [ ] Document where templates live (Storage path) and how to update safely

**Deliverable:** Controlled template lifecycle with clear naming/ownership.

---

## 8) Quality, Parity & Golden Tests
- [ ] Build **golden sample set** (anonymised) of legacy inputs + outputs
- [ ] Write parity tests that compare Python output vs legacy output:
  - Numeric totals (within ±0.01 tolerance)
  - Dates/formatting rules
  - File metadata (naming, presence)
- [ ] Include edge cases: missing signatures, partial weeks, leap years, DST

**Deliverable:** Automated parity suite demonstrating equivalence (or deliberate differences documented).

---

## 9) Observability, Audit & CT Hooks
- [ ] Structured logs with `runId`/`correlationId`
- [ ] Persist **Run** + **Event** docs for 180 days
- [ ] Metrics: items processed, failures, duration, retries
- [ ] Alerts: repeated failures, template checksum mismatch
- [ ] Daily digest to ops via CT (optional)

**Deliverable:** Clear operational visibility of migration pipelines.

---

## 10) CI/CD & Packaging
- [ ] GitHub Actions:
  - Lint + unit tests
  - Parity tests against `samples/`
  - Package wheels/zip for Desktop Manager inclusion
- [ ] Versioning: tag releases consumed by Desktop Manager
- [ ] Artifact publishing: GitHub Releases + checksum

**Deliverable:** Repeatable builds consumed by Desktop Manager.

---

## 11) Cutover & Decommission Plan
- [ ] **Pilot**: run Python + legacy side‑by‑side for 2–4 weeks
- [ ] Staff sign‑off checklist (Faye/Ben): parity confirmed
- [ ] Freeze legacy templates/macros; tag repo `legacy-v1`
- [ ] Switch staff usage to Desktop Manager; disable macros
- [ ] Archive old tools in `swan-excel-tools` and Drive
- [ ] Announce cutoff date and rollback procedure

**Deliverable:** Clean, auditable cutover with rollback path.

---

## 12) Milestones
**Phase 1 — Setup & Capture**  
- Repo created; VBA exported; templates inventoried

**Phase 2 — Mapping & Design**  
- Field maps written; Python module design approved

**Phase 3 — Timesheets**  
- Python path live; parity green on samples

**Phase 4 — Invoices**  
- PDF generation live; finance queue integration proven

**Phase 5 — Cutover**  
- Staff switched; legacy decommissioned

---

## 13) Acceptance Criteria (MVP)
- [ ] All **legacy macros** and templates documented in repo
- [ ] Python pipeline ingests **timesheets** and builds **invoices**
- [ ] Outputs match legacy results on golden set (numerical parity)
- [ ] Files written with correct naming + Storage locations
- [ ] CT shows events and daily counts (ingested/generated)
- [ ] Staff sign‑off recorded; legacy tools archived

---

## 14) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Parity gaps (rounding/VAT) | M | H | Shared rounding helper; golden tests; finance sign‑off |
| Hidden macro dependencies | M | M | Full VBA export; dependency map; pilot |
| Template drift post‑cutover | M | M | Template registry + checksum; change control |
| Staff adoption delay | M | M | Dual‑run pilot, clear comms, quick fixes |
| PII in legacy files | L | H | Anonymise samples; redact logs; storage policies |

---

## 15) Related Documents
- [Work Orders Index](work_orders_index.md)  
- [Work Order – Desktop Manager](work_order_desktop_manager__MERGED.md)  
- [Work Order – Firebase Backend](work_order_firebase_backend.md)  
- [Work Order – Finance Integration](work_order_finance_integration__MERGED.md)  
- [Work Order – Control Tower](work_order_control_tower.md)  
- [Vision Docs Index](../design/vision_index.md)

---

> Notes: This merged WO **expands your original Excel Migration plan** (repo + VBA export, documentation, Python replacement in Desktop App, testing, cutover) into an execution‑ready, testable roadmap with field mappings, parity testing, CT observability, and clear acceptance criteria.
---

### 📏 Canonical Data Rules (Swan)
- Use **snake_case** field names; FKs end with **`_id`**.
- Money uses `{ "amount_minor": int, "currency": "GBP" }` (no floats).
- Dates = `*_date` (date) and `*_at` (datetime, ISO-8601).
- Import common types from **[`docs/schemas/common/common.json`](../schemas/common/common.json)**.
- Follow **PII redaction** policy in **[`docs/schemas/PII_POLICY.md`](../schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`docs/design/field_lineage.md`](../design/field_lineage.md)**.
