 <div align="center">
   
  <img src="assets/logo.png" width="60" alt="Smart AI Skills Logo" />
  <h1>Smart Instructions Library of AI Skill</h1>

  <p>
    <a href="https://www.npmjs.com/package/@harshitj183/ai-skills"><img src="https://img.shields.io/npm/v/@harshitj183/ai-skills.svg?style=for-the-badge&color=blue" alt="npm version"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License: MIT"></a>
    <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge" alt="PRs Welcome"></a>
  </p>


 
  <img src="assets/banner.png" width="850" alt="AI Skills CLI Dashboard" />
  <br />
  <p><em>The ultimate repository of compressed, high-fidelity AI developer skills.</em></p>
</div>

Welcome to the **Ultimate AI Skill Library**. We analyzed over **1,200+ raw skills** from top official repositories across the globe (*Vercel, Anthropic, HashiCorp, Microsoft, OpenAI, Letta, Composio, Stripe, Supabase*) and compressed them into a perfectly engineered, hyper-specialized vault of **17 Mega-Skills** and **8 Master Roles**.

This library gives your AI agents extreme precision, bypassing general hallucinations entirely, and enforcing industry-standard architecture straight into their context windows.

---

## <img src="https://cdn.simpleicons.org/npm" width="24" align="center" /> Quickstart: The Smart CLI

Our interactive CLI module gives you absolute control over what skills are deployed and auto-configures your IDE.

```bash
npx @harshitj183/ai-skills init
```

<p align="center">
  <img src="assets/init_demo.png" width="700" alt="CLI Init Demo" />
</p>

### Available Commands:
1. **`init`** – Installs the full library quietly by default (perfect for letting your AI agent select skills dynamically).
   - `npx @harshitj183/ai-skills init -i` (Interactive picker)
   - `npx @harshitj183/ai-skills init -r frontend_expert.md -s react_best_practices.md` (CLI filtering)
2. **`configure`** – Auto-detects and writes the rules file for your specific IDE (`.cursorrules`, `.windsurfrules`, `CLAUDE.md`, etc.).
3. **`update`** – Safely pulls the newest official skills from the registry without overwriting your custom skills.
4. **`create <skill_name>`** – Scaffolds a new highly-optimized custom Mega-Skill inside `smart-instructions/custom/`.
5. **`fetch <skill_name>`** – Fetches an external skill from the 100+ curated options in the Skill Bank registry.

---

## <img src="https://cdn.simpleicons.org/graphql" width="24" align="center" /> Architecture: What is Included?

```mermaid
graph TD;
    A[SKILL.md - Master Rulebook] --> B[Roles Directory];
    A --> C[Mega-Skills Directory];
    B --> D(Backend Expert);
    B --> E(Frontend Expert);
    B --> F(System Engineer);
    C --> G(Supabase Architecture);
    C --> H(Cloudflare Edge Deploy);
    C --> I(OpenAI Strict Models);
```

### 1. The Core Engine (`SKILL.md`)
The central controller. This file dictates how the AI behaves: commanding aggressive accuracy, strictly typed JSON generation, minimal boilerplate, and routing prompts automatically to the correct roles.

### 2. The 8 Master Roles (`roles/`)
Eliminate the need for extensive prompting. Just tag a role file.
- `backend_expert.md`, `frontend_expert.md`, `gpt5_core.md`, `subagent_orchestrator.md`, `code_reviewer.md`, `product_manager.md`, `security_auditor.md`, `technical_writer.md`, `ui_ux_designer.md`, `wisdom_extractor.md`

### 3. The 17 Mega-Skills (`skills/`)
Give your AI absolute technical dominance over specific frameworks.

| Category | Skills Included | Example Technologies |
| :--- | :--- | :--- |
| **<img src="https://cdn.simpleicons.org/fastapi" width="16" align="center"/> Orchestration (WAVE 4)** | `parallel_agent_dispatcher.md`, `plan_architect.md`, `plan_executor.md`, `external_skill_retrieval.md` | Concurrent subagents, Blueprints, Skill Bank fetching |
| **<img src="https://cdn.simpleicons.org/vlc" width="16" align="center"/> Engineering (WAVE 3)** | `tdd_mastery.md`, `systematic_debugging.md`, `progressive_disclosure.md`, `writing_skills.md` | Red-Green-Refactor, Wolf-Fence, Context Optimization, Meta-Skill |
| **<img src="https://cdn.simpleicons.org/amazonwebservices" width="16" align="center"/> Infrastructure** | `mcp_master.md`, `hashicorp_terraform.md`, `azure_graph_integrator.md`, `antigravity_mastery.md` | Terraform, Azure AD, MCP Servers |
| **<img src="https://cdn.simpleicons.org/react" width="16" align="center"/> Frontend & Apps** | `react_best_practices.md`, `react_native_performance.md`, `playwright_testing.md` | React 19, Expo, Playwright |
| **<img src="https://cdn.simpleicons.org/supabase" width="16" align="center"/> Backend & APIs** | `supabase_architect.md`, `stripe_integration.md`, `openai_structured_outputs.md` | PostgreSQL, Stripe, OpenAI |
| **<img src="https://cdn.simpleicons.org/antigravity" width="16" align="center"/> Orchestration** | `composio_integrator.md`, `sanity_architecture.md`, `vercel_cloudflare_deploy.md`, `github_automation.md` | Next.js, Cloudflare, Sanity CMS |
| **<img src="https://cdn.simpleicons.org/anthropic" width="16" align="center"/> AI Reasoning** | `prompt_reasoning_trees.md`, `letta_agent_memory.md`, `anthropic_documents.md` | Claude, ReAct, Memory Persistence |

---

## 📚 Professional Documentation

