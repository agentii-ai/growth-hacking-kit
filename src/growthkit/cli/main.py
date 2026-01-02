"""Main CLI application for Growth Hacking Kit."""

import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from growthkit import __version__
from growthkit.cli import config, utils
from growthkit.cli import specify as specify_module
from growthkit.cli import plan as plan_module
from growthkit.cli import tasks as tasks_module
from growthkit.cli import implement as implement_module

# Initialize Typer app
app = typer.Typer(
    name="growthkit",
    help="Growth Hacking Kit - Spec-driven growth campaign management for AI SaaS products",
    no_args_is_help=True,
)

console = Console()


def print_banner():
    """Display the Growth Hacking Kit ASCII banner."""
    banner = r"""
   ____                   _   _       _   _            _    _             _  ___ _
  / ___|_ __ _____      _| |_| |__   | | | | __ _  ___| | _(_)_ __   __ _| |/ (_) |_
 | |  _| '__/ _ \ \ /\ / / __| '_ \  | |_| |/ _` |/ __| |/ / | '_ \ / _` | ' /| | __|
 | |_| | | | (_) \ V  V /| |_| | | | |  _  | (_| | (__|   <| | | | | (_| | . \| | |_
  \____|_|  \___/ \_/\_/  \__|_| |_| |_| |_|\__,_|\___|_|\_\_|_| |_|\__, |_|\_\_|\__|
                                                                     |___/
                              Growth Hacking Kit v0.2.0
                         Spec-Driven Campaign Management for AI SaaS
    """
    console.print(f"[bold cyan]{banner}[/bold cyan]")


@app.command()
def init(
    project_name: Optional[str] = typer.Argument(
        None, help="Project name or path (use '.' or '--here' for current directory)"
    ),
    ai: Optional[str] = typer.Option(
        None,
        "--ai",
        help="Target AI agent (claude, cursor-agent, windsurf, copilot)",
    ),
    script: Optional[str] = typer.Option(
        "bash",
        "--script",
        help="Script type (bash or powershell)",
    ),
    ignore_agent_tools: bool = typer.Option(
        False,
        "--ignore-agent-tools",
        help="Skip agent tool detection",
    ),
    no_git: bool = typer.Option(
        False,
        "--no-git",
        help="Skip git repository initialization",
    ),
    here: bool = typer.Option(
        False,
        "--here",
        help="Initialize in current directory",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Force overwrite existing files",
    ),
    skip_tls: bool = typer.Option(
        False,
        "--skip-tls",
        help="Skip TLS verification",
    ),
    debug: bool = typer.Option(
        False,
        "--debug",
        help="Enable debug logging",
    ),
    github_token: Optional[str] = typer.Option(
        None,
        "--github-token",
        help="GitHub token for API requests",
    ),
) -> None:
    """
    Initialize a new Growth Hacking Kit project.

    Examples:
        growthkit init my-campaign --ai claude
        growthkit init . --ai cursor-agent
        growthkit init --here --ai windsurf
    """
    # Display ASCII banner
    print_banner()

    console.print("[bold cyan]Growth Hacking Kit[/bold cyan] - Initializing project...")
    console.print("")

    # Determine project directory
    if here or project_name == ".":
        project_dir = Path.cwd()
    elif project_name:
        project_dir = Path(project_name).absolute()
    else:
        console.print("[red]Error:[/red] Project name required (or use --here)")
        sys.exit(1)

    # Create project directory
    project_dir.mkdir(parents=True, exist_ok=True)
    console.print(f"[green]✓[/green] Project directory: {project_dir}")

    # Initialize git repository if not --no-git
    if not no_git:
        try:
            utils.init_git_repo(project_dir)
            console.print("[green]✓[/green] Git repository initialized")
        except Exception as e:
            if not force:
                console.print(f"[yellow]⚠[/yellow] Git initialization failed: {e}")

    # Create directory structure
    (project_dir / config.PACKAGE_DIR).mkdir(exist_ok=True)
    (project_dir / config.PACKAGE_DIR / "memory").mkdir(exist_ok=True)
    (project_dir / config.PACKAGE_DIR / "scripts" / "bash").mkdir(parents=True, exist_ok=True)
    (project_dir / config.PACKAGE_DIR / "templates" / "commands").mkdir(parents=True, exist_ok=True)
    (project_dir / "specs").mkdir(exist_ok=True)

    console.print("[green]✓[/green] Directory structure created")

    # Copy constitution template
    constitution_src = Path(__file__).parent.parent / "templates" / "constitution.md"
    constitution_dst = project_dir / config.CONSTITUTION_FILE
    if constitution_src.exists():
        constitution_dst.parent.mkdir(parents=True, exist_ok=True)
        constitution_dst.write_text(constitution_src.read_text())
        console.print("[green]✓[/green] Constitution installed")
    else:
        console.print("[yellow]⚠[/yellow] Constitution template not found (this is okay)")

    # Detect or set AI agent
    if not ai:
        detected_agents = utils.detect_installed_agents()
        available = [agent for agent, installed in detected_agents.items() if installed]

        if available:
            ai = available[0]
            console.print(f"[green]✓[/green] Detected AI agent: {ai}")
        else:
            ai = config.DEFAULT_AI_AGENT
            console.print(f"[yellow]⚠[/yellow] No AI agent detected, defaulting to {ai}")

    # Determine script type based on platform
    import platform

    if script is None:
        script = "ps" if platform.system() == "Windows" else "sh"

    # Try to download templates from GitHub releases
    console.print(f"\n[cyan]Downloading Growth Hacking Kit templates for {ai}...[/cyan]")

    template_zip = utils.download_template_from_github(
        agent=ai, script=script, github_token=github_token, skip_tls=skip_tls
    )

    if template_zip and template_zip.exists():
        console.print(f"[green]✓[/green] Downloaded template: {template_zip.name}")

        # Extract template
        if utils.extract_template(template_zip, project_dir):
            console.print("[green]✓[/green] Templates installed from GitHub release")
        else:
            console.print("[yellow]⚠[/yellow] Template extraction failed, using default structure")
    else:
        console.print(
            "[yellow]⚠[/yellow] Could not download templates from GitHub, using default structure"
        )

    # Create agent command directories (fallback if download failed)
    for agent_name in config.AGENT_DIRS.keys():
        agent_cmd_dir = project_dir / config.AGENT_DIRS[agent_name]
        agent_cmd_dir.mkdir(parents=True, exist_ok=True)

    console.print("[green]✓[/green] Agent command directories verified")

    # Output next steps
    console.print("\n[bold green]Project initialized successfully![/bold green]\n")
    console.print("Next steps:")
    console.print("  1. Launch your AI agent in the project directory")
    console.print("  2. Run [cyan]/growthkit.constitution[/cyan] to establish principles")
    console.print("  3. Run [cyan]/growthkit.specify[/cyan] to create campaign specifications")
    console.print("  4. Run [cyan]/growthkit.plan[/cyan] to plan implementation")
    console.print("  5. Run [cyan]/growthkit.tasks[/cyan] to generate task breakdown")
    console.print("  6. Run [cyan]/growthkit.implement[/cyan] to execute campaign")

    if debug:
        console.print("\n[dim]Debug info:")
        console.print(f"  Project: {project_dir}")
        console.print(f"  AI Agent: {ai}")
        console.print(f"  Kit Version: {__version__}[/dim]")


