OpenAI Codex を使ってカレントリポジトリのコード・ドキュメント全体をレビューし、改善点を洗い出す。

**Model selection:**
- If the user provided a model name as argument: "$ARGUMENTS", use that model.
- If no argument was provided (empty), default to `gpt-5.3-codex`.

Available models for reference:
- gpt-5.3-codex (latest, highest quality)
- gpt-5.2-codex (previous gen)
- gpt-5.1-codex-mini (lightweight, saves credits)

**Steps:**

1) Run the following command, replacing MODEL with the selected model:
```sh
codex exec -m MODEL -s read-only "You are a senior code reviewer. Thoroughly review ALL code and documentation files in this repository. For each file, check for:
1. Bugs and correctness risks (logic errors, edge cases, race conditions)
2. Security issues (hardcoded secrets, injection risks, missing input validation, OWASP top 10)
3. Maintainability concerns (code duplication, unclear naming, missing error handling, dead code)
4. Documentation quality (factual accuracy, outdated information, missing context, inconsistencies between docs)
5. Improvement opportunities (better patterns, performance, readability)

Be concise and actionable. Prioritize issues by severity (Critical > High > Medium > Low).
Output in Japanese." -o /tmp/codex-review.txt
```

2) Read `/tmp/codex-review.txt` and summarize in Japanese:
- Which model was used
- Critical / High severity issues (bugs, security)
- Medium severity issues (maintainability, documentation quality)
- Low severity / improvement suggestions
- Concrete next steps (prioritized action items)

If `codex exec` fails and the file is empty, include the error output and suggest rerunning.
