# SOP – Documentation Audit Process

## 🎯 Purpose
Ensure all documentation (`README.md`, `INDEX.md`, SOPs, schemas, diagrams, etc.) is **compliant, consistent, navigable, and error-free** by performing regular audits.

---

## 📝 Audit Scope

### 1. **File Types to Audit**
- `README.md` (root + subprojects)  
- `INDEX.md` (all docs folders)  
- SOPs (`docs/sop/*.md`)  
- Diagrams (`docs/diagrams/*.md`)  
- Schemas (`docs/schemas/*.json`)  

### 2. **Audit Frequency**
- **Monthly** scheduled audit.  
- **On-demand** after major merges or documentation updates.

---

## 🧾 Audit Checklist

### A. **Metadata Compliance**
- Each file must have:
  - Title (`# Heading`).  
  - **Last Updated:** ISO date.  
  - **Version:** (`vX.Y`) if SOP/governance doc.  

---

### B. **README.md Checks**
- Must exist at repo root + subprojects.  
- Contains **📌 Quick Links** section.  
- Links to:
  - Central `docs/index.md`.  
  - `CHANGELOG.md`.  
  - Key SOPs (Meta-Docs, File Standards, Docs Update).  
- “Last Updated” stamp present.  
- Content length reasonable (<200 lines).

---

### C. **INDEX.md Checks**
- Must exist in `/docs/` and major subfolders.  
- Contains sections:
  - 📊 Diagrams  
  - 🧩 Schemas  
  - 📑 SOPs  
  - 🛠 Scripts  
  - 🧪 Fixtures/Validators  
  - 🧭 Navigation  
- All files in folder are listed (no orphans).  
- Back-link footer present if nested.

---

### D. **Link Integrity**
- Verify all relative links resolve.  
- Flag missing or broken links.  
- Ensure cross-links:
  - README ↔ Index ↔ Docs.  
  - SOPs ↔ Index.  

---

### E. **Back-Link Enforcement**
- All SOPs and diagrams must end with:
  ```markdown
  ---
  ⬅ Return to [Docs Index](../index.md)
  ```
- Validate for presence + correctness.

---

### F. **Change Logging**
- Every major update logged in `CHANGELOG.md`.  
- Changelog entry format:
  ```markdown
  ## vX.Y (YYYY-MM-DD)
  - Added: ...
  - Updated: ...
  - Removed: ...
  ```

---

### G. **Formatting Standards**
- Headings hierarchical (start with `#`).  
- Code blocks fenced properly.  
- No 500+ character lines.  
- Markdown syntax valid.

---

## 📌 Audit Process

1. **Extract Repo Tree**  
   Identify all `README.md` and `INDEX.md` files.

2. **Run Automated Checks**  
   - Link validator (relative paths).  
   - Metadata & back-link enforcement script.  
   - Orphan file detector.  

3. **Manual Review**  
   - Confirm business context + clarity.  
   - Spot-check formatting and content accuracy.  

4. **Generate Report**  
   - Compliance summary (✅/⚠️/❌ per file).  
   - Broken links list.  
   - Orphans list.  

5. **Remediation**  
   - Update files as per SOPs.  
   - Log updates in `CHANGELOG.md`.  
   - Package fixes as `swan_repo_docs_audit_{date}.zip`.

---

## ✅ Outcome
- Documentation is always compliant with Swan SOPs.  
- Links are intact.  
- Files are traceable and discoverable.  
- Repo passes **governance audit** for documentation.

---
⬅ Return to [Docs Index](../index.md)
