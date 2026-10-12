Great question. Here’s a practical, no-nonsense guide to **README best practices** — tailored to your multi-repo setup (code repos + `swan_system_docs`).

---

# README Best Practices (for Swan)

## 1) Keep the README purpose-built

Different repos have different audiences. Shape the README accordingly:

* **Code repo (e.g., `swan-desktop-manager`)** → for developers who need to build/run/test/deploy this module.
* **Docs repo (`swan_system_docs`)** → for *everyone* as the project’s entry point (architecture, plans, governance).
* **Org landing (optional GitHub org profile)** → 1-screen intro + links to the key repos.

> Rule of thumb: put only what a reader **must** know to use *this* repo, and link to the docs repo for cross-cutting detail.

---

## 2) Core sections that every README should have

1. **What this repo is** (one paragraph: problem + scope + audience)
2. **Quickstart** (prereqs → install → run; copy/paste commands that work fresh)
3. **Configuration** (env vars, `.env.example`, secrets policy, common pitfalls)
4. **Test & CI** (how to run tests locally; what CI does on PR and on main)
5. **Releases/Deploy** (how/when it ships; links to environments if relevant)
6. **Troubleshooting** (top 3 issues + fixes)
7. **Links** (to system architecture, phase plans, work orders, issue templates)
8. **Contributing** (point to a single CONTRIBUTING in `swan_system_docs`)
9. **License / Contact** (even if “placeholder”)

> Keep it **actionable** and **short**; link out for deep detail.

---

## 3) Make it reliably usable

* **Executable snippets**: Everything in Quickstart should run on a clean machine (Windows + macOS/Linux). If it’s conditional, label it.
* **Provide `.env.example`** (never real secrets) and reference it explicitly.
* **Use relative links** within the repo; **explicit** links to `swan_system_docs` for cross-repo docs (prevents link rot).
* **Show status** with badges (once CI exists): build, tests, lint, deploy.
* **Screenshots/diagram PNGs** help non-engineers understand the module fast.

---

## 4) Keep READMEs DRY (don’t duplicate)

* Don’t restate the whole architecture in every code repo. Link to:
  `swan_system_docs/docs/design/swan_erp_system_architecture.md`
* Don’t paste full governance rules in every repo. Link to:
  `swan_system_docs/docs/CONTRIBUTING.md`
* Avoid duplicating long “why” narratives—keep that centralized.

---

## 5) Consistency rules for multiple repos

* **Shared section order** (so contributors always know where to look).
* **Shared phrasing** for common bits (e.g., secrets policy).
* **Same badge style** across repos.
* **Same call-outs** to the docs hub (architecture, plans, work orders, templates).

---

## 6) Maintenance hygiene

* Add a short “**Last updated**” line (manual or CI-injected).
* Review on every major change; READMEs go stale fast.
* Prefer links to **indexes** (e.g., “Visual Docs Index”) instead of linking to 10 separate files — fewer places to update.

---

## 7) Common mistakes to avoid

* “Monorepo” folder trees in a multi-repo world (confuses onboarding).
* Setup steps that skip an ecosystem (e.g., add Python but forget portal/npm or Firebase functions).
* Missing `.env.example` and missing `.gitignore` entries for `/secrets/`.
* Promising CI/CD that doesn’t exist yet (label it as “planned” and link to the work order).

---

## 8) Drop-in templates

### A) Code repo README (template)

```markdown
# <repo-name> — <one-line purpose>

## What this repo is
Short scope + who should use it. Link to system docs for the big picture.

## Quickstart
# Windows (PowerShell)
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# or bootstrap: pip install <packages> && pip freeze > requirements.txt
# Run: python -m <module>  (or npm run dev, etc.)

# macOS/Linux (bash)
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Configuration
Copy .env.example to .env and fill in values.
Never commit real secrets; see /secrets/ policy below.

## Secrets
/secrets/ (gitignored) for local-only credentials (e.g., service account JSON).
Use GitHub Actions Secrets in CI/CD.

## Tests & CI
pytest (or npm test)
CI: .github/workflows/<name>.yml (build, test, lint, deploy)

## Troubleshooting
- Common error A → fix
- Common error B → fix

## Links
- System Architecture: swan_system_docs/docs/design/swan_erp_system_architecture.md
- Phase Plans: swan_system_docs/docs/plans/phase_plans_index.md
- Work Orders: swan_system_docs/docs/work_order_master.md

## Contributing
Follow swan_system_docs/docs/CONTRIBUTING.md

## License / Contact
License: <…> • Email: placeholder • Maintainer: @ben.pitman
```

### B) `swan_system_docs` README (top-level)

(You already have this — we just generated `README_system_docs.md`. Keep it as your authoritative index.)

---

## 9) When to split docs out of the README

* If a section exceeds ~1–2 screens or includes decision history, move it to `/docs/` (or `swan_system_docs`) and **link** from the README.
* For architecture and governance, always split (the README should summarize and link).

---

## 10) Badges to add later (once CI is live)

* Build/Test (GitHub Actions)
* Lint/Format (e.g., flake8/ruff, eslint)
* Coverage (e.g., Codecov)
* Deploy (Firebase/Vercel status)
* Docs status (optional)

---

### TL;DR

* Treat READMEs as **entry points** — quick to read, quick to act on.
* Keep **cross-cutting** details centralized in `swan_system_docs`.
* Make setup **copy/paste runnable** and include `.env.example`.
* Use consistent structure across repos; **link, don’t duplicate**.

If you like, I can turn the **code-repo template** above into `README_TEMPLATE.md` and drop it into `swan_system_docs/docs/templates/` so you can clone it into each new repo.
