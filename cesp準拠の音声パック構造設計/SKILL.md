# CESP準拠の音声パック構造設計

> Coding Event Sound Pack Specification（CESP）に従い、各イベントカテゴリ（session.start/task.complete/input.required等）ごとにサウンドファイルと音量・ラベルをopenpeon.jsonマニフェストで定義する

- 出典: https://github.com/PeonPing/peon-ping
- 投稿者: PeonPing
- カテゴリ: ui-ux

## なぜ使うのか

イベント種別ごとに適切な音声（挨拶/完了/エラー等）を割り当て、複数パック間で互換性を保つことで、開発者が簡単にパックを切り替え・共有できる。標準化により他IDE・ツールへの移植も容易

## いつ使うのか

オリジナルの音声パックを作成・配布したい時、複数プロジェクトで異なるキャラクター音声を使い分けたい時、チームで統一パックを共有したい時

## やり方

1. パックディレクトリに`openpeon.json`を作成、`name`/`version`/`sounds`を定義
2. `sounds`配列で各音声の`category`（CESP標準：session.start/task.acknowledge/task.complete/task.error/input.required/resource.limit/user.spam）を指定
3. `file`（相対パス）、`label`（表示名）、`volume`（0.0-1.0）を各音声に設定
4. パックを`~/.openpeon/packs/<pack_name>/`に配置
5. `config.json`の`default_pack`または`pack_rotation`でパック名を指定
6. ランタイムがマニフェストを読み込み、カテゴリに応じた音声をランダム選択

### 入力

- 音声ファイル（WAV/OGG/MP3等、各CESPカテゴリに1つ以上）
- openpeon.jsonマニフェスト（CESP v1.0準拠）

### 出力

- ~/.openpeon/packs/<pack_name>/にインストール可能な音声パック
- peon packs list/use/nextコマンドで切り替え可能なパックエントリ

## 使うツール・ライブラリ

- CESP v1.0仕様（https://github.com/PeonPing/openpeon）
- JSON（マニフェスト記述）

## コード例

```
{
  "name": "peon",
  "version": "1.0.0",
  "sounds": [
    {
      "category": "session.start",
      "file": "ready-to-work.wav",
      "label": "Ready to work?",
      "volume": 0.8
    },
    {
      "category": "task.complete",
      "file": "work-work.wav",
      "label": "Work, work.",
      "volume": 0.7
    },
    {
      "category": "input.required",
      "file": "something-need-doing.wav",
      "label": "Something need doing?",
      "volume": 0.75
    }
  ]
}
```

## 前提知識

- Claude Code/Cursor/Windsurf等のフック機能を持つAI開発環境の基礎知識
- シェルスクリプト（bash/PowerShell）の基本的な読み書き
- JSON設定ファイルの編集経験
- SSH/devcontainer/Codespacesの基本（リモート通知機能を使う場合）
- Model Context Protocol（MCP）の概念（MCP機能を使う場合）

## 根拠

> 「AI coding agents don't notify you when they finish or need permission. You tab away, lose focus, and waste 15 minutes getting back into flow.」（問題定義）

> 「peon.sh is a Claude Code hook registered for SessionStart, SessionEnd, SubagentStart, Stop, Notification, PermissionRequest, PostToolUseFailure, and PreCompact events.」（フック実装の詳細）

> 「The key difference: the agent chooses the sound. Instead of automatically playing a fixed sound on every event, the agent calls play_sound with exactly what it wants」（MCP方式の差別化ポイント）

> 「Coding on a remote server or inside a container? peon-ping auto-detects SSH sessions, devcontainers, and Codespaces, then routes audio and notifications through a lightweight relay」（リモート対応の自動検出機能）

> 「path_rules: Array of { 'pattern': '...', 'pack': '...' } objects. Assigns a pack to sessions based on the working directory using glob matching」（プロジェクト別パック切り替えの仕組み）
