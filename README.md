# Growth Hacking Kit

**Spec-driven growth campaign management for AI SaaS products**

Growth Hacking Kit is a CLI tool that applies systematic, constitution-driven methodology to growth campaigns. Built for growth marketers, founders, and product managers working on AI/LLM SaaS products.

## Key Features

| Feature | Description | Benefit |
|---------|-------------|---------|
| **Constitution-Driven** | Seven Core Principles enforce proven growth patterns | Avoid common pitfalls (Pilot Purgatory, Wrapper Trap, Cost-Per-Query Suicide) |
| **Multi-Platform** | Platform-specific tactics (X/Twitter 16:9, TikTok 9:16, LinkedIn case studies) | Native content that matches platform algorithms |
| **Viral Loop Engineering** | Built-in Remix, Integration, and Watermark loop mechanisms | Systematic k-factor >1.1 growth |
| **Test-Before-Scale** | Mandatory pilot phases (<10% budget) with validation gates | Reduce wasted spend on unvalidated campaigns |
| **Agent-First** | Slash commands for Claude Code, Cursor, Windsurf, Copilot | AI agents execute campaigns systematically |

## Installation

**Requirements**: Python 3.11+, [uv](https://github.com/astral-sh/uv)

```bash
# Install via uv (recommended)
uv tool install growthkit-cli

# Verify installation
growthkit --version
```

## Quick Start

### 1. Initialize Project

```bash
# Create new project
growthkit init my-campaign --ai claude

# Or initialize in current directory
growthkit init --here --ai cursor-agent
```

This creates:
- `.growthkit/` directory with constitution, templates, scripts
- Slash commands for your AI agent (`/growthkit.specify`, `/growthkit.plan`, etc.)
- Git repository (unless `--no-git` specified)

### 2. Create Campaign Specification

In your AI agent (Claude Code, Cursor, etc.), run:

```
/growthkit.specify Launch Product Hunt campaign with demo video,
first-100-user incentives, and maker community engagement strategy
```

This generates:
- New branch `001-product-hunt-launch`
- `specs/001-product-hunt-launch/spec.md` with user stories, requirements, success metrics
- Constitution Check validation results

### 3. Plan Campaign Implementation

```
/growthkit.plan Use X/Twitter for vibe coding demos, TikTok for 15-second
wow moments, Product Hunt for launch day. Pilot budget: $500, scale budget: $5000
```

This generates:
- `specs/001-product-hunt-launch/plan.md` with platform-specific tactics
- Constitution Check gate validation
- Research documents for GEO optimization
- Pilot phase scope (<10% budget)

### 4. Generate Task Breakdown

```
/growthkit.tasks
```

This generates:
- `specs/001-product-hunt-launch/tasks.md` with dependency-ordered tasks
- Phases: Setup → Pilot → Validation → Scale → Measure
- Parallel opportunities marked with [P]

### 5. Execute Campaign

```
/growthkit.implement
```

This executes:
- All tasks in dependency order
- Content creation in platform-native formats
- Pilot validation checkpoint (pause before scaling)
- Retrospective generation with learnings

## 2025 Growth Metrics Benchmarks

| Metric | Definition | Benchmark (Good) | Why It Matters |
|--------|-----------|------------------|----------------|
| **Acceptance Rate** | % of AI suggestions accepted | >30% | Measures product stickiness |
| **Time-to-Wow** | Seconds to Magic Moment | <5 minutes | Faster = higher conversion |
| **Time-to-Trust** | Days to production use | <7 days | Trust drives enterprise adoption |
| **Agent Autonomy** | Steps without human intervention | 5+ steps | Efficiency multiplier |
| **k-factor** | New users per existing user | >1.1 | Sustainable viral growth |
| **NRR** | Net Revenue Retention | 106-120% | Expansion > churn |
| **Time-to-First-Share** | Hours until social post | <24 hours | Viral loop activation |

## Seven Core Principles

1. **Spec-Driven Growth**: Every campaign starts with measurable specifications
2. **Viral Loop Engineering**: Remix, Integration, or Watermark loops built in
3. **Agent-First Architecture**: Content optimized for LLM citation (Answer Density)
4. **Measurement-First Development**: Primary, activation, and engagement metrics defined upfront
5. **Multi-Platform Distribution**: Platform-specific tactics (X: 16:9, TikTok: 9:16, etc.)
6. **Test-Before-Scale**: Pilot phase (<10% budget) with validation gates
7. **Community-Led Amplification**: Organic reach prioritized over paid ads

## Platform-Specific Tactics

### X/Twitter
- **Format**: 30-60s screen recordings, 16:9 aspect ratio
- **Viral Mechanism**: Quote tweets, developer community amplification
- **Example**: "Watch me build a SaaS in 60 seconds with [Product]"

### TikTok
- **Format**: 15-30s vertical video, 9:16 aspect ratio, hook in first 3 seconds
- **Viral Mechanism**: Duets, remixes, trending audio overlays
- **Example**: "POV: You just discovered AI that codes for you"

### LinkedIn
- **Format**: Data-driven case studies with ROI metrics
- **Viral Mechanism**: Professional sharing, credibility signals
- **Example**: "How [Company] reduced onboarding from 7 days to 5 minutes with AI"

### Product Hunt
- **Format**: Demo video + first-100-user incentives
- **Viral Mechanism**: Maker community engagement, upvote momentum
- **Example**: Launch day with exclusive early access perks

## Multi-Kit Coexistence

Growth Hacking Kit is designed to coexist with other *-kit variants:

| Kit | Package Name | Directory | Slash Commands | Purpose |
|-----|--------------|-----------|----------------|---------|
| **Spec Kit** | `specify-cli` | `.specify/` | `/speckit.*` | Software development |
| **Growth Hacking Kit** | `growthkit-cli` | `.growthkit/` | `/growthkit.*` | Growth campaigns |
| **Blog Kit** | `blogkit-cli` | `.blogkit/` | `/blogkit.*` | Content marketing |
| **PD Kit** | `pdkit-cli` | `.pdkit/` | `/pdkit.*` | Product design |

Install multiple kits on the same machine without conflicts:

```bash
uv tool install specify-cli
uv tool install growthkit-cli
uv tool install blogkit-cli

# All commands work independently
specify init my-app
growthkit init my-campaign
blogkit init my-blog
```

## CLI Commands

### `growthkit init`

Initialize a new growth-hacking-kit project.

```bash
growthkit init <project-name> [OPTIONS]

Options:
  --ai TEXT              Target AI agent (claude, cursor-agent, windsurf, copilot)
  --script TEXT          Script type (bash, powershell)
  --ignore-agent-tools   Skip agent tool installation
  --no-git              Skip git initialization
  --here                Initialize in current directory
  --force               Overwrite existing files
  --skip-tls            Skip TLS verification for network requests
  --debug               Enable debug logging
  --github-token TEXT   GitHub token for private repositories
```

**Examples**:

```bash
# Claude Code user
growthkit init my-campaign --ai claude

# Cursor user in existing directory
growthkit init --here --ai cursor-agent

# Windows user with PowerShell
growthkit init my-campaign --ai copilot --script powershell
```

### `growthkit check`

Verify dependencies and environment.

```bash
growthkit check

Checks:
  ✅ Git installed (version 2.39.0)
  ✅ Python installed (version 3.11.5)
  ✅ uv installed (version 0.1.23)
  ✅ Claude Code detected
  ⚠️  Cursor not found
```

## Constitution Check Gates

Every campaign plan is validated against mandatory and advisory gates:

### Mandatory Gates (MUST pass before implementation)

- ✅ Campaign specification exists
- ✅ Growth type identified (Vibe/Trust/Agentic)
- ✅ Target audience specific (not "developers" but "Python backend devs using FastAPI")
- ✅ Viral loop mechanism specified (Remix/Integration/Watermark)
- ✅ k-factor target defined (>1.1 for sustainable growth)
- ✅ Primary/activation/engagement metrics set
- ✅ Pilot phase scope defined (<10% of final budget)

### Advisory Gates (re-check after design)

- ⚠ Content optimized for "Answer Density" (structured tables, benchmarks)
- ⚠ Platform-specific content strategy defined
- ⚠ Community-led amplification plan established

## Common Anti-Patterns (Failure Modes)

| Anti-Pattern | Description | Fix |
|--------------|-------------|-----|
| **Pilot Purgatory** | Endless A/B testing, never scaling | Set time-box (2-4 weeks), clear go/no-go criteria |
| **Wrapper Trap** | Over-reliance on OpenAI without differentiation | Add unique workflows, custom models, proprietary data |
| **Cost-Per-Query Suicide** | Free tier loses money on every query | Price by value (seats, outputs) not usage (tokens) |
| **Generic Cross-Platform** | Same content on X/Twitter and TikTok | Platform-native content (X: 16:9, TikTok: 9:16) |

## Examples

### Example 1: Product Hunt Launch Campaign

```bash
# Initialize project
growthkit init product-hunt-launch --ai claude

# In Claude Code, run:
/growthkit.specify Launch Product Hunt campaign with demo video,
first-100-user incentives, and maker community engagement strategy

/growthkit.plan Use Product Hunt for launch day, X/Twitter for
pre-launch buzz, GitHub for technical walkthrough. Pilot budget: $200,
scale budget: $2000

/growthkit.tasks

/growthkit.implement
```

**Results**:
- Branch: `001-product-hunt-launch`
- Spec: User stories for launch day, pre-launch, post-launch engagement
- Plan: Platform-specific tactics (demo video format, upvote strategy, maker outreach)
- Tasks: 45 tasks across Setup, Pilot, Scale, Measure phases
- Implementation: AI agent executes tasks, creates content, tracks metrics

### Example 2: TikTok Viral Loop

```bash
growthkit init tiktok-viral --ai cursor-agent

# In Cursor, run:
/growthkit.specify Create TikTok viral loop with 15-second wow moments
showcasing AI code generation, targeting junior developers and bootcamp students

/growthkit.plan Use TikTok for primary distribution (9:16 vertical,
hook in 3 seconds), X/Twitter for cross-promotion. Pilot budget: $300,
scale budget: $3000

/growthkit.tasks

/growthkit.implement
```

**Results**:
- Viral loop: Watermark Loop (branded outputs shared on social)
- Target k-factor: >1.2 (TikTok's virality multiplier)
- Content format: 15-30s vertical videos with trending audio overlays
- Success metric: Time-to-First-Share <12 hours (TikTok velocity)

## Project Structure

After `growthkit init`, your project will have:

```
my-campaign/
├── .growthkit/
│   ├── memory/
│   │   └── constitution.md        # Seven Core Principles
│   ├── scripts/
│   │   ├── bash/
│   │   │   ├── common.sh
│   │   │   ├── check-prerequisites.sh
│   │   │   ├── create-new-feature.sh
│   │   │   ├── setup-plan.sh
│   │   │   └── update-agent-context.sh
│   │   └── powershell/            # Windows equivalents
│   └── templates/
│       ├── spec-template.md
│       ├── plan-template.md
│       ├── tasks-template.md
│       └── commands/              # Slash command templates
│           ├── growthkit-specify.md
│           ├── growthkit-plan.md
│           ├── growthkit-tasks.md
│           ├── growthkit-implement.md
│           └── growthkit-constitution.md
├── .claude/commands/              # Claude Code integration
│   ├── growthkit-specify.md      # Symlink to .growthkit/templates/commands/
│   ├── growthkit-plan.md
│   └── ...
├── specs/                         # Campaign documentation
│   └── 001-campaign-name/
│       ├── spec.md                # Campaign specification
│       ├── plan.md                # Implementation plan
│       ├── tasks.md               # Task breakdown
│       ├── research.md            # Platform research
│       ├── retrospective.md       # Post-campaign learnings
│       └── checklists/
│           └── requirements.md    # Quality validation
└── README.md
```

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Links

- **Documentation**: [docs.growth-hacking-kit.dev](https://docs.growth-hacking-kit.dev)
- **GitHub**: [github.com/agentii/growth-hacking-kit](https://github.com/agentii/growth-hacking-kit)
- **Issues**: [github.com/agentii/growth-hacking-kit/issues](https://github.com/agentii/growth-hacking-kit/issues)

---

**Growth Hacking Kit v0.1.0** - Built with systematic growth methodology for AI SaaS products.
