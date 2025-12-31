"""Campaign specification command for Growth Hacking Kit."""

from pathlib import Path

import typer
from rich.console import Console

from growthkit.cli import config, utils
from growthkit.constitution.validator import ConstitutionValidator

console = Console()


def specify_command(
    description: str = typer.Argument(..., help="Campaign description"),
    force: bool = typer.Option(False, "--force", help="Force overwrite existing spec"),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging"),
) -> None:
    """
    Create a growth campaign specification from natural language description.

    This command:
    1. Extracts campaign name from description
    2. Creates/checks campaign branch
    3. Generates spec.md from template
    4. Validates against Constitution Check gates
    5. Creates quality checklist

    Example:
        growthkit specify "Launch Product Hunt campaign with demo video"
    """
    console.print("[bold cyan]Growth Hacking Kit[/bold cyan] - Creating campaign specification...")

    # Step 1: Extract campaign name and number
    campaign_name = utils.extract_campaign_name(description)
    campaign_number = utils.get_next_campaign_number()
    branch_name = f"{campaign_number:03d}-{campaign_name}"

    console.print(f"[green]✓[/green] Campaign: {branch_name}")

    if debug:
        console.print(f"[dim]Debug: Description: {description[:50]}...[/dim]")
        console.print(f"[dim]Debug: Extracted name: {campaign_name}[/dim]")

    # Step 2: Create campaign branch and directory
    try:
        created_branch = utils.create_campaign_branch(campaign_number, campaign_name)
        campaign_dir = utils.create_campaign_directory(campaign_number, campaign_name)
        console.print(f"[green]✓[/green] Branch created: {created_branch}")
        console.print(f"[green]✓[/green] Directory created: {campaign_dir}")
    except Exception as e:
        console.print(f"[red]✗[/red] Failed to create branch: {e}")
        raise typer.Exit(1)

    # Step 3: Generate spec from template
    spec_file = campaign_dir / "spec.md"

    if spec_file.exists() and not force:
        console.print(f"[yellow]⚠[/yellow] Spec already exists: {spec_file}")
        console.print("[yellow]Use --force to overwrite[/yellow]")
        raise typer.Exit(1)

    # Render spec template with campaign context
    context = {
        "FEATURE_NAME": campaign_name.replace("-", " ").title(),
        "FEATURE_BRANCH": branch_name,
        "CAMPAIGN_DESCRIPTION": description,
        "CAMPAIGN_NAME": campaign_name,
        "CAMPAIGN_NUMBER": campaign_number,
        "DATE": Path(spec_file).stat().st_ctime if spec_file.exists() else "",
        "KIT_NAME": config.KIT_NAME,
    }

    try:
        # Read template from .growthkit/templates/
        spec_template_path = Path(config.get_project_root()) / config.TEMPLATES_DIR / "spec-template.md"

        if not spec_template_path.exists():
            # Fallback: use spec from .specify if available
            spec_template_path = Path(config.get_project_root()) / ".specify" / "templates" / "spec-template.md"

        if not spec_template_path.exists():
            console.print(f"[red]✗[/red] Spec template not found: {spec_template_path}")
            raise typer.Exit(1)

        spec_content = utils.render_template(spec_template_path, context)
        spec_file.write_text(spec_content)
        console.print(f"[green]✓[/green] Spec created: {spec_file}")
    except Exception as e:
        console.print(f"[red]✗[/red] Failed to generate spec: {e}")
        raise typer.Exit(1)

    # Step 4: Run Constitution Check
    validator = ConstitutionValidator()
    validation_result = validator.validate_spec(branch_name)

    if validation_result["status"] == "PASS":
        console.print("[green]✓[/green] Constitution Check: PASS")
        passed_count = len(validation_result.get("passed_gates", []))
        console.print(f"  All {passed_count} mandatory gates passed")
    else:
        console.print("[yellow]⚠[/yellow] Constitution Check: Some gates failed")
        for failure in validation_result.get("failed_gates", []):
            console.print(f"  [{failure['gate_id']}] {failure['message']}")

    # Check for clarification markers
    clarification_result = validator.count_clarification_markers(branch_name)
    if clarification_result["status"] == "PASS":
        console.print(f"[green]✓[/green] Clarification markers: {clarification_result['count']}/{clarification_result['max_allowed']}")
    else:
        console.print(f"[yellow]⚠[/yellow] Too many clarification markers: {clarification_result['count']}/{clarification_result['max_allowed']}")
        console.print("  Please review and clarify remaining items")

    # Step 5: Create quality checklist
    checklist_file = campaign_dir / "checklists" / "requirements.md"
    checklist_content = _generate_quality_checklist(campaign_name, branch_name)
    checklist_file.write_text(checklist_content)
    console.print(f"[green]✓[/green] Quality checklist created: {checklist_file}")

    # Step 6: Summary and next steps
    console.print("\n[bold green]Campaign specification created![/bold green]\n")
    console.print(f"Campaign:  {branch_name}")
    console.print(f"Spec file: {spec_file}")
    console.print(f"Checklist: {checklist_file}")
    console.print("\nNext steps:")
    console.print("  1. Review the spec.md for completeness")
    console.print("  2. Address any Constitution Check warnings")
    console.print("  3. Run /growthkit.plan to create implementation plan")


def _generate_quality_checklist(campaign_name: str, branch_name: str) -> str:
    """Generate spec quality checklist."""
    return f"""# Specification Quality Checklist: {campaign_name.replace('-', ' ').title()}

**Purpose**: Validate specification completeness and quality before proceeding to planning
**Campaign**: {branch_name}
**Created**: [DATE]

## Content Quality

- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and growth outcomes
- [ ] Written for non-technical stakeholders
- [ ] All mandatory sections completed
- [ ] Growth type clearly identified (Vibe/Trust/Agentic Growth)

## Requirement Completeness

- [ ] No [NEEDS CLARIFICATION] markers remain (max 3 allowed)
- [ ] Requirements are testable and unambiguous
- [ ] Success criteria are measurable
- [ ] Success criteria are technology-agnostic (no implementation details)
- [ ] Target audience is specific (not "everyone")
- [ ] Scope is clearly bounded
- [ ] Dependencies and assumptions identified

## Growth Hacking Specifics

- [ ] Primary growth metric defined (k-factor, NRR, time-to-wow, etc.)
- [ ] Viral loop mechanism identified (Remix/Integration/Watermark)
- [ ] Pilot scope clearly defined (budget, duration, audience size)
- [ ] Key assumptions documented
- [ ] Platform strategy identified (X/Twitter, TikTok, LinkedIn, GitHub, Product Hunt)
- [ ] Community amplification path identified

## Validation Results

- [ ] Content Quality: PASS
- [ ] Requirement Completeness: PASS
- [ ] Growth Hacking Specifics: PASS
- [ ] Constitution Check: PASS

## Recommendations

1. Proceed to `/growthkit.plan` to design implementation tactics
2. During planning, address platform-specific strategies
3. Document GEO optimization opportunities
4. Identify pilot scope and validation gates

**Status**: Ready for planning when all sections complete ✓

**Last Updated**: [DATE]
"""
