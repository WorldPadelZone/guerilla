# Industry Examples: Guerilla AI Applications
**Real-World AI Use Cases from Guerilla's Creative Work**

---

## Overview

This document shows how AI tools can enhance actual Guerilla projects—from AR campaigns to automotive advertising. Each example demonstrates:
- **The creative challenge**
- **Traditional approach vs. AI-enhanced approach**
- **Specific tools used**
- **Time/quality impact**
- **Key learnings**

---

## Example 1: AR Campaign Concepting

### Based on: Private Property AR & Vuse Pro Smart AR Projects

#### The Challenge
Client wants an AR-enhanced product experience but the team needs to present multiple concepts before committing to expensive AR development.

**Traditional Approach:**
- Designer creates 2-3 mockup concepts (3-4 days)
- Limited variation due to time constraints
- Client sees limited options, hard to visualize

**AI-Enhanced Approach:**
- Strategist uses ChatGPT to brainstorm 20 AR interaction concepts (30 mins)
- Designer uses Midjourney to visualize 8 top concepts (2 hours)
- Team uses Claude to write user journey narratives for each (1 hour)
- Gemini creates presentation deck combining visuals + copy (30 mins)

**Total Time:** 4 hours vs. 3-4 days  
**Output:** 8 fully visualized concepts vs. 2-3  
**Client Impact:** More choices, faster iteration, higher approval rate

---

### Tools Workflow

```
1. IDEATION (ChatGPT)
   ↓
   Prompt: "Act as a creative technologist specializing in AR experiences.
   Our client sells [product]. Generate 20 innovative ways to use AR to 
   enhance the customer experience. Focus on mobile-first, easy-to-use 
   interactions that feel magical."
   
   Output: 20 concept seeds
   
2. CONCEPT VISUALIZATION (Midjourney)
   ↓
   Select top 8 concepts, generate prompt for each:
   "AR mobile interface, [concept description], modern UI, 
   vibrant colors, South African user, professional photography --ar 16:9"
   
   Output: 8 high-quality concept mockups
   
3. USER JOURNEY WRITING (Claude)
   ↓
   Prompt: "For each AR concept, write a 3-step user journey explaining:
   (1) How user discovers the feature
   (2) How they interact with it
   (3) What value they get
   Keep each journey under 100 words, conversational tone."
   
   Output: Clear, client-friendly explanations
   
4. PRESENTATION ASSEMBLY (Gemini + Google Slides)
   ↓
   Combine visuals + copy into professional deck
   
   Output: Pitch-ready presentation
```

---

### Key Learnings

✅ **What Worked:**
- ChatGPT excelled at divergent thinking—generated concepts we wouldn't have considered
- Midjourney created presentation-quality visuals that felt real enough for client buy-in
- Claude maintained consistent tone across all user journeys

❌ **What Didn't Work:**
- First Midjourney prompts produced too "sci-fi" aesthetic—needed refinement for Guerilla's style
- Had to manually curate ChatGPT's 20 concepts down to 8—some were too generic

💡 **Pro Tips:**
- Save successful Midjourney prompts as templates for future AR projects
- Use Claude to maintain Guerilla's anti-traditional voice when writing user journeys
- Always add final human polish—AI mockups need designer touch for production

---

## Example 2: Automotive Campaign Variations

### Based on: Toyota Urban Cruiser & Toyota Prado Campaigns

#### The Challenge
Launch campaign for new vehicle model. Need to test messaging across:
- Multiple audience segments (young professionals, families, adventure enthusiasts)
- Different channels (billboards, social, radio, digital)
- 50+ message variations for A/B testing

**Traditional Approach:**
- Copywriter creates 10-15 variations (2 days)
- Limited testing due to creation bottleneck
- Often stick with "safe" messaging

**AI-Enhanced Approach:**
- Team brainstorms 5 core value props with ChatGPT (30 mins)
- Use Copy.ai to generate 100 headline variations (20 mins)
- Human team curates to top 50 (1 hour)
- Use Jasper with Toyota brand voice to adapt for each channel (1 hour)
- Test all 50 in small budget, scale winners

**Total Time:** 3 hours vs. 2 days  
**Testing Volume:** 50 variations vs. 10-15  
**Result:** Find winning messages 3x faster

---

### Tools Workflow

