# プラグインのインストールと利用

> Awesome Copilotマーケットプレイスから公開されているプラグイン（agents/skills/instructionsのバンドル）をCopilot CLI経由でインストールし、即座に利用する

- 出典: https://github.com/github/awesome-copilot
- 投稿者: github
- カテゴリ: agent-orchestration

## なぜ使うのか

ゼロからカスタマイズを書くのではなく、コミュニティが検証済みのベストプラクティスを再利用することで開発効率と品質を向上させる

## いつ使うのか

特定の技術スタック、ワークフロー、コーディング規約に特化したCopilot体験が必要な時

## やり方

1. `copilot plugin install <plugin-name>@awesome-copilot` でプラグインをインストール（マーケットプレイスが未登録の場合は `copilot plugin marketplace add github/awesome-copilot` を先に実行）
2. VS CodeまたはCLIでCopilotを起動すると、インストールしたプラグインのagents/skills/instructionsが自動適用される
3. Webサイト https://awesome-copilot.github.com で全文検索・フィルタリングして必要なプラグインを探す
4. AI agentから利用する場合はllms.txtを参照して機械可読形式でリソースを取得

### 入力

- プラグイン名（Awesome Copilot Webサイトまたはリポジトリのドキュメントから取得）
- Copilot CLIまたはVS Code with Copilot拡張

### 出力

- インストールされたagents/skills/instructionsがCopilotの動作に組み込まれる
- ファイルパターンに応じた自動適用されるコーディング規約
- 専用チャットコマンドやMCP server連携

## 使うツール・ライブラリ

- Copilot CLI
- VS Code
- github/awesome-copilot リポジトリ
- awesome-copilot.github.com Webサイト

## コード例

```
# プラグインインストール（マーケットプレイス登録済みの場合）
copilot plugin install <plugin-name>@awesome-copilot

# マーケットプレイス未登録の場合は先に登録
copilot plugin marketplace add github/awesome-copilot
copilot plugin install <plugin-name>@awesome-copilot
```

## 前提知識

- GitHub Copilot（個人またはOrganizationサブスクリプション）
- VS CodeまたはCopilot CLI
- 基本的なGit操作知識
- 対象技術スタック（導入するagents/skills/instructionsが対象とする言語・フレームワーク）の基礎知識

## 根拠

> 「A community-created collection of custom agents, instructions, skills, hooks, workflows, and plugins to supercharge your GitHub Copilot experience.」

> 「copilot plugin install <plugin-name>@awesome-copilot」
