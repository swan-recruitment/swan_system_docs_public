You pasted the **remote URL** as if it were a command—that’s why Bash says “No such file or directory.” Use it with `git remote add` (or `set-url`). Here’s the exact sequence for this repo:

```bash
# you're already here:
# ~/swan-erp-system/swan-accounts-integration

# 1) make sure we're on main
git branch -M main

# 2) add (or update) the remoteswan-contractor-portal
git remote add origin git@github.com:swan-recruitment/swan_system_docs_public.git 2> /dev/null || \
git remote set-url origin git@github.com:swan-recruitment/swan_system_docs.git

# 3) stage & commit (if needed)
git add .
git commit -m "feat(swan-packs-config repo): initial commit" || echo "Nothing to commit"

# 4) push
eval $(ssh-agent -s) && ssh-add ~/.ssh/id_ed25519   
git push -u origin main
```

Quick checks if something errors:

* See the remote: `git remote -v`
* If GitHub repo isn’t empty: `git pull origin main --allow-unrelated-histories` then resolve/commit/push.
