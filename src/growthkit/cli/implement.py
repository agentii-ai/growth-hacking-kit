"""Campaign implementation command for Growth Hacking Kit."""

import re
from datetime import datetime
from typing import Any

import typer
from rich.console import Console

from growthkit.cli import utils

console = Console()


def implement_command(
    description: str = typer.Argument(..., help="Campaign name or task list"),
    force: bool = typer.Option(False, "--force", help="Skip checkpoint confirmations"),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging"),
) -> None:
    """
    Execute campaign tasks with checkpoint validations.

    This command:
    1. Loads task breakdown (tasks.md)
    2. Guides execution through Setup → Pilot → Scale → Measure phases
    3. Validates checkpoints before proceeding
    4. Tracks execution progress
    5. Generates retrospective report

    Example:
        growthkit implement "001-product-hunt-launch"
    """
    console.print("[bold cyan]Growth Hacking Kit[/bold cyan] - Starting campaign execution...\n")

    # Step 1: Load tasks
    try:
        campaign_dir = utils.get_campaign_dir_from_branch(description)
        tasks_file = campaign_dir / "tasks.md"

        if not tasks_file.exists():
            console.print(f"[red]✗[/red] Tasks file not found: {tasks_file}")
            console.print("[yellow]Run /growthkit.tasks first to generate task breakdown[/yellow]")
            raise typer.Exit(1)

        tasks_content = tasks_file.read_text()
        console.print(f"[green]✓[/green] Tasks loaded: {tasks_file.parent.name}")

        # Parse phases
        phases = _parse_execution_phases(tasks_content)
        console.print(f"[green]✓[/green] Identified {len(phases)} execution phases\n")

        if debug:
            console.print(f"[dim]Debug: Tasks size: {len(tasks_content)} chars[/dim]")
            console.print(f"[dim]Debug: Phases: {phases}[/dim]\n")

    except Exception as e:
        console.print(f"[red]✗[/red] Failed to load tasks: {e}")
        raise typer.Exit(1)

    # Step 2: Guide through execution phases
    execution_log = []

    for phase_num, phase in enumerate(phases, 1):
        console.print(f"\n[bold cyan]Phase {phase_num}: {phase}[/bold cyan]")
        console.print("=" * 50)

        # Extract tasks for this phase
        phase_tasks = _extract_phase_tasks(tasks_content, phase)
        console.print(f"Tasks in this phase: {len(phase_tasks)}\n")

        # Log phase start
        execution_log.append(
            {
                "phase": phase,
                "timestamp": datetime.now().isoformat(),
                "status": "started",
            }
        )

        # Checkpoint before major phases
        if phase in ["Pilot", "Scale", "Measure"]:
            should_proceed = _confirm_phase_start(phase, force)
            if not should_proceed:
                console.print(f"[yellow]⚠[/yellow] Skipping {phase} phase")
                execution_log[-1]["status"] = "skipped"
                continue

        # Execute phase tasks
        for task in phase_tasks:
            task_id = task.get("id", "")
            task_desc = task.get("description", "")

            if "[CP]" in task_desc:
                # Checkpoint task
                console.print(f"\n[bold yellow]Checkpoint: {task_desc}[/bold yellow]")
                checkpoint_ok = _validate_checkpoint(task_desc, force)
                if not checkpoint_ok:
                    console.print("[red]✗[/red] Checkpoint failed. Halting execution.")
                    execution_log[-1]["status"] = "failed_checkpoint"
                    raise typer.Exit(1)
                console.print("[green]✓[/green] Checkpoint passed")
            else:
                # Regular task
                is_parallel = "[P]" in task_desc
                marker = "[P]" if is_parallel else ""
                console.print(f"  {marker} {task_id}: {task_desc}")

        console.print(f"\n[green]✓[/green] {phase} phase complete")
        execution_log[-1]["status"] = "complete"

    # Step 3: Generate retrospective
    try:
        console.print("\n[bold cyan]Step 3: Generating Retrospective[/bold cyan]")
        retrospective_file = campaign_dir / "retrospective.md"
        retrospective_content = _generate_retrospective(campaign_dir.name, phases, execution_log)
        retrospective_file.write_text(retrospective_content)
        console.print(f"[green]✓[/green] Retrospective created: {retrospective_file}")

    except Exception as e:
        console.print(f"[yellow]⚠[/yellow] Failed to generate retrospective: {e}")

    # Step 4: Summary
    console.print("\n[bold green]Campaign execution complete![/bold green]\n")
    console.print(f"Campaign:        {campaign_dir.name}")
    console.print(f"Phases completed: {len(phases)}")
    console.print(
        f"Retrospective:    {retrospective_file if retrospective_file.exists() else 'N/A'}"
    )
    console.print("\nNext steps:")
    console.print("  1. Review retrospective.md for learnings")
    console.print("  2. Analyze success metrics")
    console.print("  3. Plan next growth phase")
    console.print("  4. Share results with team")


