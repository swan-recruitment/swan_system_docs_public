# Contractor Workflow – From Onboarding to Reporting

This document describes the main end-to-end workflow in the Swan ERP system, beginning at the CATSone webhook and ending with reporting and analytics.

---

## Workflow Stages

### 1. ATS → Contract Creation
- **Trigger:** CATSone sends “candidate placed” webhook.
- **Functions:** ATS Webhook Handler parses payload, applies field mappings, writes contractor + contract records, emits `ats.webhook.received`.
- **Outputs:** Contractor + contract records in Firestore, Control Tower logs.

---

### 2. Contract Document Generation & Portal Account
- **Functions:** Document Generator produces contract DOCX, sends to e-signature service, saves signed PDF to Storage. Emits `contract.document.signed`.
- **Portal:** Contractor Portal account created, welcome email sent.
- **Outputs:** Active contractor portal account, signed contract linked to record.

---

### 3. Timesheet & Invoice Submission (Contractor)
- **Portal:** Contractor submits weekly/fortnightly/monthly timesheets and invoices.
- **Data:** Stored in Firestore (`timesheets`, `invoices`, `uploads`) with receipts in Storage.
- **Functions:** Validation, OCR assist, emits `portal.uploaded`.
- **Outputs:** Pending submissions visible to staff in Desktop Manager.

---

### 4. Timesheet & Invoice Entry (Staff)
- **Desktop Manager:** Staff manually enter emailed/paper submissions, review portal entries, batch monthly submissions.
- **Functions:** Schema validation, approval workflow, emits `finance.timesheet.approved` or `finance.invoice.approved`.
- **Outputs:** Approved records ready for invoicing and payroll.

---

### 5. Sales Invoice Generation
- **Functions:** Invoice Generator aggregates approved timesheets/expenses into invoices, emits `finance.invoice.generated`.
- **Integration:** Finance Integration pushes invoices to external accounts system (e.g., Xero/Sage).
- **Data:** Invoice records updated with `sage_id` and status.
- **Outputs:** Client receives invoice, invoice status visible in Control Tower.

---

### 6. Payroll / Accounts
- **Functions:** Payment Poller queries accounting API, updates invoices/expenses, triggers payroll payments, emits `finance.payment.reconciled`.
- **Outputs:** Contractors reimbursed, payment statuses visible in Contractor Portal.

---

### 7. Reporting & Observability
- **Control Tower:** Ingests all events, monitors anomalies, generates daily digest KPIs, dashboards.
- **Analytics Exporter:** Exports Firestore data to BI warehouse for deeper analysis.
- **Outputs:** Management visibility on contracts, invoices, performance, and compliance.

---

## Visual Diagram

```mermaid
flowchart TD
    A[CATSone ATS] -->|Candidate Placed Webhook| B[ATS Webhook Handler]
    B --> C[Firestore: Contractors + Contracts]
    B --> CT1[Control Tower Logs]

    C --> D[Document Generator]
    D --> E[E-signature Service]
    E --> F[Signed Contract PDF in Storage]
    D --> P[Contractor Portal Account]

    P --> G[Contractor Submits Timesheets/Invoices]
    G --> H[Firestore: Timesheets, Invoices, Uploads]

    H --> I[Desktop Manager Review/Approval]
    I --> J[Approved Records]

    J --> K[Invoice Generator]
    K --> L[Client Invoice PDF/CSV]
    K --> ACCT[Accounts System]

    ACCT --> M[Payment Poller]
    M --> N[Payroll/Contractor Payment]

    J --> CT2[Control Tower Events]
    ACCT --> CT3[Control Tower Events]
    M --> CT4[Control Tower Events]

    N --> R[Reporting & Analytics]
    CT2 --> R
    CT3 --> R
    CT4 --> R
