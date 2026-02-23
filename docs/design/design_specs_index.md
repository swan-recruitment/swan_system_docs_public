# 📚 Design Specs Index – Swan Recruitment ERP

This is the **living index** for all Design Specifications across the Swan ERP system.  
Use it to track which specs are **Drafted / In Progress / Approved / Deferred** and where they live.

> Status keys: 🟡 Drafted · 🟦 In Progress · ✅ Approved · ⏸️ Deferred

---

## 1) Must‑Have Design Specs

| Spec | Repo | Suggested Path | Status | Notes |
|---|---|---|---|---|
| CATSone → Contract Generator (Cloud Function) | `swan-firebase-backend` | `docs/design/contract_generator.md` | 🟡 Drafted | Draft text shared in chat; create file in repo. |
| Timesheet/Invoice Status Sync (Cloud Function) | `swan-firebase-backend` | `docs/design/status_sync.md` |  |  |
| Auth Roles & Claims (Contractor vs Staff) | `swan-firebase-backend` | `docs/design/auth_roles_claims.md` |  |  |
| Firestore + Realtime DB Schema | `swan-firebase-backend` | `docs/design/db_schema.md` |  | Include ERDs/mermaid. |
| Timesheet Entry Module (Desktop App) | `swan-desktop-manager` | `docs/design/timesheet_entry_module.md` |  | Structured forms with validation, batch entry, OCR ingestion and weekly/fortnightly/monthly cadence. |
| Invoice Entry Module (Desktop App) | `swan-desktop-manager` | `docs/design/invoice_entry_module.md` |  | Includes review/approval workflow, aggregation of weekly submissions into monthly invoices, and integration with Accounts API. |
| Expense Entry Module (Portal & Desktop) | `swan-contractor-portal` + `swan-desktop-manager` | `docs/design/expense_entry_module.md` |  | Allow contractors to submit expenses with receipts; staff review and approve; integrate with client invoicing and contractor reimbursement. |
| Invoice Generation & Export | `swan-desktop-manager` | `docs/design/invoice_generation_export.md` |  | PDF/Excel output. |
| Reporting (Pandas → PDF/Excel) | `swan-desktop-manager` | `docs/design/reporting_module.md` |  |  |
| Document Uploads (Portal) | `swan-contractor-portal` | `docs/design/portal_uploads.md` |  | Timesheets, invoices, expenses. |
| Status Dashboard (Portal) | `swan-contractor-portal` | `docs/design/portal_status_dashboard.md` |  | Realtime DB binding. |
| Contractor → Client Invoice Automation | `swan-accounts-integration` | `docs/design/invoice_automation.md` |  |  |
| Payment Status Sync | `swan-accounts-integration` | `docs/design/payment_status_sync.md` |  |  |
| Reconciliation Engine | `swan-accounts-integration` | `docs/design/reconciliation_engine.md` |  |  |
| System Health Monitor | `swan-control-tower` | `docs/design/health_monitor.md` |  |  |
| Manual Workflow Triggers API | `swan-control-tower` | `docs/design/manual_triggers_api.md` |  |  |
| Alerts & Notifications (Slack/Email) | `swan-control-tower` | `docs/design/alerts_notifications.md` |  |  |

---

## 2) Nice‑to‑Have Design Specs

| Spec | Repo | Suggested Path | Status | Notes |
|---|---|---|---|---|
| Firebase Emulator Setup | `swan-firebase-backend` | `docs/design/emulator_setup.md` |  |  |
| Hosting Setup (Portal) | `swan-contractor-portal` | `docs/design/hosting_setup.md` |  |  |
| Hosting Setup (Website) | `swan-website` | `docs/design/hosting_setup.md` |  |  |
| Desktop GUI Skeleton | `swan-desktop-manager` | `docs/design/gui_skeleton.md` |  | PyQt/Tkinter choice. |
| Auth UI Wiring (Portal) | `swan-contractor-portal` | `docs/design/auth_ui_wiring.md` |  |  |
| SEO & Analytics (Website) | `swan-website` | `docs/design/seo_analytics.md` |  | GA4 + sitemap. |

