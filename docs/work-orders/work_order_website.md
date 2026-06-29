# 📝 Work Order: Swan Recruitment – Company Website (swan-website)

**Last updated:** 2025-09-27  
**Backlinks:** [Master WO (Full)](work_order_master__FULL.md) · [Work Orders Index](work_orders_index.md)

## 🎯 Objective
Build a **public-facing website** for Swan Recruitment that establishes credibility, explains services, and provides a clear entry point to the **Contractor Portal**. The site must be **fast**, **accessible**, **SEO‑friendly**, and **easy to operate**.  
*(Expanded from your current work order skeleton covering setup, content, branding, portal link, forms, SEO, and deployment.)*

**Non‑goals (MVP)**
- Full CMS/editor experience (optional Phase 2+)
- Contractor account features (live in the Contractor Portal)
- Complex blog/news engine (simple static pages first)

---

## 🔑 Status Keys
🟡 Drafted · 🟦 In Progress · ✅ Complete · ⏸ Deferred  

**Status:** 🟡 Drafted

---

## 1) Project & Environments Setup
- [ ] Repository: `swan-website`
- [ ] Framework: **Next.js** (recommended for SSR/SEO) or Vite + React (static)
- [ ] Styling: TailwindCSS (+ optional shadcn/ui for components)
- [ ] Environments: `dev`, `staging`, `prod`
- [ ] Firebase Hosting:
  - [ ] Hosting targets for staging/production
  - [ ] **Preview channels** on pull requests
- [ ] Configuration:
  - [ ] `.env.local`, `.env.staging`, `.env.production` (no secrets in repo)
  - [ ] Base URL, GA4 ID, reCAPTCHA keys

**Deliverable:** Skeleton site builds locally and deploys to **staging** on merge.

---

## 2) Content & Pages
- [ ] **Home** — overview, value proposition, clear CTA to Contact & Contractor Portal
- [ ] **About** — company history, team, values
- [ ] **Services** — sectors (energy), contract model (PSC), capabilities
- [ ] **Contact** — form + full contact details, address
- [ ] **Legal** — Privacy Policy, Terms of Use, Cookies
- [ ] **Contractor Portal** — prominent “Contractor Login” CTA

**Structure**
- [ ] Pages as React/Next pages (`/pages` or `/app`) with content in Markdown/JSON for easy edits
- [ ] Shared components: Header, Footer, CTA blocks, Hero, Testimonials/Logos (optional)

**Deliverable:** All primary **static pages** authored and linked in nav & footer.

---

## 3) Design & Branding
- [ ] **Brand tokens**: colors, spacing, typography declared in Tailwind config
- [ ] **Logo & favicon** prepared at multiple resolutions
- [ ] **Responsive** grid (mobile‑first), tested on common breakpoints
- [ ] **Accessibility** (WCAG AA): semantic landmarks, aria labels, focus states, keyboard nav
- [ ] **Image optimisation**: Next/Image or build‑time compression
- [ ] **Performance budgets** for Core Web Vitals (LCP < 2.5s, CLS < 0.1)

**Deliverable:** Professional, on‑brand UI that passes **accessibility** checks.

---

## 4) Contractor Portal Integration
- [ ] “Contractor Login” button in header + hero CTA → links to **Contractor Portal** URL
- [ ] **Maintenance banner**: show if portal status = maintenance/outage
  - [ ] Read status from a lightweight flag in Firestore/RTDB or Control Tower health endpoint
- [ ] **Deep links** (optional): docs pages may link to portal help

**Deliverable:** Clear, reliable **entry point** into the portal from the website.

---

## 5) Contact & Forms
- [ ] Contact form (name, email, company, message)
- [ ] Validation (client + server)
- [ ] Backend: call **Firebase Function** to deliver mail to inbox (or log to CT for follow‑up)
- [ ] **Spam protection**: reCAPTCHA v3 or hCaptcha
- [ ] **GDPR**: consent checkbox, link to Privacy Policy, retention note (e.g., 12 months)

**Deliverable:** Secure, reliable contact flows with consent captured.

---