def _parse_execution_phases(tasks_content: str) -> list[str]:
    """Extract phase sections from tasks.md."""
    phases = []

    section_pattern = r"^## Phase \d+: (\w+)"
    for match in re.finditer(section_pattern, tasks_content, re.MULTILINE):
        phase_name = match.group(1)
        if phase_name not in phases:
            phases.append(phase_name)

    # Ensure standard order
    standard_order = ["Setup", "Pilot", "Scale", "Measure"]
    return [p for p in standard_order if p in phases]


def _extract_phase_tasks(tasks_content: str, phase: str) -> list[dict[str, Any]]:
    """Extract tasks for a specific phase."""
    tasks: list[dict[str, Any]] = []

    # Find phase section
    phase_pattern = rf"^## Phase \d+: {phase}.*?(?=^## Phase|\Z)"
    phase_match = re.search(phase_pattern, tasks_content, re.MULTILINE | re.DOTALL)

    if not phase_match:
        return tasks

    phase_section = phase_match.group(0)

    # Extract tasks from this section
    task_pattern = r"- \[ \] (T\d+)\s*(.*?)$"
    for match in re.finditer(task_pattern, phase_section, re.MULTILINE):
        task_id = match.group(1)
        task_desc = match.group(2).strip()

        tasks.append(
            {
                "id": task_id,
                "description": task_desc,
                "completed": False,
            }
        )

    return tasks


def _confirm_phase_start(phase: str, force: bool) -> bool:
    """Confirm before starting major phase."""
    if force:
        return True

    console.print(f"\n[bold yellow]Ready to start {phase} phase?[/bold yellow]")
    console.print("Review the phase tasks above before proceeding.\n")

    response = typer.prompt("Continue? (yes/no)", default="yes")
    return response.lower() in ["yes", "y"]


def _validate_checkpoint(checkpoint_desc: str, force: bool) -> bool:
    """Validate checkpoint conditions."""
    if force:
        console.print("[yellow]Skipping checkpoint validation (--force)[/yellow]")
        return True

    console.print("\nValidate checkpoint conditions:")
    console.print("  - All preceding tasks are complete")
    console.print("  - All metrics within expected ranges")
    console.print("  - No blockers identified")

    response = typer.prompt("\nCheckpoint validated? (yes/no)", default="yes")
    return response.lower() in ["yes", "y"]


