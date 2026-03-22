# ドメイン特化型スキルコレクションを一括導入する

> claude-starter（40スキル）、Agent Almanac（317スキル）、agentskills.sh（69,000+スキル）のような大規模コレクションから、プロジェクトに最適なスキルセットを一括インストールする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: agent-orchestration

## なぜ使うのか

個別にスキルを探す手間を省き、実績のあるスキルセットをテンプレートとして導入することで、立ち上げ時間を大幅に短縮できるから

## いつ使うのか

新規プロジェクトの初期セットアップ時、特定分野（科学計算、AWS開発、プロダクトマネジメント等）で体系的なスキルセットが必要なとき

## やり方

1. プロジェクトの特性を分析（フロントエンド中心、データ分析中心、セキュリティ重視等）
2. 対応するコレクションを選定（例: claude-starter for 汎用開発、K-Dense-AI/claude-scientific-skills for 科学計算）
3. git clone でリポジトリ全体を取得
4. 不要なスキルを削除、必要なスキルのみ ~/.claude/skills/ にシンボリックリンクまたはコピー
5. README に従って追加設定（MCP サーバー、API キー等）を実施
6. サンプルプロジェクトで動作確認

### 入力

- プロジェクトのドメイン・技術スタック
- コレクションのドキュメント・README

### 出力

- プロジェクト最適化されたスキルセット（数十〜数百スキル）
- 即座に利用可能なAI開発環境

## 使うツール・ライブラリ

- claude-starter
- Agent Almanac
- agentskills.sh
- K-Dense-AI/claude-scientific-skills
- aws-skills

## コード例

```
# 例: claude-starter（40スキル）を一括導入
git clone https://github.com/raintree-technology/claude-starter
cd claude-starter
cp -r skills/* ~/.claude/skills/

# 例: 科学計算プロジェクト向け
git clone https://github.com/K-Dense-AI/claude-scientific-skills
cd claude-scientific-skills
# 必要なスキルのみ選択的にコピー
cp -r bioinformatics cheminformatics machine-learning ~/.claude/skills/

# 例: agentskills.sh から検索してインストール
# （ブラウザで https://agentskill.sh を開き、キーワード検索→インストールコマンドをコピー）
```

## 前提知識

- Claude Code の基本的な使い方（セットアップ、セッション開始、基本的なプロンプト）
- ~/.claude/skills/ ディレクトリの役割とスキル読み込みの仕組み
- SKILL.md の基本構造（name, description, 使用条件等のフロントマター）
- git の基本操作（clone, pull）
- ターミナル/コマンドラインの基本操作
- （MCP利用時）Node.js/Python環境、API認証の基礎知識

## 根拠

> 「docx - Create, edit, analyze Word docs with tracked changes, comments, formatting」 - ドキュメント処理スキルの例

> 「test-driven-development - Use when implementing any feature or bugfix, before writing implementation code」 - TDDスキルの説明

> 「claude-starter - Production-ready Claude Code configuration template with 40 auto-activating skills across 8 domains, TOON format support for 30-60% token savings」 - 大規模スキルコレクションの例

> 「agentskills.sh - Browse and install 69,000+ AI agent skills for Claude Code, Cursor, Copilot, Windsurf, Zed, and 20+ AI tools」 - 最大規模のスキルマーケットプレイス
