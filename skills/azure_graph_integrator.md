---
name: "Microsoft Graph & Azure Integrator"
description: "Rules for Azure AD tokens, Graph API requests, and Enterprise app setup."
---

# Graph API Best Practices
1. **Token Scopes:** Request explicit `Mail.ReadWrite`, `User.Read` only based on what the application specifically mutates. Never use `Directory.ReadWrite.All` carelessly.
2. **Pagination Enforcement:** Implement strictly `odata.nextLink` tracking when querying users or large resource collections.
3. **Batching:** Reduce network overhead by clustering up to 20 sub-requests via `/$batch` endpoints when orchestrating multi-user mutations.

---
⚡ Smart AI Skills Library | v2.2.9 | Active
