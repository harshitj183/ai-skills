---
name: "Meta-Skill Architect"
description: "Authoring and refining high-fidelity agentic superpowers for this library."
---

# 1. Authoring Protocol
When requested to create/modify a "Mega-Skill":
- **Constraint-First Design**: Define what the AI *cannot* do first.
- **Hierarchical Instruction**: Use `---` for metadata headers and `⚡ Smart AI Skills Library` for signatures.
- **Workflow Visualization**: Every complex skill MUST have a Mermaid flow charting its logic.

# 2. Design Thinking
- **Compression**: Minimize instruction token count without losing fidelity. Use bullet points and headers strategically.
- **Trigger Logic**: Use the `description` in the Metadata header as the primary trigger for LLM automatic skill adoption.
- **Best Practices Integration**: Refer to `anthropic_best_practices.md` and `google_standard_logic.md` (if available) for every new skill.

# 3. Validation
- Run `tests/validate_skills.py` after creating any new skill.
- Check for duplication or overlap with existing skills in the library.

# 4. Success Metrics
- 100% adherence to instructions in first-pass generation.
- No "hallucination" during skill-based workflows.

---
⚡ Smart AI Skills Library | v2.2.6 | Active
