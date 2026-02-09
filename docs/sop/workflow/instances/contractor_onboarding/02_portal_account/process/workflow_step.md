---
title: "Portal Account Setup – Workflow Step"
slug: "portal-account-setup-workflow-step"
canonical_step_id: "contractor-onboarding/02_portal_account"
owner: "Ben"
status: draft
created: "2025-09-28"
updated: "2025-09-28"
---

> **Breadcrumb:** [SOPs](/docs/sop/README.md) › [Workflows](/docs/sop/workflow/README.md) › [Contractor Onboarding](../) › [02 Portal Account](../02_portal_account/README.md) › Process


# Workflow Step Breakdown – Portal Account Setup

Provision portal account once contract exists.

## Inputs
- Contract record; contractor name/email

## Actions
- Backend receives signal  
- Creates account with unique ID  
- Hashes password, assigns role  
- Sends welcome email

## Outputs
- Active account  
- Email delivered
