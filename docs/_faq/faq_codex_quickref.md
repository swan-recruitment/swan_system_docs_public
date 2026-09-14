# FAQ — Codex Quick Reference

This is a pocket guide for using Codex with the Swan ERP repos.  
For full details, see [FAQ — What is Codex?](faq_codex.md).

---

## 🔹 Install (one-time)

Open **Ubuntu via WSL** and run:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y nodejs npm git
npm install -g @openai/codex
codex signin
```

---

## 🔹 Run Codex

1. **Navigate to a repo root** (not project umbrella):
   ```bash
   cd /mnt/c/Users/Ben/swan-erp-system/<repo-name>
   ```

2. **Switch to coding model**:
   ```bash
   codex /model gpt-5-codex
   ```

3. **Run a prompt**:
   ```bash
   codex "Scan this repo and summarize its structure."
   ```

---

## 🔹 Workflow at a Glance

- **Local CLI (WSL):** quick repo scans, run tests, doc cleanups.  
- **VS Code extension:** inline refactors, apply diffs, lightweight jobs.  
- **Cloud Agent:** heavy jobs, CI, PR automation.  

---

## 🔹 Safety

- Always branch before Codex tasks:
  ```bash
  git checkout -b codex-task
  ```
- Review changes:
  ```bash
  git diff
  ```
- Default = approval mode (safe). Use read-only or full access if needed.

---

## 🔹 Starter Prompts by Repo

- **swan-accounts-integration**
  ```
  Audit API calls to external accounting systems and summarize data flow.
  ```

- **swan-contractor-portal**
  ```
  Run test suite, list failing tests, propose minimal fixes.
  ```

- **swan-control-tower**
  ```
  Map job scheduling flow, highlight bottlenecks, suggest optimizations.
  ```

- **swan-desktop-manager**
  ```
  Review Electron build configs, flag deprecated deps, suggest migrations.
  ```

- **swan-excel-tools**
  ```
  Test CSV export/import, handle edge cases, unify delimiter handling.
  ```

- **swan-firebase-backend**
  ```
  Map Cloud Functions, document triggers, flag security-sensitive code.
  ```

- **swan-website**
  ```
  Check SEO & accessibility, suggest quick fixes, propose CI checks.
  ```

- **swan_system_docs**
  ```
  Build a Markdown index by ERP module, standardize terminology, update glossary.
  ```

---

## 🔹 One-Liner Check

- **Am I in WSL?**
  ```bash
  uname -a   # should say Linux / WSL2
  ```
- **Am I in a repo?**
  ```bash
  ls -a | grep .git   # should return ".git"
  ```

---
