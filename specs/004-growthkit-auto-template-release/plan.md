# Implementation Plan: Automated Growth-Hacking-Kit Template Release Generation

**Feature**: Automated template release generation for 17 AI agents with Growth Hacking Kit templates
**Branch**: 004-growthkit-auto-template-release
**Created**: 2025-12-24
**Status**: Design Phase

---

## Executive Summary

This plan implements automated generation and publication of 34 Growth Hacking Kit template variants (17 AI agents × 2 script types) to GitHub releases, triggered by git tags. The system adapts Blog-Tech-Kit's proven release infrastructure to generate Growth-Hacking-Kit branded templates with `/growthkit.*` commands, sourcing content from `.growthkit/` directory.

**Key Objectives**:
1. Generate 34 template ZIP files with Growth Hacking Kit branding and commands from `.growthkit/` source
2. Automate release creation on git tag pushes (e.g., `v0.2.0`)
3. Validate templates ensure no Spec-Kit references remain
4. Publish to GitHub releases with checksums and release notes
5. Optimize CLI installation with "Growth Hacking Kit" ASCII graphics

**Success Criteria**:
- `growthkit init` downloads templates from growth-hacking-kit repository
- All templates pass validation (correct namespace, required files from `.growthkit/`, no spec-kit references)
- Release generation completes in under 10 minutes
- Local build script allows testing before CI
- CLI displays "Growth Hacking Kit" ASCII banner on initialization

**Critical Distinction**: Templates are sourced from `.growthkit/` and packaged into `.growthkit/` working directory structure, enabling multi-kit coexistence.

---

## Technical Context

### Source Architecture

**Growth-Hacking-Kit Source Structure** (`.growthkit/` directory):
```
.growthkit/
├── memory/
│   └── constitution.md           # Growth Hacking Kit constitution v1.1.0
├── scripts/
│   └── bash/
│       ├── common.sh
│       ├── setup-plan.sh
│       ├── check-prerequisites.sh
│       ├── update-agent-context.sh
│       ├── setup-agent-commands.sh
│       └── create-new-feature.sh
├── templates/
│   ├── spec-template.md
│   ├── plan-template.md
│   ├── tasks-template.md
│   └── commands/
│       ├── growthkit-constitution.md
│       ├── growthkit-specify.md
│       ├── growthkit-plan.md
│       ├── growthkit-tasks.md
│       └── growthkit-implement.md
```

**Target Template Structure** (extracted by `growthkit init`):
```
project-root/
├── .growthkit/                    # Shared working directory
│   ├── memory/
│   │   └── constitution.md       # From .growthkit/memory/constitution.md
│   ├── scripts/
│   │   ├── bash/                 # From .growthkit/scripts/bash/
│   │   │   ├── common.sh
│   │   │   ├── setup-plan.sh
│   │   │   └── ...
│   │   └── powershell/           # (for ps variants)
│   └── templates/
│       ├── spec-template.md      # From .growthkit/templates/
│       ├── plan-template.md
│       └── tasks-template.md
└── .{agent}/                      # e.g., .claude/
    └── commands/
        ├── growthkit-constitution.md
        ├── growthkit-specify.md
        ├── growthkit-plan.md
        └── ...                   # All from .growthkit/templates/commands/
```

### Existing Infrastructure Analysis

**Current State** (from Blog-Tech-Kit reference and codebase):

1. **GitHub Actions Workflow** (`.github/workflows/release.yml` exists):
   - Currently triggers on git tags (`v*`)
   - Runs tests, builds Python package, publishes to PyPI
   - Creates GitHub release
   - **NEEDS MODIFICATION**: Add template generation step before release

2. **Build Script Pattern** (to be created, based on Blog-Tech-Kit):
   - Generates templates for 17 agents (claude, gemini, copilot, cursor-agent, qwen, opencode, windsurf, codex, kilocode, auggie, roo, codebuddy, amp, shai, q, jules, qoder)
   - Supports both bash (sh) and PowerShell (ps) variants
   - Uses `.genreleases/` directory for build artifacts
   - Implements `generate_commands()` function to transform templates
   - **KEY**: use `.growthkit/` source in generated templates

