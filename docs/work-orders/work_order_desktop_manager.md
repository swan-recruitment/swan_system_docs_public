# 🖥️ Work Order — Desktop Manager (Staff App)

**Last updated:** 2025-09-27  
**Backlinks:** [Master WO (Full)](/swan_system_docs/docs/work_order_master.md) · [Work Orders Index](work_orders_index.md)

---

## 1) Purpose & Scope
The **Desktop Manager** is a staff-facing app for Swan operators (Ben, Alex, Faye, Craig) that:
- Generates and manages **contract packs** locally (templates, merges, PDFs, zips).
- Provides **safe local file operations** (staging, previews, signed docs ingestion).
- Works **offline-first**, syncs on reconnect, and reconciles with **Control Tower (CT)**.
- Can **trigger CT operations** (e.g., contract regeneration, invoice/export retries) with audit.
- Ships for **Windows and macOS**, with a **secure auto-update** channel.

Out of scope (v1): contractor-facing features (handled by Portal), rich dashboards (handled by CT UI later).

---

## 2) Users & Roles
- **Operator (default):** Run flows (packs, retries), view local queue, sync with CT.
- **Maintainer:** Configure secrets, template paths, environment, update channel.
- **Viewer (optional):** Read-only (audit history, logs).

RBAC is local (app profiles) + remote (CT role tokens).

---

## 3) Core Flows (step-by-step)

### 3.1 Contract Pack Generation
**Goal:** Produce a contract pack (PDF bundle + zip) from template and data.

**Inputs:**
- Contractor record (id, name, rate, client, start/end, compliance flags).
- Template selection (client standard / role variant).
- Optional annexes (IR35, NDA, bank details form).

**Steps:**
1. **Select Contractor** → search by name/ID or paste `contractor_id`.
2. **Fetch Data** (online): query Firebase/CT for latest canonical fields.  
   **Fetch Data** (offline): use last-synced local cache; show “stale” badge.
3. **Template Resolve** → locate template set; verify placeholders vs data (lint).
4. **Merge** → fill DOCX/ODT placeholders → generate **PDF**.
5. **Assemble Pack** → include annexes; generate **zip**; compute checksums.
6. **Sign/Approve** → optional e-sign webhook or manual sign placeholder.
7. **Emit Event** → `desktop.trigger.contract` to CT with `runId`; attach pack manifest.
8. **Store Locally** → write to **staging** folder with deterministic path:
   - `~/SwanDesktop/staging/{{contractor_id}}/{{YYYY-MM-DD}}/pack.zip`

**Outcomes:**
- Local pack in staging.
- CT **run** created with audit trail.
- Optional upload to Drive (if online).

**Errors:** template mismatch, missing fields, PDF conversion failure → logged locally, event to CT DLQ if online.

---

### 3.2 Local File Ops (ingest signed docs)
**Goal:** Validate and ingest signed contract PDFs back into system of record.

**Steps:**
1. Drop **signed PDFs** into `~/SwanDesktop/incoming/` (watcher).
2. Validate **file name pattern** (`{{contractor_id}}_signed_{{date}}.pdf`), size, PDF header.
3. **Associate** with existing run or contractor; compute SHA256 checksum.
4. **Upload** to Drive and write **pointer** to Firebase (or queue if offline).
5. Emit `desktop.ingest.contract.signed` event to CT with metadata (no PII file bytes).

**Outcomes:** signed document archived; status updated; run closed if all artifacts complete.

---

### 3.3 Offline Mode & Sync
- **Local queue** for: events (to CT), Drive uploads, Firebase writes.
- **Conflict rules:** server wins for canonical fields; local only for file artifacts.
- **Sync policy:** exponential backoff; on success, reconcile and mark “synced” with timestamps.
- **Visibility:** “Offline” banner; per-item sync status; retry button.

---

### 3.4 CT Trigger Integration
**Allow-list triggers** callable from Desktop:
- `contract.regenerate` (inputs: `contract_id` or `contractor_id`).  
- `finance.export.retry` (inputs: `invoice_number`).  
- `portal.notify.retry` (inputs: `contractor_id`).

**Security:** Desktop signs requests with CT **Bearer token** + **HMAC** over body.  
**Audit:** CT creates `runId`; Desktop stores `runRef` and links artifacts/logs.

---

## 4) Architecture

### 4.1 App Stack
- **Shell:** Electron (Windows/macOS) or Tauri (leaner, Rust core).  
- **UI:** React + Tailwind.  
- **Runtime:** Node.js + Rust/Python helpers for PDF/zip.  
- **Local DB:** SQLite (via better-sqlite3) to store cache/queue/manifests.  
- **IPC:** Main/renderer for file ops; background job worker.

### 4.2 File Layout (local)
```
~/SwanDesktop/
  staging/                # generated packs awaiting approval/upload
  incoming/               # watched folder for signed PDFs
  cache/                  # contractor snapshots, template manifests
  queue/                  # pending events/uploads
  logs/                   # local logs (rotated, redacted)
  config.json             # environment, endpoints, tokens
```

### 4.3 Templates
- Stored in Drive or repo; synced down to `{cache}/templates/` with **version manifest**.  
- Placeholder syntax: `{{ field_name }}` using canonical names.  
- **Template Lint** checks all placeholders exist in data snapshot.

