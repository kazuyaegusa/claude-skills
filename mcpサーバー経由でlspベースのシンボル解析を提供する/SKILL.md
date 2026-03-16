# MCPサーバー経由でLSPベースのシンボル解析を提供する

> Language Server Protocol実装をMCPサーバーでラップし、`find_symbol`/`insert_after_symbol`等のツールをLLMに公開する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: claude-code-workflow

## なぜ使うのか

LLMは通常ファイル全体を読むかgrepしかできないが、IDE同様のシンボル解決があれば必要な関数・クラスだけをピンポイントで取得・編集でき、トークン効率と精度が劇的に向上する

## いつ使うのか

コーディングエージェントが大規模プロジェクトで特定のクラス/関数を探す際、ファイル全体読み込みやgrep検索では非効率・不正確な場合

## やり方

1. `uv`をインストール
2. `uvx --from git+https://github.com/oraios/serena serena start-mcp-server --help`でオプション確認
3. Claude Code/Claude Desktop等のMCPクライアント設定ファイルに起動コマンドを追加（例: `~/.config/claude-code/mcp.json`に`{"command": "uvx", "args": ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server"]}`）
4. LLMがプロジェクト内でシンボル名を指定して検索・編集できるようになる

### 入力

- LSP対応言語（30+: Python/Java/TypeScript/Rust/Go等）のプロジェクト
- MCP対応LLMクライアント（Claude Code/Claude Desktop/Codex/VSCode+Cline等）

### 出力

- LLMがシンボル名で関数・クラス定義を取得
- 参照元・参照先シンボルのリスト
- シンボル単位での挿入・置換編集

## 使うツール・ライブラリ

- Serena (https://github.com/oraios/serena)
- uv (Pythonパッケージマネージャー)
- 各言語のLSP実装（自動管理）
- MCP SDK (Python)

## コード例

```
# MCPクライアント設定例 (~/.config/claude-code/mcp.json)
{
  "mcpServers": {
    "serena": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server"]
    }
  }
}
```

## 前提知識

- Model Context Protocol (MCP) の基本概念
- Language Server Protocol (LSP) の役割（IDE補完・参照解析の仕組み）
- LLMのツール呼び出し（Function Calling）の仕組み
- Python環境とuvパッケージマネージャーの使い方
- コーディングエージェント（Claude Code/Cursor等）の基本的な使用経験

## 根拠

> 「Serena provides essential semantic code retrieval and editing tools that are akin to an IDE's capabilities, extracting code entities at the symbol level」（シンボルレベル抽出がIDE相当）

> 「support for over 30 programming languages」（30+言語対応）

> 「Most users report that Serena has strong positive effects ... described to be a game changer, providing an enormous productivity boost」（コミュニティ評価）

> 「Visual Studio Code team, together with Microsoft's Open Source Programs Office and GitHub Open Source have decided to sponsor Serena」（Microsoft公式スポンサー）

> 「Simply implement a new tool by subclassing serena.agent.Tool and implement the apply method」（カスタムツール追加方法）
