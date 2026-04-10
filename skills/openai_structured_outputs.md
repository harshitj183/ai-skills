---
name: "OpenAI Structured Outputs Expert"
description: "Rules for extreme JSON schema strictness and function calling optimizations."
---

# Function Calling Optimization
1. **JSON Schema Strictness:** Enforce `strict: true` validation on all `response_format` JSON Schema definitions. Do not use generic `object` types without defined explicit properties.
2. **Hallucination Prevention:** When returning enum arrays, reject all outputs not exactly mapping to the predefined subset.
3. **System Prompt Alignment:** Embed function definitions within the system instruction block rather than heavily relying on implicit user prompts to guess shapes.

---
⚡ Smart AI Skills Library | v2.2.9 | Active
