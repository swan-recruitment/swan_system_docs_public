# FAQ — Why does a repo look “missing” or mis-mapped?

Sometimes when listing remotes or looping through repos, a repo may appear “missing” or show the wrong mapping (e.g. a folder called `swan-website` pointing to `swan_systems_docs.git`). This FAQ explains why and how to fix it.

---

## 🧑‍🤝‍🧑 Who

- **Who does this affect?**  
  Developers working with multiple repos in the Swan ERP system under the umbrella folder.  
- **Who usually spots it?**  
  Anyone running `git remote -v` loops or Codex tasks across all repos.

---

## ❓ What

- **What’s happening?**  
  A repo is not appearing as expected because:
  - The folder path in WSL doesn’t match the actual Windows path.  
  - The folder is misnamed compared to its remote (`swan-website` vs `swan_system_docs`).  
  - The remote URL points to the wrong GitHub repo (`swan_systems_docs` vs `swan_system_docs`).  

---

## ⚙️ How

### Step 1 — Verify the umbrella path in WSL
```bash
# list user folders on C:
ls -d /mnt/c/Users/* | sed 's#/mnt/c/Users/##'

# search across drives for swan erp system
find /mnt/c /mnt/d -maxdepth 4 -type d -iname "*swan*erp*system*" 2>/dev/null

# convert a known Explorer path to WSL form
wslpath -a "C:\Users\Ben\swan-erp-system"
```

### Step 2 — Map folders to remotes
```bash
cd /mnt/c/Users/Ben/swan-erp-system   # adjust if different
for d in swan-*; do
  if [ -d "$d/.git" ]; then
    echo -n "$d → "
    git -C "$d" remote get-url origin
  fi
done
```

### Step 3 — Fix mismatches

**Case A — Folder is wrong, remote is right**
```bash
mv swan-website swan_system_docs
git -C swan_system_docs remote -v
```

**Case B — Remote is wrong, folder is right**
```bash
cd swan_system_docs
git remote set-url origin git@github.com:swan-recruitment/swan_system_docs.git
git remote -v
```

**Case C — Repo is missing locally**
```bash
git clone git@github.com:swan-recruitment/swan_system_docs.git
```

---

## 💡 Why

- **Why does this matter?**  
  Codex and Git commands assume the folder and remote are aligned. If they’re not:
  - Codex may refuse to run in that folder.  
  - Pushes and PRs may go to the wrong repo.  
  - Automated loops miss repos entirely.

---

## 📍 Where

- **Where to check:**  
  Run these commands at the **umbrella project folder** where all repos live (e.g., `/mnt/c/Users/Ben/swan-erp-system/`).  
- **Where issues show up:**  
  - In `git remote -v` output  
  - In Codex not recognizing the repo root  
  - In GitHub showing duplicate or missing repos

---

## 🕑 When

- **When to run checks:**  
  - After cloning new repos  
  - After renaming folders  
  - Before first using Codex across all repos  
- **When to fix:**  
  Immediately, to avoid bad pushes or mis-mapped PRs.

---

## 🔒 Safety Notes

- Always double-check before running `mv` or `git remote set-url`.  
- If unsure, back up the repo folder.  
- Consistency is key: pick **one canonical name** (`swan_system_docs`) and stick to it locally and on GitHub.

---

## 📖 Script: Clean Folder → Origin Table

```bash
cd /mnt/c/Users/Ben/swan-erp-system
printf "%-28s | %s\n" "Folder" "Origin"
printf "%-28s-+-%s\n" "----------------------------" "----------------------------------------------"
for d in swan-*; do
  if [ -d "$d/.git" ]; then
    origin=$(git -C "$d" remote get-url origin 2>/dev/null || echo "—")
    printf "%-28s | %s\n" "$d" "$origin"
  fi
done
```

This outputs a clean table to spot any folder/remote mismatches at a glance.

---

## ✅ Usage Summary

- Run the mapping script at the umbrella folder.  
- Confirm that all 8 repos map correctly:
  - `swan-accounts-integration`  
  - `swan-contractor-portal`  
  - `swan-control-tower`  
  - `swan-desktop-manager`  
  - `swan-excel-tools`  
  - `swan-firebase-backend`  
  - `swan-website`  
  - `swan_system_docs` (ensure singular/plural is consistent)  
- Fix names/remotes if anything looks off.  
- Once clean, Codex can safely operate on each repo.

---
