# Tasks: Automated Growth-Hacking-Kit Template Release Generation

**Feature**: Automated template release generation for multiple AI agents from `.growthkit/` source
**Branch**: 004-growthkit-auto-release
**Created**: 2026-01-04
**Status**: Ready for Implementation

---

## Implementation Strategy

This feature enables automated generation and publication of 34 Growth-Hacking-Kit template variants (17 AI agents × 2 script types) to GitHub releases. Tasks are organized by user story to enable independent implementation and testing.

**MVP Scope**: User Story 1 (P1) - Release Manager Creates New Growth-Hacking-Kit Release
**Incremental Delivery**: US1 → US2 → US3

---

## Phase 1: Setup & Verification

**Goal**: Verify .growthkit/ source directory and create PowerShell script variants

### Setup Tasks

- [ ] T001 Verify .growthkit/ directory structure and Growth-Hacking-Kit constitution v1.1.0 in .growthkit/memory/constitution.md
- [ ] T002 List all bash scripts in .growthkit/scripts/bash/ and verify 5 scripts present
- [ ] T003 List all template files in .growthkit/templates/ and verify spec, plan, tasks templates present
- [ ] T004 List all command files in .growthkit/templates/commands/ and verify 9 growthkit.*.md files present
- [ ] T005 Scan .growthkit/ for any speckit or blogkit references using grep -r
- [ ] T006 Create .growthkit/scripts/powershell/ directory for PowerShell script variants
- [ ] T007 [P] Port .growthkit/scripts/bash/common.sh to .growthkit/scripts/powershell/common.ps1
- [ ] T008 [P] Port .growthkit/scripts/bash/setup-plan.sh to .growthkit/scripts/powershell/setup-plan.ps1
- [ ] T009 [P] Port .growthkit/scripts/bash/check-prerequisites.sh to .growthkit/scripts/powershell/check-prerequisites.ps1
- [ ] T010 [P] Port .growthkit/scripts/bash/create-new-feature.sh to .growthkit/scripts/powershell/create-new-feature.ps1
- [ ] T011 [P] Port .growthkit/scripts/bash/update-agent-context.sh to .growthkit/scripts/powershell/update-agent-context.ps1

**Acceptance Criteria**:
- ✅ All 5 bash scripts verified in .growthkit/scripts/bash/
- ✅ All 9 command files verified with growthkit.* naming
- ✅ Constitution is Growth-Hacking-Kit v1.1.0
- ✅ No speckit or blogkit references found
- ✅ All 5 PowerShell scripts created with proper conventions

---

## Phase 2: Foundational Infrastructure

**Goal**: Create GitHub workflows scripts directory and core build infrastructure

### Foundational Tasks

- [ ] T012 Create .github/workflows/scripts/ directory for workflow scripts
- [ ] T013 [P] Create empty placeholder .github/workflows/scripts/get-next-version.sh
- [ ] T014 [P] Create empty placeholder .github/workflows/scripts/check-release-exists.sh
- [ ] T015 [P] Create empty placeholder .github/workflows/scripts/create-release-packages.sh
- [ ] T016 [P] Create empty placeholder .github/workflows/scripts/generate-release-notes.sh
- [ ] T017 [P] Create empty placeholder .github/workflows/scripts/create-github-release.sh
- [ ] T018 Make all workflow scripts executable with chmod +x

**Acceptance Criteria**:
- ✅ Directory .github/workflows/scripts/ created
- ✅ All 5 script files created
- ✅ All scripts are executable

---

## Phase 3: User Story 1 - Release Manager Creates New Growth-Hacking-Kit Release (P1)

**Goal**: Enable maintainer to create releases with 34 template variants by pushing git tags

**Independent Test**: Maintainer can push a version tag (e.g., `git tag v0.1.0 && git push --tags`), workflow triggers automatically, generates all 34 templates from .growthkit/ source, and publishes GitHub release with proper naming and checksums.

### US1: Core Build Script

