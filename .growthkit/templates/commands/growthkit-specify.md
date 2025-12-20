# /growthkit.specify

Create a campaign specification for systematic growth hacking.

## Usage

Run this command to generate a campaign specification from your campaign description.

### Basic Example

```
/growthkit.specify Launch Product Hunt campaign with demo video, first-100-user incentives, and maker community engagement strategy
```

## What This Does

This command will:

1. **Create a new feature branch** with format `###-campaign-name` (e.g., `001-product-hunt-launch`)
2. **Generate `specs/###-campaign-name/spec.md`** with:
   - User stories covering complete campaign workflow
   - Functional requirements for all campaign aspects
   - Success criteria with measurable outcomes
   - Edge case handling
3. **Run Constitution Check validation** to ensure:
   - Growth type is identified (Vibe/Trust/Agentic)
   - Target audience is specific (not generic)
   - Viral loop mechanism is defined (Remix/Integration/Watermark)
   - k-factor target is set (>1.1 for sustainable growth)
   - Metrics are defined (primary, activation, engagement)
4. **Flag ambiguous requirements** with [NEEDS CLARIFICATION] markers (max 3)
5. **Validate specification quality** against checklists

## Next Steps

Once your specification is validated:

1. Read the generated `spec.md` to understand campaign requirements
2. Review Constitution Check results - ensure all mandatory gates pass
3. Run `/growthkit.plan` to design platform-specific implementation tactics
4. Run `/growthkit.tasks` to generate actionable task breakdown
5. Run `/growthkit.implement` to execute campaign

## Tips

- Be **specific about target audience** (e.g., "junior Python devs learning FastAPI" not just "developers")
- Define **at least one viral loop** (how users share/discover the campaign)
- Include **success metrics** (what does good look like?)
- Mention **platforms** you plan to use (X/Twitter, TikTok, LinkedIn, GitHub, Product Hunt)
- Explain **why this campaign matters** to your business
