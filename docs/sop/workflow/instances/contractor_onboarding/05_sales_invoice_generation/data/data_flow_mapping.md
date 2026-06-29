---
title: "Sales Invoice Generation – Data Flow"
slug: "sales-invoice-generation-data-flow"
canonical_step_id: "contractor-onboarding/05_sales_invoice_generation"
owner: "Ben"
status: draft
created: "2025-09-28"
updated: "2025-09-28"
---

> **Breadcrumb:** [SOPs](/docs/sop/README.md) › [Workflows](/docs/sop/workflow/README.md) › [Contractor Onboarding](../) › [05 Sales Invoice Generation](../05_sales_invoice_generation/README.md) › Data


# Data Flow – Sales Invoice Generation

## Sources
- ERP Timesheet table.  
- ERP Invoice table.  

## Transformations
- Format into Sales Invoice template.  
- Insert invoice number from sequence manager.  

## Destinations
- Client (via email or portal).  
- ERP archive.  
- Finance DB.  

## Validation
- Invoice number uniqueness.  
- Totals reconcile with ERP records.  
