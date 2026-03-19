# SMF SEO

[![SMF Works](https://img.shields.io/badge/SMF-Works-blue)](https://smfworks.com)
[![OpenClaw](https://img.shields.io/badge/Built%20for-OpenClaw-green)](https://github.com/openclaw/openclaw)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**AI-Powered SEO Content Engine**

Create content that ranks. From keyword research to published drafts, SMF SEO guides you through the entire SEO workflow with data-driven decisions at every step.

## Overview

SMF SEO is an OpenClaw skill that automates and guides the complete SEO content creation process. It combines AI-powered research with proven SEO strategies to help you create articles that rank on Google.

### What Makes It Different

- **E-E-A-T Focused:** Built around Google's Experience, Expertise, Authoritativeness, and Trustworthiness guidelines
- **Data-Driven:** Every decision backed by SERP analysis and competitor research
- **Workflow-Based:** Step-by-step process from keyword to publication
- **People-First:** Write for humans, not just search engines

## Features

### 🔍 Keyword Intelligence
- Discover low-competition, high-intent keywords
- Analyze search volume, difficulty, and commercial value
- Find long-tail variants and related queries
- Score keywords by intent match × volume × competition

### 📊 SERP Analysis
- Analyze top 10 ranking results
- Extract content structure and depth
- Identify content gaps to exploit
- Determine what Google wants for your keyword

### 📝 Content Outlines
- Generate SEO-optimized article structures
- Proper heading hierarchy (H1 → H2 → H3)
- Include schema markup recommendations
- Internal linking strategy

### ✍️ SEO-Optimized Drafts
- E-E-A-T compliant content generation
- Proper on-page SEO (titles, meta descriptions, URLs)
- Semantic coverage of related topics
- Featured snippet optimization

### 🔄 Content Refresh
- Identify declining content
- Update outdated information
- Improve internal linking
- Regain lost rankings

### 📅 Content Strategy
- Build topical authority with pillar + cluster content
- 3-month content calendars
- Competitor gap analysis
- Priority scoring system

## The SEO Content Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    SEO Content Workflow                      │
└─────────────────────────────────────────────────────────────┘

  ┌──────────────┐
  │ 1. Keyword   │──▶ Research volume, difficulty, intent
  │ Intelligence │
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 2. SERP      │──▶ Analyze top 10 results
  │ Analysis     │     Find content gaps
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 3. Outline   │──▶ Structure with H1-H6 hierarchy
  │ Creation     │     Plan internal links
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 4. Content   │──▶ Write with E-E-A-T principles
  │ Writing      │     Add unique expertise
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 5. Optimize  │──▶ On-page SEO, schema markup
  │ & Publish    │     Social sharing tags
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │ 6. Monitor   │──▶ Track rankings & traffic
  │ & Refresh    │     Update as needed
  └──────────────┘
```

## Installation

### Prerequisites

- OpenClaw installed and running
- GitHub access for skill repository

### Install as OpenClaw Skill

```bash
# Clone to OpenClaw skills directory
git clone https://github.com/mikesmoltbot-hub/SMF-SEO.git \
  ~/.openclaw/skills/smf-seo

# Verify installation
ls ~/.openclaw/skills/smf-seo/
# Should show: SKILL.md, templates/, references/
```

### Usage

Once installed, the skill is automatically available in OpenClaw. Use it by referencing SEO content tasks:

```
"SMF SEO: Create an SEO-optimized article targeting the keyword 'best AI automation tools for small business'"
```

## Quick Start Examples

### Example 1: New Article from Keyword

**Prompt:**
```
"Create an SEO-optimized article targeting:
Keyword: 'best project management software for small teams'
Word count: 2000
Tone: Professional but approachable
Include: Comparison table, pricing section, FAQ"
```

**SMF SEO will:**
1. Research the keyword and competition
2. Analyze top-ranking content
3. Create an optimized outline
4. Draft the article with proper E-E-A-T
5. Provide on-page SEO checklist

### Example 2: Content Refresh

**Prompt:**
```
"Refresh this old blog post:
[paste existing content]

Target keyword: 'AI automation tools'
Current issues: Dropped from position 5 to 15, outdated pricing
Add: Current data, new tools released in 2026, better internal links"
```

**SMF SEO will:**
1. Analyze current SERP
2. Identify what's changed
3. Recommend specific updates
4. Provide refreshed content
5. Suggest new internal linking opportunities

### Example 3: Content Strategy

**Prompt:**
```
"Build a 3-month content calendar for SMF Works.

Content pillars:
1. AI tools for small business
2. Workflow automation (Zapier, Make, n8n)
3. Lead generation systems

Goal: Generate leads through organic search
Output: 12 article ideas with keywords and priority scores"
```

**SMF SEO will:**
1. Research each content pillar
2. Find keyword opportunities
3. Analyze competition gaps
4. Score articles by potential ROI
5. Deliver prioritized content calendar

## Configuration

### SMF Works Context (Pre-configured)

The skill comes with SMF Works branding pre-configured:

```yaml
Domain: smfworks.com
Services: AI automation consulting, lead gen systems, workflow optimization
Content Pillars:
  1. AI tools for small business
  2. Automation workflows
  3. Lead generation systems
  4. No-code/low-code solutions

Target Audience: Small business owners, entrepreneurs, solopreneurs
Pain Points:
  - Manual processes eating time
  - Can't afford enterprise tools
  - Confused by AI hype
  - Don't know where to start

Brand Voice: Direct, practical, skip the jargon, no corporate fluff
```

### Customization

To customize for your own brand, edit the context section in `SKILL.md`:

```markdown
## [Your Brand] Context

- **Domain:** yourdomain.com
- **Primary services:** [Your services]
- **Content pillars:** [Your topics]
- **Target audience:** [Your audience]
- **Brand voice:** [Your tone]
```

## The Six Phases Explained

### Phase 1: Keyword Intelligence

**Input:** Seed topic or competitor URL  
**Output:** Prioritized keyword list

**Process:**
1. Search for related queries and questions
2. Find long-tail variants ("[topic] vs", "[topic] how to")
3. Extract "People Also Ask" questions
4. Score by: intent match × volume × competition

**Key Metrics:**
- Search Volume: Monthly searches (higher ≠ always better)
- Keyword Difficulty: Competition level (<30 for new sites)
- Search Intent: Informational, navigational, transactional
- CPC: Cost-per-click indicates value
- Trend: Seasonal or growing interest

### Phase 2: SERP Analysis

**Before writing, analyze the top 10:**

- **Content Type:** Blog? Product page? Listicle?
- **Content Depth:** Word count and detail level
- **Content Gaps:** What's missing you can add?
- **Common Elements:** Videos? Tables? FAQs?
- **Domain Authority:** Competing with Wikipedia or blogs?

### Phase 3: Outline Creation

**Structure for SEO success:**

```
H1: Target Keyword (exact or close variant)
  H2: Introduction (hook + promise + proof)
  H2: What is [Topic]? (definition)
  H2: Why [Topic] Matters (benefits, stats)
  H2: [Number] Best [Topic] Options
    H3: Option 1
    H3: Option 2
  H2: How to Choose (buying guide)
  H2: FAQ
  H2: Conclusion (CTA + summary)
```

### Phase 4: Content Writing with E-E-A-T

**E-E-A-T Requirements (Critical for 2026):**

- **Experience:** "We've implemented this for 50+ clients..."
- **Expertise:** Cite authoritative sources, include data
- **Authoritativeness:** Link to existing content, show credentials
- **Trustworthiness:** Author bio, cite sources, be transparent

**On-Page SEO Checklist:**

- [ ] Title tag: 50-60 chars, keyword near front
- [ ] Meta description: 150-160 chars, compelling CTA
- [ ] URL slug: Short, keyword-rich
- [ ] H1: One per page, includes keyword
- [ ] H2-H6: Logical hierarchy
- [ ] Internal links: 2-5 to relevant pages
- [ ] External links: 1-3 to authoritative sources
- [ ] Images: Descriptive filenames, alt text
- [ ] Schema markup: Article, FAQ, HowTo
- [ ] Mobile-friendly and fast (< 2.5s LCP)

### Phase 5: Optimization & Publishing

**Pre-publish:**
- Grammar/spelling check
- Readability score (aim for 8th grade)
- Semantic coverage verified
- Featured snippet optimized
- Social sharing tags set
- E-E-A-T check complete

**Post-publish:**
- Share on social media
- Build internal links
- Submit to Google Search Console
- Monitor after 2-4 weeks

### Phase 6: Content Refresh

**When to refresh:**
- Dropped 5+ positions
- Outdated information (>1 year old)
- Competitors published better content
- Traffic declining

**Refresh process:**
1. Re-analyze SERP
2. Update statistics and examples
3. Add new sections based on gaps
4. Improve internal linking
5. Only update date if significant changes
6. Resubmit to Google Search Console

## Technical SEO Integration

### Core Web Vitals
- **LCP:** < 2.5 seconds (largest content paint)
- **INP:** < 200 milliseconds (interaction speed)
- **CLS:** < 0.1 (layout stability)

### Structured Data
- Article schema for blog posts
- FAQ schema for FAQ sections
- HowTo schema for tutorials
- Organization schema for company info

### Content Clustering

**Build topical authority:**

**Pillar Page:** Comprehensive guide (3,000+ words)
**Cluster Content:** 5-10 focused articles (1,000-2,000 words)

**Example:**
- **Pillar:** "The Complete Guide to AI Automation for Small Business"
- **Cluster:**
  - "Best AI Email Automation Tools"
  - "How to Automate Lead Scoring"
  - "n8n vs Zapier: Which is Better?"
  - "10 Workflow Automations to Save 10 Hours/Week"

## Competitor Gap Analysis

**Purpose:** Find what competitors rank for that you don't

**Process:**
1. Search "site:competitor.com [your topic]"
2. Analyze their top 3-5 ranking URLs
3. Extract H2s, word count, target keywords
4. Search "[competitor] vs" and "alternatives to [competitor]"
5. Identify: What topics do they cover? What angles are they missing?

**Example Output:**
> "Competitor X ranks for 'AI automation examples' with 2,000 words. We have no equivalent. **Recommendation:** Create '50 AI Automation Examples for Small Business' (2,500 words, industry-specific breakdowns)."

## When to Spawn Subagents

**Use `sessions_spawn` for:**

✅ Long-form drafting (>1,500 words)
- Include target keyword, outline, brand voice
- Wait for completion, review, publish

✅ Multi-article content calendars
- Research and brief 12 articles in parallel
- Output: 12 content briefs with priorities

✅ SERP analysis at scale
- Analyze top 10 for 5 keywords simultaneously
- Parallel processing saves time

✅ Content refresh batching
- Audit 10 existing posts at once
- Output: Priority refresh list

**Don't spawn for:**
- Single paragraph responses
- Simple web searches
- Tasks requiring immediate back-and-forth

## Success Metrics

| Metric | Target | Timeline |
|--------|--------|----------|
| Rankings | Top 10 for primary keyword | 8 weeks |
| Traffic | 100+ organic sessions/month | 3 months |
| CTR | Above 3% from search results | Ongoing |
| Engagement | Avg time on page > 2 minutes | Ongoing |
| Conversions | 1 per 500 sessions | Ongoing |

## AI Content Best Practices

With Google's stance on AI-generated content:

✅ **Always have human review** before publishing
✅ **Add unique expertise** — personal anecdotes, original research
✅ **Avoid generic AI patterns** — overly formal tone, repetitive structure
✅ **Demonstrate E-E-A-T** — experience, expertise, authority, trust
✅ **Use AI as starting point** — not the final product

## Tools Integration

SMF SEO works with OpenClaw tools:

- `web_search` — Keyword and competitor research
- `web_fetch` — SERP content analysis
- `summarize` — Competitor content analysis
- `sessions_spawn` — Long-form content drafting

## Troubleshooting

### Low Rankings After Publishing

**Check:**
- Is content truly better than top 10?
- Are Core Web Vitals passing?
- Is E-E-A-T clearly demonstrated?
- Are internal links built?

### Content Not Getting Indexed

**Actions:**
- Submit URL to Google Search Console
- Check robots.txt isn't blocking
- Verify noindex tag isn't present
- Build internal links to the page

### Traffic But No Conversions

**Review:**
- Is CTA clear and compelling?
- Does content match search intent?
- Is funnel optimized post-click?

## Roadmap

- [ ] Automated rank tracking integration
- [ ] Content performance dashboard
- [ ] AI-powered title/meta generation
- [ ] Automated internal linking suggestions
- [ ] Competitor monitoring alerts
- [ ] Content decay detection

## Support

- **Issues:** [GitHub Issues](https://github.com/mikesmoltbot-hub/SMF-SEO/issues)
- **Email:** michael@smfworks.com
- **Website:** [smfworks.com](https://smfworks.com)
- **OpenClaw Docs:** [docs.openclaw.ai](https://docs.openclaw.ai)

## License

MIT License - See [LICENSE](./LICENSE) for details.

---

*Part of the SMF Works Skill Library for OpenClaw*

**[Get SMF Works SEO Services →](https://smfworks.com/contact)**