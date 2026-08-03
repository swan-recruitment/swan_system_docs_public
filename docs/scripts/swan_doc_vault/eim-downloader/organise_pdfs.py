import csv, os, shutil
from pathlib import Path

BASE_PATH = Path(".")
DOWNLOADS_DIR = BASE_PATH / "00_downloads"
MASTER_CSV = BASE_PATH / "master_entries.csv"

def main():
    if not MASTER_CSV.exists(): 
        print("No master_entries.csv found."); return
    with MASTER_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            parent_code, parent_title = row["parent_code"], row["parent_title"].replace(" ","_").replace(":","")
            child_code = row["child_code"]
            src = DOWNLOADS_DIR / f"{child_code}.pdf"
            if not src.exists(): 
                print(f"Missing {src}"); continue
            parent_folder = BASE_PATH / f"{parent_code}-{parent_title}"
            parent_folder.mkdir(exist_ok=True)
            dest = parent_folder / src.name
            shutil.move(str(src), str(dest))
            print(f"Moved {child_code} -> {parent_folder}")

if __name__ == "__main__": main()
