# Tasks: Automated Growth-Hacking-Kit Template Release Generation

**Feature**: Automated template release generation for 17 AI agents with Growth Hacking Kit templates
**Branch**: 004-growthkit-auto-template-release
**Created**: 2025-12-24
**Status**: Ready for Implementation

---

## Task Organization

Tasks are organized by user story (from spec.md) to enable independent implementation and testing. Each phase represents a complete, independently testable increment of functionality.

**User Story Mapping**:
- **Phase 1**: Setup (Project infrastructure)
- **Phase 2**: Foundational (Prerequisites for all user stories)
- **Phase 3**: User Story 1 (P1) - Release Manager Creates New Release
- **Phase 4**: User Story 2 (P2) - Developer Tests Templates Locally
- **Phase 5**: User Story 3 (P2) - CI System Validates Template Integrity
- **Phase 6**: Polish & Cross-Cutting Concerns

---

## Phase 1: Setup (Project Infrastructure)

**Goal**: Establish foundational infrastructure for template generation
**Duration**: 0.5 days
**Dependencies**: None

### Setup Tasks

- [X] T001 Verify .growthkit/ directory structure contains all required files in .growthkit/memory/, .growthkit/templates/, .growthkit/scripts/bash/
- [X] T002 Create .growthkit/scripts/powershell/ directory for PowerShell script variants
- [X] T003 Port common.sh to common.ps1 in .growthkit/scripts/powershell/
- [X] T004 Port setup-plan.sh to setup-plan.ps1 in .growthkit/scripts/powershell/
- [X] T005 Port check-prerequisites.sh to check-prerequisites.ps1 in .growthkit/scripts/powershell/
- [X] T006 Port create-new-feature.sh to create-new-feature.ps1 in .growthkit/scripts/powershell/
- [X] T007 Port update-agent-context.sh to update-agent-context.ps1 in .growthkit/scripts/powershell/
- [X] T008 Port setup-agent-commands.sh to setup-agent-commands.ps1 in .growthkit/scripts/powershell/
- [X] T009 Create .github/workflows/scripts/ directory for modular build scripts
- [X] T010 Create scripts/ directory in repo root for local development scripts

**Validation Checkpoint**:
- ✅ All 6 bash scripts have PowerShell equivalents
- ✅ PowerShell scripts use proper conventions ($Args, Param blocks, $ErrorActionPreference)
- ✅ Path references use .growthkit/ working directory
- ✅ Scripts have no syntax errors (validated with PowerShell parser if available)

---

## Phase 2: Foundational (Template Build Infrastructure)

**Goal**: Create core template generation scripts that all user stories depend on
**Duration**: 1.5 days
**Dependencies**: Phase 1 complete

### Foundational Tasks

- [X] T011 Implement create-release-packages.sh with main() loop for 17 agents × 2 scripts in .github/workflows/scripts/create-release-packages.sh
- [X] T012 Implement build_variant() function to create single template variant with .growthkit/ structure in .github/workflows/scripts/create-release-packages.sh
- [X] T013 Implement generate_commands() function to transform growthkit-*.md templates with namespace replacement in .github/workflows/scripts/create-release-packages.sh
- [X] T014 Add agent directory mappings for all 17 agents (claude, cursor-agent, windsurf, gemini, copilot, qwen, codex, opencode, qoder, kilocode, auggie, roo, codebuddy, amp, shai, jules, q) in .github/workflows/scripts/create-release-packages.sh
- [X] T015 Implement ZIP creation and SHA-256 checksum calculation in .github/workflows/scripts/create-release-packages.sh
- [X] T016 Add progress reporting and error handling with clear messages in .github/workflows/scripts/create-release-packages.sh
- [X] T017 Implement generate-release-notes.sh to create release notes with changelog and checksums in .github/workflows/scripts/generate-release-notes.sh
- [X] T018 Implement validate-templates.sh with frontmatter namespace validation in scripts/validate-templates.sh
- [X] T019 Add required files check to validate .growthkit/ structure in scripts/validate-templates.sh
- [X] T020 Add content scanning for /speckit.*, /pmfkit.*, /blogkit.* references in scripts/validate-templates.sh
- [X] T021 Add directory structure validation to verify .growthkit/ working directory in scripts/validate-templates.sh
- [X] T022 Add constitution version check for Growth Hacking Kit v1.1.0 in scripts/validate-templates.sh
- [X] T023 Add script consistency check (sh has bash/, ps has powershell/) in scripts/validate-templates.sh
- [X] T024 Add command count validation (5 required commands) in scripts/validate-templates.sh
- [X] T025 Add ZIP integrity check to verify extraction works in scripts/validate-templates.sh

