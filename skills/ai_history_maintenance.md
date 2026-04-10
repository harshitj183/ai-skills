---
name: "🤖 AI History Maintenance Skill"
description: "This skill provides mandatory instructions for AI agents working on the `@harshitj183/ai-skills` project to maintain history."
---

# 🤖 AI History Maintenance Skill

This skill provides mandatory instructions for AI agents working on the `@harshitj183/ai-skills` project to maintain project history and transparency.

---

## 🧐 Skill Summary
Empowers AI agents to systematically document their actions, changes, and milestones within the project's dedicated `history/CONTEXT.md` system.

## 🛠️ Implementation Guide

### 1. Mandatory Updates
After completing any major task (e.g., adding a new skill, fixing a bug, updating configurations), you **MUST** update the master context file:
- **`history/CONTEXT.md`**: Append or update the relevant section with your AI name, date, and a bulleted list of tasks performed or changes made.

### 2. Format and Tone
- Use professional, clear markdown.
- Maintain structured sections (e.g., Activity Log, System Architecture, Current Status).
- Include dates in `YYYY-MM-DD` or `Month DD, YYYY` format in the Activity Log section.
- Always sign the update with `*Last updated by: AI Assistant (<Name>)*`.

### 3. Verification
Before concluding any session, verify that:
- The `history/CONTEXT.md` file accurately reflects the current state of the project.
- No other scattered history files are created, maintaining the single-file context principle.

## 🌟 Best Practices
- **Proactive Documentation**: If you see a gap in history, fill it immediately in `CONTEXT.md`.
- **Continuous Logging**: Update logs incrementally during long-running tasks.
- **Context Awareness**: Read the `CONTEXT.md` file at the start of any new session to understand previous work and milestones.

### 4. Data Sensitivity & Privacy (CRITICAL)
- **NO PII/Secrets**: Never write API keys, passwords, bearer tokens, or sensitive Personally Identifiable Information (PII) to `CONTEXT.md` or logs.
- **Abstract Logic**: Describe *what* you did (e.g., "Updated auth logic") rather than showing the literal credentials or private data.
- **Audit Logs**: If you accidentally log a secret, rotate it immediately and scrub the history files.

---
*Signed: AI History Architect*

---
⚡ Smart AI Skills Library | v2.2.7 | Active
