"""Constitution Check gates definitions for Growth Hacking Kit.

Gates define mandatory and advisory requirements that campaigns must meet
before planning and implementation.
"""

from dataclasses import dataclass
from enum import Enum


class GateStatus(Enum):
    """Status of a Constitution Check gate."""
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"
    SKIP = "SKIP"


class PrincipleID(Enum):
    """Growth Hacking Kit Seven Core Principles."""
    P1 = "Spec-Driven Growth"  # noqa: E741
    P2 = "Viral Loop Engineering"
    P3 = "Agent-First Architecture"
    P4 = "Measurement-First Development"
    P5 = "Multi-Platform Distribution"
    P6 = "Test-Before-Scale"
    P7 = "Community-Led Amplification"


@dataclass
class MandatoryGate:
    """Mandatory gate that MUST pass before phase 0 research."""

    gate_id: str
    principle: PrincipleID
    description: str
    validation_criteria: str
    failure_message: str

    # Mandatory gates for spec validation
    SPEC_EXISTS = "MG-001"
    GROWTH_TYPE_IDENTIFIED = "MG-002"
    TARGET_AUDIENCE_SPECIFIC = "MG-003"
    VIRAL_LOOP_DEFINED = "MG-004"
    K_FACTOR_TARGET = "MG-005"
    METRICS_DEFINED = "MG-006"
    PILOT_SCOPED = "MG-007"


@dataclass
class AdvisoryGate:
    """Advisory gate that should be checked after phase 1 design."""

    gate_id: str
    principle: PrincipleID
    description: str
    validation_criteria: str
    recommendation: str

    # Advisory gates for plan validation
    CONTENT_OPTIMIZED = "AG-001"
    PLATFORM_STRATEGY = "AG-002"
    COMMUNITY_AMPLIFICATION = "AG-003"


# Define mandatory gates
MANDATORY_GATES = {
    "spec_exists": MandatoryGate(
        gate_id="MG-001",
        principle=PrincipleID.P1,
        description="Campaign specification exists",
        validation_criteria="File specs/###-campaign-name/spec.md exists and contains user stories",
        failure_message="No campaign specification found. Run /growthkit.specify first.",
    ),
    "growth_type_identified": MandatoryGate(
        gate_id="MG-002",
        principle=PrincipleID.P1,
        description="Growth type identified (Vibe/Trust/Agentic)",
        validation_criteria="Spec.md explicitly defines growth type in requirements",
        failure_message="Growth type not identified. Must be one of: Vibe Growth, Trust Growth, Agentic Growth",
    ),
    "target_audience_specific": MandatoryGate(
        gate_id="MG-003",
        principle=PrincipleID.P1,
        description="Target audience is specific (not generic)",
        validation_criteria="Spec defines concrete target audience (e.g., 'Python backend devs using FastAPI' not 'developers')",
        failure_message="Target audience too generic. Must be specific cohort with concrete characteristics.",
    ),
    "viral_loop_defined": MandatoryGate(
        gate_id="MG-004",
        principle=PrincipleID.P2,
        description="Viral loop mechanism specified",
        validation_criteria="Spec includes at least one viral loop: Remix Loop, Integration Loop, or Watermark Loop",
        failure_message="No viral loop mechanism defined. Must specify: Remix Loop (output sharing), Integration Loop (workflow inhabitation), or Watermark Loop (branded outputs).",
    ),
    "k_factor_target": MandatoryGate(
        gate_id="MG-005",
        principle=PrincipleID.P2,
        description="k-factor target defined (>1.1 for sustainable growth)",
        validation_criteria="Spec includes primary metric with k-factor target ≥1.1",
        failure_message="k-factor target not defined or below 1.1. Sustainable viral growth requires k-factor >1.1.",
    ),
    "metrics_defined": MandatoryGate(
        gate_id="MG-006",
        principle=PrincipleID.P4,
        description="Primary, activation, and engagement metrics set",
        validation_criteria="Spec defines all three metric types with targets",
        failure_message="Missing metric definitions. Must include: primary (k-factor), activation (Time-to-Wow), engagement (daily active users).",
    ),
    "pilot_scoped": MandatoryGate(
        gate_id="MG-007",
        principle=PrincipleID.P6,
        description="Pilot phase scope defined (<10% of final budget)",
        validation_criteria="Plan includes pilot budget <10% of scale budget with success criteria",
        failure_message="Pilot phase scope not defined. Must allocate <10% of final budget to pilot validation.",
    ),
}

# Define advisory gates
ADVISORY_GATES = {
    "content_optimized": AdvisoryGate(
        gate_id="AG-001",
        principle=PrincipleID.P3,
        description="Content optimized for 'Answer Density' (structured tables, benchmarks)",
        validation_criteria="README and documentation use structured tables, metrics, benchmarks",
        recommendation="Add structured tables, data-driven examples, and benchmark comparisons to increase LLM citation likelihood.",
    ),
    "platform_strategy": AdvisoryGate(
        gate_id="AG-002",
        principle=PrincipleID.P5,
        description="Platform-specific content strategy defined",
        validation_criteria="Plan includes platform-specific tactics (X: 16:9, TikTok: 9:16, LinkedIn case studies, etc.)",
        recommendation="Define content format and viral mechanism for each target platform.",
    ),
    "community_amplification": AdvisoryGate(
        gate_id="AG-003",
        principle=PrincipleID.P7,
        description="Community-led amplification plan",
        validation_criteria="Plan includes organic reach strategy (GitHub stars, retrospective sharing, user showcase)",
        recommendation="Prioritize organic reach and community engagement over paid ads.",
    ),
}


# Complexity tracking schema
@dataclass
class ComplexityViolation:
    """Document a justified violation of a constitution principle."""

    principle: PrincipleID
    gate_id: str
    violation_description: str
    why_necessary: str
    risk_introduced: str
    monitoring_plan: str
    discontinuation_conditions: str
