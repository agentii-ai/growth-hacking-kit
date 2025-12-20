# Growth Hacking Kit - Troubleshooting Guide

## Common Issues and Solutions

### Installation Issues

#### Issue: `growthkit` command not found after installation

**Symptoms**: After running `pip install growthkit-cli`, the `growthkit` command is not available.

**Solutions**:

1. **Check installation**:
   ```bash
   pip show growthkit-cli
   ```

2. **Verify PATH**:
   ```bash
   which growthkit
   ```

3. **Reinstall**:
   ```bash
   pip uninstall growthkit-cli
   pip install growthkit-cli
   ```

4. **Use python module syntax**:
   ```bash
   python -m growthkit.cli.main init my-project
   ```

#### Issue: `ModuleNotFoundError: No module named 'growthkit'`

**Symptoms**: ImportError when trying to import growthkit programmatically.

**Solutions**:

1. **Install in development mode**:
   ```bash
   cd /path/to/growth-hacking-kit
   pip install -e .
   ```

2. **Check Python version**:
   ```bash
   python --version
   # Requires Python 3.11 or higher
   ```

3. **Install dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

### Project Initialization Issues

#### Issue: Git repository not initialized

**Symptoms**:
```
✗ Git initialization failed: Not a git repository
```

**Solutions**:

1. **Skip git and do it manually**:
   ```bash
   growthkit init my-project --no-git
   cd my-project
   git init
   ```

2. **Initialize existing git repo**:
   ```bash
   cd existing-repo
   growthkit init . --here --no-git
   ```

3. **Check git is installed**:
   ```bash
   git --version
   ```

#### Issue: Agent not detected

**Symptoms**:
```
⚠ No AI agent detected, defaulting to claude
```

**Solutions**:

1. **Specify agent explicitly**:
   ```bash
   growthkit init my-project --ai cursor-agent
   ```

2. **Check if agent is installed**:
   ```bash
   growthkit check
   ```

3. **Install Claude Code**:
   - Visit: https://claude.com/claude-code
   - Install the CLI tool

### Campaign Specification Issues

#### Issue: Specification validation fails

**Symptoms**:
```
✗ Specification validation failed
[FAIL] MG-001: Growth type not identified
```

**Solutions**:

1. **Check specification content**:
   - Ensure spec includes one of: "Vibe Growth", "Trust Growth", "Agentic Growth"
   - Add target audience information
   - Define viral loop (Remix, Integration, or Watermark)
   - Specify K-factor target (> 1.1)

2. **View validation details**:
   ```bash
   growthkit specify "Your campaign description" --debug
   ```

3. **Example specification requirement**:
   ```markdown
   ## Campaign Overview

   This is a **Vibe Growth** campaign targeting startup founders.

   ### Viral Loop Strategy

   Using **Remix Loop**: Users share personalized campaign versions

   ### Metrics

   - K-factor > 1.3
   - Time-to-wow < 5 minutes
   ```

#### Issue: Too many [NEEDS CLARIFICATION] markers

**Symptoms**:
```
✗ Specification has 5 clarification markers (max: 3)
```

**Solutions**:

1. **Resolve ambiguities**:
   - Replace `[NEEDS CLARIFICATION]` markers with concrete specifications
   - Max 3 markers allowed per spec

2. **Run clarify command**:
   ```bash
   growthkit clarify 001-campaign-name
   ```

### Planning Issues

#### Issue: Plan generation fails

**Symptoms**:
```
✗ Plan not found
Run /growthkit.plan first to create implementation plan
```

**Solutions**:

1. **Create specification first**:
   ```bash
   growthkit specify "Your campaign"
   growthkit plan 001-campaign-name
   ```

2. **Check spec validity**:
   ```bash
   cat specs/001-campaign-name/spec.md
   ```

3. **Debug plan generation**:
   ```bash
   growthkit plan 001-campaign-name --debug
   ```

### Task Generation Issues

#### Issue: Tasks file not created

**Symptoms**:
```
✗ Tasks file not found
Run /growthkit.tasks first to generate task breakdown
```

**Solutions**:

1. **Generate tasks from plan**:
   ```bash
   growthkit plan 001-campaign-name
   growthkit tasks 001-campaign-name
   ```

2. **Verify plan exists**:
   ```bash
   ls specs/001-campaign-name/plan.md
   ```

3. **Check plan content**:
   ```bash
   grep "Phase" specs/001-campaign-name/plan.md
   ```

#### Issue: Task IDs are not sequential

**Symptoms**: Tasks have gaps in numbering (T001, T002, T004)

**Solutions**:

1. **Regenerate tasks**:
   ```bash
   growthkit tasks 001-campaign-name --force
   ```

2. **Manual fix** (if needed):
   - Edit tasks.md
   - Renumber tasks sequentially
   - Use [P] and [CP] markers correctly

### Campaign Execution Issues

#### Issue: Cannot start campaign execution

**Symptoms**:
```
✗ Tasks file not found
Run /growthkit.tasks first to generate task breakdown
```

**Solutions**:

1. **Complete workflow first**:
   ```bash
   growthkit specify "Campaign description"
   growthkit plan 001-campaign-name
   growthkit tasks 001-campaign-name
   growthkit implement 001-campaign-name
   ```

2. **Skip interactive confirmations**:
   ```bash
   growthkit implement 001-campaign-name --force
   ```

#### Issue: Checkpoint validation fails

**Symptoms**:
```
✗ Checkpoint failed. Halting execution.
```

**Solutions**:

1. **Review checkpoint criteria**:
   - Check metrics are within target ranges
   - Verify all preceding tasks are complete
   - Ensure no blockers remain

