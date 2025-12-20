# Growth Hacking Kit - API Reference

## Overview

The Growth Hacking Kit provides a Python CLI for spec-driven growth campaign management. This document describes the public API for programmatic use.

## Table of Contents

- [Installation](#installation)
- [Core Modules](#core-modules)
- [CLI Commands](#cli-commands)
- [Constitution Check](#constitution-check)
- [Configuration](#configuration)
- [Examples](#examples)

## Installation

```bash
# Install from PyPI
pip install growthkit-cli

# Or install for development
git clone https://github.com/agentii/growth-hacking-kit.git
cd growth-hacking-kit
pip install -e ".[dev]"
```

## Core Modules

### growthkit.cli.config

Configuration constants and settings.

```python
from growthkit.cli.config import (
    KIT_NAME,
    PACKAGE_DIR,
    SPECS_DIR,
    AGENT_DIRS,
    BRANCH_PATTERN,
    DEFAULT_AI_AGENT,
)

# Example: Get the growthkit directory name
package_dir = PACKAGE_DIR  # ".growthkit"

# Example: Get all supported agents
agents = AGENT_DIRS  # {"claude": ".claude", "cursor": ".cursor", ...}
```

### growthkit.cli.utils

Utility functions for common operations.

```python
from growthkit.cli.utils import (
    create_campaign_branch,
    get_next_campaign_number,
    extract_campaign_name,
    get_campaign_dir_from_branch,
    detect_installed_agents,
    render_template,
    run_bash_script,
)

# Example: Create a new campaign branch
branch_name = create_campaign_branch(1, "product-hunt-launch")
# Returns: "001-product-hunt-launch"

# Example: Get the next campaign number
next_num = get_next_campaign_number()
# Returns: 1

# Example: Extract campaign name from description
name = extract_campaign_name("Launch Product Hunt campaign with demo video")
# Returns: "product-hunt-launch"

# Example: Get campaign directory
campaign_dir = get_campaign_dir_from_branch("001-product-hunt-launch")
# Returns: Path to specs/001-product-hunt-launch/

# Example: Detect installed AI agents
agents = detect_installed_agents()
# Returns: {"claude": True, "cursor": False, "windsurf": False, "copilot": False}

# Example: Render a Jinja2 template
content = render_template(
    Path(".growthkit/templates/spec-template.md"),
    {"campaign_name": "Product Hunt Launch"}
)

# Example: Run a bash script
result = run_bash_script("check-prerequisites", [])
# Returns: {"stdout": "...", "stderr": "", "returncode": 0, "success": True}
```

### growthkit.cli.specify

Campaign specification generation.

```python
from growthkit.cli.specify import specify_command

# Example: Create a new campaign specification
specify_command(
    description="Launch Product Hunt campaign with demo video",
    force=False,
    debug=False
)
```

### growthkit.cli.plan

Implementation planning.

```python
from growthkit.cli.plan import plan_command

# Example: Create implementation plan
plan_command(
    description="001-product-hunt-launch",
    force=False,
    debug=False
)
```

### growthkit.cli.tasks

Task generation.

```python
from growthkit.cli.tasks import tasks_command

# Example: Generate task breakdown
tasks_command(
    description="001-product-hunt-launch",
    force=False,
    debug=False
)
```

### growthkit.cli.implement

Campaign execution.

```python
from growthkit.cli.implement import implement_command

# Example: Execute campaign
implement_command(
    description="001-product-hunt-launch",
    force=False,  # Skip interactive confirmations
    debug=False
)
```

### growthkit.constitution.validator

Constitution Check validation.

```python
from growthkit.constitution.validator import ConstitutionValidator

validator = ConstitutionValidator()

# Example: Validate specification
spec_results = validator.validate_spec("001-product-hunt-launch")
# Returns:
# {
#     "status": "PASS" | "FAIL",
#     "passed_gates": [...],
#     "failed_gates": [...],
# }

# Example: Validate plan
plan_results = validator.validate_plan("001-product-hunt-launch")
# Returns:
# {
#     "status": "PASS" | "FAIL",
#     "mandatory_gates": {"passed": [...], "failed": [...]},
#     "advisory_gates": {"passed": [...], "failed": [...]},
# }

# Example: Count clarification markers
markers = validator.count_clarification_markers("001-product-hunt-launch")
# Returns:
# {
#     "count": 2,
#     "max_allowed": 3,
#     "status": "PASS",
#     "markers": ["[NEEDS CLARIFICATION...]", "[NEEDS CLARIFICATION...]"]
# }

# Example: Extract growth type
growth_type = validator.extract_growth_type(spec_content)
# Returns:
# {
#     "identified_types": ["vibe", "trust"],
#     "primary_type": "vibe",
#     "count": 2
# }

# Example: Extract viral loop
viral_loop = validator.extract_viral_loop(spec_content)
# Returns:
# {
#     "identified_loops": ["remix"],
#     "primary_loop": "remix",
#     "count": 1
# }

# Example: Extract metrics
metrics = validator.extract_metrics(spec_content)
# Returns:
# {
#     "metrics": {
#         "k_factor": {"found": True, "value": "1.5"},
#         "time_to_wow": {"found": True, "value": "3"},
#         "nrr": {"found": False, "value": None},
#         ...
#     },
#     "defined_count": 2
# }
```

## CLI Commands

### growthkit init

Initialize a new Growth Hacking Kit project.

```bash
growthkit init my-campaign --ai claude
growthkit init . --here --ai cursor-agent
growthkit init project-dir --ai windsurf --force
```

**Options**:
- `--ai`: Target AI agent (claude, cursor-agent, windsurf, copilot)
- `--script`: Script type (bash or powershell) - default: bash
- `--no-git`: Skip git repository initialization
- `--here`: Initialize in current directory
- `--force`: Force overwrite existing files
- `--debug`: Enable debug logging

### growthkit check

Check for installed dependencies and AI agents.

```bash
growthkit check
growthkit check --debug
```

### growthkit specify

Create a campaign specification from natural language description.

```bash
growthkit specify "Launch Product Hunt campaign with demo video"
growthkit specify "Build Twitter/X viral loop strategy" --force
```

**Options**:
- `--force`: Force overwrite existing spec
- `--debug`: Enable debug logging

### growthkit plan

Create an implementation plan from an approved specification.

```bash
growthkit plan "001-product-hunt-launch"
growthkit plan "001-product-hunt-launch" --force
```

**Options**:
- `--force`: Force overwrite existing plan
- `--debug`: Enable debug logging

### growthkit tasks

Generate actionable task breakdown from implementation plan.

```bash
growthkit tasks "001-product-hunt-launch"
growthkit tasks "001-product-hunt-launch" --force
```

**Options**:
- `--force`: Force overwrite existing tasks
- `--debug`: Enable debug logging

### growthkit implement

Execute campaign tasks with checkpoint validations.

```bash
growthkit implement "001-product-hunt-launch"
growthkit implement "001-product-hunt-launch" --force
```

**Options**:
- `--force`: Skip checkpoint confirmations
- `--debug`: Enable debug logging

### growthkit version

Show version information.

```bash
growthkit version
```

## Constitution Check

The Constitution Check system validates specifications and plans against 10 gates based on Seven Core Principles.

### Mandatory Gates (Spec Validation)

1. **spec_exists**: Specification file exists
2. **growth_type_identified**: Vibe, Trust, or Agentic growth identified
3. **target_audience_specific**: Target audience clearly defined
4. **viral_loop_defined**: Remix, Integration, or Watermark loop selected
5. **k_factor_target**: K-factor metric specified (>1.1)
6. **metrics_defined**: Primary activation, engagement, or other metrics defined
7. **pilot_scoped**: Pilot phase budget and scope defined

### Advisory Gates (Plan Validation)

1. **content_optimized**: Content optimization mentioned
2. **platform_strategy**: Multi-platform strategy (X/Twitter, TikTok, LinkedIn, GitHub, Product Hunt)
3. **community_amplification**: Community amplification strategy

## Configuration

### Environment Variables

```bash
# Set default AI agent for new projects
export GROWTHKIT_DEFAULT_AI=cursor-agent

# Enable debug logging
export GROWTHKIT_DEBUG=true

# Set custom template directory
export GROWTHKIT_TEMPLATES_DIR=/path/to/templates
```

### Configuration Files

All configuration is code-based in `src/growthkit/cli/config.py`. Key constants:

```python
KIT_NAME = "growthkit"                    # Kit identifier
PACKAGE_DIR = ".growthkit"                # Main directory
SPECS_DIR = "specs"                       # Specifications directory
CONSTITUTION_FILE = ".growthkit/memory/constitution.md"  # Constitution location

# Supported AI agents and their command directories
AGENT_DIRS = {
    "claude": ".claude",
    "cursor-agent": ".cursor",
    "windsurf": ".windsurf",
    "copilot": ".copilot",
}

# Campaign branch naming pattern
BRANCH_PATTERN = r"^(\d{3})-(.+)$"

# Default AI agent if none detected
DEFAULT_AI_AGENT = "claude"
```

## Examples

### Complete Workflow

```bash
# 1. Initialize project
growthkit init my-startup --ai claude

# 2. Create campaign specification
growthkit specify "Launch Product Hunt campaign targeting startup founders"

# 3. Create implementation plan
growthkit plan 001-product-hunt-launch

# 4. Generate task breakdown
growthkit tasks 001-product-hunt-launch

# 5. Execute campaign with checkpoints
growthkit implement 001-product-hunt-launch

# 6. Review retrospective
cat specs/001-product-hunt-launch/retrospective.md
```

### Programmatic Usage

```python
from pathlib import Path
from growthkit.cli import utils
from growthkit.constitution.validator import ConstitutionValidator

# Create a campaign
branch = utils.create_campaign_branch(1, "twitter-launch")

# Validate campaign
validator = ConstitutionValidator()
spec_results = validator.validate_spec("001-twitter-launch")

if spec_results["status"] == "PASS":
    print("✓ Specification is valid")
else:
    print("✗ Specification has failures:")
    for failure in spec_results["failed_gates"]:
        print(f"  - {failure['gate']}: {failure['message']}")
```

### Error Handling

```python
from pathlib import Path
from growthkit.cli import utils

try:
    campaign_dir = utils.get_campaign_dir_from_branch("001-product-hunt-launch")
except ValueError as e:
    print(f"Campaign not found: {e}")
    exit(1)
```

## Architecture

### Directory Structure

```
.growthkit/
├── memory/
│   └── constitution.md          # Seven Core Principles
├── scripts/
│   ├── bash/                    # Bash utilities
│   └── powershell/              # PowerShell utilities (planned)
└── templates/
    ├── spec-template.md         # Specification template
    ├── plan-template.md         # Plan template
    ├── tasks-template.md        # Tasks template
    └── commands/                # AI agent command templates
        ├── growthkit-specify.md
        ├── growthkit-plan.md
        ├── growthkit-tasks.md
        └── growthkit-implement.md

specs/
└── {campaign-id}/
    ├── spec.md                  # Campaign specification
    ├── plan.md                  # Implementation plan
    ├── tasks.md                 # Task breakdown
    ├── retrospective.md         # Execution retrospective
    ├── checklists/
    │   ├── requirements.md      # Quality checklist
    │   └── planning.md          # Planning checklist
    └── assets/                  # Campaign assets
```

### Module Structure

```python
growthkit/
├── __init__.py                  # Version: "0.1.0"
├── __main__.py                  # python -m execution
├── cli/
│   ├── config.py                # 45+ configuration constants
│   ├── main.py                  # Typer CLI application
│   ├── utils.py                 # 20+ utility functions
│   ├── specify.py               # Specification command
│   ├── plan.py                  # Planning command
│   ├── tasks.py                 # Task generation command
│   └── implement.py             # Execution command
├── constitution/
│   ├── gates.py                 # 10 Constitution Check gates
│   └── validator.py             # Validation logic
└── templates/
    └── constitution.md          # Seven Core Principles template
```

## Performance Targets

- CLI initialization: <2 seconds
- Specification generation: <5 seconds
- Constitution Check validation: <1 second
- Plan generation: <5 seconds
- Task generation: <5 seconds

## Limitations

1. **No database**: File-based specifications in markdown
2. **Single git repo**: One .git per project
3. **Manual approval**: AI generates, user reviews before posting
4. **No auto-posting**: Platform posting requires user authorization
5. **Markdown-based**: All artifacts are markdown for version control

## Support

- **Issues**: https://github.com/agentii/growth-hacking-kit/issues
- **Discussions**: https://github.com/agentii/growth-hacking-kit/discussions
- **Email**: support@agentii.ai

## License

MIT License - See LICENSE file for details
