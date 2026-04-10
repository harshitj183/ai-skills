---
name: "Sanity CMS Architect"
description: "Guidelines for scalable content modeling, GROQ, and Answer Engine Optimization (AEO)."
---

# Content Modeling
1. **Never use deep nesting for core content:** Break massive documents down into discrete `document` types and link them with `reference` types to maximize query flexibility.
2. **GROQ Projections:** Never use raw `*[_type == "post"]` without projections. Always map out specifically what the frontend needs: `*[_type == "post"] { title, slug, "authorName": author->name }`.
3. **Draft States:** Account for draft filtering. By default, ensure `!(_id in path("drafts.**"))` is applied to production API endpoint fetchers unless explicit Preview modes are active.

# SEO & AEO Patterns
- Embed rich schemas (JSON-LD) dynamically based on structured portable text arrays.
- Precompute image dimensions and `.lqip` blur hashes directly in GROQ so the UI never experiences Cumulative Layout Shift (CLS).

---
⚡ Smart AI Skills Library | v2.2.7 | Active
