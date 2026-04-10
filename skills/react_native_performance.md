---
name: "React Native Performance"
description: "Rules for Expo, React Native upgrades, and mobile UI rendering."
---

# Rendering Optimization
1. **Avoid Anonymous Functions in Renders:** Pass memoized functions down to child components to prevent excessive re-rendering.
2. **Lists:** Use `@shopify/flash-list` over standard `FlatList` for massive performance gains in large lists.
3. **Images:** Pre-fetch and cache images robustly using `expo-image` over native Image.

# Upgrading Guidelines
- Never upgrade React Native manually by directly editing `package.json` blindly. Always consult the official React Native Upgrade Helper for native iOS/Android code changes.
- In Expo, strictly follow `npx expo install --fix` policies.

---
⚡ Smart AI Skills Library | v2.2.7 | Active
