# SMF SEO+GEO — Content Optimization Engine

Create content that ranks in both traditional search AND AI-powered answers. This skill guides you through the complete SEO+GEO content workflow — from keyword research to published draft — with data-driven decisions at every step.

## What It Does

- **Keyword Research**: Find low-competition, high-intent keywords
- **SERP Analysis**: Understand what Google wants for your target keyword
- **Content Outlines**: Structure articles that satisfy search intent
- **SEO-Optimized Drafts**: Write with proper heading hierarchy, internal links, and meta tags
- **GEO Optimization**: Get content cited in ChatGPT, Perplexity, Gemini, and Google AI Overviews
- **Content Refresh**: Update old posts to regain lost rankings in both traditional and AI search

## SMF Works Context

- **Domain:** smfworks.com
- **Primary services:** AI automation consulting, lead gen systems, workflow optimization
- **Content pillars:**
  1. AI tools for small business
  2. Automation workflows (Zapier, Make, n8n, OpenClaw)
  3. Lead generation systems
  4. No-code/low-code solutions
- **Target audience:** Small business owners, entrepreneurs, solopreneurs who need AI automation but don't have technical teams
- **Audience pain points:** Manual processes eating time, can't afford enterprise tools, confused by AI hype, don't know where to start with automation
- **Brand voice:** Direct, practical, skip the jargon, show don't tell, no corporate fluff
- **Key competitors to monitor:** [Add competitors]
- **Existing high-performing content:** [Add top posts for internal linking]

## Quick Start

### 1. New Article from Keyword

"Create an SEO-optimized article targeting the keyword: 'best project management software for small teams'

Target word count: 2000
Tone: Professional but approachable
Include: Comparison table, pricing section, FAQ"

### 2. Content Refresh

"Refresh this old blog post for better SEO performance:
[paste existing content]

Target keyword: [keyword]
Current issues: [dropped rankings, outdated info, etc.]
Add: Current data, new sections, better internal links"

### 3. Content Strategy

"Build a 3-month content calendar for a [industry] business targeting [audience].

Focus topics: [topic 1], [topic 2], [topic 3]
Goal: [leads/brand awareness/authority]
Output: 12 article ideas with target keywords and priority scores"

## The SEO Content Workflow

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

### Phase 3: Outline Creation

Structure for SEO success:

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
 H2: [Topic] FAQ
 H2: Conclusion (CTA + summary)
```

### Phase 4: Content Writing with E-E-A-T

**E-E-A-T Requirements (Critical for 2026):**

- **Experience:** Demonstrate firsthand knowledge. Use "we've implemented this for clients" or "in our testing..."
- **Expertise:** Cite authoritative sources, include expert quotes, reference industry data
- **Authoritativeness:** Link to SMF Works' existing content, mention credentials where relevant
- **Trustworthiness:** Include author bio, cite sources, be transparent about limitations

**SMF Works E-E-A-T Assets to Leverage:**
- Client implementations: "We've set up 50+ automation workflows..."
- Real data: "In our testing of 10 AI tools..."
- Process screenshots: "Here's our actual n8n workflow..."
- Industry expertise: "Having worked with 100+ small businesses..."

**On-Page SEO Checklist:**

- [ ] Title tag: 50-60 chars, includes keyword near front
- [ ] Meta description: 150-160 chars, compelling CTA, includes keyword
- [ ] URL slug: Short, keyword-rich, no stop words
- [ ] H1: One per page, includes keyword naturally
- [ ] H2-H6: Logical hierarchy, keywords where natural
- [ ] Internal links: 2-5 to relevant SMF Works pages
- [ ] External links: 1-3 to authoritative sources
- [ ] Images: Descriptive filenames, alt text, compressed
- [ ] Schema markup: Article, FAQ, HowTo where applicable
- [ ] Mobile-friendly: Responsive design
- [ ] Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1

**Content Quality Standards:**

- Original insights, not just rehashed content
- Expert quotes or data where possible
- Actionable takeaways in every section
- Scannable with bullet points and short paragraphs
- Multimedia: images, videos, infographics
- **People-first:** Write for humans, not search engines (Google's Helpful Content System)

**Semantic Coverage:**

Instead of "keyword density," cover related subtopics and questions:
- Google's "People Also Ask" questions
- Related searches at bottom of SERP
- Subtopics from top-ranking content
- Industry terminology and concepts

### Phase 5: Optimization & Publishing

**Pre-publish Checklist:**

- [ ] Grammar/spelling check
- [ ] Readability score (aim for 8th grade)
- [ ] Semantic coverage: Related subtopics naturally included
- [ ] Featured snippet optimization: Answer in first paragraph (40-60 words), use definition-style formatting
- [ ] Social sharing: Open Graph tags, Twitter cards
- [ ] E-E-A-T check: Author bio, citations, unique expertise demonstrated

**Post-publish:**

- Share on social media
- Build internal links from existing content
- Monitor rankings after 2-4 weeks
- Update based on performance data

## Content Refresh Strategy

When to refresh:
- Dropped 5+ positions in rankings
- Outdated information (older than 1 year)
- Competitors published better content
- Traffic declining month-over-month

Refresh process:
1. Re-analyze SERP for new competitors
2. Update statistics and examples
3. Add new sections based on content gaps
4. Improve internal linking
5. **Only update publish date if significant changes made** (Google penalizes date-only updates)
6. Resubmit to Google Search Console (manual user step)

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

Apply these in addition to standard SEO:

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

### GEO Content Checklist

Add to your standard SEO checklist:

- [ ] Answer the main question in the first 50-100 words (directly, no preamble)
- [ ] Include 3+ statistical data points with source attribution
- [ ] Add FAQ section with schema markup (5+ questions)
- [ ] Include comparison table with specific numbers
- [ ] Cite authoritative sources (industry reports, research papers, recognized brands)
- [ ] Add author bio with credentials
- [ ] Include publication date prominently
- [ ] Use clear H2/H3 structure with question-style headers
- [ ] Add "How to verify" or "What the data shows" sections
- [ ] Reference your own brand in context of expertise (when legitimate)

### Testing GEO Performance

Manual audit:
1. Search your target keyword in ChatGPT (with web browsing) and Perplexity
2. Check if your content or competitors are cited
3. Note which content format (table, bullet, paragraph) is being cited
4. Look for gaps where your content could provide better answers

**Note:** There's no Google Search Console for GEO — citation tracking requires manual checking or third-party tools.

### GEO Content Format

When drafting, signal GEO intent:

```
Article: [Title]
Target keyword: [keyword]
SEO goal: [traditional ranking target]
GEO goal: [be cited for question: "what is X?" / "how to X?" / "best X for Y"]