Visit our full documentation folder for a deep dive into every feature:
- **[System Architecture](docs/architecture.md)**: Technical design and hierarchical roles.
- **[CLI Power User Guide](docs/cli-guide.md)**: Speeding up your workflow with `init`, `update`, and `create`.
- **[AI History System](docs/history-system.md)**: Why and how your AI should track its actions.
- **[Contribution Guide](docs/contribution-guide.md)**: Help us grow the world's best AI skill library.

---

## 🏛️ AI History Tracking (v2.2.7 Update)

Version 2.2.7 consolidates the built-in History tracking system into a single, robust file. When you initialize the library, it creates a private `history/` folder in your project that allows AI agents to maintain a timeline of their actions, achievements, and technical decisions.

<p align="center">
  <img src="assets/history_preview.png" width="750" alt="AI History Tracking Preview" />
</p>

- **`history/CONTEXT.md`**: The master context file that tracks AI activity logs, project milestones, system architecture decisions, and current project status in one unified document. This significantly improves AI reasoning consistency by keeping all context in one place.

---

## 🏦 Dynamic Skill Retrieval (Skill Bank)

Version 2.2.7 introduces direct CLI access to the **Skill Bank** system. If you need a technical capability that isn't currently in the local library, you can autonomously search, fetch, and standardize instructions from a curated list of top-tier external repositories directly from the terminal.

- **`registry/skill_bank.json`**: An internal database of **100+ high-fidelity AI instruction repositories** covering Backend, Frontend, Cloud, AI, and Security.
- **`npx @harshitj183/ai-skills fetch <skill_name>`**: A powerful CLI command to autonomously fetch any external skill from the registry. The CLI handles pathing, standardization, and YAML metadata formatting.
- **Zero-Boilerplate Integration**: Automatically standardizes external rules into our high-fidelity signature format, saved directly to `smart-instructions/skills/external/`.

---

## <img src="https://cdn.simpleicons.org/github" width="24" align="center" /> Usage Across AI Platforms

Run the installer once in your project root, then configure your preferred AI tool:

```bash
npx @harshitj183/ai-skills init
```

This places all files inside `smart-instructions/` in your project. Your `.gitignore` is automatically updated.

---

### <img src="https://cdn.simpleicons.org/visualstudiocode" width="18" align="center" /> 1. Cursor IDE
Rename `smart-instructions/SKILL.md` to `.cursorrules` at your project root. Every Cursor chat will automatically follow the rules.
```
mv smart-instructions/SKILL.md .cursorrules
```
Or reference individual skills surgically:
> *"@react_best_practices.md implement a new dashboard."*

---

### <img src="https://cdn.simpleicons.org/anthropic" width="18" align="center" /> 2. Claude Code (CLI)
Claude Code auto-reads `CLAUDE.md` from your root. Copy the contents:
```bash
cp smart-instructions/SKILL.md CLAUDE.md
```
Or tell Claude directly: *"Read `smart-instructions/SKILL.md` as your core directive."*

---

### <img src="https://cdn.simpleicons.org/openai" width="18" align="center" /> 3. ChatGPT (Web / Custom GPT)
**Option A — Custom Instructions:**
- Go to Settings → Custom Instructions → paste contents of `SKILL.md`

**Option B — Project Knowledge (ChatGPT Plus):**
- Create a new Project → Upload `SKILL.md` and any skill files you need

**Option C — Chat Upload:**
- Attach `SKILL.md` directly to your conversation as a file

---

### <img src="https://cdn.simpleicons.org/githubcopilot" width="18" align="center" /> 4. GitHub Copilot (VS Code)
Copy instructions to the Copilot-specific file:
```bash
cp smart-instructions/SKILL.md .github/copilot-instructions.md
```
Or reference in chat: *"#file:smart-instructions/react_best_practices.md refactor this component."*

---

### <img src="https://cdn.simpleicons.org/google" width="18" align="center" /> 5. Gemini / Antigravity (Google)
Tell Antigravity: *"Read `smart-instructions/SKILL.md` and act according to the Roles inside."*
Antigravity automatically detects skill files in your workspace.

---

### <img src="https://cdn.simpleicons.org/codium" width="18" align="center" /> 6. Windsurf IDE (Codeium)
Windsurf supports `.windsurfrules` file:
```bash
cp smart-instructions/SKILL.md .windsurfrules
```

---

### <img src="https://cdn.simpleicons.org/zedindustries" width="18" align="center" /> 7. Zed Editor
Add to Zed's AI assistant context:
- Settings → Assistant → System Prompt → paste `SKILL.md` contents

---

### 8. Cline / Continue.dev (VS Code Extensions)
Place the skill files in `.clinerules` or `.continuerules`:
```bash
cp smart-instructions/SKILL.md .clinerules
```
For Continue.dev, add to `config.json` under `systemMessage`.

---

### 9. Aider (Terminal AI)
```bash
aider --read smart-instructions/SKILL.md
```

---

### 10. Any LLM API (OpenAI, Groq, Mistral, Llama)
Paste `SKILL.md` content as your `system` message in the API call:
```javascript
{ role: "system", content: fs.readFileSync("smart-instructions/SKILL.md", "utf8") }
```

---

## Open Source & Community

We are actively maintaining this library to continuously fuse the latest breakthroughs from top tech teams into single mega-skills. Found a massive repo with a great deployment guide? Compression is welcome! PRs are open.

---

## 👨‍💻 Connect & Follow

Stay updated with the latest AI skills and architectural breakthroughs:

- **Follow me on GitHub**: [@harshitj183](https://github.com/harshitj183)
- **Check out my other projects**: [Harshit's Repositories](https://github.com/harshitj183?tab=repositories)

---

**License:** MIT
