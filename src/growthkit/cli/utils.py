"""Utility functions for Growth Hacking Kit CLI."""

import json
import os
import re
import subprocess
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from typing import Any, Optional

import git
from jinja2 import Environment, FileSystemLoader, Template

from growthkit.cli.config import (
    AGENT_DIRS,
    KIT_NAME,
    PACKAGE_DIR,
    SPECS_DIR,
    get_project_root,
)

# Constants for template downloads
GITHUB_REPO = "your-org/growth-hacking-kit"  # TODO: Update with actual repo
GITHUB_API_URL = "https://api.github.com"
GITHUB_RELEASES_URL = f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/releases"


# Git Operations


def init_git_repo(project_dir: Path) -> git.Repo:
    """Initialize a git repository in the project directory."""
    return git.Repo.init(project_dir)


def create_campaign_branch(campaign_number: int, campaign_name: str) -> str:
    """
    Create a new campaign branch with format ###-campaign-name.

    Args:
        campaign_number: The campaign number (e.g., 1, 2, 3)
        campaign_name: The short campaign name (2-4 words)

    Returns:
        The full branch name (e.g., "001-product-hunt-launch")
    """
    branch_name = f"{campaign_number:03d}-{campaign_name}"

    try:
        repo = git.Repo(get_project_root())

        # Create and checkout new branch
        if branch_name not in repo.heads:
            new_branch = repo.create_head(branch_name)
            new_branch.checkout()
        else:
            repo.heads[branch_name].checkout()

        return branch_name
    except git.exc.InvalidGitRepositoryError:
        raise ValueError("Not a git repository. Run 'git init' first or use 'growthkit init' with --no-git flag.")


def get_next_campaign_number() -> int:
    """
    Find the next available campaign number by checking:
    1. Remote branches
    2. Local branches
    3. specs/ directories

    Returns:
        The next available campaign number
    """
    max_number = 0

    try:
        repo = git.Repo(get_project_root())

        # Check remote branches
        try:
            for ref in repo.remote().refs:
                if match := re.match(r"^origin/(\d{3})-", ref.name):
                    max_number = max(max_number, int(match.group(1)))
        except (git.exc.GitCommandError, ValueError):
            pass

        # Check local branches
        for branch in repo.heads:
            if match := re.match(r"^(\d{3})-", branch.name):
                max_number = max(max_number, int(match.group(1)))
    except git.exc.InvalidGitRepositoryError:
        pass

    # Check specs/ directories
    specs_dir = get_project_root() / SPECS_DIR
    if specs_dir.exists():
        for item in specs_dir.iterdir():
            if item.is_dir() and (match := re.match(r"^(\d{3})-", item.name)):
                max_number = max(max_number, int(match.group(1)))

    return max_number + 1


def extract_campaign_name(description: str) -> str:
    """
    Extract a short campaign name (2-4 words) from campaign description.

    Args:
        description: Full campaign description

    Returns:
        Short campaign name suitable for branch name (lowercase, hyphens)

    Example:
        "Launch Product Hunt campaign with demo video" -> "product-hunt-launch"
    """
    # Remove common growth hacking keywords
    stop_words = {
        "campaign", "with", "using", "for", "and", "the", "a", "an",
        "strategy", "tactics", "growth", "hacking", "launch", "create",
        "build", "implement", "execute", "run", "start", "begin",
    }

    # Extract words
    words = re.findall(r'\b\w+\b', description.lower())

    # Filter out stop words and keep meaningful words
    meaningful_words = [w for w in words if w not in stop_words and len(w) > 2]

    # Take first 2-4 meaningful words
    campaign_words = meaningful_words[:4] if len(meaningful_words) >= 4 else meaningful_words[:3]

    # If we don't have enough words, use first 3 words from original
    if len(campaign_words) < 2:
        campaign_words = [w for w in words[:3] if len(w) > 2]

    return "-".join(campaign_words[:4])


def get_git_status() -> dict[str, Any]:
    """
    Get git repository status.

    Returns:
        Dictionary with git status information
    """
    try:
        repo = git.Repo(get_project_root())
        return {
            "is_repo": True,
            "branch": repo.active_branch.name,
            "is_dirty": repo.is_dirty(),
            "untracked_files": repo.untracked_files,
            "modified_files": [item.a_path for item in repo.index.diff(None)],
        }
    except git.exc.InvalidGitRepositoryError:
        return {"is_repo": False}


# Agent Detection


