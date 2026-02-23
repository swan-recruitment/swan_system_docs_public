# Cloud Functions Refactor and Integration Plan

This document provides a comprehensive plan for refactoring the existing Firebase
Cloud Functions (previously used in the legacy recruitment system) and
integrating them into the new Swan ERP architecture.  The aim is to deliver
modular, maintainable functions that align with the updated data models, event
taxonomy and PII policies while supporting the expanded feature set discussed in
prior conversations.

## 1 Goals

The primary goals of this refactor are:

1. **Align with the new data model** – map incoming ATS data into the
   canonical Firestore collections (`contracts`, `contractors`, `clients`,
   `timesheets`, `invoices`, `expenses`, etc.) and avoid using a generic
   `filtered_incoming_data` collection.
2. **Externalise configuration** – move field mappings, template IDs and
   file‑upload settings to configuration files rather than hard‑coding them in
   functions.  This makes updates safer and easier.
3. **Adopt an event‑driven architecture** – emit well‑defined events
   (e.g., `ats.webhook.received`, `backend.parsed`, `finance.invoice.generated`)
   following the event taxonomy【732451832762994†L10-L45】; let downstream
   functions listen for these events instead of chaining Firestore triggers.
4. **Enforce PII handling rules** – ensure that sensitive data is stored only
   in secure collections, that control‑tower events contain IDs rather than
   personal details【97822270448558†L5-L34】, and that redactions/masks are
   applied where required.
5. **Improve observability and resilience** – include structured logging,
   heartbeats and error handling; surface failures to the Control Tower.
6. **Modularise code** – break the monolithic `index.js` into smaller modules
   for clarity and testability.

## 2 Current functions summary

The existing `functions.zip` archive contains the following functions:

| Function | Trigger | Purpose |
|---|---|---|
| **`handleCatsWebhook`** | HTTP | Accepts CATSone XML payloads, maps fields using a hard‑coded dictionary, stores the result in `filtered_incoming_data`, adds a webhook timestamp and UUID, and sends a heartbeat. |
| **`updateTemplateOnCreate`** | Firestore on create | When a document is written to `filtered_incoming_data`, determines which DOCX templates to use based on `contractor_employment_type`, fills them with data and writes the base64 outputs back to the document. |
| **`addWordFileToCATS`** | Firestore on update | Detects when template files have been added to a document and uploads them as candidate attachments via CATSone’s API. |
| **`createCSVOnCreate`** and **`createCSVOnUpdate`** | Firestore on create/update | Build a simple CSV from selected fields of `filtered_incoming_data` and store it in a `csv_files` collection. |
| **`copyCSVToDrive`** | Firestore on write | Uploads CSVs from the `csv_files` collection to a Google Drive folder using service‑account credentials. |
| **Heartbeat helpers** | HTTP & internal | Functions to record operational heartbeats into `system_heartbeats` for monitoring. |

These functions were written as a proof of concept and serve as a good starting
point, but they require significant changes to support the new ERP design.

## 3 Refactoring roadmap

### 3.1 Prepare configuration and schema

1. **Field mapping file**: Move the `FIELD_MAPPINGS` dictionary into a JSON
   configuration (`field_mappings.json`) already present in `swan‑firebase‑backend`.
   Functions should load this file at runtime rather than hard‑coding the
   mappings.  Normalise keys (remove trailing underscores, correct typos) and
   update the mapping whenever the ATS fields change.
2. **Template configuration**: Create a `template_config.json` that maps
   employment types to template IDs and placeholder names.  Store DOCX
   templates in a versioned Firestore collection or Cloud Storage bucket.
3. **Secrets management**: Ensure API keys (CATSone, Google Drive) and service
   credentials are stored in Cloud Functions Config or Secret Manager.  Rotate
   keys regularly and do not commit them to source control.

### 3.2 Redesign ingestion pipeline

1. **Rewrite `handleCatsWebhook` into `atsWebhookHandler`**:
   - Accept only `POST` requests with valid XML.
   - Parse the XML and map fields using `field_mappings.json`.
   - Construct domain objects: `contract`, `contractor`, `client`, `rate_card`,
     etc., based on the new data model.
   - Write these objects into their respective Firestore collections.  If a
     related document already exists (e.g., the contractor), update it
     idempotently.
   - Emit an event (e.g., `ats.webhook.received`) to the Control Tower via
     Pub/Sub or Firestore events, containing only IDs and metadata (no PII)
    【732451832762994†L10-L45】.
   - Record a heartbeat (`module: 'ats-webhook-handler'`) on success.
   - Log errors and emit `backend.fn.error` events as per the event taxonomy.

2. **Separate the template generation into `docGenerator`**:
   - Listen for events or Firestore writes indicating that a new contract
     requires documentation.  Use the template configuration to fetch the
     correct DOCX files and fill them with data.
   - Store generated documents in Cloud Storage or attach them to the relevant
     Firestore document via a pointer (`drive_url` + `checksum_sha256`),
     following the payload principles【732451832762994†L50-L54】.
   - Emit `desktop.trigger.contract` or `artifact.pointer.written` events once
     documents are generated.

