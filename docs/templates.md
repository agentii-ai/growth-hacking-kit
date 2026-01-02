# Growth Hacking Kit - Template Reference

## Overview

The Growth Hacking Kit provides pre-built templates for 17 different AI agents. Each agent has two script variants (bash and PowerShell), totaling **34 template combinations**.

## Supported Agents

The Growth Hacking Kit supports templates for the following AI agents:

| Agent | Template | Use Case |
|-------|----------|----------|
| **Claude** (Claude Code) | `growthkit-template-claude-{sh\|ps}` | Anthropic's AI coding assistant |
| **Cursor Agent** | `growthkit-template-cursor-agent-{sh\|ps}` | Cursor editor AI agent |
| **Windsurf** | `growthkit-template-windsurf-{sh\|ps}` | Codeium's Windsurf IDE |
| **Gemini** | `growthkit-template-gemini-{sh\|ps}` | Google's Gemini AI |
| **Copilot** | `growthkit-template-copilot-{sh\|ps}` | GitHub Copilot CLI |
| **Qwen** | `growthkit-template-qwen-{sh\|ps}` | Alibaba's Qwen AI |
| **Codex** | `growthkit-template-codex-{sh\|ps}` | OpenAI Codex |
| **OpenCode** | `growthkit-template-opencode-{sh\|ps}` | Open-source code generation |
| **Qoder** | `growthkit-template-qoder-{sh\|ps}` | Specialized code assistant |
| **KiloCode** | `growthkit-template-kilocode-{sh\|ps}` | High-efficiency code generation |
| **Auggie** | `growthkit-template-auggie-{sh\|ps}` | Augmented coding assistant |
| **Roo** | `growthkit-template-roo-{sh\|ps}` | Kangaroo-inspired AI agent |
| **CodeBuddy** | `growthkit-template-codebuddy-{sh\|ps}` | Friendly code assistant |
| **Amp** | `growthkit-template-amp-{sh\|ps}` | Amplified code generation |
| **Shai** | `growthkit-template-shai-{sh\|ps}` | Specialized AI helper |
| **Jules** | `growthkit-template-jules-{sh\|ps}` | Jules code assistant |
| **Q** | `growthkit-template-q-{sh\|ps}` | Q-series AI agent |

## Template Structure

Each template follows a consistent directory structure:

```
.growthkit/
├── memory/
│   └── constitution.md          # Growth Hacking Kit governance document
├── templates/
│   ├── spec-template.md        # Growth specification template
│   ├── plan-template.md        # Campaign plan template
│   ├── tasks-template.md       # Task breakdown template
│   ├── drafts/                 # Draft templates and examples
│   └── commands/
│       ├── growthkit-specify.md    # /growthkit.specify command
│       ├── growthkit-plan.md       # /growthkit.plan command
│       ├── growthkit-tasks.md      # /growthkit.tasks command
│       ├── growthkit-implement.md  # /growthkit.implement command
│       └── growthkit-constitution.md # /growthkit.constitution command
└── scripts/
    ├── bash/                   # Bash scripts for automation
    │   ├── common.sh
    │   ├── setup-plan.sh
    │   ├── check-prerequisites.sh
    │   ├── create-new-feature.sh
    │   ├── update-agent-context.sh
    │   └── setup-agent-commands.sh
    └── powershell/             # PowerShell scripts (Windows)
        ├── common.ps1
        ├── setup-plan.ps1
        ├── check-prerequisites.ps1
        ├── create-new-feature.ps1
        ├── update-agent-context.ps1
        └── setup-agent-commands.ps1
```

## Key Files

### Constitution (`constitution.md`)
The foundational governance document that outlines:
- **Growth Hacking Principles** - Core tenets for viral mechanics
- **Measurement-First Development** - 2025 Dashboard metrics
- **Multi-Platform Distribution** - Viral mechanisms by platform
- **Constitution Check Gates** - Explicit criteria for spec alignment

**Version**: 1.1.0 (Growth Hacking Kit branded)

### Command Templates
The `/growthkit.*` commands are pre-configured in `templates/commands/`:

```
/growthkit.specify      → Create growth campaign specifications
/growthkit.plan         → Plan campaign execution strategy
/growthkit.tasks        → Break down into actionable growth tasks
/growthkit.implement    → Execute tasks with checkpoints
/growthkit.constitution → Review governance and principles
```

### Script Utilities
Shell scripts in `scripts/{bash,powershell}/` provide:
- **common.sh/ps1** - Shared utilities and logging
- **setup-plan.sh** - Initialize campaign planning structure
- **check-prerequisites.sh** - Validate environment requirements
- **create-new-feature.sh** - Scaffold new growth initiatives
- **update-agent-context.sh** - Sync agent with latest templates
- **setup-agent-commands.sh** - Configure agent command access

## Platform Support

### Script Types

Templates come in two variants:

| Type | Platform | Location | Extension |
|------|----------|----------|-----------|
| **bash** | Unix/Linux/macOS | `.growthkit/scripts/bash/` | `.sh` |
| **powershell** | Windows | `.growthkit/scripts/powershell/` | `.ps1` |

### Automatic Platform Detection

When running `growthkit init`:

