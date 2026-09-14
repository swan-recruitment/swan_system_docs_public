---
title: "Portal Account Setup – Data Flow"
slug: "portal-account-setup-data-flow"
canonical_step_id: "contractor-onboarding/02_portal_account"
owner: "Ben"
status: draft
created: "2025-09-28"
updated: "2025-09-28"
---

> **Breadcrumb:** [SOPs](/docs/sop/README.md) › [Workflows](/docs/sop/workflow/README.md) › [Contractor Onboarding](../) › [02 Portal Account](../02_portal_account/README.md) › Data


# Data Flow – Portal Account Setup

## Source
- ERP contract record (contractor ID, email)

## Transformations
- Generate unique ID  
- Hash password  
- Assign permissions

## Destinations
- Portal DB  
- Email notification system
