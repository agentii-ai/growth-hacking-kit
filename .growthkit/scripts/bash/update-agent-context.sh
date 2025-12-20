#!/usr/bin/env bash

# Update agent context files for Growth Hacking Kit
# Updates CLAUDE.md, .cursor/README.md, .windsurf/README.md with technology references

set -e

# Source common utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Get project root
PROJECT_ROOT=$(get_project_root)
cd "$PROJECT_ROOT"

log_info "Updating agent context files..."

# Create/update CLAUDE.md
CLAUDE_FILE="$PROJECT_ROOT/CLAUDE.md"
cat > "$CLAUDE_FILE" << 'EOF'
# Growth Hacking Kit - Claude Code Context

## Overview
This is a Growth Hacking Kit project - a spec-driven methodology for growth campaign management for AI SaaS products.

## Project Structure
- `.growthkit/` - Kit-specific files (memory, scripts, templates)
- `specs/###-campaign-name/` - Campaign specifications, plans, and tasks
- `src/growthkit/` - Python CLI implementation

## Key Files to Reference
- `.growthkit/memory/constitution.md` - Seven Core Principles and Constitution Check gates
- `specs/001-*/spec.md` - Campaign specifications
- `specs/001-*/plan.md` - Implementation plans
- `specs/001-*/tasks.md` - Task breakdowns

## Available Slash Commands
- `/growthkit.constitution` - Create/update project principles
- `/growthkit.specify` - Generate campaign specification
- `/growthkit.plan` - Create implementation plan
- `/growthkit.tasks` - Generate task breakdown
- `/growthkit.implement` - Execute campaign tasks

## Technology Stack
- **Language**: Python 3.11+
- **CLI Framework**: typer
- **Templating**: Jinja2
- **Git Operations**: gitpython
- **Testing**: pytest

## Growth Hacking Principles
1. **Spec-Driven Growth** - Every campaign starts with measurable specifications
2. **Viral Loop Engineering** - Remix, Integration, or Watermark loops built in
3. **Agent-First Architecture** - Content optimized for LLM citation (Answer Density)
4. **Measurement-First Development** - Primary, activation, engagement metrics upfront
5. **Multi-Platform Distribution** - Platform-specific tactics (X: 16:9, TikTok: 9:16, etc.)
6. **Test-Before-Scale** - Pilot phase (<10% budget) with validation gates
7. **Community-Led Amplification** - Organic reach prioritized over paid ads

## Constitution Check Gates
**Mandatory** (must pass before planning):
- Campaign spec exists
- Growth type identified (Vibe/Trust/Agentic)
- Target audience is specific
- Viral loop mechanism defined
- k-factor target set (>1.1)
- Metrics defined (primary, activation, engagement)
- Pilot phase scoped (<10% budget)

**Advisory** (check after design):
- Content optimized for "Answer Density"
- Platform-specific tactics defined
- Community amplification plan established

## Growth Metrics (2025 Benchmarks)
- **Acceptance Rate**: >30% (AI suggestion acceptance)
- **Time-to-Wow**: <5 minutes (first aha moment)
- **Time-to-Trust**: <7 days (production use)
- **k-factor**: >1.1 (sustainable viral growth)
- **NRR**: 106-120% (expansion revenue)
- **Time-to-First-Share**: <24 hours (social sharing)

## Common Patterns
- **Campaign branching**: `git checkout -b ###-campaign-name`
- **Spec validation**: Check for Constitution Check gate passes
- **Platform tactics**: X/Twitter (30-60s 16:9), TikTok (15-30s 9:16), LinkedIn (case studies)
- **Multi-kit coexistence**: /growthkit.* commands don't conflict with /speckit.* commands

## Notes
- All campaigns should validate against constitution principles before planning
- Pilot phases are mandatory - never scale without validation
- Platform-specific content is required (not generic cross-platform)
EOF

log_success "Updated: $CLAUDE_FILE"

# Create/update .cursor/README.md
CURSOR_README="$PROJECT_ROOT/.cursor/README.md"
mkdir -p "$(dirname "$CURSOR_README")"
cat > "$CURSOR_README" << 'EOF'
# Growth Hacking Kit - Cursor Context

## Quick Start
This project uses Growth Hacking Kit for spec-driven growth campaign management.

Available commands:
- `/growthkit.constitution` - Define project principles
- `/growthkit.specify` - Create campaign spec
- `/growthkit.plan` - Plan campaign implementation
- `/growthkit.tasks` - Generate task breakdown
- `/growthkit.implement` - Execute campaign

See `.growthkit/memory/constitution.md` for governance principles.
See `CLAUDE.md` for detailed context.
EOF

log_success "Created: $CURSOR_README"

# Create/update .windsurf/README.md
WINDSURF_README="$PROJECT_ROOT/.windsurf/README.md"
mkdir -p "$(dirname "$WINDSURF_README")"
cat > "$WINDSURF_README" << 'EOF'
# Growth Hacking Kit - Windsurf Context

## Quick Start
This project uses Growth Hacking Kit for spec-driven growth campaign management.

Available commands:
- `/growthkit.constitution` - Define project principles
- `/growthkit.specify` - Create campaign spec
- `/growthkit.plan` - Plan campaign implementation
- `/growthkit.tasks` - Generate task breakdown
- `/growthkit.implement` - Execute campaign

See `.growthkit/memory/constitution.md` for governance principles.
See `CLAUDE.md` for detailed context.
EOF

log_success "Created: $WINDSURF_README"

log_success "Agent context files updated"
