# 📡 Event Taxonomy — Swan Systems

**Last updated:** 2025-09-27  
**Backlinks:** [Control Tower WO](../work_orders/work_order_control_tower.md) · [Firebase Backend WO](../work_orders/work_order_firebase_backend.md) · [Data Flow (Full)](data_flow__FULL.md)

---

This is the **authoritative list of event names** flowing through Control Tower (CT). Events should be **lowercase**, dot-delimited, and carry **IDs not PII** (see PII policy).

## 1) Intake
- `portal.uploaded` — a contractor uploads a file/form via Portal (metadata only).  
- `portal.validated` — schema/format validation passed.  
- `excel.timesheet.ingested` — legacy Excel intake processed.

## 2) Processing
- `backend.parsed` — Firebase function parsed payload and created/updated records.  
- `backend.transform.applied` — business rules applied (totals, VAT, mappings).  
- `backend.fn.error` — backend function failed (include error code and runRef).

## 3) Artifacts
- `desktop.trigger.contract` — Desktop initiated contract pack generation.  
- `desktop.ingest.contract.signed` — signed contract PDF ingested (pointer + checksum).  
- `artifact.pointer.written` — file pointer stored in Firestore (Drive URL + hash).

## 4) Finance
- `finance.invoice.generated` — Swan invoice created/emitted.  
- `finance.export.sent` — export pushed to finance system.  
- `finance.payment.reconciled` — payment matched; invoice status updated.

## 5) Governance / Orchestration
- `ct.run.started` — CT started a tracked run (idempotent).  
- `ct.run.completed` — CT completed a run (success/failure).  
- `ct.anomaly.detected` — QA job found an issue (dangling FK, alias drift, etc.).  
- `ct.digest.daily` — daily summary posted (counts, failures, KPIs).

---

## Payload Principles
- **IDs only:** `contractor_id`, `client_id`, `invoice_number`, `upload_id`, `run_id`.  
- **Pointers not bytes:** `drive_url`, `checksum_sha256`.  
- **Money:** `{ "amount_minor": int, "currency": "GBP" }` (no floats).  
- **Timestamps:** ISO 8601 `*_at` fields.  
- **No PII** in CT events (see [`PII_POLICY.md`](../schemas/PII_POLICY.md)).

---

## Versioning
- Additions: minor version bump in CT.  
- Renames/removals: breaking change; require migration note in release.

