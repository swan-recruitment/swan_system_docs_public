# Swan ERP – Chat Updates Summary

This document summarises all updates made during the most recent design and planning session.
 created on 27/09/2025 @ 23:30.00 

---

## 1. New Features Added to Design

- **Email ingestion & attachments**  
  Module for monitoring a mailbox, storing attachments in Firebase Storage and extracting metadata into Firestore.

- **Digital signature integration**  
  Contracts are sent for signing via DocuSign/Adobe Sign. Signed PDFs are stored and linked to contract records.

- **Client self-service portal**  
  Clients can log in to download invoices, approve timesheets, and view payment statuses.

- **Advanced analytics & BI**  
  Data exported to a warehouse/BI tool (e.g., BigQuery, PowerBI) for profitability, forecasting, and KPI dashboards.

- **Search & tagging service**  
  Indexed search for contracts, invoices, and uploads with metadata tagging for auditability.

- **Compliance & retention automation**  
  Scheduled tasks for archival, anonymisation, or deletion of data in line with GDPR.

- **Marketing & lead generation**  
  - Primary focus: targeted email and telephone campaigns.  
  - Supporting role: website credibility content and contact form lead capture.

- **In-house CRM**  
  Firestore-based module for leads, contacts, opportunities, and interactions, linked to contracts and invoices.

- **Timesheet & invoice entry improvements**  
  - Support for weekly, fortnightly, and monthly cadences.  
  - Validation and review workflows.  
  - OCR assistance for uploaded PDFs.  
  - Aggregation of multiple weekly entries into monthly cycles.  
  - Supervisor approval step.

- **Expense entry & reimbursement**  
  Contractors upload expenses with receipts via the portal; staff review/approve in desktop app; approved expenses flow into invoices and payroll.

- **Additional proposed features** (all modular design specs created):  
  - Identity & compliance checks (KYC, right-to-work).  
  - Contract template management and versioning.  
  - Payroll integration (contractor reimbursement).  
  - SMS/messaging notifications.  
  - Scheduling/calendar sync.  
  - Knowledge base & ticketing portal.  
  - Multi-currency and tax support.  
  - Data warehouse & ML exports.  
  - Disaster recovery & continuity.  
  - Mobile companion app (or PWA).  
  - Offline mode & sync.  
  - Workflow reminders and escalations.  
  - Contractor/client performance feedback.  
  - Rate card & budget management.  
  - Document viewer & annotation.  
  - Chatbot/contextual help.  
  - Slack/Teams integration.

---

## 2. Cloud Functions

- Refactored **legacy functions plan** created (`cloud_functions_refactor_plan.md`).  
  Includes:
  - Goals and scope.  
  - Summary of existing functions (ATS webhook, template generation, CSV export, Drive upload).  
  - Refactoring roadmap (split into smaller modules).  
  - Event taxonomy alignment.  
  - PII redaction compliance.  
  - Suggested 10-week timeline.

- **New function specs added**:  
  - Schema validation & transformation.  
  - Access audit logging & PII redaction.  
  - Daily digest & maintenance (heartbeats, data retention).  
  - Payment reconciliation poller.  
  - Lead scoring and follow-up scheduler.  
  - Contract expiry notifier and budget watchdog.

---

## 3. Architecture & Data Model Updates

- Architecture expanded with new bullets for:  
  - Email ingestion.  
  - Digital signature integration.  
  - Expense management.  
  - CRM module.  
  - Validation, audit, and digest functions under System Integration Layer.

- Data models outlined for core Firestore collections:  
  - `contracts`, `contractors`, `clients`, `timesheets`, `invoices`, `expenses`, `uploads`, `events`, `leads`, `contacts`, `opportunities`, `interactions`, `rate_cards`, `budgets`.

- Data flows documented:  
  - CATSone webhook → field mapping → Firestore.  
  - Contractor portal uploads → Firestore + Storage → approvals → invoices.  
  - CSV export and Google Drive integration.  
  - Finance system reconciliation.  
  - Control Tower observability.  
  - CRM and marketing pipeline.  
  - BI export and dashboards.

- **Field mappings**:  
  - `field_mappings.json` created to store ATS → Firestore field mapping.  
  - Contract generator spec updated to reference this mapping.  
  - Trailing underscores and typos fixed.  
  - Sensitive fields flagged for PII handling.

---

## 4. Visuals & Diagrams

- **ERP flow diagram updated** (`swan_erp_flow_diagram.mmd`, `.md`, `.html`):  
  - Added Schema Validation & Transformation under Cloud Functions.  
  - Added Audit & PII Redaction and Daily Digest & Maintenance under Control Tower.  
  - Added Email Ingestion node feeding into Firestore.

---

## 5. Repository Notes

- Main repo path confirmed:  
  `C:\Users\Ben\swan-erp-system`

- Repo packages updated multiple times with new design docs, plans, and diagrams.  
- Latest additions include:  
  - `docs/plans/cloud_functions_refactor_plan.md`  
  - `docs/updates/chat_updates_summary.md` (this document)

---

## 6. Next Steps

- Flesh out design specs for each new module.  
- Prioritise core vs nice-to-have modules for development sequencing.  
- Implement event-driven patterns in refactored functions.  
- Add more detailed entity schemas for Firestore collections.  
- Expand visual diagrams to cover contractor lifecycle end-to-end.

---

## 7. Updated System Overview Diagram

```mermaid
flowchart TD

    %% External Systems
    A[CATSone ATS] -->|Webhook: Candidate Placed| B[Firebase Backend]
    Z[Accounting System] <--> I[Finance Integration]

    %% Firebase Core
    subgraph F[Firebase Backend]
        B --> C[Firestore DB]
        B --> D[Realtime DB]
        B --> E[Cloud Functions]

        %% Core Functions
        E --> V1[Schema Validation & Transformation]
        E --> V2[Field Mapping Loader]
        E --> V3[Document Generator]
        E --> V4[CSV Exporter]
        E --> V5[Drive Uploader]
        E --> V6[Payment Reconciliation]
        E --> V7[Lead Scoring & Follow-up]
        E --> V8[Contract Expiry Notifier]
        E --> V9[Budget Watchdog]

        %% New
        U[Email Ingestion] -->|Attachments & Metadata| C
    end

    %% Contractor Portal + Website
    subgraph W[Portal + Website]
        P[Contractor Portal]
        Q[Client Portal]
        R[Public Website]

        P -->|Timesheets, Invoices, Expenses| C
        P -->|View Status Updates| D
        Q -->|Approve Timesheets, View Invoices| C
        R -->|Lead Capture| L[CRM Leads]
    end

    %% Desktop App
    X[Desktop Manager] -->|Timesheet/Invoice/Expense Entry & Approval| C

    %% CRM & Marketing
    subgraph CRM[CRM & Marketing]
        L[Leads]
        M[Contacts & Opportunities]
        N[Interactions]
        L --> M --> N
    end

    %% Control Tower
    subgraph CT[Control Tower]
        H[Heartbeat Monitor]
        J[Audit & PII Redaction]
        K[Daily Digest & Maintenance]
        O[Observability Dashboards]
        P2[Slack/Teams Notifier]
    end

    %% Analytics
    Y[BI / Data Warehouse] -->|Dashboards & Forecasting| O
    C -->|Export Snapshots| Y
