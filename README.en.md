# Antigravity Skills

[Chinese](README.md)\|[English](README.en.md)

through modular**Skills**Definition, giving Agents professional capabilities in specific fields (such as full-stack development, complex logic planning, multimedia processing, etc.), allowing Agents to systematically solve complex problems like human experts.

## 📂 Directory Structure

    .
    ├── .claude-plugin/    # Claude 插件配置文件 (plugin.json, marketplace.json)
    ├── skills/             # Antigravity Skills 技能库
    │   ├── skill-name/     # 独立技能目录
    │   │   ├── SKILL.md    # 技能核心定义与Prompt（必须）
    │   │   ├── scripts/    # 技能依赖的脚本（可选）
    │   │   ├── examples/   # 技能使用示例（可选）
    │   │   └── resources/  # 技能依赖的模板与资源（可选）
    ├── docs/               # 用户手册与文档指南
    │   └── Antigravity_Skills_Manual_CN.md  # 中文使用手册
    ├── spec/               # 规范文档
    ├── template/           # 新技能模板
    └── README.md

## 🔌Compatibility

Antigravity Skills follow the common**SKILL.md**format that works with any AI coding assistant that supports Agentic Skills:

| Tool name (Agent)  | type      | compatibility | Project Path        | Global Path                     |
| :----------------- | :-------- | :------------ | :------------------ | :------------------------------ |
| **Antigravity**    | IDE       | ✅ Full        | `.agent/skills/`    | `~/.gemini/antigravity/skills/` |
| **Claude Code**    | CLI       | ✅ Full        | `.claude/skills/`   | `~/.claude/skills/`             |
| **Gemini CLI**     | CLI       | ✅ Full        | `.gemini/skills/`   | `~/.gemini/skills/`             |
| **Codex**          | CLI       | ✅ Full        | `.codex/skills/`    | `~/.codex/skills/`              |
| **Cursor**         | IDE       | ✅ Full        | `.cursor/skills/`   | `~/.cursor/skills/`             |
| **GitHub Copilot** | Extension | ⚠️ Partial    | `.github/skills/`   | `~/.copilot/skills/`            |
| **OpenCode**       | CLI       | ✅ Full        | `.opencode/skills/` | `~/.config/opencode/skills/`    |
| **Windsurfing**    | IDE       | ✅ Full        | `.windsurf/skills/` | `~/.codeium/windsurf/skills/`   |
| **Trae**           | IDE       | ✅ Full        | `.trae/skills/`     | `~/.trae/skills/`               |

> [!TIP]Most tools will automatically discover`.agent/skills/`skills in. For maximum compatibility, clone/copy to this directory.

## 📖Quick Start

### 1. Prepare skill library

First clone this repository locally (it is recommended to put it in a fixed location for global reference):

```bash
git clone https://github.com/guanyang/antigravity-skills.git ~/antigravity-skills
```

### 2. Install skills (Symlink method)

We strongly recommend using**Symlink**Install it so that when you pass`git pull`When this repository is updated, all tools will automatically synchronize with the latest features.

#### 🔹 Option A: Project Level Installation

Enables the skill for the current project only. In your project root directory run:

```bash
mkdir -p .agent/skills
ln -s ~/antigravity-skills/skills/* .agent/skills/
```

#### 🔹 Option B: Global Installation (Global Level)

Skills are enabled by default in all projects. Run the corresponding commands according to different tools and give some examples:

| Tool name       | Global installation commands (macOS/Linux)                                                                   |
| :-------------- | :----------------------------------------------------------------------------------------------------------- |
| **Universal**   | `mkdir -p ~/.agent/skills && ln -s ~/antigravity-skills/skills/* ~/.agent/skills/`                           |
| **Claude Code** | `mkdir -p ~/.claude/skills && ln -s ~/antigravity-skills/skills/* ~/.claude/skills/`                         |
| **Antigravity** | `mkdir -p ~/.gemini/antigravity/skills && ln -s ~/antigravity-skills/skills/* ~/.gemini/antigravity/skills/` |
| **Gemini**      | `mkdir -p ~/.gemini/skills && ln -s ~/antigravity-skills/skills/* ~/.gemini/skills/`                         |
| **Codex**       | `mkdir -p ~/.codex/skills && ln -s ~/antigravity-skills/skills/* ~/.codex/skills/`                           |