2. **Skip checkpoint** (if needed):
   ```bash
   growthkit implement 001-campaign-name --force
   ```

3. **Check retrospective for details**:
   ```bash
   cat specs/001-campaign-name/retrospective.md
   ```

### Constitution Check Issues

#### Issue: Mandatory gate fails

**Symptoms**:
```
[FAIL] MG-002: Target audience not specified
```

**Solutions**:

1. **Review gate requirements**:
   - See API.md for gate descriptions
   - Update specification to meet requirement
   - Regenerate plan/tasks

2. **Check gate validation**:
   ```python
   from growthkit.constitution.validator import ConstitutionValidator

   validator = ConstitutionValidator()
   results = validator.validate_spec("001-campaign-name")

   for failure in results["failed_gates"]:
       print(f"{failure['gate']}: {failure['message']}")
   ```

### File System Issues

#### Issue: Campaign not found

**Symptoms**:
```
ValueError: Campaign not found: 001-campaign-name
```

**Solutions**:

1. **List existing campaigns**:
   ```bash
   ls specs/
   ```

2. **Check naming format**:
   - Must match `###-campaign-name` pattern
   - Example: `001-product-hunt-launch`

3. **Use full path**:
   ```bash
   # Instead of campaign name, use full directory name
   growthkit plan 001-product-hunt-launch
   ```

#### Issue: Permission denied on scripts

**Symptoms**:
```
Permission denied: .growthkit/scripts/bash/common.sh
```

**Solutions**:

1. **Make scripts executable**:
   ```bash
   chmod +x .growthkit/scripts/bash/*.sh
   ```

2. **Fix recursively**:
   ```bash
   chmod -R +x .growthkit/scripts/
   ```

### CLI Output Issues

#### Issue: No colored output in terminal

**Symptoms**: Output appears without colors

**Solutions**:

1. **Check if terminal supports colors**:
   ```bash
   echo $TERM
   ```

2. **Force color output**:
   ```bash
   FORCE_COLOR=1 growthkit init my-project
   ```

3. **Use --debug for more information**:
   ```bash
   growthkit init my-project --debug
   ```

### Development Issues

#### Issue: Tests fail

**Symptoms**:
```
FAILED tests/test_specify.py::test_specify_command_creates_spec_file
```

**Solutions**:

1. **Install test dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

2. **Run specific test**:
   ```bash
   pytest tests/test_specify.py -v
   ```

3. **Run with coverage**:
   ```bash
   pytest tests/ --cov=src/growthkit
   ```

4. **Debug test**:
   ```bash
   pytest tests/test_specify.py -vv -s
   ```

#### Issue: Linting errors

**Symptoms**:
```
error: One or more files failed linting
```

**Solutions**:

1. **Auto-fix with black**:
   ```bash
   black src/growthkit tests
   ```

2. **Auto-fix with ruff**:
   ```bash
   ruff check --fix src/growthkit tests
   ```

3. **Check what needs fixing**:
   ```bash
   ruff check src/growthkit
   black --check src/growthkit
   ```

### Performance Issues

#### Issue: Commands run slowly

**Symptoms**: Commands take >10 seconds to complete

**Solutions**:

1. **Check debug output**:
   ```bash
   growthkit specify "Campaign" --debug
   ```

2. **Profile execution**:
   ```bash
   python -m cProfile -s cumtime src/growthkit/cli/main.py init project --ai claude
   ```

3. **Verify system resources**:
   ```bash
   df -h  # Check disk space
   free -h  # Check memory
   ```

### Multi-Agent Issues

#### Issue: Agent command directory not created

**Symptoms**:
```
.claude/commands/ directory not found
```

**Solutions**:

1. **Manually create**:
   ```bash
   mkdir -p .claude/commands
   mkdir -p .cursor/commands
   mkdir -p .windsurf/commands
   ```

2. **Reinitialize project**:
   ```bash
   growthkit init . --here --force
   ```

#### Issue: Wrong agent directory created

**Symptoms**: `.cursor/` created instead of `.cursor-agent/`

**Solutions**:

1. **Check agent configuration**:
   ```python
   from growthkit.cli.config import AGENT_DIRS
   print(AGENT_DIRS)
   ```

2. **Manually rename**:
   ```bash
   mv .cursor .cursor-agent
   ```

## Getting Help

If you encounter issues not listed here:

1. **Check documentation**:
   - README.md - Getting started
   - docs/API.md - API reference
   - CONTRIBUTING.md - Development guide

2. **File an issue**:
   - https://github.com/agentii/growth-hacking-kit/issues
   - Include error message and reproduction steps

3. **Ask questions**:
   - https://github.com/agentii/growth-hacking-kit/discussions
   - Email: support@agentii.ai

## Debug Mode

Enable debug mode for verbose output:

```bash
growthkit init my-project --debug
growthkit specify "Campaign" --debug
growthkit plan 001-campaign --debug
growthkit tasks 001-campaign --debug
growthkit implement 001-campaign --debug
```

Debug mode includes:
- Detailed error messages with stack traces
- File system operations logging
- Configuration settings output
- Timing information for operations
- Module import information

## Performance Optimization

If experiencing slow performance:

1. **Clear Python cache**:
   ```bash
   find . -type d -name __pycache__ -exec rm -r {} +
   find . -type f -name "*.pyc" -delete
   ```

2. **Rebuild environments**:
   ```bash
   pip install --force-reinstall growthkit-cli
   ```

3. **Check disk space**:
   ```bash
   df -h
   # Free up space if <1GB available
   ```

4. **Monitor resources**:
   ```bash
   top
   # Check CPU and memory usage during execution
   ```

---

**Last Updated**: 2025-12-20
**Version**: 0.1.0
