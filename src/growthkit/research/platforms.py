"""Platform specifications and tactics for Growth Hacking Kit."""

# Platform specifications with format requirements and viral mechanisms
PLATFORMS = {
    "twitter": {
        "name": "X/Twitter",
        "format": "30-60s screen recording",
        "aspect_ratio": "16:9",
        "resolution": "1920x1080",
        "file_format": "mp4",
        "viral_mechanism": "Quote tweets, retweets, developer community amplification",
        "example_campaign": "Vibe coding demo with conversational narrative",
        "character_limit": 280,
        "hook_strategy": "First 3 seconds establish value proposition",
        "tone": "Conversational, authentic, humorous",
        "best_times": ["9-11 AM UTC", "3-5 PM UTC"],
    },
    "tiktok": {
        "name": "TikTok",
        "format": "15-30s vertical video",
        "aspect_ratio": "9:16",
        "resolution": "1080x1920",
        "file_format": "mp4",
        "viral_mechanism": "Duets, remixes, trending audio overlays, cross-posting",
        "example_campaign": "POV: You discovered AI that codes for you",
        "hook_strategy": "Hook in first 3 seconds, action by second 5",
        "tone": "Energetic, fast-paced, authentic, trending",
        "trending_audio": "Current trending sounds for category",
        "best_times": ["6-9 AM", "6-10 PM"],
        "editing": "Quick cuts, transitions, text overlays, trending effects",
    },
    "linkedin": {
        "name": "LinkedIn",
        "format": "Data-driven case studies, professional insights",
        "aspect_ratio": "1:1 or 16:9",
        "file_format": "pdf, mp4, or markdown",
        "viral_mechanism": "Professional sharing, credibility signals, ROI metrics",
        "example_campaign": "How [Company] reduced onboarding from 7 days to 5 minutes with AI",
        "tone": "Professional, data-driven, metric-focused",
        "key_elements": ["Problem statement", "Solution description", "Quantified results", "Lessons learned"],
        "metrics_to_highlight": ["Time saved", "Cost reduction", "User adoption rate", "Quality improvements"],
        "best_times": ["Tuesday-Thursday", "8-10 AM"],
        "engagement_strategy": "Thought leadership, industry insights, case studies",
    },
    "github": {
        "name": "GitHub",
        "format": "Code examples, integration guides, repository templates",
        "viral_mechanism": "Stars, forks, community contributions, README visibility",
        "key_elements": ["Comprehensive README.md", "Code examples", "Quick start guide", "API documentation"],
        "documentation_strategy": "Answer Density - structured tables, benchmarks, code examples",
        "example_campaign": "Open-source integration for [Product]",
        "best_practices": [
            "Clear project structure",
            "Detailed README with badges",
            "Example projects",
            "Contributing guidelines",
            "Issue templates",
        ],
        "metrics_to_track": ["Stars gained", "Forks", "Pull requests", "Open issues", "Contributors"],
    },
    "product_hunt": {
        "name": "Product Hunt",
        "format": "Demo video + product page",
        "aspect_ratio": "16:9",
        "file_format": "mp4",
        "viral_mechanism": "Upvotes, maker community engagement, launch day momentum",
        "demo_video_strategy": "Show value in first 10 seconds, feature walkthrough, use cases",
        "engagement_strategy": [
            "Maker community outreach",
            "Press kit distribution",
            "Product video with captions",
            "First-100-user incentives",
            "Live launch engagement",
        ],
        "first_100_users": "Special perks: extended trial, lifetime discount, dedicated support",
        "launch_day_strategy": "Active monitoring, rapid response to comments, AMAs, screenshots",
        "metrics_to_track": ["Upvotes", "Launch day rank", "Comments volume", "Click-through rate"],
        "best_practices": [
            "Tagline clarity",
            "Hero image quality",
            "Demo video presence",
            "Community responding",
            "Regular updates",
        ],
    },
}

