---
title: "Payroll & Accounts – Data Flow"
slug: "payroll-accounts-data-flow"
canonical_step_id: "contractor-onboarding/06_payroll_accounts"
owner: "Ben"
status: draft
created: "2025-09-28"
updated: "2025-09-28"
---

> **Breadcrumb:** [SOPs](/docs/sop/README.md) › [Workflows](/docs/sop/workflow/README.md) › [Contractor Onboarding](../) › [06 Payroll Accounts](../06_payroll_accounts/README.md) › Data


# Data Flow – Payroll & Accounts

## Sources
- ERP timesheet records.  
- ERP invoice data.  
- Contractor bank details.  

## Transformations
- Calculate payment (hours × rate).  
- Apply deductions (if any).  
- Format bank payment file.  

## Destinations
- Bank system.  
- ERP finance tables.  
- General Ledger.  

## Validation
- Match against contract rates.  
- Validate bank account.  
