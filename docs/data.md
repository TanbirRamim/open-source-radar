# Using the data

Everything behind the website is published as one JSON file that anyone can use in their own tools, bots, newsletters or dashboards:

```text
https://tanbirramim.github.io/open-source-radar/data/issues.json
```

It is refreshed twice a day. The same data, without the website extras, is committed at [`data/issues.json`](../data/issues.json). Please cache it rather than downloading it on every request, and link back to this project when you publish something built on it.

## Shape

```jsonc
{
  "generated_at": "2026-09-13T01:43:41+00:00",   // when the data was collected (UTC)
  "topic_titles": { "web": "Web development" },  // website file only: topic slug to title
  "repositories": {
    "owner/repo": {
      "url": "https://github.com/owner/repo",
      "description": "What the project is",
      "stars": 12345,
      "forks": 678,
      "language": "Rust",                        // primary language
      "license": "MIT",                          // SPDX id, or null
      "pushed": "2026-09-12",                    // last push date
      "topics": ["cli", "terminal"],             // GitHub topics
      "buckets": ["devtools"],                   // Open Source Radar topic slugs (see scripts/config.toml)
      "open_count": 4,                           // listed issues in this project
      "policy": {
        "ai": "none",                            // none | policy | disclose | restricted (detected, may be wrong)
        "ai_file": null,                         // file the AI rule was found in
        "cla": false,                            // CLA mentioned in contribution files
        "dco": false                             // DCO / Signed-off-by mentioned
      }
    }
  },
  "issues": [
    {
      "repo": "owner/repo",
      "number": 42,
      "title": "Crash when the config file is empty",
      "url": "https://github.com/owner/repo/issues/42",
      "labels": ["bug", "good first issue"],
      "level": "beginner",                       // beginner | help-wanted
      "created": "2026-08-01",
      "updated": "2026-09-10",
      "comments": 2,
      "closed_pr": false                         // a pull request for it was closed without merging
    }
  ]
}
```

## Example: five newest beginner issues in Go

```bash
curl -s https://tanbirramim.github.io/open-source-radar/data/issues.json \
  | jq -r '.repositories as $r | [.issues[] | select(.level == "beginner" and $r[.repo].language == "Go")]
           | sort_by(.created) | reverse | .[:5][] | "\(.title)\n  \(.url)"'
```
