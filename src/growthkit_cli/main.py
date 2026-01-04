"""
Main CLI entry point for Growth-Hacking-Kit
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from growthkit_cli import __version__
from growthkit_cli.commands.init import init_command

console = Console()

ASCII_ART = """
   ____                   _   _       _   _            _    _             _  ___ _
  / ___|_ __ _____      _| |_| |__   | | | | __ _  ___| | _(_)_ __   __ _| |/ (_) |_
 | |  _| '__/ _ \\ \\ /\\ / / __| '_ \\  | |_| |/ _` |/ __| |/ / | '_ \\ / _` | ' /| | __|
 | |_| | | | (_) \\ V  V /| |_| | | | |  _  | (_| | (__|   <| | | | | (_| | . \\| | |_
  \\____|_|  \\___/ \\_/\\_/  \\__|_| |_| |_| |_|\\__,_|\\___|_|\\_\\_|_| |_|\\__, |_|\\_\\_|\\__|
                                                                      |___/
"""


def print_banner():
    """Print the Growth Hacking Kit ASCII banner"""
    banner_text = Text(ASCII_ART, style="bold cyan")
    console.print(banner_text)
    console.print(
        Panel(
            "[bold white]Systematic Growth Campaign Management[/bold white]\\n"
            "[dim]Spec-driven growth hacking with viral loop engineering[/dim]",
            border_style="cyan",
            padding=(0, 2),
        )
    )
    console.print()


@click.group()
@click.version_option(version=__version__, prog_name="growthkit")
@click.pass_context
def cli(ctx):
    """
    Growth-Hacking-Kit CLI - Systematic growth campaign management

    Initialize growth campaign projects with templates for multiple AI agents.
    """
    if ctx.invoked_subcommand is None:
        print_banner()


# Register commands
cli.add_command(init_command, name="init")


if __name__ == "__main__":
    cli()
