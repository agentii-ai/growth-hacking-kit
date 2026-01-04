<div align="center">
    <img src="./media/logo.png" alt="Growth Hacking Kit Logo" width="200" height="200"/>
    <h1>🚀 Growth Hacking Kit</h1>
    <h3><em>Discover and validate growth strategies faster with AI agents.</em></h3>
</div>

<p align="center">
    <strong>A spec-driven toolkit for systematic growth campaign planning and execution of AI SaaS products, built on the foundations of spec-kit.</strong>
</p>

<p align="center">
    <a href="https://github.com/agentii-ai/growth-hacking-kit/actions"><img src="https://img.shields.io/badge/status-production-green" alt="Status"/></a>
    <a href="https://github.com/agentii-ai/growth-hacking-kit/stargazers"><img src="https://img.shields.io/github/stars/agentii-ai/growth-hacking-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/agentii-ai/growth-hacking-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/agentii-ai/growth-hacking-kit" alt="License"/></a>
    <a href="https://kits.agentii.ai"><img src="https://img.shields.io/badge/kits-agentii.ai-blue" alt="Kit Variants"/></a>
</p>

---

## 🎯 What is Growth Hacking Kit?

**Growth Hacking Kit** is a specialized variant of [**Spec-Kit**](https://github.com/github/spec-kit), adapted for growth campaign planning and execution of AI SaaS products.

While Spec-Kit enables spec-driven software development with AI agents, **Growth Hacking Kit applies the same methodology to the domain of growth marketing, viral mechanics, and campaign validation**—helping founders and growth teams discover sustainable growth through structured, AI-assisted workflows instead of ad-hoc experimentation.

### Key Differences from Spec-Kit

| Aspect | Spec-Kit | Growth Hacking Kit |
|--------|----------|--------------------|
| **Focus** | Software feature development | Growth campaign planning & execution |
| **Primary Workflow** | Specification → Plan → Code → Test | Specification → Research → Tasks → Execute |
| **Success Metrics** | Code quality, test coverage, performance | K-factor, time-to-wow, engagement rate, NRR |
| **Deliverables** | Production software & APIs | Campaign specifications, growth tactics, retrospective analysis |
| **CLI Command** | `specify` | `growthkit` |
| **Agent Commands** | `/speckit.*` | `/growthkit.*` |

---

## 🚀 Get Started

### 1. Install Growth Hacking Kit

Choose your preferred installation method:

#### Option 1: One-Time Usage (Recommended)

Run directly without installing—always uses the latest version:

```bash
uvx --from git+https://github.com/agentii-ai/growth-hacking-kit.git growthkit init my-product
```

> **Note**: This project is improving rapidly. We recommend `uvx` to always get the latest features and fixes.

#### Option 2: Persistent Installation

Install once and use everywhere (may require periodic updates):

```bash
uv tool install growthkit-cli --from git+https://github.com/agentii-ai/growth-hacking-kit.git
```

Then use the tool directly:

```bash
growthkit init my-product
```

To update to the latest version:

```bash
uv tool install growthkit-cli --force --from git+https://github.com/agentii-ai/growth-hacking-kit.git
```

### 2. Initialize Your First Growth Campaign Project

```bash
growthkit init my-ai-product
cd my-ai-product
```

This creates a project with growth-specific templates, constitution, and agent commands.

### 3. Launch Your AI Agent

Open your AI assistant (Claude Code, Cursor, Windsurf, etc.) in the project directory. You'll see `/growthkit.*` commands available:

```bash
/growthkit.constitution    # Establish growth-specific principles
/growthkit.specify         # Define what you're trying to grow
/growthkit.clarify         # Resolve ambiguities in your hypothesis
/growthkit.plan            # Create campaign execution plan
/growthkit.tasks           # Generate actionable growth tasks
/growthkit.implement       # Execute growth campaign workflow
```

### 4. Run Your First Growth Discovery Workflow

```bash
/growthkit.specify Launch Product Hunt campaign for AI code assistant targeting solo developers and small teams, focusing on onboarding speed and code generation quality
```

This generates a growth specification with:
- Sharp personas (role, company, tools, environment)
- Growth type and viral loop mechanism
- Platform-specific distribution strategy
- Success metrics (k-factor, time-to-wow, activation rate)
- Pilot phase budget and scope

---

## 🤖 Supported AI Agents

Growth Hacking Kit works with all agents supported by Spec-Kit:

| Agent | Support | Notes |
|-------|---------|-------|
| [Claude Code](https://www.anthropic.com/claude-code) | ✅ | Native support |
| [Cursor](https://cursor.sh/) | ✅ | Full integration |
| [Windsurf](https://windsurf.com/) | ✅ | Complete support |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ✅ | Verified working |
| [GitHub Copilot](https://github.com/features/copilot) | ✅ | Compatible |
| [Qoder CLI](https://qoder.com/cli) | ✅ | Supported |
| Plus 10+ additional agents | ✅ | See Spec-Kit docs |

---

## 📦 Growth Hacking Kit Templates

Growth Hacking Kit provides **34 project templates** (17 agents × 2 script types) automatically downloaded when you run `growthkit init`. Each template includes:

- **Growth Hacking Kit Constitution v1.1.0** with 7 growth-focused principles
- **Workflow templates**: spec-template.md, plan-template.md, tasks-template.md
- **5 core commands**:
  - `/growthkit.specify` - Define growth campaign
  - `/growthkit.plan` - Create campaign plan
  - `/growthkit.tasks` - Generate task breakdown
  - `/growthkit.implement` - Execute with checkpoints
  - `/growthkit.constitution` - View governance
- **Automation scripts**: Bash and PowerShell for cross-platform support
- **Memory system**: .growthkit/ working directory with growth governance

### Supported Template Agents (17 Total)

Templates available for all major AI agents in both **bash** and **PowerShell** variants:

**Tier 1 (Official)**: Claude Code • Cursor Agent • Windsurf • Google Gemini
**Tier 2**: GitHub Copilot • Qwen • Codex • OpenCode
**Tier 3**: Qoder • KiloCode • Auggie • Roo • CodeBuddy • AMP • Shai • Jules • Q

**👉 [Full Template Reference →](./docs/templates.md)** - See all 17 agents, template structure, platform support, and customization guides.

Download from [GitHub Releases](https://github.com/anthropics/growth-hacking-kit/releases) with SHA-256 checksums.

---

## 🎯 Core Growth Workflow

### Phase 1: Specification (`/growthkit.specify`)

Define **WHAT** you're trying to grow and **WHY**:
- Target personas (role/skill, company, tools, environment)
- Growth type (Vibe Growth, Trust Growth, Agentic Growth)
- Viral loop mechanism (Remix Loop, Integration Loop, Watermark Loop)
- Success metrics (k-factor >1.1, time-to-wow <5 min, NRR >106%)
- Platform distribution strategy
- Pilot phase budget and scope

### Phase 2: Clarification (`/growthkit.clarify`)

Resolve ambiguities before committing to execution:
- Validate persona sharpness and specificity
- Clarify growth mechanisms and viral loops
- Define success metrics precisely
- Identify unstated assumptions about distribution

### Phase 3: Planning (`/growthkit.plan`)

Define **HOW** you'll execute growth:
- Platform-specific tactics (X/Twitter 16:9, TikTok 9:16, LinkedIn case studies)
- Content strategy and creative direction
- Audience targeting and acquisition strategy
- Pilot phase validation criteria
- Scale phase budget and timeline

### Phase 4: Task Breakdown (`/growthkit.tasks`)

Generate actionable growth tasks:
- Organize by phases: Setup → Pilot → Scale → Measure
- Pilot phase execution (<10% of total budget)
- Go/no-go validation checkpoints
- Scale phase parallel opportunities
- Measurement and retrospective tasks

### Phase 5: Execution (`/growthkit.implement`)

Execute growth campaign systematically:
- Create campaign assets (video, copy, graphics)
- Run pilot phase with audience segment
- Validate go/no-go criteria before scaling
- Execute full-scale distribution
- Measure and document learnings

---

## 🌟 Growth Hacking Kit Constitution

Growth Hacking Kit is built on 7 core principles that guide all campaign work:

### I. Spec-Driven Growth
Plan every campaign with measurable specifications before execution.

### II. Viral Loop Engineering
Build systematic viral mechanics (Remix, Integration, or Watermark) into every campaign.

### III. Agent-First Distribution
Optimize content for AI agent citation and algorithmic amplification.

### IV. Measurement-First Metrics
Define success metrics (k-factor, time-to-wow, engagement) upfront, not retrospectively.

### V. Platform-Native Tactics
Create platform-specific content (X: 16:9, TikTok: 9:16, LinkedIn: professional) that matches algorithms.

### VI. Test-Before-Scale
Run mandatory pilot phases (<10% budget) with validation gates before full rollout.

### VII. Community-Led Growth
Prioritize organic community amplification over paid advertising.

See [`memory/constitution.md`](./memory/constitution.md) for full details.

---

## 📚 Reference Documentation

Growth Hacking Kit includes comprehensive reference materials to guide your campaigns:

- **`refs/0_overview.md`** - Overview of growth campaigns for AI SaaS products
- **`refs/1_principles_for_constitution.md`** - Growth-specific principles and patterns
- **`refs/2_define_for_specify.md`** - How to structure sharp growth specifications
- **`refs/3_project_management_for_plan.md`** - Campaign planning methodology
- **`refs/4_pm_tasking_for_tasks.md`** - Growth campaign task patterns
- **`refs/instructions.md`** - How to create your own kit variants

---

## 🔧 Multi-Kit Installation

Growth Hacking Kit is designed to coexist with Spec-Kit and other kit variants:

```bash
# Install Spec-Kit for software development
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Install Growth Hacking Kit for growth campaigns
uv tool install growthkit-cli --from git+https://github.com/agentii-ai/growth-hacking-kit.git

# Both tools work independently
specify init my-feature      # Software feature project
growthkit init my-campaign   # Growth campaign project
```

In your AI agent, both command namespaces are available:
- `/speckit.*` commands for software development workflows
- `/growthkit.*` commands for growth campaign workflows

---

## 🎛️ CLI Reference

### `growthkit init` - Initialize Growth Campaign Project

```bash
growthkit init <PROJECT_NAME>
growthkit init my-product --agent claude
growthkit init my-product --agent cursor-agent --script ps   # PowerShell scripts
```

**Options:**
- `--agent, -a` - Specify AI assistant (claude, cursor-agent, windsurf, gemini, copilot, qoder, qwen, opencode, codex, kilocode, auggie, roo, codebuddy, amp, shai, q, bob)
- `--script, -s` - Script variant (sh for bash/zsh, ps for PowerShell)
- `--version, -v` - Template version to download (default: latest)
- `--force, -f` - Overwrite existing directory without confirmation

**Interactive Mode:**

If you don't provide options, the CLI will prompt you interactively:

```bash
growthkit init my-product
# Prompts for: agent selection, script type
```

---

## 🚀 Examples by Growth Type

### Vibe Growth (Developer Tools - Cursor, Claude Code)

```
growthkit init ai-code-assistant
/growthkit.specify "Validate product-market-fit for AI-powered code generation among backend engineers working at Series A SaaS companies, similar to Cursor's approach"
```

Expected artifacts:
- Personas: Backend engineers at 50-500 person SaaS, use Python/Go/Rust
- Viral loop: Watermark Loop (code snippets shared with product watermark)
- Success metric: Time-to-first-completion <10 seconds, edit distance <15%
- K-factor target: >1.2 (developer network effects)

### Trust Growth (Vertical AI - Harvey, Writer)

```
growthkit init contract-ai
/growthkit.specify "Validate willingness-to-pay for AI-powered legal document analysis among solo practitioners and small law firms with 1-10 lawyers"
```

Expected artifacts:
- Personas: Solo practitioners and 2-person law firms, spending >$5k/month on legal research
- Viral loop: Integration Loop (AI outputs embedded in existing legal workflows)
- Success metric: Time-to-first-document <3 minutes, cost savings >50% vs. manual review
- K-factor target: >1.1 (professional referral network)

### Agentic Growth (Creative Tools - Runway, HeyGen)

```
growthkit init video-generation
/growthkit.specify "Validate demand for text-to-video generation among YouTube creators and TikTok content creators with 10k-100k subscriber base"
```

Expected artifacts:
- Personas: Content creators, 20-40 hours/week creating videos, spend $200-500/month on tools
- Viral loop: Remix Loop (creators share generated videos with platform attribution)
- Success metric: Time-to-first-render <5 minutes, video completion rate >80%
- K-factor target: >1.3 (TikTok/YouTube network effects)

---

## 📖 Learn More

- **[Growth Hacking Kit Specification](./specs/001-growth-hacking-kit/spec.md)** - Full feature specification
- **[Growth Hacking Kit Implementation Plan](./specs/001-growth-hacking-kit/plan.md)** - Technical implementation details
- **[API Reference](./docs/API.md)** - Complete API documentation
- **[Troubleshooting Guide](./docs/TROUBLESHOOTING.md)** - Common issues and solutions
- **[Spec-Kit Repository](https://github.com/github/spec-kit)** - Upstream project for software development
- **[Spec-Driven Development Methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md)** - Core methodology

---

## 🚧 Roadmap

### Phase 1: Core Growth Workflow ✅ COMPLETE
- `growthkit init` - Project initialization with 17 AI agents
- `/growthkit.specify` - Campaign specification
- `/growthkit.clarify` - Ambiguity resolution
- `/growthkit.plan` - Campaign planning
- `/growthkit.tasks` - Task generation
- `/growthkit.implement` - Campaign execution

### Phase 2: Growth Intelligence (v0.2.0) 🔄 PLANNED
- Growth metrics dashboard
- Viral loop analyzer
- Platform-specific optimization engine
- A/B testing framework
- Real-time campaign monitoring

### Phase 3: Team Collaboration (v0.3.0) 🔄 PLANNED
- Multi-user campaign management
- Shared retrospectives
- Team role-based access
- Campaign templates library

### Phase 4: Advanced Analytics (v1.0.0) 🔄 PLANNED
- Attribution modeling
- Cohort analysis
- Predictive growth forecasting
- Community sentiment analysis

---

## 🏗️ Project Structure

```
growth-hacking-kit/
├── .claude/commands/          # Claude Code slash commands
│   ├── growthkit-constitution.md
│   ├── growthkit-specify.md
│   ├── growthkit-clarify.md
│   ├── growthkit-plan.md
│   ├── growthkit-tasks.md
│   └── growthkit-implement.md
├── .growthkit/                # Growth Hacking Kit templates
│   ├── memory/
│   │   └── constitution.md        # Growth principles (v0.1.0)
│   ├── templates/
│   │   ├── spec-template.md       # Campaign specification template
│   │   ├── plan-template.md       # Campaign planning template
│   │   ├── tasks-template.md      # Task breakdown template
│   │   └── commands/              # Agent command templates
│   └── scripts/
│       ├── bash/                  # Bash automation scripts
│       └── powershell/            # PowerShell automation scripts
├── docs/                      # Documentation
│   ├── API.md                 # API reference
│   └── TROUBLESHOOTING.md     # Troubleshooting guide
├── specs/
│   └── 001-growth-hacking-kit/    # Feature specification
├── tests/                     # Test suite
├── src/growthkit/             # Source code
│   ├── cli/                   # CLI commands
│   ├── constitution/          # Validation engine
│   └── research/              # Growth research modules
├── pyproject.toml
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── PROJECT_COMPLETION_SUMMARY.md
```

---

## 🔧 Prerequisites

- **Linux/macOS/Windows**
- [Supported](#-supported-ai-agents) AI coding agent
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Verify Your Setup

Ensure you have the required tools installed:

```bash
# Check uv installation
uv --version

# Check Python version
python --version

# Check Git installation
git --version
```

---

## 🌐 Creating Your Own Kit Variant

Growth Hacking Kit demonstrates how to adapt spec-driven methodology to any domain. Want to create a variant for product design, marketing, or business writing?

See [`refs/instructions.md`](./refs/instructions.md) for a comprehensive guide on:
- How to fork and adapt spec-kit for your domain
- How to define domain-specific principles
- How to create templates and reference materials
- How to enable multi-kit coexistence

**Example variants:**
- **`pd-kit`** - Product design and UX workflows
- **`marketing-kit`** - Content marketing and distribution
- **`writing-kit`** - Technical and business writing
- **`blog-kit`** - Blog content planning

All variants are published at [**kits.agentii.ai**](https://kits.agentii.ai).

---

## 🙏 Acknowledgements

Growth Hacking Kit is built on the excellent work of the [**Spec-Kit**](https://github.com/github/spec-kit) project from GitHub. We preserve 100% of Spec-Kit's architecture and infrastructure while adapting templates and methodology for growth campaign planning and execution.

**Spec-Kit Credits:**
- [Den Delimarsky](https://github.com/localden)
- [John Lam](https://github.com/jflam)

---

## 💬 Support

For issues, questions, or feedback:

- **GitHub Issues**: [Report on Growth Hacking Kit](https://github.com/agentii-ai/growth-hacking-kit/issues)
- **Spec-Kit Issues**: [Report on Spec-Kit](https://github.com/github/spec-kit/issues)
- **Kit Variants**: [Visit kits.agentii.ai](https://kits.agentii.ai)
- **Documentation**: [API Reference](./docs/API.md) | [Troubleshooting](./docs/TROUBLESHOOTING.md)

---

## 📄 License

This project is licensed under the terms of the MIT open source license. See [LICENSE](./LICENSE) for details.

**Note**: Growth Hacking Kit extends Spec-Kit's MIT license. For Spec-Kit license details, see [Spec-Kit LICENSE](https://github.com/github/spec-kit/blob/main/LICENSE).

---

## 🌟 Why Growth Hacking Kit?

### For Growth Teams & Founders:
- **Systematic**: Replace intuition-based growth with structured, hypothesis-driven campaigns
- **AI-Assisted**: Leverage AI agents for specification, planning, and execution
- **Validated**: Reference templates based on proven growth patterns from successful AI products
- **Evidence-Driven**: Focus on measurable metrics (k-factor, time-to-wow) and validation gates

### For the Open Source Community:
- **Reproducible**: Spec-driven workflows are more transparent and collaborative than ad-hoc processes
- **Extensible**: Growth Hacking Kit serves as a reference for creating domain-specific kit variants
- **Community-Friendly**: All templates and reference materials are open source and MIT-licensed
- **Professional**: Built on proven Spec-Kit infrastructure, adapted by experienced growth leaders

---

**Ready to systematize your growth with confidence?**

```bash
growthkit init my-product
```

Let's build sustainable growth through measurement, validation, and community amplification.

---
