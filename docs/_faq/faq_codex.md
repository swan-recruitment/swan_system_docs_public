# FAQ — What is Codex?

Codex is OpenAI’s coding agent. It integrates into your local repos, VS Code, and GitHub cloud workflows to help automate repetitive coding and documentation tasks. It reads repo structure, applies edits, runs commands, and can even draft PRs.

---

## 🧑‍🤝‍🧑 Who

- **Who provides Codex?**  
  OpenAI, included with ChatGPT Plus, Pro, Team, Edu, and Enterprise plans.

- **Who uses Codex?**  
  Developers, maintainers, and technical writers working inside the Swan ERP system repos (`swan-contractor-portal`, `swan-firebase-backend`, `swan_system_docs`, etc).

- **Who benefits most?**  
  Anyone maintaining multiple repos who wants consistency, speed, and automated repo housekeeping.

---

## ❓ What

- **What is Codex?**  
  A repo-aware coding agent that can:
  - Scan repositories for structure and risks
  - Propose or apply code and doc edits
  - Run tests locally or in the cloud
  - Generate documentation or consistency reports
  - Draft GitHub pull requests

- **What model does it use?**  
  `gpt-5-codex`, a version of GPT-5 tuned specifically for programming tasks.

- **What environments does it support?**  
  - **CLI (terminal)** via WSL/Ubuntu (Linux environment inside Windows)
  - **VS Code extension** (inline editing and diff review)
  - **Cloud Agent** (heavy jobs + PR automation via GitHub)

---

## ⚙️ How

- **How to install Codex CLI (inside WSL/Ubuntu):**
  ```bash
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y nodejs npm git
  npm install -g @openai/codex
  codex signin
  ```

- **How to run Codex:**
  1. Open Ubuntu (via WSL).
  2. `cd` into a repo root, e.g.:
     ```bash
     cd /mnt/c/Users/Ben/swan-erp-system/swan_system_docs
     ```
  3. Switch to coding model:
     ```bash
     codex /model gpt-5-codex
     ```
  4. Run prompts like:
     ```bash
     codex "Scan all docs and generate a Markdown index grouped by ERP module."
     ```

- **How to keep safe:**
  - Work in **approval mode** (default): Codex asks before edits/commands.
  - Always create a new branch before Codex tasks:
    ```bash
    git checkout -b codex-task-1
    ```
  - Review Codex’s proposed diffs with:
    ```bash
    git diff
    ```

---

## 💡 Why

- **Why use Codex?**
  - 🚀 **Speed:** automates repetitive tasks (scans, cleanups, edits).  
  - 📚 **Consistency:** enforces uniform naming, docs, workflows across repos.  
  - 🔎 **Insight:** quickly summarizes, documents, or proposes changes.  

- **Why WSL?**  
  Codex CLI is tested on Linux/macOS. Windows support is experimental. WSL gives a stable Linux environment inside Windows.

---

## 📍 Where

- **Where does Codex run?**
  - **Locally (CLI):** inside WSL/Ubuntu, scoped to a repo folder.  
  - **In VS Code:** via the Codex extension, inline with your editor.  
  - **In the Cloud:** at chatgpt.com/codex, integrated with GitHub.

- **Where are the repos?**  
  Under:  
  ```
  C:\Users\Ben\swan-erp-system\
  ```
  Each subfolder (e.g. `swan-firebase-backend`, `swan_system_docs`) is its own repo.

---

## 🕑 When

- **When to use CLI:**  
  For quick local scans, tests, or repo-wide consistency checks.

- **When to use VS Code extension:**  
  While actively editing code or docs; apply Codex diffs inline.

- **When to use Cloud Agent:**  
  For heavy tasks (full builds, running test suites, PR automation).

- **When not to use Codex:**  
  - If your repo has uncommitted changes (Codex works best on clean states).  
  - If you don’t want automated edits (use read-only planning mode instead).

---

## 🔒 Safety Notes

- Codex runs sandboxed. By default:
  - No network access
  - Writes limited to repo root
- You can tighten or loosen permissions with `approval`, `read-only`, or `full access` modes.
- Always review diffs (`git diff` or GitHub PR) before merging.
- Business/Enterprise plans disable training on your data by default.

---

## 📖 Appendix — Quickstart Prompts by Repo

Run these from the repo root inside WSL.

---

### 1. `swan-accounts-integration`

```
Audit this repo for external API calls to accounting systems.
- Document each integration point
- Summarize data flow in/out
- Suggest improvements for error handling
```

---

### 2. `swan-contractor-portal`

```
Run the test suite.
- Identify failing tests
- Propose minimal code fixes
- Generate diffs only, no auto-apply
```

---

### 3. `swan-control-tower`

```
Scan all modules for scheduling logic.
- Build a flowchart of how jobs are queued
- Highlight bottlenecks
- Suggest optimization opportunities
```

---

### 4. `swan-desktop-manager`

```
Review Electron build configs.
- Verify packaging scripts
- Flag any deprecated dependencies
- Propose migration steps to latest stable versions
```

---

### 5. `swan-excel-tools`

```
Check all spreadsheet export/import utilities.
- Ensure consistent CSV delimiter handling
- Add tests for edge cases (commas, quotes, line breaks)
- Propose a unified export module
```

---

### 6. `swan-firebase-backend`

```
Map all Firebase Cloud Functions.
- Document triggers and runtime logic
- Identify security-sensitive code (auth, payments)
- Suggest improvements for error logging
```

---

### 7. `swan-website`

```
Analyze SEO and accessibility compliance.
- Report on meta tags, headings, alt text
- Suggest quick HTML fixes
- Draft a CI check to enforce them
```

---

### 8. `swan_system_docs`

```
Scan all documentation.
- Build a Markdown index grouped by ERP module
- Check for inconsistent terminology
- Propose glossary updates
```

---

## ✅ Usage Notes

- Always branch before using Codex:
  ```bash
  git checkout -b codex-task
  ```
- Use CLI for local scans, VS Code for inline edits, Cloud Agent for PRs.  
- Start with approval mode until you’re confident.  
- Codex is powerful, but **you are always the reviewer**.
