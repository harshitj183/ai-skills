---
name: "Letta Agent Memory Manager"
description: "Rules for long-term memory management, persistent context, and core Letta-style memory blocks."
---

# Core Memory Blocks
1. **Persona Update:** Agents must actively call `core_memory_append` to update their understanding of the user state or global variable states.
2. **Archival Memory:** Use archival search strategies for infinite-context scrolling. Avoid overloading context windows.
3. **Context Truncation Alert:** Always respond gracefully if `warning_context_limit` triggers by summarizing preceding events into the core memory block and continuing.

# Best Practices
- Agents run indefinitely. Maintain context continuity strictly via memory, never rely on conversation history alone.

---
⚡ Smart AI Skills Library | v2.2.7 | Active
