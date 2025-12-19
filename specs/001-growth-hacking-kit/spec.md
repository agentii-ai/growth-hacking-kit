# Feature Specification: Growth Hacking Kit

**Feature Branch**: `001-growth-hacking-kit`
**Created**: 2025-12-19
**Status**: Draft
**Input**: User description: "this growth-hacking-kit project is a fork of the github.com spec-kit project focused on project management for discovering and validating product-market fit for ai saas products. It must support multi-kit coexistence (spec-kit, blog-kit, pd-kit) through clean naming and namespace strategy."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Initialize Growth Campaign Project (Priority: P1)

A growth marketer or founder wants to start a systematic growth hacking campaign for their AI SaaS product using spec-driven methodology. They need to bootstrap a project with the growth-hacking-kit CLI and establish foundational principles before creating campaigns.

**Why this priority**: This is the entry point for the entire toolkit. Without successful initialization, no other workflows can function. It establishes the foundation (constitution, directory structure, agent integration) that all subsequent growth campaigns depend on.

**Independent Test**: Can be fully tested by running `growthkit init my-campaign --ai claude` and verifying that:
1. Project directory structure is created (`.growthkit/`, `specs/`, templates)
2. Constitution file exists at `.growthkit/memory/constitution.md`
3. Slash commands (`/growthkit.specify`, `/growthkit.plan`, etc.) are available in the AI agent
4. No naming conflicts occur if spec-kit is also installed on the same machine

**Acceptance Scenarios**:

1. **Given** a user has Python 3.11+ and uv installed, **When** they run `uv tool install growthkit-cli --from git+https://github.com/[org]/growth-hacking-kit.git`, **Then** the `growthkit` command is available globally without conflicting with `specify` command from spec-kit
2. **Given** the growthkit CLI is installed, **When** user runs `growthkit init my-campaign --ai claude`, **Then** a new directory `my-campaign/` is created with `.growthkit/` subdirectory (not `.specify/`)
3. **Given** a project initialized with growthkit, **When** user launches Claude Code in the project, **Then** slash commands `/growthkit.specify`, `/growthkit.plan`, `/growthkit.tasks`, `/growthkit.implement`, `/growthkit.constitution` are available
4. **Given** both spec-kit and growthkit are installed, **When** user has both `.specify/` and `.growthkit/` directories in a project, **Then** `/speckit.plan` invokes spec-kit workflow and `/growthkit.plan` invokes growthkit workflow without collision

---

### User Story 2 - Create Growth Campaign Specification (Priority: P2)

A growth marketer wants to specify a growth campaign (e.g., "Launch Product Hunt campaign for AI coding assistant") using natural language, focusing on target audience, viral loops, and success metrics without worrying about implementation details.

**Why this priority**: After initialization, campaign specification is the first creative step. It translates business goals into structured requirements that the AI agent can validate against the growth-hacking constitution. Without clear specs, campaigns lack measurable outcomes and governance.

**Independent Test**: Can be fully tested by running `/growthkit.specify Launch Product Hunt campaign with demo video, first-100-user incentives, and maker community engagement strategy` and verifying:
1. A new branch `###-product-hunt-launch` is created
2. `specs/###-product-hunt-launch/spec.md` contains user stories, functional requirements, and success metrics
3. Constitution Check validates that spec includes: viral loop mechanism, k-factor target, primary/activation/engagement metrics
4. No technical implementation details (APIs, frameworks, ad platforms) leak into the spec

**Acceptance Scenarios**:

1. **Given** a growthkit project with constitution established, **When** user runs `/growthkit.specify [campaign description]`, **Then** a new feature branch is created with pattern `###-campaign-name` and spec file is generated in `specs/###-campaign-name/spec.md`
2. **Given** a campaign specification is created, **When** the AI agent processes the description, **Then** the spec includes: target audience definition, at least one viral loop mechanism (Remix/Integration/Watermark), primary metric with target (e.g., "k-factor >1.1"), activation metric (Time-to-Wow or Time-to-Trust), and measurable success criteria
3. **Given** the spec contains ambiguous requirements, **When** the AI agent identifies gaps, **Then** at most 3 [NEEDS CLARIFICATION] markers are added for critical scope/security/UX decisions, prioritized by impact
4. **Given** a spec violates constitution principles (e.g., no viral loop defined), **When** validated, **Then** the spec fails Constitution Check with clear feedback on which principle (I-VII) was violated

