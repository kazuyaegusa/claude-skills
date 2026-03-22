# oh-my-claudecodeのプラグインセットアップ

> Claude Codeにマルチエージェントオーケストレーション機能を追加する初期設定

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code単体では複雑タスクの自動分散実行ができないため、OMCプラグインで32種の専門エージェント・自動並列化・永続実行機能を導入する

## いつ使うのか

Claude Codeを初めて使う時、または複雑な開発タスクを自動化したい時の最初のステップ

## やり方

1. `/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode` でマーケットプレイス登録
2. `/plugin install oh-my-claudecode` でインストール
3. `/setup` でClaude Code初期設定
4. `/omc-setup` でOMC固有設定完了
5. `autopilot: <タスク>` で即実行可能

### 入力

- Claude Code CLI がインストール済み
- Claude Max/Pro サブスクリプション または Anthropic API key

### 出力

- OMCプラグインが有効化され、autopilot/team/ralph等のコマンドが使用可能
- ~/.claude/settings.json にOMC設定が追加

## 使うツール・ライブラリ

- Claude Code CLI
- oh-my-claudecode plugin

## コード例

```
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
/setup
/omc-setup
```

## 前提知識

- Claude Code CLIの基本操作（インストール・起動）
- Claude Max/ProサブスクリプションまたはAnthropic APIキー
- tmux（CLI workers使用時）
- Node.js/npm（プラグインインストール時）
- Git（スキルのバージョン管理時）

## 根拠

> 「Multi-agent orchestration for Claude Code. Zero learning curve.」
