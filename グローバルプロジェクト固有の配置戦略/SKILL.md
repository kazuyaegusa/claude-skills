# グローバル/プロジェクト固有の配置戦略

> `~/.claude/agents/` に配置したエージェントは全プロジェクトで利用可能(グローバル)、`.claude/agents/` に配置したエージェントは当該プロジェクトのみで有効(ローカル)とし、同名の場合はローカルが優先される

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

チーム共通のワークフロー(コードレビュー、セキュリティ監査等)はグローバルで統一し、プロジェクト固有のカスタマイズ(特定フレームワーク用のlint設定等)はローカルで上書きできるようにするため。これにより一貫性と柔軟性を両立する

## いつ使うのか

チーム全体で標準化したいエージェントはグローバルに、プロジェクト固有のルール(例: 特定のlinter設定、独自フレームワーク)を持つ場合はローカルに配置

## やり方

1. **グローバル配置**: `cp categories/04-quality-security/code-reviewer.md ~/.claude/agents/` で全プロジェクトから利用可能にする
2. **プロジェクト固有配置**: `cp categories/02-language-specialists/python-pro.md .claude/agents/` で当該リポジトリ専用のカスタマイズ版を作成
3. 同名エージェントが両方に存在する場合、Claude Codeは `.claude/agents/` を優先して読み込む
4. チーム標準エージェントはdotfilesリポジトリや社内パッケージでグローバル配布し、個別プロジェクトの要件は `.claude/agents/` でオーバーライド
5. `.gitignore` に `.claude/agents/` を追加するか、チーム共有したい場合はコミットする

### 入力

- エージェント定義ファイル
- 配置先(~/.claude/agents/ または .claude/agents/)

### 出力

- Claude Codeから呼び出し可能なエージェント
- 優先度に従った名前解決(ローカル > グローバル)

## 使うツール・ライブラリ

- ファイルシステム
- Git(.gitignore)

## コード例

```
# グローバル配置(全プロジェクト共通)
cp categories/04-quality-security/code-reviewer.md ~/.claude/agents/

# プロジェクト固有配置
cp categories/02-language-specialists/python-pro.md .claude/agents/

# .gitignore
.claude/agents/  # または共有したい場合はコミット
```

## 前提知識

- Claude Code CLIの基本操作(/agents コマンド、サブエージェント概念)
- Markdownの読み書き(frontmatterとYAML構文)
- Bashコマンド(curl, chmod)の基礎知識
- プロジェクトとグローバルの設定ファイル配置の違い(~/.config vs .config的な概念)
- 開発ライフサイクル(開発→テスト→デプロイ→運用)の理解
