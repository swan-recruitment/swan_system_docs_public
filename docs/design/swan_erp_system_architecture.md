# Swan Recruitment – ERP System Architecture Document

## 1. Overview
Swan Recruitment is a UK-based company specializing in contractual recruitment for design engineers in the energy sector.  
With over 35 years of industry experience and a small but expert 4-person team, Swan is building a **custom recruitment ERP system** to unify and streamline its operations.

This ERP integrates candidate sourcing, contract generation, contractor management, finance, reporting, and a number of other aspects into a **single end-to-end workflow**, using **Firebase** as the backbone.

---

## 2. ERP Module Mapping

### 2.1 Human Resources (HR / Talent Management)
- **CATSone (ATS)**  
  - Manages candidate sourcing, job orders, and placements.  
  - Workflow triggers (e.g., "Candidate Placed") initiate downstream contract creation.  

- **Contractor Portal (Website)**  
  - Each active contractor receives an account.  
  - Features: upload timesheets, invoices, expenses, and track statuses (*Submitted, Awaiting Approval, Paid*).  
  - Linked to Firebase for real-time updates.  

---

### 2.2 Finance & Accounting
 - **Timesheet & Invoice Entry (Manual Input)**  
   - Staff capture contractor timesheets and invoices manually for each live contract, at **weekly**, **fortnightly** or **monthly** cadence.  
   - To minimise errors that impact sales invoices and payroll, the entry interface enforces validation rules (e.g., dates within contract period, correct units/rates) and prompts a **review/approval step** before submission.  
   - For contractors who submit monthly but send all timesheets at once, the system aggregates the weekly entries into a single payroll cycle aligned to the **last Friday of the month**.  
   - The module supports structured entry forms, pre‑populated fields, and can ingest scanned timesheets via **OCR** to suggest hour totals; staff can adjust or correct these suggestions before saving.  
   - Once approved, the system generates client invoices and pushes them to the Accounts API, and updates the contractor’s pay history.  

 - **Expense Entry & Reimbursement**  
   - Contractors submit reimbursable expenses (e.g., travel, materials) via the portal with receipt uploads.  
   - Expenses are stored in a dedicated `expenses` collection linked to the contractor and contract.  
   - Staff review and approve or reject each expense in the Desktop App; approved expenses are rolled into the appropriate client invoice and reimbursed to the contractor.  
   - Expense categories, limits and tax treatment are configurable, and validation rules ensure receipts are attached and dates fall within the contract period.  

- **Operations Desktop App (Finance Oversight)**  
  - Approve/reject contractor invoices.  
  - Update statuses in Firebase → reflected instantly in Contractor Portal.  
  - Generate financial reports (outstanding invoices, paid/unpaid balance).  

  - **Digital Signature Integration**  
    - Integrate with a third‑party e‑signature provider (e.g., DocuSign, Adobe Sign) to manage contract sign‑off.  
    - When a candidate is placed in CATSone, a Cloud Function generates a contract and sends it for signature.  
    - Signed PDFs are stored in Firebase Storage and linked to the contract record.  

---

### 2.3 Operations & Contract Management
- **Operations Desktop App (Core Module)**  
  - Central staff-facing cockpit for contract/assignment management.  
  - Review/edit assignments pulled from Firebase.  
  - Search and access contracts, invoices, and timesheets.  
  - Trigger manual syncs if automated workflows fail.  
   - **Timesheet & Invoice Entry Module:** Provides structured forms for entering weekly, fortnightly or monthly timesheets and invoices.  
     - Highlights expected submission dates and flags missing or overdue timesheets.  
     - Performs real‑time validation (contract dates, hours, rates) and pre‑populates fields based on contract data.  
     - Supports batch entry and aggregation for contractors who submit multiple timesheets at month end.  
     - Includes an optional OCR upload to parse scanned or PDF timesheets and reduce typing.  
     - Allows a supervisor to review and approve entries before they trigger invoice generation and payroll updates.  

   - **Expense Entry & Approval Module:** Enables contractors to submit expense claims with attached receipts and category selection via the portal.  
     - Staff review each claim in the Desktop App, apply policy checks and approve or reject.  
     - Approved expenses are included in the next client invoice and reimbursed to the contractor via the payroll system.  
     - Provides dashboards to track pending, approved and rejected expenses.

