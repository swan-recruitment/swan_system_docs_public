# 🛡️ PII Policy (Swan Systems)

**Purpose:** Define how personally identifiable information (PII) is handled across Portal, Backend, Finance, and Control Tower.

## Handling Rules
- **CT events must not contain direct PII.** Replace with hashes or references.
- **Storage of truth:** PII lives in Firestore secure collections or the finance system, not in CT payloads.
- **Mask for reports:** Where PII-derived business identifiers are needed (e.g., VAT), mask except for last two characters.
- **Access control:** Finance-only data is RBAC limited; logs never include PII values.

## Redaction Table
| Field Pattern         | CT Events Handling                | Source of Truth                    |
|-----------------------|-----------------------------------|------------------------------------|
| `email`               | hash or drop                      | Firestore (secure)                 |
| `phone`               | drop                              | Firestore (secure)                 |
| `bank_account_*`      | drop                              | Finance system                     |
| `ni_number`           | drop                              | Firestore (secure)                 |
| `passport_number`     | drop                              | Firestore (secure)                 |
| `address`             | keep city/country; drop lines     | Firestore                          |
| `vat_number`          | mask (prefix + last 2, e.g. GB******12) | Firestore/Finance           |
| `registered_number`   | keep                              | Firestore/Finance                  |
| `name`                | drop or replace with role label   | Firestore                          |

## Retention
- Invoices & timesheets retained **7 years** (statutory).
- CT events: summarized, non-PII metadata only.

## GDPR
- Right-to-erasure processed via Compliance, subject to statutory retention.