### 4.4 Security
- Tokens stored using OS keychain (macOS Keychain / Windows Credential Manager).  
- Local at-rest encryption for `config.json` secrets.  
- No raw PII in CT events; only IDs and pointers/hashes.  
- Checksum every artifact; log immutable manifest entries.

---

## 5) Packaging & Updates

### 5.1 Packaging
- **Windows:** MSI via electron-builder/tauri-bundler; signed with Swan cert.  
- **macOS:** `.dmg` notarised app; auto-updater enabled; signed with Developer ID.

### 5.2 Auto-update strategy
- Provider: GitHub Releases (private) or self-hosted endpoint.  
- **Channels:** `stable` (default), `beta` (opt-in).  
- **Safety:** staged rollout (10% → 50% → 100%), rollback if error rate > threshold.

### 5.3 Versioning
- Semantic: `MAJOR.MINOR.PATCH`.  
- Show current version and channel in app footer; allow manual “Check for updates”.

---

## 6) Telemetry & Logging
- Local structured logs (JSON) with rotating files.  
- CT **events** for key actions: `desktop.trigger.contract`, `desktop.ingest.contract.signed`, `desktop.error`.  
- Optional Sentry for crash reporting (no PII).  
- Daily summary appended to CT digest (count of runs, failures, retries).

---

## 7) Non-Functional Requirements
- **Reliability:** No data loss in offline queues; resume-safe.  
- **Performance:** Pack generation < 10s typical; UI responsive under 1k cached records.  
- **Security:** Tokens & secrets never written in plaintext; PII redaction for CT events.  
- **Usability:** Keyboard shortcuts for common actions; clear statuses; undo for destructive ops.

---

## 8) Acceptance Criteria
- [ ] Generate a contract pack end-to-end with current templates (Windows + macOS).  
- [ ] Ingest signed PDF from `incoming/` → Drive + Firebase pointer updated.  
- [ ] Offline queue survives app restarts; reconciles on reconnect.  
- [ ] CT trigger calls succeed with HMAC; `runId` visible in Desktop.  
- [ ] Auto-update works on both OSes with signed artifacts.  
- [ ] Logs redact PII; CT daily digest summarises Desktop activity.

---

## 9) Risks & Mitigations
- **Template drift** → Lint on every merge; version manifest; fail fast.  
- **File watcher false positives** → Hash-based dedupe; debounce writes.  
- **Update failures** → Staged rollout; offline installer fallback.  
- **Queue corruption** → SQLite WAL, checksums, repair routine; export queue to file.  
- **Secrets leakage** → OS keychain; encrypted config; least privilege tokens.

---

## 10) Smoke-Test Plan (scriptable)
**Goal:** Validate core scenarios locally before shipping.

1. **Pack generation (happy path)**  
   - Input: sample contractor `ctr_demo_001`; template `client_std_v1`.  
   - Expect: `staging/.../pack.zip`, CT `runId` created, manifest written.

2. **Signed ingest**  
   - Drop `ctr_demo_001_signed_2025-10-01.pdf` into `incoming/`.  
   - Expect: upload to Drive (or queued), Firebase pointer written, event to CT.

3. **Offline queue**  
   - Disable network → generate pack; should be queued.  
   - Re-enable → queue flushes; CT run visible.

4. **CT trigger**  
   - Run `contract.regenerate` with `contract_id=K123`.  
   - Expect: HTTP 202, `runId`, events attached.

5. **Auto-update dry run**  
   - Point to `beta` channel with newer version; confirm update and rollback path.

---

## 11) Implementation Notes
- Prefer **Tauri** for footprint/perf/security; fall back to Electron if ecosystem dictates.  
- PDF gen: `libreoffice-headless` or `pdf-lib` for templating; measure both.  
- Watcher: chokidar (Electron) / tauri-plugin-fs-watch (Tauri).  
- Local DB: better-sqlite3 (Electron) / sqlx (Tauri).

---
---

## This Work Order Emits / Consumes (Event Taxonomy)
See [Event Taxonomy](../design/event_taxonomy.md) for full definitions and payload rules (IDs only, pointers not bytes, Money in minor units, ISO timestamps, **no PII**).

**Emits (Desktop Manager):**
- `desktop.trigger.contract` — operator initiated contract pack generation (includes `run_id`).
- `desktop.ingest.contract.signed` — signed PDF ingested; checksum + pointer attached.
- `artifact.pointer.written` — when Desktop writes pointers via Backend (if applicable).
- `backend.fn.error` — surfaced by Backend for Desktop-originated failures.

**Consumes (Desktop Manager):**
- `ct.run.started` / `ct.run.completed` — display run progress & results inside the app.
- `backend.transform.applied` — confirmation that template merge/transform completed.

**Notes:**
- Desktop never sends raw file bytes in events; it writes artifacts to Drive and emits pointers with checksums.

### 📏 Canonical Data Rules (Swan)
- Use **snake_case** field names; FKs end with **`_id`**.
- Money uses `{ "amount_minor": int, "currency": "GBP" }` (no floats).
- Dates = `*_date` (date) and `*_at` (datetime, ISO-8601).
- Import common types from **[`docs/schemas/common/common.json`](../schemas/common/common.json)**.
- Follow **PII redaction** policy in **[`docs/schemas/PII_POLICY.md`](../schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`docs/design/field_lineage.md`](../design/field_lineage.md)**.