def detect_installed_agents() -> dict[str, bool]:
    """
    Detect which AI coding agents are installed.

    Returns:
        Dictionary mapping agent name to installed status
    """
    agents = {}

    # Claude Code detection (via claude-code command)
    agents["claude"] = _check_command_exists("claude-code")

    # Cursor detection (via cursor command or app)
    agents["cursor"] = _check_command_exists("cursor") or _check_app_exists("Cursor")

    # Windsurf detection (via windsurf command or app)
    agents["windsurf"] = _check_command_exists("windsurf") or _check_app_exists("Windsurf")

    # GitHub Copilot detection (via gh copilot)
    agents["copilot"] = _check_command_exists("gh") and _check_gh_copilot()

    return agents


def _check_command_exists(command: str) -> bool:
    """Check if a command exists in PATH."""
    try:
        subprocess.run(
            ["which", command],
            check=True,
            capture_output=True,
            text=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def _check_app_exists(app_name: str) -> bool:
    """Check if a macOS app exists (macOS only)."""
    if os.name != "posix":
        return False

    try:
        result = subprocess.run(
            ["mdfind", f"kMDItemKind == 'Application' && kMDItemDisplayName == '{app_name}'"],
            check=True,
            capture_output=True,
            text=True,
        )
        return bool(result.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def _check_gh_copilot() -> bool:
    """Check if GitHub Copilot CLI extension is installed."""
    try:
        result = subprocess.run(
            ["gh", "extension", "list"],
            check=True,
            capture_output=True,
            text=True,
        )
        return "gh-copilot" in result.stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_agent_command_dir(agent: str) -> Path:
    """
    Get the command directory for a specific agent.

    Args:
        agent: Agent name (claude, cursor, windsurf, copilot)

    Returns:
        Path to agent command directory
    """
    if agent not in AGENT_DIRS:
        raise ValueError(f"Unknown agent: {agent}. Must be one of {list(AGENT_DIRS.keys())}")

    return get_project_root() / AGENT_DIRS[agent]


# Template Rendering


def render_template(template_path: Path, context: dict[str, Any]) -> str:
    """
    Render a Jinja2 template with the given context.

    Args:
        template_path: Path to template file
        context: Dictionary of template variables

    Returns:
        Rendered template content
    """
    # Add KIT_NAME to context if not present
    if "KIT_NAME" not in context:
        context["KIT_NAME"] = KIT_NAME

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    # Load template
    env = Environment(loader=FileSystemLoader(template_path.parent))
    template = env.get_template(template_path.name)

    return template.render(**context)


def render_template_string(template_string: str, context: dict[str, Any]) -> str:
    """
    Render a Jinja2 template string with the given context.

    Args:
        template_string: Template content as string
        context: Dictionary of template variables

    Returns:
        Rendered template content
    """
    # Add KIT_NAME to context if not present
    if "KIT_NAME" not in context:
        context["KIT_NAME"] = KIT_NAME

    template = Template(template_string)
    return template.render(**context)


# Campaign Management


def create_campaign_directory(campaign_number: int, campaign_name: str) -> Path:
    """
    Create a campaign directory in specs/.

    Args:
        campaign_number: Campaign number (e.g., 1)
        campaign_name: Short campaign name (e.g., "product-hunt-launch")

    Returns:
        Path to created campaign directory
    """
    branch_name = f"{campaign_number:03d}-{campaign_name}"
    campaign_dir = get_project_root() / SPECS_DIR / branch_name

    # Create directory structure
    campaign_dir.mkdir(parents=True, exist_ok=True)
    (campaign_dir / "checklists").mkdir(exist_ok=True)
    (campaign_dir / "assets").mkdir(exist_ok=True)

    return campaign_dir


# Shell Script Execution


def run_bash_script(script_name: str, args: list[str] | None = None) -> dict[str, Any]:
    """
    Run a bash script from .growthkit/scripts/bash/.

    Args:
        script_name: Name of script (without .sh extension)
        args: Optional arguments to pass to script

    Returns:
        Dictionary with script output (stdout, stderr, returncode)
    """
    script_path = get_project_root() / PACKAGE_DIR / "scripts" / "bash" / f"{script_name}.sh"

    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")

    cmd = ["bash", str(script_path)]
    if args:
        cmd.extend(args)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=get_project_root(),
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode,
        "success": result.returncode == 0,
    }


def parse_json_output(output: str) -> dict[str, Any]:
    """Parse JSON output from bash scripts."""
    try:
        return json.loads(output)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON output: {e}")


def get_campaign_dir_from_branch(branch_or_campaign: str) -> Path:
    """
    Get campaign directory from branch name or campaign ID.

    Args:
        branch_or_campaign: Branch name (e.g., "001-product-hunt-launch") or campaign ID

    Returns:
        Path to campaign directory

    Raises:
        ValueError: If campaign directory not found
    """
    specs_dir = get_project_root() / SPECS_DIR

    # Try exact match first
    if (specs_dir / branch_or_campaign).exists():
        return specs_dir / branch_or_campaign

    # Try to find by pattern
    for campaign_dir in specs_dir.iterdir():
        if campaign_dir.is_dir() and campaign_dir.name.startswith(branch_or_campaign):
            return campaign_dir

    raise ValueError(f"Campaign not found: {branch_or_campaign}")


# Template Download from GitHub Releases


def get_latest_release_version(github_token: Optional[str] = None, skip_tls: bool = False) -> Optional[str]:
    """
    Get the latest release version from GitHub.

    Args:
        github_token: Optional GitHub token for API requests
        skip_tls: Skip TLS verification (for testing)

    Returns:
        Latest release version (e.g., "v0.2.0") or None if not found
    """
    try:
        headers = {"Accept": "application/vnd.github.v3+json"}
        if github_token:
            headers["Authorization"] = f"token {github_token}"

        request = urllib.request.Request(f"{GITHUB_RELEASES_URL}/latest", headers=headers)

        if skip_tls:
            import ssl
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context=context)
        else:
            response = urllib.request.urlopen(request)

        data = json.loads(response.read().decode())
        return data.get("tag_name")
    except Exception:
        # Fallback: return None and let caller handle
        return None


