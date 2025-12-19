# Implementation Plan: Growth Hacking Kit

**Branch**: `001-growth-hacking-kit` | **Date**: 2025-12-19 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-growth-hacking-kit/spec.md`

**Note**: This plan transforms spec-kit into growth-hacking-kit while maintaining multi-kit coexistence. The core infrastructure (Python CLI, agent integration, template system) is reused; only package names, directories, and slash commands are kit-specific.

## Summary

Growth Hacking Kit is a featured variant of spec-kit that applies spec-driven methodology to growth campaign management for AI SaaS products. It inherits spec-kit's CLI model (`uv tool install`), agent integration (.claude/, .cursor/, .windsurf/), and workflow structure (specify → plan → tasks → implement) but operates in an isolated namespace to enable multi-kit coexistence.

**Key Technical Decisions**:
1. **Package Isolation**: `growthkit-cli` PyPI package, `.growthkit/` directory, `/growthkit.*` slash commands
2. **Shared Infrastructure**: Reuse spec-kit's Python codebase with parameterized kit name (`KIT_NAME = "growthkit"`)
3. **Constitution-Driven**: Enforce Seven Core Principles via Constitution Check gates during planning
4. **Platform-Specific**: Generate content in native formats (X/Twitter 16:9, TikTok 9:16, LinkedIn case studies)

## Technical Context

**Language/Version**: Python 3.11+ (matching spec-kit for consistency and modern type hints)

**Primary Dependencies**:
- **CLI Framework**: `typer` (same as spec-kit) for command-line interface with rich help
- **Templating**: `jinja2` for rendering spec/plan/tasks templates with kit-specific variables
- **YAML/JSON Parsing**: `pyyaml`, `python-json-logger` for parsing agent command files and slash command metadata
- **Git Operations**: `gitpython` for branch creation, status checks (inherited from spec-kit)
- **HTTP/Research**: `httpx` for web research during Phase 0 (GEO optimization, platform specs)
- **Packaging**: `uv` for modern Python packaging and tool installation

**Storage**: File-based (markdown files in `specs/###-campaign-name/`, no database required)

**Testing**: `pytest` with fixtures for CLI testing, template rendering validation, Constitution Check gate logic

**Target Platform**: Cross-platform CLI (Linux, macOS, Windows) installed via `uv tool install growthkit-cli`

**Project Type**: Single Python CLI project with template assets

**Performance Goals**:
- CLI command execution <2 seconds for `growthkit init`
- Spec generation <5 seconds for `/growthkit.specify` (per SC-017)
- Constitution Check validation <1 second (regex parsing of spec.md)

**Constraints**:
- **Multi-kit coexistence**: MUST NOT overwrite `.specify/` directory or `/speckit.*` commands
- **Agent compatibility**: MUST work with Claude Code, Cursor, Windsurf, Copilot (same agents as spec-kit)
- **Offline-first**: Templates and constitution must work without network (research phase may require network)
- **Kit-agnostic templates**: Templates must use `{{KIT_NAME}}` variable, not hardcoded "growthkit"

**Scale/Scope**:
- Target: Growth marketers/founders managing 5-20 concurrent campaigns per project
- Template library: ~10 core templates (spec, plan, tasks, constitution, research, data-model, contracts, quickstart, retrospective, checklist)
- Constitution: 7 core principles with ~15 Constitution Check gates
- Refs library: 7 reference documents (0_overview.md through 7_optimization.md)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**This feature implements the Growth Hacking Kit itself, so Constitution Check validates the implementation aligns with the constitution it will enforce.**

### Mandatory Gates (MUST pass before Phase 0 research)

