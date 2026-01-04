"""
Init command for Growth-Hacking-Kit CLI
"""

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

from growthkit_cli.utils import (
    AGENTS,
    SCRIPTS,
    download_template,
    get_latest_version,
    validate_agent,
    validate_script,
)

console = Console()


@click.command()
@click.argument("project_name", required=False)
@click.option(
    "--agent",
    "-a",
    type=click.Choice(AGENTS, case_sensitive=False),
    help="AI agent to use (e.g., claude, cursor-agent, windsurf)",
)
@click.option(
    "--script",
    "-s",
    type=click.Choice(SCRIPTS, case_sensitive=False),
    default="sh",
    help="Script type: sh (bash) or ps (PowerShell)",
)
@click.option(
    "--version",
    "-v",
    help="Template version to download (default: latest)",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Overwrite existing directory",
)
def init_command(project_name, agent, script, version, force):
    """
    Initialize a new Growth-Hacking-Kit project

    Creates a new project directory with templates for your chosen AI agent.

    Examples:

        growthkit init my-campaign --agent claude

        growthkit init my-campaign --agent cursor-agent --script ps

        growthkit init my-campaign -a windsurf -s sh
    """
    console.print()
    console.print("[bold cyan]Growth-Hacking-Kit Initializer[/bold cyan]")
    console.print()

    # Get project name if not provided
    if not project_name:
        project_name = Prompt.ask(
            "[cyan]Project name[/cyan]",
            default="my-growth-campaign",
        )

    # Get agent if not provided
    if not agent:
        console.print("\\n[bold]Available AI Agents:[/bold]")
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Agent", style="cyan")
        table.add_column("Description")

        agent_descriptions = {
            "claude": "Claude Code (Anthropic)",
            "cursor-agent": "Cursor AI",
            "windsurf": "Windsurf IDE",
            "gemini": "Google Gemini",
            "copilot": "GitHub Copilot",
            "qoder": "Qoder AI",
            "qwen": "Qwen AI",
            "opencode": "OpenCode AI",
            "codex": "OpenAI Codex",
            "kilocode": "Kilocode AI",
            "auggie": "Augment Code",
            "roo": "Roo Cline",
            "codebuddy": "CodeBuddy AI",
            "amp": "AMP AI",
            "shai": "Shai AI",
            "q": "Amazon Q",
            "bob": "Bob AI",
        }

        for agent_name in AGENTS:
            table.add_row(agent_name, agent_descriptions.get(agent_name, ""))

        console.print(table)
        console.print()

        agent = Prompt.ask(
            "[cyan]Choose an agent[/cyan]",
            choices=AGENTS,
            default="claude",
        )

    # Validate inputs
    if not validate_agent(agent):
        console.print(f"[red]Error: Invalid agent '{agent}'[/red]")
        console.print(f"[yellow]Available agents: {', '.join(AGENTS)}[/yellow]")
        sys.exit(1)

    if not validate_script(script):
        console.print(f"[red]Error: Invalid script type '{script}'[/red]")
        console.print(f"[yellow]Available scripts: {', '.join(SCRIPTS)}[/yellow]")
        sys.exit(1)

    # Get version
    if not version:
        console.print("[dim]Fetching latest version...[/dim]")
        version = get_latest_version()

    # Create target directory
    target_dir = Path.cwd() / project_name

    if target_dir.exists() and not force:
        if not Confirm.ask(
            f"[yellow]Directory '{project_name}' already exists. Overwrite?[/yellow]"
        ):
            console.print("[yellow]Aborted.[/yellow]")
            sys.exit(0)

    # Download and extract template
    console.print()
    console.print(
        Panel(
            f"[bold]Project:[/bold] {project_name}\\n"
            f"[bold]Agent:[/bold] {agent}\\n"
            f"[bold]Script:[/bold] {script}\\n"
            f"[bold]Version:[/bold] {version}",
            title="Configuration",
            border_style="cyan",
        )
    )
    console.print()

    success = download_template(agent, script, version, target_dir)

    if success:
        console.print()
        console.print(
            Panel(
                f"[bold green]✓ Project initialized successfully![/bold green]\\n\\n"
                f"[bold]Next steps:[/bold]\\n"
                f"  1. cd {project_name}\\n"
                f"  2. Review .specify/memory/constitution.md\\n"
                f"  3. Start with: /{agent.replace('-', '')}.specify\\n\\n"
                f"[dim]Templates are in .specify/templates/[/dim]\\n"
                f"[dim]Commands are in .{agent.split('-')[0]}/commands/[/dim]",
                title="Success",
                border_style="green",
            )
        )
        console.print()
    else:
        console.print()
        console.print("[red]✗ Failed to initialize project[/red]")
        sys.exit(1)
