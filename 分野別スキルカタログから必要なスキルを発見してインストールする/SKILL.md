# 分野別スキルカタログから必要なスキルを発見してインストールする

> awesome-claude-skillsのような分野別整理されたカタログから、プロジェクトのニーズに合致するスキルを検索し、リポジトリをクローン/ダウンロードして ~/.claude/skills/ 配下にインストールする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回プロンプトを試行錯誤するより、コミュニティで検証済みのベストプラクティスをスキル形式で導入する方が、品質・再現性・学習コストの面で圧倒的に効率的だから

## いつ使うのか

新規プロジェクト開始時、既存環境に機能追加が必要になったとき、特定分野でAIの能力不足を感じたとき

## やり方

1. awesome-claude-skills のカテゴリ一覧（Document Skills, Development & Code Tools, Data & Analysis等）から目的に合う分野を特定
2. 各スキルの説明とリンク先GitHubリポジトリを確認
3. git clone または手動ダウンロードで SKILL.md を取得
4. ~/.claude/skills/ に配置（スキル名ディレクトリを作成）
5. Claude Code セッションで自動認識されることを確認

### 入力

- プロジェクトの技術スタック・要件
- 解決したい課題（例: セキュリティ診断、テスト自動化、ドキュメント生成等）

### 出力

- ~/.claude/skills/ 配下にインストールされたスキル群
- Claude Code で即座に利用可能な専門知識

## 使うツール・ライブラリ

- awesome-claude-skills (GitHub)
- git
- Claude Code

## コード例

```
# 例: VibeSec（セキュリティスキル）をインストール
git clone https://github.com/BehiSecc/VibeSec-Skill ~/.claude/skills/vibesec

# 例: TDD スキルをインストール
git clone https://github.com/obra/superpowers ~/.claude/skills/superpowers
cd ~/.claude/skills/superpowers/skills/test-driven-development
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

> 「If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked」 - セキュリティスキルの重要性を強調

> 「test-driven-development - Use when implementing any feature or bugfix, before writing implementation code」 - TDDスキルの説明

> 「linear-claude-skill - Manage Linear issues, projects, and teams with MCP tools, SDK scripts, and GraphQL fallbacks」 - MCP連携スキルの例

> 「claude-starter - Production-ready Claude Code configuration template with 40 auto-activating skills across 8 domains, TOON format support for 30-60% token savings」 - 大規模スキルコレクションの例
