# 📦 Project Delivery Plan – Swan Recruitment ERP System

This document consolidates all individual work orders into a single **Project Delivery Plan** for Swan Recruitment’s ERP modernization project.  
It provides a step-by-step roadmap for delivering each system component in order.

---

## **1. Master Project Work Order**
(From `work_order_master.md`)

- Defines the **overall roadmap** (Foundations → Backend → Apps → Finance → Orchestration).  
- Covers all major subprojects and establishes phased delivery.

---

## **2. Firebase Backend**
(From `work_order_firebase_backend.md`)

- Firebase project setup, Emulator Suite, Firestore & Realtime DB schema, security rules.  
- Cloud Functions for CATSone webhook, contract generator, and status sync.  
- Authentication with role-based access.  
- GitHub Actions CI/CD pipeline.

---

## **3. Desktop App**
(From `work_order_desktop_app.md`)

- Python project for **staff operations cockpit**.  
- GUI framework (PyQt or Tkinter).  
- Firebase Admin SDK integration.  
- Modules: Contracts, Timesheets, Invoices, Reports.  
- Migration of VBA workflows.  
- Packaging for Windows (.exe).

---

## **4. Contractor Portal**
(From `work_order_contractor_portal.md`)

- React/Vite web portal for contractors.  
- Firebase Authentication with restricted roles.  
- Document upload workflows (timesheets, invoices, expenses).  
- Realtime DB dashboard for status tracking.  
- Responsive UI/UX with Firebase Hosting + GitHub Actions.

---

## **5. Website**
(From `work_order_website.md`)

- Public-facing Swan Recruitment website.  
- Pages: Home, About, Services, Contact.  
- Branding, responsive design, accessibility.  
- Contact form integrated with Firebase Functions.  
- Contractor Portal entry point.  
- SEO + analytics setup.  
- Firebase Hosting deployment.

---

## **6. Finance Integration**
(From `work_order_finance_integration.md`)

- Connect ERP to accounting API (Xero, QuickBooks, Sage).  
- Automate contractor invoice → client invoice workflows.  
- Payment status sync back to Firebase and portal.  
- Reconciliation reports (CSV/Excel/PDF).  
- Secure API credentials + audit logging.  
- CI/CD pipeline for integration service.

---

## **7. Excel Migration**
(From `work_order_excel_migration.md`)

- Repo for legacy VBA macros and templates.  
- Documentation of all VBA workflows.  
- Python replacements built into Desktop App.  
- Side-by-side validation against Excel.  
- Decommission and archive Excel system.

---

## **8. Control Tower**
(From `work_order_control_tower.md`)

- Central monitoring & orchestration tool.  
- Health checks for Firebase, portal, website, desktop app.  
- Data integrity verification (Firestore ↔ Realtime DB).  
- Manual workflow triggers + overrides.  
- Version tracking per component.  
- Notifications (Slack, email, logging).  
- Deployment on Firebase Functions or Cloud Run.

---

## **Delivery Flow**
1. Foundations – GitHub, Docs, repo structure.  
2. Backend – Firebase setup.  
3. Apps – Desktop App + Contractor Portal.  
4. Website – Public site + portal entry point.  
5. Finance – Accounting API integration.  
6. Migration – Replace legacy Excel tools.  
7. Control Tower – Central orchestration and monitoring.  

---

✅ This **Project Delivery Plan** provides a single top-level file to track all work orders, ensuring Swan Recruitment’s ERP modernization can be delivered step by step with clear milestones.
