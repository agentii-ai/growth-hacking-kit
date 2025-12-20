"""Constitution Check validation logic for Growth Hacking Kit."""

import re
from pathlib import Path
from typing import Any

from growthkit.constitution.gates import (
    ADVISORY_GATES,
    MANDATORY_GATES,
    AdvisoryGate,
    GateStatus,
    MandatoryGate,
)
from growthkit.cli.config import get_campaign_dir


class ConstitutionValidator:
    """Validates specs and plans against Constitution Check gates."""

    def __init__(self):
        self.mandatory_gates = MANDATORY_GATES
        self.advisory_gates = ADVISORY_GATES

    def validate_spec(self, campaign: str) -> dict[str, Any]:
        """
        Validate a campaign specification against mandatory gates.

        Args:
            campaign: Campaign name (e.g., "001-product-hunt-launch")

        Returns:
            Dictionary with validation results
        """
        campaign_dir = get_campaign_dir(campaign)
        spec_file = campaign_dir / "spec.md"

        if not spec_file.exists():
            return {
                "status": GateStatus.FAIL.value,
                "passed_gates": 0,
                "failed_gates": len(self.mandatory_gates),
                "failures": [
                    {
                        "gate_id": "MG-001",
                        "gate": "spec_exists",
                        "status": GateStatus.FAIL.value,
                        "message": "Specification file not found",
                    }
                ],
            }

        # Read spec content
        spec_content = spec_file.read_text()

        results = {
            "campaign": campaign,
            "spec_file": str(spec_file),
            "passed_gates": [],
            "failed_gates": [],
            "warnings": [],
        }

        # Validate each mandatory gate
        for gate_name, gate in self.mandatory_gates.items():
            validation_result = self._validate_gate(gate_name, gate, spec_content)
            if validation_result["status"] == GateStatus.PASS.value:
                results["passed_gates"].append(validation_result)
            else:
                results["failed_gates"].append(validation_result)

        # Overall status
        results["status"] = (
            GateStatus.PASS.value
            if len(results["failed_gates"]) == 0
            else GateStatus.FAIL.value
        )

        return results

    def validate_plan(self, campaign: str) -> dict[str, Any]:
        """
        Validate a campaign plan against mandatory and advisory gates.

        Args:
            campaign: Campaign name (e.g., "001-product-hunt-launch")

        Returns:
            Dictionary with validation results
        """
        campaign_dir = get_campaign_dir(campaign)
        plan_file = campaign_dir / "plan.md"

        if not plan_file.exists():
            return {
                "status": GateStatus.FAIL.value,
                "message": "Plan file not found. Run /growthkit.plan first.",
            }

        plan_content = plan_file.read_text()

        results = {
            "campaign": campaign,
            "plan_file": str(plan_file),
            "mandatory_gates": {
                "passed": [],
                "failed": [],
            },
            "advisory_gates": {
                "passed": [],
                "failed": [],
            },
        }

        # Validate mandatory gates
        for gate_name, gate in self.mandatory_gates.items():
            validation_result = self._validate_gate(gate_name, gate, plan_content)
            if validation_result["status"] == GateStatus.PASS.value:
                results["mandatory_gates"]["passed"].append(validation_result)
            else:
                results["mandatory_gates"]["failed"].append(validation_result)

        # Validate advisory gates
        for gate_name, gate in self.advisory_gates.items():
            validation_result = self._validate_advisory_gate(
                gate_name, gate, plan_content
            )
            results["advisory_gates"][
                "passed" if validation_result["status"] == GateStatus.PASS.value else "failed"
            ].append(validation_result)

        # Overall status
        results["status"] = (
            GateStatus.PASS.value
            if len(results["mandatory_gates"]["failed"]) == 0
            else GateStatus.FAIL.value
        )

        return results

    def _validate_gate(
        self, gate_name: str, gate: MandatoryGate, content: str
    ) -> dict[str, Any]:
        """Validate a single mandatory gate."""
        # Simple regex-based validation
        validation_checks = {
            "spec_exists": lambda c: bool(re.search(r"^#\s+Feature\s+Specification", c, re.MULTILINE)),
            "growth_type_identified": lambda c: bool(
                re.search(r"(Vibe Growth|Trust Growth|Agentic Growth)", c)
            ),
            "target_audience_specific": lambda c: bool(
                re.search(r"target audience|Target audience", c)
            ),
            "viral_loop_defined": lambda c: bool(
                re.search(r"(Remix Loop|Integration Loop|Watermark Loop)", c)
            ),
            "k_factor_target": lambda c: bool(
                re.search(r"k-factor\s*[>≥]\s*[0-9.]+", c, re.IGNORECASE)
            ),
            "metrics_defined": lambda c: bool(
                re.search(r"(primary|activation|engagement)\s+metric", c, re.IGNORECASE)
            ),
            "pilot_scoped": lambda c: bool(
                re.search(r"pilot.*budget|budget.*pilot", c, re.IGNORECASE)
            ),
        }

        check_func = validation_checks.get(gate_name, lambda c: False)
        passed = check_func(content)

        return {
            "gate_id": gate.gate_id,
            "gate": gate_name,
            "principle": gate.principle.value,
            "status": GateStatus.PASS.value if passed else GateStatus.FAIL.value,
            "description": gate.description,
            "message": gate.validation_criteria if passed else gate.failure_message,
        }

    def _validate_advisory_gate(
        self, gate_name: str, gate: AdvisoryGate, content: str
    ) -> dict[str, Any]:
        """Validate a single advisory gate."""
        advisory_checks = {
            "content_optimized": lambda c: bool(
                re.search(r"\|.*\|.*\|", c)  # Tables
            ),
            "platform_strategy": lambda c: bool(
                re.search(r"(X/Twitter|TikTok|LinkedIn|GitHub|Product Hunt)", c)
            ),
            "community_amplification": lambda c: bool(
                re.search(r"(organic|community|GitHub|retrospective)", c, re.IGNORECASE)
            ),
        }

        check_func = advisory_checks.get(gate_name, lambda c: False)
        passed = check_func(content)

        return {
            "gate_id": gate.gate_id,
            "gate": gate_name,
            "principle": gate.principle.value,
            "status": GateStatus.PASS.value if passed else GateStatus.WARNING.value,
            "description": gate.description,
            "message": gate.recommendation,
        }

    def count_clarification_markers(self, campaign: str) -> dict[str, Any]:
        """
        Count [NEEDS CLARIFICATION] markers in specification.

        Args:
            campaign: Campaign name

        Returns:
            Dictionary with marker counts by priority
        """
        campaign_dir = get_campaign_dir(campaign)
        spec_file = campaign_dir / "spec.md"

        if not spec_file.exists():
            return {"count": 0, "max_allowed": 3, "status": "PASS"}

        content = spec_file.read_text()
        matches = re.findall(r"\[NEEDS CLARIFICATION[^\]]*\]", content)

        return {
            "count": len(matches),
            "max_allowed": 3,
            "status": "PASS" if len(matches) <= 3 else "FAIL",
            "markers": matches,
        }

    def extract_growth_type(self, content: str) -> dict[str, Any]:
        """
        Extract growth type from specification.

        Args:
            content: Specification content

        Returns:
            Dictionary with identified growth types
        """
        growth_types = {
            "vibe": bool(re.search(r"Vibe Growth", content)),
            "trust": bool(re.search(r"Trust Growth", content)),
            "agentic": bool(re.search(r"Agentic Growth", content)),
        }

        identified = [g_type for g_type, found in growth_types.items() if found]

        return {
            "identified_types": identified,
            "primary_type": identified[0] if identified else "unspecified",
            "count": len(identified),
        }

    def extract_viral_loop(self, content: str) -> dict[str, Any]:
        """
        Extract viral loop type from specification.

        Args:
            content: Specification content

        Returns:
            Dictionary with identified viral loops
        """
        viral_loops = {
            "remix": bool(re.search(r"Remix Loop", content)),
            "integration": bool(re.search(r"Integration Loop", content)),
            "watermark": bool(re.search(r"Watermark Loop", content)),
        }

        identified = [loop for loop, found in viral_loops.items() if found]

        return {
            "identified_loops": identified,
            "primary_loop": identified[0] if identified else "unspecified",
            "count": len(identified),
        }

    def extract_metrics(self, content: str) -> dict[str, Any]:
        """
        Extract metrics from specification.

        Args:
            content: Specification content

        Returns:
            Dictionary with identified metrics
        """
        metrics = {
            "k_factor": re.search(r"k-factor\s*[>≥]\s*([0-9.]+)", content, re.IGNORECASE),
            "time_to_wow": re.search(r"time.to.wow|time-to-wow\s*[:<]\s*(\d+)", content, re.IGNORECASE),
            "nrr": re.search(r"NRR|Net Revenue Retention\s*[=:]\s*([0-9.]+)%?", content, re.IGNORECASE),
            "primary_activation": re.search(
                r"primary.*activation|activation.*primary", content, re.IGNORECASE
            ),
            "engagement_rate": re.search(
                r"engagement\s+rate|engagement.*metric", content, re.IGNORECASE
            ),
        }

        identified = {
            name: {
                "found": bool(match),
                "value": match.group(1) if match and match.groups() else None,
            }
            for name, match in metrics.items()
        }

        return {
            "metrics": identified,
            "defined_count": sum(1 for m in identified.values() if m["found"]),
        }
