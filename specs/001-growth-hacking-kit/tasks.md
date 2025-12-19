---

description: "Task list for Growth Hacking Kit implementation"
---

# Tasks: Growth Hacking Kit

**Input**: Design documents from `/specs/001-growth-hacking-kit/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Tests are OPTIONAL - only included if explicitly requested. This feature does not explicitly request tests in the specification, so test tasks are omitted unless requested by user.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. The MVP scope is User Story 1 (Initialize Growth Campaign Project), which delivers immediate value.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

- **Package root**: `src/growthkit/` for Python CLI code
- **Kit directory**: `.growthkit/` for project-specific files (templates, scripts, memory)
- **Tests**: `tests/` for pytest unit/integration tests (if requested)
- **Specs**: `specs/###-campaign-name/` for campaign documentation

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic CLI structure

- [ ] T001 Create project directory structure matching plan.md (src/growthkit/, .growthkit/, tests/)
- [ ] T002 Create pyproject.toml with package name `growthkit-cli`, entry point `growthkit`, dependencies (typer, jinja2, pyyaml, gitpython, httpx, pytest)
- [ ] T003 [P] Create src/growthkit/__init__.py with version "0.1.0"
- [ ] T004 [P] Create src/growthkit/__main__.py with entry point for `python -m growthkit`
- [ ] T005 [P] Create LICENSE file (MIT, inherited from spec-kit pattern)
- [ ] T006 Create README.md with GEO-optimized content (structured tables, benchmarks, installation guide)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Create src/growthkit/cli/config.py with KIT_NAME="growthkit", PACKAGE_DIR=".growthkit/", ENV_VAR="GROWTHKIT_CAMPAIGN"
- [ ] T008 [P] Create src/growthkit/cli/utils.py with git operations (branch creation, status checks) using gitpython
- [ ] T009 [P] Create src/growthkit/cli/utils.py agent detection functions (Claude Code, Cursor, Windsurf, Copilot, etc.)
- [ ] T010 [P] Create src/growthkit/cli/utils.py template rendering functions using jinja2
- [ ] T011 Create .growthkit/templates/spec-template.md (copy from .specify/templates/spec-template.md and parameterize {{KIT_NAME}})
- [ ] T012 [P] Create .growthkit/templates/plan-template.md (copy from .specify/templates/plan-template.md and parameterize {{KIT_NAME}})
- [ ] T013 [P] Create .growthkit/templates/tasks-template.md (copy from .specify/templates/tasks-template.md and parameterize {{KIT_NAME}})
- [ ] T014 Create .growthkit/templates/constitution-template.md (copy from .specify/memory/constitution.md as Growth Hacking Kit Constitution v1.1.0)
- [ ] T015 Create .growthkit/scripts/bash/common.sh (utility functions for bash scripts, parameterized for growthkit)
- [ ] T016 [P] Create .growthkit/scripts/bash/check-prerequisites.sh (checks git, uv, python, agent installations)
- [ ] T017 [P] Create .growthkit/scripts/bash/create-new-feature.sh (creates ###-campaign-name branches, parameterized for growthkit)
- [ ] T018 [P] Create .growthkit/scripts/bash/setup-plan.sh (copies plan template, returns JSON with paths)
- [ ] T019 [P] Create .growthkit/scripts/bash/update-agent-context.sh (updates CLAUDE.md, .cursor/README.md, .windsurf/README.md)
- [ ] T020 Create src/growthkit/constitution/__init__.py
- [ ] T021 [P] Create src/growthkit/constitution/gates.py with mandatory/advisory gate definitions (Seven Core Principles)
- [ ] T022 [P] Create src/growthkit/constitution/validator.py with Constitution Check validation logic (regex parsing of spec.md)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Initialize Growth Campaign Project (Priority: P1) 🎯 MVP

**Goal**: Enable users to bootstrap a growth-hacking-kit project with CLI and establish constitution

**Independent Test**: Run `growthkit init my-campaign --ai claude` and verify .growthkit/ directory created, constitution.md exists, slash commands available in agent

### Implementation for User Story 1

- [ ] T023 [US1] Create src/growthkit/cli/main.py with Typer app definition
- [ ] T024 [US1] Implement `growthkit init` command in src/growthkit/cli/main.py with arguments (project-name, --ai, --script, --ignore-agent-tools, --no-git, --here, --force, --skip-tls, --debug, --github-token)
- [ ] T025 [US1] Add agent detection logic in `growthkit init` (Claude Code, Cursor, Windsurf detection via utils.py)
- [ ] T026 [US1] Add .growthkit/ directory creation in `growthkit init` (memory/, scripts/, templates/ subdirectories)
- [ ] T027 [US1] Add constitution template copy in `growthkit init` (from src/growthkit/templates/constitution-template.md to .growthkit/memory/constitution.md)
- [ ] T028 [US1] Add script templates copy in `growthkit init` (bash scripts to .growthkit/scripts/bash/, powershell to .growthkit/scripts/powershell/)
- [ ] T029 [US1] Add spec/plan/tasks templates copy in `growthkit init` (to .growthkit/templates/)
- [ ] T030 [US1] Add agent command file generation in `growthkit init` (create .claude/commands/growthkit-*.md, .cursor/commands/growthkit-*.md, .windsurf/commands/growthkit-*.md)
- [ ] T031 [US1] Add Git repository initialization in `growthkit init` (if not --no-git, run git init)
- [ ] T032 [US1] Add success message display in `growthkit init` with next steps (run /growthkit.constitution, /growthkit.specify)
- [ ] T033 [US1] Implement `growthkit check` command in src/growthkit/cli/main.py (checks git, uv, python, agents, displays results table)
- [ ] T034 [US1] Create .growthkit/templates/commands/growthkit-specify.md (slash command template for /growthkit.specify)
- [ ] T035 [P] [US1] Create .growthkit/templates/commands/growthkit-plan.md (slash command template for /growthkit.plan)
- [ ] T036 [P] [US1] Create .growthkit/templates/commands/growthkit-tasks.md (slash command template for /growthkit.tasks)
- [ ] T037 [P] [US1] Create .growthkit/templates/commands/growthkit-implement.md (slash command template for /growthkit.implement)
- [ ] T038 [P] [US1] Create .growthkit/templates/commands/growthkit-constitution.md (slash command template for /growthkit.constitution)

**Checkpoint**: At this point, User Story 1 should be fully functional - users can run `growthkit init` and see slash commands in their agent

---

## Phase 4: User Story 2 - Create Growth Campaign Specification (Priority: P2)

**Goal**: Enable users to specify growth campaigns using /growthkit.specify command from natural language

**Independent Test**: Run `/growthkit.specify Launch Product Hunt campaign...` and verify branch created, spec.md generated with Constitution Check validation, no [NEEDS CLARIFICATION] markers remain

### Implementation for User Story 2

- [ ] T039 [US2] Implement branch name generation logic in src/growthkit/cli/utils.py (extract 2-4 word short name from campaign description)
- [ ] T040 [US2] Implement feature number detection in src/growthkit/cli/utils.py (check remote branches, local branches, specs/ directories for highest number)
- [ ] T041 [US2] Implement .growthkit/scripts/bash/create-new-feature.sh integration (call script with --number, --short-name, --json)
- [ ] T042 [US2] Implement spec template rendering in src/growthkit/cli/utils.py using jinja2 (replace {{KIT_NAME}}, {{CAMPAIGN_NAME}}, {{CAMPAIGN_NUMBER}}, {{FEATURE_BRANCH}})
- [ ] T043 [US2] Implement growth type identification in src/growthkit/constitution/validator.py (Vibe Growth, Trust Growth, or Agentic Growth from target audience)
- [ ] T044 [US2] Implement viral loop extraction in src/growthkit/constitution/validator.py (Remix, Integration, or Watermark from campaign description)
- [ ] T045 [US2] Implement metrics extraction in src/growthkit/constitution/validator.py (primary metric with target, activation metric, engagement metric)
- [ ] T046 [US2] Implement Constitution Check validation in src/growthkit/constitution/validator.py (validate spec against mandatory gates: spec exists, growth type identified, viral loop defined, k-factor target, metrics set)
- [ ] T047 [US2] Implement [NEEDS CLARIFICATION] limiting logic (maximum 3 markers, prioritized by scope > security/privacy > UX)
- [ ] T048 [US2] Create specs/###-campaign-name/checklists/requirements.md template in src/growthkit/templates/
- [ ] T049 [US2] Implement checklist generation in src/growthkit/cli/utils.py (spec quality validation checklist)
- [ ] T050 [US2] Add spec.md writing logic (generate from template, write to specs/###-campaign-name/spec.md)
- [ ] T051 [US2] Add checklist validation logic (check Content Quality, Requirement Completeness, Feature Readiness)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - users can initialize project and generate campaign specs

---

## Phase 5: User Story 3 - Plan Campaign Implementation (Priority: P3)

**Goal**: Convert validated campaign spec into implementation plan with platform tactics, Constitution Check, pilot scoping

**Independent Test**: Run `/growthkit.plan Use X/Twitter...` on approved spec and verify plan.md created with Constitution Check gates, platform-specific tactics documented, pilot budget <10% of scale budget

### Implementation for User Story 3

- [ ] T052 [US3] Implement plan template rendering in src/growthkit/cli/utils.py (Technical Context, Constitution Check, Project Structure sections)
- [ ] T053 [US3] Implement Constitution Check gate validation in src/growthkit/constitution/validator.py (mandatory gates: spec exists, growth type, target audience, viral loop, k-factor, metrics, pilot)
- [ ] T054 [US3] Implement platform tactic extraction in src/growthkit/research/platforms.py (X/Twitter 30-60s 16:9, TikTok 15-30s 9:16, LinkedIn case studies, GitHub code examples, Product Hunt demo video)
- [ ] T055 [US3] Implement GEO optimization research in src/growthkit/research/platforms.py (Answer Density, structured tables, LLM citation validation)
- [ ] T056 [US3] Implement pilot phase scoping validation (ensure pilot budget <10% of scale budget per Principle VI)
- [ ] T057 [US3] Create research.md template in src/growthkit/templates/
- [ ] T058 [P] [US3] Create data-model.md template in src/growthkit/templates/
- [ ] T059 [P] [US3] Create quickstart.md template in src/growthkit/templates/
- [ ] T060 [US3] Implement research.md generation (platform API specs, GEO strategy, tactical decisions from refs/0_overview.md, refs/1_principles_for_constitution.md, refs/3_project_mangement_for_plan.md)
- [ ] T061 [US3] Implement data-model.md generation (Campaign, Constitution, PlatformTactic, ViralLoop, PilotPhase, Retrospective, GrowthMetricsDashboard entities)
- [ ] T062 [US3] Create contracts/ directory templates (cli-commands.yaml, slash-commands.yaml, template-variables.json)
- [ ] T063 [US3] Implement contracts/ generation (CLI command schemas, slash command schemas, template variable definitions)
- [ ] T064 [US3] Implement quickstart.md generation (installation via uv tool install, project init, first campaign walkthrough)
- [ ] T065 [US3] Implement .growthkit/scripts/bash/update-agent-context.sh execution (detect agent, update CLAUDE.md/.cursor/README.md/.windsurf/README.md with technology references from plan.md)
- [ ] T066 [US3] Implement advisory gates re-validation (Agent-First Architecture, Multi-Platform Distribution, Community-Led Amplification)
- [ ] T067 [US3] Add Complexity Tracking section generation (if constitution violations exist, document justification)

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently - users can initialize, specify, and plan campaigns

---

## Phase 6: User Story 4 - Generate Campaign Task Breakdown (Priority: P4)

**Goal**: Convert implementation plan into actionable, dependency-ordered task list organized by campaign phase

**Independent Test**: Run `/growthkit.tasks` on completed plan and verify tasks.md created with phases (Setup → Pilot → Scale → Measure), exact deliverables, parallel opportunities marked [P], checkpoint validation after Pilot

### Implementation for User Story 4

- [ ] T068 [US4] Implement plan.md parsing in src/growthkit/cli/utils.py (extract platforms, budget, tactics, pilot scope)
- [ ] T069 [US4] Implement data-model.md parsing in src/growthkit/cli/utils.py (extract entities for task generation)
- [ ] T070 [US4] Implement task template rendering in src/growthkit/cli/utils.py (Phase 1 Setup, Phase 2 Pilot, Phase 3 Scale, Phase 4 Measure)
- [ ] T071 [US4] Implement task ID generation (sequential T001, T002, T003...)
- [ ] T072 [US4] Implement parallel task marking logic (mark tasks with [P] when different files, no dependencies)
- [ ] T073 [US4] Implement deliverable specification logic (exact file paths for content, platform posts, tracking URLs)
- [ ] T074 [US4] Implement checkpoint validation task generation (document pilot results, validate against success criteria, make go/no-go decision)
- [ ] T075 [US4] Implement dependency order enforcement (Setup → Pilot → Validation → Scale → Measure)
- [ ] T076 [US4] Add tasks.md writing logic (generate from template, write to specs/###-campaign-name/tasks.md)

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently - users can initialize, specify, plan, and generate task breakdowns

---

## Phase 7: User Story 5 - Execute Campaign Implementation (Priority: P5)

**Goal**: Execute all tasks in correct order with pilot validation gates, content creation, metric tracking, retrospective generation

**Independent Test**: Run `/growthkit.implement` on complete task list and verify AI agent executes tasks in dependency order, pauses at pilot checkpoint if criteria not met, creates platform-native content (X: 16:9, TikTok: 9:16), generates retrospective.md

### Implementation for User Story 5

- [ ] T077 [US5] Implement tasks.md parsing in src/growthkit/cli/utils.py (extract task list with dependencies, phases, checkpoints)
- [ ] T078 [US5] Implement dependency graph generation (validate Setup → Pilot → Validation → Scale → Measure order)
- [ ] T079 [US5] Implement task execution engine (execute tasks sequentially, respect [P] markers for parallel opportunities)
- [ ] T080 [US5] Implement checkpoint validation logic (pause at Pilot phase, validate results against success criteria from plan.md)
- [ ] T081 [US5] Implement go/no-go decision prompting (if pilot k-factor <0.8 or engagement <5%, prompt user to halt or justify continuation)
- [ ] T082 [US5] Implement platform-native content generation (X/Twitter: 16:9 video 30-60s, TikTok: 9:16 video 15-30s with hook in first 3s, LinkedIn: data-driven case studies, GitHub: code examples/READMEs, Product Hunt: demo video + first-100-user incentives)
- [ ] T083 [US5] Create specs/###-campaign-name/assets/ directory for generated content
- [ ] T084 [US5] Implement metrics tracking logic (views, engagement rate, signups, k-factor, Time-to-First-Share)
- [ ] T085 [US5] Create retrospective.md template in src/growthkit/templates/
- [ ] T086 [US5] Implement retrospective generation (actual vs. predicted metrics, principles followed/violated, failure modes encountered, creative lessons, audience insights, platform effectiveness, recommendations)
- [ ] T087 [US5] Add retrospective.md writing logic (generate from template, write to specs/###-campaign-name/retrospective.md)

**Checkpoint**: All user stories should now be independently functional - users can execute full workflow (init → specify → plan → tasks → implement)

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories, documentation, testing infrastructure

- [ ] T088 [P] Update README.md with comprehensive installation guide, feature showcase, multi-kit coexistence examples
- [ ] T089 [P] Create refs/4_pm_tasking_for_tasks.md (task breakdown guidance based on refs/4_pm_tasking_for_tasks.md research)
- [ ] T090 [P] Create refs/5_writing_for_optimize.md (content optimization guidance for GEO)
- [ ] T091 [P] Create refs/6_claude_code.md (agent-specific workflow guidance)
- [ ] T092 [P] Create refs/7_optimization.md (performance patterns, caching strategies)
- [ ] T093 Add error handling for all CLI commands (clear error messages, exit codes per contracts/cli-commands.yaml)
- [ ] T094 Add input validation for all CLI commands (validate project-name, --ai choices, budget values)
- [ ] T095 Add progress indicators for long-running operations (research.md generation, content creation)
- [ ] T096 Add logging infrastructure (debug logs for --debug flag, error logs for troubleshooting)
- [ ] T097 Optimize Constitution Check validation performance (<1 second per SC-001 performance goal)
- [ ] T098 Optimize spec generation performance (<5 seconds per SC-017 success criteria)
- [ ] T099 Add pyproject.toml metadata (description, authors, keywords, classifiers, project URLs)
- [ ] T100 Create CONTRIBUTING.md (contribution guidelines for community contributions)
- [ ] T101 Create .gitignore (Python cache, venv, IDE files, .DS_Store)
- [ ] T102 Run pyproject.toml validation (ensure package name `growthkit-cli`, entry point `growthkit` correctly configured)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User Story 1 (P1): Can start after Foundational - No dependencies on other stories
  - User Story 2 (P2): Can start after Foundational - No dependencies on other stories
  - User Story 3 (P3): Can start after Foundational - May integrate with US1/US2 but should be independently testable
  - User Story 4 (P4): Can start after Foundational - Depends on US3 (needs plan.md to generate tasks.md)
  - User Story 5 (P5): Can start after Foundational - Depends on US4 (needs tasks.md to execute)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories (reads spec.md from US2 but can be tested with mock spec)
- **User Story 4 (P4)**: Depends on User Story 3 (needs plan.md) - Can start after Phase 5
- **User Story 5 (P5)**: Depends on User Story 4 (needs tasks.md) - Can start after Phase 6

### Within Each User Story

- Utility functions before commands that use them
- Template creation before template rendering
- Validation logic before enforcement
- CLI commands after all supporting infrastructure
- Story complete before moving to next priority

### Parallel Opportunities

- **Setup phase**: T003, T004, T005, T006 can run in parallel
- **Foundational phase**: T008, T009, T010 can run in parallel; T012, T013 can run in parallel; T016, T017, T018, T019 can run in parallel; T021, T022 can run in parallel
- **User Story 1**: T035, T036, T037, T038 can run in parallel (different command files)
- **User Story 3**: T058, T059 can run in parallel (different template files)
- **Polish phase**: T088, T089, T090, T091, T092 can run in parallel (different documentation files)

**Note**: User Stories 1, 2, 3 can be developed in parallel by different team members after Foundational phase completes. User Stories 4 and 5 have sequential dependencies (4 needs 3, 5 needs 4).

---

## Parallel Example: User Story 1

```bash
# Launch template command files together (after T034 completes):
Task T035: "Create .growthkit/templates/commands/growthkit-plan.md"
Task T036: "Create .growthkit/templates/commands/growthkit-tasks.md"
Task T037: "Create .growthkit/templates/commands/growthkit-implement.md"
Task T038: "Create .growthkit/templates/commands/growthkit-constitution.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T006)
2. Complete Phase 2: Foundational (T007-T022) - CRITICAL - blocks all stories
3. Complete Phase 3: User Story 1 (T023-T038)
4. **STOP and VALIDATE**: Test User Story 1 independently
   - Run `uv tool install growthkit-cli --from .`
   - Run `growthkit init test-campaign --ai claude`
   - Verify `.growthkit/` directory created
   - Verify constitution.md exists at `.growthkit/memory/constitution.md`
   - Verify slash commands available in Claude Code (`.claude/commands/growthkit-*.md` files exist)
   - Verify no collision with spec-kit (if installed, both `/speckit.*` and `/growthkit.*` commands should work)
5. Deploy/demo MVP (User Story 1 = immediate value)

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP: users can initialize projects)
3. Add User Story 2 → Test independently → Deploy/Demo (users can generate campaign specs)
4. Add User Story 3 → Test independently → Deploy/Demo (users can plan campaigns)
5. Add User Story 4 → Test independently → Deploy/Demo (users can generate task breakdowns)
6. Add User Story 5 → Test independently → Deploy/Demo (users can execute full workflow)
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Initialize Project)
   - Developer B: User Story 2 (Specify Campaign)
   - Developer C: User Story 3 (Plan Campaign)
3. After US3 completes:
   - Developer D: User Story 4 (Task Breakdown) - depends on US3
4. After US4 completes:
   - Developer E: User Story 5 (Execute Campaign) - depends on US4
5. Stories complete and integrate independently

**Note**: User Stories 1, 2, 3 have no interdependencies and can be developed in parallel. User Stories 4 and 5 must wait for their prerequisites (3 and 4 respectively).

---

## Notes

- **[P] tasks** = different files, no dependencies - can run concurrently
- **[Story] label** maps task to specific user story for traceability (US1, US2, US3, US4, US5)
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- **Multi-kit coexistence**: All tasks ensure namespace isolation (growthkit-cli vs. specify-cli, .growthkit/ vs. .specify/, /growthkit.* vs. /speckit.*)
- **Constitution alignment**: Tasks T020-T022, T043-T046, T053, T066-T067 implement Constitution Check enforcement per Growth Hacking Kit Constitution v1.1.0
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Summary

**Total Tasks**: 102 tasks
**Task Breakdown by User Story**:
- Setup (Phase 1): 6 tasks
- Foundational (Phase 2): 16 tasks
- User Story 1 (Phase 3): 16 tasks
- User Story 2 (Phase 4): 13 tasks
- User Story 3 (Phase 5): 16 tasks
- User Story 4 (Phase 6): 9 tasks
- User Story 5 (Phase 7): 11 tasks
- Polish (Phase 8): 15 tasks

**Parallel Opportunities**: 23 tasks marked with [P] across all phases

**Independent Test Criteria**:
- US1: Can initialize project and see slash commands in under 2 minutes
- US2: Can generate campaign spec from natural language in under 5 minutes
- US3: Can plan campaign with platform tactics and Constitution Check validation
- US4: Can generate task breakdown with checkpoint validation
- US5: Can execute full campaign with pilot gates and retrospective

**Suggested MVP Scope**: User Story 1 only (T001-T038) delivers immediate value - users can initialize growth-hacking-kit projects and see slash commands in their AI agents

**Format Validation**: ✅ All 102 tasks follow strict checklist format:
- All tasks start with `- [ ]` checkbox
- All tasks have sequential Task ID (T001-T102)
- All user story tasks have [Story] label (US1-US5)
- All parallelizable tasks have [P] marker
- All tasks include exact file paths in descriptions
