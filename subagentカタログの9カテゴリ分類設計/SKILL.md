# subagentカタログの9カテゴリ分類設計

> 130以上のsubagentを機能軸で9つのカテゴリ（Core Development, Language Specialists, Infrastructure, Quality & Security, Data & AI, Developer Experience, Specialized Domains, Business & Product, Meta & Orchestration）に分類し、それぞれをプラグインパッケージとして配布する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

分類なしでは必要なagentを探せず、導入判断もできない。カテゴリ分けにより「Pythonの専門家が欲しい→Language Specialists」「CI/CD自動化→Infrastructure」と直感的に選択でき、プラグイン単位でインストールすることで依存関係も明確化される

## いつ使うのか

大量のsubagentを管理・配布する必要があるとき

## やり方

1. 機能軸で9カテゴリを定義
2. 各agentをカテゴリ配下のディレクトリに配置（例: categories/02-language-specialists/python-pro.md）
3. カテゴリごとにplugin名を割り当て（例: voltagent-lang）
4. README.mdで各カテゴリの説明とagent一覧を記載
5. プラグインマーケットプレイスに登録

### 入力

- 130以上のsubagent定義ファイル（.md）
- 各agentの役割・専門領域の情報

### 出力

- 9カテゴリのディレクトリ構造
- 各カテゴリのREADME.md
- プラグインパッケージ（voltagent-*）

## 使うツール・ライブラリ

- Claude Code plugin marketplace
- GitHub repository

## 前提知識

- Claude Codeの基本操作（subagent作成・呼び出し）
- YAML frontmatterの理解
- Claude APIのモデル種別（opus/sonnet/haiku）の特性
- ~/.claude/agents/ と .claude/agents/ の違い（global/project-specific）
- 最小権限の原則（Principle of Least Privilege）

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.

> 9 categories: Core Development, Language Specialists, Infrastructure, Quality & Security, Data & AI, Developer Experience, Specialized Domains, Business & Product, Meta & Orchestration
