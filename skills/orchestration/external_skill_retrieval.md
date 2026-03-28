---
name: "External Skill Retrieval"
description: "Dynamic expansion of the library by fetching skills from external repositories."
---

# 1. Trigger Condition
Activate this skill if:
- The user requests a technology or workflow (e.g., "Java optimizations", "Go concurrency") that is NOT present in the local `skills/` or `roles/` directory.
- A current task requires expert-level instructions for a specialized tool not yet modeled in the library.

# 2. Retrieval Protocol
1. **Identify the Gap**: Clearly define the missing capability.
2. **Access Skill Bank**: Read the internal registry at `registry/skill_bank.json` to get the list of external repository URLs and categories.
3. **Search & Fetch**:
   - Use the `browser_subagent` or `read_url_content` to search the top repositories (e.g., `awesome-cursorrules`) for the specific skill.
   - Look for `.cursorrules`, `SKILL.md`, or README files that contain technical instructions.
4. **Ingest & Standardize**:
   - Download the raw instruction text.
   - **MUST**: Pass the text through the `Meta-Skill Architect` (`skills/writing_skills.md`) to convert it into this library's high-fidelity format (YAML metadata, Mermaid diagrams, System Signature).
5. **Execute**: Once standardized, adopt the new skill immediately for the task.

# 3. Decision Log
- If a skill is fetched, record it in `history/ai_activity_log.md` as "External Skill Ingestion: [Skill Name] from [URL]".

# 4. Success Criteria
- The external skill is successfully adapted to the library's style.
- The user's request is fulfilled using the newly acquired 'superpower'.

---
⚡ Smart AI Skills Library | v2.2.6 | Active
