Awesome—here’s a clean, end-to-end view of **data workflow across the entire Swan project**, tying together the Portal, Firebase backend, Excel legacy, Finance, Control Tower, Website, and Desktop Manager. I’ll keep this actionable and map it to the docs you already have.

---

# 0) What “flows” through Swan (at a glance)

**Primary streams**

* **Contractor → Timesheet → Invoice → Finance** (core cashflow)
* **Starter/Contract Data** from CATSone/CRM → Contractor record
* **Artifacts** (PDFs, packs, signed docs) via Portal/Email/Desktop → Drive/Firestore
* **Orchestration** metadata via Control Tower (CT events, runs, digests)

**Authoritative systems (by domain)**

* **Contractor/Contract/Timesheet**: Firebase (target state), Excel (legacy tails)
* **Invoices & Payments**: Finance system (Xero/Sage) as SoT; CT mirrors state
* **Artifacts**: Google Drive (archive) + Firestore pointers
* **Orchestration**: Control Tower is the source of truth for *status* and *runs*

---

# 1) End-to-end pipeline (single pass)

1. **Sources / Entry**

   * Portal uploads (timesheets, contractor invoices, packs)
   * Email (legacy intake for some contracts)
   * Starters from CATSone → contractor profile & contract
   * Website (lead/contact forms) → CRM/ops (non-PII events to CT)

2. **Intake & Validation**

   * Schema check (canonical JSON names; alias map applied)
   * File validation (PDF header, size, naming convention)
   * Lightweight anti-duplication (hash + filename pattern)

3. **Identity & Linking**

   * Ensure `*_id` FKs present (`contractor_id`, `client_id`)
   * Assign/validate `invoice_number` (global unique, formatted)
   * Attach artifact pointers (Drive URL + checksum) to Firestore docs

4. **Storage (write-through)**

   * **Firestore** for structured records (contractor/timesheet/invoice/control)
   * **Drive** for files (originals + generated), with Firestore pointer

5. **Transformation**

   * Timesheet → rolled into client invoice (calc totals, VAT, PO)
   * Contractor invoice → cross-checked to Swan invoice
   * Data normalized: Money in minor units, ISO dates, snake_case

6. **Orchestration (CT)**

   * Emit events: `portal.uploaded`, `backend.parsed`, `finance.invoice.generated`, `finance.reconciled`, `desktop.ingest.contract.signed`
   * CT creates *runs* for long ops (contract generation, exports)
   * Daily digest + anomaly checks (missing links, dangling FKs)

7. **Finance**

   * Export Swan invoices to Finance
   * Reconciliation import (bank/payments) → update `reconciled: true`
   * Round-trip state back to CT dashboards and Firestore

8. **Feedback & Closure**

   * Notify contractor/client as needed (Portal notices)
   * Archive lifecycle states (Submitted/Processed/Paid/Archived)
   * Retain 7 years; redact PII in CT payloads per policy

---

# 2) Dataset lifecycles (condensed)

* **Timesheet**: `submitted → accepted → processed → archived`
* **Invoice (Swan)**: `draft/issued → accepted → paid → archived`
* **Finance item**: `raised → reconciled → reported`
* **Contract Pack**: `generated → signed_ingested → archived`

(Expanded state machines and field definitions are in `docs/design/data_flow__EXPANDED.md` and `docs/design/field_lineage.md`.)

---

# 3) System swimlanes (who does what)

```mermaid
flowchart LR
  subgraph Contractor/Staff
    P[Portal] -->|
      timesheet/invoice/PDF
    | FBE[Firebase Backend]
    DM[Desktop Manager] --> FBE
    Email[Email (Legacy)] --> VBA[Excel VBA]
  end

  FBE --> FS[Firestore]
  VBA --> FS
  P --> Drive[(Google Drive)]
  DM --> Drive

  FS --> CT[Control Tower]
  Drive --> CT

  FS --> FIN[Finance System]
  FIN --> CT

  CT --> Dash[Dashboards & Digests]
```

**Roles**

* **Portal**: clean intake, minimal PII in events
* **Firebase**: schema, IDs, transformations, pointers
* **Desktop Manager**: pack generation, signed ingest, offline queue
* **Finance**: definitive payment status; hands back reconciliation
* **CT**: events/runs, QA checks, status visibility, alerts/digests

---

# 4) Data contracts you’ve already standardised (use everywhere)

* **Canonical types** (`Id`, `Money`, `Address`, `ISODate`, `ISODateTime`)
  → `docs/schemas/common/common.json`
* **Naming**: snake_case; foreign keys end with `_id`
* **Money**: `{ "amount_minor": 123456, "currency": "GBP" }`
* **PII/Redaction**: CT events carry IDs + hashes/pointers only
  → `docs/schemas/PII_POLICY.md`
* **Top 10 field lineage**: SoT, transformations, consumers
  → `docs/design/field_lineage.md`

---

# 5) Event taxonomy (minimal, covers the flow)

* **Intake**:
  `portal.uploaded`, `portal.validated`, `excel.timesheet.ingested`
* **Processing**:
  `backend.parsed`, `backend.transform.applied`, `backend.fn.error`
* **Artifacts**:
  `desktop.trigger.contract`, `desktop.ingest.contract.signed`, `artifact.pointer.written`
* **Finance**:
  `finance.invoice.generated`, `finance.export.sent`, `finance.payment.reconciled`
* **Governance**:
  `ct.run.started`, `ct.run.completed`, `ct.anomaly.detected`, `ct.digest.daily`

(*These names map cleanly to CT “runs” and dashboards.*)

---

# 6) Controls & Observability (what to measure)

**Data-quality gates**

* Alias-to-canonical ratio < 1% (post-cutover)
* Zero dangling foreign keys (daily CT job)
* Timesheet ↔ invoice linkage completeness (100%)

**Operational KPIs**

* % portal submissions failing validation (< 2%)
* Invoice auto-match rate (> 90%)
* Reconciliation time (median < 3 days)
* Desktop offline queue age (P95 < 24h)

**Security/Compliance**

* Redaction pass rate (100% CT events)
* Retention policy audits (quarterly)

---

# 7) Today vs Target (how you’ll get there)

**Today (hybrid)**: portal + some email; Firebase + Excel; finance CSV import → CT
**Target (clean)**: portal-only; Firebase replaces Excel; **CT authoritative** for lifecycle; **Finance API** live; automated archival + lineage.

You’ve already documented this in `data_flow__FULL.md` and aligned the WOs to it.

---

# 8) Concrete next moves (high impact, low risk)

1. **Lock the event names** (list above) and add to CT/WO:

   * Add a short “Event Taxonomy” block to **Control Tower WO** and **Firebase Backend WO**.
2. **Add two CT QA jobs** (described in Control Tower WO):

   * Dangling FK scan (daily)
   * Alias usage audit (daily → report in digest)
3. **Portal/Backend**: enforce **Money** and **FK** rules at write-time (reject on violation).
4. **Finance**: agree `invoice_number` uniqueness + format & confirm it’s returned in every reconciliation row.
5. **Desktop Manager**: implement the **manifest + checksum** pattern for every pack & signed ingest (you’ve specified it; just make it a hard rule).

---

## Want me to push any of this into the repo now?

I can:

* Add an **“Event Taxonomy”** section to the **Control Tower** and **Firebase Backend** WOs,
* Create a short `docs/design/event_taxonomy.md` (one-pager),
* Add a `docs/tasks/ct_quality_jobs.md` spec with the two daily QA jobs and success criteria.

Say the word and I’ll wire those changes straight in.
