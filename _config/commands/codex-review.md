# /codex-review

Run a Codex-based PR-style review on the current repo’s uncommitted diff, write it to `/tmp/codex-review.txt`, then summarize the findings in chat.

1) Generate the review file:
```sh
codex exec -m gpt-5.3-codex -s read-only "Review the following code changes for bugs, security issues, and maintainability. Be concise. CHANGES: $(git diff)" -o /tmp/codex-review.txt
```

2) Read `/tmp/codex-review.txt` and summarize:
- Key bugs / correctness risks
- Security issues (if any)
- Maintainability concerns
- Concrete next steps

If `git diff` is empty, say “No changes detected.” If `codex exec` fails and the file is empty, include the error output and suggest rerunning after fixing connectivity/auth.
