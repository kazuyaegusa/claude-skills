# Usage Monitoringによるコスト最適化

> ローカルのClaude Codeログを解析し、プロジェクト別・モデル別のトークン消費量、コスト、使用パターンをダッシュボードで可視化

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

どのプロジェクトが高コストか、どのプロンプトが非効率かを把握しないと、予算超過やトークン枯渇のリスクが高まる

## いつ使うのか

複数プロジェクトでClaude Codeを使用、予算管理が必要、チームでコスト配分を追跡したい時

## やり方

1. Usage MonitoringツールをインストールしてClaude Codeログにアクセス権を付与
2. ツールがログをパースし、トークン・コスト・モデル使用率を集計
3. Webダッシュボードまたはターミナルで可視化
4. アラート設定で上限到達時に通知

### 入力

- Claude Codeのログファイル（~/.local/share/claude/logs等）

### 出力

- プロジェクト別・モデル別コストレポート
- Burn Rate予測とアラート

## 使うツール・ライブラリ

- ccflare（美しいWebダッシュボード）
- CC Usage（CLIベース統計）
- Claudex（フルテキスト検索付きブラウザ）

## コード例

```
# 例: CC Usageで月間コスト確認
ccusage report --month 2025-04
# Output:
# Project A: $45.32 (Sonnet-4.5)
# Project B: $12.18 (Haiku)
# Total: $57.50
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- Git/GitHubの基礎知識（ブランチ、コミット、PR）
- ターミナル操作とシェルスクリプトの基本
- Markdown記法の理解
- 使用する言語・フレームワークの基礎知識（TypeScript、Python、Go等）
