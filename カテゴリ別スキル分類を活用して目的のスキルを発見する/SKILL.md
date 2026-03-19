# カテゴリ別スキル分類を活用して目的のスキルを発見する

> 12の機能別カテゴリ（Document Skills、Development & Code Tools、Data & Analysis、Scientific & Research Tools、Writing & Research、Learning & Knowledge、Media & Content、Health & Life Sciences、Collaboration & Project Management、Security & Web Testing、Utility & Automation、Collections）に整理されたスキルリストから必要なものを選ぶ

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

200以上のスキルを線形に探索すると時間がかかるが、カテゴリ分類により「今解決したい問題領域」から逆引きで候補を絞り込める

## いつ使うのか

Claude Codeで新しいタスクを実行する前、既存のスキルが存在するか確認したい時

## やり方

1. 解決したいタスクの種類を特定（例: 「Word文書を自動生成したい」→ Document Skills）
2. 該当カテゴリのセクションを読み、説明文から最適なスキルを選択
3. リンク先のGitHubリポジトリでSKILL.mdを確認
4. `~/.claude/skills/` に配置してClaude Codeで使用

### 入力

- 解決したいタスクの種類（例: PDF解析、TDD、セキュリティ監査）

### 出力

- タスクに適したスキルの候補リスト
- 各スキルのGitHubリポジトリURL

## 使うツール・ライブラリ

- awesome-claude-skills リポジトリ
- GitHub

## 前提知識

- Claude Codeの基本的な使い方（スキルの配置場所 ~/.claude/skills/ の理解）
- GitHubリポジトリのクローン方法
- npm/npx の基本操作（一部スキルのインストールに必要）
- MCP（Model Context Protocol）の概念（外部ツール連携スキルを使う場合）

## 根拠

> カテゴリ分類: '📄 Document Skills', '🛠 Development & Code Tools', '📊 Data & Analysis', '🔬 Scientific & Research Tools', '✍️ Writing & Research', '📘 Learning & Knowledge', '🎬 Media & Content', '🏥 Health & Life Sciences', '🤝 Collaboration & Project Management', '🛡 Security & Web Testing', '🔧 Utility & Automation', '🗂️ Collections'

> 収録スキル例: 'docx - Create, edit, analyze Word docs with tracked changes', 'test-driven-development - Use when implementing any feature or bugfix', 'VibeSec-Skill - VibeSec helps Claude write secure code and prevent common vulnerabilities', 'pm-skills - 24 product management skills across the Triple Diamond lifecycle'

> コレクション例: 'OpenPaw - 38-skill bundle that turns Claude Code into a personal assistant. Run via npx pawmode', 'agentskill.sh - Browse and install 69,000+ AI agent skills'

> Tip: 'If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked.'
