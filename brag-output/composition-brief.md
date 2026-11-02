# Hyperframes Composition Brief: Open Source Radar

## Objective
Create a short launch-style brag video for Open Source Radar.

## Output
- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 23 seconds

## Source Material
- Project root: `~/oss-contrib/open-source-radar`
- Primary files read: `site/index.html`, `site/assets/style.css`, `site/assets/app.js`, `README.md`, `issues/by-language/python.md`
- Product name: Open Source Radar
- Tagline / strongest claim: "Find an open source issue you can start today."
- Key UI or visual moment to recreate: the query line box (`is:issue is:open no:assignee -linked:pr`) growing as filters are applied, then real issue rows with the amber "Beginner label" pill
- Copy that must appear verbatim:
  - Find an open source issue you can start today.
  - is:issue is:open no:assignee -linked:pr
  - 3,571 open issues · 1,389 labeled for beginners · 1,208 active projects
  - 258 issues in 82 projects match.
  - Beginner label
  - Refreshed every 12 hours.
  - tanbirramim.github.io/open-source-radar

## Creative Direction
- Tone preset: polished
- Creative direction: a confident, warm product film on the site's light paper, with a real UI demo at its center
- Interpretation: fewer scenes, longer holds, fast-in-then-settle entrances, slow crossfades, restrained sound
- Angle: the honest problem first ("Most 'good first issue' lists are stale. Half are already taken."), then the product doing the thing: query line grows, issue rows arrive, rules badges visible, refreshed every 12 hours.
- Hook: two plain lines on paper with the radar rings drawing in behind
- Outro / punchline: "Refreshed every 12 hours." then lockup + URL + "Free and open source · MIT licensed"
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Unrelated visual redesign (no dark mode, no gradients, no neon)

## Visual Identity
- Background: #EAF0F5 (surface #F7FAFC)
- Text: #13263A (soft #4A5F74, rules #C9D5E0)
- Accent: #0E7C72 teal (#0A5F57 strong), #C2710C amber on #FBE9D1 wash
- Display font: Bricolage Grotesque (local woff2 in `assets/fonts/`)
- Body font: Atkinson Hyperlegible; code: JetBrains Mono (local woff2 in `assets/fonts/`)
- Visual references from the project: radar favicon (three rings, amber dot), the query box with 2px ink border and ink CTA button, the issue row layout, the amber Beginner pill, the rule badge chips, the post images in `~/Desktop/open-source-radar-media`

## Storyboard
Use the storyboard in `brag-output/brag-plan.md` as the creative contract.

Scene summary:
1. Hook — 4.2s — "Most 'good first issue' lists are stale." / "Half are already taken."
2. Reveal — 4.8s — headline + three stats count up, landing on 8.74s
3. Query line — 5.5s — cursor picks Python and Beginner labels; terms flash in amber; summary line
4. Issues arrive — 4.5s — three real rows on the beat grid, then "Project rules up front." callout on 17.47s
5. Outro — 4.0s — "Refreshed every 12 hours." then lockup, URL, MIT line; music fades

## Audio
- Audio role: warm bed with sparse professional accents
- Audio arc: quiet start, one warm payoff at the stats, small precise UI sounds during the demo, a soft confirmation on the rules, one bell on the lockup, fade to silence
- Music: `assets/music/happy-beats-business-moves-vol-12-by-ende-dot-app.mp3`
- Music treatment: volume 0.32 from 0s, fade to 0 over 21.4–23.0s
- Music cue guidance: preset at `assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json` (109.96 BPM). Strong cue locks: 8.74s (stats), 13.11s (beginner term), 17.47s (rules callout). Beat grid for rows: 14.73 / 15.84 / 16.93s.
- Audio-reactive treatment: subtle; per-frame data at `assets/music/audio-data.json` (30fps, 8 bands) drives the radar rings' opacity/scale (bass + RMS), never text
- Audio-coupled moments:
  - Hook line 2 — soft impact
  - Stats land — soft impact, beat-locked 8.74s
  - Select clicks — click_003
  - Query term flashes — drop_001
  - Issue rows — drop_002 on the beat grid
  - Rules callout — soft impact, beat-locked 17.47s
  - Lockup — impactBell_heavy_000
- SFX selection guidance: low HF-risk files from `sfx-analysis.md`; volume 0.5–0.7; nothing on crossfades
- SFX analysis guidance: `~/.claude/plugins/marketplaces/brag/skills/brag/assets/sfx/sfx-analysis.md`
- Exact SFX choice: Hyperframes chooses final timestamps and density after the animation exists.
- Audio files: copied into `brag-output/composition/assets/` (music, cues, sfx, fonts)

## Hyperframes Instructions
Load `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-cli`. /brag is its own workflow; do not enter the `hyperframes` intent interview.

Requirements:
- Show at least one real UI, copy, or visual element from the source project.
- Keep all text readable in the final render.
- Keep the video within 15-25 seconds.
- Include the planned music/SFX layer.
- Treat cue metadata as optional timing hints; readability first.
- Use local assets for audio and fonts; GSAP from the scaffold's CDN tag.
- Run `hyperframes check` before render.
