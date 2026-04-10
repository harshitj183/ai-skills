---
name: "HashiCorp Terraform Auto-Deployer"
description: "HCL code generation and AWS/GCP Provider orchestration."
---

# Terraform Module Generation
1. **State Isolation:** Never use a single unified `apply` for an entire company stack. Isolate state using Workspaces or entirely separate `prod/`, `staging/` directories.
2. **Data Variables:** Hardcode absolutely nothing. Use `variables.tf` heavily and separate environment tiers via `terraform.tfvars`.
3. **Provider Pinning:** Always pin provider versions inside the `required_providers` block block to prevent breaking API changes from propagating automatically.

# Best Practices
- Output strictly what is necessary (e.g., Load Balancer URLs) to prevent leaking exact subnet or SG configurations.
- Default to `for_each` over `count` when looping to avoid shifting indices issues upon list modifications.

---
⚡ Smart AI Skills Library | v2.2.9 | Active
