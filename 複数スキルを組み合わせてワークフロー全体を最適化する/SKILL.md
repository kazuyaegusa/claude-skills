# 複数スキルを組み合わせてワークフロー全体を最適化する

> TDD（test-driven-development） + セキュリティ（VibeSec） + デバッグ（systematic-debugging）のように、複数の独立したスキルを同時に有効化し、開発の各フェーズで適切なスキルが自動適用されるようにする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一スキルでは不十分な複雑なワークフロー（例: 機能開発→テスト→セキュリティ検証→デバッグ）を、専門化されたスキルの組み合わせで網羅的にカバーできるから

## いつ使うのか

エンタープライズレベルの品質基準が求められるプロジェクト、複数の専門領域（開発・QA・セキュリティ等）が関与する開発フロー

## やり方

1. プロジェクトのワークフロー全体を分析（開発→テスト→レビュー→デプロイ等）
2. 各フェーズに対応するスキルを awesome-claude-skills から選定
3. 全てのスキルを ~/.claude/skills/ にインストール
4. CLAUDE.md でスキルの優先順位・適用条件を明示（必要に応じて）
5. 開発中、各フェーズでClaude が適切なスキルを自動選択することを確認

### 入力

- プロジェクトの完全な開発ワークフロー定義
- 品質基準・コンプライアンス要件

### 出力

- 各フェーズで自動適用されるスキルセット
- 一貫性のある高品質なコード・ドキュメント

## 使うツール・ライブラリ

- test-driven-development skill
- VibeSec-Skill
- systematic-debugging skill
- defense-in-depth skill
- CLAUDE.md

## コード例

```
# ~/.claude/skills/ の構成例
~/.claude/skills/
  ├── test-driven-development/  # 機能開発時に自動適用
  ├── vibesec/                  # コード生成時にセキュリティチェック
  ├── systematic-debugging/     # バグ発生時に適用
  ├── defense-in-depth/         # レビュー時に多層防御を検証
  └── finishing-a-development-branch/  # ブランチ完了時のチェックリスト

# CLAUDE.md での優先順位設定例（オプション）
## スキル適用優先順位
1. 新機能実装時: test-driven-development → vibesec
2. バグ修正時: systematic-debugging → test-driven-development
3. ブランチマージ前: defense-in-depth → finishing-a-development-branch
```

## 前提知識

- Claude Code の基本的な使い方（セットアップ、セッション開始、基本的なプロンプト）
- ~/.claude/skills/ ディレクトリの役割とスキル読み込みの仕組み
- SKILL.md の基本構造（name, description, 使用条件等のフロントマター）
- git の基本操作（clone, pull）
- ターミナル/コマンドラインの基本操作
- （MCP利用時）Node.js/Python環境、API認証の基礎知識

## 根拠

> 「A curated list of Claude Skills」 - awesome-claude-skills リポジトリの冒頭文
