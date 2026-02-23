import os
import re
import csv
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

# -------------------- CONFIG --------------------
BASE_URL = "https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/"
BASE_PATH = r"C:\Users\Ben\swan-erp-system\swan-doc-vault\vault\guides\employers_guilde"

# Parent → Child structure (expand as you add screenshots)
ENTRIES = [
    ("EIM00010", "Data protection", [
        ("EIM00010", "Data protection"),
    ]),
    ("EIM00100", "About this manual", [
        ("EIM00100", "About this manual"),
    ]),
    ("EIM00500", "Employment income: contents", [
        ("EIM00505", "General: contents"),
        ("EIM01000", "Particular items: A to P: contents"),
        ("EIM01650", "Particular items: New Deal, employment zones and particular exemptions: contents"),
        ("EIM03050", "Employee Ownership Trusts – qualifying bonus payments: introduction"),
        ("EIM03100", "Removal or transfer costs: contents"),
        ("EIM03600", "Restrictive covenants: contents"),
        ("EIM04700", "Particular items: R to Z: contents"),
    ]),
    # Add more parents + children here as you upload screenshots
]
# ------------------------------------------------

INVALID = r'[<>:"/\\|?*\x00-\x1F]'
TRAILING = r'[\. ]+$'

def safe_title(title: str) -> str:
    t = title.replace(" ", "_").replace(":", "")
    t = re.sub(INVALID, "-", t)
    t = re.sub(TRAILING, "", t)
    return t

def write_parent_index(parent_folder: Path, parent_code: str, parent_title: str, rows: list):
    """
    rows: list of dicts with keys child_code, child_title, filename, url, saved_path
    """
    lines = []
    lines.append(f"{parent_code} — {parent_title}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("-" * 80)
    for r in rows:
        lines.append(f"{r['child_code']} — {r['child_title']}")
        lines.append(f"  File : {r['filename']}")
        lines.append(f"  URL  : {r['url']}")
        lines.append("")
    (parent_folder / "index.txt").write_text("\n".join(lines), encoding="utf-8")

def main():
    base = Path(BASE_PATH)
    base.mkdir(parents=True, exist_ok=True)

    master_csv = base / "master_index.csv"
    master_rows = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for parent_code, parent_title, children in ENTRIES:
            parent_folder = base / f"{parent_code}-{safe_title(parent_title)}"
            parent_folder.mkdir(exist_ok=True)

            parent_rows = []

            for child_code, child_title in children:
                url = BASE_URL + child_code.lower()
                pdf_path = parent_folder / f"{child_code}.pdf"

                print(f"Fetching {url}")
                try:
                    page.goto(url, wait_until="networkidle")
                    page.pdf(path=str(pdf_path), format="A4")
                    print(f"Saved → {pdf_path}")
                except Exception as e:
                    print(f"⚠️ Failed {child_code}: {e}")

                row = {
                    "parent_code": parent_code,
                    "parent_title": parent_title,
                    "child_code": child_code,
                    "child_title": child_title,
                    "filename": pdf_path.name,
                    "saved_path": str(pdf_path),
                    "url": url,
                }
                parent_rows.append({
                    "child_code": child_code,
                    "child_title": child_title,
                    "filename": pdf_path.name,
                    "url": url,
                    "saved_path": str(pdf_path),
                })
                master_rows.append(row)

            # write/update per-parent index.txt
            write_parent_index(parent_folder, parent_code, parent_title, parent_rows)

        browser.close()

    # write/update master_index.csv
    write_header = not master_csv.exists()
    with master_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["parent_code","parent_title","child_code","child_title","filename","saved_path","url"]
        )
        writer.writeheader()
        writer.writerows(master_rows)

    print(f"Master index written: {master_csv}")

if __name__ == "__main__":
    main()
