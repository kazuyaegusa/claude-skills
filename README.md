# Claude Code Skills & Config Sync

kazuyaegusa の Claude Code 環境（スキル・設定・コマンド）を Git で管理し、複数デバイス間で自動同期するリポジトリ。

## 新しいデバイスでのセットアップ（1コマンド）

```bash
curl -sL https://raw.githubusercontent.com/kazuyaegusa/claude-skills/main/setup-env.sh | bash
```

または手動:

```bash
git clone https://github.com/kazuyaegusa/claude-skills.git ~/.claude/skills
bash ~/.claude/skills/setup-env.sh
```

これにより以下が自動で行われる:

1. `~/.claude/skills/` にスキルリポジトリを配置
2. `~/.claude/CLAUDE.md`（グローバル開発ルール）を配置
3. `~/.claude/settings.json`（Claude Code 設定）を配置
4. `~/.claude/commands/*.md`（スラッシュコマンド）を配置
5. macOS の場合 launchd で 5分おき自動同期を設定

## 同期される設定一覧

| ファイル | 説明 | 同期先 |
|---|---|---|
| `_config/CLAUDE.md` | グローバル開発ルール（日本語応答、チーム自動編成、ハルシネーション防止等） | `~/.claude/CLAUDE.md` |
| `_config/settings.json` | Claude Code 設定（モデル、Agent Teams 有効化等） | `~/.claude/settings.json` |
| `_config/keybindings.json` | キーバインド設定（存在する場合のみ） | `~/.claude/keybindings.json` |
| `_config/commands/*.md` | スラッシュコマンド定義 | `~/.claude/commands/*.md` |
| `_config/mcp.json.template` | MCP サーバー設定テンプレート（手動設定が必要） | 手動 |
| `*/SKILL.md` | 各スキル本体（219+ スキル） | そのまま `~/.claude/skills/` 配下 |
| `_index.md` | スキル索引（自動生成、自動スキル選択に使用） | そのまま |

## カスタムスキル（自作）

| スキル | コマンド | 説明 |
|---|---|---|
| `discord-context-search` | `/discord-context-search <キーワード>` | Discord エクスポートデータから文脈検索・要約 |
| `folder-digest` | `/folder-digest [パス]` | フォルダ内容を構造化レポートとして出力 |
| `pdf-logo-remover` | `/remove-pdf-logo <PDF>` | PDF からロゴ/ウォーターマークを一括除去 |
| `phase-report` | `/phase-report` | フェーズ完了レポートを自動生成・コミット・プッシュ |
| `project-review` | `/project-review [パス]` | プロジェクトを多角的にレビュー・修正 |
| `quality-harness` | `/quality-harness [パス]` | Python プロジェクトに品質ハーネスを一括セットアップ |
| `repo-tracker` | `/repo-tracker <GitHub URL>` | GitHub リポジトリの変更を定期監視・Discord通知 |

## カスタムコマンド（スラッシュコマンド）

| コマンド | 説明 |
|---|---|
| `/codex-review` | OpenAI Codex でコードレビュー |
| `/ecc-ja` | Everything Claude Code 日本語ナビ |
| `/install-skill` | スキルカタログからインストール |
| `/list-skills` | インストール済みスキル一覧 |
| `/search-skills` | スキルカタログ検索 |
| `/remove-pdf-logo` | PDF ロゴ除去 |

## 自動同期の仕組み

```
[Mac A] ~/.claude/                [Mac B] ~/.claude/
   |                                  |
   | sync_config_to_repo()            | sync_config_to_repo()
   v                                  v
[Mac A] ~/.claude/skills/_config/ ←→ [Mac B] ~/.claude/skills/_config/
   |                   ^               |                   ^
   | git push          | git pull      | git push          | git pull
   v                   |               v                   |
   +---→ GitHub (kazuyaegusa/claude-skills.git) ←---+
```

- `_config/sync.sh` が launchd により 5分ごとに実行
- ローカル変更を `_config/` にコピー → commit → push
- リモート変更を pull → `_config/` から `~/.claude/` にコピー
- 競合時は `pull --rebase` で自動解決

## 手動同期

```bash
bash ~/.claude/skills/_config/sync.sh
```

## 同期ログ

```bash
tail -20 ~/.claude/sync.log
```

## ディレクトリ構造

```
~/.claude/skills/
├── README.md              ← このファイル
├── setup-env.sh           ← 新デバイス用ブートストラップ
├── _config/               ← 同期設定ファイル
│   ├── CLAUDE.md
│   ├── settings.json
│   ├── keybindings.json   （存在する場合）
│   ├── commands/*.md
│   ├── mcp.json.template
│   └── sync.sh            ← 自動同期スクリプト
├── _index.md              ← スキル索引（自動生成）
├── discord-context-search/ ← 自作スキル
├── folder-digest/
├── pdf-logo-remover/
├── phase-report/
├── project-review/
├── quality-harness/
├── repo-tracker/
├── everything-claude-code-ja/
└── (200+ コミュニティスキル)/
```
