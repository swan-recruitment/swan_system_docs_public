---
title: "Timesheet & Invoice Submission – Data Flow"
slug: "timesheet-invoice-submission-data-flow"
canonical_step_id: "contractor-onboarding/03_timesheet_invoice_submission"
owner: "Ben"
status: draft
created: "2025-09-28"
updated: "2025-09-28"
---

> **Breadcrumb:** [SOPs](/docs/sop/README.md) › [Workflows](/docs/sop/workflow/README.md) › [Contractor Onboarding](../) › [03 Timesheet Invoice Submission](../03_timesheet_invoice_submission/README.md) › Data


# Data Flow – Timesheet & Invoice Submission

## Sources
- Contractor portal uploads.  
- Email submissions (attachments).  

## Transformations
- Parse submission.  
- Validate contractor ID, contract ID, week number, hours, invoice amount.  
- Normalize file names.  

## Destinations
- ERP: Timesheets table, Invoices table.  
- Archive folder.  

## Integrity & Validation
- Duplicate detection.  
- Schema validation.  
- SLA enforcement.  

## Security
- Protect contractor PII.  
- Store invoices in compliance-controlled folder.  
