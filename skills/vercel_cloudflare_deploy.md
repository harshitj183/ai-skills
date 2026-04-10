---
name: "Vercel & Cloudflare Deployment Master"
description: "Rules for Next.js, Edge Functions, Vercel configs, and Cloudflare Workers."
---

# Vercel Next.js Rules
1. **Edge Runtime:** Prefer edge runtime for middleware and lightweight route handlers. Understand Edge limits (1MB code size, 50ms startup).
2. **Caching:** Strategically use Incremental Static Regeneration (ISR) with `revalidate` over pure SSR or Client-side fetching for speed.
3. **Environment Variables:** Map to `production`, `preview`, and `development` safely. Never leak `NEXT_PUBLIC_` secrets.

# Cloudflare Workers
- Do not use Node.js specific standard libraries (like `fs`, `path`) in Cloudflare workers without compatibility flags.
- Rely on Workers KV for high-read low-write data, and Durable Objects for state orchestration.
- Respond rapidly. Execution limits exist. Keep it minimal and fetch externally optimally asynchronously.

---
⚡ Smart AI Skills Library | v2.2.7 | Active
