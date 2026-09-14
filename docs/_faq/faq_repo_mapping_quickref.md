# FAQ — Repo Mapping Quick Reference

This is the short version of the repo mapping FAQ. Use it as a command cheatsheet.

---

## Verify umbrella path in WSL
```bash
# list user folders on C:
ls -d /mnt/c/Users/* | sed 's#/mnt/c/Users/##'

# search across drives for swan erp system
find /mnt/c /mnt/d -maxdepth 4 -type d -iname "*swan*erp*system*" 2>/dev/null

# convert Explorer path to WSL
wslpath -a "C:\Users\Ben\swan-erp-system"
```

---

## Map folders to remotes
```bash
cd /mnt/c/Users/Ben/swan-erp-system   # adjust if needed
for d in swan-*; do
  if [ -d "$d/.git" ]; then
    echo -n "$d → "
    git -C "$d" remote get-url origin
  fi
done
```

---

## Fix mismatches

**Folder wrong, remote right**
```bash
mv swan-website swan_system_docs
git -C swan_system_docs remote -v
```

**Remote wrong, folder right**
```bash
cd swan_system_docs
git remote set-url origin git@github.com:swan-recruitment/swan_system_docs.git
git remote -v
```

**Repo missing locally**
```bash
git clone git@github.com:swan-recruitment/swan_system_docs.git
```

---

## Clean folder → origin table
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

---

## Quick Checklist

- Confirm all 8 repos appear with correct origins.  
- Canonical list:
  - `swan-accounts-integration`
  - `swan-contractor-portal`
  - `swan-control-tower`
  - `swan-desktop-manager`
  - `swan-excel-tools`
  - `swan-firebase-backend`
  - `swan-website`
  - `swan_system_docs`  
- Rename folders or update remotes if needed.  
- Keep everything consistent before using Codex.  

---
