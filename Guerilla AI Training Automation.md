Guerilla AI Training Automation
1) Product name

Guerilla AI Boot-Up — Facilitator Pack Generator

2) One-line purpose

Every two weeks, automatically generate and email a facilitator-ready session pack (course outline + content + practical project/homework) for Guerilla Africa’s internal AI training programme—current, sharp, and on brand.

3) Target users

Primary: Facilitator (receives the session pack email)

Secondary: Ops/Programme admin (manages schedule, topics, recipients, settings)

4) Outcomes and success criteria
Must achieve

Email arrives every two weeks with:

“AI News You Can Use” (recent, relevant updates)

Session overview, objectives, timed agenda

Core content: talking points + examples

Homework/project: clear deliverables + evaluation criteria

Content matches Guerilla’s tone: confident, edgy, no fluff, but still clear and responsible.

Content is not stale: explicit “version/trend check” baked in.

System is repeatable and coherent across 24 sessions (curriculum spine).

Nice to have

Archive each session pack (JSON + rendered HTML) for audit/reuse.

Admin dashboard to preview/edit before sending.

Optional later workflow for homework submissions & feedback.

5) Curriculum structure: “spine” vs dynamic
Decision

Use a fixed 24-session curriculum spine (titles + intent/outcomes) stored in the system and referenced by session number.

Why: prevents drift. Ensures pacing and progression.
What changes over time: examples, tools referenced, news section, and homework variations.

Spine data requirements (per session)

session_number (1–24)

title

intent (1–2 sentences)

theme_tag (Foundations / Image / Video / Copy / Strategy / Ops)

core_skill (briefing, taste, iteration, etc.)

optional tool_focus (e.g., LLM, image gen, video gen, automation)

6) Content voice and brand guidelines
Guerilla Africa “flavour”

Punchy, confident, direct.

No corporate training tone.

No buzzword soup.

“Taste > tools”, “speed with standards”, “ship smart”.

Guardrails

No profanity required. If used, keep it minimal and not insulting.

Avoid unverified claims and rumours.

If a detail can’t be verified (e.g., exact version), speak capability-level and add a “verify in tool UI/release notes” note.

7) Core workflow overview
Trigger

Scheduled: every 14 days (bi-weekly)

Timezone: Africa/Johannesburg

Steps

Determine next session number (based on start date + count, or stored pointer).

Load curriculum spine row for that session.

Research step (freshness): gather 2–4 updates for AI News You Can Use and confirm major tool changes.

Generate session pack in strict JSON (contract output).

Render JSON into branded HTML email (styled, readable).

Send email to facilitator + optional CC list.

Archive JSON + HTML + send metadata in storage.

8) Required integrations

At minimum, implement placeholders if connectors aren’t available.

Email delivery

SMTP / Gmail / Outlook (choose based on what Anti-gravity supports)

Must support HTML email

Storage (for archives)

One of:

Database (built-in), Airtable, Google Sheets, Notion DB, or file storage (Drive/S3)

Store:

session JSON

rendered HTML

timestamps

session number + title

“sources used” list for news section (if available)

Optional (later)

Slack/Teams post: “Session pack sent” + highlights.

9) Research requirements for “AI News You Can Use”

This is the freshness engine. It must be conservative and source-based.

Constraints

Provide 2–4 items max.

Prefer:

official release notes/docs

reputable tech publications

Each item must include:

title

what_changed

why_it_matters

practical_implication

source_name

source_date

optional source_url

If research is unavailable

Output a clear fallback:

“No verified updates found in the last X days from reliable sources”

Provide capability-level notes and “verify in tool UI”

10) Output contracts (data + email)
A) Session pack JSON (LLM must output ONLY valid JSON)

Use this schema:

