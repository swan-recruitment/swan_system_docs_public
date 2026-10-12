# Diagrams – Workflow Documentation
**Last Updated:** 2025-09-28 21:23 BST

This folder stores all visual process maps related to the Swan ERP workflows.  
Each diagram must follow the standard naming convention and be linked from the relevant SOP in `/docs/sop/`.  

---

## 📑 Naming Convention

- **wf** → prefix for workflow diagrams  
- **[workflow]** → short workflow name (e.g., `onboarding`, `payroll`, `reporting`)  
- **[step#]** → two-digit step number (`01`, `02`, …)  
- **[name]** → short descriptive tag for the step (`contract_creation`, `timesheet_entry`)  
- **[ext]** → file extension (`.drawio`, `.png`, `.bpmn`, `.svg`)  

### Examples
- `wf_onboarding_01_contract_creation.drawio`  
- `wf_onboarding_01_contract_creation.png`  
- `wf_timesheet_03_invoice_processing.bpmn`  
- `wf_reporting_07_monthly_summary.svg`  

---

## 📂 Storage Rules
- Always keep both the **source file** (`.drawio` or `.bpmn`) and an **exported image** (`.png` or `.svg`).  
- Store all diagrams here in `/docs/diagrams/`.  
- **Link both** in SOPs:  
  - The **image** (`.png` or `.svg`) for readability.  
  - The **source file** for editing.  

---

  ## 🔗 Linking Example (from SOP)
  ### Diagram Reference
  - Source: [/docs/diagrams/wf_onboarding_01_contract_creation.drawio](../diagrams/wf_onboarding_01_contract_creation.drawio)  
  - Image: ![Contract Creation](../diagrams/wf_onboarding_01_contract_creation.png)

---
---
⬅ Return to [Docs Index](../index.md)