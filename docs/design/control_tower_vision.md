
# 🌐 Control Tower Vision Document
**Location:** `docs/design/control_tower_vision.md`  
**Related:** [Work Order – Control Tower](/swan_system_docs/docs/work-orders/work_order_control_tower.md) • [Phase Plans Index](../plans/phase_plans_index.md) • [Work Order Master](../work_order_master.md)

---

## 1) Executive Summary
The **Control Tower** is the command center for the Swan ERP. It provides **visibility, orchestration, governance, and intelligence** across all subsystems (Firebase backend, Contractor Portal, Website, Payments/Reconciliation, Desktop Manager, etc.).  
This document defines the **why**, **what**, and **how**, and lays out a **multi‑phase roadmap** from MVP to intelligent automation.

**Goals**
- **Reliability:** Detect failures quickly; enable fast recovery.
- **Operability:** One place to observe jobs, systems, versions, and data flows.
- **Control:** Trigger/retry workflows safely with audit, approvals, and RBAC.
- **Insight:** Track KPIs across the contractor lifecycle; surface anomalies.
- **Evolution:** Grow from simple checks to predictive and prescriptive automation.

**Non‑Goals (for MVP)**
- Building a full BI platform (dashboards should be focused on operations, not full finance BI).
- Replacing subsystem UIs (Control Tower is orchestration first; UIs can come later).
- Storing long‑term system of record data (observe/coordinate rather than own).

---

## 2) Context & Personas
**Business context:** Lean recruitment operation delivering engineering talent, with workflows spanning **candidate → contract → timesheet → invoice → payment → reporting**.

**Key personas**
- **Admin (Faye)** – processes timesheets/invoices; needs status, quick retries, and confidence.
- **Ops (Ben)** – oversees systems; needs health, metrics, change visibility, and overrides.
- **Client Liaison (Alex)** – wants summaries/SLAs on delivery; limited, read‑only views.
- **Recruiter/Sales (Craig)** – occasional visibility; limited, read‑only views.
- **Engineer/Developer** – needs deep logs, deploy/version info, and diagnostics.

---

## 3) Requirements

### 3.1 Functional Requirements
1. **Health & Status**
   - Service health (Firebase, Portal, Website, Payments, Integrations).
   - Data‑flow health (e.g., “all expected timesheets received by Monday 10:00”).

2. **Workflow Orchestration**
   - Trigger and chain jobs (e.g., *Starter Flow → Contract Gen → CSV Export → Drive Upload*).
   - Retry with context; backoff and idempotency.
   - Conditional branching (skip invoice if timesheet missing, etc.).

3. **Observability**
   - **Events & Runs:** each job run emits events (start, success, failure, metrics).
   - **Logs:** link to detailed logs (stored in subsystem or central store).
   - **Metrics/KPIs:** time‑to‑contract, invoice cycle time, timesheet compliance rate, failure rates.

4. **Governance**
   - **RBAC** (Admin/Operator/Viewer) and least‑privilege access.
   - **Audit trail** for actions/changes (who/what/when/why/context).
   - **Change visibility:** show current versions/tags per repo; highlight drift from `main`.

5. **Notifications**
   - Slack/Email alerts for failures, SLO breaches, and daily digests.

6. **APIs**
   - REST API for health, runs, triggers, metrics, and configuration.

### 3.2 Non‑Functional Requirements
- **Availability:** 99.5%+ (MVP) → 99.9% (Phase 3).
- **Latency:** Health checks < 2s; trigger ack < 1s.
- **Security:** OAuth/JWT for UI/API; signed webhooks; encrypted secrets.
- **Compliance:** GDPR‑aware logging; data retention & redaction policies.
- **Portability:** Local dev + cloud deploy; minimal vendor lock‑in around orchestration.
- **Cost Awareness:** Prefer serverless/managed for MVP; scale only where needed.

---

## 4) High‑Level Architecture

```mermaid
flowchart LR
  subgraph CT[Control Tower]
    API[REST API (FastAPI)]
    UI[Web UI (optional)]
    SCHED[Scheduler / Job Orchestrator]
    OBS[Observability Collector]
    RBAC[AuthN/AuthZ & Audit]
    CFG[Config & Secrets]
    BUS[Event Bus (in‑proc/queue)]
    STORE[(State Store)]
  end

  subgraph FB[Firebase Backend]
    FAPI[Functions/API]
    FFIRE[Firestore/RTDB/Storage]
  end

  subgraph CP[Contractor Portal]
    CWEB[Frontend]
    CBFF[Backend API]
  end

  subgraph PAY[Payments/Reconciliation]
    PBFF[Payments API/ETL]
  end

  subgraph DESK[Desktop Manager]
    DAPP[Private Desktop App]
  end

  API <---> UI
  API --> SCHED
  SCHED <--> BUS
  OBS --> STORE
  RBAC --> API
  CFG --> SCHED
  SCHED --> FAPI
  SCHED --> CBFF
  SCHED --> PBFF
  API <--> DAPP
  FAPI --> OBS
  CBFF --> OBS
  PBFF --> OBS
```

