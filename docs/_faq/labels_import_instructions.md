# Importing labels.json into a GitHub repo

## Option A: GitHub CLI (gh)
```bash
# 1) Ensure you are in the repo root and authenticated: gh auth login
# 2) Remove existing labels (optional)
gh label list --json name -q '.[].name' | xargs -I {} gh label delete "{}" -y

# 3) Create labels from labels.json
# Requires jq. Install: https://stedolan.github.io/jq/
jq -c '.[]' labels.json | while read -r label; do
  name=$(echo "$label" | jq -r '.name')
  color=$(echo "$label" | jq -r '.color')
  description=$(echo "$label" | jq -r '.description')
  gh label create "$name" --color "$color" --description "$description" || gh label edit "$name" --color "$color" --description "$description"
done
```

## Option B: Probot Settings App
- Add `labels.json` content under the `labels:` section of `.github/settings.yml`
- Install the **Settings** app: https://probot.github.io/apps/settings/
- Push to `main` to sync labels automatically.
