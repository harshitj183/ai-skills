---
name: "Parallel Agent Dispatcher"
description: "High-fidelity management of multiple concurrent worker agents using Wave Execution."
---

# 1. Wave Execution Protocol
Complex tasks must be broken into **Synchronous Waves** to prevent state pollution.

```mermaid
graph LR
    subgraph Wave1 [Wave 1: Strategy]
    A[Structure Agent] --> B[Architecture Logic]
    end
    subgraph Wave2 [Wave 2: Construction]
    C[Frontend Worker] --- D[Backend Worker] 
    D --- E[Database Worker]
    end
    subgraph Wave3 [Wave 3: Quality]
    F[QA Agent] --> G[Security Auditor]
    end
    Wave1 --> Wave2 --> Wave3
```

# 2. Inter-Agent Communication (Bus)
- **State Bucket**: Agents must write their progress to a shared `scratch/wave_output.json`.
- **Gating**: Wave 2 cannot start until Wave 1 results pass the **Coordinator's** validation.

# 3. Role Allocation
- **Worker A**: Implementer (Code generation).
- **Worker B**: Adversary (Edge cases and failure testing).
- **Worker C**: Refiner (Design polish and documentation).

# 4. Resource Gating
- Limit each agent to 3 specific file scopes to avoid context overflow.
- All code must pass `tests/validate_skills.py` before Wave 3 completion.

---
⚡ Smart AI Skills Library | v2.2.7 | Active
