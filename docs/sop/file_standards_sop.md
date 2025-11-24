# SOP – File Creation & Update Standards

## 🎯 Purpose
Ensure all files in the Swan ERP Project are consistently documented with **metadata, timestamps, and links**, making updates traceable and navigable.

---

## 📝 Standards for All Files

### 1. **Header Information**
Each file must start with a clear header containing:
- **Title** (H1 heading with file name or purpose)  
- **Description/Purpose** (1–2 lines)  
- **Last Updated:** `YYYY-MM-DD HH:MM TZ`  
- **Version (if applicable):** `vX.Y`
- **File PATH** Link to PATH  

---

### 2. **Change Tracking**
- Any update must be logged in `CHANGELOG.md` at repo root.  
- In-file optional: add a short `Changelog` section if the file is critical (schemas, SOPs).  

Example:
```markdown
## Changelog
- v1.1 (2025-09-29) – Added timestamp rules
- v1.0 (2025-09-28) – Initial creation
```

---

### 3. **Back-Linking (Docs Only)**
- All `docs/*.md` files must end with:
  ```markdown
  ---
  ⬅ Return to [Docs Index](../index.md)
  ```

---

### 4. **Indexing**
- Every new or updated file must be listed in the nearest `INDEX.md`.  
- Root README Quick Links updated if significant (e.g., new SOP, major schema).  

---

### 5. **Timestamps**
- Update `Last Updated:` on every edit.  
- Format: `YYYY-MM-DD HH:MM TZ` (ISO date + 24h time + timezone).  
- This ensures files can be sorted and tracked over time.  

---

### 6. **Versioning**
- SOPs, schemas, and critical governance docs must carry a **version number** (`vX.Y`).  
- Increment version when:
  - **Minor update** → bump `Y` (e.g., `v1.1`).  
  - **Major change** → bump `X` (e.g., `v2.0`).  

---

### 7. **Packaging Updates**
- When multiple files are updated together, bundle into a `.zip` with:  
  - Updated files  
  - `DELTA_README.md` describing changes, timestamps, versions  

---

## ✅ Outcome
- Every file is self-describing with metadata.  
- Every update is timestamped and logged.  
- Navigation and indexing remain intact.  
- Repo maintains consistency across all docs.