Include for GEO:
- Opening: Direct answer (40-60 words)
- Statistics: [3+ data points with sources]
- FAQ: [5+ questions from PAA]
- Comparison table: [with specific metrics]
- Author credentials: [relevant experience]
```

### Multi-Platform GEO

Different AI platforms cite different sources:

| Platform | Primary Source Types |
|----------|---------------------|
| **ChatGPT** | Web content, Reddit, forums, news |
| **Perplexity** | Academic, news, detailed articles |
| **Gemini/Google AI** | Google-indexed content, SGE sources |
| **Claude** | Broader training data, less real-time |

**Strategy:** Create platform-agnostic content that satisfies all — good structure, authoritative sources, and direct answers work everywhere.

---

## Technical SEO Basics

**Core Web Vitals:**
- **LCP (Largest Contentful Paint):** < 2.5 seconds
- **INP (Interaction to Next Paint):** < 200 milliseconds
- **CLS (Cumulative Layout Shift):** < 0.1

**Crawl & Index:**
- XML sitemap submitted to Google Search Console
- Robots.txt configured properly
- Canonical URLs set for duplicate content
- Noindex on thin/duplicate pages

**Structured Data:**
- Article schema for blog posts
- FAQ schema for FAQ sections
- HowTo schema for tutorials
- Organization schema for SMF Works

## Link Building Guidance

**Internal Linking:**
- Link to 2-5 relevant existing SMF Works articles
- Use descriptive anchor text (not "click here")
- Prioritize high-authority pages

**External Link Building (Manual/User-driven):**
- Guest posting on industry blogs
- Digital PR (original research, data studies)
- Broken link building

## Content Clustering & Topic Authority

Build topical authority with pillar + cluster content:

**Pillar Page:** Comprehensive guide (3,000+ words) covering broad topic
**Cluster Content:** 5-10 focused articles (1,000-2,000 words) on subtopics

**Example for SMF Works:**
- **Pillar:** "The Complete Guide to AI Automation for Small Business"
- **Cluster:**
  - "Best AI Email Automation Tools"
  - "How to Automate Lead Scoring"
  - "n8n vs Zapier: Which is Better?"
  - "AI Customer Service: Setup Guide"
  - "10 Workflow Automations to Save 10 Hours/Week"

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

**Example Output:**
"Competitor X ranks for 'AI automation examples' with a 2,000-word guide. We have no equivalent. Recommended: Create '50 AI Automation Examples for Small Business' (2,500 words, includes industry-specific breakdowns)."

## When to Spawn Subagents

Use `sessions_spawn` for:

1. **Long-form drafting** (>1,500 words)
   - Spawn writing model (e.g., ollama/kimi-k2.5:cloud) with full content brief
   - Include: target keyword, outline, SMF brand voice, internal links
   - Wait for completion, review, then publish

2. **Multi-article content calendars**
   - Spawn subagent to research and brief 12 articles
   - Output: 12 content briefs with keywords and priority scores

3. **SERP analysis at scale**
   - Spawn subagent to analyze top 10 results for 5 target keywords
   - Parallel processing saves time

4. **Content refresh batching**
   - Spawn subagent to audit 10 existing posts
   - Output: Refresh priority list with specific recommendations

**Do NOT spawn for:**
- Single paragraph responses
- Simple web searches
- Tasks requiring immediate back-and-forth
- Resource page outreach

## Success Metrics

- **Rankings:** Target top 10 for primary keyword within 8 weeks
- **Traffic:** Minimum 100 organic sessions/month per article after 3 months
- **CTR:** Above 3% average from search results
- **Engagement:** Average time on page > 2 minutes
- **Conversions:** At least 1 conversion action per 500 sessions

## Tools Integration

This skill works with:
- `web_search` — for keyword and competitor research
- `web_fetch` — for SERP analysis
- `summarize` — for competitor content analysis
- `sessions_spawn` — for drafting with writing models (use for long-form content generation)

## AI Content Considerations

With Google's stance on AI-generated content:
- Always have human review before publishing
- Add unique expertise, personal anecdotes, original research
- Avoid generic AI patterns (overly formal tone, repetitive structure)
- Ensure content demonstrates E-E-A-T
- Use AI as a starting point, not the final product

---

*SMF Works SEO Content Engine — Optimized for OpenClaw*
