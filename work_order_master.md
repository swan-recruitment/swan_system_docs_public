# 🧭 Master Work Order (FULL Governance Edition): Swan Recruitment — Strategy, Delivery & Compliance

**Last updated:** 2025-09-27  

---

## 0) Why this document exists
You already have execution‑ready Work Orders (WOs) for each subsystem. This **FULL** Master Work Order ties them to **business outcomes**, sets **program KPIs**, enforces **governance & compliance**, and lays out **dependency, capacity, and escalation** models so delivery stays predictable as Swan scales.

---

## 1) Strategic Alignment → Business Outcomes
| Subsystem | Strategic Purpose | Primary Outcome | Secondary Outcome |
|---|---|---|---|
| Contractor Portal | Digitise contractor interactions (onboarding, uploads, status) | Faster onboarding; fewer manual touches | Better data quality for invoicing |
| Firebase Backend | Single source of truth + workflow engine | Reliable contract/timesheet lifecycle | Lower maintenance via serverless |
| Website | Lead capture & credibility | More qualified leads | Lower pre‑sales time |
| Finance Integration | Invoice export, payment ingest | Accurate, timely invoicing | Improved cash flow |
| Desktop Manager | Safe local orchestration for staff | Repeatable operations | Fewer production credentials needed |
| Control Tower | Visibility + orchestration + audit | Reduced downtime; faster recovery | Operational metrics & SLOs |
| Excel Migration | De‑risk legacy, unify processes | Eliminate double entry | Audit trail over e‑mail/Excel |
| Visuals & Docs | Shared mental model & standards | Faster onboarding | Fewer architectural regressions |

**Strategic goals (2025–2026):** shorten lead→contract time, reduce invoice cycle time, increase operational reliability (measured via CT SLOs).

---

## 2) Program KPIs (targets & measurement)
| KPI | Target | Measured by | Notes |
|---|---|---|---|
| Contractor onboarding time | ↓ 50% vs legacy | Portal events + CT | From document receipt to “Ready to bill” |
| Timesheet→Invoice accuracy | ≥ 99% | Finance export validations | Parallel run during migration |
| Invoice cycle time (issue→paid) | ≤ 14 days median | Finance events + CT | Tracked as rolling 30d |
| CT event coverage | ≥ 90% of key flows | CT events/type vs expected | Gaps logged as backlog items |
| CI pass rate (protected branches) | ≥ 85% | GitHub Actions | Signals quality gates working |
| Docs link health | 0 broken for 30 consecutive days | Link‑check CI | “Green bar” policy |

> KPIs are reviewed monthly in the governance audit; changes require Owner approval.

---

## 3) Governance Framework (people, rules, lifecycle)

### 3.1 Roles
- **Owner**: Benjamin Ian Pitman — program lead & architect.  
- **Reviewers**: Alex (finance/client), Craig (recruitment), Faye (timesheets).  
- **Contributors**: engineers/contractors/assistants assigned per WO.

### 3.2 RACI (example — Finance Integration)
- **R**: Engineer implementing export/payment ingest  
- **A**: Ben  
- **C**: Alex (finance semantics), Faye (invoice ops)  
- **I**: Craig (upstream workflow visibility)

### 3.3 Change Control
1) PR with WO change → 2) Reviewer sign‑off → 3) Owner approves → 4) Archive snapshot in `docs/work_orders/archive/`.

### 3.4 Lifecycle States
`Draft` → `In Progress` → `Complete` → `Archived`  
- Archived WOs stay indexed with 🔒 tag + date; links must continue to resolve.

### 3.5 Documentation Rules
- Each WO must: **(a)** link back to this Master, **(b)** declare Owner & Status, **(c)** include Acceptance Criteria & Risks, **(d)** reference relevant Visuals.  
- `work_orders_index.md` is authoritative for status/owner/last updated.

---

## 4) Delivery Phases (with sub‑milestones & exits)

