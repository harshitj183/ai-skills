---
name: "Progressive Disclosure"
description: "Optimizing AI context window via dynamic, tiered instruction loading."
---

# 1. Mission Strategy
- Prevent "context drowning" — only load the instruction blocks relevant to the *immediate task*.
- Use these tiers to manage your focus:

```mermaid
graph TD;
    A[Core Engine: SKILL.md] --> B[Tier 1: Master Role (High-Level Task)];
    B --> C[Tier 2: Mega-Skill (Specific Feature)];
    C --> D[Tier 3: Supporting Documentation (Detailed Reference)];
```

# 2. Execution Guidelines
- **Lazy Loading**: When the user requests a broad feature, load the Master Role. When the first sub-task is identified, load the corresponding Mega-Skill.
- **Context Clearing**: When a task is 100% complete, acknowledge the outcome and implicitly drop that specific skill's context unless it's needed for the next step.
- **Reference Paths**: Always reference skills by their full path in the library to enable easy retrieval for yourself.

# 3. Dynamic Precision
- If a skill is too broad, create a specialized "fragment" or "skill-variant" for the current task on-the-fly, but always keep it consistent with the parent library.

---
⚡ Smart AI Skills Library | v2.2.7 | Active
