# Feature Specification: Automated Template Release Generation for Growth Hacking Kit

**Feature Branch**: `004-growthkit-auto-template-release`
**Created**: 2025-12-20
**Status**: Draft
**Input**: Automated template release generation for growthkit with templates from .growthkit/ directory, supporting 17 different AI agents and both bash/PowerShell script variants

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Release Manager Creates New Growth Hacking Kit Release (Priority: P1)

A Growth Hacking Kit maintainer wants to create a new release with templates for all supported AI agents (Claude Code, Cursor, Windsurf, Copilot, Gemini, Qwen, Codex, opencode, Qoder, Kilocode, Auggie, CodeBuddy, Amp, Roo, SHAI, Jules, Amazon Q) using both bash and PowerShell script variants. They should be able to trigger the release process that automatically generates 34 template ZIP files and publishes them to GitHub releases.

**Why this priority**: This is the core capability that enables Growth Hacking Kit to have its own releases and stop relying on Spec-Kit template fallback, ensuring users get growthkit-specific templates with `/growthkit.*` commands and growth-focused constitution.

**Independent Test**: Can be fully tested by triggering the release workflow, verifying all 34 ZIP files are generated correctly, confirming the GitHub release is published with proper naming and versioning, and checking that `growthkit init` downloads growthkit templates (not spec-kit fallback).

**Acceptance Scenarios**:

1. **Given** the maintainer has merged changes to main branch, **When** they push to main (affecting .growthkit/, memory/, scripts/, or templates/ paths), **Then** the automated workflow triggers and generates all template variants
2. **Given** the workflow is running, **When** it processes each agent/script combination, **Then** it creates correctly structured ZIP files with Growth Hacking Kit branding and `/growthkit.*` commands
3. **Given** all templates are generated, **When** the workflow publishes the release, **Then** a GitHub release appears with all 34 ZIP files attached and proper release notes including changelog and SHA-256 checksums
4. **Given** a release is published, **When** users run `growthkit init my-campaign --ai claude`, **Then** the CLI downloads templates from growthkit releases (not spec-kit fallback)

---

### User Story 2 - Developer Tests Template Generation Locally (Priority: P2)

A developer wants to test template generation locally before pushing changes, ensuring their modifications to templates or scripts work correctly across all agent/script combinations without waiting for CI/CD.

**Why this priority**: Enables rapid iteration and validation of template changes, reducing the feedback loop for development.

**Independent Test**: Can be tested by running the local build script and verifying all template ZIPs are created in the dist/ directory with correct structure and content.

**Acceptance Scenarios**:

1. **Given** a developer has modified templates in .growthkit/, **When** they run `./scripts/build-templates.sh`, **Then** all 34 template variants are generated locally in `dist/templates/`
2. **Given** templates are built locally, **When** the developer inspects a ZIP file, **Then** it contains the correct directory structure with agent-specific commands and Growth Hacking Kit branding
3. **Given** a build completes, **When** errors occur in any template, **Then** the script reports which template failed and provides actionable error messages
4. **Given** local testing is complete, **When** the developer commits changes, **Then** CI validation runs the same build process to catch issues before release

---

### User Story 3 - CI System Validates Template Integrity (Priority: P2)

The continuous integration system should validate that all templates are correctly formatted, contain required files from .growthkit/, and have proper Growth Hacking Kit branding before allowing merge to main.

**Why this priority**: Prevents broken or incomplete templates from being released, maintaining quality standards and ensuring all templates follow the specification.

**Independent Test**: Can be tested by triggering CI on a pull request and verifying it checks for required files, validates command references, ensures no Spec-Kit references remain, and confirms growthkit-specific constitution is present.

**Acceptance Scenarios**:

1. **Given** a pull request modifies templates, **When** CI runs validation, **Then** it verifies all templates contain required files (commands from .growthkit/templates/commands/, scripts from .growthkit/scripts/, constitution from .growthkit/memory/)
2. **Given** CI is validating templates, **When** it finds `/speckit.*` references that should be `/growthkit.*`, **Then** the build fails with clear error messages
3. **Given** CI validation passes, **When** templates are generated, **Then** automated tests extract and verify the structure of each ZIP file
4. **Given** all validations pass, **When** maintainer merges the PR, **Then** the changes are ready for the next release

---

### Edge Cases

