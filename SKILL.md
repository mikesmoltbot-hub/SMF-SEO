# SMF SEO+GEO — Content Optimization Engine

Create content that ranks in both traditional search AND AI-powered answers. This skill guides you through the complete SEO+GEO content workflow — from keyword research to published draft — with data-driven decisions at every step.

## What It Does

- **Keyword Research**: Find low-competition, high-intent keywords
- **SERP Analysis**: Understand what Google wants for your target keyword
- **Content Outlines**: Structure articles that satisfy search intent
- **SEO-Optimized Drafts**: Write with proper heading hierarchy, internal links, and meta tags
- **GEO Optimization**: Get content cited in ChatGPT, Perplexity, Gemini, and Google AI Overviews
- **Content Refresh**: Update old posts to regain lost rankings in both traditional and AI search

---

## First-Time Setup

**On first use, this skill will launch an interactive onboarding wizard.** The AI will ask you 8 questions to customize the skill for your organization. This takes about 2-3 minutes.

**Questions will cover:**
1. Your website domain
2. Primary services/products
3. Content pillars (main topic areas)
4. Target audience description
5. Key competitors to monitor
6. Existing high-performing content (for internal linking)
7. Brand voice preferences
8. Your name/credentials (for author bylines)

**Your answers are saved locally** in `~/.smf/skills/smf-seo-gee/config.json` — never sent anywhere.

**To re-run setup:** Say "reconfigure SMF SEO" or run `smfw reconfigure smf-seo-gee`

---

## Onboarding Wizard Dialogue

When the user first invokes this skill, conduct this exact dialogue to configure it. Ask one question at a time. After all questions, save the config and confirm.

**Wizard Script:**

```
Welcome to SMF SEO+GEO! I'll configure this skill for your organization.

First, I need to ask you 8 questions. Your answers are saved locally and never sent anywhere.

Let's start:

1. What is your website domain? (e.g., example.com)
   → Store in config.organization.domain

2. What is your organization/company name?
   → Store in config.organization.name

3. What are your primary services or products? (Tell me what you offer)
   → Store in config.organization.primary_services (newline-separated list)

4. What are your main content topic areas? (Your blog categories or expertise areas)
   → Store in config.organization.content_pillars (newline-separated list)

5. Who is your target audience? (Describe your ideal customer or reader)
   → Store in config.organization.target_audience

6. What are your audience's main pain points? (What problems do they face?)
   → Store in config.organization.audience_pain_points (newline-separated list)

7. Who are your main competitors? (Websites you'd like to outrank)
   → Store in config.organization.key_competitors (newline-separated list)

8. Do you have existing high-performing content? (Pages that rank well already)
   → Store in config.organization.existing_high_performing_content (URLs or titles, newline-separated)

Now brand details:

9. How would you describe your brand voice? (e.g., 'Direct and practical' or 'Friendly and conversational')
   → Store in config.brand.voice

10. What name should appear as the author on articles?
    → Store in config.brand.author_name

11. What credentials or bio should appear with articles?
    → Store in config.brand.author_credentials

12. Default target word count for articles? (Press Enter for 2000)
    → Store in config.preferences.default_word_count (number)

That's it! Saving your configuration...
✅ Setup complete! Your SEO+GEO skill is ready.
```

**After saving, run:**
```bash
python3 ~/.smf/skills/smf-seo-gee/scripts/config_manager.py complete
```

**Re-run trigger:** If user says "reconfigure SEO" or "update SEO settings", restart the wizard from question 1.

---

## Quick Start (After Setup)

### 1. New Article from Keyword

"Create an SEO-optimized article targeting the keyword: '[your keyword]'

Target word count: [number]
Tone: [your brand voice]
Include: [comparison table / FAQ / pricing section / etc.]"

### 2. Content Refresh

"Refresh this old blog post for better SEO + GEO performance:
[paste existing content]

Target keyword: [keyword]
Current issues: [dropped rankings / outdated info / etc.]"

### 3. Content Strategy

"Build a 3-month content calendar for [industry] targeting [audience].
Focus topics: [topic 1], [topic 2], [topic 3]
Goal: [leads / brand awareness / authority]"

---

## The SEO+GEO Content Workflow

### Phase 1: Keyword Intelligence (Agent Actions)

**Input:** Seed topic or competitor URL
**Output:** Prioritized keyword list with difficulty scores