### Phase 1 — Foundations
**Objectives:** repos, CI, schema baselines.  
**Sub‑milestones:** (1.1) Repos + branch protections; (1.2) CI green; (1.3) Canonical schemas in `docs/schemas/`.  
**Exit:** portal→backend→Firestore event proven; CI green.  
**Dependencies:** none.

### Phase 2 — Core Operations
**Objectives:** portal uploads, website leads, finance v1, excel migration.  
**Sub‑milestones:** (2.1) Portal e2e upload→invoice; (2.2) Website lead capture; (2.3) Finance export validated in sandbox.  
**Exit:** ≥ 3 full contractor→payment test cases.  
**Dependencies:** P1 complete.

### Phase 3 — Control & Oversight
**Objectives:** CT ingestion, daily digest, desktop triggers, dashboards.  
**Sub‑milestones:** (3.1) Backend+Finance events into CT; (3.2) 08:00 digest; (3.3) Desktop contract.regenerate trigger.  
**Exit:** ≥ 500 events ingested with zero loss; operator run audit visible.  
**Dependencies:** P2 complete.

### Phase 4 — Scale & Optimisation
**Objectives:** RBAC & rotation; replay & DLQ recovery; CT UI skeleton; spectral lint for OpenAPI.  
**Sub‑milestones:** (4.1) Tokens rotated; (4.2) Replay tool; (4.3) CT UI scaffold.  
**Exit:** SLOs met; 30‑day zero‑broken‑links streak.  
**Dependencies:** P3 complete.

### Phase 5 — Data & Insights (future)
**Objectives:** CT analytics views, trend reports, management pack.  
**Exit:** automated monthly “Ops Pack” published from CT data.

### Phase 6 — Resilience & Scale (future)
**Objectives:** disaster recovery, multi‑region posture, performance hardening.  
**Exit:** DR test passes; p95 intake latency < 2m sustained.

---

## 5) Dependency Mapping (blocking vs soft)

**Blocking dependencies (must complete first):**
- Excel Migration validation → Finance Integration go‑live.  
- Finance v1 live → CT triggers that depend on finance data.  
- Backend schemas baseline → Portal/Website feature parity.

**Soft dependencies (parallel ok, cross‑link later):**
- Visuals updates ↔ active WOs.  
- CT UI scaffold ↔ CT API (can trail by one phase).

See diagram: `docs/design/visuals/master_dependencies.mmd`.

---

## 6) Resource & Capacity Planning (lightweight)
| WO | Owner | Reviewers | Est. Effort | Window | Notes |
|---|---|---|---|---|---|
| Firebase Backend | Ben | Craig | 2–3 wks | P1 | Schemas + workflows |
| Contractor Portal | Ben | Craig | 2–4 wks | P1–P2 | Uploads/UX loops |
| Finance Integration | Alex (impl via eng) | Faye | 3–5 wks | P2 | Export + payment ingest |
| Excel Migration | Ben | Faye | 1–2 wks | P2 | Parallel run & diffs |
| Control Tower | Ben | Alex | 3–5 wks | P3 | Ingest, runs, digest |
| Desktop Manager | Ben | Alex | 1–2 wks | P3 | Triggers + views |
| Website | Ben | Alex | 1–2 wks | P2 | Lead capture |
| Visuals & Docs | Ben | — | Ongoing | P1–P4 | Diagrams & indices |

> If the same person is on multiple critical items, time‑slice: 60/20/20 across priorities, or defer non‑blocking work to the next phase.

---

## 7) Escalation & Decision Rights
- **Severity P0** (prod outage, blocked invoicing): escalate to **Owner** immediately; notify Alex for client impact.  
- **Severity P1** (major degradation, risky data mismatch): Owner + relevant Reviewer within 4 business hours.  
- **Severity P2/P3**: track in backlog and address in next sprint/phase.  
- **Decision rights:** Owner is final tie‑breaker after Reviewer input.

---

## 8) Compliance & Auditability (pragmatic)
- **Traceability**: every invoice must be linkable to timesheets & approvals (IDs in events & runs).  
- **Data protection**: redact PII in CT events; store documents in Storage with controlled ACLs.  
- **Retention**: events 180d, runs 365d, systems 90d; backups daily.  
- **Access**: principle of least privilege; service tokens rotated quarterly.  
- **Evidence**: preserve daily digests and CI logs for audit trails.

