# SOP – Documentation Updates (New, Changed, Removed Files)

## 🎯 Purpose
Ensure all documentation changes (SOPs, diagrams, schemas, indexes, README updates, etc.) are **systematically integrated, indexed, and communicated**.

---

## 📝 Steps

### 1. **Create or Update the File**
- Place new or updated files in their correct folder:
  - SOPs → `swan_system_docs/docs/sop/`
  - Diagrams → `swan_system_docs/docs/diagrams/`
  - Schemas → `swan_system_docs/docs/schemas/`
  - Indexes → `docs/` of relevant folder
  - READMEs → repo root or subproject root
- Use consistent naming (`snake_case.md`).

---

### 2. **Update Indexes**
- If a file is **new**:
  - Add it to the nearest `INDEX.md` under the correct section.
  - Ensure alphabetical/logical grouping.
- If a file is **removed**:
  - Remove its link from all relevant `INDEX.md` files.
- If a file is **renamed**:
  - Update all affected links across indexes.

---

### 3. **Update Root README**
- Ensure Quick Links include:
  - Central `docs/index.md`
  - Key SOPs
  - CHANGELOG.md
- If the update is significant (new SOP, major schema, roadmap shift), add/update Quick Link.

---

### 4. **Update CHANGELOG.md**
- Every update must be logged.
- Format:
  ```markdown
  ## vX.Y (YYYY-MM-DD)
  - Added: new diagram X
  - Updated: README with new Quick Link
  - Removed: deprecated schema Y
  ```
- Newest entries at the top.

---

### 5. **Back-Linking**
- Ensure all SOPs and diagrams end with:
  ```markdown
  ---
  ⬅ Return to [Docs Index](../index.md)
  ```
- Apply consistently across updated files.

---

### 6. **Packaging (Optional)**
- If distributing update separately:
  - Bundle updated files into a `.zip`
  - Include a `DELTA_README.md` with:
    - List of files changed
    - Instructions where to copy
- Naming convention:  
  `swan_repo_update_{topic}_vX.Y.zip`

---

### 7. **Governance Rules**
- No file may exist **unindexed**.  
- Every file must be discoverable from:
  - Its folder `INDEX.md`
  - Central `docs/index.md`
  - (if relevant) Root README Quick Links
- **CHANGELOG.md** is the source of truth for tracking.  
- CI enforcement (future): fail build if docs are out of sync.

---

## ✅ Outcome
- All doc changes are indexed, linked, and logged.  
- Users can always navigate via README → Index → Docs.  
- Repo remains consistent across versions.