| Email Ingestion & Attachment Module | `swan-firebase-backend` | `docs/design/email_ingestion.md` |  | Ingest emails via IMAP/POP or Gmail API, store attachments in Storage and extract metadata. |
| Digital Signature Integration | `swan-firebase-backend` | `docs/design/digital_signature.md` |  | Integrate with an e‑signature platform to send contracts for signature and store signed PDFs. |
| Client Self‑Service Portal | `swan-website` | `docs/design/client_portal.md` |  | Portal for clients to view invoices, payment status and approve timesheets. |
| Advanced Analytics & BI | `swan-desktop-manager` | `docs/design/analytics_bi.md` |  | Data warehouse and business‑intelligence dashboards for profitability and forecasting. |
| MFA & SSO Authentication | `swan-accounts-integration` | `docs/design/auth_mfa_sso.md` |  | Support multi‑factor authentication and single sign‑on via corporate IdP. |
| Document Search & Tagging Service | `swan-firebase-backend` | `docs/design/document_search_tagging.md` |  | Search index over documents with tagging for quick retrieval and audit. |
| Compliance & Retention Policies | `swan_system_docs` | `docs/design/compliance_retention.md` |  | Define automated archival, deletion and anonymisation rules to meet GDPR and retention requirements. |
| Marketing & Lead Generation | `swan-website` | `docs/design/marketing_lead_generation.md` |  | Define email and telephone marketing strategies to attract new clients; include CRM integration, call tracking, and website as lead capture channel. |
| CRM (Leads, Contacts, Opportunities) | `swan-firebase-backend` | `docs/design/crm_module.md` |  | Design the in‑house CRM data model, UI flows and integrations for tracking companies, contacts, opportunities and interactions. |
| Identity & Compliance Checks | `swan-firebase-backend` | `docs/design/identity_compliance.md` |  | Integrate KYC/AML services to verify contractor documents and store verification results. |
| Contract Template Management | `swan-firebase-backend` | `docs/design/contract_template_management.md` |  | Versioned contract templates with merge fields and approval workflows. |
| Payments & Payroll Integration | `swan-accounts-integration` | `docs/design/payroll_integration.md` |  | Handle contractor payments via bank transfer or payroll provider and expose pay‑slip history. |
| SMS & Messaging Notifications | `swan-control-tower` | `docs/design/sms_notifications.md` |  | Send reminders and alerts via SMS or chat apps (e.g., Twilio, Slack). |
| Scheduling & Calendar Sync | `swan-desktop-manager` | `docs/design/scheduling_calendar_sync.md` |  | Integrate with calendar APIs (Google/Outlook) for interview and contract date scheduling. |
| Knowledge Base & Ticketing | `swan-website` | `docs/design/support_kb_ticketing.md` |  | Provide a support portal with searchable FAQs and ticket submission for contractors and clients. |
| Multi‑currency & Tax Rules | `swan-accounts-integration` | `docs/design/multi_currency_tax.md` |  | Support multiple currencies and configurable tax/VAT rules in invoicing. |
| Data Warehousing & Machine Learning | `swan-control-tower` | `docs/design/data_warehouse_ml.md` |  | Export Firestore data to a warehouse (e.g., BigQuery) for advanced analytics and ML models. |
| Disaster Recovery & Continuity | `swan_system_docs` | `docs/design/disaster_recovery_continuity.md` |  | Define backup, restoration and business continuity procedures across all modules. |
| Mobile Companion App | `swan-mobile-app` | `docs/design/mobile_app.md` |  | A lightweight app/PWA for contractors to submit timesheets and expenses, view approvals and receive notifications. |
| Offline Mode & Sync | `swan-desktop-manager` + `swan-contractor-portal` | `docs/design/offline_sync.md` |  | Implement local caching and queued updates so staff and contractors can work without connectivity and synchronise changes later. |
| Workflow Reminders | `swan-control-tower` | `docs/design/workflow_reminders.md` |  | Automated email/SMS notifications for approaching deadlines, overdue timesheets and escalations. |
| Performance & Feedback Tracking | `swan-control-tower` | `docs/design/performance_feedback.md` |  | Capture metrics such as on‑time submissions and client feedback, and surface them in dashboards. |
| Rate Card & Budget Management | `swan-firebase-backend` | `docs/design/rate_card_budget.md` |  | Manage rate cards, contract budgets and spend caps; alert when limits are reached. |
| Document Viewer & Annotation | `swan-desktop-manager` | `docs/design/document_viewer.md` |  | In‑app preview and annotation of uploaded documents (timesheets, receipts) without downloading. |
| Chatbot & Contextual Help | `swan-website` | `docs/design/chatbot_help.md` |  | Embed a help assistant or chatbot in the portal/desktop app to answer common questions. |
| Slack/Teams Integration | `swan-control-tower` | `docs/design/slack_teams_integration.md` |  | Push control‑tower alerts and workflow updates into team chat channels for quicker response. |
| Schema Validation & Transformation | `swan-firebase-backend` | `docs/design/schema_validation_transformation.md` |  | Cloud Function(s) to validate Firestore writes against JSON schemas and apply derived calculations before persisting or emitting events. |
| Access Audit & PII Redaction | `swan-firebase-backend` | `docs/design/access_audit_pii_redaction.md` |  | Functions to log access events and redact sensitive fields before emitting Control Tower events, in accordance with the PII policy【97822270448558†L15-L34】. |
| Daily Digest & Maintenance Jobs | `swan-control-tower` | `docs/design/daily_digest_maintenance.md` |  | Scheduled functions that generate daily summaries, monitor stale heartbeats, enforce data retention and trigger clean‑up tasks. |

---

## 3) How to use this index

1. **Create the file** at the suggested path inside the target repo.  
2. Paste the **Design Spec Template** and fill it in.  
3. Update the **Status** here (🟡 → 🟦 → ✅).  
4. Link back to the relevant **Work Order** milestone.  

> Tip: Keep specs to **1–2 pages** with a **Mermaid diagram** when helpful.

---

## 4) Design Spec Template (quick link)
- Template filename suggestion: `docs/design/_template.md`
- Contents should match the standard sections:
  - Overview · Inputs & Outputs · Architecture & Flow · Technology · Risks · Testing

---

## 🧭 Vision Docs

**Purpose:** Capture strategic, forward‑looking guides that complement execution‑focused Work Orders.  
Vision docs articulate *why* we’re building something, the *phased evolution* (MVP → Expansion → Intelligence), and the *architectural shape* over time.

**Index**
- **Control Tower Vision** — `docs/design/control_tower_vision.md`  
  - Overview, personas, requirements (functional & non‑functional)  
  - Architecture (Mermaid), component detail, data model  
  - Representative flows, KPIs/SLOs, notifications & escalation  
  - Security & compliance, environments & deployment, versioning  
  - Risks, roadmap, testing strategy, ops runbooks, config matrix  
  - Acceptance criteria & open questions



**See also:** [Vision Docs Index](./vision_index.md)
