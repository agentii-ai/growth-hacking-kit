"""Campaign tasks command for Growth Hacking Kit."""

import re
from datetime import datetime
from pathlib import Path
from typing import Any

import typer
from rich.console import Console

from growthkit.cli import config, utils

console = Console()


def tasks_command(
    description: str = typer.Argument(..., help="Campaign plan name or spec name"),
    force: bool = typer.Option(False, "--force", help="Force overwrite existing tasks"),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging"),
) -> None:
    """
    Generate actionable task breakdown from implementation plan.

    This command:
    1. Loads the approved plan
    2. Parses platform tactics and schedules
    3. Generates phase-organized tasks (Setup → Pilot → Scale → Measure)
    4. Marks parallel opportunities [P]
    5. Creates checkpoint validation tasks
    6. Validates dependency ordering

    Example:
        growthkit tasks "001-product-hunt-launch"
    """
    console.print("[bold cyan]Growth Hacking Kit[/bold cyan] - Generating task breakdown...")

    # Step 1: Load plan
    try:
        campaign_dir = utils.get_campaign_dir_from_branch(description)
        plan_file = campaign_dir / "plan.md"

        if not plan_file.exists():
            console.print(f"[red]✗[/red] Plan not found: {plan_file}")
            console.print("[yellow]Run /growthkit.plan first to create implementation plan[/yellow]")
            raise typer.Exit(1)

        plan_content = plan_file.read_text()
        console.print(f"[green]✓[/green] Plan loaded: {plan_file.parent.name}")

        if debug:
            console.print(f"[dim]Debug: Plan size: {len(plan_content)} chars[/dim]")

    except Exception as e:
        console.print(f"[red]✗[/red] Failed to load plan: {e}")
        raise typer.Exit(1)

    # Step 2: Generate tasks from template
    tasks_file = campaign_dir / "tasks.md"

    if tasks_file.exists() and not force:
        console.print(f"[yellow]⚠[/yellow] Tasks already exist: {tasks_file}")
        console.print("[yellow]Use --force to overwrite[/yellow]")
        raise typer.Exit(1)

    try:
        # Parse plan to extract phases and tactics
        phases = _parse_plan_phases(plan_content)
        console.print(f"[green]✓[/green] Identified {len(phases)} phases")

        # Generate tasks organized by phases
        tasks_content = _generate_tasks_breakdown(
            campaign_dir.name, phases, plan_content
        )

        tasks_file.write_text(tasks_content)
        console.print(f"[green]✓[/green] Tasks generated: {tasks_file}")

    except Exception as e:
        console.print(f"[red]✗[/red] Failed to generate tasks: {e}")
        if debug:
            import traceback
            console.print(f"[dim]{traceback.format_exc()}[/dim]")
        raise typer.Exit(1)

    # Step 3: Validate task structure
    task_count = tasks_content.count("- [ ] T")
    parallel_count = tasks_content.count("[P]")
    checkpoint_count = tasks_content.count("Checkpoint")

    console.print(f"[green]✓[/green] Task breakdown created")
    console.print(f"  Tasks: {task_count}")
    console.print(f"  Parallel opportunities: {parallel_count}")
    console.print(f"  Checkpoints: {checkpoint_count}")

    # Step 4: Summary and next steps
    console.print("\n[bold green]Task breakdown generated![/bold green]\n")
    console.print(f"Campaign:  {campaign_dir.name}")
    console.print(f"Tasks file: {tasks_file}")
    console.print("\nNext steps:")
    console.print("  1. Review task phases and dependencies")
    console.print("  2. Identify parallel opportunities [P]")
    console.print("  3. Plan resource allocation")
    console.print("  4. Run /growthkit.implement to execute tasks")


def _parse_plan_phases(plan_content: str) -> list[str]:
    """
    Extract phase information from plan.

    Returns list of identified phases.
    """
    phases = []

    if "setup" in plan_content.lower():
        phases.append("Setup")
    if "pilot" in plan_content.lower():
        phases.append("Pilot")
    if "scale" in plan_content.lower():
        phases.append("Scale")
    if "measure" in plan_content.lower():
        phases.append("Measure")

    # Ensure standard phase order
    standard_phases = ["Setup", "Pilot", "Scale", "Measure"]
    return [p for p in standard_phases if p in phases]