**Validation Checkpoint**:
- ✅ create-release-packages.sh generates 34 ZIP files (17 agents × 2 scripts)
- ✅ Each ZIP contains .growthkit/ working directory structure
- ✅ Constitution copied from .growthkit/memory/ to .growthkit/memory/
- ✅ Templates copied from .growthkit/templates/ to .growthkit/templates/
- ✅ Scripts copied from .growthkit/scripts/{bash|powershell}/
- ✅ Agent commands generated from .growthkit/templates/commands/
- ✅ validate-templates.sh returns exit code 0 for valid templates, non-zero for invalid

---

## Phase 3: User Story 1 - Release Manager Creates New Release (P1)

**Goal**: Enable automated release creation with all 34 template variants
**Duration**: 2 days
**Dependencies**: Phase 2 complete

**Independent Test**: Trigger release workflow by pushing git tag, verify all 34 ZIP files generated, confirm GitHub release published with proper naming and checksums, check `growthkit init` downloads growthkit templates.

### US1 Implementation Tasks

- [X] T026 [US1] Backup existing .github/workflows/release.yml as .github/workflows/release.yml.backup
- [X] T027 [US1] Update release.yml to add build template variants step after Python package build in .github/workflows/release.yml
- [X] T028 [US1] Add validate templates step to release workflow in .github/workflows/release.yml
- [X] T029 [US1] Add generate release notes step to release workflow in .github/workflows/release.yml
- [X] T030 [US1] Modify release creation step to use release_notes.md instead of CHANGELOG.md in .github/workflows/release.yml
- [X] T031 [US1] Add upload template assets step to upload all 34 ZIPs in .github/workflows/release.yml
- [X] T032 [US1] Update release workflow to pass artifacts between jobs using actions/upload-artifact and actions/download-artifact in .github/workflows/release.yml
- [X] T033 [US1] Test workflow with dry-run by creating test branch and triggering workflow_dispatch
- [X] T034 [US1] Verify workflow generates all 34 templates and validates them correctly
- [X] T035 [US1] Add error handling for partial template generation failures in .github/workflows/release.yml
- [X] T036 [US1] Add retry logic for GitHub API rate limit handling in .github/workflows/release.yml

**US1 Acceptance Criteria**:
- ✅ Workflow triggers on git tag push (v*)
- ✅ All 34 templates generated and validated
- ✅ GitHub release created with all 34 ZIP files
- ✅ Release notes include changelog and SHA-256 checksums
- ✅ Workflow completes in under 10 minutes
- ✅ No manual file uploads required

---

## Phase 4: User Story 2 - Developer Tests Templates Locally (P2)

**Goal**: Enable local template testing before CI/CD
**Duration**: 1 day
**Dependencies**: Phase 2 complete (can run in parallel with Phase 3)

**Independent Test**: Run local build script, verify all template ZIPs created in dist/ directory with correct structure and content.

### US2 Implementation Tasks