---

## 9) Communication & Reporting
- **Weekly**: short status note (what shipped, risks, blockers).  
- **Monthly**: governance audit (KPIs vs targets, link health, schema drift).  
- **Quarterly**: board review + archived snapshot + roadmap refresh.  
- **CT Digest**: 08:00 Europe/London daily roll‑up for operations.

---

## 10) Backlog Integration
- All unresolved work funnels to **`docs/tasks/backlog.md`**.  
- Each WO should carry its own TODOs, but canonical planning happens in the backlog.  
- No WO closes with open critical TODOs unless explicitly deferred in backlog.

---

## 11) Quality Gates & Automation
- **Docs**: link‑check CI must pass; visuals exported; backlinks present.  
- **APIs**: OpenAPI (Spectral lint) — tracked in backlog to implement CI step.  
- **Code**: unit/functional tests on PR; protected branches require passing checks.  
- **CT**: HMAC verification, idempotency, DLQ with replay audit (once implemented).

---

## 12) Risk Register (expanded)
| Risk | L | I | Owner | Mitigation |
|---|:--:|:--:|---|---|
| Schema drift across repos | M | H | Ben | Central schemas + CI validation |
| Invoice export mismatch | M | H | Alex | Parallel run, diff reports, sign‑off |
| Alert fatigue in CT | M | M | Ben | Thresholds, dedupe, digest for low‑prio |
| Resource contention (single‑threaded) | H | M | Ben | Time‑slicing; sequence blocking work |
| Broken links in docs | M | M | Ben | Link‑check CI; quarterly audit |
| Secrets leakage | L | H | Ben | Secret manager, rotation, scope reduction |

---

## 13) Program‑Level Acceptance Criteria
- [ ] All WOs are **present, cross‑linked, and lifecycle‑tagged**.  
- [ ] KPIs are baselined, and 3 months of measurements exist.  
- [ ] CT ingests ≥ 90% of key flows; digest runs daily.  
- [ ] Finance: 1 month with **zero manual corrections**.  
- [ ] Docs: 30‑day zero‑broken‑links streak.  
- [ ] Security: token rotation completed; access reviews logged.

---

## 14) Appendices

### 14.1 Relationship & Dependency Diagrams
- Relationships map: `docs/design/visuals/master_relationships.mmd` (see Expanded MWO).  
- Dependency map (this doc): `docs/design/visuals/master_dependencies.mmd`.

### 14.2 Work Orders Index (authoritative)
See: `work_orders_index.md` for live status/owner table.

### 14.3 Glossary
**CT** — Control Tower; **DLQ** — Dead Letter Queue; **SLO** — Service Level Objective.

---

## 15) Related Documents
- [Work Orders Index](../docs/work-orders/work_orders_index.md)  
- [Phase Plans Index](../docs/plans/phase_plans_index.md)  
- Child WOs: Portal · Backend · Website · Finance · Desktop · Control Tower · Excel Migration · Visuals · GitHub Setup

> This **FULL** Master WO binds strategy ↔ delivery ↔ audit. Keep it lean by pushing tactical details into the child WOs and the backlog, but never let this document drift: it defines how Swan delivers reliably.
---

### 📏 Canonical Data Rules (Swan)
- Use **snake_case** field names; FKs end with **`_id`**.
- Money uses `{ "amount_minor": int, "currency": "GBP" }` (no floats).
- Dates = `*_date` (date) and `*_at` (datetime, ISO-8601).
- Import common types from **[`docs/schemas/common/common.json`](../schemas/common/common.json)**.
- Follow **PII redaction** policy in **[`docs/schemas/PII_POLICY.md`](../docs/schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`docs/design/field_lineage.md`](../docs/design/field_lineage.md)**.
- [System Docs Audit WO](work-orders/work_order_system_docs_audit.md)
