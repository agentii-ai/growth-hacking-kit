# /growthkit.tasks

Generate actionable task breakdown from campaign plan.

## Usage

Run this command to create a task list organized by campaign phases.

### Example

```
/growthkit.tasks
```

## What This Does

This command will:

1. **Parse `plan.md`** to extract:
   - Platform targets and content formats
   - Budget allocation (pilot vs. scale)
   - Success criteria and metrics
   - Tactical decisions and platform mechanics
2. **Generate `specs/###-campaign-name/tasks.md`** with tasks organized by phases:
   - **Phase 1 - Setup**: Infrastructure, tracking, community
   - **Phase 2 - Pilot**: Execute pilot with <10% budget
   - **Phase 3 - Validation**: Check results against success criteria
   - **Phase 4 - Scale**: Roll out to full budget (go/no-go decision)
   - **Phase 5 - Measure**: Track metrics, generate learnings
3. **Mark parallel opportunities** with [P] for concurrent execution
4. **Specify exact deliverables** (file paths, platform posts, tracking URLs)
5. **Define dependency order** (Setup → Pilot → Validation → Scale → Measure)

## Task Structure

```
- [ ] T001 [Phase 1] Setup description with exact deliverables
- [ ] T002 [P] [Phase 1] Parallel task - can run with T001
- [ ] T003 [Phase 2] Pilot task - depends on Phase 1 completion
```

## Next Steps

1. Review `tasks.md` - verify task sequence makes sense
2. Check for parallel opportunities marked with [P]
3. Identify dependencies - ensure setup completes before pilot
4. Run `/growthkit.implement` to execute all tasks in order

## Tips

- **Phase 1 (Setup)**: Should complete in 1-3 days
- **Phase 2 (Pilot)**: Run for 2-4 weeks with <10% budget
- **Phase 3 (Validation)**: Pause here - evaluate results before scaling
- **[P] tasks**: Can run in parallel to speed execution
- **Exact deliverables**: Each task should specify what file/post/URL it creates