- **Assignment Contract Creation**  
  - Triggered when candidate is placed in CATSone.  
  - Firebase Cloud Functions generate contracts from stored templates.  
  - Contracts stored in Firebase and pushed to candidate’s ATS record.  

  - **Email Ingestion & Attachment Processing**  
    - A dedicated email inbox (using IMAP/POP or the Gmail API) listens for incoming timesheets, invoices, signed contracts or other documents sent via email.  
    - Attachments are downloaded automatically, stored in Firebase Storage and parsed by a Cloud Function that extracts metadata (e.g., contractor ID, contract ID, invoice number) and creates corresponding records in Firestore.  
    - Unrecognised or malformed emails are surfaced in the Desktop App for manual review.  

---

### 2.4 CRM & Client Management
- **Client Invoicing**  
  - Client invoices automatically generated from approved contractor data.  
  - Linked with assignment and contractor records.  

  - **Client Self‑Service Portal**  
    - Extend the contractor portal approach to clients, allowing them to log in and view invoices, payment statuses and approve timesheets.  
    - Role‑based access ensures clients see only their own data.  
    - Reduces email traffic and improves transparency for client stakeholders.  

- **Reporting & Analytics**  
  - Contractor activity reports (hours, submissions).  
  - Client activity dashboards (active contracts, billing).  
  - Company KPIs (placements, revenue, cash flow).  

  - **Advanced Analytics & Business Intelligence**  
    - Build a data warehouse or integrate with a BI tool (e.g., BigQuery, Looker, PowerBI) to provide richer insights such as contract profitability, revenue forecasting and pipeline analytics.  
    - Expose these dashboards through the Control Tower or Desktop App to support management decision‑making.  

  - **Marketing & Lead Generation**  
    - Focus on personalised **email and telephone outreach** to attract new clients (not candidates).  
    - Maintain the public website as a credibility anchor and initial contact point, but the primary marketing activities will involve targeted email campaigns and direct phone calls.  
    - Capture leads via the website’s contact forms and telephone enquiries, store them in a CRM or the Control Tower, and use these tools to plan and track follow‑up calls and email sequences.  
    - Use marketing analytics to measure the effectiveness of outreach (open rates, call outcomes) and adjust campaigns accordingly.

  - **In‑house CRM (Lead & Client Management)**  
    - Implement a simple customer relationship management module inside the ERP using Firestore and the Realtime Database.  
    - Track **companies**, **contacts**, **opportunities** and **interactions** (calls, emails, notes) in dedicated collections.  
    - Provide staff interfaces in the Desktop App or Control Tower to create leads, log telephone calls, schedule follow‑ups and update deal stages.  
    - Relate CRM records to contracts and invoices to maintain a unified view of each client’s lifecycle.  
    - Optionally export CRM data to external tools if more sophisticated sales or marketing automation is required in future.

---

### 2.5 System Integration Layer (ERP Backbone)
- **Firebase (Core Hub)**  
  - **Firestore Database:** Stores structured contract and assignment details.  
  - **Realtime Database:** Tracks status updates (e.g., invoice approvals) and pushes them to contractors in real-time.  
  - **Cloud Functions:** Automates workflows, transforms data, integrates with APIs.  

      - **Schema Validation & Transformation:** Custom Cloud Functions validate incoming writes against JSON schemas, compute derived fields (e.g., totals, taxes) and enforce canonical naming before persisting data.  Such functions emit events like `backend.transform.applied` when transformations succeed【732451832762994†L21-L24】.

      - **Access Audit & PII Redaction:** When data flows into the Control Tower, dedicated functions log who accessed which records and automatically redact or mask sensitive fields (e.g., emails, bank details) according to the PII policy【97822270448558†L15-L34】.

      - **Daily Digest & Maintenance Jobs:** Scheduled tasks generate daily summaries of system activity (e.g., counts of timesheets processed, invoices generated), monitor stale heartbeats, and enforce data retention rules by archiving or anonymising data past statutory limits.  These tasks emit digest events (e.g., `ct.digest.daily`) for the Control Tower【732451832762994†L41-L45】.