3. **Template Sources** (existing in `.growthkit/`):
   - `.growthkit/memory/constitution.md` - Growth Hacking Kit v1.1.0 constitution
   - `.growthkit/templates/` - Template files (spec, plan, tasks)
   - `.growthkit/scripts/bash/` - Bash scripts only (no PowerShell variants yet)
   - `.growthkit/templates/commands/*.md` - Command templates with YAML frontmatter

4. **CLI Integration** (existing in `src/growthkit/cli/`):
   - `growthkit init` command scaffolds projects
   - Currently creates basic directory structure
   - **NEEDS**: Download template functionality from GitHub releases
   - **NEEDS**: "Growth Hacking Kit" ASCII banner

### Technology Stack

- **Build Tool**: Bash (v4.0+) with standard Unix utilities (sed, awk, grep, zip)
- **CI/CD**: GitHub Actions (ubuntu-latest runner)
- **Release Platform**: GitHub Releases API
- **Version Control**: Git with semantic versioning
- **Archive Format**: ZIP with SHA-256 checksums
- **CLI Framework**: Python 3.11+ with Typer and Rich

### Dependencies

**Required**:
- Bash shell with arrays and modern syntax
- `zip` utility for archive creation
- Git for versioning and changelog generation
- GitHub CLI (`gh`) for release creation (available in Actions)
- Standard Unix text processing tools (sed, awk, grep)
- Python 3.11+ for CLI enhancements

**Optional**:
- PowerShell for testing ps variants on Windows

### Key Design Decisions

1. **Trigger on git tags**: Release workflow triggers on `v*` tags (matches existing pattern)
2. **Use `/growthkit.*` namespace**: Prevents conflicts with spec-kit, pmf-kit, blog-kit
3. **Source from `.growthkit/`, package to `.growthkit/`**: Per constitution multi-kit coexistence strategy
4. **Bash for all scripts**: Matches existing infrastructure
5. **Auto-extract version from git tags**: Use tag name as version (e.g., `v0.2.0`)
6. **Validate before release**: Multi-phase validation prevents bad releases
7. **17 agents × 2 scripts = 34 variants**: Comprehensive agent support

---

## Constitution Check

### Principle I: Data-Driven Growth Experimentation ✅

**Compliance**: Feature enables A/B testing of different template structures across platforms
**Evidence**: Automated release infrastructure allows rapid iteration on campaign templates
**Application**: Release automation enables quick testing of template effectiveness

### Principle II: Platform-Specific Optimization ✅

**Compliance**: Templates sourced from `.growthkit/` contain platform-specific growth tactics
**Evidence**:
- Constitution from `.growthkit/memory/constitution.md` includes platform optimization principles
- Templates support 17 different AI agent platforms
- Bash and PowerShell variants for cross-platform compatibility

### Principle III: Viral Loop Engineering (NON-NEGOTIABLE) ✅

**Compliance**: Templates include viral loop mechanics and sharing incentives
**Evidence**:
- Growth Hacking Kit constitution v1.1.0 defines viral loop principles
- Templates support growth campaign structure
- Release automation enables rapid viral loop testing

### Principle VII: Rapid Iteration & Learning ✅

**Compliance**: Reuses Blog-Tech-Kit release infrastructure patterns, enables quick updates
**Evidence**:
- Adapts proven workflow structure
- No new external dependencies
- Simple bash scripts instead of complex frameworks
- Git tag triggers allow immediate releases after changes

### Multi-Kit Namespace Isolation ✅

**Compliance**: **CRITICAL FOR THIS FEATURE** - Uses `/growthkit.*` namespace throughout
**Evidence**:
- FR-005: "All agent command files MUST use `/growthkit.*` command prefix"
- FR-024: "Validation MUST verify agent command frontmatter uses correct `agent: growthkit.{command}` format"
- FR-023: "Validation MUST scan for unintended `/speckit.*` references"

