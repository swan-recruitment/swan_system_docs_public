# 🚀 Phase 4 Delivery Plan – Swan Recruitment ERP

This document outlines the detailed delivery plan for **Phase 4 (Contractor Portal + Website Setup)** of the Swan Recruitment ERP modernization project.  
It combines both projects since they share hosting, branding, and Firebase integration.

---

## Phase 4 – Contractor Portal + Website Setup
**Objective:** Build the contractor-facing portal and the public-facing website.  
- **Contractor Portal:** Contractors log in, upload timesheets/invoices/expenses, and track status in real time.  
- **Website:** Provides Swan Recruitment’s online presence and acts as the entry point into the Contractor Portal.

### Work Orders
- **Contractor Portal Work Order** → (`work_order_contractor_portal.md`)  
- **Website Work Order** → (`work_order_website.md`)

### Must-Have Design Specs
- [ ] Document Upload Workflow (Portal) → `docs/design/portal_uploads.md`  
- [ ] Status Dashboard (Portal) → `docs/design/portal_status_dashboard.md`  
- [ ] Auth UI Wiring (Portal) → `docs/design/auth_ui_wiring.md`  
- [ ] Hosting Setup (Portal) → `docs/design/hosting_setup.md`  
- [ ] Hosting Setup (Website) → `docs/design/hosting_setup.md`  
- [ ] SEO & Analytics (Website) → `docs/design/seo_analytics.md`  

### Actions
1. **Project Setup**
   - Initialize React/Vite apps for both Portal and Website  
   - Add `.gitignore`, `README.md`, and initial GitHub Actions workflows  

2. **Authentication**
   - Integrate Firebase Auth (email/password, optional Google SSO)  
   - Add role-based restrictions (Contractors only access their own data)  
   - Secure contractor-only Firestore rules  

3. **Contractor Portal Features**
   - **Uploads:** Enable contractors to upload timesheets, invoices, and expenses (files → Firebase Storage, metadata → Firestore)  
   - **Status Dashboard:** Display real-time status updates from Realtime DB (*Submitted → Awaiting Approval → Approved → Paid*)  
   - **Profile Binding:** Ensure each upload is linked to contractor + contract ID  

4. **Website Features**
   - Static pages: Home, About, Services, Contact  
   - Contact form: integrates with Firebase Function to send emails  
   - Contractor Portal login link visible on homepage and nav bar  
   - Apply Swan Recruitment branding and mobile responsiveness  

5. **Deployment**
   - Configure Firebase Hosting for both Portal and Website  
   - Add GitHub Actions pipeline for auto-deploy on `main` branch merges  
   - Set up **staging** and **production** hosting environments  

6. **Testing**
   - Unit tests for React components  
   - Integration tests for Firebase Auth and uploads  
   - Manual testing of contact form and portal login  
   - UAT with a small group of contractors  

**Deliverable:** A secure, real-time Contractor Portal and a public Website hosted on Firebase, integrated with the backend and providing a professional branded online presence.

---

## Combined Deliverable (Phase 4)
By the end of Phase 4, Swan Recruitment will have:  
- A **Contractor Portal** where contractors can log in, upload timesheets/invoices/expenses, and track status.  
- A **public Website** presenting company information and linking to the portal.  
- Firebase Hosting and CI/CD pipelines managing both.  
- Secure and role-based contractor authentication.  

---

📌 **Next Step After Phase 4:** Begin **Phase 5 – Finance Integration (Accounting API + Reconciliation)**.
