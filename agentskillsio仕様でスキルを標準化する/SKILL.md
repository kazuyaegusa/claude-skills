# agentskills.io仕様でスキルを標準化する

> agentskills.io（またはagentskill.sh）のスキル仕様に従って、Claude Code以外のAIツール（Cursor, Copilot, Windsurf, Zed等）でも利用可能なスキルを作成する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code専用のスキルは他のAI開発ツールで再利用できない。標準仕様に準拠することで、69,000以上のスキルマーケットプレイスとの互換性が確保され、ツール間でのスキル共有が可能になる

## いつ使うのか

複数のAI開発ツールを使っているチームで、スキルを共通化したい時。または、より広いユーザーベースにスキルを公開したい時

## やり方

1. agentskills.io または agentskill.sh の仕様を確認
2. SKILL.md に仕様準拠のメタデータを記載
3. pm-skills や product-on-purpose/pm-skills のような既存の準拠例を参考にする
4. agentskill.sh にスキルを登録（任意）
5. Claude Code, Cursor, Windsurf等でテスト

### 入力

- agentskills.io仕様ドキュメント
- 既存のスキル実装

### 出力

- クロスプラットフォーム互換のスキル
- agentskill.sh マーケットプレイス登録

## 使うツール・ライブラリ

- agentskills.io
- agentskill.sh
- pm-skills（参考実装）

## 前提知識

- Claude Codeの基本的な使い方（スキルのインストール・有効化方法）
- Gitの基本操作（clone, pull）
- Markdown記法の読み書き
- （スキル開発の場合）Python, Node.js, Bashのいずれかの基礎知識
- （MCP Server利用の場合）API認証（OAuth, API Key）の基本理解

## 根拠

> "A curated list of Claude Skills."

> "If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked."

> "skill-creator - Template / helper to build new Claude skills."

> "agentskill.sh - Browse and install 69,000+ AI agent skills for Claude Code, Cursor, Copilot, Windsurf, Zed, and 20+ AI tools."

> "pm-skills - 24 product management skills across the Triple Diamond lifecycle with agentskills.io spec compliance"
