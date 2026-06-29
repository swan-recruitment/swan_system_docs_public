# 🚀 Phase 3 Delivery Plan – Swan Recruitment ERP

This document outlines the detailed delivery plan for **Phase 3 (Desktop App Setup & Excel Migration)** of the Swan Recruitment ERP modernization project.  
It links Work Orders and Design Specs to clear deliverables.

---

## Phase 3 – Desktop App Setup & Excel Migration
**Objective:** Develop the **swan-desktop-manager** app as the internal operations cockpit and migrate all legacy Excel/VBA workflows into Python.

### Work Orders
- **Desktop App Work Order** → (`work_order_desktop_app.md`)  
- **Excel Migration Work Order** → (`work_order_excel_migration.md`)

### Must-Have Design Specs
- [ ] Timesheet Entry Module → `docs/design/timesheet_entry_module.md`  
- [ ] Invoice Entry Module → `docs/design/invoice_entry_module.md`  
- [ ] Invoice Generation & Export → `docs/design/invoice_generation_export.md`  
- [ ] Reporting Module (Pandas → PDF/Excel) → `docs/design/reporting_module.md`  

### Actions
1. **Project Setup**
   - Initialize Python repo structure (`src/`, `tests/`, `requirements.txt`)  
   - Configure virtual environment + CI tests  

2. **GUI Skeleton**
   - Choose GUI framework (PyQt recommended for modern UI)  
   - Implement navigation bar: Contracts, Timesheets, Invoices, Reports  

3. **Firebase Integration**
   - Add Firebase Admin SDK + service account credentials  
   - Build data access layer (`firebase_service.py`)  
   - Connect app to Firestore + Realtime DB for live updates  

4. **Excel Migration**
   - Export all VBA macros from legacy Excel system  
   - Document VBA workflows in `swan-excel-tools` repo  
   - Rebuild workflows as Python modules inside Desktop App  
   - Ensure Firestore replaces file-based storage  

5. **Core Modules**
   - **Timesheet Entry:** staff can enter contractor hours → Firestore  
   - **Invoice Entry:** staff can record contractor invoices → Firestore  
   - **Invoice Generation:** app generates client invoices (PDF/Excel)  
   - **Reports:** summary reports (Pandas → CSV/Excel/PDF export)  

6. **Testing**
   - Compare Python outputs with legacy Excel for same input data  
   - Add regression tests for timesheet + invoice workflows  
   - Mock Firestore in test suite  

7. **Packaging & Distribution**
   - Use PyInstaller to build `.exe` for staff machines  
   - Create installer + usage documentation  

**Deliverable:** A production-ready Desktop App that replaces Excel for timesheet and invoice entry, integrates directly with Firebase, and provides reporting.

---

## Combined Deliverable (Phase 3)
By the end of Phase 3, Swan Recruitment will have:  
- A working **Desktop App** for internal staff.  
- Legacy Excel/VBA workflows fully retired and replaced with Python modules.  
- Client invoices and reports generated directly from the system.  
- Staff using a consistent, GUI-based operations cockpit.  

---

📌 **Next Step After Phase 3:** Begin **Phase 4 – Contractor Portal + Website Setup**.
