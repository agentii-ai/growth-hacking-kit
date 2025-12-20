# /growthkit.implement

Execute all campaign tasks in dependency order with pilot validation gates.

## Usage

Run this command to begin systematic campaign execution.

### Example

```
/growthkit.implement
```

## What This Does

This command will:

1. **Parse `specs/###-campaign-name/tasks.md`** to extract:
   - Task list with dependencies
   - Phase structure (Setup → Pilot → Validation → Scale → Measure)
   - Checkpoint validation criteria
2. **Execute tasks in order**, respecting:
   - Sequential dependencies (Phase 1 before Phase 2)
   - Parallel opportunities marked [P]
   - Checkpoint validation gates
3. **Handle content creation**:
   - Generate platform-native content (X: 16:9 mp4, TikTok: 9:16 mp4)
   - Create tracking URLs with UTM parameters
   - Build documentation files
4. **Validate pilot results** before scaling:
   - Check k-factor against target (>0.8 minimum)
   - Verify engagement rate (>5% minimum)
   - Document results and learnings
   - **Pause execution** if validation fails
5. **Generate retrospective** at completion:
   - Actual vs. predicted metrics
   - Principles followed/violated
   - Learnings for future campaigns
   - Recommendations

## Execution Flow

```
Phase 1: Setup (1-3 days)
  ├─ T001: Create tracking infrastructure
  ├─ [P] T002: Set up analytics
  ├─ [P] T003: Design community engagement
  └─ Checkpoint: All setup complete

Phase 2: Pilot (2-4 weeks)
  ├─ T004: Create pilot content
  ├─ [P] T005: Post to platforms
  └─ Checkpoint: Collect pilot metrics

Phase 3: Validation ⚠️ PAUSE HERE
  ├─ T006: Analyze results (k-factor, engagement)
  ├─ Decision: Go/No-Go to scale?
  └─ If no-go: Halt, document why

Phase 4: Scale
  ├─ T007: Increase budget allocation
  ├─ [P] T008: Scale content production
  └─ Checkpoint: Scale successful?

Phase 5: Measure
  ├─ T009: Generate retrospective
  ├─ T010: Document learnings
  └─ Complete: Campaign finished
```

## Pilot Validation Checkpoint

If pilot results don't meet success criteria (k-factor <0.8 or engagement <5%), the command will **pause and ask**:

> "Pilot validation failed. Do you want to:"
> 1. **Halt** - Stop campaign execution
> 2. **Pivot** - Adjust creative/audience and re-pilot
> 3. **Proceed** - Scale anyway (requires justification in Constitution Tracking)

## Next Steps

After `/growthkit.implement` completes:

1. Review generated `retrospective.md` - what was learned?
2. Check metrics against 2025 benchmarks
3. Document learnings for future campaigns
4. Plan next campaign iteration (run `/growthkit.specify` again)

## Tips

- **Pilot is mandatory** - Never skip to scale without validation
- **Monitor metrics daily** during pilot phase
- **Document assumptions** - What did you expect vs. reality?
- **Be ready to pivot** - If pilot metrics are weak, adjust and re-pilot
- **Learn and iterate** - Retrospective insights feed next campaign
