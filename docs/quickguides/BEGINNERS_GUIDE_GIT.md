# Beginner’s Guide to Git & GitHub

This guide is written for complete beginners. It covers the essentials you need to start using Git on your computer and GitHub online.

---

## 1. What Git & GitHub Are
- **Git** → version control on your computer. Tracks changes to files and lets you roll back, branch, or merge.  
- **GitHub** → a website that hosts Git repos in the cloud. Lets you back up, share, and collaborate.  

Think of it like this:  
📂 Local repo (on your PC) ↔ 🌐 Remote repo (on GitHub).

---

## 2. Core Concepts
- **Repository (repo):** A project folder tracked by Git.  
- **Commit:** A saved snapshot of changes with a message.  
- **Branch:** A separate line of work inside the repo. Default is usually `main`.  
- **Push:** Send commits from local → GitHub.  
- **Pull:** Bring commits from GitHub → local.  
- **Clone:** Download a copy of a repo from GitHub.  
- **Remote:** The reference to a GitHub repo (usually called `origin`).  

---

## 3. First-Time Setup (Local)
Run these in Git Bash or your terminal:
```bash
git config --global user.name "Your Name"
git config --global user.email "you@company.com"
```

Verify with:
```bash
git config --global --list
```

---

## 4. Everyday Workflow
### Step 1. Clone the repo
```bash
git clone https://github.com/org-name/repo-name.git
cd repo-name
```

### Step 2. Make changes
Edit files, add new docs, etc.

### Step 3. Stage changes
```bash
git add file1 file2   # or git add . to stage all
```

### Step 4. Commit
```bash
git commit -m "docs: add new workflow step"
```

### Step 5. Push
```bash
git push origin main
```

---

## 5. The README “Gotcha”
When creating a repo on GitHub, you can **Initialize with README**.

- **If checked:** GitHub creates its own README file → the repo already has one commit. If you also have a local README, you’ll need to `git pull` first to merge.  
- **If unchecked:** The repo is empty, and your local push goes through cleanly.  

👉 If you already have local files, leave “Initialize with README” **unticked**.

---

## 6. Branching Basics
```bash
git checkout -b feature/my-new-doc   # create new branch
# make edits
git add .
git commit -m "docs: draft new guide"
git push origin feature/my-new-doc
```
Then open a **Pull Request** on GitHub to merge your branch into `main`.

---

## 7. Resolving Common Issues
- **Repository not found** → The repo hasn’t been created on GitHub or URL is wrong.  
- **Updates were rejected** → Remote has commits you don’t. Fix with:
  ```bash
  git pull --rebase origin main
  git push origin main
  ```
- **“LF will be replaced by CRLF” warning** → Normal on Windows. Safe to ignore.  

---

## 8. Quality-of-Life Tools
- **GitHub Desktop** → GUI for Git. Beginner friendly.  
- **VS Code Git panel** → Stage/commit/push directly from the editor.  
- **Git LFS** → Needed if storing large files (images, zips).  

---

## 9. Golden Rules
1. Always write clear commit messages.  
2. Use branches for bigger changes, not `main`.  
3. Pull before pushing if others are working on the same repo.  
4. Keep a `.gitignore` file to exclude temp/unnecessary files.  
5. Use Pull Requests (PRs) for review before merging to `main`.  

---

## 10. Visual Summary

```
Local (your PC)                     Remote (GitHub)
-----------------                   ----------------
git add  -------- stage  -------->
git commit ---- save history ----->
git push ---- upload commits ----->
<----- git pull ---- download -----
```

---

✅ With just these basics, you can handle 95% of GitHub workflows. The rest (rebasing, CI/CD, etc.) can come later.
