"""Campaign plan command for Growth Hacking Kit."""

from datetime import datetime
from pathlib import Path
from typing import Any

import typer
from rich.console import Console

from growthkit.cli import config, utils
from growthkit.constitution.validator import ConstitutionValidator

console = Console()


def plan_command(
    description: str = typer.Argument(..., help="Campaign plan description or existing spec name"),
    force: bool = typer.Option(False, "--force", help="Force overwrite existing plan"),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging"),
) -> None:
    """
    Create an implementation plan from an approved specification.

    This command:
    1. Loads the approved specification
    2. Generates platform-specific tactics
    3. Creates GEO optimization research
    4. Generates supporting documents (research.md, data-model.md, quickstart.md)
    5. Validates against Constitution Check gates
    6. Updates agent context

    Example:
        growthkit plan "001-product-hunt-launch"
    """
    console.print("[bold cyan]Growth Hacking Kit[/bold cyan] - Creating implementation plan...")

    # Step 1: Load specification
    try:
        campaign_dir = utils.get_campaign_dir_from_branch(description)
        spec_file = campaign_dir / "spec.md"

        if not spec_file.exists():
            console.print(f"[red]✗[/red] Specification not found: {spec_file}")
            raise typer.Exit(1)

        spec_content = spec_file.read_text()
        console.print(f"[green]✓[/green] Specification loaded: {spec_file.parent.name}")

        if debug:
            console.print(f"[dim]Debug: Spec size: {len(spec_content)} chars[/dim]")

    except Exception as e:
        console.print(f"[red]✗[/red] Failed to load specification: {e}")
        raise typer.Exit(1)

    # Step 2: Extract key elements from spec
    validator = ConstitutionValidator()
    growth_type = validator.extract_growth_type(spec_content)
    viral_loop = validator.extract_viral_loop(spec_content)
    metrics = validator.extract_metrics(spec_content)

    console.print(f"[green]✓[/green] Growth type: {growth_type['primary_type']}")
    console.print(f"[green]✓[/green] Viral loop: {viral_loop['primary_loop']}")
    console.print(f"[green]✓[/green] Metrics defined: {metrics['defined_count']}")

    # Step 3: Generate plan from template
    plan_file = campaign_dir / "plan.md"

    if plan_file.exists() and not force:
        console.print(f"[yellow]⚠[/yellow] Plan already exists: {plan_file}")
        console.print("[yellow]Use --force to overwrite[/yellow]")
        raise typer.Exit(1)

    try:
        # Render plan template with campaign context
        context = {
            "CAMPAIGN_NAME": campaign_dir.name.split("-", 1)[1],
            "CAMPAIGN_BRANCH": campaign_dir.name,
            "GROWTH_TYPE": growth_type['primary_type'].title(),
            "VIRAL_LOOP": viral_loop['primary_loop'].title(),
            "METRICS": ", ".join([m for m, v in metrics['metrics'].items() if v['found']]),
            "DATE": datetime.now().strftime("%Y-%m-%d"),
            "KIT_NAME": config.KIT_NAME,
        }

        plan_template_path = Path(config.get_project_root()) / config.TEMPLATES_DIR / "plan-template.md"
        if not plan_template_path.exists():
            plan_template_path = Path(config.get_project_root()) / ".specify" / "templates" / "plan-template.md"

        if not plan_template_path.exists():
            console.print(f"[red]✗[/red] Plan template not found: {plan_template_path}")
            raise typer.Exit(1)

        plan_content = utils.render_template(plan_template_path, context)
        plan_file.write_text(plan_content)
        console.print(f"[green]✓[/green] Plan created: {plan_file}")

    except Exception as e:
        console.print(f"[red]✗[/red] Failed to generate plan: {e}")
        raise typer.Exit(1)

    # Step 4: Validate plan against Constitution Check
    validation_result = validator.validate_plan(campaign_dir.name)

    if validation_result["status"] == "PASS":
        console.print("[green]✓[/green] Constitution Check: PASS")
        passed = len(validation_result.get("mandatory_gates", {}).get("passed", []))
        console.print(f"  All {passed} mandatory gates passed")
    else:
        console.print("[yellow]⚠[/yellow] Constitution Check: Some gates failed")
        for failure in validation_result.get("mandatory_gates", {}).get("failed", []):
            console.print(f"  [{failure['gate_id']}] {failure['message']}")

    # Step 5: Create supporting documents
    try:
        # Create research.md
        research_file = campaign_dir / "research.md"
        research_content = _generate_research_document(
            campaign_dir.name, growth_type, viral_loop, metrics
        )
        research_file.write_text(research_content)
        console.print(f"[green]✓[/green] Research document created: {research_file}")

        # Create data-model.md
        data_model_file = campaign_dir / "data-model.md"
        data_model_content = _generate_data_model(campaign_dir.name)
        data_model_file.write_text(data_model_content)
        console.print(f"[green]✓[/green] Data model created: {data_model_file}")

        # Create quickstart.md
        quickstart_file = campaign_dir / "quickstart.md"
        quickstart_content = _generate_quickstart(campaign_dir.name)
        quickstart_file.write_text(quickstart_content)
        console.print(f"[green]✓[/green] Quickstart guide created: {quickstart_file}")

    except Exception as e:
        console.print(f"[yellow]⚠[/yellow] Some supporting documents failed: {e}")

    # Step 6: Summary and next steps
    console.print("\n[bold green]Implementation plan created![/bold green]\n")
    console.print(f"Campaign:  {campaign_dir.name}")
    console.print(f"Plan file: {plan_file}")
    console.print(f"Research:  {research_file if research_file.exists() else 'N/A'}")
    console.print(f"Data model: {data_model_file if data_model_file.exists() else 'N/A'}")
    console.print("\nNext steps:")
    console.print("  1. Review the plan.md for platform tactics")
    console.print("  2. Check GEO optimization strategy in research.md")
    console.print("  3. Run /growthkit.tasks to generate task breakdown")
    console.print("  4. Review data-model.md for schema reference")


