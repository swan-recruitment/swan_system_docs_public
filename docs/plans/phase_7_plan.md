# 🚀 Phase 7 Delivery Plan – Swan Recruitment ERP

This document outlines the detailed delivery plan for **Phase 7 (Control Tower Setup)** of the Swan Recruitment ERP modernization project.  
The Control Tower acts as the orchestration and monitoring layer across all modules, ensuring visibility, reliability, and centralized management.

---

## Phase 7 – Control Tower Setup
**Objective:** Build the **swan-control-tower** to monitor system health, orchestrate workflows, and provide unified reporting across the ERP ecosystem.

### Work Order
- **Control Tower Work Order** → (`work_order_control_tower.md`)

### Must-Have Design Specs
- [ ] System Health Monitor → `docs/design/system_health_monitor.md`  
- [ ] Manual Workflow Trigger API → `docs/design/manual_triggers.md`  
- [ ] Alerting & Notifications → `docs/design/alerts_notifications.md`  
- [ ] Version Visibility Dashboard → `docs/design/version_dashboard.md`  

### Actions
1. **Project Setup**
   - Initialize Control Tower repo (`swan-control-tower`)  
   - Create basic Node.js or Python backend service  
   - Add frontend dashboard (React/Next.js or Streamlit)  

2. **System Health Monitoring**
   - Track status of Firebase Functions, Firestore, Realtime DB, Hosting  
   - Track Contractor Portal uptime and Website availability  
   - Monitor Desktop App sync with Firebase  
   - Log metrics into Firestore/BigQuery  

3. **Manual Workflow Orchestration**
   - Provide admin UI + API to trigger key workflows:  
     - Re-run Contract Generator  
     - Reset contractor account  
     - Force invoice reconciliation  
   - Secure with staff-only access + logging  

4. **Alerting & Notifications**
   - Configure Slack/email alerts for failed functions or sync issues  
   - Notify staff when invoices or timesheets are overdue  
   - Log all alerts for auditing  

5. **Version & Deployment Visibility**
   - Display current deployed version for each repo (via GitHub API + tags)  
   - Show latest successful deployment logs  
   - Highlight repos with pending updates or CI failures  

6. **CI/CD Integration**
   - GitHub Actions pipeline for Control Tower deployment  
   - Automated tests for monitoring + triggers  
   - Deploy to Firebase Hosting or container service (Cloud Run/Docker)  

**Deliverable:** A live Control Tower dashboard for Swan Recruitment staff, providing health checks, workflow controls, notifications, and version visibility.

---

## Combined Deliverable (Phase 7)
By the end of Phase 7, Swan Recruitment will have:  
- A **Control Tower dashboard** monitoring all ERP components.  
- Secure admin workflows to manually trigger and reset processes.  
- Proactive alerts for failures, delays, or sync issues.  
- Clear visibility of system versions and deployment status.  

---

📌 **Next Step After Phase 7:** Begin **Phase 8 – Final Rollout & Continuous Improvement**, focused on staff onboarding, contractor onboarding, and iterative feature enhancements.