- [X] T037 [P] [US2] Create scripts/build-templates.sh wrapper script for local development
- [X] T038 [P] [US2] Add version argument handling with usage instructions in scripts/build-templates.sh
- [X] T039 [P] [US2] Add AGENTS and SCRIPTS environment variable support for subset building in scripts/build-templates.sh
- [X] T040 [P] [US2] Configure output to dist/templates/ directory (not .genreleases/) in scripts/build-templates.sh
- [X] T041 [P] [US2] Add build manifest generation with JSON output in scripts/build-templates.sh
- [X] T042 [P] [US2] Add verbose progress output and summary with file sizes in scripts/build-templates.sh
- [X] T043 [P] [US2] Integrate validation automatically after build completes in scripts/build-templates.sh
- [X] T044 [US2] Test local build with single agent (AGENTS=claude SCRIPTS=sh ./scripts/build-templates.sh v0.2.0-test)
- [X] T045 [US2] Extract and manually inspect single agent template structure
- [X] T046 [US2] Test full local build with all 34 variants
- [X] T047 [US2] Verify build-manifest.json contains all variants with correct metadata
- [X] T048 [US2] Add .gitignore entry for dist/ directory to prevent accidental commits

**US2 Acceptance Criteria**:
- ✅ Local build script generates all 34 templates in under 5 minutes
- ✅ Supports AGENTS and SCRIPTS filters for incremental testing
- ✅ Creates build-manifest.json with variant metadata
- ✅ Displays summary with file counts, sizes, and checksums
- ✅ Validation runs automatically and fails build if errors detected
- ✅ Build produces identical results to CI builds (reproducible)

---

## Phase 5: User Story 3 - CI System Validates Template Integrity (P2)

**Goal**: Prevent broken templates from being released
**Duration**: 1 day
**Dependencies**: Phase 2 complete, Phase 4 recommended (can run in parallel with Phase 3)

**Independent Test**: Trigger CI on pull request, verify it checks for required files, validates command references, ensures no Spec-Kit references remain, confirms growthkit-specific constitution present.

### US3 Implementation Tasks

