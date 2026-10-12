---
doc_type: sop
sop_family: workflow
template: data_flow_mapping
title: "SOP Template: Data Flow & Mapping"
slug: "sop_data_flow_mapping"
workflow: ""
step_number: ""
version: "0.1"
status: draft
owner: "Ben"
reviewers: []
created: "2025-09-27"
updated: "2025-09-27"
tags: ["Workflow"]
links:
  related_sops: []
  diagrams: []
  systems: []
notes: ""
---

> **See also:**  
> - [Workflow Step Breakdown](../../workflow/templates/sop_workflow_step.md)  
> - [Metrics & KPIs](../../workflow/templates/sop_metrics_kpi.md)  
> - [Risk & Control Register](../../workflow/templates/sop_risk_control.md)  
> - [Visual Process Map](../../workflow/templates/sop_visual_map.md)


# SOP Template: Data Flow & Mapping

This template is designed to help document and analyze the **data flow** within a workflow step.  
Use it alongside `sop_workflow_step.md` to fully capture both process and information movement.  

---

## Full Template

### 1. Data Overview
- **Data Name / Entity:**  
- **Step / Workflow Context:**  
- **Brief Description:**  

---

### 2. Purpose & Role
- Why is this data required in the process?  
- How does it support the workflow outcome?  

---

### 3. Sources (Inputs)
- Origin of the data (system, form, file, API, manual entry):  
- Trigger for data creation/collection:  
- Required fields / attributes:  

---

### 4. Transformations
- Does the data change in this step? (validation, formatting, calculations, enrichment)  
- Business rules applied:  
- Key dependencies or mappings (e.g., IDs, keys, lookups):  

---

### 5. Destinations (Outputs)
- Where is the data stored, sent, or displayed?  
- Systems, teams, or files receiving the data:  
- Data format at output (CSV, JSON, DB record, etc.):  

---

### 6. Integrity & Validation
- How is data quality ensured?  
- Checks or validations applied:  
- Error handling if data fails validation:  

---

### 7. Security & Access
- Who can view/edit this data at this step?  
- Sensitive fields? (PII, financials, etc.)  
- Compliance considerations (GDPR, ISO, etc.):  

---

### 8. Risks & Failure Points
- What could go wrong with the data here?  
- Risks of duplication, corruption, or loss:  
- Backup / rollback / audit trail available?  

---

### 9. Metrics & Success Criteria
- How do you know the data flow is correct?  
- Success measures (accuracy %, data timeliness, completeness):  

---

### 10. Notes / Variations
- Exceptions, optional fields, or special cases:  
- Additional comments:  

---

## Quick Checklist

Use this when you want a rapid data flow review without filling in the full template.

- [ ] Data name / entity  
- [ ] Workflow step context  
- [ ] Short description  

**Purpose & Role**  
- [ ] Why is this data needed?  
- [ ] What outcome does it support?  

**Sources (Inputs)**  
- [ ] Where does it come from?  
- [ ] What fields are required?  

**Transformations**  
- [ ] Is it validated, transformed, or enriched?  
- [ ] Any business rules applied?  

**Destinations (Outputs)**  
- [ ] Where does it go next?  
- [ ] In what format?  

**Integrity & Validation**  
- [ ] Are there data quality checks?  
- [ ] How are errors handled?  

**Security & Access**  
- [ ] Who can access/modify?  
- [ ] Any sensitive fields or compliance issues?  

**Risks & Failure Points**  
- [ ] What can go wrong with this data?  
- [ ] Backup or rollback in place?  

**Metrics & Success Criteria**  
- [ ] How do we know the data flow worked?  
- [ ] Any KPIs?  

**Notes / Variations**  
- [ ] Exceptions / special cases?  
- [ ] Comments or lessons learned?  
