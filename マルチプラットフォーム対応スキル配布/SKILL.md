# マルチプラットフォーム対応スキル配布

> Agent Skills仕様（agentskills.io）に準拠したSKILL.mdと、各IDE固有のフォーマット（hooks.json、.gemini/skills/等）を同一リポジトリで提供し、npx skills add コマンドで一括インストール可能にする。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code、Cursor、Gemini CLI、Kiro、OpenClaw等、16以上のIDEでAIエージェントが使われているが、それぞれ独自のスキルフォーマットを持つ。統一インストール手段を提供することで、ユーザーは環境を問わず同じワークフローを導入できる。

## いつ使うのか

複数IDE環境で使われるスキルを配布したい場合、Agent Skills仕様に準拠したツールを開発したい場合。

## やり方

1. Agent Skills仕様に従い SKILL.md を作成（description、instructions、examples、hooks定義）
2. プラットフォーム固有の配置（.cursor/、.gemini/、.kiro/、.github/、.mastracode/等）を追加
3. hooks.json でPreToolUse、PostToolUse、Stopの各hookスクリプトを定義
4. bash版とPowerShell版のスクリプトを用意し、OS判定で切り替え
5. npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g でグローバルインストール可能に
6. 各IDE向けにREADMEとセットアップドキュメント（docs/gemini.md、docs/cursor.md等）を提供

### 入力

- Agent Skills仕様
- 各IDE固有のスキルフォーマット仕様

### 出力

- SKILL.md（Agent Skills準拠）
- hooks.json（Cursor、GitHub Copilot、Mastra Code等）
- .gemini/skills/、.kiro/、.openclaw/等の配置
- bash/PowerShell版hookスクリプト

## 使うツール・ライブラリ

- npx skills CLI
- Agent Skills仕様（agentskills.io）

## 前提知識

- Claude CodeまたはAgent Skills対応IDE（Cursor、Gemini CLI、Kiro、OpenClaw等）の基本操作
- markdownファイルの読み書き
- hookの概念（PreToolUse、PostToolUse、Stop）の理解
- bash または PowerShell の基本知識（hookスクリプトカスタマイズ時）
- gitの基本操作（セッションリカバリー機能利用時）

## 根拠

> 16 Supported IDEs: Claude Code, Gemini CLI, OpenClaw, Kiro, Cursor, Continue, Kilocode, OpenCode, Codex, FactoryAI Droid, Antigravity, CodeBuddy, AdaL CLI, Pi Agent, GitHub Copilot, Mastra Code

> npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g — Works with Claude Code, Cursor, Codex, Gemini CLI, and 40+ agents supporting the Agent Skills spec.