**Agent Steps:**
1. Run `web_search` with seed topic to find related queries
2. Run `web_search` with "[topic] vs" and "[topic] how to" to find long-tail variants
3. Run `web_fetch` on Google's "People Also Ask" results
4. Score keywords by: intent match × likely volume × competition signal
5. Output ranked list with reasoning for top 5 picks

**Key metrics to consider:**

- **Search Volume:** Monthly searches (higher ≠ always better)
- **Keyword Difficulty:** Competition level (start with <30 for new sites)
- **Search Intent:** Informational, navigational, transactional, commercial
- **CPC:** Cost-per-click indicates commercial value
- **Trend:** Seasonal or growing interest?

### Phase 2: SERP Analysis (Agent Actions)

Before writing, analyze the top 10 results:

**Agent Steps:**
1. `web_search` the target keyword
2. For each of the top 5 results:
   - `web_fetch` the URL
   - Extract: title, H1, H2s, approximate word count
   - Note: content type (listicle, guide, comparison)
3. Identify content gaps (topics top results miss)
4. Output: SERP analysis report with recommended angle

**What to analyze:**

- **Content Type:** Blog post? Product page? Listicle? Guide?
- **Content Depth:** Word count, sections covered, detail level
- **Content Gaps:** What's missing that you can add?
- **Common Elements:** Do all top results have videos? Tables? FAQs?
- **Domain Authority:** Are you competing with Wikipedia or small blogs?

### Phase 3: GEO Fit Assessment (Agent Actions)

**New for GEO:** Identify which questions AI engines will ask and how to structure content for citation.

**Agent Steps:**
1. `web_search` the keyword and identify "People Also Ask" questions
2. Search in ChatGPT/Perplexity (if available) for the same query
3. Identify: What direct answers is AI providing? What sources does it cite?
4. Note: Which format is being cited — paragraph, table, bullet list, FAQ?
5. Determine: Where can your content be THE cited source?

**GEO Opportunities to Look For:**
- Questions with direct factual answers (statistics, definitions)
- Comparison queries where AI summarizes options
- "How to" queries where AI provides step-by-step summaries
- FAQ sections where AI pulls individual Q&A pairs

### Phase 4: Outline Creation

Structure for SEO + GEO success:

```
H1: Target Keyword (exact or close variant)
 H2: Introduction (hook + promise + proof)
 H2: What is [Topic]? (definition for informational intent)
 H2: Why [Topic] Matters (benefits, statistics)
 H2: [Number] Best [Topic] Options (for listicles)
   H3: Option 1
   H3: Option 2
   H3: Option 3
 H2: How to Choose (buying guide section)
 H2: [Topic] FAQ (Schema: FAQ)
 H2: Conclusion (CTA + summary)
```

**GEO-Enhanced Outline Elements:**
- Add statistical callouts: "X% of businesses..." format
- Include comparison tables in the outline
- Plan FAQ section with direct-answer questions
- Mark sections where AI could cite specific data points

### Phase 5: Content Writing with E-E-A-T + GEO

**E-E-A-T Requirements (Critical for 2026):**

- **Experience:** Demonstrate firsthand knowledge. Use "we've implemented this for clients" or "in our testing..."
- **Expertise:** Cite authoritative sources, include expert quotes, reference industry data
- **Authoritativeness:** Link to your existing content, mention credentials where relevant
- **Trustworthiness:** Include author bio, cite sources, be transparent about limitations

**GEO Requirements:**

- **Direct answers first:** Answer the main question in the first 50-100 words
- **Statistics with attribution:** "According to [Source], X%..." format
- **Comparison tables:** For side-by-side comparisons (AI extracts these easily)
- **FAQ with schema:** Use question-style headers with direct answers
- **Brand mentions where relevant:** "We've helped 50+ clients..."

**Config-driven content:**
The AI reads `~/.smf/skills/smf-seo-gee/config.json` for organization-specific details:
- Domain, services, audience — used to personalize content
- Competitors — used for comparison angles
- Brand voice — used to calibrate tone
- Author credentials — used for bylines

**On-Page SEO Checklist:**

