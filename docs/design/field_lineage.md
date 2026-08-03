# 🔁 Field Lineage (Top 10 Fields)

This index tracks **source of truth**, **transformations**, **consumers**, and **audit** trails for key fields.

## 1) invoice_number
- **SoT:** Firebase InvoiceCounter
- **Format:** `INV-YYYY-####` (or KSUID in future)
- **Transforms:** Formatting only; uniqueness enforced
- **Consumers:** Portal receipt, Finance export, CT events, Desktop Manager
- **Audit:** Appears in `finance.invoice.generated`, `finance.payment.webhook`, CT runs

## 2) approval_status
- **SoT:** Portal/Backend approval workflow
- **Values:** `pending|approved|rejected`
- **Consumers:** Invoice creation pipeline, CT dashboards
- **Audit:** Timesheet events; backend errors on mismatch

## 3) reconciled
- **SoT:** Finance system
- **Type:** boolean
- **Consumers:** CT dashboards, Finance reports
- **Audit:** Reconciliation import job; daily digest

## 4) contractor_id
- **SoT:** Starter intake (CATSone/Portal)
- **Type:** string (UUID/KSUID)
- **Consumers:** Timesheets, Invoices, CT
- **Audit:** Present on all related records

## 5) client_id
- **SoT:** Starter intake / CRM
- **Type:** string
- **Consumers:** Invoices, Finance mappings
- **Audit:** FK checks in CT

## 6) sage_id
- **SoT:** Finance system
- **Type:** string|null
- **Consumers:** Finance export, reconciliation
- **Audit:** Outbound export logs

## 7) vat_number
- **SoT:** Company master data
- **Type:** string
- **Transforms:** Mask in reports
- **Consumers:** Finance documents
- **Audit:** CT should never carry full value

## 8) total (money)
- **SoT:** Invoice calculation
- **Type:** `{amount_minor:int, currency:string}`
- **Consumers:** Finance export, CT KPIs
- **Audit:** Sum checks, reconciled totals

## 9) created_at
- **SoT:** System write time
- **Type:** ISO datetime
- **Consumers:** SLAs, TTL, retention
- **Audit:** Present on all write paths

## 10) updated_at
- **SoT:** System update time
- **Type:** ISO datetime
- **Consumers:** drift detection, audits
- **Audit:** Change logs, CT runs