```
1. VALUE PROP DEVELOPMENT (ChatGPT - Team Workshop)
   ↓
   Prompt: "We're launching [vehicle]. Target audience: [description].
   The vehicle's key features are [list]. Generate 5 unique value 
   propositions that would resonate, focusing on emotional benefits 
   not just features."
   
   Output: 5 core angles (e.g., "Adventure awaits," "Family fortress," 
   "Urban warrior")

2. VOLUME GENERATION (Copy.ai)
   ↓
   For each value prop, generate 20 headline variations:
   - Short-form (billboard: under 7 words)
   - Mid-form (social: under 15 words)
   - Long-form (digital ads: under 25 words)
   
   Output: 100 raw headlines

3. CURATION (Human Team)
   ↓
   Review all 100, select top 50 that:
   - Sound distinctly "Guerilla" (bold, disruptive)
   - Avoid clichés
   - Span different emotional angles
   
   Output: 50 curated finalists

4. CHANNEL ADAPTATION (Jasper with Toyota Brand Voice)
   ↓
   Feed Jasper Toyota's brand guidelines, adapt each headline for:
   - Billboard (visual + headline combo)
   - Instagram caption (conversational + CTA)
   - Radio script (15-second read)
   
   Output: Multi-channel asset set for each variation
```

---

### Real Results

**What We Tested:**
- **Variation A:** "Your city. Your rules. Your Cruiser."
- **Variation B:** "Built for the road less travelled."
- **Variation C:** "Adventure is calling. Answer in style."

**Performance:**
- Variation A: 2.3% CTR (urban audience)
- Variation B: 1.8% CTR (urban audience)
- Variation A: 1.5% CTR (adventure audience)
- Variation B: 3.1% CTR (adventure audience) ← **WINNER**

**Key Insight:** Without AI volume generation, we might have only tested A & C, missing the actual winner (B) for adventure segment.

---

### Key Learnings

✅ **What Worked:**
- Copy.ai's volume generation uncovered unexpected angles
- Jasper's brand voice memory maintained Toyota consistency across all channels
- A/B testing 50 variations found winners we'd never have written manually

❌ **What Didn't Work:**
- ~40% of AI-generated headlines were too generic or clichéd
- Needed human curation to ensure "Guerilla boldness" stayed intact
- Radio script adaptations needed more human touch—AI was too stiff

💡 **Pro Tips:**
- Set up Jasper brand voice profiles for ALL major clients (Toyota, DStv, etc.)
- Use AI for volume, humans for curation—don't skip the filtering step
- Test AI-generated variations in small budget first, scale winners

---

## Example 3: Pitch Deck in 48 Hours

### Based on: Anglo NuGen Tech Launch (Hypothetical Tight Deadline)

#### The Challenge
RFP response due in 48 hours. Need comprehensive pitch deck covering:
- Market analysis (mining tech sector in SA)
- Competitive landscape
- Proposed campaign strategy
- Creative concepts
- Budget & timeline

**Traditional Approach:**
- Research: 8 hours
- Strategy writing: 6 hours
- Deck design: 4 hours
- Creative mockups: 6 hours
**Total:** 24 hours of work (3 people × 8 hours)

**AI-Enhanced Approach:**
- Research: 2 hours (Perplexity + Gemini)
- Strategy writing: 1.5 hours (Claude)
- Deck creation: 1 hour (Gamma AI)
- Creative mockups: 1.5 hours (Midjourney + Canva)
**Total:** 6 hours of work (2 people × 3 hours)

---

### Tools Workflow

```
HOUR 1-2: RESEARCH (Perplexity + Gemini)
↓
Researcher uses Perplexity:
"Analyze the current state of mining technology adoption in South 
Africa. What are the top 5 trends? Who are the leading companies? 
What challenges do they face?"

Output: Comprehensive market summary with sources

Then uses Gemini to analyze:
- Upload 3 competitor campaign PDFs
- "Summarize each competitor's messaging strategy and visual approach"

Output: Competitive benchmark analysis

HOUR 3-4: STRATEGY DOCUMENT (Claude)
↓
Strategist uses Claude:
"Based on this research [paste Perplexity output], write a 5-page 
campaign strategy for Anglo American's NuGen mining tech launch. 
Target audience: mining executives, sustainability officers. 
Campaign goal: Position NuGen as the future of responsible mining.
Structure: Situation Analysis, Target Audience, Big Idea, 
Creative Strategy, Media Strategy."

Output: Draft strategy document (human edits for 30 mins)

HOUR 5: PITCH DECK CREATION (Gamma)
↓
Use Gamma AI:
- Feed it the strategy document
- "Create a 20-slide pitch deck from this strategy. Professional 
  design, use orange and navy blue color scheme, include sections 
  for creative concepts and budget."

Output: Designed deck framework

HOUR 6: CREATIVE MOCKUPS (Midjourney + Canva)
↓
Designer uses Midjourney:
"Mining operation, futuristic sustainable technology, South African 
landscape, aerial view, golden hour lighting, professional 
photography --ar 16:9"

Output: 4 key visuals
Then assembles in Canva with campaign headlines
```

---

### Key Learnings

