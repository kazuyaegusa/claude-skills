# スキルのセキュリティ監査とベッティングを実施する

> スキルは任意コード実行可能なため、導入前にSKILL.mdと全スクリプトをレビューし、信頼できるソース・バージョン管理・最小権限原則・定期監査を適用する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

悪意あるスキルはデータ漏洩・プロンプトインジェクション増幅・セキュリティ侵害を引き起こし得る。企業環境では特にリスク管理が必須

## いつ使うのか

新規スキル導入時、エンタープライズ環境への展開前、定期監査実施時

## やり方

1. 信頼できるソース（公式、著名コミュニティ、内製）からのみ導入
2. SKILL.md、scripts/内の全コード、resources/を手動レビュー
3. 機密データアクセス要求があるスキルは慎重に評価
4. Gitでバージョン管理、タグ付けしてロールバック可能に
5. コードレビュー・ピアレビューを経てチーム配布
6. 最小権限原則で必要な権限のみ付与
7. 定期的にインストール済みスキルを監査
8. 非本番環境で徹底的にテスト後、本番導入
9. エンタープライズでは内部リポジトリ・承認フローを整備
10. 既知の脆弱性レポート（例: 'Weaponizing Claude Code Skills'）を参照

### 入力

- スキルフォルダ一式
- セキュリティポリシー

### 出力

- レビュー済み・承認済みスキル、監査ログ

## 使うツール・ライブラリ

- Git
- コードレビューツール
- 内部承認フロー

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Freeプランではスキル利用不可）
- YAML frontmatter、Markdown記法の基礎知識
- Git/GitHubの基本操作（バージョン管理・配布時）
- Python/JavaScriptなどスクリプト言語の基礎（カスタムスキル作成時）
- Claude Code CLI、Claude.ai、またはClaude APIの利用経験
- プロンプトエンジニアリング、MCP、Subagents、Projectsとの違いの理解

## 根拠

> Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> Use skill-creator: 1. Enable the skill-creator skill 2. Ask Claude: 'Use the skill-creator to help me build a skill for [your task]' 3. Answer the interactive questions 4. Claude generates the complete skill structure

> **Oct 16, 2025**: Claude Skills officially announced - Available across Claude.ai, Code, and API

> Security: Malicious skills may introduce vulnerabilities or enable data exfiltration, Prompt injection attacks could be amplified, Weaponizing Claude Code Skills研究レポート存在

> Enterprise: As of October 2025, Claude.ai does not support centralized admin management for custom skills. Use version control and internal repositories.