---

### User Story 3 - Plan Campaign Implementation (Priority: P3)

A growth team member wants to convert a validated campaign specification into a detailed implementation plan with research, platform-specific tactics, content strategies, and task breakdown that respects the growth-hacking constitution.

**Why this priority**: Planning bridges strategy (spec) and execution (tasks). It's where platform-specific tactics (X/Twitter, TikTok, LinkedIn) are designed, GEO content is structured, and pilot phases are scoped. Without planning, teams jump to execution without validating assumptions.

**Independent Test**: Can be fully tested by running `/growthkit.plan Use X/Twitter for vibe coding demos, TikTok for 15-second wow moments, Product Hunt for launch day. Pilot budget: $500, scale budget: $5000` on an approved spec and verifying:
1. `specs/###-campaign-name/plan.md` is created with Constitution Check gate validation results
2. Plan includes: platform-specific content formats (aspect ratios, viral mechanisms), GEO-optimized content structure (Answer Density), pilot phase scope (<10% of budget), instrumentation plan (tracking metrics)
3. Constitution Check validates: all mandatory gates passed (spec exists, viral loop defined, metrics set, pilot scoped), advisory gates documented (GEO optimization, platform-specific content, community strategy)
4. No unjustified complexity violations (e.g., paid ads without pilot validation must be justified in "Complexity Tracking" section)

**Acceptance Scenarios**:

1. **Given** an approved campaign spec exists, **When** user runs `/growthkit.plan [platform and budget choices]`, **Then** a `plan.md` file is created with: technical context (target platforms, budget allocation, tools), Constitution Check section showing gate validation status, platform-specific tactics (X/Twitter: 30-60s screen recordings, TikTok: vertical 9:16 video, etc.), and pilot phase definition (<10% budget)
2. **Given** a plan includes mandatory gates, **When** Constitution Check runs, **Then** it validates: ✅ Campaign spec exists, ✅ Growth type identified (Vibe/Trust/Agentic), ✅ Target audience specific (not "developers" but "Python backend devs using FastAPI"), ✅ Viral loop mechanism specified, ✅ k-factor target defined, ✅ Primary/activation/engagement metrics set, ✅ Pilot phase scope defined
3. **Given** a plan includes paid ads without pilot validation, **When** Constitution Check runs, **Then** implementation is BLOCKED and "Complexity Tracking" section must document: why violation is necessary, what risk it introduces, how it will be monitored, under what conditions it will be discontinued
4. **Given** a plan targets TikTok, **When** platform-specific tactics are defined, **Then** plan specifies: 15-30 second format, 9:16 vertical aspect ratio, hook in first 3 seconds, viral mechanisms (duets, remixes, trending audio overlays)

---

### User Story 4 - Generate Campaign Task Breakdown (Priority: P4)

A growth team wants to convert the implementation plan into an actionable, dependency-ordered task list organized by user story (campaign phase) so tasks can be executed systematically with clear checkpoints for pilot validation.

**Why this priority**: Task breakdown transforms planning into execution. It ensures dependencies are respected (e.g., content creation before platform posting, pilot before scaling), parallel work is identified, and teams can track progress incrementally.

**Independent Test**: Can be fully tested by running `/growthkit.tasks` on a completed plan and verifying:
1. `specs/###-campaign-name/tasks.md` is created with tasks organized by campaign phase (Setup, Pilot, Scale, Measure)
2. Tasks include exact deliverables (file paths, platform posts, tracking URLs)
3. Dependency order is clear (e.g., "Create demo video" before "Post to Product Hunt", "Pilot TikTok campaign" before "Scale TikTok budget")
4. Parallel opportunities are marked with [P] for tasks that can run simultaneously (e.g., creating X/Twitter and TikTok content in parallel)

**Acceptance Scenarios**:

1. **Given** a validated campaign plan exists, **When** user runs `/growthkit.tasks`, **Then** `tasks.md` is generated with phases: Phase 1 (Setup - infrastructure, tracking, community), Phase 2 (Pilot - <10% budget execution), Phase 3 (Scale - full budget rollout), Phase 4 (Measure - retrospective and learnings)
2. **Given** tasks are organized by phase, **When** viewing the task list, **Then** each task specifies: exact deliverable (e.g., "Create 60-second screen recording showing app build in specs/001-campaign/assets/twitter-demo.mp4"), platform target (X/Twitter, TikTok, Product Hunt), metrics to track (views, engagement rate, signups), checkpoint validation criteria
3. **Given** the plan includes multiple platforms, **When** tasks are generated, **Then** parallel opportunities are marked: [P] tasks that can run concurrently (e.g., [P] Create X/Twitter content, [P] Create TikTok content, [P] Set up Product Hunt page)
4. **Given** tasks include pilot phase, **When** pilot completes, **Then** a checkpoint task requires: document pilot results (conversion rates, engagement, CAC), validate against success criteria (e.g., "k-factor >0.8"), make go/no-go decision to scale

