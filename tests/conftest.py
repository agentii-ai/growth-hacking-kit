"""Pytest configuration."""

import pytest


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "integration: integration tests")
    config.addinivalue_line("markers", "unit: unit tests")
    config.addinivalue_line("markers", "slow: slow tests")


@pytest.fixture
def campaign_dir(tmp_path):
    """Create a test campaign directory structure."""
    campaign_dir = tmp_path / "001-test-campaign"
    campaign_dir.mkdir()
    (campaign_dir / "checklists").mkdir()
    (campaign_dir / "assets").mkdir()
    return campaign_dir


@pytest.fixture
def spec_file(campaign_dir):
    """Create a sample spec.md file."""
    spec_content = """# Feature Specification: Test Campaign

**Feature Branch**: `001-test-campaign`
**Status**: Draft

## User Scenarios & Testing

### User Story 1 - Test Campaign

A growth manager wants to test campaign automation.

**Acceptance Scenarios**:
1. Campaign launches on primary platform
2. Metrics are tracked automatically
3. Go/no-go decision is made

## Requirements

### Functional Requirements

- **FR-001**: System MUST support Vibe Growth campaigns
- **FR-002**: System MUST track k-factor > 1.1
- **FR-003**: System MUST measure time-to-wow < 5 minutes

## Success Criteria

- **SC-001**: Campaign completes in under 30 days
- **SC-002**: All metrics are captured
"""
    spec_file = campaign_dir / "spec.md"
    spec_file.write_text(spec_content)
    return spec_file


@pytest.fixture
def plan_file(campaign_dir):
    """Create a sample plan.md file."""
    plan_content = """# Implementation Plan: Test Campaign

**Campaign**: 001-test-campaign
**Status**: Draft

## Platform Strategy

### X/Twitter (16:9 Landscape)
- Launch primary content
- Monitor k-factor

### TikTok (9:16 Portrait)
- Secondary platform push
- Engage creators

## Technical Architecture

The plan includes platform-specific tactics and GEO optimization.

## Phase Breakdown

### Phase 1: Setup
- Prepare assets
- Configure tracking

### Phase 2: Pilot
- Launch on Twitter
- Monitor metrics

### Phase 3: Scale
- Expand to TikTok
- Optimize content

### Phase 4: Measure
- Aggregate results
- Analyze learnings
"""
    plan_file = campaign_dir / "plan.md"
    plan_file.write_text(plan_content)
    return plan_file


@pytest.fixture
def tasks_file(campaign_dir):
    """Create a sample tasks.md file."""
    tasks_content = """# Task Breakdown: Test Campaign

**Campaign**: 001-test-campaign
**Status**: Ready for execution

## Phase 1: Setup

- [ ] T001 [SETUP] Create content calendar
- [ ] T002 [SETUP] Set up platform credentials

## Phase 2: Pilot

- [ ] T003 [P] Launch on primary platform
- [ ] T004 [PILOT] Monitor metrics
- [ ] T005 [CP] Pilot Checkpoint Validation

## Phase 3: Scale

- [ ] T006 [P] Expand to secondary platforms
- [ ] T007 [P] Create platform variants
- [ ] T008 [SCALE] Monitor scale metrics

## Phase 4: Measure

- [ ] T009 [MEASURE] Aggregate final metrics
- [ ] T010 [MEASURE] Create retrospective
"""
    tasks_file = campaign_dir / "tasks.md"
    tasks_file.write_text(tasks_content)
    return tasks_file
