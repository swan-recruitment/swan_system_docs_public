# <Repo Name> – <One-line Purpose>

## 📌 Overview
This repository contains the <short description of the module>.  
It is part of the **Swan Recruitment ERP system**, a Firebase-driven workflow platform linking candidate placement, contracts, timesheets, invoicing, and finance reconciliation.

For full system context, see:  
[Swan ERP System Architecture](../../design/swan_erp_system_architecture.md)

---

## 🚀 Quickstart

### Prerequisites
- OS: Windows 10/11, macOS 13+, or Linux
- Package Manager: pip / npm / yarn (depending on repo)
- Runtime:
  - Python 3.11+ (for desktop/CLI)
  - Node.js 20+ (for portals/frontend)
- GitHub account with access to Swan repos

### Setup

#### 1. Clone repo
```powershell
git clone https://github.com/<org>/<repo-name>.git
cd <repo-name>
```

#### 2. Create virtual environment (Python only)
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
_or (macOS/Linux):_
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### 3. Install dependencies (Node.js only)
```bash
npm install
# or
yarn install
```

#### 4. Environment configuration
Copy `.env.example` → `.env` and fill in required values.

Common variables:
```
FIREBASE_PROJECT_ID=<your_project>
FIREBASE_API_KEY=<firebase_api_key>
SERVICE_ACCOUNT_KEY=./secrets/service_account.json
PORT=3000
```

#### 5. Run
- **Python:**
```powershell
python -m <main_module>
```
- **Node.js/React/Vite:**
```bash
npm run dev
```

---

## ⚙️ Configuration

### Environment Files
- `.env` – runtime config (never commit)
- `.env.example` – template with placeholders
- `/secrets/` – for local-only sensitive files (gitignored)

### Secrets Policy
- Never commit real secrets.  
- Use GitHub Actions Secrets for CI/CD.  
- Local secrets belong in `/secrets/`.  

Add to **.gitignore** (if not already present):
```
/secrets/
*.json
*.key
*.pem
```

---

## 🧪 Tests & CI

### Local tests
```powershell
pytest
# or
npm test
```

### Continuous Integration
- CI runs via GitHub Actions, validating:
  - Install & build
  - Lint/format
  - Unit tests
- Workflow file: `.github/workflows/<ci-name>.yml`

> Add badges once CI is enabled.

---

## 🛠 Common Tasks

### Format / Lint
```powershell
# Python
ruff check . --fix
black .

# Node.js
npm run lint
npm run format
```

### Generate Docs (if supported)
```powershell
npm run docs
```

### Update Dependencies
```powershell
pip install -U -r requirements.txt
npm update
```

---

## 🐞 Troubleshooting

- **Firebase auth errors** → ensure `SERVICE_ACCOUNT_KEY` path is correct.
- **Port already in use** → change `PORT` in `.env`.
- **npm install fails on Windows** → try `npm install --force` or clear cache.

---

## 🔗 Links

- **System Docs Hub** → `swan_system_docs` repository  
- **Architecture Overview** → `swan_system_docs/docs/design/swan_erp_system_architecture.md`  
- **Phase Plans** → `swan_system_docs/docs/plans/phase_plans_index.md`  
- **Work Orders** → `swan_system_docs/docs/work_order_master.md`  

---

## 🤝 Contributing

- Use the PR template (`.github/pull_request_template.md`)  
- Apply label taxonomy (`.github/labels.json`)  
- Follow [Contributing Guidelines](../../CONTRIBUTING.md)  

---

## 📦 Deployment

- CI/CD via GitHub Actions → Firebase Hosting / Cloud Run / Vercel (varies per repo).  
- Deployment triggers (example):
  - `main` → staging  
  - `release/*` → production  

More details: see `docs/deployment.md` (to be added per repo).

---

## 📅 Roadmap

- [ ] Feature A (planned)  
- [ ] Feature B (planned)  
- [x] Core setup (done)  

System-wide roadmap: `swan_system_docs/docs/plans/phase_plans_index.md`

---

## 🔐 Security & Compliance

- **GDPR** – minimal PII, retention policies applied  
- **Secrets** – GitHub Actions Secrets + local `/secrets/` only  
- **Audit** – PR + labels + work orders provide traceability  

---

## 📬 Contact

- Maintainer: **Ben Pitman** (@ben.pitman)  
- Email: **placeholder** (to be updated)  
- Org: Swan Recruitment  
