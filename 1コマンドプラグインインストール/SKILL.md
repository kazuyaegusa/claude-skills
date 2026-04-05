# 1コマンドプラグインインストール

> 依存関係チェック・フックスクリプト配置・Worker起動を単一コマンドで完了させる

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

複雑なセットアップは導入障壁になる。キャッシュ済み依存チェック + 自動Bun/uvインストールで初回実行を高速化

## いつ使うのか

Claude Codeに永続メモリを導入したい時（初回セットアップ）

## やり方

1. `npx claude-mem install` 実行
2. 依存チェッカー（pre-hookスクリプト）がBun/Node.js/uvを検証
3. 不足している場合は自動インストール
4. 7つのフックスクリプトを `~/.claude/hooks/` にコピー
5. Workerサービス起動（Bun管理、port 37777）
6. Claude Code再起動で有効化

### 入力

- Claude Codeインストール（`~/.claude/` 存在）

### 出力

- フックスクリプト配置完了
- Workerサービス起動
- 設定ファイル `~/.claude-mem/settings.json` 生成

## 使うツール・ライブラリ

- npx（npm package runner）
- Bun（JavaScriptランタイム）
- uv（Python環境管理）

## コード例

```
# インストールコマンド
npx claude-mem install

# Gemini CLI用
npx claude-mem install --ide gemini-cli

# プラグインマーケットプレイス経由
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

## 前提知識

- Claude Codeの基本操作とプラグインシステムの理解
- Node.js 18.0.0+の実行環境
- SQLiteの基本概念（テーブル、クエリ）
- ベクトル検索・埋め込みの基礎知識（Chroma理解のため）
- ライフサイクルフック・イベント駆動設計の概念
- TypeScript/JavaScript（カスタマイズ時）

## 根拠

> 「Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.」

> 「Install with a single command: npx claude-mem install」