**Validation Gate**: Templates MUST pass namespace validation before release

---

## Architecture Overview

### System Components

```

 GitHub Actions Workflow (.github/workflows/release.yml)
 Trigger: Git tag push (v*)
            ,

               > Step 1: Run Tests
                 Run pytest to ensure kit quality

               > Step 2: Build Python Package
                 Build and publish to PyPI

               > Step 3: Build Template Variants (NEW)
                 Script: create-release-packages.sh

                  For each agent in 17 agents:
                    For each script in [sh, ps]:
                      1. Create .growthkit/ structure
                      2. Copy from .growthkit/memory/,
                         .growthkit/scripts/, .growthkit/templates/
                      3. Generate command files
                      4. Create agent directory
                      5. ZIP the structure
                      6. Calculate SHA-256

                 Output: 34 ZIP files in .genreleases/

               > Step 4: Validate Templates (NEW)
                 Script: validate-templates.sh
                 Checks:
                   - Frontmatter uses growthkit.* namespace
                   - No /speckit.* references in content
                   - Required files from .growthkit/ present
                   - Directory structure correct (.growthkit/ working dir)
                 Output: PASS/FAIL

               > Step 5: Create GitHub Release
                 Upload 34 ZIP files + Python package
                 Generate release notes with checksums
```

### Build Process Detail

```
Template Build Flow (per variant):

Source Files                    Build Process                    Output


.growthkit/
  memory/
    constitution.md

  templates/
    spec-template.md
    plan-template.md                   ,
    tasks-template.md
    ...

  scripts/                                        .growthkit/
    bash/                                           memory/
      common.sh                                     scripts/
      create-new-feature.sh               $          templates/
      setup-plan.sh
      ...
  (no powershell/ yet - need to create)
                            <

  templates/commands/
    growthkit-constitution.md
    growthkit-plan.md
    growthkit-tasks.md                    > generate_commands()
    growthkit-implement.md                  - Extract frontmatter
    growthkit-specify.md                    - Replace {SCRIPT}
                                            - Rewrite paths
                                            - Set namespace
                                 ,

                                         4
                               .{agent}/commands/
                                 growthkit-specify.md
                                 growthkit-plan.md
                                 growthkit-tasks.md
                                 growthkit-implement.md
                                 growthkit-constitution.md


                                         4

                           zip -r growthkit-template-
                             {agent}-{script}-{ver}.zip
                                      ,

                                       4
                       growthkit-template-claude-sh-v0.2.0.zip
                                (45.2 KB)
                    sha256:3f8b9e72d1a4c...
```

---

## Phase 0: Research & Design

**Status**: COMPLETED (spec.md and plan.md in progress)
**Duration**: 0.5 days
**Outputs**: plan.md (this document)

### Research Tasks

✅ **R1: Review Blog-Tech-Kit release process**
- Analyzed specs/003-blogkit-auto-template-release/ thoroughly
- Identified adaptable patterns
- Documented Growth Hacking Kit specific changes needed

✅ **R2: Verify .growthkit/ directory contents**
- Confirmed 5 bash scripts present
- Confirmed 3 template files present
- Confirmed 5 command files present with growthkit-* naming
- **GAP IDENTIFIED**: No PowerShell script variants (need to create)

✅ **R3: Document Growth Hacking Kit constitution requirements**
- Read .growthkit/memory/constitution.md v1.1.0
- Identified multi-kit coexistence requirements
- Documented .growthkit/ → .growthkit/ packaging strategy

✅ **R4: Analyze existing CLI structure**
- CLI uses Typer framework with Rich for formatting
- `growthkit init` exists but doesn't download templates yet
- No ASCII banner currently displayed

**Deliverables**:
- ✅ plan.md: Technology decisions and Blog-Tech-Kit adaptations (this document)

---

## Phase 1: PowerShell Scripts Creation

**Goal**: Enable ps template variants by creating PowerShell equivalents
**Duration**: 0.5 days
**Dependencies**: Phase 0 complete

### Tasks

#### Task 1.1: Create PowerShell Script Directory

