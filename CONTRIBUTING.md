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

## Documentation

- Update README.md for user-facing changes
- Add docstrings to all functions
- Document new Constitution Check gates
- Update this file for development changes

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
