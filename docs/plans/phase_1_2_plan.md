# 🚀 Phase 1 + Phase 2 Delivery Plan – Swan Recruitment ERP

This document outlines the detailed delivery plan for **Phase 1 (Foundations)** and **Phase 2 (Backend Core)** of the Swan Recruitment ERP modernization project.  
It links Work Orders and Design Specs to clear deliverables.

---

## Phase 1 – Foundations
**Objective:** Establish GitHub structure, repos, and documentation baseline.

### Work Orders
- **Master Project Work Order** → (`work_order_master.md`)  
- **GitHub Setup Work Order** → repo creation, org setup, branch protection, CI basics

### Actions
1. Create **new GitHub organization** (e.g., `swancms`).  
2. Initialize repositories for each major project:  
   - `swan_system_docs`  
   - `swan-firebase-backend`  
   - `swan-desktop-manager`  
   - `swan-contractor-portal`  
   - `swan-website`  
   - `swan-accounts-integration`  
   - `swan-excel-tools`  
   - `swan-control-tower`  
3. Push **Project Delivery Plan** and all **Work Orders** into `swan_system_docs`.  
4. Add **Design Spec Template** + **Design Specs Index** into `/docs/design/`.  
5. Configure **branch protection rules**:  
   - Protect `main` branch  
   - Require PR reviews before merge  

**Deliverable:** GitHub org live with repos, planning docs, and workflows version-controlled.

---

## Phase 2 – Backend Core
**Objective:** Build and deploy the Firebase backend as the central integration layer.

### Work Order
- **Firebase Backend Setup** → (`work_order_firebase_backend.md`)

### Must-Have Design Specs
- [ ] Contract Generator Function → `docs/design/contract_generator.md`  
- [ ] Timesheet/Invoice Status Sync → `docs/design/status_sync.md`  
- [ ] Auth Roles & Claims → `docs/design/auth_roles_claims.md`  
- [ ] Firestore + Realtime DB Schema → `docs/design/db_schema.md`  

### Actions
1. **Firebase Project Setup**
   - Create Firebase project, enable Firestore, Realtime DB, Auth, Functions  
   - Enable Emulator Suite for local testing  

2. **Schema + Security**
   - Define Firestore collections: `contracts`, `contractors`, `timesheets`, `invoices`, `users`  
   - Define Realtime DB nodes: `/timesheetStatus/{contractorId}`, `/invoiceStatus/{contractorId}`  
   - Write baseline security rules (contractor-only access)  

3. **Cloud Functions**
   - Implement **Contract Generator** → triggered by CATSone webhook  
   - Implement **Status Sync** → staff approval updates → Realtime DB → Contractor Portal  

4. **Authentication**
   - Enable email/password login  
   - Assign roles via claims: Contractor vs Staff  
   - Enforce role-based Firestore security  

5. **CI/CD**
   - Add GitHub Actions workflow:  
     - Run emulator tests on PRs  
     - Deploy functions automatically on merge to `main`  

**Deliverable:** A Firebase backend that:  
- Receives CATSone webhooks and generates contracts  
- Stores contracts in Firestore and syncs with CATSone API  
- Updates contractor portal with live timesheet/invoice statuses  
- Provides secure role-based authentication  
- Has automated deployment pipeline via GitHub Actions  

---

## Combined Deliverable (Phase 1 + Phase 2)
By the end of these phases, Swan Recruitment will have:  
- A **fully structured GitHub organization** with repos, docs, and branch policies.  
- A **working Firebase backend** integrated with CATSone, Contractor Portal, and Desktop App workflows.  
- Core data models, authentication, and functions in place for the rest of the ERP system to build on.

---

📌 **Next Step After Phase 2:** Begin **Phase 3 – Desktop App Setup & Excel Migration**.
