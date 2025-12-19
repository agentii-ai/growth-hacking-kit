<!--
SYNC IMPACT REPORT
==================
Version Change: 1.0.0 → 1.1.0 (Minor - principle enhancements and metric additions)
Modified Principles:
  - Principle II (Viral Loop Engineering): Added specific examples from Cursor, Lovable, Pika, HeyGen
  - Principle IV (Measurement-First Development): Added 2025 Dashboard benchmarks (Acceptance Rate, Time-to-Trust, Agent Autonomy, NRR)
  - Principle V (Multi-Platform Distribution): Enhanced with platform-specific viral mechanisms and content formats
  - Principle VI (Test-Before-Scale): Added specific failure mode documentation (Pilot Purgatory, Wrapper Trap, Cost-Per-Query Suicide)
Added Sections:
  - Constitution Check Gates (explicit criteria for plan-template.md compliance)
  - Growth Metrics Dashboard (2025 benchmarks section under Principle IV)
  - Platform Viral Mechanisms (detailed tactics under Principle V)
  - Common Anti-Patterns (specific failure modes under Principle VI)
Removed Sections: None
Templates Requiring Updates:
  ✅ .specify/templates/plan-template.md (Constitution Check gates now explicitly defined)
  ✅ .specify/templates/spec-template.md (alignment confirmed - Success Criteria maps to Principle IV metrics)
  ✅ .specify/templates/tasks-template.md (alignment confirmed - user story independence supports Test-Before-Scale)
  ✅ .claude/commands/*.md (commands validated - use growthkit.* namespace per Multi-Kit Architecture Standards)
Follow-up TODOs:
  - When implementing campaigns, reference specific examples from refs/0_overview.md and refs/1_principles_for_constitution.md
  - Update campaign retrospectives with learnings that may inform future principle refinements
  - Maintain refs/ documents as living reference library with quarterly updates from latest growth research
-->

# Growth Hacking Kit Constitution

## Core Principles

### I. Spec-Driven Growth (NON-NEGOTIABLE)

Every growth campaign MUST begin with a written specification before execution. Growth campaigns must follow the spec → plan → tasks → implement workflow inherited from spec-kit.

**Rationale**: Growth hacking is complex, multi-step work requiring systematic planning. Ad-hoc execution leads to inconsistent brand voice, wasted spend, and unmeasurable outcomes. Spec-driven development ensures campaigns are documented, repeatable, and can be improved through iteration. Analysis of successful 2024-2025 AI SaaS companies (Cursor, Lovable, Harvey) shows that systematic, planned approaches outperform reactive tactics.

**Requirements**:
- Campaign specifications MUST define target audience, success metrics, and viral loops
- All growth experiments MUST be documented in `specs/###-campaign-name/spec.md`
- No implementation without an approved specification and technical plan
- Specifications MUST reference Growth Hacking Principles from refs/1_principles_for_constitution.md
- Specifications MUST identify which growth type applies: Vibe Growth (prosumer), Trust Growth (enterprise), or Agentic Growth (developer)

### II. Viral Loop Engineering

Every campaign MUST identify and design explicit viral growth loops. Growth is not an accident; it is engineered through systematic user-to-user propagation.

**Rationale**: Based on 2024-2025 analysis of successful AI SaaS products (Cursor, Lovable, Pika, HeyGen), growth comes from "viral artifacts" - outputs users share that market the product. Traditional funnel optimization is secondary to creating shareable outcomes. The most successful products engineer viral coefficients (k-factor) >1.1 through deliberate loop design.

**Requirements**:
- Specifications MUST define at least one viral loop mechanism:
  - **Remix Loop**: Users share outputs (apps, content) that link back to tool
    - *Example: Lovable.dev* - Users share app URLs with visible "Build Your Own" CTAs, creating GitHub-style fork effect
    - *Example: Canva* - "Magic Switch" outputs include remix links
  - **Integration Loop**: Product grows by inhabiting user workflows (terminal, repo, social)
    - *Example: Cursor* - Lives in VS Code fork, grows through "Shadow Workspace" stickiness
    - *Example: Notion Q&A* - Users migrate more data to make AI smarter, creating retention lock-in
  - **Watermark Loop**: Free tier outputs carry product branding
    - *Example: HeyGen/Pika* - Generous free tiers with branded outputs shared on TikTok/Instagram
    - *Example: PhotoRoom* - Background removal includes subtle branding on free tier
- Each campaign MUST measure viral coefficient (k-factor) and document in metrics
  - Target: k-factor >1.1 for sustainable viral growth
  - Minimum viable: k-factor >0.8 with clear path to >1.0
- Campaigns targeting developers MUST focus on "Vibe Coding" patterns (zero-friction creation)
  - Primary metric: Time-to-Wow <5 minutes
  - Distribution: X/Twitter screen recordings, GitHub integrations, Dev.to technical content
- Campaigns targeting enterprise MUST focus on "Trust-as-a-Service" patterns (compliance, safety)
  - Primary metric: Time-to-Trust <7 days (signup to production deployment)
  - Distribution: LinkedIn case studies, compliance documentation, verified partnerships

### III. Agent-First Architecture

Growth campaigns MUST be designed for AI agent execution and LLM-based search engines, not just human-read SEO.

**Rationale**: In 2025, discovery happens through ChatGPT, Perplexity, and agent-driven search. Traditional SEO keywords are replaced by Generative Engine Optimization (GEO) - high fact-density content that LLMs cite as ground truth. Companies like HubSpot and Notion are winning by publishing structured knowledge graphs that AI agents prefer as canonical sources.

**Requirements**:
- Campaign content MUST optimize for "Answer Density" (structured data, clear definitions, statistics)
  - Include tables, bulleted lists, concrete numbers, and definitions
  - Avoid vague marketing language; use specific, factual statements
  - Structure content for LLM citation (clear headings, scannable format)
- Documentation MUST use machine-readable formats (JSON schemas, OpenAPI specs, clear tables)
- Product MUST provide CLI/API interfaces for agent integration, not just web UIs
  - Example: Claude Code lives in terminal, reducing Time-to-Hello-World to one command
- Growth artifacts (landing pages, docs) MUST be tested against LLM citation probability
  - Validate: Ask ChatGPT/Perplexity about your product category; verify your content is cited
  - Optimize: Increase fact density if not appearing in agent responses

### IV. Measurement-First Development

Growth experiments MUST define success metrics before implementation. Vanity metrics (signups, pageviews) are forbidden without corresponding activation metrics.

**Rationale**: AI SaaS growth metrics differ from traditional SaaS. The critical metrics are "Time-to-Wow" (prosumer) and "Time-to-Trust" (enterprise), not just MAU or conversion rate. Analysis of 2024-2025 successful products shows that agent-specific metrics (Acceptance Rate, Agent Autonomy, NRR) are stronger predictors of sustainable growth than traditional funnel metrics.

**Requirements**:
- Every campaign spec MUST define:
  - **Primary metric**: The one number that defines success (e.g., Acceptance Rate >30%, Viral Coefficient >1.1)
  - **Activation metric**: Time from signup to first value delivery (e.g., Time-to-First-Deploy <7 days)
  - **Engagement metric**: Agent autonomy score, integration depth, or usage intensity
- Plans MUST include instrumentation implementation (tracking code, analytics setup)
- Post-campaign MUST document actual vs. predicted metrics and learnings

**Growth Metrics Dashboard (2025 Benchmarks)**:

| Metric | Definition | Why it Matters | Benchmark (Good) |
|--------|-----------|----------------|------------------|
| **Acceptance Rate** | % of AI suggestions accepted by user (Cursor/Copilot pattern) | Measures actual utility vs. annoyance | >30% |
| **Time-to-Wow** | Seconds from signup to first "Magic Moment" | Prosumer activation metric | <5 minutes |
| **Time-to-Trust** | Time from signup to production deployment | Enterprise activation metric | <7 days |
| **Agent Autonomy** | How many steps agent completes without human intervention | Differentiates "Chatbot" from "Agent" | 5+ steps |
| **Viral Coefficient (k-factor)** | # of new users generated per existing user | Measures viral loop effectiveness | >1.1 (sustainable viral) |
| **Expansion/NRR** | Net Revenue Retention (AI usage scales with data) | Revenue growth from existing customers | 106%-120% |
| **Time-to-First-Share** | How long until user shares output on social | Viral loop velocity | <24 hours |

### V. Multi-Platform Distribution

Growth campaigns MUST target platform-specific content formats and viral mechanisms, not generic cross-posting.

**Rationale**: In 2024-2025, successful AI products grow through platform-native content: screen recordings on X/Twitter, short-form video on TikTok, technical write-ups on Dev.to/Medium, GitHub integrations for developer tools. Generic cross-posting fails because each platform has distinct virality mechanics and content consumption patterns.

**Requirements**:
- Campaign specs MUST define target platforms and platform-specific tactics:
  - **X/Twitter**: "Vibe coding" screen recordings, thread storytelling, Magic Moments
    - *Format*: 30-60 second screen recordings showing "I just built X in Y minutes"
    - *Viral mechanism*: Quote tweets with user's own variations
    - *Example*: Cursor grew to $200M ARR with zero spend via X developer community
  - **TikTok/Instagram**: Short-form demos, before/after transformations
    - *Format*: 15-30 second "wow" moments with hook in first 3 seconds
    - *Viral mechanism*: Duets, remixes, trending audio overlays
    - *Example*: Pika/HeyGen outputs are social-first, creating automatic billboards
  - **LinkedIn**: Enterprise trust signals, case studies, compliance documentation
    - *Format*: Data-driven case studies with specific ROI metrics
    - *Viral mechanism*: Professional validation through shares and comments
    - *Example*: Harvey/Writer grow through verified enterprise success stories
  - **GitHub/Dev.to**: Technical deep-dives, integration guides, open-source tie-ins
    - *Format*: Code examples, integration walkthroughs, architectural decisions
    - *Viral mechanism*: Stars, forks, repository templates
    - *Example*: Claude Code grows through CLI integration and developer workflows
  - **Product Hunt**: Launch strategy with demo video and first-day engagement plan
    - *Format*: Concise demo video + first-100-user incentives
    - *Viral mechanism*: Upvotes and "Maker" community validation
    - *Example*: Lovable.dev leveraged PH for initial prosumer adoption
- Each platform MUST have tailored content, not automated cross-posts
- Plans MUST identify platform-specific viral mechanisms (quote tweets, duets, forks, remixes)
- Content MUST be created in platform-native formats:
  - Don't: Post YouTube link on TikTok
  - Do: Create vertical 9:16 video natively for TikTok
  - Don't: Share same text across X and LinkedIn
  - Do: Adapt tone and format (X: conversational threads; LinkedIn: professional insights)

### VI. Test-Before-Scale (TDD for Growth)

Growth experiments MUST be validated at small scale before budget allocation. Failed experiments MUST be documented as rigorously as successful ones.

**Rationale**: Most growth experiments fail. The discipline is documenting why, learning, and iterating. This is "Red-Green-Refactor" applied to marketing - test hypothesis, validate signal, scale what works. Analysis of 2024-2025 failures shows predictable anti-patterns that can be avoided through systematic pilot validation.

**Requirements**:
- Every campaign MUST have a "pilot phase" with <10% of final budget
- Pilot results MUST be documented before scaling (conversion rates, engagement, CAC)
- Failed experiments MUST document:
  - Hypothesis that was tested
  - Why it failed (creative, audience, timing, platform)
  - What was learned for future iterations
- No campaign may scale without documented pilot validation or explicit "exploratory spike" justification

**Common Anti-Patterns (2024-2025 Failure Modes)**:

1. **Pilot Purgatory (95% Enterprise AI Failure Rate)**
   - *Symptom*: Enterprise pilots succeed in sandbox but never reach production
   - *Cause*: Cannot bridge "Integration Cliff" with messy real-world data
   - *Prevention*: Pilot MUST test against production-like data complexity, not clean test sets
   - *Campaign requirement*: Enterprise campaigns MUST document integration requirements in spec

2. **The "Wrapper" Trap**
   - *Symptom*: Product is thin wrapper around GPT-4; gets crushed when model updates
   - *Cause*: No proprietary moat beyond API orchestration
   - *Prevention*: Build proprietary "Edit Prediction Models" (Cursor) or "Knowledge Graphs" (Writer/Harvey)
   - *Campaign requirement*: Marketing MUST emphasize proprietary differentiation, not just "powered by GPT-4"

3. **Cost-Per-Query Suicide**
   - *Symptom*: Agent burns $5 of compute to solve $1 problem
   - *Cause*: No model routing strategy; every query hits expensive SOTA model
   - *Prevention*: Route simple queries to cheaper models (Claude Haiku, GPT-4 Mini), complex reasoning to SOTA
   - *Campaign requirement*: Free tier economics MUST be validated in pilot; unlimited free tier is unsustainable without smart routing

4. **Generic Cross-Platform Content**
   - *Symptom*: Same video posted to YouTube, TikTok, Instagram, LinkedIn with zero engagement
   - *Cause*: No platform-native adaptation (wrong aspect ratio, wrong tone, wrong format)
   - *Prevention*: Create platform-specific content per Principle V requirements
   - *Campaign requirement*: Each platform MUST have tailored creative, not automated syndication

### VII. Community-Led Amplification

Growth campaigns MUST leverage user-generated content and community voices over paid advertising as the primary growth channel.

**Rationale**: Analysis of Cursor, Lovable, Pika, HeyGen shows that paid ads are secondary to community-driven virality. Users trust other users, not brands. The most successful AI products grew through Discord communities, X/Twitter conversations, and organic creator content. Cursor reached $200M ARR with zero marketing spend through pure community-led growth.

**Requirements**:
- Campaign specs MUST define community engagement strategy:
  - Discord/Slack community presence and moderation plan
  - User showcase programs (spotlight successful user creations)
  - Ambassador/creator partnerships (not traditional influencer sponsorships)
    - *Example*: HeyGen's "MrBeast Strategy" - partnered with top creators for translation showcase
  - Open development (public roadmap, changelog, feature voting)
    - *Example*: Lovable.dev shares real-time metrics and user success stories
- Plans MUST prioritize organic reach over paid reach (>70% budget to product/community, <30% to ads)
- User testimonials MUST be video/screen-recording format, not text quotes
  - Text quote: "This tool is great!" (low trust)
  - Video proof: Screen recording showing "I built this app in 20 minutes" (high trust)
- Community feedback loops MUST inform product iteration (not just marketing copy)
  - Example: Pika used Discord feedback to offer 8-10x more free generations than competitors
- Campaign MUST identify "Power Users" who become organic evangelists
  - Provide early access, exclusive features, or recognition (not payment)
  - Amplify their content (retweets, features, case studies)

## Multi-Kit Architecture Standards

To enable coexistence of multiple *-kit variants (spec-kit, growth-hacking-kit, pm-kit, pd-kit, blog-kit, etc.) on a single system, the following namespace and installation standards are MANDATORY:

### Namespace Isolation

**Package Names**: Each kit MUST use a unique PyPI package name to avoid installation conflicts:
- `specify-cli` (original spec-kit)
- `growthkit-cli` (this project)
- `pmkit-cli`, `pdkit-cli`, `blogkit-cli` (future variants)

**Command Namespace**: Each kit MUST use its own slash command prefix:
- Spec-kit: `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`
- Growth Hacking Kit: `/growthkit.specify`, `/growthkit.plan`, `/growthkit.tasks`, `/growthkit.implement`
- Future kits: `/pmkit.*`, `/pdkit.*`, `/blogkit.*`

**Directory Structure**: Each kit MUST use its own hidden directory to avoid file conflicts:
- Spec-kit: `.specify/`
- Growth Hacking Kit: `.growthkit/`
- Future kits: `.pmkit/`, `.pdkit/`, `.blogkit/`

**Environment Variables**: Each kit MUST use prefixed environment variables:
- Spec-kit: `SPECIFY_FEATURE`
- Growth Hacking Kit: `GROWTHKIT_CAMPAIGN`
- Future kits: `PMKIT_PROJECT`, `PDKIT_DESIGN`, etc.

### Shared Agent Integration

While directory structures and commands are isolated, agent integration files (`.claude/`, `.windsurf/`, `.cursor/`) may be shared across kits when multiple kits are installed in the same project.

**Requirements**:
- Command files in `.claude/commands/` MUST use the kit-specific prefix (e.g., `growthkit-specify.md`, not `specify.md`)
- Alternatively, use subdirectories: `.claude/commands/growthkit/specify.md`
- Agent guidance files (CLAUDE.md) MAY reference multiple kits if installed together
- Kits MUST NOT overwrite or conflict with each other's command definitions

### Installation Model

Growth Hacking Kit MUST follow the spec-kit installation patterns:

**CLI Installation**: Via `uv tool install`
```bash
uv tool install growthkit-cli --from git+https://github.com/[org]/growth-hacking-kit.git
```

**Command Structure**: CLI must support standard operations:
```bash
growthkit init <project-name>        # Initialize new project
growthkit init . --force              # Initialize in current directory
growthkit check                       # Verify dependencies
growthkit --ai claude|cursor|windsurf # Specify target agent
```

**Agent Detection**: Must check for installed agents (claude, cursor-agent, windsurf, etc.) and generate appropriate config files

## Growth Hacking Governance

### Constitution Supremacy

This constitution supersedes all ad-hoc marketing practices, growth tactics, and campaign decisions. When growth opportunities conflict with these principles, principles win.

**Rationale**: Without governance, growth hacking devolves into spammy tactics, brand inconsistency, and unsustainable user acquisition. This constitution ensures quality, repeatability, and ethical growth.

### Constitution Check Gates

When the `/growthkit.plan` command executes, the following Constitution Check gates MUST be validated:

**Mandatory Gates (MUST pass before Phase 0 research)**:
1. **Spec-Driven Growth (Principle I)**:
   - ✅ Campaign specification exists in `specs/###-campaign-name/spec.md`
   - ✅ Growth type identified (Vibe Growth, Trust Growth, or Agentic Growth)
   - ✅ Target audience defined with specificity (not "developers" but "Python backend devs using FastAPI")

2. **Viral Loop Engineering (Principle II)**:
   - ✅ At least one viral loop mechanism specified (Remix, Integration, or Watermark)
   - ✅ Viral coefficient target defined (k-factor goal)
   - ✅ Platform-specific viral mechanisms documented

3. **Measurement-First Development (Principle IV)**:
   - ✅ Primary metric defined with specific target (e.g., "Acceptance Rate >30%")
   - ✅ Activation metric defined (Time-to-Wow or Time-to-Trust)
   - ✅ Engagement metric defined (Agent Autonomy, Integration Depth, or Usage Intensity)

4. **Test-Before-Scale (Principle VI)**:
   - ✅ Pilot phase scope defined (<10% of final budget)
   - ✅ Pilot success criteria documented before implementation

**Advisory Gates (re-check after Phase 1 design)**:
1. **Agent-First Architecture (Principle III)**:
   - ⚠ Content optimized for "Answer Density" (structured data, clear definitions)
   - ⚠ LLM citation validation plan included

2. **Multi-Platform Distribution (Principle V)**:
   - ⚠ Each target platform has tailored content strategy (not generic cross-posting)
   - ⚠ Platform-specific formats documented (aspect ratios, tone, viral mechanisms)

3. **Community-Led Amplification (Principle VII)**:
   - ⚠ Organic reach prioritized over paid reach (>70% budget to product/community)
   - ⚠ User showcase or ambassador program outlined

**Complexity Justification**:
- If any mandatory gate fails, implementation is BLOCKED until justified or fixed
- If advisory gates fail, document justification in plan.md "Complexity Tracking" section

### Amendment Process

1. Amendments MUST be proposed via pull request with rationale
2. Version MUST increment per semantic versioning:
   - **MAJOR**: Breaking changes to principles (e.g., removing a core requirement)
   - **MINOR**: New principles added or material expansions
   - **PATCH**: Clarifications, examples, or non-semantic wording fixes
3. Amendment MUST update all dependent templates (spec, plan, tasks)
4. Amendment MUST include migration guidance if changing existing workflows

### Compliance Verification

- All campaign specifications MUST reference this constitution and document adherence
- `/growthkit.plan` command MUST include "Constitution Check" gate validation
- Campaign reviews MUST verify alignment with Viral Loop Engineering and Measurement-First principles
- Failed campaigns MUST document which principle was violated (if any) or what was learned
- Retrospectives MUST identify which anti-patterns (if any) contributed to failure

### Complexity Justification

Growth tactics that violate principles (e.g., paid ads without pilot validation, generic cross-posting) MUST be explicitly justified in the campaign plan:
- Why the violation is necessary
- What risk it introduces
- How it will be monitored
- Under what conditions it will be discontinued

Unjustified violations are grounds for campaign rejection.

### Continuous Improvement

This constitution is a living document. As Growth Hacking Kit is used in real campaigns:
- Document learnings in campaign retrospectives
- Propose principle refinements based on outcomes
- Update refs/ documents with new research and case studies
- Share successful patterns back to the community

Use `refs/` as the working reference library:
- `refs/0_overview.md`: Current state of AI SaaS growth (updated quarterly from latest research)
- `refs/1_principles_for_constitution.md`: Detailed principle derivations with case studies
- `refs/2_define_for_specify.md`: Guidance for campaign specification
- `refs/3_project_mangement_for_plan.md`: Guidance for campaign planning
- `refs/4_pm_tasking_for_tasks.md`: Guidance for task breakdown
- `refs/5_writing_for_optimize.md`: Guidance for content optimization
- `refs/6_claude_code.md`: Agent-specific workflow guidance
- `refs/7_optimization.md`: Performance and iteration patterns

**Version**: 1.1.0 | **Ratified**: 2025-12-19 | **Last Amended**: 2025-12-19
