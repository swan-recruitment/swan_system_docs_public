# Swan ERP Docs – Index

Welcome to the Swan ERP documentation hub. This page links out to **diagrams**, **schemas**, **fixtures**, **validators**, **SOPs**, and **developer tools** used across the MVP and beyond.

---

## 🔰 Start Here
- **README** (root): [`README.md`](../README.md)
- **MVP Flow Diagram**: [`System Overview`](./diagrams/system_overview.md)

---

## 📊 Diagrams
- **System Overview** → `docs/diagrams/system_overview.md`
- **Governance Flow** → `docs/diagrams/governance_flow.md`
- **Canonical Data Rules** → `docs/diagrams/canonical_data_rules.md`
- **Roadmap Timeline** → `docs/diagrams/roadmap_timeline.md`

---

## 🧩 Schemas
- **Event Schema** → `docs/schemas/event.schema.json`
- **Run Schema** → `docs/schemas/run.schema.json`
- **Common Types** → `docs/schemas/common/common.json` _(placeholder path; add when available)_
- **PII Policy** → `docs/schemas/PII_POLICY.md` _(placeholder path; add when available)_

---

## 🧪 Fixtures
- **Valid**: `docs/fixtures/event.json`, `docs/fixtures/run.json`
- **Invalid**: `docs/fixtures/event.invalid.json`, `docs/fixtures/run.invalid.json`

---

## ✅ Validators
- **Event**: `docs/fixtures/validate_event.js`, `docs/fixtures/validate_event.py`
- **Run**: `docs/fixtures/validate_run.js`, `docs/fixtures/validate_run.py`

> Run with an optional file path to validate a specific fixture, e.g.  
> `node docs/fixtures/validate_event.js docs/fixtures/event.invalid.json`

---

## 📑 SOPs
- **File Standards SOP** → `docs/sop/file_standards_sop.md`
- **Docs Audit Process** → `docs/sop/docs_audit_process.md`
- **MVP Stub Packaging** → `docs/sop/mvp_stub_packaging.md`
- **Schema Lifecycle** → `docs/sop/schema_lifecycle.md`

---

## 🛠 Developer Tools & Scripts
- **Repo Checker** → `scripts/check_repo.ps1`
- **PR Creator** → `create_pr.ps1`

---

## 🧭 Navigation
- Back to **README**: [`../Comprehensive_README_v6.md`](../Comprehensive_README_v6.md)
- Explore **diagrams**: `./diagrams/`
- Explore **fixtures**: `./fixtures/`
- Explore **schemas**: `./schemas/`
- Explore **SOPs**: `./sop/`

---

**Last updated:** 2025-09-28

---
⬅ Return to [Docs Index](../index.md)
