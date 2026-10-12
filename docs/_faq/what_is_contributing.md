Great question 👍

The **CONTRIBUTING.md** file is used as a **contributor guide** in a GitHub repository. Think of it as the **rulebook** for how you (and anyone else in the future) should work with your docs and planning repo.

Here’s what it does for you specifically:

---

## 📌 Purpose of CONTRIBUTING.md

* **Sets standards** → Ensures diagrams, specs, and plans are all structured the same way.
* **Explains workflows** → Tells contributors how to use issue templates, labels, and PR checklists.
* **Prevents drift** → Reduces the risk of broken links, inconsistent naming, or undocumented changes.
* **Onboards new people fast** → Even if Swan stays just you + 3 staff, this file makes it possible to grow (freelancers, auditors, or future hires) without confusion.
* **Supports governance** → Codifies what you’ve already been building with Work Orders, Phase Plans, and indexes.

---

## 📂 Where it lives

* At the root of your docs/planning repo (`/CONTRIBUTING.md`).
* GitHub automatically highlights it when someone opens a PR or Issue, so it’s **visible at the right time**.

---

## ⚙️ How it’s used in practice

1. You (or a teammate) want to update a diagram → open CONTRIBUTING.md → see that you must produce `.md`, `.mmd`, and `.html` formats, and update indexes.
2. Someone opens an issue for Phase 5 → the Phase 5 issue template pops up → CONTRIBUTING.md explains how labels, KPIs, and DoD must be filled in.
3. Before merging a PR → contributor checks the **PR checklist** in CONTRIBUTING.md to ensure links updated, risks listed, reviewers tagged.
4. CI/CD → you decide to add markdown lint and link checks. CONTRIBUTING.md documents this so failures make sense.

---

## 🎯 Why it matters for Swan ERP

You’re building a **multi-repo, multi-phase ERP-like system** with lots of moving parts. Even though the team is small, without a CONTRIBUTING.md you risk:

* Forgetting to update cross-links between indexes and diagrams.
* Phase plans drifting away from work orders.
* PRs being merged without clear DoD.

With this file in place, your **governance process becomes explicit, enforceable, and teachable**.

---