---

### User Story 5 - Execute Campaign Implementation (Priority: P5)

A growth team member wants to execute all tasks in the correct order, respecting dependencies and pilot validation gates, with the AI agent handling content creation, platform posting, and metric tracking according to the plan.

**Why this priority**: Execution is the final step where strategy becomes reality. The AI agent systematically works through tasks, validates pilot results before scaling, and documents learnings for future campaigns.

**Independent Test**: Can be fully tested by running `/growthkit.implement` on a complete task list and verifying:
1. AI agent executes tasks in dependency order (Setup → Pilot → Validation → Scale)
2. Pilot validation checkpoint pauses execution if success criteria not met
3. Platform-specific content is created in native formats (X: .mp4 with 16:9, TikTok: .mp4 with 9:16)
4. Metrics are tracked and documented throughout execution
5. Retrospective document is created with learnings for future campaigns

**Acceptance Scenarios**:

1. **Given** a complete task list exists, **When** user runs `/growthkit.implement`, **Then** AI agent executes tasks sequentially, creates all deliverables (content files, tracking links, platform posts), validates checkpoints (pilot results before scaling), and documents progress
2. **Given** a pilot phase task completes, **When** pilot results are analyzed, **Then** execution pauses for validation: if success criteria met (e.g., k-factor >0.8, engagement rate >5%), proceed to scale; if not met, document why (creative, audience, timing, platform) and halt scaling
3. **Given** content creation tasks execute, **When** platform is X/Twitter, **Then** output format is 30-60 second .mp4 at 16:9 ratio with screen recording, captions, and "vibe coding" narrative; **When** platform is TikTok, **Then** output format is 15-30 second .mp4 at 9:16 ratio with hook in first 3 seconds
4. **Given** the campaign completes, **When** retrospective task runs, **Then** AI agent creates `specs/###-campaign-name/retrospective.md` documenting: actual vs. predicted metrics (k-factor, CAC, Time-to-First-Share), which principles were followed/violated, what was learned (creative lessons, audience insights, platform effectiveness), recommendations for future campaigns

---

### Edge Cases

- What happens when a user tries to run `/growthkit.plan` without an existing spec? (Should error with message: "No campaign specification found. Run /growthkit.specify first.")
- What happens when both spec-kit and growthkit are installed and user runs `/specify` (without prefix)? (Should error with message: "Ambiguous command. Use /speckit.specify or /growthkit.specify.")
- What happens when a campaign spec violates multiple constitution principles? (Should list all violations in Constitution Check with priority order: mandatory gates first, advisory gates second)
- What happens when a pilot fails validation but user wants to proceed anyway? (Should require explicit justification in "Complexity Tracking" section: why risk is acceptable, how failure will be monitored)
- What happens when platform APIs change (e.g., Twitter/X video specs)? (Should document in retrospective and update refs/ documents for future campaigns)
- What happens when a user installs growthkit over an existing spec-kit project? (Should detect existing `.specify/` directory, offer to migrate or coexist, create `.growthkit/` without overwriting spec-kit files)

## Requirements *(mandatory)*

### Functional Requirements

**Multi-Kit Coexistence (Critical)**

- **FR-001**: System MUST use `growthkit-cli` as PyPI package name to avoid collision with `specify-cli`
- **FR-002**: System MUST use `.growthkit/` as hidden directory for all growthkit-specific files (memory, scripts, templates)
- **FR-003**: System MUST use `/growthkit.*` namespace for all slash commands (`/growthkit.specify`, `/growthkit.plan`, `/growthkit.tasks`, `/growthkit.implement`, `/growthkit.constitution`)
- **FR-004**: System MUST detect existing spec-kit installation (`.specify/` directory) and avoid overwriting or conflicting with spec-kit files
- **FR-005**: System MUST allow both spec-kit and growthkit to coexist in the same project with independent `.specify/` and `.growthkit/` directories
- **FR-006**: System MUST use `GROWTHKIT_CAMPAIGN` environment variable (not `SPECIFY_FEATURE`) for non-Git repository feature override

