# Public Mirror Pack for `swan_system_docs`

This pack publishes a **sanitized public snapshot** of your private repo, so others can review
your code and standards **without secrets**.

## What's inside
- `.mirrorignore-public` — deny-list of files/folders that will **never** be published
- `.github/workflows/publish-sanitized-mirror.yml` — GitHub Actions workflow to stage everything
  except deny-listed items, scan for secrets, and push to the public mirror over SSH
- `MIRROR_PROVENANCE.json` — generated at runtime to record which commit produced the mirror

## One-time setup
1. Create the public repo: `swan-recruitment/swan_system_docs_public` (empty, Public).
2. Generate an SSH keypair (outside your repo):
   ```bash
   ssh-keygen -t ed25519 -C "mirror-bot" -f mirror_rsa -N ""
   ```
3. Public repo → **Settings → Deploy keys → Add deploy key**  
   - paste `mirror_rsa.pub`, enable **Allow write access**
4. Private repo (`swan_system_docs`) → **Settings → Secrets and variables → Actions → New repository secret**  
   - Name: `MIRROR_SSH_KEY`  
   - Value: contents of `mirror_rsa` (private key)

## Install
- Drop `.mirrorignore-public` in the repo root.
- Drop the workflow file into `.github/workflows/`.
- Commit to `main`.

## Run
- GitHub → **Actions → Publish sanitized mirror (public) → Run workflow**.
- Or push to `main`; there’s also a Monday 06:00 UTC schedule.

## Customize
- Edit `.mirrorignore-public` to add/remove folders.
- To expose more later (still safe), remove lines from the deny-list.
- If your public repo has a different name, edit:
  - `env.MIRROR_REPO` and `MIRROR_SSH_URL` in the workflow.

Generated: 2025-10-03T12:58:38.759719Z
