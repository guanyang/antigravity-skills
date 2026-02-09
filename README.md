# Antigravity Skills

[简体中文](README.zh-CN.md) | [English](README.md)

Empower agents with professional capabilities in specific fields (such as full-stack development, complex logic planning, multimedia processing, etc.) through modular **Skills** definitions, allowing agents to solve complex problems systematically like human experts.

## 📂 Directory Structure

```
.
├── .claude-plugin/     # Claude plugin configuration files
├── skills/             # Antigravity Skills library
│   ├── skill-name/     # Individual skill directory
│   │   ├── SKILL.md    # Core skill definition and Prompt (Required)
│   │   ├── scripts/    # Scripts relied upon by the skill (Optional)
│   │   ├── examples/   # Skill usage examples (Optional)
│   │   └── resources/  # Templates and resources relied upon by the skill (Optional)
├── docs/               # User manual and documentation guides
├── scripts/            # Maintenance scripts
├── skills_sources.json # Skills synchronization source config
├── skills_index.json   # Skills metadata index
├── spec/               # Specification documents
├── template/           # New skill template
└── README.md
```

## 🔌 Compatibility

Antigravity Skills follow the universal **SKILL.md** format and can work seamlessly with any AI coding assistant that supports Agentic Skills:

| Tool Name (Agent) | Type | Compatibility | Project Path | Global Path |
| :--- | :--- | :--- | :--- | :--- |
| **Antigravity** | IDE | ✅ Full | `.agent/skills/` | `~/.gemini/antigravity/skills/` |
| **Claude Code** | CLI | ✅ Full | `.claude/skills/` | `~/.claude/skills/` |
| **Gemini CLI** | CLI | ✅ Full | `.gemini/skills/` | `~/.gemini/skills/` |
| **Codex** | CLI | ✅ Full | `.codex/skills/` | `~/.codex/skills/` |
| **Cursor** | IDE | ✅ Full | `.cursor/skills/` | `~/.cursor/skills/` |
| **GitHub Copilot** | Extension| ⚠️ Partial | `.github/skills/` | `~/.copilot/skills/` |
| **OpenCode** | CLI | ✅ Full | `.opencode/skills/` | `~/.config/opencode/skills/` |
| **Windsurf** | IDE | ✅ Full | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| **Trae** | IDE | ✅ Full | `.trae/skills/` | `~/.trae/skills/` |

> [!TIP]
> Most tools will automatically discover skills in `.agent/skills/`. For maximum compatibility, please clone/copy into this directory.

## 📖 Quick Start

### 1. Prepare the Skills Library
First, clone this repository locally (it is recommended to place it in a fixed location for global reference):
```bash
git clone https://github.com/guanyang/antigravity-skills.git ~/antigravity-skills
```

### 2. Install Skills (Symlink Method)
We strongly recommend using **Symbolic Links (Symlink)** for installation, so that when you update this repository via `git pull`, all tools will automatically sync the latest features.

#### 🔹 Method A: Project Level Installation
Enable skills only for the current project. Run in your project root:
```bash
mkdir -p .agent/skills
ln -s ~/antigravity-skills/skills/* .agent/skills/
```

#### 🔹 Method B: Global Level Installation
Enable skills by default in all projects. Run the corresponding command based on the tool; common examples:

| Tool Name | Global Installation Command (macOS/Linux) |
| :--- | :--- |
| **General** | `mkdir -p ~/.agent/skills && ln -s ~/antigravity-skills/skills/* ~/.agent/skills/` |
| **Claude Code** | `mkdir -p ~/.claude/skills && ln -s ~/antigravity-skills/skills/* ~/.claude/skills/` |
| **Antigravity** | `mkdir -p ~/.gemini/antigravity/skills && ln -s ~/antigravity-skills/skills/* ~/.gemini/antigravity/skills/` |
| **Gemini** | `mkdir -p ~/.gemini/skills && ln -s ~/antigravity-skills/skills/* ~/.gemini/skills/` |
| **Codex** | `mkdir -p ~/.codex/skills && ln -s ~/antigravity-skills/skills/* ~/.codex/skills/` |

#### 🔹 Method C: Claude Plugin Installation (Claude Code Only)
If you primarily use **Claude Code**, you can install with one click via the plugin marketplace (this method automatically handles skill loading):

```bash
# 1. Start Claude Code
# 2. Add the plugin marketplace
/plugin marketplace add guanyang/antigravity-skills

# 3. Install the plugin from the marketplace
/plugin install antigravity-skills@antigravity-skills
```

### 3. Using Skills
Enter `@[skill-name]` or `/skill-name` in the chat box to invoke them, for example:
```text
/canvas-design Help me design a 16:9 blog cover about "Deep Learning"
```

