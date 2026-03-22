# Teamモードでのステージ型パイプライン実行

> 複数Claude エージェントを plan→PRD→exec→verify→fix の段階的パイプラインで協調動作させる

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一エージェントでは大規模タスクで途中失敗や見落としが発生するが、Teamモードは各段階で検証ループを回すため確実に完遂できる

## いつ使うのか

TypeScriptエラー一括修正、リファクタリング、複数ファイルの同期変更など、確実な完遂が必要な時

## やり方

1. ~/.claude/settings.json に `{"env": {"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"}}` を追加
2. `/team 3:executor "fix all TypeScript errors"` のように実行（3は並列度）
3. 自動的に team-plan でタスク分割
4. team-prd で要件定義
5. team-exec で並列実行
6. team-verify で検証
7. エラーあれば team-fix で修正ループ

### 入力

- Claude Code settings.json編集権限
- OMCがインストール済み
- 修正対象のコードベース

### 出力

- タスクが完全に検証された状態で完了
- 途中の計画・実行・検証ログが残る

## 使うツール・ライブラリ

- Claude Code experimental teams feature
- oh-my-claudecode

## コード例

```
# settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}

# 実行
/team 3:executor "fix all TypeScript errors"
```

## 前提知識

- Claude Code CLIの基本操作（インストール・起動）
- Claude Max/ProサブスクリプションまたはAnthropic APIキー
- tmux（CLI workers使用時）
- Node.js/npm（プラグインインストール時）
- Git（スキルのバージョン管理時）

## 根拠

> 「Team runs as a staged pipeline: team-plan → team-prd → team-exec → team-verify → team-fix (loop)」
