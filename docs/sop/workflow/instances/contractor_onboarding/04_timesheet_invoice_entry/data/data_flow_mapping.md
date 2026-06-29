---
title: "Timesheet & Invoice Entry – Data Flow"
slug: "timesheet-invoice-entry-data-flow"
canonical_step_id: "contractor-onboarding/04_timesheet_invoice_entry"
owner: "Ben"
status: draft
created: "2025-09-28"
updated: "2025-09-28"
---

> **Breadcrumb:** [SOPs](/docs/sop/README.md) › [Workflows](/docs/sop/workflow/README.md) › [Contractor Onboarding](../) › [04 Timesheet Invoice Entry](../04_timesheet_invoice_entry/README.md) › Data


# Data Flow – Timesheet & Invoice Entry

## Sources
- Contractor submissions (portal/email).  
- Backend CSV feeds.  

## Transformations
- Validate hours vs contract.  
- Parse invoice details.  

## Destinations
- ERP Timesheets table.  
- ERP Invoices table.  

## Integrity & Validation
- Duplicate detection.  
- Cross-check with contract ID.  