- [X] T049 [P] [US3] Create .github/workflows/ci.yml for pull request validation
- [X] T050 [P] [US3] Add trigger for pull requests affecting .growthkit/**, memory/**, scripts/**, templates/** paths in .github/workflows/ci.yml
- [X] T051 [P] [US3] Add checkout step with full git history for validation in .github/workflows/ci.yml
- [X] T052 [P] [US3] Add build templates step using create-release-packages.sh in .github/workflows/ci.yml
- [X] T053 [P] [US3] Add validate templates step that fails on any errors in .github/workflows/ci.yml
- [X] T054 [P] [US3] Add shellcheck linting for bash scripts in .github/workflows/ci.yml
- [X] T055 [P] [US3] Add PSScriptAnalyzer linting for PowerShell scripts in .github/workflows/ci.yml
- [X] T056 [US3] Create test fixtures with intentional errors for validation testing in test-data/
- [X] T057 [US3] Create test-validation.sh script to verify validation catches errors
- [X] T058 [US3] Test negative case: Wrong namespace (agent: speckit.specify)
- [X] T059 [US3] Test negative case: Missing required file (remove constitution.md)
- [X] T060 [US3] Test negative case: Speckit reference in content (/speckit.plan)
- [X] T061 [US3] Test negative case: Wrong scripts (both bash/ and powershell/ in sh variant)
- [X] T062 [US3] Test positive case: Valid template passes all checks
- [X] T063 [US3] Add validation report generation with detailed error messages in scripts/validate-templates.sh
- [X] T064 [US3] Test CI workflow by creating test PR with template changes

**US3 Acceptance Criteria**:
- ✅ CI triggers on pull requests modifying templates
- ✅ Validation catches all template issues (namespace, missing files, references)
- ✅ Build fails with clear error messages when validation fails
- ✅ All negative test cases correctly fail validation
- ✅ Positive test case passes validation
- ✅ 95% of template problems detected before merge to main

---

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: CLI enhancements, documentation, and end-to-end testing
**Duration**: 1.5 days
**Dependencies**: Phases 3, 4, 5 complete

### CLI Enhancement Tasks

- [X] T065 [P] Add download_template_from_github() function in src/growthkit/cli/utils.py
- [X] T066 [P] Add extract_template() function to extract ZIP to project directory in src/growthkit/cli/utils.py
- [X] T067 [P] Add get_latest_release_version() function using GitHub API in src/growthkit/cli/utils.py
- [X] T068 [P] Add graceful fallback if release not found in src/growthkit/cli/utils.py
- [X] T069 Integrate template download into growthkit init command in src/growthkit/cli/main.py
- [X] T070 Add platform detection for bash vs powershell templates in src/growthkit/cli/main.py
- [X] T071 Add print_banner() function with "Growth Hacking Kit" ASCII art in src/growthkit/cli/main.py
- [X] T072 Integrate banner display at start of growthkit init command in src/growthkit/cli/main.py
- [X] T073 Test ASCII banner display on different terminal widths
- [X] T074 Test template download from GitHub releases
- [X] T075 Verify growthkit init creates correct project structure with downloaded templates

### Documentation Tasks

- [X] T076 [P] Update README.md with templates section and ASCII banner screenshot in README.md
- [X] T077 [P] Add template structure documentation explaining .growthkit/ directory layout in README.md
- [X] T078 [P] Create docs/templates.md with comprehensive template reference
- [X] T079 [P] Document all 17 agents with directory structures in docs/templates.md
- [X] T080 [P] Update CONTRIBUTING.md with template testing instructions in CONTRIBUTING.md
- [X] T081 [P] Document local build process for developers in CONTRIBUTING.md
- [X] T082 [P] Document release process for maintainers in CONTRIBUTING.md
- [X] T083 Add troubleshooting section for common template issues in docs/templates.md

### End-to-End Testing Tasks

- [X] T084 Create test release by pushing git tag v0.2.0-test
- [X] T085 Monitor GitHub Actions workflow completion
- [X] T086 Verify all 34 templates uploaded to GitHub release
- [X] T087 Download each template and verify structure
- [X] T088 Test growthkit init with claude agent and verify template download
- [X] T089 Test growthkit init with cursor-agent and verify template download
- [X] T090 Test growthkit init with windsurf agent and verify template download
- [X] T091 Verify no spec-kit/pmf-kit/blog-kit references in any template
- [X] T092 Verify Growth Hacking Kit constitution v1.1.0 present in all templates
- [X] T093 Verify ASCII banner displays correctly across different terminals
- [X] T094 Measure release workflow duration (target: under 10 minutes)
- [X] T095 Create production release v0.2.0 by pushing git tag
- [X] T096 Announce release and update documentation links

**Validation Checkpoint**:
- ✅ Full release workflow completes in under 10 minutes
- ✅ All templates pass validation (100% success rate)
- ✅ CLI successfully scaffolds projects with downloaded templates
- ✅ ASCII banner displays correctly on initialization
- ✅ Documentation is complete and accurate
- ✅ No spec-kit/pmf-kit/blog-kit references remain in any template

---

## Task Dependency Graph

```
Phase 1: Setup
  T001-T010 (Prerequisites)
  │
  ↓
Phase 2: Foundational
  T011-T025 (Build & Validation Scripts)
  │
  ├───────────────────┬───────────────────┐
  ↓                   ↓                   ↓
Phase 3: US1         Phase 4: US2         Phase 5: US3
T026-T036            T037-T048            T049-T064
(Release Auto)       (Local Build)        (CI Validation)
  │                   │                   │
  └───────────────────┴───────────────────┘
                      ↓
                 Phase 6: Polish
                 T065-T096
                 (CLI + Docs + E2E Testing)
```

### Critical Path

**T001 → T002-T010 → T011-T025 → T026-T036 → T084-T096**

(Setup → Foundational → US1 Release Automation → E2E Testing)

**Estimated Total Time**: ~7 days (with full focus), ~10-12 days (with interruptions)

---

## Parallel Execution Opportunities

### Phase 1 (Setup)
- **Parallel**: T003-T008 (Port all PowerShell scripts simultaneously - different files)

### Phase 2 (Foundational)
- **Parallel**: T017 (generate-release-notes.sh) can be developed while T011-T016 (create-release-packages.sh) is in progress
- **Parallel**: T018-T025 (validate-templates.sh) can be developed in parallel with T011-T017

### Phase 3-5 (User Stories)
- **Phase 4 can run in parallel with Phase 3** (different files, no dependencies)
- **Phase 5 can run in parallel with Phase 3** (different files, but benefits from Phase 4 completion)

### Phase 6 (Polish)
- **Parallel**: T065-T068, T076-T083 (Different files - CLI utils, documentation)
- **Sequential**: T069-T075 (CLI integration depends on utils), T084-T096 (E2E testing depends on all previous phases)

---

## Implementation Strategy

### MVP Scope (Minimum Viable Product)

**Goal**: Get first release working end-to-end

**MVP Tasks** (in order):
1. Phase 1: Setup (T001-T010) - **REQUIRED**
2. Phase 2: Foundational (T011-T025) - **REQUIRED**
3. Phase 3: US1 (T026-T036) - **REQUIRED** (core capability)
4. Basic E2E Test (T084-T086, T095) - **REQUIRED**

**MVP delivers**:
- Automated release creation with 34 templates
- GitHub release with all assets
- Basic validation

**Post-MVP Iterations**:
- **Iteration 2**: Phase 4 (US2) - Local development workflow
- **Iteration 3**: Phase 5 (US3) - CI validation
- **Iteration 4**: Phase 6 - CLI enhancements + full documentation

### Incremental Delivery Approach

1. **Week 1**: Setup + Foundational (Phases 1-2)
   - Deliverable: Working build scripts that generate all 34 templates locally

2. **Week 2**: Release Automation (Phase 3)
   - Deliverable: Automated GitHub releases with templates

3. **Week 3**: Developer Experience (Phases 4-5)
   - Deliverable: Local testing + CI validation

4. **Week 4**: Polish + Launch (Phase 6)
   - Deliverable: CLI enhancements, documentation, production release

---

## Task Status Tracking

| Phase | Total Tasks | P1 Tasks | P2 Tasks | Status |
|-------|-------------|----------|----------|--------|
| 1: Setup | 10 | 0 | 0 | ✅ Complete |
| 2: Foundational | 15 | 0 | 0 | ✅ Complete |
| 3: US1 (P1) | 11 | 11 | 0 | ✅ Complete |
| 4: US2 (P2) | 12 | 0 | 12 | ✅ Complete |
| 5: US3 (P2) | 16 | 0 | 16 | ✅ Complete |
| 6: Polish | 32 | 0 | 0 | ✅ Complete |
| **TOTAL** | **96** | **11** | **28** | **✅ 100% Complete (96/96 tasks)** |

---

## Success Criteria Mapping

### Release Automation Success (SC-001 to SC-005)
- **Covered by**: Phase 3 (US1) + T084-T096 (E2E Testing)
- **Tasks**: T026-T036, T084-T086, T094-T095

### Template Quality (SC-006 to SC-010)
- **Covered by**: Phase 2 (Validation) + Phase 5 (US3)
- **Tasks**: T018-T025, T049-T064, T087, T091-T092

### Developer Experience (SC-011 to SC-014)
- **Covered by**: Phase 4 (US2) + Phase 5 (US3)
- **Tasks**: T037-T048, T049-T064

### Platform Support (SC-015 to SC-017)
- **Covered by**: Phase 1 (PowerShell) + Phase 2 (Agent Configs)
- **Tasks**: T002-T008, T014, T087-T090

### CLI Enhancements
- **Covered by**: Phase 6 (CLI Enhancements)
- **Tasks**: T065-T075, T088-T090, T093

---

## Next Actions

**Immediate Next Steps**:

1. ✅ **Start Phase 1**: Verify .growthkit/ structure (T001)
2. ✅ **Create PowerShell scripts**: Port all 6 bash scripts (T002-T008)
3. ✅ **Set up directories**: Create workflow and scripts directories (T009-T010)
4. ✅ **Begin Phase 2**: Implement create-release-packages.sh (T011-T016)

**Before Starting**:
- Ensure git repository is on feature branch `004-growthkit-auto-template-release`
- Ensure .growthkit/ directory has all required source files
- Have access to GitHub repository for testing CI/CD workflows

---

**Tasks Document Version**: 1.0
**Last Updated**: 2025-12-24
**Status**: Ready for Implementation
**Total Tasks**: 96
**Estimated Duration**: 7-12 days
