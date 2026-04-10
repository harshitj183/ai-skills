---
name: "GitHub Automation Expert"
description: "Rules for branching, merging, rebasing, CI/CD Actions, and PR generation."
---

# Git Workflow
1. **Commit Messages:** Follow Conventional Commits format exactly: `feat(scope): message` or `fix(scope): message`.
2. **Rebasing:** Prefer rebasing over merge commits to keep the history linear. Warn against rebasing public branches.
3. **Conflict Resolution:** Never just guess. Always evaluate `<<<<<<< HEAD` blocks contextually based on recent timeline logic.

# GitHub Actions
- Keep workflows DRY. Use reusable workflows or composite actions for repeating test steps.
- Set explicit read/write permissions for `GITHUB_TOKEN`.
- Optimize action caching mapping (e.g. `actions/cache` or `setup-node` caching).

---
⚡ Smart AI Skills Library | v2.2.9 | Active