- **Website Backend**  
  - Administers contractor portal accounts.  
  - Manages authentication and account lifecycle.  

  - **Search & Tagging Service**  
    - Implement a search index (e.g., Algolia or OpenSearch) over uploaded documents and metadata.  
    - Allow staff to locate contracts, invoices and correspondence quickly, and tag documents with status and category metadata for improved reporting and auditability.  

  - **Compliance & Retention Automation**  
    - Enforce GDPR and data‑retention policies automatically: after a specified retention period, documents can be archived or anonymised.  
    - Use Cloud Functions or scheduled jobs to handle archiving, deletion and anonymisation tasks.  

---

## 3. Architecture Diagram (Textual)

```
CATSone (ATS)
   ↓ (Webhook → Firebase Functions)
Firebase (Hub)
   ├── Firestore (Contracts, Assignments)
   ├── Realtime DB (Live Status)
   ├── Cloud Functions (Automation & Integration)
   ↓
Operations Desktop App (Python)
   ├── Contract Management
   ├── Timesheet/Invoice Oversight
   ├── Reporting
   ↓
Accounts API (Finance Integration)

Website
   ├── Contractor Portal (Self-service)
   ├── Backend (Admin)
```

---

## 4. Technology Stack
- **Core Integration:** Firebase (Firestore, Realtime DB, Cloud Functions)  
- **ATS:** CATSone (3rd party SaaS)  
- **Frontend & Portal:** Website (React/Vite frontend + Firebase auth)  
- **Desktop App:** Python (Tkinter/PyQt + Firebase SDKs)  
- **Data Entry:** Excel + VBA macros (short term)  
- **Finance:** Accounts software API integration  
- **Reports & Analytics:** Python (Pandas, Matplotlib, Seaborn)  

 - **Email Ingestion:** IMAP/POP connector or Google Workspace/Gmail API for automatic attachment download.  
 - **Digital Signatures:** Third‑party e‑signature platform integration (DocuSign, Adobe Sign).  
 - **Authentication & Security:** Multi‑factor authentication (MFA) and optional Single Sign‑On (SSO) via a corporate identity provider.  
 - **Search:** Algolia, OpenSearch or equivalent for document indexing and retrieval.  
 - **Advanced Analytics:** BigQuery, Looker, PowerBI or similar BI platforms for dashboards and forecasting.  

---

## 5. Risks & Limitations
- **Excel Dependency:** Timesheet/Invoice entry remains manual-heavy. Long-term migration to Desktop App recommended.  
- **Error Handling:** Cloud Functions require robust retries and logging.  
- **Data Security:** Must ensure compliance with UK/EU data regulations (GDPR). Encryption, audit logs, and secure authentication required.  
- **Single Point of Failure:** Firebase is the central hub. Backup/redundancy strategy needed.  

---

## 6. Roadmap

### Phase 1 – Core Backbone
- Finalize Firebase structure (Firestore + Realtime DB).  
- Implement ATS webhook → Contract creation workflow.  
- Build Desktop App contract management module.  

### Phase 2 – Contractor Workflow
- Deploy Contractor Portal MVP.  
- Link approvals via Desktop App → real-time portal updates.  

### Phase 3 – Finance Integration
- Connect timesheet/invoice entry to Accounts API.  
- Gradual migration of Excel workflows into Desktop App.  

### Phase 4 – Automation & Scaling
- CI/CD pipeline for Firebase Functions.  
- Reporting dashboards in Desktop App.  
- Secure audit logging and compliance framework.  

---

## 7. Summary
This system is a **bespoke ERP for recruitment**, designed for Swan Recruitment’s size and specialization.  
By combining ATS workflows, contract generation, contractor self-service, and financial automation — all tied together via Firebase — Swan achieves the benefits of a full ERP in a lean, cost-effective, and scalable architecture.