- What happens if a template ZIP fails to generate for one agent but succeeds for others? (Should fail the entire build and report which agent failed)
- How does the system handle version numbering when multiple releases happen on the same day? (Use Git commit hash and timestamp for uniqueness)
- What if the GitHub API rate limit is exceeded during release publication? (Implement retry logic with exponential backoff)
- How are templates validated to ensure no Spec-Kit references remain and all .growthkit/ content is included? (Regex scanning for /speckit references and file manifest validation)
- What happens if the release workflow is triggered but no templates have changed? (Skip release creation and report as no-op)
- How does the system handle migration if .growthkit/ structure changes in future versions? (Document in migration guide, provide upgrade path in build script)

## Requirements *(mandatory)*

### Functional Requirements

#### Template Generation

- **FR-001**: System MUST generate template variants for all 17 supported AI agents: claude, cursor-agent, windsurf, copilot, gemini, qwen, codex, opencode, qoder, kilocode, auggie, codebuddy, amp, roo, shai, jules, q
- **FR-002**: System MUST generate both bash (sh) and PowerShell (ps) script variants for each agent, resulting in 34 total template combinations (17 agents × 2 script types)
- **FR-003**: Each template MUST include agent-specific command directory (e.g., `.claude/commands/`, `.cursor/commands/`, `.windsurf/commands/`)
- **FR-004**: Each template MUST contain Growth Hacking Kit specific files from .growthkit/ directory: constitution.md from .growthkit/memory/, growth-focused spec/plan/tasks templates from .growthkit/templates/, and growth-specific command files from .growthkit/templates/commands/
- **FR-005**: All agent command files MUST use `/growthkit.*` command prefix (not `/speckit.*`)
- **FR-006**: Template naming MUST follow pattern: `growthkit-template-{agent}-{script}-v{version}.zip` for consistency with growthkit CLI expectations
- **FR-007**: Each template ZIP MUST contain proper directory structure: `.{agent}/commands/`, `.growthkit/templates/`, `.growthkit/scripts/{bash|powershell}/`, `.growthkit/memory/` with growthkit-specific files

#### Build System

- **FR-008**: System MUST provide local build script (`scripts/build-templates.sh`) that generates all 34 template variants in `dist/templates/` directory
- **FR-009**: Build script MUST copy content from .growthkit/ source directory into proper structure in generated templates
- **FR-010**: Build script MUST be idempotent and support incremental rebuilds
- **FR-011**: Build script MUST validate template structure before creating ZIP files
- **FR-012**: Build script MUST report progress and any errors encountered during generation
- **FR-013**: Build script MUST calculate and verify SHA-256 checksums for each generated ZIP file
- **FR-014**: Build script MUST support both bash and PowerShell execution environments

#### GitHub Actions Workflow

- **FR-015**: System MUST provide GitHub Actions workflow (`.github/workflows/release.yml`) that triggers on push to main when .growthkit/, memory/, scripts/, or templates/ paths are modified
- **FR-016**: Workflow MUST execute the build script to generate all template variants
- **FR-017**: Workflow MUST create a GitHub release with generated templates as release assets
- **FR-018**: Workflow MUST generate release notes that include changelog, template list, and SHA-256 checksums
- **FR-019**: Workflow MUST support manual triggering via `workflow_dispatch` for testing and hotfixes
- **FR-020**: Workflow MUST extract version from git tag or package version

#### Template Validation

- **FR-021**: System MUST provide validation script (`scripts/validate-templates.sh`) that verifies template integrity
- **FR-022**: Validation MUST check for presence of required files in each template: command files from .growthkit/templates/commands/, templates from .growthkit/templates/, scripts from .growthkit/scripts/
- **FR-023**: Validation MUST scan for unintended `/speckit.*` references that should be `/growthkit.*`
- **FR-024**: Validation MUST verify agent command frontmatter uses correct `agent: growthkit.{command}` format
- **FR-025**: Validation MUST confirm all templates reference Growth Hacking Kit (not Spec-Kit) in branding and documentation
- **FR-026**: Validation MUST verify Growth Hacking Kit constitution (v1.1.0 with Seven Core Principles) is present in templates
- **FR-027**: Validation MUST check that all platform research references (Twitter, TikTok, LinkedIn, GitHub, Product Hunt) are present

#### CI Integration

- **FR-028**: System MUST provide CI workflow (`.github/workflows/ci.yml`) that runs on pull requests
- **FR-029**: CI MUST execute template validation before allowing merge
- **FR-030**: CI MUST build all templates to ensure they can be generated successfully
- **FR-031**: CI MUST fail if any template contains Spec-Kit references or missing required files from .growthkit/
- **FR-032**: CI MUST perform linting on shell scripts and PowerShell scripts to ensure quality

### Key Entities