**CLI Initialization**

- **FR-007**: CLI MUST support `growthkit init <project-name>` to create new project with `.growthkit/` structure
- **FR-008**: CLI MUST support `growthkit init .` or `growthkit init --here` to initialize in current directory
- **FR-009**: CLI MUST support `--ai` option to specify target agent (claude, cursor-agent, windsurf, copilot, etc.)
- **FR-010**: CLI MUST detect installed agents (claude, cursor-agent, windsurf) and generate appropriate `.claude/commands/*.md`, `.cursor/commands/*.md`, or `.windsurf/commands/*.md` files with kit-specific prefixes (e.g., `growthkit-specify.md`, not `specify.md`)
- **FR-011**: CLI MUST copy constitution template from `.growthkit/memory/constitution.md` to project on initialization
- **FR-012**: CLI MUST support `growthkit check` to verify dependencies (git, uv, python, agent CLIs)

**Campaign Specification (/growthkit.specify)**

- **FR-013**: System MUST create new branch with pattern `###-campaign-name` where ### is next available number
- **FR-014**: System MUST check remote branches, local branches, and `specs/` directories to find highest existing feature number for the campaign-name
- **FR-015**: System MUST generate `specs/###-campaign-name/spec.md` from `.growthkit/templates/spec-template.md`
- **FR-016**: System MUST validate spec against Growth Hacking Constitution principles (I-VII) and generate Constitution Check feedback
- **FR-017**: System MUST identify growth type (Vibe Growth, Trust Growth, or Agentic Growth) based on target audience and product category
- **FR-018**: System MUST extract at least one viral loop mechanism (Remix, Integration, or Watermark) from campaign description
- **FR-019**: System MUST define primary metric with target (e.g., "k-factor >1.1"), activation metric (Time-to-Wow or Time-to-Trust), and engagement metric
- **FR-020**: System MUST limit [NEEDS CLARIFICATION] markers to maximum 3, prioritized by scope > security/privacy > UX > technical details

**Campaign Planning (/growthkit.plan)**

- **FR-021**: System MUST generate `specs/###-campaign-name/plan.md` from `.growthkit/templates/plan-template.md`
- **FR-022**: System MUST include Constitution Check section with gate validation results: mandatory gates (MUST pass before Phase 0 research), advisory gates (re-check after Phase 1 design)
- **FR-023**: System MUST validate mandatory gates: ✅ Campaign spec exists, ✅ Growth type identified, ✅ Target audience specific, ✅ Viral loop mechanism specified, ✅ k-factor target defined, ✅ Primary/activation/engagement metrics set, ✅ Pilot phase scope defined
- **FR-024**: System MUST document platform-specific tactics for each target platform (X/Twitter, TikTok, LinkedIn, GitHub, Product Hunt) with format, viral mechanism, and example
- **FR-025**: System MUST define pilot phase scope (<10% of final budget) and pilot success criteria
- **FR-026**: System MUST create "Complexity Tracking" section for any constitution violations that require justification
- **FR-027**: System MUST generate `research.md` for platform best practices, content format specs, and GEO optimization research

**Task Breakdown (/growthkit.tasks)**

- **FR-028**: System MUST generate `specs/###-campaign-name/tasks.md` from `.growthkit/templates/tasks-template.md`
- **FR-029**: System MUST organize tasks by campaign phase: Setup (Phase 1), Pilot (Phase 2), Scale (Phase 3), Measure (Phase 4)
- **FR-030**: System MUST include checkpoint validation tasks after Pilot phase: document pilot results, validate against success criteria, make go/no-go decision
- **FR-031**: System MUST mark parallel tasks with [P] when tasks can run concurrently (different platforms, no dependencies)
- **FR-032**: System MUST specify exact deliverables for each task (file paths, platform posts, tracking URLs, metrics to capture)
- **FR-033**: System MUST respect dependency order: Setup → Pilot → Validation → Scale → Measure

**Campaign Execution (/growthkit.implement)**