- [ ] Title tag: 50-60 chars, includes keyword near front
- [ ] Meta description: 150-160 chars, compelling CTA, includes keyword
- [ ] URL slug: Short, keyword-rich, no stop words
- [ ] H1: One per page, includes keyword naturally
- [ ] H2-H6: Logical hierarchy, keywords where natural
- [ ] Internal links: 2-5 to relevant existing pages
- [ ] External links: 1-3 to authoritative sources
- [ ] Images: Descriptive filenames, alt text, compressed
- [ ] Schema markup: Article, FAQ, HowTo where applicable
- [ ] Mobile-friendly: Responsive design
- [ ] Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1

**GEO Content Checklist:**

- [ ] Answer main question directly in first 50-100 words
- [ ] Include 3+ statistical data points with source attribution
- [ ] Add FAQ section with schema markup (5+ questions from PAA)
- [ ] Include comparison table with specific numbers
- [ ] Cite authoritative sources (industry reports, research papers)
- [ ] Add author bio with credentials
- [ ] Include publication date prominently
- [ ] Use clear H2/H3 structure with question-style headers
- [ ] Add "What the data shows" sections with specific numbers

### Phase 6: Optimization & Publishing

**Pre-publish Checklist:**

- [ ] Grammar/spelling check
- [ ] Readability score (aim for 8th grade)
- [ ] Semantic coverage: Related subtopics naturally included
- [ ] Featured snippet optimization: Answer in first paragraph (40-60 words)
- [ ] Social sharing: Open Graph tags, Twitter cards
- [ ] E-E-A-T check: Author bio, citations, unique expertise demonstrated
- [ ] GEO check: Direct answers, stats, FAQ schema verified

**Post-publish:**

- Share on social media
- Build internal links from existing content
- Monitor rankings after 2-4 weeks
- Check AI citation presence (manual ChatGPT/Perplexity audit)
- Update based on performance data

### Phase 7: Monitor & Refresh

**Tracking for SEO:**
- Rank positions in Google Search Console
- Organic traffic in analytics
- CTR from search results
- Engagement metrics (time on page, bounce rate)

**Tracking for GEO (manual):**
- Search query in ChatGPT with web browsing
- Search query in Perplexity
- Note if your content is cited
- Note which content format is being cited

**When to refresh:**
- Dropped 5+ positions in Google rankings
- AI citation lost to competitor
- Outdated statistics or information
- Competitors published better content

## GEO: Generative Engine Optimization

GEO optimizes content to be **cited** in AI-generated answers — ChatGPT, Perplexity, Gemini, Google AI Overviews. Unlike SEO (where you want clicks), GEO aims for zero-click visibility inside AI responses.

**Key insight:** GEO and SEO are complementary, not competing. The same article can rank in Google AND be cited by ChatGPT. Optimize for both.

### Why GEO Matters Now

- Zero-click searches grew from 56% to 69% since Google AI Overviews launched
- ~93% of AI Mode searches end without any click
- Your content can be the primary source for an AI answer without you receiving a single visit
- Being cited by name in AI answers = brand authority even without traffic

### GEO vs SEO

| Factor | SEO | GEO |
|--------|-----|-----|
| **Goal** | Rank in search results | Be cited in AI answers |
| **Target** | Google, Bing | ChatGPT, Perplexity, Gemini, AI Overviews |
| **Success metric** | Position ranking, CTR | Citation frequency, brand mentions |
| **Content focus** | Keywords, backlinks, meta tags | Authority signals, statistics, clear answers |
| **Traffic model** | Click-through to your site | Zero-click brand exposure |

### GEO Optimization Techniques

#### 1. Authoritative Citations
- **Name authoritative sources** — AI models favor content that cites credible sources
- **Include statistics with attribution** — "According to [Source], 73% of businesses..."
- **Reference industry leaders** — name companies, tools, experts in your space
- **Link to authoritative sources** — don't just name them, link to them

#### 2. Statistical Evidence
- AI models favor content with **quantifiable data points**
- Include: percentages, rankings, dollar amounts, timeframes
- Format as: "X% of [audience] [does something]" — easily extractable
- Add comparison tables with specific numbers

#### 3. Definitive Answers
- Answer questions **directly in the first 50-100 words**
- Use clear, declarative statements:
  - ❌ "Many businesses struggle with..."
  - ✅ "75% of small businesses fail within 5 years due to poor lead management."
- AI extracts direct answers — don't bury the point in caveats

#### 4. Structured Data & Schema
- **FAQ schema** — AI pulls answers from FAQ sections frequently
- **HowTo schema** — for tutorials and processes
- **Article schema** — helps AI categorize and cite properly
- **Organization schema** — establishes brand authority