# GEO (Generative Engine Optimization) guidelines for LLM citation
GEO_GUIDELINES = {
    "answer_density": {
        "definition": "Structured, data-rich content that LLMs preferentially cite",
        "techniques": [
            "Use markdown tables for comparisons and benchmarks",
            "Include specific metrics and percentages",
            "Provide concrete examples with numbers",
            "Structure with headers for easy scanning",
            "Use bullet points for key takeaways",
            "Include citations and sources",
        ],
        "example": "Instead of 'AI is fast', write: 'Reduced processing time from 3 minutes (baseline) to 12 seconds (AI-powered) = 93% improvement'",
    },
    "structured_data": {
        "definition": "Content formatted for machine parsing and citation",
        "techniques": [
            "JSON schemas in documentation",
            "Markdown tables for comparisons",
            "Ordered lists with specific outcomes",
            "Code examples with explanations",
            "FAQ sections with direct answers",
        ],
    },
    "citation_signals": {
        "definition": "Markers that increase LLM citation likelihood",
        "techniques": [
            "Academic or authoritative tone",
            "Specific dates and versions",
            "Benchmark comparisons",
            "Direct quotes and attributions",
            "Research citations",
            "Official documentation references",
        ],
    },
}

# Viral loop mechanisms
VIRAL_LOOPS = {
    "remix_loop": {
        "name": "Remix Loop",
        "description": "Users share outputs that link back to the tool with CTAs",
        "example": "Lovable.dev: Users share generated apps with 'Build Your Own' CTAs",
        "mechanics": {
            "user_action": "Create output (app, content, design)",
            "sharing_mechanism": "Share output with product branding/watermark",
            "incoming_mechanism": "Viewer sees CTA, builds own output",
            "cycle": "User → Output → Shared → New User → New Output",
        },
        "k_factor_potential": "1.0-2.0",
    },
    "integration_loop": {
        "name": "Integration Loop",
        "description": "Product inhabits user workflows, grows through stickiness",
        "example": "Cursor: Lives in VS Code fork, grows through 'Shadow Workspace' productivity",
        "mechanics": {
            "integration_point": "Product becomes part of daily workflow",
            "stickiness": "Hard to switch once integrated",
            "network_effect": "User influence → peer adoption",
            "cycle": "Workflow → Integration → Stickiness → Peer Adoption",
        },
        "k_factor_potential": "0.8-1.5",
    },
    "watermark_loop": {
        "name": "Watermark Loop",
        "description": "Free tier outputs carry product branding shared on social",
        "example": "HeyGen/Pika: Generous free tiers with branded watermarks on output videos",
        "mechanics": {
            "free_offering": "High-quality free output with product watermark",
            "sharing_incentive": "User shares to social because output is valuable",
            "discovery": "Viewers see watermark, visit product",
            "cycle": "Free Output → Watermark → Shared → Discovery → Signup",
        },
        "k_factor_potential": "0.5-1.3",
    },
}

# 2025 Growth Metrics Dashboard
GROWTH_METRICS_DASHBOARD = {
    "acceptance_rate": {
        "definition": "% of AI suggestions accepted by users",
        "benchmark": ">30%",
        "why_it_matters": "Measures product stickiness and user trust",
        "measurement": "accepted_suggestions / total_suggestions",
    },
    "time_to_wow": {
        "definition": "Seconds to reach Magic Moment (first aha moment)",
        "benchmark": "<5 minutes (300 seconds)",
        "why_it_matters": "Faster WOW = higher conversion",
        "measurement": "median(time_to_first_successful_output)",
    },
    "time_to_trust": {
        "definition": "Days until user goes to production",
        "benchmark": "<7 days",
        "why_it_matters": "Trust drives enterprise adoption",
        "measurement": "median(days_to_first_production_deployment)",
    },
    "agent_autonomy": {
        "definition": "Steps without human intervention",
        "benchmark": "5+ steps",
        "why_it_matters": "Efficiency multiplier",
        "measurement": "avg(steps_per_session_without_user_input)",
    },
    "k_factor": {
        "definition": "New users per existing user (viral coefficient)",
        "benchmark": ">1.1 (sustainable viral growth)",
        "why_it_matters": "Sustainable viral growth",
        "measurement": "new_users / inviting_users",
        "targets": {
            "minimum": 0.8,
            "sustainable": 1.1,
            "strong_viral": 1.5,
        },
    },
    "nrr": {
        "definition": "Net Revenue Retention (expansion revenue)",
        "benchmark": "106-120%",
        "why_it_matters": "Expansion > churn",
        "measurement": "(MRR_end + expansion) / MRR_start",
    },
    "time_to_first_share": {
        "definition": "Hours until user shares campaign/output on social",
        "benchmark": "<24 hours",
        "why_it_matters": "Viral loop activation speed",
        "measurement": "median(hours_from_account_creation_to_first_share)",
    },
}
