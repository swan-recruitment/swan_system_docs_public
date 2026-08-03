# ✅ Control Tower Quality Jobs (Daily)

**Last updated:** 2025-09-27  
**Backlinks:** [Control Tower WO](../work_orders/work_order_control_tower.md) · [Event Taxonomy](../design/event_taxonomy.md) · [Work Orders Index](../work_orders/work_orders_index.md)

---

## Job A — Dangling Foreign Keys Scan
**Goal:** ensure all `*_id` references resolve (no orphaned links).

**Scope:** `contractor_id`, `client_id`, `invoice_number` across timesheets, invoices, artifacts.

**Logic (pseudocode):**
1. Scan collections for documents containing these keys.  
2. For each key, verify referenced document exists (by ID or index).  
3. Emit `ct.anomaly.detected` with a batch payload of failures.  
4. Include remediation hints (file/link to source document).

**Success criteria:**
- 0 unresolved references.  
- All failures included in `ct.digest.daily` under **Data Integrity**.

---

## Job B — Alias Usage Audit
**Goal:** detect non-canonical field names at ingest (e.g., `invoiceNo` instead of `invoice_number`).

**Input:** CT event logs and latest documents for the day.

**Logic:**
1. Maintain an alias map (e.g., `invoiceNo` → `invoice_number`).  
2. Count occurrences of aliases in the last 24h across events and writes.  
3. Emit `ct.anomaly.detected` if alias ratio ≥ 1%.  
4. Output list of offending paths to the digest.

**Success criteria:**
- Alias ratio < 1% (target near 0% after cutover).  
- Trend graph in CT over time (optional).

---

## Output / Reporting
- Both jobs write to CT store for inclusion in `ct.digest.daily`.  
- Failures are linkable to the offending document/file where possible.