## 6) SEO & Analytics
- [ ] Meta titles/descriptions per page
- [ ] Open Graph & Twitter cards
- [ ] `sitemap.xml` + `robots.txt`
- [ ] Structured data (JSON‑LD): `Organization`, `WebSite`, `BreadcrumbList` (as applicable)
- [ ] Google Analytics (GA4) initialised via env var
- [ ] **Cookie consent** banner if analytics enabled

**Deliverable:** Site **discoverable** and **measurable** from day one.

---

## 7) Performance
- [ ] Static generation where possible (ISR/SSG for Next.js)
- [ ] Asset caching headers, gzip/brotli
- [ ] Lazy‑load non‑critical images/components
- [ ] Preload critical fonts; use system fonts as fallback
- [ ] Lighthouse workflow in CI (budgets for LCP/CLS/TTI)

**Deliverable:** CI shows stable **Core Web Vitals** within budget.

---

## 8) Deployment & CI/CD
- [ ] GitHub Actions:
  - [ ] Lint & type check
  - [ ] Unit tests (if any)
  - [ ] Build site
  - [ ] Deploy to **Firebase Hosting**:
    - Preview on PR
    - Staging on merge to `main`
    - Production on tag (e.g., `v0.1.0`)
- [ ] Rollback doc (how to revert to previous channel/deploy)

**Deliverable:** Automated deployments to staging/prod with **preview URLs**.

---

## 9) Observability & Monitoring
- [ ] Uptime check (simple scheduled ping or Control Tower probe)
- [ ] Error logging (client) to a central collector
- [ ] 404/500 reporting
- [ ] Daily status digest to ops (optional, via CT)

**Deliverable:** Basic **operational visibility** for the public site.

---

## 10) Milestones
**Phase 1 — Skeleton**
- Repo created; framework initialised; Hosting target configured

**Phase 2 — Content**
- Home, About, Services, Contact, Legal authored

**Phase 3 — Branding & Accessibility**
- Brand tokens applied; WCAG AA checks pass

**Phase 4 — Portal Integration**
- Contractor Login CTAs + maintenance banner wired

**Phase 5 — Deploy & Monitor**
- CI/CD to staging/prod; uptime + error logging in place

---

## 11) Acceptance Criteria (MVP)
- [ ] Pages render with correct content + metadata
- [ ] Contractor Login visible and links to portal
- [ ] Contact form sends and records consent
- [ ] Sitemap & robots accessible; GA4 events visible
- [ ] CI builds; staging deploys on merge; prod deploys on tag
- [ ] Lighthouse budgets met on staging

---

## 12) Risks & Mitigations
| Risk | L | I | Mitigation |
|---|:--:|:--:|---|
| Poor Core Web Vitals | M | M | Image optimisation, code‑split, cache headers |
| SEO misconfig | M | M | CI checks for sitemap/robots/meta |
| Broken portal link | L | H | E2E test for CTA; maintenance banner |
| Form spam | H | M | reCAPTCHA + rate limiting |
| PII handling in forms | L | H | Consent + retention policy; secure function |

---

## 13) Related Documents
- [Work Order Master](../work_order_master.md)
- [Phase Plans Index](../plans/phase_plans_index.md)
- [Contractor Portal Work Order](work_order_contractor_portal.md)
- [Control Tower Work Order](work_order_control_tower.md)
- [Vision Docs Index](../design/vision_index.md)

---

> Notes: This work order expands the original items (setup, content pages, branding, portal integration, forms, SEO, deployment) into an **execution‑ready** plan with accessibility, performance, observability, and acceptance criteria baked in.
---

### 📏 Canonical Data Rules (Swan)
- Use **snake_case** field names; FKs end with **`_id`**.
- Money uses `{ "amount_minor": int, "currency": "GBP" }` (no floats).
- Dates = `*_date` (date) and `*_at` (datetime, ISO-8601).
- Import common types from **[`../schemas/common/common.json`](../schemas/common/common.json)**.
- Follow **PII redaction** policy in **[`../schemas/PII_POLICY.md`](../schemas/PII_POLICY.md)**.
- See **Field Lineage**: **[`../design/field_lineage.md`](../design/field_lineage.md)**.
