---
name: "Supabase Architect"
description: "Supabase & PostgreSQL security, migrations, and best practices."
---

# Database Guidelines
1. **Migrations First:** Never execute destructive raw SQL via editors. Always use `supabase migration new` and apply via `supabase db push`.
2. **Row Level Security (RLS):** Every table MUST have `ENABLE ROW LEVEL SECURITY`. Default to denying all access, then specify explicit `CREATE POLICY` for `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
3. **Indexing:** Add indices for any column used frequently in `WHERE` clauses, foreign keys, or `ORDER BY`.

# Edge Functions
- Always use standard Deno environments for Edge Functions. 
- Validate JWTs heavily (use `verify_jwt: true` default).
- Don't deploy bloated dependencies; prefer standard libraries.

---
⚡ Smart AI Skills Library | v2.2.9 | Active
