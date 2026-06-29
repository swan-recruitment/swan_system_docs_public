# Swan Recruitment – Operations Q&A Checklist (Expanded)

## 1) Day-to-Day Rhythm — what does a typical workday/week look like?
- [✅] Daily focus on sourcing candidates and managing job orders.
- [✅] Regular contractor communication (queries, onboarding, support).
- [✅] Weekly payroll and invoicing cycles.
- [✅] Daily/weekly check-ins as a small team to align work.
- [✅] weekly/monthly/quarterly finance reporting.
- [ ] Other: ___

## 2) Recruitment Workflow — how is sourcing done?
- [✅] Use of ATS (CATSone) to manage job orders and candidates.
- [✅] Manual sourcing via LinkedIn, CV databases, referrals.
- [✅] Online sourcing via company website and joboards.
- [✅] Client requests trigger manual targeted search and shortlist building.
- [✅] Candidate placements feed directly into contract creation.
- [ ] Other: ___

## 3) Contractor Onboarding — what happens once placed?
- [✅] Contracts generated automatically (via Firebase cloud functions + templates). Backup via desktop management app
- [✅] E-signatures collected using DocuSign/Adobe Sign.
- [✅] Contractor set up on Contractor Portal for timesheets and invoices.
- [✅] Compliance checks (ID, right-to-work, insurance) logged in system.
- [ ] Other: ___

## 4) Timesheet & Invoicing — how are hours/pay handled?
- [✅] Contractors submit timesheets weekly, fortnightly, or monthly.
- [✅] Portal or email ingestion used for submission.
- [✅] OCR/manual entry used for timesheet data capture.
- [✅] Staff review/approve → triggers client invoice + contractor pay.
- [✅] Aggregation for month-end contractors.
- [ ] Other: ___

## 5) Expenses — how are they processed?
- [✅] Contractors upload receipts and claims via Portal or email to swan.accounts@swanrecruitment.com
- [✅] Staff review and approve/reject in Desktop App.
- [✅] Approved expenses rolled into client invoice and reimbursed.
- [✅] Categories, limits, and tax rules enforced automatically.
- [ ] Other: ___

## 6) Payroll — how do we pay contractors?
- [✅] Payroll cycles aligned with client invoicing (weekly/fortnightly/monthly).
- [✅] Cycles always end on a friday. Monthly cycles runs till the last Friday of each month. 
- [✅] If the Friday of a week falls within the month all days from that week are included on that months cycle
- [❓] Approved timesheets → payroll batch creation.
- [✅] Employer NI/pension contributions applied as relevant.
- [✅] Payments made via bank transfer (tracked in ERP).
- [ ] Other: ___

## 7) Finance — how do we handle client billing?
- [✅] Client invoices automatically generated from approved contractor data.
- [✅] Desktop App/Control Tower generates financial reports (outstanding, paid/unpaid).
- [✅] Accounts API sync pushes invoices into accounting system.
- [✅] Clients pay on agreed terms; reminders/escalations tracked.
- [ ] Other: ___

## 8) Compliance & Records — what’s logged daily?
- [✅] Right-to-work checks and ID storage.
- [✅] Insurance and HSE compliance tracking.
- [✅] GDPR: all contractor/client data logged, encrypted, and auditable.
- [✅] Retention policies automate archiving and anonymisation.
- [ ] Other: ___

## 9) Team Operations — how do we run internally?
- [ ] Daily team comms (chat, calls, email).
- [✅] fortnightly operations/finance review.
- [✅] Shared ownership of work across the 4-person team.
- [✅] Ops/finance tasks handled by shared oversight, not siloed.
- [ ] Other: ___

## 10) Reporting — what is reviewed regularly?
- [ ] Contractor activity (hours, placements).
- [ ] Client activity (open contracts, billing, payments).
- [ ] Company KPIs (revenue, placements, cash flow).
- [ ] Operational performance (timesheet delays, error rates).
- [ ] Other: ___
