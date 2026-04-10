---
name: "Antigravity OS & Workflow Mastery"
description: "Advanced interaction rules for CLI invocation, bash routing, and OS-level operations."
---

# CLI Orchestration
1. **Parallel Tooling:** Maximize parallel CLI invocations using `run_command` concurrently across batch jobs if states don't mutually conflict.
2. **Terminal Scraping:** Never use raw `cat` for files larger than 1000 lines. Default to `grep_search` and `view_content_chunk` to prevent context explosion.
3. **Activation Scripts:** Handle agent overload gracefully in Windows/Linux by slicing stdout responses and avoiding infinite crash loops in stderr rendering.

# Workflow Bundling
- Construct workflows as strict YAML-frontmatter markdown files with `// turbo` tags to permit specific safe auto-execution loops for repetitive tasks.

---
⚡ Smart AI Skills Library | v2.2.9 | Active