#### 🔹 Solution C: Claude Plugin installation (Claude Code only)

If you mainly use**Claude Code**, which can be installed with one click through the plug-in market (this method will automatically handle skill loading):

```bash
# 1. 启动 Claude Code
# 2. 添加插件市场
/plugin marketplace add guanyang/antigravity-skills

# 3. 从市场安装插件
/plugin install antigravity-skills@antigravity-skills
```

### 3. Use skills

Enter in the dialog box`@[skill-name]`or`/skill-name`can be called, for example:

```text
/canvas-design 帮我设计一张关于“Deep Learning”的博客封面，尺寸 16:9
```

### 4. More information

-   **View manual**: Please refer to the detailed usage[docs/Antigravity_Skills_Manual.md](docs/Antigravity_Skills_Manual.md)。
-   **environment dependence**: Some skills depend on the Python environment, please ensure that the system has installed the necessary libraries (such as`pdf2docx`,`pandas`wait).

## 🚀 Integrated Skills

### 🎨Creative & Design

These skills focus on visual presentation, UI/UX design, and artistic creation.

-   **`@[algorithmic-art]`**: Use p5.js code to create algorithmic art and generative art
-   **`@[canvas-design]`**: Create posters and artwork based on design philosophy (output PNG/PDF)
-   **`@[frontend-design]`**: Create high-quality, production-grade front-end interfaces and web components of various kinds
-   **`@[ui-ux-pro-max]`**: Professional UI/UX design intelligence, providing a complete set of design solutions such as color matching, fonts, layout, etc.
-   **`@[web-artifacts-builder]`**: Build complex, modern web applications (based on React, Tailwind, Shadcn/ui)
-   **`@[theme-factory]`**: Generate matching theme styles for documents, slides, HTML, etc.
-   **`@[brand-guidelines]`**: Apply Anthropic official brand design specifications (color, typography, etc.)
-   **`@[slack-gif-creator]`**: Create high-quality GIF animations specifically for Slack

### 🛠️ Development & Engineering

These skills cover the full life cycle of coding, testing, debugging and code review.

-   **`@[test-driven-development]`**: Test-driven development (TDD), writing tests before writing implementation code
-   **`@[systematic-debugging]`**: Systematic debugging to solve bugs, test failures or abnormal behaviors
-   **`@[webapp-testing]`**: Interactive testing and validation of local web applications using Playwright
-   **`@[receiving-code-review]`**: Handle code review feedback and perform technical verification rather than blind modifications
-   **`@[requesting-code-review]`**: Proactively initiate code reviews to verify code quality before merging or completing tasks
-   **`@[finishing-a-development-branch]`**: Guide the finishing work of the development branch (merge, PR, cleanup, etc.)
-   **`@[subagent-driven-development]`**: Coordinate multiple sub-agents to execute independent development tasks in parallel

### 📄 Documentation & Office

These skills are used to handle professional documents in a variety of formats and office needs.

-   **`@[doc-coauthoring]`**: Guide users to collaboratively write structured documents (proposals, technical specifications, etc.)
-   **`@[docx]`**: Create, edit and analyze Word documents
-   **`@[xlsx]`**: Create, edit and analyze Excel spreadsheets (supports formulas, charts)
-   **`@[pptx]`**: Create and modify PowerPoint presentations
-   **`@[pdf]`**: Process PDF documents, including extracting text, tables, merging/splitting and filling out forms
-   **`@[internal-comms]`**: Drafting various corporate internal communication documents (weekly reports, announcements, FAQs, etc.)
-   **`@[notebooklm]`**: Query Google NotebookLM notebooks for exact document-based answers