- [ ] T019 [US1] Implement build_variant() function in .github/workflows/scripts/create-release-packages.sh to create .specify/ structure
- [ ] T020 [US1] Implement copy logic to copy from .growthkit/memory/ to .specify/memory/ in build_variant()
- [ ] T021 [US1] Implement copy logic to copy from .growthkit/templates/ to .specify/templates/ in build_variant()
- [ ] T022 [US1] Implement script selection logic to copy bash/ or powershell/ based on variant type
- [ ] T023 [US1] Implement generate_commands() function to transform growthkit.*.md templates for each agent
- [ ] T024 [US1] Implement agent directory mapping for all 17 agents (claude, cursor-agent, windsurf, gemini, copilot, qoder, qwen, opencode, codex, kilocode, auggie, codebuddy, amp, shai, q, bob, roo)
- [ ] T025 [US1] Implement ZIP creation and SHA-256 checksum calculation in build_variant()
- [ ] T026 [US1] Implement main loop to iterate through 17 agents × 2 script types in create-release-packages.sh
- [ ] T027 [US1] Add progress reporting and error handling to create-release-packages.sh

### US1: Helper Scripts

- [ ] T028 [P] [US1] Implement get-next-version.sh to extract version from git tag ($GITHUB_REF)
- [ ] T029 [P] [US1] Implement check-release-exists.sh to check if release already published using gh CLI
- [ ] T030 [P] [US1] Implement generate-release-notes.sh to create changelog from commits since last tag
- [ ] T031 [US1] Update generate-release-notes.sh to list all 34 ZIP files with SHA-256 checksums
- [ ] T032 [US1] Update generate-release-notes.sh to reference "Growth-Hacking-Kit CLI" (not Spec-Kit or Blog-Tech-Kit)
- [ ] T033 [P] [US1] Implement create-github-release.sh to publish release with gh CLI and upload 34 ZIP assets

### US1: GitHub Actions Workflow

- [ ] T034 [US1] Create .github/workflows/release.yml with tag trigger (on: push: tags: - 'v*.*.*')
- [ ] T035 [US1] Add checkout step with fetch-depth: 0 to release.yml
- [ ] T036 [US1] Add get next version step calling get-next-version.sh in release.yml
- [ ] T037 [US1] Add check release exists step calling check-release-exists.sh in release.yml
- [ ] T038 [US1] Add create release packages step calling create-release-packages.sh in release.yml
- [ ] T039 [US1] Add validate release packages step (placeholder for Phase 4) in release.yml
- [ ] T040 [US1] Add generate release notes step calling generate-release-notes.sh in release.yml
- [ ] T041 [US1] Add create GitHub release step calling create-github-release.sh with GITHUB_TOKEN in release.yml
- [ ] T042 [US1] Add workflow_dispatch trigger for manual testing in release.yml

### US1: First Release Test

- [ ] T043 [US1] Create test tag v0.0.1-test locally with git tag
- [ ] T044 [US1] Push test tag to trigger workflow with git push origin v0.0.1-test
- [ ] T045 [US1] Monitor workflow execution in GitHub Actions UI
- [ ] T046 [US1] Verify 34 ZIP files generated in workflow artifacts
- [ ] T047 [US1] Verify release notes include Growth-Hacking-Kit CLI branding
- [ ] T048 [US1] Delete test tag and release after validation

**US1 Acceptance Criteria**:
- ✅ Workflow triggers on version tag push
- ✅ All 34 template variants generated from .growthkit/ source
- ✅ GitHub release created with proper versioning
- ✅ Release notes include changelog and SHA-256 checksums
- ✅ All templates use /growthkit.* namespace
- ✅ Constitution is Growth-Hacking-Kit v1.1.0

---

## Phase 4: User Story 2 - Developer Tests Template Generation Locally (P2)

**Goal**: Enable developers to test template generation locally before pushing changes

**Independent Test**: Developer can run `./scripts/build-templates.sh v0.1.0-test`, verify all 34 templates generated in dist/templates/, inspect ZIP structure, and see clear error messages if any template fails.

### US2: Local Build Wrapper

- [ ] T049 [US2] Create scripts/build-templates.sh wrapper script with version argument validation
- [ ] T050 [US2] Implement DIST_DIR creation and GENRELEASES_DIR export in build-templates.sh
- [ ] T051 [US2] Add call to create-release-packages.sh from build-templates.sh
- [ ] T052 [US2] Implement generate_manifest() function to create build-manifest.json in build-templates.sh
- [ ] T053 [US2] Add progress output and summary display in build-templates.sh
- [ ] T054 [US2] Add support for AGENTS and SCRIPTS env vars for subset building in build-templates.sh

