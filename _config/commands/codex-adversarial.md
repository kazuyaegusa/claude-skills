OpenAI Codex を使ってカレントリポジトリのコードを **敵対的（adversarial）視点** で厳格レビューする。通常レビューより意図的に批判的・攻撃的な目線でバグ・脆弱性・設計欠陥を洗い出す。

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
codex exec -m MODEL -s read-only "You are an adversarial security reviewer. Your job is to FIND FLAWS. Assume this code has bugs — your goal is to prove it. Mercilessly critique ALL code in this repository for:

1. Security vulnerabilities (OWASP Top 10, injection, auth bypass, hardcoded secrets, SSRF, path traversal, insecure deserialization)
2. Logic bugs and edge cases that WILL cause failures in production (race conditions, off-by-one, null handling, integer overflow)
3. Design flaws, anti-patterns, and architectural weaknesses that make the system fragile
4. Data handling issues (PII leaks, missing encryption, insecure storage, logging sensitive data)
5. Dependency risks (known CVEs, outdated packages, supply chain concerns)

DO NOT be polite. DO NOT say 'overall the code looks good'. List every issue you find.
Prioritize: Critical > High > Medium. Skip Low unless it compounds with other issues.
For each issue: file path, line number (if possible), what's wrong, how to exploit/trigger it, and the fix.
Output in Japanese." -o /tmp/codex-adversarial.txt
```

2) Read `/tmp/codex-adversarial.txt` and summarize in Japanese:
- Which model was used
- Critical issues (immediate action required)
- High severity issues (should fix before release)
- Medium severity issues (fix in next sprint)
- Attack scenarios: how a malicious actor could chain these issues
- Prioritized remediation plan

If `codex exec` fails and the file is empty, include the error output and suggest rerunning.