#### 5. Semantic Content Structuring
- **Use clear question headers** — "What is X?", "How does Y work?"
- **Numbered lists for comparisons** — AI can extract and present cleanly
- **Comparison tables** — markdown/HTML tables are easily parsed
- **Bullet points for key takeaways** — scannable structure helps AI identify main points

#### 6. Natural Language Q&A
- Include "People Also Ask" questions verbatim
- Answer follow-up questions in the same section
- Cover related subtopics (semantic coverage also helps traditional SEO)

#### 7. Brand Mentions & Social Proof
- Name your brand in context of expertise: "SMF Works has implemented 50+ automation workflows..."
- Include recognizable client outcomes: "One client cut response time by 80% using..."
- Author bio with credentials helps establish authority

#### 8. Source Credibility Signals
- Include publication date (AI prefers fresh content)
- Author byline with credentials
- Citation list at bottom of article
- Links to original research/data

### Multi-Platform GEO

Different AI platforms cite different sources:

| Platform | Primary Source Types |
|----------|---------------------|
| **ChatGPT** | Web content, Reddit, forums, news |
| **Perplexity** | Academic, news, detailed articles |
| **Gemini/Google AI** | Google-indexed content, SGE sources |
| **Claude** | Broader training data, less real-time |

**Strategy:** Create platform-agnostic content that satisfies all — good structure, authoritative sources, and direct answers work everywhere.

## Content Clustering & Topic Authority

Build topical authority with pillar + cluster content:

**Pillar Page:** Comprehensive guide (3,000+ words) covering broad topic
**Cluster Content:** 5-10 focused articles (1,000-2,000 words) on subtopics

**Internal Linking Architecture:**
- All cluster posts link TO the pillar
- Pillar links TO relevant cluster posts
- Cluster posts link to each other where relevant

## Competitor Content Gap Analysis (Agent Actions)

**When:** Before writing any article
**Purpose:** Find what competitors rank for that you don't

**Agent Steps:**
1. `web_search` "site:competitor.com [your topic]" to find their top content
2. `web_fetch` 3-5 of their highest-ranking URLs
3. Extract their H2s, word count, and target keywords
4. `web_search` "[competitor] vs" and "alternatives to [competitor]" for opportunity keywords
5. Identify: What topics do they cover that you don't? What angles are they missing?
6. Output: Gap analysis report with priority content opportunities

## When to Spawn Subagents

Use `sessions_spawn` for:

1. **Long-form drafting** (>1,500 words)
   - Spawn writing model with full content brief
   - Include: target keyword, outline, brand voice from config, internal links
   - Wait for completion, review, then publish

2. **Multi-article content calendars**
   - Spawn subagent to research and brief 12 articles
   - Output: 12 content briefs with keywords and priority scores

3. **SERP analysis at scale**
   - Spawn subagent to analyze top 10 results for 5 target keywords
   - Parallel processing saves time

4. **GEO audit for multiple keywords**
   - Spawn subagent to test keyword in ChatGPT/Perplexity and report citation gaps

**Do NOT spawn for:**
- Single paragraph responses
- Simple web searches
- Tasks requiring immediate back-and-forth

## Success Metrics

**SEO Metrics:**
- **Rankings:** Target top 10 for primary keyword within 8 weeks
- **Traffic:** Minimum 100 organic sessions/month per article after 3 months
- **CTR:** Above 3% average from search results
- **Engagement:** Average time on page > 2 minutes

**GEO Metrics:**
- **Citations:** Appear in ChatGPT/Perplexity responses for target queries
- **Brand mentions:** Get named as source in AI answers
- **Authority signals:** Author bio clicks, source link clicks from AI responses

## Tools Integration

This skill works with:
- `web_search` — for keyword and competitor research
- `web_fetch` — for SERP analysis and competitor content
- `summarize` — for competitor content analysis
- `sessions_spawn` — for drafting with writing models

## Config File

Configuration is stored at: `~/.smf/skills/smf-seo-gee/config.json`

**To reconfigure:** Run `python3 ~/.smf/skills/smf-seo-gee/scripts/config_manager.py reset`

---

*SMF Works SEO+GEO Content Engine — Optimized for OpenClaw*
*Part of SMF Works Skills Library — github.com/smfworks/smfworks-skills*
