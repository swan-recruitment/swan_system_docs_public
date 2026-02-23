# Canonical Data Rules

```mermaid
flowchart LR
    A[snake_case Fields] --> B[ *_id Foreign Keys ]
    A --> C[ *_date vs *_at ]
    A --> D[ Money Object {amount_minor, currency} ]
    A --> E[ Common Types<br/>common.json ]
    A --> F[ PII Policy<br/>PII_POLICY.md ]
    A --> G[ Field Lineage<br/>field_lineage.md ]
```
---
⬅ Return to [Docs Index](../index.md)
