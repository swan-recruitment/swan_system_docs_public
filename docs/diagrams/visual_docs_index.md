# 📊 Visual Documentation Index – Swan Recruitment ERP

This index tracks all **Mermaid-based diagrams** created for the Swan ERP project.  
It ensures visual documentation stays consistent, complete, and cross-linked with design specs and phase plans.

---

## ✅ Completed Diagrams
| Diagram | File(s) | Status | Linked To |
|---|---|---|---|
| System Flow Diagram | `swan_erp_flow_diagram.md`, `.mmd`, `.html` | ✅ Complete | Phase 1+2 Plan |
| Firestore & Realtime DB ERD | `swan_erp_erd.md`, `.mmd`, `.html` | ✅ Complete | DB Schema Spec (Phase 2) |

---

## 🟡 Pending Diagrams
| Diagram | File(s) | Status | Linked To |
|---|---|---|---|
| Sequence Diagram – Contract Generator | `swan_erp_sequence_contract.md`, `.mmd`, `.html` | 🟡 Drafting | Contract Generator Spec |
| Module Interaction Map | `swan_erp_module_map.md`, `.mmd`, `.html` | 🟡 Drafting | Control Tower (Phase 7) |
| Deployment Diagram (Optional) | `swan_erp_deployment.md`, `.mmd`, `.html` | ⏸ Deferred | CI/CD Planning |

---

## 📌 Usage Guidelines
- Diagrams live in `/docs/diagrams/` in the `swan_system_docs` repo.  
- Each diagram should exist in three formats:  
  - `.md` → renders on GitHub  
  - `.mmd` → raw Mermaid source for editing  
  - `.html` → standalone preview in browser  
- Cross-link diagrams into:  
  - **Design Specs** (technical detail)  
  - **Phase Plans** (delivery context)  
  - **Work Orders** (dependencies)  

---

## 📅 Maintenance
- Update diagrams whenever schema or workflows change.  
- Mark status as ✅ Complete, 🟡 Drafting, or ⏸ Deferred.  
- Ensure all diagrams are referenced in the **Design Specs Index** or **Phase Plans Index**.  

