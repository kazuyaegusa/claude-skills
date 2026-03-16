# マルチツール変換スクリプトによる11ツール対応

> ./scripts/convert.sh を実行して、全スキルを Cursor (.mdc), Aider (CONVENTIONS.md), Windsurf, Kilo Code 等の各ツール固有形式に一括変換する

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

ツールごとにスキルを書き直す手間を削減し、知識資産の再利用性を最大化する。ユーザーはツール移行時にスキルを作り直す必要がない

## いつ使うのか

複数のAIコーディングツールを併用している場合、または将来的にツールを変更する可能性がある場合

## やり方

1. リポジトリをクローン
2. ./scripts/convert.sh --tool all を実行（約15秒）
3. integrations/ 配下に各ツール用ディレクトリが生成される
4. ./scripts/install.sh --tool <toolname> --target <path> で対象プロジェクトにインストール
5. 各ツールの README で動作確認方法を確認

### 入力

- SKILL.md 形式で定義された156個のスキル
- 対象ツール名（cursor, aider, windsurf, kilocode, opencode, augment, antigravity）

### 出力

- 各ツール固有形式に変換されたスキルファイル群
- ツール別の README
- インストール検証用スクリプト

## 使うツール・ライブラリ

- Bash
- 各ツールのCLI（インストール時）

## コード例

```
# 全ツール向けに変換
./scripts/convert.sh --tool all

# Cursor プロジェクトにインストール
./scripts/install.sh --tool cursor --target /path/to/project

# 検証
find .cursor/rules -name "*.mdc" | wc -l  # 156と表示されるべき
```

## 前提知識

- Claude CodeまたはOpenAI Codex等のAIコーディングツールの基本的な使い方
- SKILL.md形式やエージェント概念の理解（ただしREADMEに説明あり）
- Bash/シェルスクリプトの基本知識（インストールスクリプト実行用）
- Python 3.x の実行環境（CLIツール使用時）
- Git/GitHub の基本操作

## 根拠

> 「192 production-ready Claude Code skills, plugins, and agent skills for 11 AI coding tools」

> 「Works with: Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity」

> 「5,200+ GitHub stars — the most comprehensive open-source Claude Code skills & agent plugins library」

> 「254 CLI scripts (all stdlib-only, zero pip installs)」

> 「Scans for: command injection, code execution, data exfiltration, prompt injection, dependency supply chain risks, privilege escalation」
