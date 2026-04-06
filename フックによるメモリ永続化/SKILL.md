# フックによるメモリ永続化

> SessionStartフックで前回の文脈を自動ロード、SessionEndフックで現在の状態を自動保存し、セッション間での文脈保持を実現

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはデフォルトではセッション終了時に文脈が失われる。手動で文脈をコピー・ペーストする手間を排除し、長期プロジェクトでの生産性を維持

## いつ使うのか

複数日にまたがるプロジェクト、またはセッションをまたいで同じタスクを継続する場合

## やり方

1. hooks/memory-persistence/ ディレクトリのフックをhooks.jsonに登録
2. SessionStartイベントで scripts/hooks/session-start.js が実行され、~/.claude/sessions/<session-id>/context.json から前回のTODO・ファイルパス・変数名等を読み込み
3. SessionEndイベントで scripts/hooks/session-end.js が現在の文脈を同パスに保存
4. pre-compactフックで scripts/hooks/pre-compact.js がコンパクション前の状態をバックアップ

### 入力

- hooks.json への設定追加
- scripts/hooks/*.js の配置

### 出力

- ~/.claude/sessions/<session-id>/context.json に文脈保存
- セッション再開時の自動文脈ロード

## 使うツール・ライブラリ

- Node.js
- Claude Code hooks.json

## コード例

```
// hooks.json 抜粋
{
  "matcher": "event == 'SessionStart'",
  "hooks": [{
    "type": "command",
    "command": "node scripts/hooks/session-start.js"
  }]
}
```

## 前提知識

- Claude Code CLI v2.1.0以降、またはCursor/OpenCode/Codexのいずれか
- npm/pnpm/yarn/bunのいずれかのパッケージマネージャー
- Gitの基本操作（クローン、コミット）
- JSON/YAML形式の理解
- 対象言語のテストフレームワーク（pytest/jest/go test等）の基礎知識
- （オプション）claude -p サブスクリプション認証（継続学習に必要）
