# Brag Plan: Open Source Radar

## What is this app?
Open Source Radar is a website and GitHub repo that lists open, unclaimed, beginner-friendly issues from active open source projects, sorted by language and topic, refreshed every 12 hours, with project rules (AI policy, CLA, DCO) shown before you start and a full first-contribution guide.

## The angle
The honest problem first, then the product doing the thing. Every "good first issue" list goes stale and half the issues are already taken; Open Source Radar's whole pitch is that every issue on it is *actually free*. The video shows the site's signature element, the live GitHub query line, growing as filters are applied, and then real issue rows arriving one by one. Nothing abstract: the query, the filters, the rows, the badges and the numbers are all the site's own copy.

## Hook (first 2-4 seconds)
Two lines on paper, set in the site's display face, delivered plainly:
"Most 'good first issue' lists are stale." then "Half are already taken."
Behind them the radar mark's rings draw in, echoing the favicon and the post images.

## Key moments (the middle)
- The wordmark and hero headline land: "Find an open source issue you can start today." with the three README stats counting up to 3,571 / 1,389 / 1,208.
- The query line grows: `is:issue is:open no:assignee -linked:pr` is on screen, a cursor picks Language → Python and `language:Python` flashes in amber (the site's own q-new flash), then Level → Beginner labels adds `label:"good first issue"`. Summary line reads "258 issues in 82 projects match."
- Three real issue rows slide in one by one with their Beginner label pills, repo names in teal, star counts, and rule badges ("Disclose AI use", "DCO sign-off"). Callout: "Project rules up front."

## Outro / punchline
"Refreshed every 12 hours." then the mark, the wordmark, the URL tanbirramim.github.io/open-source-radar, and "Free and open source · MIT". Music fades under the final frame.

## User flow worth showing
entry → key action → result:
1. Land on the hero and the base query line.
2. Pick a language and a level; the query line and summary update.
3. Read the filtered issue rows with badges and pick one.

## Tone
- Preset: polished
- Creative direction: a confident, warm product film on the site's light paper, with a real UI demo at its center; nothing corporate, nothing loud
- Interpretation: fewer scenes with longer holds, entrances that are fast then settle, slow crossfades, restrained sound; the humor is only in the honest hook

## Format: landscape — 1920x1080
## Duration: 23 seconds

## Visual identity (from the project)
- Background: #EAF0F5 (paper), cards/surface #F7FAFC
- Accent: #0E7C72 teal (strong #0A5F57), #C2710C amber with #FBE9D1 wash for the Beginner pill and query flash
- Text: #13263A ink, #4A5F74 soft ink, #C9D5E0 rules
- Display font: Bricolage Grotesque (800 headlines, 700 titles)
- Body font: Atkinson Hyperlegible; code: JetBrains Mono
- Strongest visual element: the query line box (2px ink border, surface fill, mono text with teal keys and amber-flash for new terms) plus the issue rows with the amber "Beginner label" pill; radar rings as the only decorative

## Share copy (draft)
Introducing Open Source Radar: find an open source issue you can start today. Every listed issue is open, unassigned, has no linked pull request and comes from a project active in the last two months, refreshed every 12 hours, with AI policy, CLA and DCO rules shown before you start.

## Audio direction
- Role: warm bed with sparse professional accents
- Music: `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3` (steady and clean, 110 BPM)
- Music treatment: starts at 0 at volume 0.32, holds, fades to 0 over the final 1.6 s under the outro
- Music cue guidance: preset read from `assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json`, tempo 109.96 BPM. Strong cue targets: 8.74 s (stats land), 13.11 s (beginner term flashes in), 17.47 s (rules callout), 19.66 s (outro wordmark). Beat-grid window for the three issue rows: 14.73 / 15.84 / 16.93 s (every other beat, ~1.1 s apart, so each row holds long enough to read).
- Audio-reactive treatment: subtle; music RMS/bass breathes the radar rings' opacity and scale on the hook and outro only, never the text
- SFX posture: sparse, motion-matched, low high-frequency-risk files
- Audio-coupled moments: hook line 2 (soft impact), filter clicks (click), query term flash (drop), issue rows (drop per row), rules callout (soft impact), outro wordmark (bell)
- Restraint rule: no sound on text fades or crossfades; SFX volume never above 0.7; nothing on every beat

## Storyboard

### Scene 1 — Hook — 4.2s (0.0–4.2)
Paper background. The radar mark's three rings draw in at large scale, faint, off-centre right (like the post images). Line 1 "Most 'good first issue' lists are stale." rises in at 0.3 s and holds. Line 2 "Half are already taken." rises in at 2.3 s and holds to the end of the scene.
Sequential/interaction: two lines, one after the other
Audio intent: quiet start, one dry accent on the second line
Audio-coupled idea: `impactSoft_medium_001` on line 2's landing; rings breathe with bass
Music: bed starts at 0
Transition mood: soft crossfade → Scene 2

### Scene 2 — Reveal — 4.8s (4.2–9.0)
Brand lockup (mark + "Open Source Radar") at top left. Hero headline "Find an open source issue you can start today." lands large at 4.6 s (fast rise, settles). At 6.6 s three stats count up beneath it, landing together on the 8.74 s cue: 3,571 open issues · 1,389 labeled for beginners · 1,208 active projects. Small line under: "updated 2026-09-13 20:28 UTC".
Sequential/interaction: three stat tiles count up together
Audio intent: the first warm payoff
Audio-coupled idea: `impactSoft_medium_004` when the stats land (beat-locked 8.74 s)
Transition mood: clean slide up → Scene 3

### Scene 3 — The query line — 5.5s (9.0–14.5)
The site's query box appears full width: `is:issue is:open no:assignee -linked:pr` in mono with teal keys, the ink "Run this search on GitHub" button on the right. Below it the filter row (Search, Language, Topic, Level, Project rules, Sort). A cursor moves to Language, clicks, and the select shows "Python"; the term `language:Python` appends to the query with the amber flash at 10.9 s. Summary appears: "258 issues in 82 projects match." The cursor moves to Level, clicks "Beginner labels", and `label:"good first issue"` appends with the amber flash on the 13.11 s cue.
Sequential/interaction: yes, simulated cursor clicks on two selects, two query terms appended one by one
Audio intent: the product doing its thing, precise and small
Audio-coupled idea: `click_003` on each select click, `drop_001` on each term flash
Transition mood: clean → Scene 4

### Scene 4 — Issues arrive — 4.5s (14.5–19.0)
The filtered list. Three real rows slide in one by one on the beat grid (14.73, 15.84, 16.93 s), each with title and number, teal repo name, star count, the amber "Beginner label" pill and rule badges:
1. RU translation mistake #98565 · getsentry/sentry · 44.8k stars · Beginner label · 4 comments
2. Autonomous Agents, Unite! #2386 · microsoft/markitdown · 183.5k stars · Beginner label · 4 comments
3. [core] Adopt 'absl::InlinedVector' for small, frequently-allocated collections #59884 · ray-project/ray · 43.8k stars · Beginner label · DCO sign-off
At 17.47 s (cue) a callout settles at the right: "Project rules up front." with the badge chips "AI policy", "CLA", "DCO sign-off". Hold to 19.0.
Sequential/interaction: yes, three rows one by one, then one callout
Audio intent: rhythm, then a soft confirmation
Audio-coupled idea: `drop_002` per row on the beat grid, `impactSoft_medium_001` on the callout (beat-locked 17.47 s)
Transition mood: soft crossfade → Scene 5

### Scene 5 — Outro — 4.0s (19.0–23.0)
"Refreshed every 12 hours." holds centred for 1.4 s, then dissolves as the mark and wordmark "Open Source Radar" land on the 19.66 s cue... adjusted: the line shows 19.0–20.4, the lockup lands at 20.4 with the URL tanbirramim.github.io/open-source-radar beneath and "Free and open source · MIT licensed". Rings breathe faintly behind. Music fades from 21.4 to 23.0.
Sequential/interaction: line, then lockup and URL
Audio intent: a single warm landing, then quiet
Audio-coupled idea: `impactBell_heavy_000` on the lockup landing (natural timing 20.4 s, between beats 20.19 and 20.75 for readability of the preceding line)
Transition mood: hold to black-free end (last frame is the lockup on paper)

**Music mood for this video:** upbeat but steady, low in the mix
**Audio summary:** a quiet bed under an honest hook, one warm hit when the stats land, small clicks and drops while the product filters, a soft confirmation on the rules, one bell on the lockup, then a fade.
