# 📊 Swan System Docs – Audit Summary

This table provides a one-page overview of the **System Docs Audit**, mapping each folder to findings and next steps.

| Folder | Findings | Next Steps |
|--------|----------|------------|
| _agentchat_ | Proto experiments, early notes | Clarify purpose; merge or formalise |
| _audit_ | Content-level review material | Clarify ownership; migrate findings into Audit WO |
| _faq_ | Quick reference docs | Review duplication with SOPs; expand CT FAQ; link in INDEX.md |
| control_tower | Configs, schemas, dashboards, cheat sheets | Expand README; link schemas; flesh dashboards; add SOPs |
| design | Vision, architecture, taxonomy, OpenAPI | Cross-link with Phase Plans; validate OpenAPI; fill missing specs |
| diagrams | ERP flows, module map, contract generator, onboarding | Standardise READMEs; complete visual index; add missing diagrams |
| labels | GitHub labels config | Sync with .github/labels.json; update workflow labels |
| lifecycles | Contractor lifecycle automation SOP | Validate `sop_ATS_to_payment`; link to SOP workflow family |
| plans | Phase 1–8 plans + schema | Validate schema; audit outdated plans; link WOs; merge extra plans |
| quickguides | ChatGPT command cheat sheets | Clarify scope; move under SOP operational if formalised |
| schemas | Shared schemas + PII policy | Fill common.json; expand PII_POLICY.md; link to canonical data rules |
| scripts | Governance automation scripts | Add usage docs; add tests; document dependencies; integrate CI |
| security | GDPR + secrets policies | Add RBAC; audit logging; cross-link SOPs; incident response policy |
| sop | Families: compliance, emergency, operational, system, workflow | Populate instances; rehouse orphan SOPs; update INSTANCE_INDEX.md |
| tasks | Backlog + SOP joborders + dashboards | Reconcile with audit WO; link to WOs; automate dashboard; expand tracker.json |
| templates | Repo README template | Add SOP/Plan/WO templates; style guide; link .github templates |
| work-orders | Subsystem WOs + delivery plan | Ensure all link to Phase Plans; apply status markers; expand draft WOs |
| workflows | Contractor lifecycle workflow doc | Cross-link SOPs + diagrams; add governance metadata |
| root docs | README, INDEX, CONTRIBUTING, Master WO, Commit Sync | Update links; refresh INDEX; sync CONTRIBUTING; CI for commit sync |

---
📌 For risks, see [Risk Register](risk_register.md).


---
## Section References (Audit WO Alignment)

- **Section 4 – Risks & Mitigations:** Risks consolidated into [Risk Register](risk_register.md).
- **Section 5 – Acceptance Criteria:** Defines audit completion checks.
- **Section 6 – Priority Guide:** Immediate, Near-term, Later priorities from audit.
- **Section 7 – Governance Rules Audit:** Current, partial, and missing governance controls.

---
