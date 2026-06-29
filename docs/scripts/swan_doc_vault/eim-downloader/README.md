# EIM Downloader Package

This package automates fetching and organising GOV.UK Employment Income Manual (EIM) pages into PDFs.

## Setup

1. Install Python 3.10+ and VS Code.
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## Usage

### Step 1: Fetch all PDFs
```bash
python fetch_all.py
```
This will:
- Crawl GOV.UK for all EIM pages
- Save PDFs into `00_downloads/`
- Create `eim_inventory.csv`

### Step 2: Organise PDFs
1. Fill in `templates/master_entries.csv` with parent→child mapping.
2. Run:
```bash
python organise_pdfs.py
```

This will move PDFs into parent folders and generate `index.txt` per folder + `master_index.csv` at base.