def _generate_retrospective(
    campaign_name: str, phases: list[str], execution_log: list[dict[str, Any]]
) -> str:
    """Generate campaign retrospective report."""

    return f"""# Campaign Retrospective: {campaign_name}

**Campaign**: {campaign_name}
**Execution Date**: {datetime.now().strftime('%Y-%m-%d')}
**Status**: Complete

## Executive Summary

This retrospective documents the Growth Hacking Kit campaign execution, including
phases completed, metrics achieved, and key learnings for future growth initiatives.

## Phases Executed

| Phase | Status | Insights |
|-------|--------|----------|
| Setup | Complete | Infrastructure and assets prepared |
| Pilot | Complete | Viral mechanics validated with limited audience |
| Scale | Complete | Full rollout across platforms |
| Measure | Complete | Final metrics aggregated and analyzed |

## Key Metrics

### Growth Metrics
- **K-Factor**: [Insert value] (Target: >1.1)
- **Time-to-Wow**: [Insert minutes] (Target: <5 min)
- **NRR**: [Insert %] (Target: >106%)

### Engagement
- **Primary Activation**: [Insert %]
- **Community Sentiment**: [Insert positive %]
- **Churn Rate**: [Insert %]

## Phase Insights

### Setup Phase
**What went well**:
- [ ] Content assets created on schedule
- [ ] Platform credentials verified
- [ ] Analytics tracking configured

**Challenges**:
- [ ] [Document any blockers]

### Pilot Phase
**What went well**:
- [ ] Viral mechanics performed better than expected
- [ ] Community engagement was strong
- [ ] Go/no-go decision made with confidence

**Challenges**:
- [ ] [Document any issues]

**Go/No-Go Decision**: GO (Proceed to Scale)

### Scale Phase
**What went well**:
- [ ] Multi-platform launch executed smoothly
- [ ] [P] Parallel tasks completed on time
- [ ] Algorithm optimization drove engagement

**Challenges**:
- [ ] [Document any scaling issues]

### Measure Phase
**What went well**:
- [ ] All metrics captured successfully
- [ ] Community learnings documented
- [ ] Retrospective process smooth

## Community Feedback

### Primary Themes
1. **Viral Loop Effectiveness**: [Describe community reactions to viral mechanics]
2. **Content Quality**: [Assess sentiment toward content]
3. **Platform-Specific**: [Note platform-specific feedback]

### User Testimonials
> [Add 1-2 representative user quotes]

## Technical Insights

### Platform Performance

| Platform | Reach | Engagement | RTW |
|----------|-------|-----------|-----|
| X/Twitter | [Count] | [%] | [Time] |
| TikTok | [Count] | [%] | [Time] |
| LinkedIn | [Count] | [%] | [Time] |
| GitHub | [Count] | [%] | [Time] |
| Product Hunt | [Count] | [%] | [Time] |

### Algorithm Wins
- [Document algorithm optimization successes]
- [Note content variations that performed best]

## Pivot Decisions

During execution, the following pivots were made:

1. **Pivot 1**: [Decision made, Reason, Results]
2. **Pivot 2**: [Decision made, Reason, Results]

## Constitution Learning

### Principles Validated
- [Principle]: [How it showed value in this campaign]

### Principle Evolution
- [Principle]: [Suggested updates based on learnings]

## Scale Recommendations

### For Next Growth Phase
1. **Platform Strategy**
   - Invest in [Platform]: [Reason]
   - De-emphasize [Platform]: [Reason]

2. **Viral Loop**
   - [Loop Type] was most effective
   - Consider [New Loop Type] for next phase

3. **Content Strategy**
   - [Content type] resonates most
   - [Content type] needs iteration

4. **Metrics to Track**
   - Add [Metric]: [Reason]
   - Reduce focus on [Metric]: [Reason]

### Budget Optimization
- Pilot Phase spent: [%] vs budget [%]
- Scale Phase spent: [%] vs budget [%]
- Recommendation: Allocate [%] to next phase

## Team Learnings

### What We Learned
- [Team learning 1]
- [Team learning 2]
- [Team learning 3]

### Process Improvements
- For next campaign: [Process improvement]
- Tooling needed: [Tool or automation]

## Next Growth Phase

### Recommendation
Based on this retrospective, the team recommends [Next Growth Phase]:
- Focus: [Growth area]
- Timeline: [Proposed timeline]
- Budget: [Proposed budget allocation]
- Team: [Team composition]

### Roadmap
```
This Campaign → Next Phase → Beyond
[Growth metrics] → [Projected growth] → [Long-term goals]
```

## Appendix

### Detailed Metrics
[Link to detailed analytics]

### Community Feedback Log
[Link to feedback compilation]

### Asset Archive
[Link to campaign assets]

---

**Campaign Status**: ✅ Complete
**Retrospective Status**: Ready for Review
**Next Steps**: Present findings to stakeholder team

**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}
**Conducted by**: Growth Hacking Kit
"""
