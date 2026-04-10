---
name: "React & Next.js Best Practices Master"
description: "Vercel's official guidelines for React Server Components, Suspense, and Composition."
---

# React Server Components (RSC)
1. **Default to Server:** Every component without `useState`, `useEffect`, or DOM events should remain a Server Component.
2. **Client Boundaries:** Push `"use client"` as low down the component tree as possible. Only wrap interactive islands, never the entire page layout.
3. **Data Fetching:** Fetch data on the Server Component level and pass it down as props. Do not use `useEffect` for data fetching unless absolutely necessary for infinite polling.

# Composition Patterns
- **Do not drill props excessively:** If passing props more than 3 levels deep, use React Context or Composition (passing `children` or JSX slots).
- **Suspense Wrappers:** Always wrap async Server Components with `<Suspense fallback={<Skeleton />}>` to prevent blocking the entire UI stream.

---
⚡ Smart AI Skills Library | v2.2.7 | Active
