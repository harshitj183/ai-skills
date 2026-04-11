# 🎨 Tailwind CSS & UX Mastery Mega-Skill

This skill enforces high-fidelity UI/UX principles using Tailwind CSS, focusing on professional design aesthetics, accessibility, and performance.

## 🎯 Design Directives

### 1. Minimalist Execution
- Avoid "Flashy for No Reason". Every shadow and border-radius must serve a cognitive load reduction purpose.
- Use `slate` or `zinc` for neutrals. Never use pitch black `#000000` unless for specific OLED optimization; use `zinc-950` instead.

### 2. Typographic Hierarchy
- Enforce `antialiased` text.
- Use `tracking-tight` for large headings (h1, h2).
- Use `leading-relaxed` for long-form body text to improve readability.

### 3. Surface & Elevation (Glassmorphism)
- Use standard elevation layers:
  - `bg-white/5` with `backdrop-blur-md` for dark mode surfaces.
  - `ring-1 ring-white/10` for subtle borders on surfaces.
  - `shadow-2xl shadow-indigo-500/10` for focused elements.

### 4. Color Palette Mastery
- **Action Colors**: Use `indigo-600` for primary, `rose-500` for danger, `emerald-500` for success.
- **Gradients**: Use 2-step soft gradients (`from-indigo-600 to-violet-600`). Avoid 3+ color rainbows.

## 🛠️ Utility Patterns

### Layout
- Use `grid` with `gap-6` as the standard spacing for dashboard items.
- Use `container mx-auto px-4` for page-level centering.

### Interactive Elements
- **Buttons**:
  ```html
  <button class="inline-flex items-center justify-center px-4 py-2 text-sm font-medium transition-all duration-200 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white active:scale-95 shadow-sm">
    Action
  </button>
  ```
- **Inputs**:
  ```html
  <input class="w-full px-3 py-2 text-sm bg-zinc-900 border border-zinc-800 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all" />
  ```

### Animation
- Use `transition-all duration-200 ease-in-out`.
- Use `hover:scale-[1.02]` sparingly for interactive cards.

## 🚫 Anti-Patterns to Avoid
- **No `px-` and `py-` in every element**: Use `space-x-` or `space-y-` on parent containers when possible.
- **No Arbitrary Values**: Avoid `top-[13px]`. Use standard Tailwind increments (`top-3` or `top-4`).
- **No Over-saturation**: Don't use `bg-blue-500` for backgrounds; use a very light tint `bg-blue-50/50` or dark `bg-blue-950`.

---
*Created by Antigravity | Contribution #1 by AI*
