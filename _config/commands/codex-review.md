The user wants to review the current repo's uncommitted diff using OpenAI Codex.

**Model selection:**
- If the user provided a model name as argument: "$ARGUMENTS", use that model.
- If no argument was provided (empty), default to `gpt-5.3-codex`.

Available models for reference:
- gpt-5.3-codex (latest, highest quality)
- gpt-5.2-codex (previous gen)
- gpt-5.1-codex-mini (lightweight, saves credits)

**Steps:**

1) First check `git diff` has content. If empty, say "No changes detected." and stop.

2) Run this command, replacing MODEL with the selected model:
```sh
codex exec -m MODEL -s read-only "Review the following code changes for bugs, security issues, and maintainability. Be concise and actionable. CHANGES: $(git diff)" -o /tmp/codex-review.txt
```

3) Read `/tmp/codex-review.txt` and summarize:
- Which model was used
- Key bugs / correctness risks
- Security issues (if any)
- Maintainability concerns
- Concrete next steps

If `codex exec` fails and the file is empty, include the error output and suggest rerunning.
