# MCPサーバー経由のエージェント主導型音声選択

> Model Context Protocol（MCP）サーバーを起動し、AIエージェントが`play_sound`ツールで任意の音声を直接指定・再生できるようにする

- 出典: https://github.com/PeonPing/peon-ping
- 投稿者: PeonPing
- カテゴリ: agent-orchestration

## なぜ使うのか

フック方式は固定イベントにしか反応しないが、MCP方式ではエージェント自身が状況判断して最適な音声を選べる（ビルド失敗時に`duke_nukem/SonOfABitch`、ファイル読み込み時に`sc_kerrigan/IReadYou`等）。より文脈に即した通知が可能

## いつ使うのか

エージェントが状況に応じて最適な音声を選びたい時、カスタムスキルやワークフロー内で明示的に音声を鳴らしたい時、Claude Desktop/Cursor等MCP対応環境で使用

## やり方

1. MCPクライアント設定（Claude Desktop/Cursor等）に`peon-mcp.js`を登録
2. `{"mcpServers": {"peon-ping": {"command": "node", "args": ["/path/to/peon-mcp.js"]}}}`
3. エージェントがMCPツール`play_sound`を呼び出し、引数に音声キー（`duke_nukem/SonOfABitch`）を指定
4. MCPサーバーがconfig.jsonとパックマニフェストを読み込み、指定キーの音声ファイルを再生
5. カタログリソース（`peon-ping://catalog`）でエージェントが事前に全パック・音声一覧をプリフェッチ可能

### 入力

- Node.js 18+
- peon-mcp.js（MCPサーバー実装）
- MCPクライアント設定ファイル

### 出力

- エージェントからの`play_sound`ツール呼び出しによる音声再生
- カタログリソース経由で全パック・音声一覧の取得

## 使うツール・ライブラリ

- Node.js
- Model Context Protocol SDK
- peon-mcp.js（提供スクリプト）

## コード例

```
// MCPクライアント設定（Claude Desktop等）
{
  "mcpServers": {
    "peon-ping": {
      "command": "node",
      "args": ["$(brew --prefix peon-ping)/libexec/mcp/peon-mcp.js"]
    }
  }
}

// エージェント側ツール呼び出し例
play_sound({"sound_key": "duke_nukem/SonOfABitch"})
play_sound({"sound_keys": ["sc_kerrigan/IReadYou", "glados/OhItsYou"]})
```

## 前提知識

- Claude Code/Cursor/Windsurf等のフック機能を持つAI開発環境の基礎知識
- シェルスクリプト（bash/PowerShell）の基本的な読み書き
- JSON設定ファイルの編集経験
- SSH/devcontainer/Codespacesの基本（リモート通知機能を使う場合）
- Model Context Protocol（MCP）の概念（MCP機能を使う場合）
