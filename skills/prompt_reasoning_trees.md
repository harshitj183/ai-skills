---
name: "Advanced Prompt Reasoning Trees"
description: "Rules for Chain-of-Thought, ReAct parsing, and Self-Reflection loops."
---

# Cognitive Pathways
1. **Chain-of-Thought (CoT):** Always wrap internal thoughts in `<thought>` tags before executing tools. Force step-by-step logic expansion.
2. **ReAct Loop:** When an agent encounters an error, it must actively evaluate the error context via a reflection step and correct its subsequent tooling schema.
3. **Task De-cluttering:** If a prompt exceeds context bounds, summarize the highest priority action into a single granular task step instead of attempting a 500-file refactor simultaneously.

---
⚡ Smart AI Skills Library | v2.2.6 | Active
