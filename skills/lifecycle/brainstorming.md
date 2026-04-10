---
name: "Idea-to-Spec Workflow"
description: "High-fidelity brainstorming to transform raw user ideas into technical specifications."
---

# 1. Ideation Flow

```mermaid
graph LR;
    A[Idea/Problem] --> B[Stakeholder Needs];
    B --> C[Constraint Mapping];
    C --> D[Solution Drafting];
    D --> E[Feasibility Check];
    E --> F[Core Spec];
```

# 1. Protocol Logic
When a user provides a raw idea or a vague request:
- **Challenge Assumptions**: Ask "Why?" and "What is the core user pain point?".
- **Constraint Identification**: List what is NOT being built.
- **Architectural Mapping**: Determine which `roles/` and `skills/` from the library will be needed for this feature.

# 2. Review Protocol

```mermaid
sequenceDiagram
    participant U as User
    participant AI as System
    AI->>U: Present Micro-Spec
    U->>AI: Provide Feedback
    AI->>AI: Refine Spec
    AI->>U: Confirm Final Design
```

# 3. External Skill Retrieval

```mermaid
graph TD;
    A[Task Requirement] --> B{Skill Library};
    B -->|Match Found| C[Load Skill Module];
    B -->|No Match| D[Generate Custom Logic];
    C --> E[Execute Task];
    D --> E[Execute Task];
```

# 4. Output: The Micro-Spec
- **Goal**: One sentence.
- **Features**: Bullet list of MUST-HAVEs.
- **Edge Cases**: Identify 3-5 failure modes.
- **Plan**: Hand-off to `skills/orchestration/plan_architect.md`.

# 3. Collaborative Loop
- Present the Micro-Spec to the user.
- Incorporate one round of feedback.
- Confirm final design before implementation.

---
⚡ Smart AI Skills Library | v2.2.7 | Active
