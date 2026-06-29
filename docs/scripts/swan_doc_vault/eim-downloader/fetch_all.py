import re, time, csv
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

BASE_URL = "https://www.gov.uk/hmrc-internal-manuals/employment-income-manual"
DOWNLOADS_DIR = Path("00_downloads")
INVENTORY_CSV = DOWNLOADS_DIR / "eim_inventory.csv"
EIM_RE = re.compile(r"^/hmrc-internal-manuals/employment-income-manual/eim\d{5}$")
DOMAIN = "www.gov.uk"

def is_eim_page(path): return bool(EIM_RE.match(path.lower()))
def fetch(url): return requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)

def discover_all(seed: str, max_pages=5000):
    queue, seen, found = [seed], {seed}, {}
    while queue and len(seen) < max_pages:
        url = queue.pop(0)
        try:
            resp = fetch(url)
        except Exception: continue
        if resp.status_code >= 400: continue
        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.find_all("a", href=True):
            full = urljoin(url, a["href"].strip())
            parsed = urlparse(full)
            if parsed.netloc != DOMAIN: continue
            if full not in seen and parsed.path.startswith("/hmrc-internal-manuals/employment-income-manual"):
                seen.add(full); queue.append(full)
            if is_eim_page(parsed.path):
                code = parsed.path.rstrip("/").split("/")[-1].upper()
                if code not in found:
                    found[code] = {"code": code, "url": f"https://{DOMAIN}{parsed.path}", "title": a.get_text(strip=True)}
        time.sleep(0.2)
    rows = [{"code": k, "url": v["url"], "title": v.get("title", "")} for k,v in found.items()]
    rows.sort(key=lambda r: r["code"])
    return rows

def save_inventory(csv_path, rows):
    csv_path.parent.mkdir(exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code","url","title"]); w.writeheader(); w.writerows(rows)

def download_pdfs(inventory, out_dir):
    out_dir.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for row in inventory:
            code, url = row["code"], row["url"]
            pdf_path = out_dir / f"{code}.pdf"
            try:
                page.goto(url, wait_until="networkidle", timeout=45000)
                page.pdf(path=str(pdf_path), format="A4", print_background=True)
                print(f"Saved {pdf_path}")
            except Exception as e:
                print(f"Failed {code}: {e}")
        browser.close()

def main():
    rows = discover_all(BASE_URL)
    save_inventory(INVENTORY_CSV, rows)
    download_pdfs(rows, DOWNLOADS_DIR)

if __name__ == "__main__": main()
