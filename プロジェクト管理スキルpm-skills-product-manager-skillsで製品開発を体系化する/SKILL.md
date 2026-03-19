# プロジェクト管理スキル（pm-skills, Product-Manager-Skills）で製品開発を体系化する

> Collaboration & Project Management カテゴリのスキル（pm-skills 24スキル、Product-Manager-Skills）を導入し、プロダクト発見、優先順位付け、PRD作成、ロードマップ計画、SaaSメトリクス分析などのPMワークフローをClaude Codeに実行させる

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

プロダクトマネージャーの業務は定型化できる部分が多いが、フレームワークやテンプレートの管理が煩雑。スキルとして体系化すれば、Claude Codeが自動的に適切なフレームワーク（例: RICE優先順位付け、Jobs-to-be-Done分析）を適用し、PMの思考プロセスを支援する

## いつ使うのか

プロダクトロードマップ作成、機能優先順位付け、PRD執筆、ユーザーインタビュー分析など、PMの定型業務を実行する時

## やり方

1. pm-skills または Product-Manager-Skills をGitHubからクローン
2. 各スキルのSKILL.mdを `~/.claude/skills/` に配置
3. Claude Codeに「新機能の優先順位をつけて」と依頼すると、RICEフレームワークを適用した分析が返る
4. 「PRDを書いて」と依頼すると、テンプレートに沿った構造化文書が生成される
5. Jira/Linear等と連携して、分析結果をissue/epicに反映

### 入力

- プロダクト要件、ユーザーフィードバック、ビジネス目標

### 出力

- 優先順位付けされた機能リスト
- 構造化されたPRD
- ロードマップドキュメント
- SaaSメトリクス分析レポート

## 使うツール・ライブラリ

- pm-skills (24スキル、agentskills.io準拠)
- Product-Manager-Skills
- Jira/Linear（任意）

## 前提知識

- Claude Codeの基本的な使い方（スキルの配置場所 ~/.claude/skills/ の理解）
- GitHubリポジトリのクローン方法
- npm/npx の基本操作（一部スキルのインストールに必要）
- MCP（Model Context Protocol）の概念（外部ツール連携スキルを使う場合）

## 根拠

> 投稿タイトル: 'BehiSecc/awesome-claude-skills - A curated list of Claude Skills.'

> カテゴリ分類: '📄 Document Skills', '🛠 Development & Code Tools', '📊 Data & Analysis', '🔬 Scientific & Research Tools', '✍️ Writing & Research', '📘 Learning & Knowledge', '🎬 Media & Content', '🏥 Health & Life Sciences', '🤝 Collaboration & Project Management', '🛡 Security & Web Testing', '🔧 Utility & Automation', '🗂️ Collections'

> 収録スキル例: 'docx - Create, edit, analyze Word docs with tracked changes', 'test-driven-development - Use when implementing any feature or bugfix', 'VibeSec-Skill - VibeSec helps Claude write secure code and prevent common vulnerabilities', 'pm-skills - 24 product management skills across the Triple Diamond lifecycle'

> コレクション例: 'OpenPaw - 38-skill bundle that turns Claude Code into a personal assistant. Run via npx pawmode', 'agentskill.sh - Browse and install 69,000+ AI agent skills'

> Tip: 'If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked.'
