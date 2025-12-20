"""Main CLI application for Growth Hacking Kit."""

import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from growthkit import __version__
from growthkit.cli import config, utils

# Initialize Typer app
app = typer.Typer(
    name="growthkit",
    help="Growth Hacking Kit - Spec-driven growth campaign management for AI SaaS products",
    no_args_is_help=True,
)

console = Console()


@app.command()
def init(
    project_name: Optional[str] = typer.Argument(
        None,
        help="Project name or path (use '.' or '--here' for current directory)"
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
    console.print("[bold cyan]Growth Hacking Kit[/bold cyan] - Initializing project...")

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

    # Create agent command directories
    for agent in config.AGENT_DIRS.keys():
        agent_cmd_dir = project_dir / config.AGENT_DIRS[agent]
        agent_cmd_dir.mkdir(parents=True, exist_ok=True)

    console.print("[green]✓[/green] Agent command directories created")

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
        console.print(f"\n[dim]Debug info:")
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
def version() -> None:
    """Show version information."""
    console.print(f"Growth Hacking Kit version [bold]{__version__}[/bold]")
    console.print(f"CLI Framework: typer")
    console.print(f"Python: 3.11+")


if __name__ == "__main__":
    app()
