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

A snapshot of this data is also published as a dataset on Hugging Face: [TanbirRamim/open-source-radar](https://huggingface.co/datasets/TanbirRamim/open-source-radar), with an `issues` table and a `repositories` table.


## Feeds

Open Source Radar automatically generates RSS feeds for beginner-friendly issues[cite: 1]. You can access them through the following links:

* **Feed Index**: [https://tanbirramim.github.io/open-source-radar/feeds/](https://tanbirramim.github.io/open-source-radar/feeds/) (Lists all active feeds)
* **Language Feeds**: [https://tanbirramim.github.io/open-source-radar/feeds/python.xml](https://tanbirramim.github.io/open-source-radar/feeds/python.xml) (replace `python` with any language slug, e.g., `javascript`, `typescript`, `rust`)
* **Topic Feeds**: [https://tanbirramim.github.io/open-source-radar/feeds/topics/ai.xml](https://tanbirramim.github.io/open-source-radar/feeds/topics/ai.xml) (replace `ai` with any topic slug, e.g., `web`, `cli`, `db`)

---

### Python Integration Example

This script uses Python standard libraries to download the central JSON database(issues.json), scan repository pathways for Python ecosystem keywords, and print out the top 5 active open-source tasks. You can easily modify this script to filter for different target keywords or repository tracks based on your requirements.

```python
import urllib.request
import json


DATA_URL = "http://localhost:8000/data/issues.json"

try:
    req = urllib.request.Request(
        DATA_URL, 
        headers={"User-Agent": "open-source-radar-data-client"}
    )
    
    with urllib.request.urlopen(req, timeout=30) as response:
        if response.status == 200:
            raw_payload = response.read().decode("utf-8")
            data = json.loads(raw_payload)
            
            # Grabbing the list from the "issues" key visible in the database schema
            issues_list = data.get("issues", [])
            
            print("Successfully processed database file.")
            print(f"Total system tracker pool: {len(issues_list)} issues found.\n")
            
            # Filtering for Python language tasks using common repository keywords
            target_issues = []
            python_repos = ["python", "django", "flask", "pandas", "numpy", "ansible"]
            
            for item in issues_list:
                repo_name = item.get("repo", "").lower()
                # If the repository matches our Python ecosystem keywords
                if any(keyword in repo_name for keyword in python_repos):
                    target_issues.append(item)
            
            print(f"--- Top 5 Open Python Tasks ({len(target_issues)} total available) ---")
            for item in target_issues[:5]:
                title = item.get("title", "No Title")
                repo = item.get("repo", "Unknown Repo")
                url = item.get("url", "#")
                print(f"🔹 {title}")
                print(f"   Repository: {repo}")
                print(f"   Link: {url}\n")
        else:
            print(f"Server rejected request with status code: {response.status}")
            
except Exception as e:
    print(f"Error accessing data stream pipeline: {e}")

...
```

---