def download_template_from_github(
    agent: str,
    script: str,
    version: Optional[str] = None,
    github_token: Optional[str] = None,
    skip_tls: bool = False
) -> Optional[Path]:
    """
    Download template ZIP from GitHub releases.

    Args:
        agent: Agent name (claude, cursor-agent, windsurf, etc.)
        script: Script type (sh or ps)
        version: Version tag (e.g., "v0.2.0"). If None, uses latest
        github_token: Optional GitHub token for API requests
        skip_tls: Skip TLS verification (for testing)

    Returns:
        Path to downloaded ZIP file or None if download failed
    """
    try:
        # Get version if not provided
        if not version:
            version = get_latest_release_version(github_token, skip_tls)
            if not version:
                return None

        # Construct download URL
        filename = f"growthkit-template-{agent}-{script}-{version}.zip"
        download_url = f"https://github.com/{GITHUB_REPO}/releases/download/{version}/{filename}"

        # Create temp file
        temp_dir = Path(tempfile.gettempdir()) / "growthkit-templates"
        temp_dir.mkdir(parents=True, exist_ok=True)
        zip_path = temp_dir / filename

        # Download
        headers = {}
        if github_token:
            headers["Authorization"] = f"token {github_token}"

        request = urllib.request.Request(download_url, headers=headers)

        if skip_tls:
            import ssl
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context=context)
        else:
            response = urllib.request.urlopen(request)

        with open(zip_path, "wb") as f:
            f.write(response.read())

        return zip_path
    except Exception:
        return None


def extract_template(zip_path: Path, target_dir: Path) -> bool:
    """
    Extract template ZIP to target directory.

    Args:
        zip_path: Path to template ZIP file
        target_dir: Directory to extract to

    Returns:
        True if extraction succeeded, False otherwise
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # List all files in the ZIP
            namelist = zip_ref.namelist()

            # Find the root directory (first directory in ZIP)
            root_dirs = set()
            for name in namelist:
                parts = Path(name).parts
                if len(parts) > 0:
                    root_dirs.add(parts[0])

            # If there's a single root directory, extract and move contents
            if len(root_dirs) == 1:
                root_dir = list(root_dirs)[0]
                temp_extract = target_dir / ".temp_extract"
                temp_extract.mkdir(parents=True, exist_ok=True)

                # Extract to temp location
                zip_ref.extractall(temp_extract)

                # Move contents from root_dir to target_dir
                source = temp_extract / root_dir
                for item in source.iterdir():
                    dest = target_dir / item.name
                    if dest.exists():
                        # Skip if already exists (don't overwrite)
                        continue
                    item.rename(dest)

                # Cleanup temp directory
                import shutil
                shutil.rmtree(temp_extract)
            else:
                # Extract directly
                zip_ref.extractall(target_dir)

        return True
    except Exception:
        return False