@app.command()
def check(debug: bool = typer.Option(False, "--debug", help="Enable debug output")) -> None:
    """
    Check for installed tools and dependencies.

    Verifies: git, python, uv, and AI agents (Claude Code, Cursor, Windsurf, Copilot)
    """
    console.print("[bold]Growth Hacking Kit - Checking prerequisites...[/bold]\n")

    # Create status table
    table = Table(title="System Status")
    table.add_column("Tool", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Details")

    # Check git
    git_ok = utils._check_command_exists("git")
    table.add_row(
        "Git",
        "[green]✓[/green]" if git_ok else "[red]✗[/red]",
        "Version control required" if git_ok else "Not found",
    )

    # Check Python
    python_ok = utils._check_command_exists("python3")
    table.add_row(
        "Python 3.11+",
        "[green]✓[/green]" if python_ok else "[red]✗[/red]",
        "Required for growthkit" if python_ok else "Not found",
    )

    # Check uv
    uv_ok = utils._check_command_exists("uv")
    table.add_row(
        "uv",
        "[green]✓[/green]" if uv_ok else "[yellow]⚠[/yellow]",
        "Recommended for package management" if uv_ok else "Not found",
    )

    # Check agents
    agents = utils.detect_installed_agents()
    table.add_row(
        "Claude Code",
        "[green]✓[/green]" if agents.get("claude") else "[dim]○[/dim]",
        "Detected" if agents.get("claude") else "Not installed",
    )
    table.add_row(
        "Cursor",
        "[green]✓[/green]" if agents.get("cursor") else "[dim]○[/dim]",
        "Detected" if agents.get("cursor") else "Not installed",
    )
    table.add_row(
        "Windsurf",
        "[green]✓[/green]" if agents.get("windsurf") else "[dim]○[/dim]",
        "Detected" if agents.get("windsurf") else "Not installed",
    )
    table.add_row(
        "GitHub Copilot",
        "[green]✓[/green]" if agents.get("copilot") else "[dim]○[/dim]",
        "Detected" if agents.get("copilot") else "Not installed",
    )

    console.print(table)

    if debug:
        console.print("\n[dim]Debug info:")
        console.print(f"  Git OK: {git_ok}")
        console.print(f"  Python OK: {python_ok}")
        console.print(f"  uv OK: {uv_ok}")
        console.print(f"  Agents: {agents}")


@app.command()
def specify(
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
    specify_module.specify_command(description, force, debug)


@app.command()
def plan(
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
    plan_module.plan_command(description, force, debug)


@app.command()
def tasks_cmd(
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
    tasks_module.tasks_command(description, force, debug)


@app.command()
def implement(
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
    implement_module.implement_command(description, force, debug)


@app.command()
def version() -> None:
    """Show version information."""
    console.print(f"Growth Hacking Kit version [bold]{__version__}[/bold]")
    console.print("CLI Framework: typer")
    console.print("Python: 3.11+")


if __name__ == "__main__":
    app()
