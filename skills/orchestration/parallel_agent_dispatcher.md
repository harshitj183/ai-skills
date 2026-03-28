---
name: "Parallel Agent Dispatcher"
description: "High-fidelity management of multiple concurrent worker agents."
---

# 1. Dispatching Protocol
When tackling tasks with decoupled logical components, split the work:

```mermaid
graph TD;
    A[Main: Coordinator] --> B[Sub: Worker A (Features)];
    A --> C[Sub: Worker B (Tests)];
    A --> D[Sub: Worker C (Docs)];
    B --> E[Review Output];
    C --> E;
    D --> E;
    E --> F[Merge & Finalize];
```

# 2. Scope Isolation
- **Context Pinning**: Each subagent gets *only* the specific files or requirements for their chunk.
- **Dependency Map**: Before dispatching, define clear interfaces or mock expectations if subagents' outputs depend on each other.

# 3. Conflict Resolution
- If two subagents propose conflicting architecture, the **Coordinator** (Main) must pause, resolve the conflict, and re-dispatch with a unified "System Design Directive".

# 4. Success Criteria
- Parallel tasks complete without logical drift.
- Final merge is verified by the Coordinator before being presented.

---
⚡ Smart AI Skills Library | v2.2.6 | Active
