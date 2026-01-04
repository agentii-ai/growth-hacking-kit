"""
Template download and initialization utilities
"""

import io
import os
import zipfile
from pathlib import Path
from typing import Optional

import requests
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

GITHUB_REPO = "agentii-ai/growth-hacking-kit"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
GITHUB_RELEASE_URL = f"https://github.com/{GITHUB_REPO}/releases/download"

# Supported agents
AGENTS = [
    "claude",
    "cursor-agent",
    "windsurf",
    "gemini",
    "copilot",
    "qoder",
    "qwen",
    "opencode",
    "codex",
    "kilocode",
    "auggie",
    "roo",
    "codebuddy",
    "amp",
    "shai",
    "q",
    "bob",
]

# Script types
SCRIPTS = ["sh", "ps"]


def get_latest_version() -> str:
    """Get the latest release version from GitHub"""
    try:
        response = requests.get(GITHUB_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["tag_name"]
    except Exception as e:
        console.print(f"[yellow]Warning: Could not fetch latest version: {e}[/yellow]")
        return "v0.3.0"  # Fallback version


def download_template(agent: str, script: str, version: str, target_dir: Path) -> bool:
    """
    Download and extract a template from GitHub releases

    Args:
        agent: Agent name (e.g., 'claude', 'cursor-agent')
        script: Script type ('sh' or 'ps')
        version: Version tag (e.g., 'v0.3.0')
        target_dir: Target directory to extract template

    Returns:
        True if successful, False otherwise
    """
    template_name = f"spec-kit-template-{agent}-{script}-{version}.zip"
    download_url = f"{GITHUB_RELEASE_URL}/{version}/{template_name}"

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task(f"Downloading {template_name}...", total=None)

            # Download the ZIP file
            response = requests.get(download_url, timeout=30)
            response.raise_for_status()

            progress.update(task, description=f"Extracting {template_name}...")

            # Extract the ZIP file
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
                # Get the root directory name from the ZIP
                root_dir = zip_ref.namelist()[0].split("/")[0]

                # Extract all files
                zip_ref.extractall(target_dir.parent)

                # Rename the extracted directory to target_dir
                extracted_path = target_dir.parent / root_dir
                if extracted_path != target_dir:
                    if target_dir.exists():
                        import shutil

                        shutil.rmtree(target_dir)
                    extracted_path.rename(target_dir)

            progress.update(task, description=f"✓ Template extracted to {target_dir}")

        return True

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            console.print(
                f"[red]Error: Template not found at {download_url}[/red]\\n"
                f"[yellow]Available agents: {', '.join(AGENTS)}[/yellow]\\n"
                f"[yellow]Available scripts: {', '.join(SCRIPTS)}[/yellow]"
            )
        else:
            console.print(f"[red]Error downloading template: {e}[/red]")
        return False
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return False


def validate_agent(agent: str) -> bool:
    """Validate that the agent is supported"""
    return agent in AGENTS


def validate_script(script: str) -> bool:
    """Validate that the script type is supported"""
    return script in SCRIPTS