**File**: `.growthkit/scripts/powershell/` (new directory)
**Purpose**: Enable ps variants by creating PowerShell equivalents of bash scripts

**Requirements**:
- Create `.growthkit/scripts/powershell/` directory
- Port `common.sh` → `common.ps1`
- Port `setup-plan.sh` → `setup-plan.ps1`
- Port `check-prerequisites.sh` → `check-prerequisites.ps1`
- Port `create-new-feature.sh` → `create-new-feature.ps1`
- Port `update-agent-context.sh` → `update-agent-context.ps1`
- Port `setup-agent-commands.sh` → `setup-agent-commands.ps1`

**Acceptance Criteria**:
- ✅ All 6 bash scripts have PowerShell equivalents
- ✅ Scripts use PowerShell conventions ($Args, Param blocks)
- ✅ Path references use `.growthkit/` working directory
- ✅ Scripts have no syntax errors

---

## Phase 2: Build Infrastructure

**Goal**: Create template generation scripts
**Duration**: 1.5 days
**Dependencies**: Phase 1 complete

### Tasks

#### Task 2.1: Create GitHub Workflows Scripts Directory

**Files**: `.github/workflows/scripts/` directory with build scripts
**Purpose**: Modular scripts for template generation

**Scripts to Create**:
1. `create-release-packages.sh` - Core template generation (~400 lines)
2. `generate-release-notes.sh` - Release notes with checksums (~100 lines)
3. `validate-templates.sh` - Template quality validation (~300 lines)

#### Task 2.2: Implement create-release-packages.sh

**Key Functions**:
1. `build_variant()`: Create single template variant
   - Copy from `.growthkit/` source to `.growthkit/` target
   - Generate agent-specific commands
   - Create ZIP archive
   - Calculate SHA-256 checksum

2. `generate_commands()`: Transform growthkit-*.md templates
   - Extract YAML frontmatter
   - Replace `__AGENT__` placeholder with `growthkit.{command}`
   - Replace `{SCRIPT}` placeholder with bash or powershell
   - Write to agent directory

3. `main()`: Loop through all agent/script combinations

**Agent Configurations**:
```bash
ALL_AGENTS=(
  claude cursor-agent windsurf gemini copilot qwen codex opencode
  qoder kilocode auggie roo codebuddy amp shai jules q
)

# Agent-specific directory mappings
case "$agent" in
  claude) mkdir -p "$base_dir/.claude/commands" ;;
  cursor-agent) mkdir -p "$base_dir/.cursor/commands" ;;
  windsurf) mkdir -p "$base_dir/.windsurf/commands" ;;
  gemini) mkdir -p "$base_dir/.gemini/commands" ;;
  copilot) mkdir -p "$base_dir/.github/agents" "$base_dir/.github/prompts" ;;
  # ... etc for all 17 agents
esac
```

**Acceptance Criteria**:
- ✅ Script generates 34 ZIP files (17 agents × 2 scripts)
- ✅ Each ZIP contains .growthkit/ working directory structure
- ✅ Constitution copied from .growthkit/memory/ to .growthkit/memory/
- ✅ Templates copied from .growthkit/templates/ to .growthkit/templates/
- ✅ Scripts copied from .growthkit/scripts/{bash|powershell}/
- ✅ Agent commands generated from .growthkit/templates/commands/

---

## Phase 3: Validation Infrastructure

**Goal**: Ensure template quality before release
**Duration**: 1 day
**Dependencies**: Phase 2 complete

### Tasks

#### Task 3.1: Create Template Validation Script

**File**: `scripts/validate-templates.sh`
**Purpose**: Automated validation of template quality

**Validation Checks**:
1. **Frontmatter Namespace Check**: Verify all commands use `agent: growthkit.*`
2. **Required Files Check**: Verify files from .growthkit/ are present in .growthkit/
3. **Content Scanning**: Search for `/speckit.` or `/pmfkit.` or `/blogkit.` references
4. **Directory Structure Validation**: Verify .growthkit/ working directory exists
5. **Constitution Version Check**: Verify Growth Hacking Kit constitution v1.1.0
6. **Script Consistency**: Ensure sh has bash/, ps has powershell/
7. **Command Count**: Verify 5 required commands present
8. **ZIP Integrity**: Test ZIP extracts without errors

