# /growthkit.plan

Convert a validated campaign specification into an implementation plan.

## Usage

Run this command to create a detailed implementation plan with platform-specific tactics.

### Example

```
/growthkit.plan Use X/Twitter for vibe coding demos (30-60s 16:9 videos), TikTok for 15-second wow moments (9:16 vertical), Product Hunt for launch day momentum. Pilot budget: $500, scale budget: $5000
```

## What This Does

This command will:

1. **Generate `specs/###-campaign-name/plan.md`** containing:
   - Technical context (target platforms, budget allocation)
   - Constitution Check validation results
   - Platform-specific tactics (X/Twitter 30-60s 16:9, TikTok 15-30s 9:16, LinkedIn case studies)
   - GEO (Generative Engine Optimization) strategy
   - Pilot phase scope (<10% of budget) with success criteria
   - Complexity tracking for any constitution violations
2. **Validate mandatory gates**:
   - Campaign spec exists ✓
   - Growth type identified ✓
   - Target audience specific ✓
   - Viral loop defined ✓
   - k-factor target set ✓
   - Metrics defined ✓
   - Pilot phase scoped ✓
3. **Generate supporting documents**:
   - `research.md` - Platform API specs and GEO optimization
   - `data-model.md` - Campaign entities and relationships
   - `quickstart.md` - Installation and first-campaign guide
   - `contracts/` - CLI and slash command schemas

## Platform-Specific Tactics

### X/Twitter
- **Format**: 30-60s screen recordings, 16:9 aspect ratio
- **Viral Mechanism**: Quote tweets, developer community amplification
- **Example**: "Watch me build X in 60 seconds with [Product]"

### TikTok
- **Format**: 15-30s vertical video, 9:16 aspect ratio
- **Hook**: First 3 seconds establish value
- **Viral Mechanism**: Duets, remixes, trending audio
- **Example**: "POV: You discovered AI that codes for you"

### LinkedIn
- **Format**: Data-driven case studies with ROI metrics
- **Viral Mechanism**: Professional sharing, credibility signals
- **Example**: "How [Company] reduced onboarding from 7 days to 5 minutes"

### Product Hunt
- **Format**: Demo video + first-100-user incentives
- **Viral Mechanism**: Upvotes, maker community engagement
- **Launch Day Strategy**: Active monitoring, rapid responses, AMAs

## Next Steps

1. Review `plan.md` - ensure platform-specific tactics match your goals
2. Check Constitution Check results - mandatory gates must pass
3. Run `/growthkit.tasks` to generate task breakdown
4. Run `/growthkit.implement` to execute campaign

## Tips

- **Pilot first**: Always allocate <10% of budget to pilot validation
- **Platform-native content**: Don't reuse same content across platforms
- **GEO optimization**: Use structured tables, benchmarks, specific metrics
- **Viral loops**: Define how users discover/share campaign (Remix/Integration/Watermark)
- **K-factor targets**: Aim for >1.1 for sustainable viral growth
