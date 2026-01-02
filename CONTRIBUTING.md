#!/usr/bin/env bash
# CONTRIBUTING.md - Contribution Guidelines for Growth Hacking Kit

## Overview

Growth Hacking Kit is a spec-driven growth campaign management tool for AI SaaS products. We welcome contributions!

## Development Setup

```bash
# Clone the repository
git clone https://github.com/agentii/growth-hacking-kit.git
cd growth-hacking-kit

# Install development dependencies
uv pip install -e ".[dev]"

# Run tests
pytest tests/

# Run linting
black src/
ruff check src/
```

## Project Structure

```
src/growthkit/
├── __init__.py              # Package initialization
├── __main__.py              # CLI entry point
├── cli/
│   ├── main.py              # Typer CLI application
│   ├── config.py            # Configuration constants
│   └── utils.py             # Utility functions (git, agents, templates)
├── constitution/
│   ├── validator.py         # Constitution Check validation logic
│   └── gates.py             # Mandatory/advisory gate definitions
├── research/
│   └── platforms.py         # Platform specifications and tactics
└── templates/
    ├── spec-template.md
    ├── plan-template.md
    ├── tasks-template.md
    ├── constitution.md
    └── commands/            # Slash command templates

.growthkit/
├── memory/
│   └── constitution.md      # Project governance (created by growthkit init)
├── scripts/
│   ├── bash/               # Bash utility scripts
│   └── powershell/         # PowerShell equivalents
└── templates/              # Project-specific templates (symlinked from src/)
```

## Architecture

### Core Concepts

1. **Kit Isolation**: Package name (`growthkit-cli`), directory (`.growthkit/`), and commands (`/growthkit.*`) are isolated from spec-kit and other *-kit variants
2. **Spec-Driven Workflow**: specify → plan → tasks → implement
3. **Constitution-Based Governance**: Seven Core Principles enforced via Constitution Check gates
4. **Multi-Platform Support**: Platform-specific content tactics (X/Twitter 16:9, TikTok 9:16, etc.)
5. **Agent-First Design**: Slash commands in Claude Code, Cursor, Windsurf, Copilot

### Key Files to Understand

- **config.py**: Kit-agnostic configuration (KIT_NAME, PACKAGE_DIR, PLATFORMS, METRICS)
- **utils.py**: Git operations, agent detection, template rendering
- **gates.py**: Constitution Check gate definitions (mandatory and advisory)
- **validator.py**: Regex-based spec/plan validation against gates
- **platforms.py**: Platform API specs, viral loops, GEO guidelines, metrics

## Implementation Guidelines

### Adding a New CLI Command

1. Add function to `src/growthkit/cli/main.py`
2. Use `@app.command()` decorator
3. Follow `growthkit init` pattern for argument handling
4. Use `rich.Console` for output formatting

Example:
```python
@app.command()
def my_command(arg: str = typer.Argument(...), option: Optional[str] = typer.Option(None)) -> None:
    """Command description."""
    console.print("[bold]Working...[/bold]")
    # Implementation
    console.print("[green]✓ Done[/green]")
```

### Adding Constitution Check Validation

1. Define gate in `src/growthkit/constitution/gates.py`
2. Implement validation logic in `src/growthkit/constitution/validator.py`
3. Use regex patterns for spec/plan content matching
4. Return status (PASS/FAIL) with clear messages

Example:
```python
# In gates.py
"viral_loop_defined": MandatoryGate(
    gate_id="MG-004",
    description="Viral loop mechanism specified",
    validation_criteria="Must include Remix/Integration/Watermark loop",
)

# In validator.py
def _validate_gate(self, gate_name, gate, content):
    pattern = r"(Remix Loop|Integration Loop|Watermark Loop)"
    passed = bool(re.search(pattern, content))
    return {"status": GateStatus.PASS.value if passed else GateStatus.FAIL.value, ...}
```

### Adding Platform Support

1. Add platform spec to `src/growthkit/research/platforms.py`
2. Define format (aspect ratio, duration, file type)
3. Define viral mechanism and example campaigns
4. Update platform-specific content generation in `/growthkit.implement`

Example:
```python
PLATFORMS["new_platform"] = {
    "name": "New Platform",
    "format": "30s video",
    "aspect_ratio": "16:9",
    "viral_mechanism": "Shares and comments",
    "example_campaign": "Your example here",
}
```

## Testing

### Test Structure

```
tests/
├── cli/
│   ├── test_init.py         # Test growthkit init command
│   └── test_check.py        # Test growthkit check command
├── constitution/
│   ├── test_validator.py    # Test Constitution Check validation
│   └── test_gates.py        # Test gate definitions
├── templates/
│   └── test_rendering.py    # Test Jinja2 rendering
└── integration/
    └── test_workflow.py     # Test full workflow
```

### Writing Tests

```python
import pytest
from growthkit.constitution.validator import ConstitutionValidator

def test_spec_validation():
    validator = ConstitutionValidator()
    result = validator.validate_spec("001-test-campaign")
    assert result["status"] == "PASS"
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/constitution/test_validator.py

# Run with coverage
pytest --cov=src/growthkit tests/
```

