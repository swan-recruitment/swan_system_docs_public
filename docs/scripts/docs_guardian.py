#!/usr/bin/env python3
"""
Docs Guardian: lightweight checks to keep critical docs and indexes consistent.
Exits non-zero on failure.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # repo root
errors = []

def path(p: str) -> Path:
    return ROOT / p.replace("/", os.sep)

# ---- Checks ----

def check_exists(label, rel_path):
    p = path(rel_path)
    if not p.exists():
        errors.append(f"[MISSING] {label}: {rel_path}")
    return p

def check_readme_links():
    targets = [
        ("Phase Plans Index", "docs/plans/phase_plans_index.md"),
        ("Work Order Master", "docs/work_order_master.md"),
        ("ERP System Architecture", "docs/diagrams/swan_erp_system_architecture.md"),
        ("Visual Docs Index", "docs/diagrams/visual_docs_index.md"),
        ("Control Tower Vision", "docs/design/control_tower_vision.md"),
        ("Vision Docs Index", "docs/design/vision_index.md"),
    ]
    readme = path("README.md").read_text(encoding="utf-8")
    for label, rel in targets:
        if label in readme:
            check_exists(label, rel)

def check_design_index():
    idx = path("docs/design/design_specs_index.md").read_text(encoding="utf-8")
    # Must include a Vision Docs section and link to CT Vision and Vision Index
    if "Vision Docs" not in idx:
        errors.append("[CONTENT] design_specs_index.md missing 'Vision Docs' section header")
    if "control_tower_vision.md" not in idx:
        errors.append("[LINK] design_specs_index.md missing Control Tower Vision link")
    if "vision_index.md" not in idx:
        errors.append("[LINK] design_specs_index.md missing Vision Docs Index link")

def check_vision_index():
    p = check_exists("Vision Docs Index", "docs/design/vision_index.md")
    txt = p.read_text(encoding="utf-8")
    # Required headers
    required_sections = [
        "Purpose", "How to Use This Index", "Current Vision Docs",
        "Pipeline (Planned Vision Docs)", "Conventions for Vision Docs",
        "Review & Merge Rules", "Change Log (this index)"
    ]
    for sec in required_sections:
        if sec not in txt:
            errors.append(f"[CONTENT] vision_index.md missing section: {sec}")
    # Must reference CT Vision
    if "control_tower_vision.md" not in txt:
        errors.append("[LINK] vision_index.md missing Control Tower Vision reference")

def main():
    check_readme_links()
    check_design_index()
    check_vision_index()

    if errors:
        print("Docs Guardian found issues:\n")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    else:
        print("Docs Guardian checks passed ✅")

if __name__ == "__main__":
    main()
