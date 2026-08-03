# Control Tower Dashboards Spec

This document defines the initial dashboards and charts.

## Executive Status
- Card per subsystem with G/A/R and last update timestamp
- Aggregate: % systems green, 7‑day trend

## Event Stream
- Timeline of events with filters: source, type, date range
- Volume chart (hourly/daily), top event types

## Runs
- Success rate, duration percentiles, failure reasons
- Drilldown: run detail with correlated events

## Finance
- Invoices generated vs paid (30d), pending count, average days-to-pay

## CI
- Failed workflows by repo (7d), top failing jobs, link to latest run

## Exceptions
- DLQ depth over time, retries count, top `backend.fn.error` signatures

> Render in the CT UI or export as static report; data pulled from Firestore/Storage.
