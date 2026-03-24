# SMF SEO+GEO — Content Optimization Engine

**Part of:** SMF Works Skills Library — [github.com/smfworks/smfworks-skills](https://github.com/smfworks/smfworks-skills)

---

## What It Does

Create content that ranks in both traditional search AND AI-powered answers. This skill guides you through the complete SEO+GEO content workflow — from keyword research to published draft.

**Features:**
- 🔍 Keyword research with difficulty scoring
- 📊 SERP analysis of top 10 results
- 📝 SEO-optimized outlines with E-E-A-T compliance
- 🤖 GEO optimization for ChatGPT, Perplexity, Gemini citations
- 🔄 Content refresh to regain lost rankings

---

## First-Time Setup

When you first use this skill, it will launch an **interactive onboarding wizard** that asks 8 questions to customize it for your organization:

1. Your website domain
2. Primary services/products
3. Content pillars (main topic areas)
4. Target audience description
5. Key competitors to monitor
6. Existing high-performing content (for internal linking)
7. Brand voice preferences
8. Your name/credentials (for author bylines)

Your answers are saved locally at `~/.smf/skills/smf-seo-gee/config.json` — never sent anywhere.

**To reconfigure later:** Run `smfw run smf-seo-gee reconfigure`

---

## Installation

```bash
# Via SMF CLI (recommended)
smfw install smf-seo-gee

# Or manually clone to ~/.smf/skills/
git clone https://github.com/smfworks/smfworks-skills.git ~/.smf/skills/smf-seo-gee
```

---

## Usage

After setup, just tell the AI what you need:

### New Article
```
"Create an SEO-optimized article targeting the keyword: 'best project management software for small teams'
Target word count: 2000
Include: Comparison table, FAQ section"
```

### Content Refresh
```
"Refresh this blog post for better SEO + GEO performance:
[paste content]
Target keyword: [keyword]"
```

### Content Strategy
```
"Build a 3-month content calendar for a [industry] business targeting [audience]"
```

---

## SEO + GEO Workflow

The skill follows a 7-phase workflow:

```
1. Keyword Intelligence → Find low-competition, high-intent keywords
2. SERP Analysis → Analyze top 10 results for content gaps
3. GEO Fit Assessment → Identify AI citation opportunities
4. Outline Creation → Structure with SEO + GEO signals
5. Content Writing → Write with E-E-A-T + GEO principles
6. Optimize & Publish → Schema markup, FAQ, meta tags
7. Monitor & Refresh → Track rankings + AI citations
```

---

## GEO: Generative Engine Optimization

GEO optimizes your content to be **cited** in AI-generated answers — ChatGPT, Perplexity, Gemini, Google AI Overviews.

| Factor | SEO | GEO |
|--------|-----|-----|
| **Goal** | Rank in search results | Be cited in AI answers |
| **Target** | Google, Bing | ChatGPT, Perplexity, Gemini |
| **Success metric** | Position ranking, CTR | Citation frequency |

**Key GEO techniques:**
- Direct answers in first 50-100 words
- Statistical data with source attribution
- FAQ sections with schema markup
- Comparison tables with specific numbers
- Authoritative source citations

---

## Configuration

Config is stored at: `~/.smf/skills/smf-seo-gee/config.json`

```bash
# Check status
smfw run smf-seo-gee status

# Reconfigure
smfw run smf-seo-gee reconfigure

# Update specific values
smfw run smf-seo-gee update organization.domain "yoursite.com"
```

---

## Files

```
smf-seo-gee/
├── SKILL.md              # OpenClaw skill definition (this file)
├── main.py               # CLI entry point
├── scripts/
│   ├── config_manager.py # Config read/write utility
│   └── setup_wizard.py   # Interactive onboarding wizard
└── README.md             # This file
```

---

## Requirements

- OpenClaw installed and running
- Web access for keyword research (web_search, web_fetch)
- Optional: Writing model for long-form drafting (sessions_spawn)

---

## License

MIT — Part of SMF Works Skills Library