- **FR-034**: System MUST parse `tasks.md` and execute tasks in dependency order, respecting checkpoint gates
- **FR-035**: System MUST pause execution at pilot validation checkpoint until user confirms go/no-go decision
- **FR-036**: System MUST create content in platform-native formats: X/Twitter (16:9 video, 30-60s), TikTok (9:16 video, 15-30s), LinkedIn (data-driven case studies), GitHub (code examples, READMEs)
- **FR-037**: System MUST track metrics during execution: views, engagement rate, signups, k-factor, Time-to-First-Share
- **FR-038**: System MUST generate `retrospective.md` at campaign completion documenting: actual vs. predicted metrics, principles followed/violated, learnings, recommendations

**Constitution Governance**

- **FR-039**: System MUST enforce Seven Core Principles during all workflows: I. Spec-Driven Growth, II. Viral Loop Engineering, III. Agent-First Architecture, IV. Measurement-First Development, V. Multi-Platform Distribution, VI. Test-Before-Scale, VII. Community-Led Amplification
- **FR-040**: System MUST reference `refs/0_overview.md` (2024-2025 growth landscape), `refs/1_principles_for_constitution.md` (principle derivations), `refs/2_define_for_specify.md` (campaign specification guidance) during spec/plan generation
- **FR-041**: System MUST validate campaign plans against 2025 Growth Metrics Dashboard benchmarks: Acceptance Rate >30%, Time-to-Wow <5 min, Time-to-Trust <7 days, Agent Autonomy 5+ steps, k-factor >1.1, NRR 106-120%, Time-to-First-Share <24 hours
- **FR-042**: System MUST block implementation if mandatory Constitution Check gates fail without explicit justification

### Key Entities