### US2: Local Testing

- [ ] T055 [US2] Test single agent build with AGENTS=claude SCRIPTS=sh ./scripts/build-templates.sh v0.1.0-test
- [ ] T056 [US2] Extract test ZIP to /tmp/test-template and verify directory structure
- [ ] T057 [US2] Verify .specify/memory/, .specify/scripts/bash/, .specify/templates/ directories exist
- [ ] T058 [US2] Verify .claude/commands/ contains 9 growthkit.*.md files
- [ ] T059 [US2] Scan extracted template for speckit references with grep -r
- [ ] T060 [US2] Verify constitution is Growth-Hacking-Kit v1.1.0 in extracted template
- [ ] T061 [US2] Test full build with ./scripts/build-templates.sh v0.1.0-test
- [ ] T062 [US2] Verify exactly 34 ZIP files created in dist/templates/
- [ ] T063 [US2] Verify build-manifest.json shows all 34 variants with status completed
- [ ] T064 [US2] Spot-check 3-4 different agent variants for correctness

**US2 Acceptance Criteria**:
- ✅ Local build script generates all 34 templates
- ✅ Templates output to dist/templates/ directory
- ✅ Build manifest JSON created with metadata
- ✅ Clear error messages if any template fails
- ✅ Supports filtering by agent or script type

---

## Phase 5: User Story 3 - CI System Validates Template Integrity (P2)

**Goal**: Prevent broken templates from being released through automated validation

**Independent Test**: CI runs validation on pull request, checks for required files from .growthkit/, validates command references, ensures no Spec-Kit references, and fails build with clear error messages if issues found.

### US3: Validation Script

- [ ] T065 [US3] Create scripts/validate-templates.sh with ZIP extraction logic
- [ ] T066 [P] [US3] Implement check_frontmatter_namespace() to verify agent: growthkit.* in all commands
- [ ] T067 [P] [US3] Implement check_required_files() to verify files from .growthkit/ present in .specify/
- [ ] T068 [P] [US3] Implement check_content_references() to scan for /speckit.* or /blogkit.* references
- [ ] T069 [P] [US3] Implement check_directory_structure() to verify .specify/ working directory exists
- [ ] T070 [P] [US3] Implement check_constitution_version() to verify Growth-Hacking-Kit v1.1.0
- [ ] T071 [P] [US3] Implement check_script_consistency() to ensure sh has bash/, ps has powershell/
- [ ] T072 [P] [US3] Implement check_command_count() to verify 9 required commands present
- [ ] T073 [P] [US3] Implement check_zip_integrity() to test ZIP extracts without errors
- [ ] T074 [US3] Implement validate_variant() function to run all checks on single ZIP
- [ ] T075 [US3] Implement main() function to process directory or single ZIP file
- [ ] T076 [US3] Add error reporting and exit code handling to validate-templates.sh

### US3: Validation Testing

- [ ] T077 [US3] Create test-data/ directory for validation test fixtures
- [ ] T078 [US3] Create test case with wrong namespace (agent: speckit.specify)
- [ ] T079 [US3] Create test case with missing constitution file
- [ ] T080 [US3] Create test case with speckit reference in content
- [ ] T081 [US3] Create test case with wrong scripts (both bash/ and powershell/)
- [ ] T082 [US3] Create test-validation.sh runner script to execute all test cases
- [ ] T083 [US3] Run validation tests and verify negative tests fail, positive test passes

### US3: Integration

- [ ] T084 [US3] Integrate validation call into scripts/build-templates.sh after template generation
- [ ] T085 [US3] Update build script to exit with code 1 if validation fails
- [ ] T086 [US3] Update .github/workflows/release.yml to call validate-templates.sh before release creation
- [ ] T087 [US3] Test workflow validation by creating intentionally broken template

**US3 Acceptance Criteria**:
- ✅ Validation script checks all 9 validation criteria
- ✅ Returns exit code 0 on success, non-zero on failure
- ✅ Clear error messages indicate which check failed
- ✅ Negative test cases cause validation failure
- ✅ Positive test case passes validation
- ✅ Build script fails if validation fails
- ✅ CI workflow blocks release if validation fails

---