```bash
# On macOS/Linux → Automatically selects bash (sh) scripts
growthkit init my-product --ai claude

# On Windows → Automatically selects PowerShell (ps) scripts
growthkit init my-product --ai claude

# Override with --script flag
growthkit init my-product --ai claude --script ps
```

## Installation & Setup

### Method 1: Automatic Download (Recommended)

Run `growthkit init` to automatically download the appropriate template:

```bash
# Download and extract template for your agent
growthkit init my-product --ai claude

# Choose specific script type
growthkit init my-product --ai claude --script sh   # Force bash
growthkit init my-product --ai claude --script ps   # Force PowerShell
```

The CLI will:
1. Display the **Growth Hacking Kit ASCII banner**
2. Detect your platform (Windows vs Unix)
3. Download the appropriate template from GitHub releases
4. Extract the template to your project directory

### Method 2: Manual Download

Download from GitHub releases:

```bash
# Get the latest release version
LATEST=$(curl -s https://api.github.com/repos/anthropics/growth-hacking-kit/releases/latest | jq -r '.tag_name')

# Download specific agent template
curl -L -O https://github.com/anthropics/growth-hacking-kit/releases/download/${LATEST}/growthkit-template-claude-sh-${LATEST}.zip

# Extract
unzip growthkit-template-claude-sh-${LATEST}.zip
```

## Customization

Each template can be customized:

1. **constitution.md** - Update governance principles for your product
2. **spec-template.md** - Modify the growth specification structure
3. **plan-template.md** - Adjust campaign planning format
4. **tasks-template.md** - Change task breakdown organization
5. **scripts/** - Add custom automation scripts

## Validation

Templates are automatically validated during:

1. **Local Development** - Run `scripts/validate-templates.sh` to check template integrity
2. **CI/CD Pipeline** - Pull requests trigger automatic validation
3. **Release Process** - All 34 templates validated before publishing to releases

## Validation Checks

The validator ensures:

✅ **Namespace Isolation** - Only `/growthkit.*` commands (no spec-kit references)
✅ **Required Files** - All core templates and constitution present
✅ **Content Integrity** - No lingering spec-kit/pmf-kit/blog-kit references
✅ **Directory Structure** - Proper `.growthkit/` hierarchy
✅ **Constitution Branding** - Growth Hacking Kit v1.1.0 governance
✅ **Script Consistency** - Proper bash/powershell separation
✅ **Command Count** - Minimum 5 growthkit-*.md commands
✅ **ZIP Integrity** - Templates extract correctly

## Troubleshooting

### Template Download Fails

**Problem**: `growthkit init` can't download templates

**Solutions**:
- Check network connectivity: `curl -I https://github.com`
- Verify GitHub token if rate-limited: `growthkit init --github-token YOUR_TOKEN`
- Skip TLS verification for testing: `growthkit init --skip-tls`

### Template Structure Issues

**Problem**: Templates don't contain expected files

**Solutions**:
- Run validation: `scripts/validate-templates.sh .growthkit/`
- Check template version: `cat .growthkit/memory/constitution.md | grep Version`
- Verify complete extraction: `ls -R .growthkit/`

### Script Execution Errors

**Problem**: Bash/PowerShell scripts fail

**Solutions**:
- Check prerequisites: `growthkit check`
- Verify script permissions: `chmod +x .growthkit/scripts/bash/*.sh`
- Run diagnostics: `.growthkit/scripts/bash/check-prerequisites.sh`

## For Developers

### Building Templates Locally

Build all 34 templates:

```bash
./scripts/build-templates.sh v0.2.0
```

Build specific agent variants:

```bash
# Single agent
AGENTS=claude ./scripts/build-templates.sh v0.2.0

# Specific script type
AGENTS=claude SCRIPTS=sh ./scripts/build-templates.sh v0.2.0

# Multiple agents
AGENTS="claude windsurf" ./scripts/build-templates.sh v0.2.0
```

### Testing Templates

Test template validation:

```bash
./scripts/test-validation.sh   # Run all tests
./scripts/validate-templates.sh dist/templates/  # Validate built templates
```

### Creating New Agent Template

Add a new agent:

1. Add agent to `AGENT_DIRS` in `src/growthkit/cli/config.py`
2. Add to agent list in build script
3. Run `./scripts/build-templates.sh v0.2.0` to generate
4. Validate: `./scripts/validate-templates.sh dist/templates/`

## Contributing

When adding or modifying templates:

1. Update `constitution.md` to reflect version changes
2. Ensure all templates use `/growthkit.*` namespace
3. Keep bash and PowerShell scripts in sync
4. Run validation: `./scripts/test-validation.sh`
5. Test with `growthkit init` before submitting PR

See [CONTRIBUTING.md](../CONTRIBUTING.md) for full guidelines.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **v1.1.0** | 2025-01 | Initial Growth Hacking Kit release with 34 templates for 17 agents |
| **v0.2.0** | 2024-12 | Foundation build with spec-kit compatibility |
| **v0.1.0** | 2024-11 | Proof of concept |

---

**Last Updated**: 2025-01-02
**Maintained By**: Growth Hacking Kit Team
**License**: Same as [Growth Hacking Kit](../LICENSE)