- **Campaign**: A growth hacking initiative with specification, plan, tasks, and retrospective. Attributes: campaign number (###), name, branch, target audience, growth type (Vibe/Trust/Agentic), viral loop mechanism, primary metric, k-factor target, budget (pilot/scale), status (draft/pilot/scale/complete)

- **Constitution**: Project governance document defining Seven Core Principles (I-VII), Constitution Check gates (mandatory/advisory), Growth Metrics Dashboard benchmarks, Multi-Kit Architecture Standards, amendment process, compliance verification rules

- **Platform Tactic**: Platform-specific content strategy for a target platform (X/Twitter, TikTok, LinkedIn, GitHub, Product Hunt). Attributes: platform name, content format (aspect ratio, duration, tone), viral mechanism (quote tweets, duets, shares, stars), example campaigns, success metrics

- **Viral Loop**: User-to-user propagation mechanism. Types: Remix Loop (users share outputs with CTAs), Integration Loop (product inhabits workflows), Watermark Loop (branded outputs on social). Attributes: loop type, k-factor target, Time-to-First-Share, user journey (User A → Agent → Output → User B)

- **Pilot Phase**: Small-scale campaign validation with <10% of final budget. Attributes: budget allocation, success criteria (k-factor, engagement rate, CAC), results documentation (actual metrics), go/no-go decision rationale

- **Retrospective**: Post-campaign learning document. Attributes: actual vs. predicted metrics (k-factor, Time-to-Wow, NRR), principles followed/violated, failure modes encountered (Pilot Purgatory, Wrapper Trap, Cost-Per-Query Suicide, Generic Cross-Platform), creative lessons, audience insights, platform effectiveness, recommendations for future campaigns

- **Growth Metrics Dashboard**: Real-time campaign performance tracking. Metrics: Acceptance Rate (% AI suggestions accepted), Time-to-Wow (seconds to Magic Moment), Time-to-Trust (days to production), Agent Autonomy (steps without intervention), k-factor (new users per existing user), NRR (Net Revenue Retention), Time-to-First-Share (hours until social post)

## Success Criteria *(mandatory)*

### Measurable Outcomes

**Multi-Kit Coexistence**

- **SC-001**: Users can install both spec-kit and growthkit on the same machine without command conflicts (100% of installations support `/speckit.*` and `/growthkit.*` coexistence)
- **SC-002**: Projects can contain both `.specify/` and `.growthkit/` directories without file collisions (100% of dual-kit projects maintain independent directory structures)
- **SC-003**: Slash command invocation is unambiguous across kits (100% of `/speckit.plan` invocations trigger spec-kit workflow, 100% of `/growthkit.plan` invocations trigger growthkit workflow)

**Campaign Specification Quality**

- **SC-004**: 90% of generated campaign specs pass Constitution Check mandatory gates on first attempt (spec exists, growth type identified, target audience specific, viral loop defined, k-factor target set, metrics defined, pilot scoped)
- **SC-005**: Campaign specs contain ≤3 [NEEDS CLARIFICATION] markers per spec (average <2 markers per spec across all campaigns)
- **SC-006**: 100% of campaign specs are technology-agnostic (no API names, framework mentions, or platform-specific implementation details in spec.md)

**Campaign Planning Accuracy**

- **SC-007**: Platform-specific tactics include correct format specs for all targeted platforms (100% of X/Twitter tactics specify 30-60s + 16:9, 100% of TikTok tactics specify 15-30s + 9:16 + hook in first 3s)
- **SC-008**: Pilot phase budget is <10% of final budget in 100% of generated plans
- **SC-009**: Constitution Check gates are validated in 100% of plans with clear pass/fail status for mandatory and advisory gates

**Task Execution Reliability**

- **SC-010**: Campaigns with pilot validation pause execution at checkpoint gate in 100% of cases, requiring explicit go/no-go decision
- **SC-011**: Task dependencies are respected in 100% of executions (Setup completes before Pilot, Pilot validates before Scale, Scale completes before Measure)
- **SC-012**: Platform-native content is created in correct formats: X/Twitter videos are 16:9, TikTok videos are 9:16, LinkedIn posts are professional case studies

**Growth Outcomes (Campaign-Level)**

- **SC-013**: Campaigns following constitution principles achieve k-factor >0.8 in pilot phase (minimum viable viral growth)
- **SC-014**: 70% of campaigns that pass pilot validation (k-factor >0.8) achieve k-factor >1.1 in scale phase (sustainable viral growth)
- **SC-015**: Retrospectives document learnings for 100% of completed campaigns (actual vs. predicted metrics, principles followed/violated, recommendations)

**User Experience**

- **SC-016**: Users can initialize a new growthkit project and see available slash commands in their AI agent in under 2 minutes
- **SC-017**: Users can generate a campaign spec from natural language description in under 5 minutes
- **SC-018**: 80% of users successfully execute a pilot campaign and make a go/no-go decision within 7 days of project initialization

**Documentation & Governance**

- **SC-019**: 100% of constitution violations in plans are explicitly justified in "Complexity Tracking" section (why necessary, risk introduced, monitoring plan, discontinuation conditions)
- **SC-020**: Constitution document is updated with campaign learnings on a quarterly basis (refs/ documents maintain 2024-2025 research currency)

## Assumptions

1. **Target Users**: Assumes users are growth marketers, founders, or product managers working on AI/LLM SaaS products who understand basic growth hacking concepts (k-factor, CAC, viral loops) but may not be technical experts

2. **AI Agent Availability**: Assumes users have access to at least one supported AI coding agent (Claude Code, Cursor, Windsurf, Copilot, etc.) and are comfortable using slash commands in conversational interfaces

3. **Platform Access**: Assumes users have accounts on target platforms (X/Twitter, TikTok, LinkedIn, Product Hunt, GitHub) and can post content programmatically or manually based on AI-generated assets

4. **Budget Constraints**: Assumes pilot phase budgets range from $100-$1000 and scale phase budgets range from $1000-$50,000, suitable for startup/SMB growth experiments (not enterprise-scale campaigns)

5. **Content Creation**: Assumes AI agents can generate video scripts, screen recordings, and social posts, but users may need to manually edit or approve content before posting (especially for brand-sensitive platforms like LinkedIn)

6. **Metrics Tracking**: Assumes users will set up basic analytics (Google Analytics, platform-native analytics, UTM parameters) to track campaign metrics; growthkit provides tracking plan but does not automatically instrument all platforms

7. **Git Workflow**: Assumes users are comfortable with Git branches and pull requests for campaign version control; campaigns follow feature-branch workflow inherited from spec-kit

8. **Multi-Kit Adoption**: Assumes some users will install multiple *-kit variants (spec-kit for software development, growthkit for marketing, pd-kit for product design) and expect clean coexistence without manual namespace management

9. **Constitution Adherence**: Assumes users value systematic, principle-driven growth over ad-hoc tactics and will respect Constitution Check gates (though explicit violation justification is allowed for exploratory campaigns)

10. **Learning Curve**: Assumes users investing in spec-driven growth methodology are willing to spend 1-2 hours learning the workflow (constitution → specify → plan → tasks → implement) before executing first campaign, trading upfront learning for long-term repeatability
