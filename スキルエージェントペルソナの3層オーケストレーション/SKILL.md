# スキル・エージェント・ペルソナの3層オーケストレーション

> スキル（How）、エージェント（What）、ペルソナ（Who）を組み合わせて、ドメイン横断的な複雑タスクをフェーズ分けして実行する

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

1つのスキルでは対応できない、複数専門領域にまたがる業務（プロダクトローンチ、アーキテクチャ移行等）を、段階的に適切な専門性を切り替えながら進められる

## いつ使うのか

スタートアップの6週間プロダクトローンチ、技術スタック移行、コンプライアンス監査など、複数の専門領域を順次またはパラレルに適用する必要がある場合

## やり方

1. タスクをフェーズに分割（例: 設計→実装→マーケティング→分析）
2. 各フェーズに適したペルソナを選択（例: startup-cto → growth-marketer → solo-founder）
3. 各ペルソナに必要なスキルをスタック（例: aws-solution-architect + senior-frontend）
4. フェーズごとにペルソナ + スキルセットを切り替えて実行
5. 必要に応じてマルチエージェントレビュー（複数ペルソナが相互チェック）を実施

### 入力

- プロジェクト全体の目標とフェーズ定義
- 各フェーズで必要な専門性のリスト
- 利用可能なペルソナ・スキルのカタログ

### 出力

- フェーズごとの成果物（設計書、実装コード、マーケティング資料等）
- フェーズ間のハンドオフドキュメント
- 最終統合アウトプット

## 使うツール・ライブラリ

- orchestration/ORCHESTRATION.md の4パターン（Solo Sprint, Domain Deep-Dive, Multi-Agent Handoff, Skill Chain）

## コード例

```
# 6週間プロダクトローンチの例
# Week 1-2: 設計・実装
cp agents/personas/startup-cto.md ~/.claude/agents/
/plugin install aws-solution-architect@claude-code-skills
/plugin install senior-frontend@claude-code-skills

# Week 3-4: マーケティング準備
cp agents/personas/growth-marketer.md ~/.claude/agents/
/plugin install launch-strategy@claude-code-skills
/plugin install seo-audit@claude-code-skills

# Week 5-6: ローンチ・分析
cp agents/personas/solo-founder.md ~/.claude/agents/
/plugin install analytics-tracking@claude-code-skills
```

## 前提知識

- Claude CodeまたはOpenAI Codex等のAIコーディングツールの基本的な使い方
- SKILL.md形式やエージェント概念の理解（ただしREADMEに説明あり）
- Bash/シェルスクリプトの基本知識（インストールスクリプト実行用）
- Python 3.x の実行環境（CLIツール使用時）
- Git/GitHub の基本操作