- **Template Variant**: A combination of agent type and script type (e.g., claude-sh, cursor-ps), resulting in 34 unique variants
- **Agent Configuration**: Metadata for each supported agent including name, command directory name, and whether it requires CLI tools
- **Template ZIP**: A compressed archive containing all files needed for a specific agent/script combination
- **Release Asset**: A ZIP file attached to a GitHub release with versioned naming and SHA-256 checksum
- **Build Manifest**: JSON file documenting all generated templates with metadata (agent, script, size, checksum, timestamp)
- **Template Base**: Source directory structure (.growthkit/) containing Growth Hacking Kit specific files before agent/script customization
- **Command File**: Markdown file with YAML frontmatter that defines a `/growthkit.*` slash command for AI agents
- **Growth Constitution**: Growth Hacking Kit constitution (v1.1.0) from .growthkit/memory/constitution.md defining seven core growth principles

## Success Criteria *(mandatory)*

### Measurable Outcomes

#### Release Automation Success

- **SC-001**: Maintainer can create a new release by pushing changes to main (affecting .growthkit/ paths), with full automation completing in under 10 minutes
- **SC-002**: Each release generates exactly 34 template ZIP files (17 agents × 2 script types) with correct naming and structure
- **SC-003**: GitHub release page displays all templates with proper versioning, release notes, and SHA-256 checksums
- **SC-004**: After release, `growthkit init` command successfully downloads templates from growthkit repository (not spec-kit fallback)
- **SC-005**: Release process is fully automated and requires zero manual file uploads or versioning

#### Template Quality

- **SC-006**: 100% of generated templates pass validation checks: correct structure, required files from .growthkit/ present, no Spec-Kit references
- **SC-007**: All templates contain `/growthkit.*` command references (zero `/speckit.*` references remain)
- **SC-008**: Each template includes Growth Hacking Kit constitution v1.1.0 with seven core growth principles from .growthkit/memory/constitution.md
- **SC-009**: Templates extract successfully and create functional growth campaign projects when used with `growthkit init`
- **SC-010**: All templates contain growth-specific research documents (platform specs, viral loop mechanics, metrics dashboards)

#### Developer Experience

- **SC-011**: Developers can build all templates locally in under 5 minutes using `./scripts/build-templates.sh`
- **SC-012**: Local builds produce identical results to CI builds (reproducible builds with same checksums)
- **SC-013**: CI validation catches template issues before merge, with 95% of problems detected before release
- **SC-014**: Build script provides clear, actionable error messages when template generation fails

#### Platform Support

- **SC-015**: All 17 supported AI agents have properly configured templates with agent-specific command directories
- **SC-016**: Both bash and PowerShell scripts are generated and validated for all agents
- **SC-017**: Users on Linux/macOS can use bash templates, Windows users can use PowerShell templates

## Assumptions

1. **Template Source**: All source files are in `.growthkit/` directory structure (constitution.md, templates/, scripts/, memory/)
2. **Naming Convention**: Template ZIPs follow `growthkit-template-{agent}-{script}-v{version}.zip` pattern for CLI expectations
3. **Version Source**: Version number comes from git tags (e.g., v0.1.0) or from package version in pyproject.toml
4. **Agent Support**: The 17 agents listed are stable and will not change frequently; changes would be documented in migration guide
5. **Build Environment**: Local builds assume bash/sh shell and POSIX tools available; CI assumes GitHub Actions runners with standard tools
6. **Storage**: Generated templates are stored as GitHub release assets (no separate S3 or artifact storage needed)
7. **CI Triggers**: Changes to .growthkit/ directory trigger release workflow; other changes don't trigger releases
8. **Script Distribution**: PowerShell scripts are for Windows users; bash scripts for Linux/macOS; both are generated for all agents
9. **Backward Compatibility**: growthkit CLI can fall back to spec-kit templates if growthkit templates not found (graceful degradation)
10. **Documentation**: All growth-specific documentation (constitution, viral loop mechanics, platform research) is included in templates

## Notes & Clarifications

- Template generation mirrors the successful blogkit release pattern (specs/003-blogkit-auto-template-release)
- Key difference from blogkit: growthkit serves growth campaigns, so constitution and templates focus on growth metrics, viral loops, and platform-specific tactics
- All 17 AI agents should be supported consistently with their command directory naming conventions
- PowerShell scripts are essential for Windows users to have native command environment

---

**Created**: 2025-12-20
**Status**: Ready for clarification and planning phases
**Next Step**: Run `/growthkit.clarify` to address any ambiguities, then `/growthkit.plan` for technical design