**Acceptance Criteria**:
- ✅ Script validates all required checks
- ✅ Returns exit code 0 on success, non-zero on failure
- ✅ Provides clear error messages
- ✅ Can validate 34 variants in under 2 minutes

---

## Phase 4: CI/CD Integration

**Goal**: Integrate template generation into existing release workflow
**Duration**: 1 day
**Dependencies**: Phase 3 complete

### Tasks

#### Task 4.1: Update GitHub Actions Release Workflow

**File**: `.github/workflows/release.yml` (modify existing)
**Purpose**: Add template generation step to existing release workflow

**Changes to Existing Workflow**:
```yaml
jobs:
  test:
    # ... existing test job ...

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      # ... existing Python package build steps ...

      # NEW: Build template variants
      - name: Build template variants
        run: |
          chmod +x .github/workflows/scripts/create-release-packages.sh
          .github/workflows/scripts/create-release-packages.sh ${{ github.ref_name }}

      # NEW: Validate templates
      - name: Validate templates
        run: |
          chmod +x scripts/validate-templates.sh
          ./scripts/validate-templates.sh .genreleases/

      # NEW: Generate release notes with template checksums
      - name: Generate release notes
        run: |
          chmod +x .github/workflows/scripts/generate-release-notes.sh
          .github/workflows/scripts/generate-release-notes.sh ${{ github.ref_name }}

      # ... existing PyPI publish step ...

  release:
    needs: build
    runs-on: ubuntu-latest
    steps:
      # MODIFY: Upload template ZIPs in addition to source archives
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          body_path: release_notes.md  # Changed from CHANGELOG.md
          draft: false
          prerelease: false

      # NEW: Upload template assets
      - name: Upload template assets
        run: |
          for zip in .genreleases/*.zip; do
            gh release upload ${{ github.ref_name }} "$zip"
          done
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Acceptance Criteria**:
- ✅ Workflow triggers on git tag push
- ✅ Validation step blocks release if errors
- ✅ All 34 templates uploaded to GitHub release
- ✅ Release notes include template checksums

---

## Phase 5: CLI Enhancements

**Goal**: Optimize CLI installation with template download and ASCII banner
**Duration**: 1 day
**Dependencies**: Phase 4 complete

### Tasks

#### Task 5.1: Add Template Download Functionality

**File**: `src/growthkit/cli/utils.py` (modify/add)
**Purpose**: Download templates from GitHub releases during `growthkit init`

**Functions to Add**:
1. `download_template_from_github()`: Download template ZIP from latest release
2. `extract_template()`: Extract ZIP to project directory
3. `get_latest_release_version()`: Get latest release version from GitHub API

**Integration into `growthkit init`**:
```python
# After detecting AI agent
if ai:
    console.print(f"[cyan]Downloading Growth Hacking Kit templates for {ai}...[/cyan]")

    # Determine script type (bash or powershell)
    script_type = "ps" if sys.platform == "win32" else "sh"

    # Download template
    template_zip = download_template_from_github(
        agent=ai,
        script=script_type,
        github_token=github_token,
        skip_tls=skip_tls
    )

    # Extract template
    extract_template(template_zip, project_dir)

    console.print("[green]✓[/green] Templates installed")