### 4. More Information
- **View Manual**: For detailed usage, please refer to [docs/Antigravity_Skills_Manual.en.md](docs/Antigravity_Skills_Manual.en.md).
- **Environment Dependencies**: Some skills rely on Python environments; please ensure your system has necessary libraries installed (e.g., `pdf2docx`, `pandas`, etc.).


## 🔄 Keeping in Sync

Many skills in this project originate from excellent open-source communities. To keep in sync with upstream repositories, you can update them in the following ways:

1.  **Configuration**: The `skills_sources.json` file in the root directory is pre-configured with the upstream repositories for major skills and usually does not need manual adjustment.
2.  **Run Sync**:
    You can choose to sync all skills or just a specific one:

    ```bash
    # Sync all configured sources
    ./scripts/sync_skills.sh

    # Sync only a specific source (e.g., anthropics-skills)
    ./scripts/sync_skills.sh anthropics-skills
    ```
    The script will automatically pull the latest code and update the corresponding skill directories.

    > **Note**: The `ui-ux-pro-max` skill has a special directory structure and does not support automatic synchronization via script for now. Please use its official installation command `uipro init --ai antigravity` to install or update.

## 🚀 Integrated Skills (Total: 55)

### 🎨 Creative & Design
These skills focus on visual expression, UI/UX design, and artistic creation.
- **`@[algorithmic-art]`**: Create algorithmic and generative art using p5.js code.
- **`@[canvas-design]`**: Create posters and artworks (PNG/PDF output) based on design philosophies.
- **`@[json-canvas]`**: Create and edit JSON Canvas files (`.canvas`) with nodes, edges, and groups (commonly used in Obsidian).
- **`@[frontend-design]`**: Create high-quality, production-grade frontend interfaces and Web components.
- **`@[ui-ux-pro-max]`**: Professional UI/UX design intelligence, providing full design schemes for colors, fonts, layouts, etc.
- **`@[web-artifacts-builder]`**: Build complex, modern Web apps (based on React, Tailwind, Shadcn/ui).
- **`@[theme-factory]`**: Generate matching themes for documents, slides, HTML, etc.
- **`@[brand-guidelines]`**: Apply Anthropic's official brand design specifications (colors, typography, etc.).
- **`@[remotion]`**: Best practices for Remotion - Video creation in React.
- **`@[web-design-guidelines]`**: Review UI code for Web Interface Guidelines compliance (accessibility, UX, design audit).
- **`@[slack-gif-creator]`**: Create high-quality animated GIFs optimized specifically for Slack.

### 🛠️ Development & Engineering
These skills cover the full lifecycle of coding, testing, debugging, and code review.
- **`@[composition-patterns]`**: React composition patterns for building scalable, flexible component libraries.
- **`@[react-best-practices]`**: Vercel's official React and Next.js performance optimization guidelines.
- **`@[react-native-skills]`**: React Native and Expo best practices for performant mobile apps.
- **`@[supabase-postgres-best-practices]`**: Postgres performance optimization and best practices from Supabase.
- **`@[test-driven-development]`**: Test-Driven Development (TDD) - write tests before implementation code.
- **`@[systematic-debugging]`**: Systematic debugging for resolving bugs, test failures, or abnormal behaviors.
- **`@[webapp-testing]`**: Use Playwright for interactive testing and verification of local web applications.
- **`@[receiving-code-review]`**: Handle code review feedback using technical verification rather than blind modification.
- **`@[requesting-code-review]`**: Proactively initiate code reviews to verify code quality before merging or completion.
- **`@[finishing-a-development-branch]`**: Guide the finalization of a development branch (merges, PRs, cleanups, etc.).
- **`@[subagent-driven-development]`**: Coordinate multiple sub-agents to perform independent development tasks in parallel.

### 📄 Documentation & Office
These skills are used for handling professional documents and office needs in various formats.
- **`@[doc-coauthoring]`**: Guide users through collaborative writing of structured documents (proposals, tech specs, etc.).
- **`@[obsidian-markdown]`**: Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, and properties.
- **`@[obsidian-bases]`**: Create and edit Obsidian Bases (`.base`) files with views, filters, formulas, and summaries.
- **`@[docx]`**: Create, edit, and analyze Word documents.
- **`@[xlsx]`**: Create, edit, and analyze Excel spreadsheets (supporting formulas and charts).
- **`@[pptx]`**: Create and modify PowerPoint presentations.
- **`@[pdf]`**: Process PDF documents, including extracting text/tables, merging/splitting, and filling forms.
- **`@[internal-comms]`**: Draft various corporate internal communication documents (weekly reports, announcements, FAQs, etc.).
- **`@[notebooklm]`**: Query Google NotebookLM notebooks for definitive, document-grounded answers.

