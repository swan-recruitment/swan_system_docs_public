# 📖 ChatGPT Command Cheat Sheets – v3 Architecture Plan

This document outlines the planned structure for **v3** of the ChatGPT Command Cheat Sheets.  
It expands beyond command listings into a **system-level playbook**.

---

## 1. 📌 Core Commands (refreshed from v2)
- Memory & Instructions (with resets, scoped memory, preferences)  
- Tasks & Reminders (time, recurring, conditional, chained)  
- File & Document handling (compare, extract, convert, summarize, export)  
- Web & GitHub (repo queries, commits, issues, PRs)  
- Images (generate, edit, transform, mockups)  
- Dev & Data (analysis, debug, export formats, fake data)  
- Swan Control Tower (tags, merges, reviews, reprioritize tasks)  
- Shortcuts (expand/compress/rewrite)  

---

## 2. 🔄 Advanced Patterns
- **Command chaining:**  
  ```
  summarize → extract risks → rewrite as checklist
  ```
- **Macros (pseudo):**  
  - `/daily-summary` = “summarize last 10 messages, list tasks, tag blockers”  
- **Conditional workflows:**  
  - “notify me if X happens → also tag #CT → also export to task list”  
- **Scoped reviews:**  
  - “review only section ## Dev & Data in v2 cheat sheet”  

---

## 3. 📖 Best Practices
- Use **Functional** in active chats (speed).  
- Use **Styled** in docs, onboarding, and Notion.  
- Keep **Control Tower** commands tagged with #CT/#CTM/#GUIDE.  
- Always confirm merges, avoid silent overwrites.  
- For exports: prefer `.md` → `.pdf` only for client delivery.  

---

## 4. 🏗️ Integration Hooks
- **Control Tower:** `/review-update-parent` always generates GitHub-ready docs.  
- **GitHub:** PR-ready commit templates for cheat sheet updates.  
- **Notion:** Styled version copies cleanly (with emojis).  
- **Excel/Sheets:** Use `export this as CSV` + analysis commands.  

---

## 5. 🎯 Scenarios & Examples
- **Daily Ops:**  
  - `remind me every morning at 9am to check invoices`  
  - `summarize last 20 lines of this doc`  
- **Project Work (Firebase):**  
  - `find where "starter webhook" is defined in swan-firebase-backend`  
  - `explain this function line by line`  
- **Debugging:**  
  - `simulate execution of this VBA function step by step`  
- **Client Prep:**  
  - `rewrite this as a client-facing email`  
  - `make this investor-ready`  

---

## 6. 🔮 Future-Proofing
- Reserved section for **new tags**, e.g., #SOP, #PIPELINE, #QA.  
- Expansion slots for new command classes (e.g., Slack integrations, API triggers).  
- Versioning notes:  
  - v1 → basic list  
  - v2 → expanded commands  
  - v3 → playbook + best practices  
