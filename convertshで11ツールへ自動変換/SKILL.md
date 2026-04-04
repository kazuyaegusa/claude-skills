# convert.shで11ツールへ自動変換

> 単一のSKILL.md形式から、Cursor（.mdc）、Aider（CONVENTIONS.md）、Windsurf（.windsurf/skills/）など11種のAIツール固有フォーマットへ一括変換する

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

各AIツールは独自のプロンプト形式・配置場所を持つ。手動で11種類書き直すと保守コストが爆発するため、変換スクリプトで標準形式→ツール固有形式の自動生成が必須

## いつ使うのか

複数のAIコーディングツールを併用している、またはツール移行を検討しているとき。スキルを一度書いて複数プラットフォームで使い回したい場合

## やり方

1. git clone https://github.com/alirezarezvani/claude-skills.git
2. cd claude-skills
3. ./scripts/convert.sh --tool all （全ツール分を生成、約15秒）
4. ./scripts/install.sh --tool cursor --target /path/to/project （特定ツールへインストール）
5. 確認: find .cursor/rules -name '*.mdc' | wc -l （248個のスキルがCursor形式で配置されているか）

### 入力

- claude-skillsリポジトリ（248 SKILL.mdファイル）
- 対象ツール名（cursor/aider/windsurf/kilocode/opencode/augment/antigravity）

### 出力

- ツール固有ディレクトリ（例: .cursor/rules/, .aider/CONVENTIONS.md）
- 各ツール用README（install/verify/update手順付き）

## 使うツール・ライブラリ

- Bash
- sed/awk（変換スクリプト内部で使用）
- Git（リポジトリ取得）

## コード例

```
#!/bin/bash
# scripts/convert.sh の簡略版イメージ
for skill in skills/*/SKILL.md; do
  skill_name=$(basename $(dirname $skill))
  
  # Cursor形式変換
  sed 's/^## /# /g' $skill > .cursor/rules/${skill_name}.mdc
  
  # Aider形式変換
  cat $skill >> .aider/CONVENTIONS.md
  
  # Windsurf形式変換
  cp $skill .windsurf/skills/${skill_name}.md
done
```

## 前提知識

- Claude Code / Cursor / Aider 等いずれかのAIコーディングツールの基本的な使い方
- Git / GitHub の基本操作（clone, pull）
- Python 3.x の実行環境（スクリプトツール利用時）
- Bashシェルの基本知識（インストールスクリプト実行時）
- （任意）マーケティング・PM・コンプライアンス等の各ドメイン知識（該当スキル使用時）

## 根拠

> Works with: Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity

> One repo, eleven platforms. Works natively as Claude Code plugins, Codex agent skills, Gemini CLI skills, and converts to 8 more tools via scripts/convert.sh. All 332 Python tools run anywhere Python runs.

> Python tools — 332 CLI scripts (all stdlib-only, zero pip installs)

> Convert all 156 skills to 7 AI coding tools with a single script: ./scripts/convert.sh --tool all

> skill-security-auditor — Security gate — scan skills for malicious code before installation. Scans for: command injection, code execution, data exfiltration, prompt injection, dependency supply chain risks, privilege escalation. Returns PASS / WARN / FAIL with remediation guidance. Zero dependencies.