**Notes**
- **STORE** can be Firestore/SQLite for MVP; migrate if needed.
- **BUS** can be in‑process (Python) initially; later, add a lightweight queue.
- **OBS** ingests events/logs, computes lightweight KPIs, and persists run history.

---

## 5) Component Detail

### 5.1 API (FastAPI)
- **Endpoints** (draft):
  - `GET /health` – CT self‑health.
  - `GET /health/subsystems` – Firebase, Portal, Payments, Website.
  - `POST /triggers/{job}` – run a job (payload includes parameters, reason, correlationId).
  - `GET /runs` / `GET /runs/{id}` – list run history / details.
  - `GET /metrics/kpi` – KPI snapshot (contract time, invoice cycle, etc.).
  - `GET /versions` – versions/tags per repo; drift indicator.
- **Auth** via OAuth/JWT; **Scopes**: `ct.viewer`, `ct.operator`, `ct.admin`.
- **Rate limits** and idempotency keys for triggers.

### 5.2 Scheduler / Orchestrator
- Run book definitions in code (Python) with **idempotent steps**.
- **Chaining:** DAG‑like execution with success/failed branches.
- **Retries:** exponential backoff, max attempts, dead‑letter capture.
- **Time windows:** e.g., timesheet completeness window closes Monday 10:00.

### 5.3 Observability Collector
- **Event model:** `{ts, subsystem, job, runId, level, msg, meta}`.
- **Aggregation:** last‑run status, rolling failure rate, duration histograms.
- **SLO evaluator:** compares metrics to SLO targets, emits alerts.

### 5.4 RBAC & Audit
- **Roles:** Viewer (read‑only), Operator (triggers), Admin (config).
- **Audit events:** `{ts, actor, action, resource, result, reason, diff}`.
- **Approvals:** optional 2‑step approval for high‑impact jobs.

### 5.5 Config & Secrets
- **Config hierarchy:** default → env → secret overrides.
- **Secret storage:** OS env vars in dev; Secret Manager/Vault in prod.
- **Safe logging:** never log secrets; redaction middleware in API.

### 5.6 Data Store
- **Entities** (MVP):
  - `Run` (id, job, status, timings, inputs, outputs, links, actor)
  - `Event` (id, runId, level, subsystem, msg, meta)
  - `KPI` (name, value, period, calcTs, source)
  - `Version` (repo, branch, tag, commit, asOf)
- **Retention:** Events 30–90 days; Runs 180 days; KPIs 365 days (export older to cold storage).

---

## 6) Representative Flows

### 6.1 Starter Flow – Retry with Context
```mermaid
sequenceDiagram
  autonumber
  participant U as Operator (Ben/Faye)
  participant CT as Control Tower API
  participant OR as Orchestrator
  participant FB as Firebase Backend
  U->>CT: POST /triggers/starter-flow {contractorId, reason}
  CT->>OR: enqueue(job="starter-flow", ctx)
  OR->>FB: POST /api/starter-flow {contractorId}
  FB-->>OR: 500 error (missing field)
  OR->>CT: emit failure event + logs
  U->>CT: GET /runs/{id} (view error context)
  U->>CT: POST /triggers/starter-flow {contractorId, fix=fieldX}
  OR->>FB: POST /api/starter-flow {contractorId, fix=fieldX}
  FB-->>OR: 200 OK (contract docs generated)
  OR-->>CT: emit success; update KPIs
```

### 6.2 Timesheet Completeness Gate
- Window closes Monday 10:00 (Europe/London).
- If missing timesheets > threshold → alert Admin; skip invoice generation; open task.

---

## 7) KPIs, SLOs & Error Budgets

### 7.1 Operational KPIs
- **Contract generation lead time** (payload received → docs generated).
- **Invoice cycle time** (timesheet accepted → invoice issued).
- **Timesheet compliance rate** (% weeks with complete submissions by deadline).
- **Job failure rate** (per subsystem, rolling 7d/30d).

### 7.2 SLOs (MVP Targets)
- **Job success rate:** ≥ 98% / 30d.
- **Time to detect failure:** ≤ 5 min (alerts).
- **Time to recover (MTTR):** P50 ≤ 15 min, P95 ≤ 60 min.

### 7.3 Error Budget
- Allocate acceptable failure minutes per month; halt risky releases when exhausted.