def _generate_research_document(
    campaign_name: str, growth_type: dict[str, Any], viral_loop: dict[str, Any], metrics: dict[str, Any]
) -> str:
    """Generate GEO optimization research document."""
    return f"""# Research & GEO Strategy: {campaign_name}

## Platform Analysis

### Primary Platforms

| Platform | Format | Aspect Ratio | Strategy |
|----------|--------|-------------|----------|
| X/Twitter | Short video + text | 16:9 | Thread + video showcase |
| TikTok | Short video | 9:16 | Quick demo, viral hooks |
| LinkedIn | Case study | 1:1 | Professional showcase |
| GitHub | Code + README | - | Integration example |
| Product Hunt | Full demo | 16:9 | Product narrative |

## Viral Loop: {viral_loop['primary_loop'].title()}

**Description**: Campaign activates {viral_loop['primary_loop']} viral loop mechanics

**Mechanics**:
- User discovers content on primary platform
- User shares or integrates with network
- Network exposure drives organic growth

## Growth Type: {growth_type['primary_type'].title()} Growth

**Characteristics**:
- Type: {growth_type['primary_type']}
- Metrics tracked: {metrics.get('metrics', {}).get('k_factor', {}).get('value', '1.0+')} k-factor target
- Time-to-wow: <5 minutes

## GEO Optimization (Answer Density)

### Answer Density Strategy

1. **Structured Data**
   - Use tables for comparisons and benchmarks
   - Include specific metrics and numbers
   - Document platform-specific specs

2. **Citation Signals**
   - Reference growth metrics from research
   - Document platform APIs and specifications
   - Include measurable success criteria

3. **Content Organization**
   - Clear hierarchical structure
   - Specific examples over generalities
   - Quantified success criteria

## Metrics Dashboard

- **Primary Metric**: {metrics['metrics'].get('k_factor', {}).get('value', 'TBD')} k-factor
- **Time-to-Wow**: <5 minutes
- **NRR Target**: 106%+
- **Engagement Rate**: {metrics['metrics'].get('engagement_rate', {}).get('value', 'TBD')}%

## Next Steps

1. Validate platform strategy
2. Create platform-specific content calendars
3. Set up tracking for viral metrics
4. Plan pilot phase rollout

---

**Created**: {datetime.now().strftime('%Y-%m-%d')}
**Status**: Research Phase Complete
"""


