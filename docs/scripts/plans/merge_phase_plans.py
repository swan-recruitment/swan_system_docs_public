#!/usr/bin/env python3
import argparse, re, pathlib, sys

REQ_HEADINGS = [
    "## Objectives",
    "## Dependencies",
    "## Entry Criteria",
    "## Exit Criteria",
    "## Risks & Mitigations",
    "## KPIs / Success Measures",
    "## Links",
]

PHASE_HEADER_RE = re.compile(r"^#{1,3}\s*Phase\s+\d", re.IGNORECASE)

def ensure_sections(text: str) -> str:
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

    fixed_blocks = []
    for b in blocks:
        missing = [h for h in REQ_HEADINGS if h not in b]
        nb = b.rstrip()
        for h in missing:
            nb += f"\n\n{h}\n\n- _TBD_"
        fixed_blocks.append(nb + "\n")
    return "\n\n".join(fixed_blocks)

def normalise_links(text: str) -> str:
    text = re.sub(r"\((\s+)", "(", text)
    text = re.sub(r"(\s+)\)", ")", text)
    text = text.replace("\\", "/")
    return text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detailed", required=True)
    ap.add_argument("--canonical", required=True)
    ap.add_argument("--archive", action="store_true")
    args = ap.parse_args()

    detailed = pathlib.Path(args.detailed)
    canonical = pathlib.Path(args.canonical)

    if not detailed.exists():
        print(f"ERROR: {detailed} not found", file=sys.stderr)
        sys.exit(2)

    src = detailed.read_text(encoding="utf-8")
    merged = ensure_sections(src)
    merged = normalise_links(merged)

    canonical.write_text(merged, encoding="utf-8")
    print(f"Wrote canonical: {canonical}")

    if args.archive and detailed.name != "phase_plans_index_detailed.md":
        detailed.rename(detailed.with_name("phase_plans_index_detailed.md"))
        print(f"Archived detailed as: {detailed.with_name('phase_plans_index_detailed.md')}")

if __name__ == "__main__":
    main()
