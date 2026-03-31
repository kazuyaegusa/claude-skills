# シンボルレベルツールでコードを検索・編集する

> find_symbol でシンボル名から定義箇所を特定し、find_referencing_symbols で使用箇所を列挙し、insert_after_symbol で既存のシンボルの後に新コードを挿入する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: other

## なぜ使うのか

ファイル全体やgrep結果を読むよりトークン消費が少なく、構造を理解した正確な編集ができるため

## いつ使うのか

特定の関数・クラス・変数を探す時、リファクタリングで参照関係を把握したい時、ファイルが長すぎてトークン制限に引っかかる時

## やり方

1. LLMがタスクを受け取る（例：「calculate_total関数をリファクタリング」）
2. LLMが find_symbol("calculate_total") を呼び出し、定義箇所を取得
3. find_referencing_symbols("calculate_total") で呼び出し元を列挙
4. 必要に応じて insert_after_symbol で新関数を追加、またはシンボル単位で置換
5. 変更が完了したらコミット

### 入力

- シンボル名（関数名/クラス名/変数名等）
- Serena MCPサーバーが起動済みの状態

### 出力

- シンボルの定義位置（ファイルパス+行番号）
- シンボルの参照一覧
- コード挿入・編集の成功/失敗

## 使うツール・ライブラリ

- find_symbol
- find_referencing_symbols
- insert_after_symbol（Serenaの提供ツール）

## コード例

```
// LLMが呼び出すツールの例（概念的表記）
find_symbol({"name": "calculate_total"})
// -> {"file": "src/billing.py", "line": 42, "definition": "def calculate_total(items): ..."}

find_referencing_symbols({"symbol": "calculate_total"})
// -> [{"file": "src/checkout.py", "line": 18}, {"file": "tests/test_billing.py", "line": 5}]

insert_after_symbol({"symbol": "calculate_total", "code": "def calculate_tax(amount): ..."})
```

## 前提知識

- MCPの基本概念（Model Context Protocolとは何か）
- LSPの基本（Language Server Protocolとは何か、なぜシンボルレベル解析ができるか）
- コーディングエージェントの基本的な動作原理（ツール呼び出し、ファイル読み書き等）
- Python/uvの基本（uvxコマンドでPythonツールを実行できる知識）
- JSONベースの設定ファイル編集（クライアント設定でMCPサーバーを登録するため）

## 根拠

> 「With it, the agent no longer needs to read entire files, perform grep-like searches or basic string replacements to find the right parts of the code and to edit code. Instead, it can use code-centric tools like find_symbol, find_referencing_symbols and insert_after_symbol.」
