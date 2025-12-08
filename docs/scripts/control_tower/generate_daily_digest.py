#!/usr/bin/env python3
import datetime

def generate_digest(now=None, stats=None):
    now = now or datetime.datetime.now().isoformat(timespec="minutes")
    stats = stats or {
        "events_today": 123,
        "errors_today": 2,
        "ci_failed": 1,
        "invoices_paid": 7
    }
    md = []
    md.append(f"# Daily Digest ({now})")
    md.append("")
    md.append(f"- Events today: **{stats['events_today']}**")
    md.append(f"- Errors today: **{stats['errors_today']}**")
    md.append(f"- CI failures: **{stats['ci_failed']}**")
    md.append(f"- Invoices paid: **{stats['invoices_paid']}**")
    return "\n".join(md)

if __name__ == "__main__":
    print(generate_digest())
