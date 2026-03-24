# カテゴリ別サブエージェント分類

> 127個のサブエージェントを10カテゴリ(Core Development、Language Specialists、Infrastructure、Quality & Security、Data & AI、Developer Experience、Specialized Domains、Business & Product、Meta & Orchestration、Research & Analysis)に整理する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

タスクの性質に応じて適切な専門家を素早く見つけられるようにするため。開発・運用・品質・ビジネスの各フェーズで必要なスキルセットを分離することで、オーバーヘッドなく最適なエージェントを選択できる

## いつ使うのか

サブエージェントが10個を超えて管理が煩雑になった時、またはチームメンバーが目的のエージェントを探しづらくなった時

## やり方

1. 開発ライフサイクル(開発→テスト→デプロイ→運用)とドメイン軸(言語/インフラ/データなど)でマトリクスを作成
2. 各サブエージェントの責務を明確に定義(例: `api-designer` はREST/GraphQL設計、`terraform-engineer` はIaC専門)
3. カテゴリごとにディレクトリ(`categories/01-core-development/`等)とプラグイン名(`voltagent-core-dev`等)を対応させる
4. README内でカテゴリ表にリンクとバッジを配置し、視覚的にナビゲート可能にする

### 入力

- サブエージェント定義ファイル(Markdown形式、frontmatterでname/description/tools/modelを記述)
- 各エージェントの責務と適用ドメイン

### 出力

- カテゴリ別ディレクトリ構造(categories/01-XX/, categories/02-YY/...)
- README内のカテゴリ表とプラグイン名マッピング

## 使うツール・ライブラリ

- Markdown
- Claude Code plugin system

## 前提知識

- Claude Code CLIの基本操作(/agents コマンド、サブエージェント概念)
- Markdownの読み書き(frontmatterとYAML構文)
- Bashコマンド(curl, chmod)の基礎知識
- プロジェクトとグローバルの設定ファイル配置の違い(~/.config vs .config的な概念)
- 開発ライフサイクル(開発→テスト→デプロイ→運用)の理解
