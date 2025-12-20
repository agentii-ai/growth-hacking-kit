# Changelog

All notable changes to Growth Hacking Kit are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-12-20

### Added

#### Core Features
- ✅ `growthkit init` - Initialize new projects with AI agent templates
- ✅ `growthkit check` - Verify dependencies and installed tools
- ✅ `growthkit specify` - Create campaign specifications from natural language
- ✅ `growthkit plan` - Generate implementation plans from specifications
- ✅ `growthkit tasks` - Break down plans into actionable tasks
- ✅ `growthkit implement` - Execute campaigns with checkpoint validations
- ✅ `growthkit version` - Show version information

#### Architecture
- Multi-kit coexistence strategy (`.growthkit/` namespace)
- Agent-first design with slash command interfaces
- Spec-driven architecture with Jinja2 templating
- Constitution Check validation system (10 gates)
- Phase-based execution model (Setup → Pilot → Scale → Measure)

#### CLI Framework
- Typer-based command line interface
- Rich console output with colors and tables
- Git integration for campaign branch management
- Debug mode (--debug flag) for all commands
- Force mode (--force flag) for non-interactive operation

#### Constitution Check
- 7 Mandatory Gates for specification validation
  - spec_exists
  - growth_type_identified (Vibe/Trust/Agentic)
  - target_audience_specific
  - viral_loop_defined (Remix/Integration/Watermark)
  - k_factor_target (>1.1)
  - metrics_defined
  - pilot_scoped

- 3 Advisory Gates for plan validation
  - content_optimized
  - platform_strategy
  - community_amplification

#### Template System
- Specification template with Jinja2 rendering
- Implementation plan template with platform tactics
- Task breakdown template with phase organization
- Campaign execution template with retrospective
- Agent command templates for integration

#### Platform Support
- X/Twitter (16:9 landscape optimization)
- TikTok (9:16 portrait optimization)
- LinkedIn (professional networking)
- GitHub (developer community)
- Product Hunt (product launches)

#### AI Agent Support
- Claude Code (`.claude/commands/`)
- Cursor Agent (`.cursor/commands/`)
- Windsurf (`.windsurf/commands/`)
- GitHub Copilot (`.copilot/commands/`)

#### Utilities
- Campaign numbering and naming
- Git repository operations
- Template rendering and validation
- Bash script execution
- Agent detection and installation checking

#### Testing
- Comprehensive test suite with pytest
- Unit tests for all commands
- Integration tests for workflows
- Test fixtures for campaign setup
- Pytest configuration with markers

#### CI/CD
- GitHub Actions workflow for testing
- Linting with ruff
- Code formatting with black
- Type checking with mypy
- Coverage reporting with codecov
- Release workflow for PyPI publishing

#### Documentation
- Comprehensive README.md
- API reference (docs/API.md)
- Troubleshooting guide (docs/TROUBLESHOOTING.md)
- Contributing guidelines (CONTRIBUTING.md)
- Implementation status tracking

#### Configuration
- 45+ configuration constants in config.py
- Support for environment variables
- Agent directory mapping
- Template directory configuration
- Branch naming patterns

### File Structure
```
growth-hacking-kit/
├── src/growthkit/
│   ├── cli/
│   │   ├── main.py (6 commands)
│   │   ├── specify.py
│   │   ├── plan.py
│   │   ├── tasks.py
│   │   ├── implement.py
│   │   ├── config.py
│   │   └── utils.py
│   └── constitution/
│       ├── gates.py
│       └── validator.py
├── .growthkit/
│   ├── memory/constitution.md
│   ├── scripts/bash/
│   └── templates/commands/
├── specs/001-growth-hacking-kit/
│   ├── spec.md (42 requirements)
│   ├── plan.md (technical design)
│   ├── tasks.md (45 tasks, 4 phases)
│   └── checklists/
├── tests/
│   ├── conftest.py
│   ├── test_init.py
│   ├── test_specify.py
│   ├── test_plan.py
│   ├── test_tasks.py
│   ├── test_implement.py
│   ├── test_validator.py
│   └── test_integration.py
├── docs/
│   ├── API.md
│   └── TROUBLESHOOTING.md
├── .github/workflows/
│   ├── tests.yml
│   └── release.yml
├── pyproject.toml
├── README.md
├── CONTRIBUTING.md
└── IMPLEMENTATION_STATUS.md
```

### Technical Details

#### Specification Generation
- Natural language campaign description parsing
- Growth type identification (Vibe/Trust/Agentic)
- Viral loop extraction (Remix/Integration/Watermark)
- Metric identification (k-factor, time-to-wow, NRR)
- Quality checklist generation

#### Planning Process
- Platform-specific tactic generation
- GEO optimization research documents
- Data model documentation
- Quickstart guide creation
- Constitution Check validation

#### Task Organization
- Phase-based structure (Setup, Pilot, Scale, Measure)
- Task ID generation (T001, T002, etc.)
- Parallel opportunity marking ([P])
- Checkpoint validation ([CP])
- Deliverable specification

#### Execution Engine
- Phase-by-phase execution tracking
- Checkpoint validation gates
- Go/no-go decision prompting
- Execution logging with timestamps
- Retrospective report generation

### Dependencies
- typer >=0.9.0
- jinja2 >=3.1.0
- pyyaml >=6.0
- gitpython >=3.1.0
- httpx >=0.25.0
- python-json-logger >=2.0.0

### Performance Targets
- CLI initialization: <2 seconds
- Specification generation: <5 seconds
- Constitution Check validation: <1 second
- Plan generation: <5 seconds
- Task generation: <5 seconds

### Known Limitations
1. No database - file-based specifications in markdown
2. No network by default - templates work offline
3. Single git repo - one .git per project
4. Manual content approval - AI generates, user reviews
5. No auto-posting - platform posting requires authorization

### For Future Versions
- PowerShell script support for Windows
- Additional AI agent integrations (Gemini, Qwen, etc.)
- Database backend option for larger teams
- Automated content posting integration
- Mobile app for campaign management
- Real-time collaboration features
- Advanced analytics dashboard
- Community template library

---

**Release Date**: 2025-12-20
**Status**: Alpha Release
**Ready for**: Community feedback and testing
