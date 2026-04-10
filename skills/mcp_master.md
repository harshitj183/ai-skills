---
name: "MCP Master Guidelines"
description: "Rules for building Model Context Protocol (MCP) servers and tools."
---

# MCP Architecture
1. **Server Instantiation:** Always use `@modelcontextprotocol/sdk/server/index.js` and `StdioServerTransport`.
2. **Schema Definition:** Define strictly typed input schemas using `zod` and map them to `ListToolsRequestSchema`.
3. **Execution Handling:** Map each named tool to its logic block inside `CallToolRequestSchema`. Parse inputs rigorously.

# Core Principles
- Treat MCP tools as pure functions; inputs go in, localized results come out. No global state side-effects.
- Provide comprehensive error handling. Never crash the stdio transport.
- Return responses strictly in the format `[{ type: "text", text: resultString }]`.

---
⚡ Smart AI Skills Library | v2.2.9 | Active
