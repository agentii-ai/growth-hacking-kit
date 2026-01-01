"""Configuration constants for Growth Hacking Kit."""

import os
from pathlib import Path

# Kit identification
KIT_NAME = "growthkit"
KIT_VERSION = "0.0.96"

# Directory structure
PACKAGE_DIR = ".growthkit/"
SPECS_DIR = "specs/"
MEMORY_DIR = f"{PACKAGE_DIR}memory/"
SCRIPTS_DIR = f"{PACKAGE_DIR}scripts/"
TEMPLATES_DIR = f"{PACKAGE_DIR}templates/"
COMMANDS_DIR = f"{TEMPLATES_DIR}commands/"

# Environment variables
ENV_VAR = "GROWTHKIT_CAMPAIGN"

# Agent integration directories
AGENT_DIRS = {
    "claude": ".claude/commands/",
    "cursor": ".cursor/commands/",
    "windsurf": ".windsurf/commands/",
    "copilot": ".github/copilot/",
}

# Branch naming
BRANCH_PREFIX = ""  # Feature numbers like 001-campaign-name
BRANCH_PATTERN = r"^\d{3}-[\w-]+$"

# Constitution
CONSTITUTION_FILE = f"{MEMORY_DIR}constitution.md"
CONSTITUTION_VERSION = "1.1.0"

# Growth types
GROWTH_TYPES = ["Vibe Growth", "Trust Growth", "Agentic Growth"]

# Viral loop types
VIRAL_LOOPS = ["Remix Loop", "Integration Loop", "Watermark Loop"]

# Platform specifications
PLATFORMS = {
    "twitter": {
        "name": "X/Twitter",
        "format": "30-60s screen recording",
        "aspect_ratio": "16:9",
        "viral_mechanism": "Quote tweets, developer community",
    },
    "tiktok": {
        "name": "TikTok",
        "format": "15-30s vertical video",
        "aspect_ratio": "9:16",
        "viral_mechanism": "Duets, remixes, trending audio",
        "hook_time": "3 seconds",
    },
    "linkedin": {
        "name": "LinkedIn",
        "format": "Data-driven case studies",
        "aspect_ratio": "1:1 or 16:9",
        "viral_mechanism": "Professional sharing, credibility signals",
    },
    "github": {
        "name": "GitHub",
        "format": "Code examples, integration guides",
        "viral_mechanism": "Stars, forks, community contributions",
    },
    "product_hunt": {
        "name": "Product Hunt",
        "format": "Demo video + first-100-user incentives",
        "viral_mechanism": "Upvotes, maker community engagement",
    },
}

# 2025 Growth Metrics Benchmarks
GROWTH_METRICS = {
    "acceptance_rate": {"benchmark": 0.30, "unit": "%"},
    "time_to_wow": {"benchmark": 300, "unit": "seconds"},  # 5 minutes
    "time_to_trust": {"benchmark": 7, "unit": "days"},
    "agent_autonomy": {"benchmark": 5, "unit": "steps"},
    "k_factor": {"benchmark": 1.1, "unit": "ratio"},
    "nrr": {"benchmark": 106, "unit": "%", "range": "106-120%"},
    "time_to_first_share": {"benchmark": 24, "unit": "hours"},
}

# Performance goals
PERFORMANCE_GOALS = {
    "init_timeout": 2,  # seconds
    "spec_generation_timeout": 5,  # seconds
    "constitution_check_timeout": 1,  # seconds
}

# CLI defaults
DEFAULT_AI_AGENT = "claude"
DEFAULT_SCRIPT_TYPE = "bash"
MAX_CLARIFICATION_MARKERS = 3


def get_project_root() -> Path:
    """Get the project root directory (where .git or .growthkit exists)."""
    current = Path.cwd()
    while current != current.parent:
        if (current / ".git").exists() or (current / PACKAGE_DIR).exists():
            return current
        current = current.parent
    return Path.cwd()


def get_current_campaign() -> str | None:
    """Get current campaign from environment variable or git branch."""
    # Check environment variable first
    if env_campaign := os.getenv(ENV_VAR):
        return env_campaign

    # Try to get from git branch
    try:
        import git

        repo = git.Repo(get_project_root())
        branch = repo.active_branch.name

        # Check if branch matches campaign pattern (###-campaign-name)
        import re

        if re.match(BRANCH_PATTERN, branch):
            return branch
    except Exception:
        pass

    return None


def get_campaign_dir(campaign: str) -> Path:
    """Get the directory for a specific campaign."""
    return get_project_root() / SPECS_DIR / campaign