def _generate_data_model(campaign_name: str) -> str:
    """Generate data model reference document."""
    return f"""# Data Model: {campaign_name}

## Core Entities

### Campaign
```yaml
Campaign:
  id: string (###-name format)
  name: string
  description: string
  created_at: timestamp
  growth_type: enum(Vibe|Trust|Agentic)
  viral_loop: enum(Remix|Integration|Watermark)
  pilot_budget: float
  scale_budget: float
```

### Constitution
```yaml
Constitution:
  version: string
  principles: list[Principle]
  mandatory_gates: list[MandatoryGate]
  advisory_gates: list[AdvisoryGate]
```

### PlatformTactic
```yaml
PlatformTactic:
  platform: enum(Twitter|TikTok|LinkedIn|GitHub|ProductHunt)
  format: string
  duration: string (e.g., "30-60s")
  aspect_ratio: string (e.g., "16:9")
  viral_mechanism: string
```

### ViralLoop
```yaml
ViralLoop:
  type: enum(Remix|Integration|Watermark)
  trigger: string
  amplification: string
  network_effect: string
```

### PilotPhase
```yaml
PilotPhase:
  start_date: date
  duration_days: integer
  budget: float (max 10% of scale_budget)
  target_audience: string
  success_criteria: list[string]
  go_no_go_date: date
```

### GrowthMetricsDashboard
```yaml
GrowthMetricsDashboard:
  k_factor: float (min 1.1)
  time_to_wow: integer (max 300 seconds)
  nrr: float (min 106%)
  engagement_rate: float
  activation_metric: string
  churn_rate: float
```

### Retrospective
```yaml
Retrospective:
  campaign_id: string
  pilot_results: dict
  learnings: list[string]
  pivot_decisions: list[string]
  scale_recommendations: list[string]
  community_feedback: list[string]
```

## Relationships

- Campaign contains PlatformTactics (1:N)
- Campaign has ViralLoop (1:1)
- Campaign has PilotPhase (1:1)
- Campaign has GrowthMetricsDashboard (1:1)
- Campaign has Retrospective (0:1)

---

**Created**: {datetime.now().strftime('%Y-%m-%d')}
**Status**: Reference Document
"""


def _generate_quickstart(campaign_name: str) -> str:
    """Generate quickstart guide."""
    return f"""# Quickstart Guide: {campaign_name}

## Installation

### Prerequisites
- Git installed and configured
- Python 3.11+
- uv package manager (recommended)

### Install Growth Hacking Kit

```bash
uv tool install growthkit-cli
```

Or with pip:
```bash
pip install growthkit-cli
```

## First Campaign Setup

### 1. Initialize Project
```bash
mkdir my-growth-campaign
cd my-growth-campaign
growthkit init my-project --ai claude
```

### 2. Create Campaign Specification
```bash
growthkit specify "Launch Product Hunt campaign with demo video"
```

Review the generated `specs/001-campaign-name/spec.md` and ensure:
- [ ] Growth type is identified
- [ ] Target audience is specific
- [ ] Viral loop mechanism is clear
- [ ] Metrics are measurable

### 3. Create Implementation Plan
```bash
growthkit plan 001-campaign-name
```

Review the generated `plan.md` for:
- Platform-specific tactics
- GEO optimization strategy
- Pilot scope definition
- Complexity tracking

### 4. Generate Task Breakdown
```bash
growthkit tasks 001-campaign-name
```

Review `tasks.md` for:
- Phase-based task organization
- Parallel opportunities [P]
- Checkpoint validations
- Dependency ordering

### 5. Execute Campaign
```bash
growthkit implement 001-campaign-name
```

Follow the guided execution:
- Checkpoint validations
- Pilot phase management
- Scale decisions
- Results measurement

## Agent Integration

When in the project directory with an AI agent:

```
/growthkit.constitution   # Establish principles
/growthkit.specify        # Create specifications
/growthkit.plan          # Plan implementation
/growthkit.tasks         # Generate task breakdown
/growthkit.implement     # Execute campaign
```

## Key Concepts

### Three Growth Types
- **Vibe Growth**: Community-driven, organic viral spread
- **Trust Growth**: Authority-driven, proven use cases
- **Agentic Growth**: AI-powered, automated expansion

### Three Viral Loops
- **Remix Loop**: Users adapt and share variations
- **Integration Loop**: Users integrate with their networks
- **Watermark Loop**: Branding embedded in shared content

### Constitution Check
Validates campaigns against Seven Core Principles:
1. Spec-Driven: Detailed specifications before implementation
2. Viral Loops: Built-in growth mechanics
3. Agent-First: AI agents as primary interface
4. Metrics: Measurable outcomes tracked
5. Multi-Platform: Organic reach on 5+ platforms
6. Test-Before-Scale: Pilot validation gates
7. Community-Led: User feedback drives decisions

## Performance Targets

- **Spec Generation**: <5 seconds
- **Plan Generation**: <10 seconds
- **Task Breakdown**: <10 seconds
- **Constitution Check**: <1 second

## Troubleshooting

### Spec Not Found
Ensure the campaign directory exists in `specs/###-campaign-name/spec.md`

### Constitution Check Failures
Review the mandatory gates in `research.md` and address requirements

### Agent Commands Not Available
Ensure AI agent is in the project directory and has access to `.growthkit/templates/commands/`

## Support

For issues and questions:
- GitHub: https://github.com/agentii/growth-hacking-kit
- Discussions: https://github.com/agentii/growth-hacking-kit/discussions

---

**Created**: {datetime.now().strftime('%Y-%m-%d')}
**Status**: Ready to Use
"""
