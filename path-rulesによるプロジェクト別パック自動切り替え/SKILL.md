# path_rulesによるプロジェクト別パック自動切り替え

> 作業ディレクトリのパスをGlobパターンでマッチングし、プロジェクトごとに異なる音声パックを自動適用する

- 出典: https://github.com/PeonPing/peon-ping
- 投稿者: PeonPing
- カテゴリ: context-management

## なぜ使うのか

複数プロジェクトを並行開発する際、どのターミナルタブ・セッションの通知か音声で即座に判別できれば、コンテキストスイッチが速くなる。手動切り替えの手間も省ける

## いつ使うのか

複数クライアント案件や個人/仕事プロジェクトを並行作業し、音声でプロジェクトを区別したい時、チームメンバー全員が同じパスルールを共有したい時

## やり方

1. `config.json`の`path_rules`配列に`{"pattern": "*/work/client-a/*", "pack": "glados"}`形式でルールを定義
2. セッション開始時、peon.shが`$PWD`を取得
3. Python fnmatch.fnmatchで上から順にパターンマッチを試行、最初にマッチしたルールのパックを採用
4. マッチしなければ`pack_rotation`または`default_pack`にフォールスルー
5. `/peon-ping-use <pack>`による`session_override`が最優先（パスルールより上位）

### 入力

- config.jsonのpath_rules配列（Globパターンとパック名のペア）
- セッション開始時の作業ディレクトリ（$PWD）

### 出力

- プロジェクトパスに応じた音声パックの自動選択
- 視覚的に区別可能な通知（パックごとに異なるキャラクター音声）

## 使うツール・ライブラリ

- Python fnmatch（Globマッチング）
- JSON（設定ファイル）

## コード例

```
// config.json
{
  "path_rules": [
    {"pattern": "*/work/client-a/*", "pack": "glados"},
    {"pattern": "*/personal/*", "pack": "peon"},
    {"pattern": "*/services/*", "pack": "sc_kerrigan"}
  ],
  "default_pack": "peon"
}

# CLI登録
peon packs bind glados  # カレントディレクトリにglados割り当て
peon packs bind sc_kerrigan --pattern "*/services/*"
```

## 前提知識

- Claude Code/Cursor/Windsurf等のフック機能を持つAI開発環境の基礎知識
- シェルスクリプト（bash/PowerShell）の基本的な読み書き
- JSON設定ファイルの編集経験
- SSH/devcontainer/Codespacesの基本（リモート通知機能を使う場合）
- Model Context Protocol（MCP）の概念（MCP機能を使う場合）
