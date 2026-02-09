# Changelog

All notable changes to this project will be documented in this file.

## [v2.3.0] - 2026-02-09
### Added
- **5 New Development Skills**:
  - `composition-patterns`: Advanced React composition patterns for scalable component libraries.
  - `react-best-practices`: Official Vercel guidelines for React and Next.js performance optimization.
  - `react-native-skills`: Best practices for building performant React Native and Expo applications.
  - `supabase-postgres-best-practices`: Comprehensive Postgres performance optimization guide from Supabase.
  - `web-design-guidelines`: Auditing rules for web interface design, accessibility, and UX compliance.
- **Script Enhancement**: Updated `scripts/sync_skills.sh` to support `include` directive in `skills_sources.json`, allowing precise file selection during synchronization.

### Changed
- **Skill Index**: Updated `skills_index.json` to include metadata for the 5 new skills and added missing entry for `remotion`.
- **Documentation**: Updated `README.md` and `README.zh-CN.md` to list new skills (Total: 55) and added Vercel/Supabase to Credits & Sources.

## [v2.2.0] - 2026-02-02
### Added
- **Sync Mechanism**: Introduced `skills_sources.json` configuration and `scripts/sync_skills.sh` script to keep skills synchronized with upstream open-source repositories.
- **Source Configuration**: Pre-configured sync sources for major skills including `anthropics-skills`, `notebooklm`, `superpowers`, etc.
- **CI Automation**: Added GitHub Action (`.github/workflows/sync-skills.yml`) to automatically sync skills daily and check for updates.

## [v2.1.0] - 2026-01-24
### Added
- **3 New Skills**:
  - `json-canvas`: Create and edit JSON Canvas files (compatible with Obsidian Canvas).
  - `obsidian-markdown`: Support for Obsidian-flavored Markdown (Wikilinks, Callouts, etc.).
  - `obsidian-bases`: Support for creating and editing Obsidian Bases database files.
- **Multilingual Support**: Introduced a bilingual README system (English/Chinese) and an English manual `docs/Antigravity_Skills_Manual.en.md`.

### Changed
- **Documentation Restructuring**: Optimized the structure of `README.md` (English) and `README.zh-CN.md` (Simplified Chinese).
- **Skill Index Update**: `skills_index.json` now aggregates metadata for all 49 skills.
- **Version Bump**: Updated plugin version to v2.1.0.

## [v2.0.2] - 2026-01-23
### Changed
- **Directory Structure Optimization**: Moved the skills library from `.agent/skills` to the root `skills/` directory and reorganized `docs/`, `spec/`, and `template/` directories.
- **Documentation Revamp**:
  - Updated `README.md` to match the new directory structure.
  - Introduced **Symlink (Symbolic Link)** installation method in "Quick Start", supporting both Project and Global levels.
  - Enhanced **Compatibility** module, supporting path specifications for multiple AI tools (Claude, Gemini, Cursor, Windsurf, Trae, etc.).
  - Updated Credits & Sources with detailed descriptions.

### Added
- **Skill Index File**: Automatically generate `skills_index.json` summarizing metadata (ID, path, name, description) for 46 skills.
- **Multi-tool Support**: Explicitly support skill loading paths for GitHub Copilot, Windsurf, Trae, and other IDEs.

### Fixed
- Updated `.gitignore` to prevent AI assistant runtime directories (e.g., `.agent`, `.claude`) from being committed.

## [v2.0.1] - 2026-01-15
### Added
- **13 Advanced Cognition & System Skills**:
  - **Core Cognition**: `bdi-mental-states` (BDI cognitive model), `memory-systems` (Memory systems), `filesystem-context` (Filesystem context).
  - **Context Engineering**: Fundamentals, Optimization, Compression, and Degradation handling.
  - **Advanced Agents**: `multi-agent-patterns` (Supervisor/Swarm), `hosted-agents`.
  - **System Design & Evaluation**: Tool design, Project development, Basic and Advanced evaluation.

## [v2.0.0] - 2026-01-14
### Released
- **Antigravity Native Skill Support**: Major release establishing the native Antigravity skill architecture.
- **Core Library**: Established 33 foundational skills covering Creative Design, Engineering, Documentation, and Planning.

## [v1.0.0] - 2026-01-14
### Released
- **Workflow Standard Support**: Initial skill support based on Antigravity workflow standards.
- **Core Library**: Established 33 foundational skills covering Creative Design, Engineering, Documentation, and Planning.