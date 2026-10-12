# Swan Recruitment – Structure Q&A Checklist (Expanded)

## 1) Company Structure — how is Swan organised?
- [ ] Small boutique agency with a senior-only team.
- [✅] Flat structure with shared responsibilities.
- [✅] Clear role assignments (finance, operations, recruitment, IT).
- [✅] Family-business style culture with tight-knit decision making.
- [ ] Other: ___

## 2) Project Structure — how does Swan manage projects?
- [ ] Projects grouped under the Swan ERP system umbrella.
- [ ] Each repo/module aligned to a specific business function (e.g., Control Tower, Accounts Integration, Contractor Portal).
- [ ] Work is tracked using checklists, work orders, and unit catalogs.
- [ ] Projects evolve in phases (MVP → scaling → automation).
- [✅] Other: Currently we don't really have a structure to manage projects. 

## 3) ERP System — what role will it play?
- [✅] Central backbone connecting recruitment, finance, compliance, and CRM.
- [✅] Reduces manual effort (Excel/Word → automated processes).
- [✅] Ensures compliance and auditability across all workflows.
- [✅] Supports real-time updates for contractors and clients.
- [ ] Other: ___

## 4) Key Systems & Tools — what do we use?
- [✅] ATS: CATSone for sourcing and placement.
- [✅] Firebase (Firestore, Realtime DB, Functions) as ERP hub.
- [✅] Contractor Portal (React/Firebase auth).
- [✅] Operations Desktop App (Python).
- [✅] Accounts API integration.
- [✅] Control Tower (docs + brain suite + unit catalog).
- [✅] Other: Sage 50 accounts, Gmail.

## 5) Repos & Code Structure — how is the ERP built?
- [✅] Multi-repo setup (umbrella root folder + child repos).
- [✅] Each repo documented with README, Project Overview, Unit Catalog, INDEX. 
- [✅] DELTA logs to track changes and syncs across repos.
- [✅ ] Public mirrors for open documentation.
- [ ] Other: ___

## 6) Teams & Roles — who does what?
- [✅] Dedicated recruiters focused on sourcing and placements. Craig
- [✅] Finance/Payroll role handling timesheets, invoicing, pay. Ben
- [✅] Operations/Compliance role ensuring contracts and regulations are followed. - Shared
- [✅] IT/Systems role maintaining ERP, Firebase, GitHub, Control Tower. - Ben
- [✅] Shared leadership and joint decision making.
- [ ] Other: ___

## 7) Control Tower — how does it fit in?
- [✅] Acts as the single source of truth (Brain Suite + Docs).
- [✅] Houses Unit Catalog, Work Orders, and documentation.
- [✅] Golden Rules maintain consistency across all projects.
- [✅] Provides project oversight and coordination between repos.
- [ ] Other: ___

## 8) External Integrations — what else plugs in?
- [✅] E-signature tools (DocuSign, Adobe Sign).
- [✅] Email ingestion (IMAP/Gmail API).
- [ ] Search services (Algolia, OpenSearch).
- [ ] BI/reporting (BigQuery, PowerBI, Looker).
- [ ] Identity/security (MFA, SSO).
- [ ] Other: ___

## 9) Governance & Oversight — how is structure maintained?
- [✅ ] Regular audits of repos and documentation.
- [✅ ] Unit Catalog ensures all components are logged and tracked.
- [✅ ] Golden Rules enforce consistency in terminology and workflows.
- [✅ ] Umbrella snapshot used to keep project state aligned.
- [ ] Other: ___