```

**Acceptance Criteria**:
- ✅ `growthkit init` downloads templates from growth-hacking-kit releases
- ✅ Falls back gracefully if release not found
- ✅ Supports both bash and PowerShell templates
- ✅ Respects --skip-tls and --github-token flags

#### Task 5.2: Add ASCII Banner

**File**: `src/growthkit/cli/main.py` (modify init command)
**Purpose**: Display "Growth Hacking Kit" ASCII graphics on initialization

**ASCII Banner Design**:
```
   ____                   _   _       _   _            _    _             _  ___ _
  / ___|_ __ _____      _| |_| |__   | | | | __ _  ___| | _(_)_ __   __ _| |/ (_) |_
 | |  _| '__/ _ \ \ /\ / / __| '_ \  | |_| |/ _` |/ __| |/ / | '_ \ / _` | ' /| | __|
 | |_| | | | (_) \ V  V /| |_| | | | |  _  | (_| | (__|   <| | | | | (_| | . \| | |_
  \____|_|  \___/ \_/\_/  \__|_| |_| |_| |_|\__,_|\___|_|\_\_|_| |_|\__, |_|\_\_|\__|
                                                                     |___/
                          Spec-Driven Growth Campaign Management
```

**Implementation**:
```python
def print_banner():
    banner = """
   ____                   _   _       _   _            _    _             _  ___ _
  / ___|_ __ _____      _| |_| |__   | | | | __ _  ___| | _(_)_ __   __ _| |/ (_) |_
 | |  _| '__/ _ \\ \\ /\\ / / __| '_ \\  | |_| |/ _` |/ __| |/ / | '_ \\ / _` | ' /| | __|
 | |_| | | | (_) \\ V  V /| |_| | | | |  _  | (_| | (__|   <| | | | | (_| | . \\| | |_
  \\____|_|  \\___/ \\_/\\_/  \\__|_| |_| |_| |_|\\__,_|\\___|_|\\_\\_|_| |_|\\__, |_|\\_\\_|\\__|
                                                                     |___/
                          Spec-Driven Growth Campaign Management
    """
    console.print(f"[bold cyan]{banner}[/bold cyan]")

@app.command()
def init(...):
    print_banner()  # Display banner first
    console.print("[bold cyan]Growth Hacking Kit[/bold cyan] - Initializing project...")
    # ... rest of init logic ...
```

**Acceptance Criteria**:
- ✅ ASCII banner displays on `growthkit init`
- ✅ Banner clearly reads "Growth Hacking Kit"
- ✅ Formatted with proper spacing and color
- ✅ Does not break on narrow terminals (graceful degradation)

---

## Phase 6: Testing & Documentation

**Goal**: Validate full system and document for users
**Duration**: 1 day
**Dependencies**: Phase 5 complete

### Tasks

#### Task 6.1: End-to-End Testing

**Test Scenarios**:
1. Create test release with git tag
2. Verify GitHub Actions workflow completes
3. Verify all 34 templates uploaded
4. Test `growthkit init` downloads templates
5. Verify ASCII banner displays correctly
6. Validate no spec-kit/pmf-kit/blog-kit references remain

**Acceptance Criteria**:
- ✅ Full release workflow completes in under 10 minutes
- ✅ All templates pass validation
- ✅ CLI successfully scaffolds projects with downloaded templates
- ✅ ASCII banner displays correctly

#### Task 6.2: Update Documentation

**Files to Update**:
- `README.md`: Add templates section and ASCII banner screenshot
- `CONTRIBUTING.md`: Add template testing instructions
- `docs/templates.md` (new): Template structure and command reference

**Acceptance Criteria**:
- ✅ README mentions Growth Hacking Kit templates
- ✅ Template structure documented
- ✅ All 17 agents listed with directory structures
- ✅ Release process documented for maintainers

---

## Success Metrics

### Quantitative Metrics

1. **Build Success Rate**: >99% of builds complete without errors
2. **Validation Pass Rate**: 100% of templates pass validation before release
3. **Release Generation Time**: <10 minutes from tag to published release
4. **CLI Download Success**: >95% of `growthkit init` commands succeed
5. **Template Consistency**: 100% use growthkit.* namespace

---

## Future Enhancements (Out of Scope)

1. **Automated PowerShell Generation**: Generate .ps1 from .sh automatically
2. **Template Customization UI**: Allow users to customize templates before download
3. **Differential Updates**: Only regenerate templates that changed
4. **Template Analytics**: Track which agents are most popular

---

**Plan Version**: 1.0
**Last Updated**: 2025-12-24
**Status**: Ready for Task Generation