### 📅Planning & Workflow

These skills help optimize workflow, task planning, and execution efficiency.

-   **`@[brainstorming]`**: Brainstorm, clarify requirements and design before starting any work
-   **`@[writing-plans]`**: Write detailed execution plans (Spec) for complex multi-step tasks
-   **`@[planning-with-files]`**: Document-based planning system (Manus-style) suitable for complex tasks
-   **`@[executing-plans]`**: Execute the existing implementation plan, including checkpoints and review mechanisms
-   **`@[using-git-worktrees]`**: Create an isolated Git work tree for parallel development or task switching
-   **`@[verification-before-completion]`**: Run the verification command before declaring that the task is completed to ensure that the evidence is conclusive
-   **`@[using-superpowers]`**: Guide users to discover and use these advanced skills

### 🧠 Core Cognition & Architecture

These skills build the Agent’s mental model, memory system, and context management capabilities.

-   **`@[bdi-mental-states]`**: Simulate the Agent’s belief (Belief), desire (Desire) and intention (Intention) models
-   **`@[memory-systems]`**: Build a long-term memory and entity tracking system based on knowledge graphs or vectors
-   **`@[context-fundamentals]`**: Understand and debug basic issues such as context windows and attention mechanisms.
-   **`@[context-optimization]`**: Optimize context efficiency and reduce Token costs through KV-cache or partitioning
-   **`@[context-compression]`**: Implement contextual compression and summarization to cope with long window restrictions
-   **`@[context-degradation]`**: Diagnose and fix context degradation issues such as "lost in the middle"
-   **`@[filesystem-context]`**: Use the file system for dynamic context offloading and management

### 📐 System Design & Evaluation

These skills focus on architectural design, tool building, and quality assessment of AI systems.

-   **`@[project-development]`**: LLM project full life cycle design, including task-model matching and pipeline architecture
-   **`@[tool-design]`**: Design efficient and clear Agent tool interface and MCP protocol
-   **`@[evaluation]`**: Establish a multi-dimensional Agent performance evaluation system and quality access control
-   **`@[advanced-evaluation]`**: Implement advanced evaluation methods such as LLM-as-a-Judge and pairwise comparisons

### 🧩 System Extension

These skills allow me to expand the boundaries of my abilities.

-   **`@[mcp-builder]`**: Build MCP (Model Context Protocol) server to connect external tools and data
-   **`@[skill-creator]`**: Create new skills or update existing ones to expand my knowledge base and workflow
-   **`@[writing-skills]`**: Toolset to assist in writing, editing, and validating skills files
-   **`@[dispatching-parallel-agents]`**: Distribute parallel tasks to multiple Agents for processing
-   **`@[multi-agent-patterns]`**: Design advanced multi-agent collaboration models such as Supervisor and Swarm
-   **`@[hosted-agents]`**: Build and deploy sandboxed, persistently running background agents

## 🌟 Credits & Sources

This project integrates the core ideas or Skill implementations of the following outstanding open source projects, and pays tribute to the original author:

-   **[Anthropic Skills](https://github.com/anthropic/skills)**: API usage paradigm and skill definition reference officially provided by Anthropic.
-   **[UI/UX Pro Max Skills](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**: Top-notch UI/UX design intelligence, providing a full set of design solutions such as color matching and layout.
-   **[Superpowers](https://github.com/obra/superpowers)**: Toolset and workflow inspiration designed to give LLM "superpowers".
-   **[Planning with Files](https://github.com/OthmanAdi/planning-with-files)**: Implement a file-based task planning system similar to Manus to improve the persistent memory of complex tasks.
-   **[NotebookLM](https://github.com/PleasePrompto/notebooklm-skill)**: Implementation of knowledge retrieval and question and answer skills based on Google NotebookLM.
-   **[Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)**: In-depth context engineering skills, covering compression, optimization and degradation processing.

## 📄 Open Source Agreement (License)

This project uses[MY License](LICENSE)The protocol is open source.
