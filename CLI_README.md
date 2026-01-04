# Growth-Hacking-Kit CLI

Command-line tool for initializing and managing growth campaign projects using the Growth-Hacking-Kit framework.

## Installation

### Via uvx (Recommended)

```bash
uvx --from git+https://github.com/agentii-ai/growth-hacking-kit.git growthkit init my-campaign
```

### Via pip

```bash
pip install git+https://github.com/agentii-ai/growth-hacking-kit.git
growthkit init my-campaign
```

### For Development

```bash
git clone https://github.com/agentii-ai/growth-hacking-kit.git
cd growth-hacking-kit
pip install -e .
```

## Usage

### Initialize a New Project

```bash
# Interactive mode (prompts for options)
growthkit init

# With project name
growthkit init my-growth-campaign

# Specify agent and script type
growthkit init my-campaign --agent claude --script sh

# Short form
growthkit init my-campaign -a cursor-agent -s ps

# Force overwrite existing directory
growthkit init my-campaign --agent windsurf --force
```

### Available Options

- `--agent, -a`: Choose AI agent (claude, cursor-agent, windsurf, gemini, copilot, etc.)
- `--script, -s`: Script type - `sh` (bash) or `ps` (PowerShell)
- `--version, -v`: Template version (default: latest)
- `--force, -f`: Overwrite existing directory

### Supported AI Agents

The CLI supports 17 AI agents:

- **claude** - Claude Code (Anthropic)
- **cursor-agent** - Cursor AI
- **windsurf** - Windsurf IDE
- **gemini** - Google Gemini
- **copilot** - GitHub Copilot
- **qoder** - Qoder AI
- **qwen** - Qwen AI
- **opencode** - OpenCode AI
- **codex** - OpenAI Codex
- **kilocode** - Kilocode AI
- **auggie** - Augment Code
- **roo** - Roo Cline
- **codebuddy** - CodeBuddy AI
- **amp** - AMP AI
- **shai** - Shai AI
- **q** - Amazon Q
- **bob** - Bob AI

## What Gets Installed

Each template includes:

- **Growth-Hacking-Kit Constitution** (v1.1.0) with growth-specific principles
- **Workflow templates**: spec.md, plan.md, tasks.md
- **5 slash commands**: /growthkit.* commands for all workflow phases
- **Scripts**: bash or PowerShell variants for automation
- **.specify/ directory**: Working directory per multi-kit coexistence strategy

## Project Structure

After initialization:

```
my-campaign/
├── .{agent}/
│   └── commands/
│       ├── growthkit.specify.md
│       ├── growthkit.plan.md
│       ├── growthkit.tasks.md
│       ├── growthkit.implement.md
│       └── growthkit.constitution.md
└── .specify/
    ├── memory/
    │   └── constitution.md (v1.1.0)
    ├── scripts/
    │   ├── bash/ (for sh variants)
    │   └── powershell/ (for ps variants)
    └── templates/
        ├── spec-template.md
        ├── plan-template.md
        └── tasks-template.md
```

## Next Steps After Init

1. Navigate to your project:
   ```bash
   cd my-campaign
   ```

2. Review the constitution:
   ```bash
   cat .specify/memory/constitution.md
   ```

3. Start your first campaign:
   ```bash
   # Use your AI agent's command
   /growthkit.specify "Launch viral referral program for SaaS product"
   ```

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/
ruff check src/
```

## License

MIT License - see LICENSE file for details

## Links

- **Homepage**: https://github.com/agentii-ai/growth-hacking-kit
- **Issues**: https://github.com/agentii-ai/growth-hacking-kit/issues
- **Releases**: https://github.com/agentii-ai/growth-hacking-kit/releases
