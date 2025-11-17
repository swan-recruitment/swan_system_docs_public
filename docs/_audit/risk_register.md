# 🛡 Swan System Docs – Risk Register

**Purpose:**  
This register consolidates risks identified across Phase Plans, Work Orders, SOPs, and Audit findings.  
It provides a single reference point for tracking likelihood, impact, controls, and owners.

---

## Risk Scoring
- **Likelihood (L):** Low (L), Medium (M), High (H)
- **Impact (I):** Low (L), Medium (M), High (H)

---

## Risk Table

| ID | Risk | Source | L | I | Current Controls | Mitigation / Next Steps | Owner | Status |
|----|------|--------|---|---|------------------|-------------------------|-------|--------|
| R-001 | Docs drift across folders | Audit WO | M | H | Audit WO, Phase review cycle | Automate checks via CI | Docs Owner | 🟡 |
| R-002 | SOP families incomplete | Audit WO | H | M | SOP templates exist | Populate instances, track via joborders | Process Owner | 🟦 |
| R-003 | Placeholders left unfilled (schemas, SOPs) | Audit WO | M | M | Templates + schemas exist | Enforce via docs_guardian.py | Tech Lead | 🟡 |
| R-004 | Duplication (FAQ vs SOPs) | Audit WO | M | L | SOP families + FAQ | Merge/retire duplicates | Docs Owner | ⏸ |
| R-005 | Outdated phase plans | Plans Audit | H | H | Phase Plans Index | Refresh and validate content | PMO | 🟦 |
| R-006 | Gaps in security policies (RBAC, audit logging) | Security Audit | H | H | GDPR + Secrets Policy | Draft new policies, link to CT | Security Lead | 🟡 |
| R-007 | Weak integration of governance into CI | Governance Audit | M | H | Scripts exist | Integrate into GitHub Actions | DevOps | 🟡 |

---

## Notes
- Status markers: 🟡 Drafted · 🟦 In Progress · ✅ Approved · ⏸ Deferred  
- Risks should be reviewed monthly in line with Audit WO cadence.  
- Owners should confirm mitigation steps and update status accordingly.

---
