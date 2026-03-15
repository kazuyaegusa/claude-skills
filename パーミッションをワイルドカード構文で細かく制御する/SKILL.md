# パーミッションをワイルドカード構文で細かく制御する

> `dangerously-skip-permissions` の代わりに `/permissions` でワイルドカード構文を使い、必要最小限の権限だけを付与する

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

全権限スキップはセキュリティリスクが高い。ワイルドカードで「npmスクリプトは全て許可するがrm -rfは許可しない」のような細かい制御が可能

## いつ使うのか

自動化セッションで毎回パーミッション確認のプロンプトが出て作業が止まる場合。ただし全スキップは避けたい場合

## やり方

1. `/permissions` コマンドを実行
2. Bash操作は `Bash(npm run *)` のようにコマンドパターンで許可
3. ファイル編集は `Edit(/docs/**)` のようにパスパターンで許可
4. `/sandbox` と組み合わせてファイル・ネットワーク隔離も設定可能

### 入力

- 許可したい操作パターンの一覧

### 出力

- 細粒度のパーミッション設定
- 安全な自動実行環境

## 使うツール・ライブラリ

- /permissions
- /sandbox
- .claude/settings.json

## コード例

```
# settings.json
{
  "permissions": {
    "allow": ["Bash(npm run *)", "Edit(/src/**)"],
    "deny": ["Bash(rm -rf *)"]
  }
}
```

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> 「公式・コミュニティのClaude Codeベストプラクティスを1箇所にまとめたリポジトリがGitHub月間トレンド入り」

> 「プログラムではなく、情報をまとめたマークダウンがトレンド入りするのがまさに今っぽい。最もレバレッジが効く場所がプログラムではなく、ナレッジになった感」