## Phase 6: Polish & Documentation

**Goal**: Complete documentation and create first production release

### Documentation Tasks

- [ ] T088 [P] Update README.md to mention Growth-Hacking-Kit templates
- [ ] T089 [P] Document template structure in README.md or docs/templates.md
- [ ] T090 [P] Document release process with tag-based trigger in CONTRIBUTING.md
- [ ] T091 [P] Add local build instructions to documentation

### First Production Release

- [ ] T092 Ensure all Phase 1-5 tasks complete
- [ ] T093 Review all changes on branch 004-growthkit-auto-release
- [ ] T094 Merge feature branch to main
- [ ] T095 Create production tag v0.1.0 with git tag v0.1.0 -m "Release v0.1.0: Initial Growth-Hacking-Kit templates"
- [ ] T096 Push tag to trigger release with git push origin v0.1.0
- [ ] T097 Monitor workflow execution with gh run watch
- [ ] T098 Verify release v0.1.0 created on GitHub with gh release view v0.1.0
- [ ] T099 Verify 34 template ZIP files present in release assets
- [ ] T100 Test growthkit init command downloads from growth-hacking-kit repository

**Acceptance Criteria**:
- ✅ Documentation updated with template information
- ✅ Release process documented
- ✅ First production release v0.1.0 published
- ✅ All 34 templates available for download
- ✅ CLI successfully downloads templates

---

## Task Dependencies

### Critical Path
T001 → T006 → T007-T011 → T012 → T015 → T019-T027 → T028-T033 → T034-T042 → T043-T048 → T092-T100

### Parallel Opportunities

**Phase 1 (Setup)**: T007, T008, T009, T010, T011 can run in parallel (different files)

**Phase 2 (Foundational)**: T013, T014, T015, T016, T017 can run in parallel (different files)

**Phase 3 (US1 Helper Scripts)**: T028, T029, T030, T033 can run in parallel (different files)

**Phase 5 (US3 Validation Checks)**: T066, T067, T068, T069, T070, T071, T072, T073 can run in parallel (different functions)

**Phase 5 (US3 Test Cases)**: T078, T079, T080, T081 can run in parallel (different test fixtures)

**Phase 6 (Documentation)**: T088, T089, T090, T091 can run in parallel (different files)

---

## User Story Completion Order

1. **User Story 1 (P1)**: Tasks T019-T048 - Release Manager Creates New Growth-Hacking-Kit Release
   - **Delivers**: Automated release generation on tag push
   - **Test**: Push version tag, verify 34 templates published to GitHub release

2. **User Story 2 (P2)**: Tasks T049-T064 - Developer Tests Template Generation Locally
   - **Delivers**: Local build script for testing before CI
   - **Test**: Run local build, verify all templates generated correctly

3. **User Story 3 (P2)**: Tasks T065-T087 - CI System Validates Template Integrity
   - **Delivers**: Automated validation prevents broken releases
   - **Test**: Create broken template, verify CI catches error

---

## Summary

**Total Tasks**: 100
- Setup & Verification (Phase 1): 11 tasks
- Foundational Infrastructure (Phase 2): 7 tasks
- User Story 1 (Phase 3): 30 tasks
- User Story 2 (Phase 4): 16 tasks
- User Story 3 (Phase 5): 23 tasks
- Polish & Documentation (Phase 6): 13 tasks

**Parallel Opportunities**: 25 tasks marked with [P] can run in parallel

**Estimated Timeline**:
- Phase 1: 0.5 days
- Phase 2: 0.5 days
- Phase 3 (US1): 2 days
- Phase 4 (US2): 1 day
- Phase 5 (US3): 2 days
- Phase 6: 1 day
- **Total**: 7 days (with parallelization, can complete in 5-6 days)

**MVP Scope**: Complete Phase 1-3 (Tasks T001-T048) for minimal viable release automation

**Key Differences from Blogkit**:
- 17 agents instead of 18 (34 variants instead of 36)
- `.growthkit/` source instead of `.blogkit/`
- Growth-Hacking-Kit constitution v1.1.0
- Tag-based trigger instead of push to main
- `/growthkit.*` namespace throughout

---

**Tasks Document Version**: 1.0
**Last Updated**: 2026-01-04
**Status**: Ready for Implementation