### 📅 Planning & Workflow
These skills help optimize workflows, task planning, and execution efficiency.
- **`@[brainstorming]`**: Brainstorm before starting any work to clarify requirements and design.
- **`@[writing-plans]`**: Write detailed execution plans (Specs) for complex multi-step tasks.
- **`@[planning-with-files]`**: A file-based planning system (Manus-style) suitable for complex tasks.
- **`@[executing-plans]`**: Execute existing implementation plans with checkpoints and review mechanisms.
- **`@[using-git-worktrees]`**: Create isolated Git worktrees for parallel development or task switching.
- **`@[verification-before-completion]`**: Run verification commands to ensure concrete evidence before declaring task completion.
- **`@[using-superpowers]`**: Guide users to discover and use these advanced skills.

### 🧠 Core Cognition & Architecture
These skills build the agent's mental models, memory systems, and context management capabilities.
- **`@[bdi-mental-states]`**: Simulate Agent's Belief-Desire-Intention (BDI) models.
- **`@[memory-systems]`**: Build long-term memory and entity tracking systems based on knowledge graphs or vectors.
- **`@[context-fundamentals]`**: Understand and debug fundamental issues like context windows and attention mechanisms.
- **`@[context-optimization]`**: Optimize context efficiency to reduce Token costs via KV-cache or partitioning.
- **`@[context-compression]`**: Implement context compression and summarization to handle long window limits.
- **`@[context-degradation]`**: Diagnose and fix context degradation issues like "lost in the middle".
- **`@[filesystem-context]`**: Utilize the filesystem for dynamic context offloading and management.

### 📐 System Design & Evaluation
These skills focus on architectural design, tool building, and quality assessment of AI systems.
- **`@[project-development]`**: Full lifecycle design of LLM projects, including task-model matching and pipeline architecture.
- **`@[tool-design]`**: Design efficient and clear agent tool interfaces and MCP protocols.
- **`@[evaluation]`**: Establish multi-dimensional agent performance evaluation systems and quality gates.
- **`@[advanced-evaluation]`**: Implement advanced evaluation methods like LLM-as-a-Judge and pairwise comparison.

### 🧩 System Extension
These skills allow me to extend my own capability boundaries.
- **`@[mcp-builder]`**: Build MCP (Model Context Protocol) servers to connect external tools and data.
- **`@[skill-creator]`**: Create new skills or update existing ones to expand my knowledge base and workflows.
- **`@[writing-skills]`**: A subset of tools to assist in writing, editing, and verifying skill files.
- **`@[dispatching-parallel-agents]`**: Dispatch parallel tasks to multiple agents for processing.
- **`@[multi-agent-patterns]`**: Design advanced multi-agent collaboration patterns like Supervisor or Swarm.
- **`@[hosted-agents]`**: Build and deploy sandboxed, persistently running background agents.

## 🌟 Credits & Sources

This project integrates core ideas or skill implementations from the following excellent open-source projects. Respect to the original authors:

- **[Anthropic Skills](https://github.com/anthropics/skills)**: Official API usage paradigms and skill definition references provided by Anthropic.
- **[UI/UX Pro Max Skills](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**: Top-tier UI/UX design intelligence, providing full design schemes for colors, layouts, etc.
- **[Superpowers](https://github.com/obra/superpowers)**: A toolkit and workflow inspiration aimed at giving LLMs "superpowers."
- **[Planning with Files](https://github.com/OthmanAdi/planning-with-files)**: Implements a Manus-style file-based task planning system to enhance persistent memory for complex tasks.
- **[NotebookLM](https://github.com/PleasePrompto/notebooklm-skill)**: Knowledge retrieval and Q&A skill implementation based on Google NotebookLM.
- **[Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)**: In-depth Context Engineering skills covering compression, optimization, and degradation handling.
- **[Obsidian Skills](https://github.com/kepano/obsidian-skills)**: Professional Obsidian integration skills, including JSON Canvas and enhanced Markdown support.
- **[Remotion Skills](https://github.com/remotion-dev/skills)**: Official Remotion skills for AI agents to create videos programmatically.
- **[Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)**: Official Vercel skills for React best practices, composition patterns, and web design guidelines.
- **[Supabase Agent Skills](https://github.com/supabase/agent-skills)**: Official Supabase skills for Postgres performance optimization and best practices.

## 🛡️ Security Policy

We take security seriously. Please refer to our [Security Policy](SECURITY.md) for information on supported versions and how to report vulnerabilities safely.

## 🤝 How to Contribute

We welcome contributions! Please refer to our **[CONTRIBUTING.md](CONTRIBUTING.md)** for detailed guidelines on how to add new skills, improve documentation, and report issues.

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).