3. **Refactor external uploads into `catsAttachmentUploader`**:
   - Detect when a contract document gains a new artifact pointer (e.g., a
     schedule or opt‑out file) and call CATSone’s API to upload the file.
   - Use exponential backoff and retries; log failures and emit
     `backend.fn.error` events when uploads fail.

4. **Remove ad‑hoc CSV generation**: Under the new design, exporting data to
   CSV may be handled by scheduled jobs or by the finance integration.  Keep
   CSV generation out of core functions unless specifically needed for legacy
   migration.

### 3.3 Implement new modules

1. **Timesheet & expense ingestion**: Write Cloud Functions to handle portal
   uploads for timesheets, invoices and expenses.  Each should:
   - Validate the file and metadata; create a `timesheet`, `invoice` or
     `expense` document in Firestore.
   - Link records to the correct `contract`, `contractor` and `client` IDs.
   - Emit `portal.uploaded` and `backend.parsed` events as appropriate.

2. **Approval & batching**: Implement triggers or scheduled functions that
   aggregate approved timesheets/expenses into `invoice` documents,
   respecting weekly, fortnightly or monthly cycles.  Generate invoice PDFs
   and emit `finance.invoice.generated` events when done【732451832762994†L35-L39】.

3. **Email ingestion**: A new HTTP or Pub/Sub function should monitor a
   dedicated mailbox, download attachments, and run them through the same
   validation and ingestion pipeline as portal uploads.  Use the same event
   names (`portal.uploaded`) for consistency.

4. **Digital signature callbacks**: Add a webhook endpoint for your e‑signature
   provider (DocuSign/Adobe Sign) to handle callbacks when a document is
   signed.  Update the relevant `contract` record, store the signed PDF and
   emit a `desktop.ingest.contract.signed` event.

5. **CRM and marketing events**: Implement functions to capture new leads from
   website forms or phone logs, store them in the `leads` collection and emit
   CRM events.  These functions should integrate with the in‑house CRM
   workflow and respect PII and consent rules.

### 3.4 Observability and compliance

1. **Event taxonomy adherence**: Ensure every function publishes events using
   the lower‑case, dot‑delimited naming convention and that payloads include
   only IDs and pointers (no PII)【732451832762994†L10-L55】.
2. **Heartbeat**: All long‑running or scheduled functions should call
   `sendHeartbeat` regularly with appropriate metadata (module, label,
   version).  Heartbeats allow the Control Tower to detect stalled
   components.
3. **Structured logging**: Use a consistent logging format (e.g., JSON) and
   severity levels (info, warn, error).  Include a `correlation_id` (such as
   `webhook_request_id` or `run_id`) so logs can be traced across functions.
4. **Error handling**: Catch exceptions, log them, and emit `backend.fn.error`
   events containing an error code and a `runRef` pointer.  Consider
   implementing a dead‑letter queue for failed writes or uploads.
5. **PII redaction**: Before emitting any event, apply the redaction rules
   defined in the PII policy (e.g., drop or hash email and phone fields,
   mask VAT numbers)【97822270448558†L15-L34】.
6. **Testing and CI/CD**: Write unit tests for each module and set up
   continuous integration to run linting and tests on every commit.  Deploy
   functions via a CI pipeline with environment‑specific configuration.

## 4 Timeline and deliverables

1. **Week 1–2: Preparation and design**
   - Finalise field mappings and template configurations.
   - Draft detailed design specs for each new function (ATS handler, template
     generator, attachment uploader, timesheet/expense handler, etc.).
   - Define the Pub/Sub topics or Firestore collections used for events.

2. **Week 3–4: Core refactor**
   - Implement the `atsWebhookHandler` and deploy it to a staging environment.
   - Refactor heartbeat and logging to use consistent modules across functions.
   - Replace the generic `filtered_incoming_data` collection with proper
     domain collections.

3. **Week 5–6: Template generation and uploads**
   - Implement the `docGenerator` and `catsAttachmentUploader` modules.
   - Store generated docs in Cloud Storage and test uploads to CATSone.
   - Decommission the CSV functions unless needed for migration.

4. **Week 7–8: Additional ingestion flows**
   - Build functions for timesheet, invoice and expense uploads from the portal.
   - Integrate email ingestion and digital signature callbacks.
   - Begin migrating legacy Excel workflows to these new endpoints.

5. **Week 9–10: Observability and polishing**
   - Ensure all functions emit events per the taxonomy and redaction rules.
   - Add automated tests, error handling and retry logic.
   - Conduct end‑to‑end tests with sample data and cut over from the legacy
     functions once validated.

## 5 Conclusion

This plan outlines the steps needed to refactor the legacy Cloud Functions and
integrate them into the modern Swan ERP architecture.  By externalising
configuration, adopting an event‑driven approach, enforcing PII and compliance
rules, and modularising the codebase, the refactored functions will be easier
to maintain, extend and monitor.  Following this roadmap will ensure that
incoming data is processed reliably, downstream systems receive the right
signals, and stakeholders have clear visibility into system health and
performance.