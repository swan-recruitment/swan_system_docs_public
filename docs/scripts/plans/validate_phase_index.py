#!/usr/bin/env python3
import sys, re, pathlib

REQ_HEADINGS = [
    "## Objectives",
    "## Dependencies",
    "## Entry Criteria",
    "## Exit Criteria",
    "## Risks & Mitigations",
    "## KPIs / Success Measures",
    "## Links",
]

PHASE_HEADER_RE = re.compile(r"^#{1,3}\s*Phase\s+\d.*", re.IGNORECASE)

def check(path: pathlib.Path) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    blocks = []
    current = []
    for ln in lines:
        if PHASE_HEADER_RE.match(ln):
            if current:
                blocks.append("\n".join(current))
                current = []
            current.append(ln)
        else:
            current.append(ln)
    if current:
        blocks.append("\n".join(current))

    missing_total = 0
    for idx, b in enumerate(blocks, 1):
        missing = [h for h in REQ_HEADINGS if h not in b]
        if missing:
            missing_total += 1
            print(f"[Phase block {idx}] Missing: {', '.join(missing)}")
    return 1 if missing_total else 0

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_phase_index.py <path-to-phase_plans_index.md>")
        sys.exit(2)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: {path} not found"); sys.exit(2)
    rc = check(path)
    if rc == 0:
        print("Validation OK: all required headings present.")
    sys.exit(rc)

if __name__ == "__main__":
    main()