1. **Spec-Driven Growth (Principle I)**:
   - ✅ Feature specification exists: [spec.md](./spec.md)
   - ✅ Growth type identified: Agentic Growth (developer tools for growth marketers)
   - ✅ Target audience specific: "Growth marketers, founders, or product managers working on AI/LLM SaaS products" (per spec Assumption #1)

2. **Viral Loop Engineering (Principle II)**:
   - ✅ Viral loop mechanism: **Integration Loop** - growthkit inhabits user workflows (terminal, campaign specs, retrospectives), grows through systematic campaign success
   - ✅ K-factor target: Not applicable (growthkit is a tool, not a campaign; success measured by user adoption via campaign outcomes)
   - ✅ Platform-specific viral mechanisms: Documentation, GitHub integration, campaign retrospective sharing

3. **Measurement-First Development (Principle IV)**:
   - ✅ Primary metric: "Users can initialize project and see slash commands in under 2 minutes" (SC-016)
   - ✅ Activation metric: "Users generate campaign spec from natural language in under 5 minutes" (SC-017)
   - ✅ Engagement metric: "80% of users execute pilot campaign within 7 days" (SC-018)

4. **Test-Before-Scale (Principle VI)**:
   - ✅ Pilot phase scope: MVP includes `growthkit init` + `/growthkit.specify` only; full workflow (`/growthkit.plan`, `/growthkit.tasks`, `/growthkit.implement`) added after pilot validation
   - ✅ Pilot success criteria: 5 beta users successfully initialize project and generate 1 campaign spec each

### Advisory Gates (re-check after Phase 1 design)

1. **Agent-First Architecture (Principle III)**:
   - ⚠ Content optimized for "Answer Density": README.md must include structured tables, benchmarks, concrete examples (to be validated in Phase 1)
   - ⚠ LLM citation validation plan: To be added in Phase 1 (document how to optimize docs for Perplexity/ChatGPT citation)

2. **Multi-Platform Distribution (Principle V)**:
   - ⚠ Platform-specific content strategy: GitHub (README, examples, templates), documentation site (quickstart, tutorials)
   - ⚠ Platform-specific formats: Markdown for GitHub, static site generation for docs (to be detailed in Phase 1)

3. **Community-Led Amplification (Principle VII)**:
   - ⚠ Organic reach prioritized: Growth via GitHub stars, word-of-mouth, campaign retrospective sharing (no paid ads for toolkit itself)
   - ⚠ User showcase program: To be defined in Phase 1 (feature successful campaign retrospectives in docs)

### Gate Evaluation: ✅ PASSED

All mandatory gates passed. Advisory gates require Phase 1 design (research.md for GEO optimization, quickstart.md for documentation strategy). No complexity violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/001-growth-hacking-kit/
├── plan.md              # This file (/growthkit.plan command output)
├── research.md          # Phase 0 output (technology choices, platform research, GEO strategy)
├── data-model.md        # Phase 1 output (Campaign, Constitution, Platform Tactic entities)
├── quickstart.md        # Phase 1 output (installation guide, first campaign walkthrough)
├── contracts/           # Phase 1 output (CLI command schemas, template variable schemas)
│   ├── cli-commands.yaml            # growthkit init/check command specifications
│   ├── slash-commands.yaml          # /growthkit.* command specifications
│   └── template-variables.json      # {{KIT_NAME}}, {{CAMPAIGN_NAME}}, etc.
├── checklists/
│   └── requirements.md  # Spec quality validation (already completed ✅)
└── tasks.md             # Phase 2 output (/growthkit.tasks command - NOT created by /growthkit.plan)
```

### Source Code (repository root)

```text
# Python CLI package (inherits spec-kit structure)
src/growthkit/
├── __init__.py
├── __main__.py          # Entry point for `python -m growthkit`
├── cli/
│   ├── __init__.py
│   ├── main.py          # Typer app with `init`, `check` commands
│   ├── config.py        # KIT_NAME="growthkit", PACKAGE_DIR=".growthkit/"
│   └── utils.py         # Git operations, agent detection, template rendering
├── templates/
│   ├── spec-template.md
│   ├── plan-template.md
│   ├── tasks-template.md
│   ├── constitution-template.md  # Growth Hacking Kit Constitution
│   └── commands/        # Slash command templates for each agent
│       ├── specify.md
│       ├── plan.md
│       ├── tasks.md
│       ├── implement.md
│       └── constitution.md
├── constitution/
│   ├── __init__.py
│   ├── validator.py     # Constitution Check gate validation logic
│   └── gates.py         # Mandatory/advisory gate definitions
└── research/
    ├── __init__.py
    └── platforms.py     # Platform API specs (X/Twitter, TikTok, LinkedIn, Product Hunt)

# Kit-specific project files (created by `growthkit init`)
.growthkit/
├── memory/
│   └── constitution.md  # Copied from templates/constitution-template.md
├── scripts/
│   ├── bash/
│   │   ├── common.sh
│   │   ├── check-prerequisites.sh
│   │   ├── create-new-feature.sh  # Creates ###-campaign-name branches
│   │   ├── setup-plan.sh
│   │   └── update-agent-context.sh
│   └── powershell/      # Windows equivalents
│       └── [mirror of bash/]
└── templates/
    ├── spec-template.md
    ├── plan-template.md
    ├── tasks-template.md
    └── commands/        # Kit-specific slash commands
        ├── growthkit-specify.md     # -> /growthkit.specify
        ├── growthkit-plan.md        # -> /growthkit.plan
        ├── growthkit-tasks.md       # -> /growthkit.tasks
        ├── growthkit-implement.md   # -> /growthkit.implement
        └── growthkit-constitution.md # -> /growthkit.constitution

# Agent integration (kit-agnostic, supports multi-kit coexistence)
.claude/commands/
├── growthkit-specify.md     # Symlink or copy from .growthkit/templates/commands/
├── growthkit-plan.md
├── growthkit-tasks.md
├── growthkit-implement.md
└── growthkit-constitution.md

.cursor/commands/
└── [same structure as .claude/]

.windsurf/commands/
└── [same structure as .claude/]

# Packaging and configuration
pyproject.toml           # Package name: growthkit-cli, entry point: growthkit
LICENSE                  # MIT (inherited from spec-kit)
README.md                # Growth Hacking Kit README (distinct from spec-kit)

# Testing
tests/
├── cli/
│   ├── test_init.py     # Test `growthkit init` creates .growthkit/ directory
│   └── test_check.py    # Test `growthkit check` detects agents
├── constitution/
│   ├── test_validator.py  # Test Constitution Check gate validation
│   └── test_gates.py      # Test mandatory/advisory gate logic
├── templates/
│   └── test_rendering.py  # Test Jinja2 rendering with KIT_NAME variable
└── integration/
    └── test_workflow.py   # Test full workflow: init → specify → plan

# References (growth hacking research)
refs/
├── 0_overview.md        # 2024-2025 growth landscape (already exists ✅)
├── 1_principles_for_constitution.md  # Principle derivations (already exists ✅)
├── 2_define_for_specify.md  # Campaign specification guidance (already exists ✅)
├── 3_project_mangement_for_plan.md  # Planning guidance (already exists ✅)
├── 4_pm_tasking_for_tasks.md        # Task breakdown guidance
├── 5_writing_for_optimize.md        # Content optimization guidance
├── 6_claude_code.md                 # Agent-specific workflows
└── 7_optimization.md                # Performance patterns
```

**Structure Decision**: Single Python CLI project with embedded templates. This matches spec-kit's architecture for consistency and allows code reuse. The critical difference is **package namespace isolation**: `growthkit-cli` package installs as `growthkit` command (not `specify`), and all project files live in `.growthkit/` directory (not `.specify/`). Slash commands use `/growthkit.*` prefix, ensuring no collision with `/speckit.*` commands when both kits are installed.

**Multi-Kit Coexistence Strategy**:
1. **Package-level isolation**: PyPI package `growthkit-cli` distinct from `specify-cli`
2. **Directory-level isolation**: `.growthkit/` directory distinct from `.specify/`
3. **Command-level isolation**: `/growthkit.*` commands distinct from `/speckit.*`
4. **Environment variable isolation**: `GROWTHKIT_CAMPAIGN` distinct from `SPECIFY_FEATURE`
5. **Agent command file naming**: `growthkit-specify.md` (not `specify.md`) in `.claude/commands/`

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

**No violations**. The implementation follows all Seven Core Principles from the constitution and passes all mandatory Constitution Check gates.
