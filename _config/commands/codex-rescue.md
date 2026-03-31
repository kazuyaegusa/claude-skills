現在のタスクや問題を OpenAI Codex に丸ごと委任して解決させる。Claudeが詰まった問題や、別モデルの視点が欲しいときに使う。

**Model selection:**
- If the user provided a model name as argument (e.g. "gpt-5.1-codex-mini fix the auth bug"), extract the model name and use it. The remaining text is the task description.
- If no model is specified, default to `gpt-5.3-codex`.

Available models for reference:
- gpt-5.3-codex (latest, highest quality)
- gpt-5.2-codex (previous gen)
- gpt-5.1-codex-mini (lightweight, saves credits)

**Steps:**

1) Ask the user: "CodeXに委任するタスクを1-2文で説明してください。（例: 'このテストが通らない原因を調査して修正して', 'パフォーマンスボトルネックを特定して改善案を出して'）"

2) Run the following command, replacing MODEL and TASK with the appropriate values:
```sh
codex exec -m MODEL -s full-auto "TASK

このリポジトリのコードを調査し、上記のタスクを完全に実行してください。
- まずリポジトリ構造を把握し、関連ファイルを特定する
- 必要なコード変更を実施する
- 変更内容と理由を日本語で報告する" -o /tmp/codex-rescue.txt
```

3) Read `/tmp/codex-rescue.txt` and report in Japanese:
- What CodeX investigated
- What changes it made (if any)
- Whether the task was successfully completed
- Any remaining issues or follow-up needed

**WARNING:** This command uses `-s full-auto` which allows CodeX to modify files. Review changes with `git diff` after execution.

If `codex exec` fails and the file is empty, include the error output and suggest rerunning.
