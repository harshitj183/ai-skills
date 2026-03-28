---
name: "Playwright Automation Tester"
description: "Rules for E2E testing using Playwright in web applications."
---

# Selection & Assertions
1. **Selectors:** Prefer user-facing attributes (`getByRole`, `getByText`, `getByLabel`) over brittle CSS selectors or XPaths.
2. **Auto-waiting:** Never use explicit timeouts (e.g., `page.waitForTimeout(5000)`). Rely entirely on Playwright's built-in auto-waiting assertions (`await expect(locator).toBeVisible()`).

# Mocking & Authentication
- Intercept and mock API calls heavily using `page.route` to create reliable, fast tests without backend dependencies.
- Reuse authentication state across browser contexts using `storageState` instead of logging in manually every single test wrapper.

---
⚡ Smart AI Skills Library | v2.2.6 | Active