## Code Style

- **Python Version**: 3.11+
- **Formatter**: black (line length: 100)
- **Linter**: ruff
- **Type Hints**: Required for all functions

```bash
# Format code
black src/ tests/

# Run linter
ruff check src/ tests/

# Fix linter issues
ruff check --fix src/ tests/
```

## Commit Guidelines

- Use clear, descriptive commit messages
- Reference task IDs from tasks.md (e.g., "T023: Implement growthkit init command")
- One task per commit when possible

Example:
```
T023: Implement growthkit init command

- Create project directory structure
- Initialize git repository
- Copy constitution template
- Detect AI agents
- Display success message with next steps
```

## Multi-Kit Coexistence

When developing features, ensure:

1. **No namespace collision**: Use `/growthkit.*` not `/specify.*`
2. **Directory isolation**: `.growthkit/` not `.specify/`
3. **Package distinction**: `growthkit-cli` not `specify-cli`
4. **Environment variable**: `GROWTHKIT_CAMPAIGN` not `SPECIFY_FEATURE`

## Template Testing

### Local Template Development

Build and test templates locally before publishing:

```bash
# Build all 34 templates locally
./scripts/build-templates.sh v0.2.0

# Build specific agent
AGENTS=claude ./scripts/build-templates.sh v0.2.0

# Build specific script type
AGENTS=claude SCRIPTS=sh ./scripts/build-templates.sh v0.2.0

# Output goes to dist/templates/
ls dist/templates/growthkit-template-*.zip
```

### Template Validation

Validate template integrity:

```bash
# Test error detection with fixtures
./scripts/test-validation.sh

# Validate built templates
./scripts/validate-templates.sh dist/templates/

# Expected output: All 34 templates pass validation
```

### Manual Template Testing

Extract and test a template manually:

```bash
# Extract a template
unzip dist/templates/growthkit-template-claude-sh-v0.2.0.zip -d /tmp/test-template

# Verify structure
ls -R /tmp/test-template/.growthkit/
cat /tmp/test-template/.growthkit/memory/constitution.md

# Test in growthkit init
growthkit init my-test --ai claude
```

### CI/CD Template Testing

The CI workflow automatically:

1. **Builds** all 34 templates using `create-release-packages.sh`
2. **Validates** templates using `validate-templates.sh`
3. **Lints** bash scripts with shellcheck
4. **Lints** PowerShell scripts with PSScriptAnalyzer
5. **Extracts** sample templates and verifies structure
6. **Publishes** to GitHub Releases with SHA-256 checksums

Triggered on PRs affecting:
- `.growthkit/**`
- `scripts/**`
- `.github/workflows/scripts/**`

### Release Process for Templates

When releasing a new version:

```bash
# 1. Update version in src/growthkit/__init__.py
# Example: __version__ = "0.2.1"

# 2. Build templates with new version
./scripts/build-templates.sh v0.2.1

# 3. Validate all templates pass
./scripts/validate-templates.sh dist/templates/

# 4. Create git tag
git tag v0.2.1

# 5. Push tag (triggers GitHub Actions release workflow)
git push origin v0.2.1

# 6. GitHub Actions will:
#    - Build all 34 templates
#    - Validate them
#    - Create release with ZIP files
#    - Upload with SHA-256 checksums
```

### Adding New Agent Templates

When adding a new AI agent:

1. **Add to configuration** (`src/growthkit/cli/config.py`):
   ```python
   AGENT_DIRS = {
       "new-agent": ".newagent/claude",  # Path pattern
       # ... existing agents
   }
   ```

2. **Add to build script** (`.github/workflows/scripts/create-release-packages.sh`):
   ```bash
   AGENTS=(
       "claude" "cursor-agent" "windsurf" "gemini" "copilot"
       "qwen" "codex" "opencode" "qoder" "kilocode"
       "auggie" "roo" "codebuddy" "amp" "shai" "jules" "q"
       "new-agent"  # Add here
   )
   ```

3. **Generate templates**:
   ```bash
   ./scripts/build-templates.sh v0.2.1
   ```

4. **Validate**:
   ```bash
   ./scripts/validate-templates.sh dist/templates/
   ```

5. **Update documentation** (`docs/templates.md`):
   - Add agent to supported agents table
   - Add to agent grid in README.md

## Documentation

- Update README.md for user-facing changes
- Add docstrings to all functions
- Document new Constitution Check gates
- Update CONTRIBUTING.md for development changes
- Update docs/templates.md when adding agents or changing template structure
- Document local build process for developers
- Document release process for maintainers

## Release Process

1. Update version in `src/growthkit/__init__.py`
2. Update CHANGELOG.md
3. Create git tag
4. Build and publish to PyPI

## Support

- **Issues**: Use GitHub Issues for bugs and features
- **Discussions**: Use GitHub Discussions for questions
- **Security**: Email security@agentii.ai for security issues

## License

All contributions are licensed under MIT License.
