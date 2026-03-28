---
name: "Systematic Debugging"
description: "Expert-level problem isolation and precision debugging methodologies."
---

# 1. The Wolf-Fence Algorithm
Search for bugs by bisecting the system:

```mermaid
graph TD;
    A[Identify Symptom] --> B[Draw Boundary];
    B --> C{Bug Is Here?};
    C -- Yes --> D[Divide and Conquer (Repeat)];
    C -- No --> E[Widen Scope];
    D --> F[Identify Root Cause];
    F --> G[Verify Fix];
```

# 2. Precision Mapping
- **Log Mining**: Capture and analyze application and environment logs.
- **Trace Analysis**: Trace data flow step-by-step from input to error.
- **Isolated Testing**: Create a minimal reproduction environment (MRE) that exists outside the main project context.

# 3. Delta Debugging
1. **Identify**: Find a "good" state and a "bad" state.
2. **Minimize**: Find the smallest set of changes (code, data, config) that transformed "good" into "bad".
3. **Isolate**: Correct the specific delta without affecting unrelated logic.

# 4. Anti-Regression Protocol
- Every bug fix **MUST** be accompanied by a regression test that would have caught it.
- Re-run the entire test suite before proposing the final fix.

---
⚡ Smart AI Skills Library | v2.2.6 | Active
