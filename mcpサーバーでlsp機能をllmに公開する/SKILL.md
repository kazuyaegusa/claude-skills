# MCPサーバーでLSP機能をLLMに公開する

> LSP（Language Server Protocol）やJetBrains IDE解析をMCPサーバーとしてラップし、LLMが find_symbol/find_referencing_symbols 等のツールを呼び出せるようにする

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: claude-code-workflow

## なぜ使うのか

LLMがファイル全体を読まずにシンボルレベルで必要な箇所だけ取得・編集できるようになり、トークン消費削減と精度向上を実現するため

## いつ使うのか

コーディングエージェントがファイル全体を読んだり文字列検索に頼っている時、大規模プロジェクトで効率が落ちている時、40+言語のどれかをLLMで扱う時

## やり方

1. uvをインストール（uv公式サイトから）
2. `uvx --from git+https://github.com/oraios/serena serena start-mcp-server --help` でオプション確認
3. クライアント（Claude Code/Codex/Claude Desktop等）の設定ファイルにMCPサーバー起動コマンドを記述
4. クライアント起動時にSerenaが自動で立ち上がり、LLMがツールを利用可能になる
5. （オプション）JetBrains IDEを使う場合は Serena JetBrains Plugin をインストール

### 入力

- uv（Pythonパッケージマネージャー）
- MCPクライアント（Claude Code/Codex/Claude Desktop/VSCode/Cursor/Cline/Roo Code等）
- （オプション）JetBrains IDE（IntelliJ/PyCharm/WebStorm等）

### 出力

- MCPサーバープロセス
- LLMから呼び出せるツール群（find_symbol/find_referencing_symbols/insert_after_symbol等）
- シンボルレベルのコード検索・編集結果

## 使うツール・ライブラリ

- uv
- Serena（https://github.com/oraios/serena）
- 各言語のLSP実装（pyright/typescript-language-server等）
- Serena JetBrains Plugin（オプション）

## コード例

```
# インストール・起動例
uvx --from git+https://github.com/oraios/serena serena start-mcp-server

# クライアント設定例（Claude Desktop）
# ~/.config/claude/mcp_config.json
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

- MCPの基本概念（Model Context Protocolとは何か）
- LSPの基本（Language Server Protocolとは何か、なぜシンボルレベル解析ができるか）
- コーディングエージェントの基本的な動作原理（ツール呼び出し、ファイル読み書き等）
- Python/uvの基本（uvxコマンドでPythonツールを実行できる知識）
- JSONベースの設定ファイル編集（クライアント設定でMCPサーバーを登録するため）

## 根拠

> 「Serena provides essential semantic code retrieval and editing tools that are akin to an IDE's capabilities, extracting code entities at the symbol level and exploiting relational structure.」

> 「The plugin naturally supports all programming languages and frameworks that are supported by JetBrains IDEs, including IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, RubyMine, GoLand」

> 「Most users report that Serena has strong positive effects on the results of their coding agents, even when used within very capable agents like Claude Code. Serena is often described to be a game changer, providing an enormous productivity boost.」

> 「We are proud to announce that the Visual Studio Code team, together with Microsoft's Open Source Programs Office and GitHub Open Source have decided to sponsor Serena with a one-time contribution!」