{
  "session_metadata": {
    "programme_name": "Guerilla AI Boot-Up",
    "session_number": 1,
    "month_label": "Month 1",
    "session_title": "",
    "session_theme_tag": "",
    "session_duration_minutes": "30–45",
    "timezone": "Africa/Johannesburg",
    "generated_date": "YYYY-MM-DD"
  },
  "ai_news_you_can_use": {
    "time_allocation_minutes": 5,
    "updates": [
      {
        "title": "",
        "what_changed": "",
        "why_it_matters": "",
        "practical_implication": "",
        "source_name": "",
        "source_date": "YYYY-MM-DD",
        "source_url": ""
      }
    ],
    "notes_for_facilitator": ""
  },
  "session_overview": {
    "summary": "",
    "why_this_matters_for_guerilla": ""
  },
  "learning_objectives": [
    ""
  ],
  "session_agenda": {
    "total_duration_minutes": "30–45",
    "agenda_items": [
      { "segment": "AI News You Can Use", "duration_minutes": 5, "description": "" },
      { "segment": "Intro", "duration_minutes": 5, "description": "" },
      { "segment": "Core Teaching", "duration_minutes": "15–20", "description": "" },
      { "segment": "Discussion / Demo", "duration_minutes": "10–15", "description": "" },
      { "segment": "Wrap + Assignment", "duration_minutes": 5, "description": "" }
    ]
  },
  "core_content": {
    "key_concepts": [
      { "concept": "", "explanation": "", "marketing_example": "" }
    ],
    "facilitator_talking_points": [
      ""
    ],
    "common_misconceptions": [
      ""
    ]
  },
  "live_demonstration_ideas": [
    { "idea": "", "purpose": "", "notes": "" }
  ],
  "homework_assignment": {
    "task_title": "",
    "context": "",
    "task_description": "",
    "expected_output": [
      ""
    ],
    "evaluation_criteria": [
      ""
    ],
    "time_estimate_minutes": 30
  },
  "facilitator_notes": {
    "prep_tips": [
      ""
    ],
    "optional_extensions": [
      ""
    ],
    "risk_and_responsibility_notes": [
      ""
    ]
  }
}

B) HTML email rendering

Render the JSON into a clean HTML template:

header (session number + title)

AI News cards

agenda table

key concepts + talking points

homework block (deliverables + rubric)

Use inline CSS for email compatibility.

Subject line format:

Guerilla AI Boot-Up — Session {N}: {Title}

11) Prompting strategy (2-stage generation)

To keep quality high and reduce hallucinations, implement two LLM calls:

Stage 1: Research summarizer (if web/browsing is available)

Input: high-level query + tool list + recency window (60–120 days)
Output: a small JSON list of verified updates with sources.

Stage 2: Session pack generator

Input:

curriculum spine row (title/intent/theme)

research JSON results (Stage 1)

constraints (session length, tone)
Output:

session pack JSON exactly matching the contract (no extra keys)

Critical LLM rule

If sources are missing or unclear: do not invent. Provide safe fallback text and “verify” notes.

12) Admin UI requirements (Anti-gravity app)
Pages

Dashboard

next send date

next session number/title

last run status

Curriculum spine editor

CRUD sessions 1–24

Settings

facilitator email(s)

CC list

schedule cadence (14 days)

timezone

“news recency window” (default 90 days)

tone toggle: “Guerilla sharp” (default ON)

Session preview

view generated JSON

view rendered HTML

“approve and send” (optional manual gate)

Archive

list of past session packs

download JSON/HTML

Permission model

Admin: edit + send

Facilitator: view only (optional)

13) Scheduling logic

Two options:

Option A (recommended): fixed bi-weekly schedule from a start date

Inputs: programme_start_date

Compute: session_number = floor((today - start_date)/14 days) + 1

Cap at 24 or roll into “season 2”

Option B: stateful pointer

Store current_session_number

On successful send, increment by 1

Prefer Option B if holidays/manual pauses are likely.

14) Quality checks before send

Implement a validator that rejects sending if:

JSON is invalid

missing required keys

“AI News” has items with empty source_name + source_date (unless explicitly using fallback mode)

Agenda total exceeds 45 minutes

Homework missing evaluation criteria

15) Security and safety notes (client trust)

Include standard facilitator notes each session:

avoid uploading confidential client data into public tools unless approved

be mindful of rights/copyright

disclosure guidance (internal policy placeholder)

don’t ship AI-generated assets without human QA

16) Deliverables Anti-gravity should generate

A working app with admin UI (pages above)

A bi-weekly scheduler workflow

Two-stage LLM pipeline (research + session pack)

HTML email template renderer

Email sender integration

Archive storage + browsing

A seeded 24-session curriculum spine (use the edgy Guerilla-aligned titles already defined in this conversation)

17) Seed curriculum spine (minimum requirement)

Anti-gravity should pre-load session 1–24 titles using the Guerilla-aligned “edgy” roadmap we defined earlier (e.g., “AI Is Not the Idea — It’s the Amplifier”, “The New Creative Stack…”, “Prompting Is Just Briefing…”, etc.). Each should include a one-line intent.

18) First run expectation

On build completion, generate:

Session 1 JSON pack

Session 1 HTML email preview

Archive entry created

Ready to schedule/send