---

## 8) Notifications & Escalation
- **Channels:** Slack and Email (configurable).
- **Policies:** 
  - Immediate: job failure, health down, SLO breach.
  - Digest: daily summary (runs, failures, top KPIs).
- **Escalation:** If unresolved after N hours → escalate to Director.

---

## 9) Security, Privacy, Compliance
- **AuthN/Z:** OAuth/JWT + RBAC; signed webhooks for inbound.
- **PII Handling:** minimize; redact logs; avoid storing PII in Events.
- **Data Retention:** see §5.6; export aged data to cold storage.
- **Approvals:** admin‑gated triggers for finance‑impacting jobs.
- **Backups:** daily state backup; tested restore procedure.

---

## 10) Environments & Deployment
- **Envs:** `dev` (local), `staging`, `prod`.
- **CI/CD:** PR checks (lint, tests), version bump, changelog, deploy on tag.
- **Config per env:** endpoints, secrets, alert routes.
- **Rollbacks:** previous tag redeploy; maintain infra as code (IaC optional).

---

## 11) Versioning & Repo Visibility
- **Track** versions for `swan-control-tower`, `swan-firebase-backend`, `swan-contractor-portal`, `swan-website`, etc.
- **Drift indicator:** behind/ahead relative to target branch (`main` or `prod`).

---

## 12) Risk Register (selected)
| Risk | Likelihood | Impact | Mitigation |
|---|:--:|:--:|---|
| Orchestrator complexity grows fast | M | M | Keep MVP small; codify runbook templates; unit tests |
| Alert fatigue | M | M | Tune thresholds; add digest; classify severities |
| Secret sprawl | L | H | Centralise secrets; rotate; least privilege |
| Vendor lock‑in | M | M | Modular abstractions; standard protocols |
| PII in logs | L | H | Redaction middleware; reviews; tests |

---

## 13) Roadmap
### Phase 1 – **MVP Foundations**
- API + Auth • Health checks • Manual triggers • Run history • Versions view

### Phase 2 – **Operational Orchestration**
- Chained jobs • Retry policies • RBAC & audit • Basic dashboard

### Phase 3 – **Monitoring & Reporting**
- Data‑flow checks • KPIs • Anomaly detection • Alerts + digests • Finance view

### Phase 4 – **Intelligence & Automation**
- Predictive maintenance • Recommendation engine • AI validation • Governance workflows

---

## 14) Testing Strategy
- **Unit:** orchestration steps, adapters, KPI calculators.
- **Integration:** end‑to‑end job flows in dev/staging using test doubles.
- **Chaos drills:** inject controlled failures; verify detection/recovery.
- **Security:** auth/perm tests, secret redaction tests.
- **Load:** ensure scheduler and store handle expected concurrency.

---

## 15) Runbooks (Ops Playbooks)
- **Job Retry:** how to locate failed run, inspect logs, re‑trigger safely.
- **Subsystem Health Down:** identification, temporary mitigation, escalation.
- **Release Flow:** tag, deploy, verify, rollback.
- **Access Requests:** grant temporary Operator role, record justification.

---

## 16) Configuration Matrix (excerpt)
| Key | Dev | Staging | Prod |
|---|---|---|---|
| Firebase API URL | http://localhost:PORT | https://staging‑fb/api | https://prod‑fb/api |
| Alerts Slack Channel | #ct‑dev | #ct‑staging | #ct‑ops |
| Digest Time (Europe/London) | 17:30 | 17:30 | 17:30 |
| Timesheet Deadline | Mon 10:00 | Mon 10:00 | Mon 10:00 |

---

## 17) Glossary & Tags
- **#CT** / **#CTM** – Control Tower (main/orchestration).
- **Starter Flow** – Initial pipeline from CATSone payload to contract docs & records.
- **Run / Event** – A single execution + its emitted messages.
- **KPI / SLO** – Metric and target for reliability/operations.
- **Roles:** Viewer / Operator / Admin.

---

## 18) Acceptance Criteria (MVP)
- [ ] Health endpoint reports all subsystems reliably.
- [ ] A manual trigger can run Starter Flow; failures captured with context.
- [ ] Run history persists across restarts; basic filtering works.
- [ ] Version view shows repos + drift relative to target branch.
- [ ] RBAC enforces Viewer vs Operator actions; audit trail records triggers.

---

## 19) Open Questions
- Should Run/Events live in Firestore (shared) or a CT‑local DB?
- Notifications: Slack only or Slack+Email from day one?
- Do we enforce approvals for finance‑impacting triggers in MVP?

---

## 20) Change Log
- **v1.0 (initial):** Vision authored and linked from Work Order.