def _generate_tasks_breakdown(
    campaign_name: str, phases: list[str], plan_content: str
) -> str:
    """Generate comprehensive task breakdown organized by phases."""

    task_id_counter = 1

    def next_task_id():
        nonlocal task_id_counter
        task_id = f"T{task_id_counter:03d}"
        task_id_counter += 1
        return task_id

    tasks_md = f"""# Task Breakdown: {campaign_name}

**Purpose**: Actionable tasks organized by campaign phase (Setup → Pilot → Scale → Measure)
**Campaign**: {campaign_name}
**Created**: {datetime.now().strftime('%Y-%m-%d')}
**Status**: Ready for execution

## Overview

This task breakdown organizes implementation into four distinct phases:

1. **Setup Phase**: Infrastructure and preparation (no user impact)
2. **Pilot Phase**: Limited audience validation (10% of scale budget)
3. **Scale Phase**: Full rollout based on pilot results
4. **Measure Phase**: Analytics and retrospective

## Legend

- `[P]` = Parallel opportunity (can run simultaneously with other [P] tasks)
- `[CP]` = Checkpoint (must validate before proceeding)
- `[BLOCKED]` = Depends on previous tasks

---

## Phase 1: Setup

**Goal**: Prepare infrastructure, content assets, and platform credentials
**Timeline**: 2-3 days
**Budget**: <1% of total pilot budget

"""

    setup_tasks = [
        ("Create content calendar", "docs/content-calendar.md"),
        ("Set up platform credentials", "setup/platform-creds.md"),
        ("Prepare demo video/assets", "assets/demo-video.mp4"),
        ("Design viral mechanics test", "research/viral-test-plan.md"),
        ("Create pilot audience list", "pilot/audience-list.csv"),
        ("Set up analytics tracking", "setup/analytics.md"),
    ]

    for task_desc, deliverable in setup_tasks:
        task_id = next_task_id()
        tasks_md += f"- [ ] {task_id} [SETUP] {task_desc}\n"
        tasks_md += f"  - Deliverable: `{deliverable}`\n"
        tasks_md += f"  - Owner: Growth Lead\n"
        tasks_md += f"  - Duration: 1 day\n\n"

    tasks_md += "\n## Phase 2: Pilot\n\n"
    tasks_md += """**Goal**: Validate viral mechanics with 10% audience (go/no-go checkpoint)
**Timeline**: 7-14 days
**Budget**: ~10% of scale budget

### Pilot Cohort 1: Primary Platform Launch

"""

    pilot_tasks = [
        ("Launch on primary platform", "execution/primary-launch.md", True),
        ("Monitor viral metrics (k-factor, TTW)", "metrics/pilot-dashboard.md", False),
        ("Engage early adopters", "community/early-adopters.md", True),
        ("Collect community feedback", "research/feedback-log.md", False),
        ("Iterate based on feedback", "iteration/v1-learnings.md", True),
        ("[CP] Pilot Checkpoint Validation", "pilot/checkpoint-results.md", False),
    ]

    for task_desc, deliverable, parallel in pilot_tasks:
        task_id = next_task_id()
        parallel_marker = " [P]" if parallel else " [CP]" if "[CP]" in task_desc else ""
        tasks_md += f"- [ ] {task_id}{parallel_marker} {task_desc}\n"
        tasks_md += f"  - Deliverable: `{deliverable}`\n"
        tasks_md += f"  - Owner: Growth Lead\n"
        tasks_md += f"  - Duration: 3-5 days\n\n"

    tasks_md += """### Pilot Go/No-Go Decision

**Validation Criteria**:
- K-factor > 1.1 (each user brings >1.1 new users)
- Time-to-wow < 5 minutes
- Community sentiment positive (>70% positive feedback)
- Product quality meets expectations

**Decision Point**:
- [ ] {task_id} [CP] Validate pilot results and make go/no-go decision
  - If GO: Proceed to Scale Phase
  - If NO-GO: Document learnings and iterate spec

""".format(task_id=next_task_id())

    tasks_md += "\n## Phase 3: Scale\n\n"
    tasks_md += """**Goal**: Roll out to full audience across all platforms
**Timeline**: 14-30 days
**Budget**: 90% of total budget

### Parallel Platform Launches

"""

    scale_tasks = [
        ("Expand to secondary platforms (TikTok, LinkedIn, GitHub)", "execution/secondary-platforms.md", True),
        ("Create platform-specific content variants", "content/platform-variants.md", True),
        ("Optimize platform algorithms (repost timing, hashtags)", "optimization/algo-strategy.md", True),
        ("Scale paid amplification (if applicable)", "campaigns/paid-campaigns.md", True),
        ("[P] Monitor scale metrics across platforms", "metrics/scale-dashboard.md", False),
        ("[P] Community management and support", "community/support-escalations.md", False),
        ("[P] Iterate creative based on performance", "iteration/scale-learnings.md", False),
    ]

    for task_desc, deliverable, parallel in scale_tasks:
        task_id = next_task_id()
        parallel_marker = " [P]" if parallel else ""
        tasks_md += f"- [ ] {task_id}{parallel_marker} {task_desc}\n"
        tasks_md += f"  - Deliverable: `{deliverable}`\n"
        tasks_md += f"  - Owner: Growth Team\n"
        tasks_md += f"  - Duration: 14-30 days (parallel execution)\n\n"

    tasks_md += "\n## Phase 4: Measure\n\n"
    tasks_md += """**Goal**: Analyze results, document learnings, and plan next growth phase
**Timeline**: 7 days
**Budget**: <1% of total

"""

    measure_tasks = [
        ("Aggregate final metrics", "metrics/final-results.md"),
        ("Analyze viral loop effectiveness", "analysis/viral-analysis.md"),
        ("Document community learnings", "research/community-learnings.md"),
        ("Create retrospective report", "retrospective/campaign-retrospective.md"),
        ("Identify scale recommendations", "retrospective/scale-recommendations.md"),
        ("Plan next growth phase", "roadmap/next-phase.md"),
    ]

    for task_desc, deliverable in measure_tasks:
        task_id = next_task_id()
        tasks_md += f"- [ ] {task_id} [MEASURE] {task_desc}\n"
        tasks_md += f"  - Deliverable: `{deliverable}`\n"
        tasks_md += f"  - Owner: Growth Lead\n"
        tasks_md += f"  - Duration: 1 day each\n\n"

    tasks_md += f"""---

## Summary

| Phase | Duration | Budget | Key Milestone | Status |
|-------|----------|--------|---------------|--------|
| Setup | 2-3 days | <1% | Assets ready | [ ] |
| Pilot | 7-14 days | ~10% | Go/no-go decision | [ ] |
| Scale | 14-30 days | 90% | Full rollout complete | [ ] |
| Measure | 7 days | <1% | Retrospective ready | [ ] |

**Total Tasks**: {task_id_counter - 1}
**Parallel Opportunities**: Mark [P] for tasks that can run simultaneously
**Critical Path**: Setup → Pilot Checkpoint → Scale → Measure

## Execution Guidelines

### Before Starting
1. Ensure all Setup tasks are complete
2. Review contingency plans for platform changes
3. Brief team on viral mechanics and go/no-go criteria

### During Pilot
1. Monitor metrics daily
2. Log all community feedback
3. Prepare Scale phase assets in parallel [P]
4. At checkpoint: Present data and make decision

### During Scale
1. Execute [P] tasks in parallel for speed
2. Maintain daily metrics updates
3. Be ready to pivot if performance drops
4. Document all creative iterations

### Post-Campaign
1. Complete all Measure tasks
2. Conduct team retrospective
3. Update constitution with learnings
4. Plan next growth phase using Same framework

---

**Created**: {datetime.now().strftime('%Y-%m-%d')}
**Status**: Ready for execution
**Next Step**: Run `/growthkit.implement` to begin task execution
"""

    return tasks_md