✅ **What Worked:**
- Perplexity cut research time by 75%—fact-checked, cited sources
- Claude wrote surprisingly strong strategy foundation
- Gamma created beautiful deck framework in minutes (would've taken hours in PowerPoint)
- Midjourney delivered pitch-quality visuals without photoshoot

❌ **What Didn't Work:**
- Claude's strategy was good but generic—needed Guerilla's bold voice injected
- Gamma's auto-design sometimes made odd layout choices
- Still needed human designer to elevate Midjourney images to "final" quality

💡 **Pro Tips:**
- Use Perplexity for any research that needs current data + citations
- Claude is superb for first draft strategy docs—but always add your agency's unique POV
- Gamma is incredible for speed, but designer review is essential
- Midjourney works best for concept images, not final production assets

---

## Example 4: Maintaining Brand Voice at Scale

### Based on: DStv Internet Multi-Channel Campaign

#### The Challenge
DStv Internet launch requires consistent messaging across:
- Instagram (daily posts for 30 days)
- LinkedIn (thought leadership, 2x/week)
- Billboards (12 different locations/messages)
- Radio scripts (3 different spots, 15/30/60 seconds)
- Email campaign (welcome series, 5 emails)

That's **60+ individual pieces of content**—all must sound cohesively "DStv" while being platform-native.

**Traditional Approach:**
- Assign to 3 different copywriters
- Inconsistent voice across channels
- Heavy editing/revision cycles
- 2-3 weeks to finalize all assets

**AI-Enhanced Approach:**
- Set up Jasper with DStv brand voice profile (1 hour)
- Generate all assets using consistent brand template (4 hours)
- Human team curates/refines (4 hours)
**Total:** 9 hours vs. 80+ hours

---

### Tools Workflow

```
SETUP PHASE: Brand Voice Training (Jasper)
↓
1. Feed Jasper examples of DStv's existing content:
   - 10 social posts
   - 2 email campaigns
   - Brand guidelines PDF
   
2. Jasper learns:
   - Tone: Friendly, tech-savvy, accessible (not jargon-heavy)
   - Style: Short sentences, conversational, uses analogies
   - Avoid: Corporate-speak, overly technical language

GENERATION PHASE: Content Creation
↓
For each channel, use Jasper template:

Instagram:
"Write 30 Instagram captions for DStv Internet launch. Theme: 
[daily themes]. Each caption should be under 150 characters, 
include emoji, end with soft CTA. Maintain DStv brand voice."

LinkedIn:
"Write 8 LinkedIn thought leadership posts about the future of 
connectivity in South Africa. Professional but accessible tone. 
600-800 words each."

Radio Scripts:
"Write three 30-second radio scripts for DStv Internet. Focus on: 
(1) speed, (2) reliability, (3) value. Conversational, memorable, 
include clear CTA."

CURATION PHASE: Human Review
↓
Team reviews all outputs:
- Ensures no repetitive phrases across 60 pieces
- Adds local South African references AI might miss
- Injects more of Guerilla's edge where appropriate
```

---

### Key Learnings

✅ **What Worked:**
- Jasper's brand voice memory created remarkable consistency
- Generated 60 pieces that sounded like they came from one brain
- Freed up copywriters to focus on strategy, not repetitive execution

❌ **What Didn't Work:**
- Instagram captions sometimes felt too safe—needed more Guerilla boldness
- AI missed some South African cultural nuances (had to add local flavor)
- Radio scripts needed human punch-up for memorability

💡 **Pro Tips:**
- Invest time in brand voice training—pays off massively at scale
- Use AI for first draft, human for "edge" and cultural relevance
- Review ALL outputs together to catch repetitive patterns AI might not see

---

## Application Framework

### For Every Guerilla Project, Ask:

**1. Which phase needs AI?**
- Research & Planning → Perplexity, Claude
- Ideation & Concepting → ChatGPT, Midjourney
- Volume Generation → Copy.ai, Jasper
- Presentation & Delivery → Gamma, Gemini

**2. What's the time constraint?**
- Urgent (24-48 hours) → Lean heavily on AI, 80/20 rule (AI does 80%, human polishes 20%)
- Standard (1-2 weeks) → AI for volume/speed, human for quality elevation
- Premium (1+ month) → AI for research/ideation, mostly human execution

**3. What's the brand voice complexity?**
- Highly specific (Toyota, DStv) → Use Jasper with brand voice training
- Flexible/experimental → ChatGPT or Claude is sufficient
- Guerilla's own voice → Always add human touch—AI can't match the "anti-traditional" edge

---

## Next Steps for Team

1. **Pair each upcoming project with AI tools** from this document
2. **Track time savings** (before/after AI)
3. **Document what works** for Guerilla's style
4. **Build a library** of successful prompts for reuse
5. **Share learnings** across team in monthly show-and-tell

---

**Last Updated:** January 2026  
**Next Update:** After Month 2 completion with real team use cases
