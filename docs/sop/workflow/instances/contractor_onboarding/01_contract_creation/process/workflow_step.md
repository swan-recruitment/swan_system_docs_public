---
title: "Contract Creation – Workflow Step"
slug: "contract-creation-workflow-step"
canonical_step_id: "contractor-onboarding/01_contract_creation"
owner: "Ben"
status: draft
created: "2025-09-28"
updated: "2025-09-28"
---

> **Breadcrumb:** [SOPs](/docs/sop/README.md) › [Workflows](/docs/sop/workflow/README.md) › [Contractor Onboarding](../) › [01 Contract Creation](../01_contract_creation/README.md) › Process


# Workflow Step Breakdown – Contract Creation

Generate contractor contracts once a placement is confirmed in CATSone.

## Inputs
- Trigger: Placement accepted in CATSone (ATS webhook).
- Data: Contractor details, Client details, Contract terms.
- Systems: CATSone, Firebase Backend, ERP Contract Generator.

## Actions
1. Webhook triggers Firebase function.  
2. Selects correct contract template.  
3. Populates fields and generates Word doc.  
4. Uploads contract into CATSone.  
5. Creates CSV log record for ERP/T&I.

## Outputs
- Completed contract (Word)  
- ERP CSV log  
- Logs

## Dependencies
- Accurate ATS data  
- Valid templates  
- Backend operational

## Risks
- Wrong template  
- Missing data  
- Upload failure

## Metrics
- Generation < 2 min  
- Error rate < 1%
