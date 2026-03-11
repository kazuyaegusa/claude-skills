---
name: repo-security-clone
description: GitHub リポジトリの URL を受け取り、セキュリティチェック → クローン → 内容説明を一連で行うスキル。
user_invocable: true
---

# Repo Security Clone — リポジトリ安全クローン＆解説スキル

GitHub リポジトリの URL を受け取り、セキュリティ観点で中身を精査した上でクローンし、何ができるリポなのかを分かりやすく説明する。

## 引数

```
/repo-security-clone <GitHubリポジトリURL> [--dir <クローン先ディレクトリ>]
```

- **GitHubリポジトリURL**（必須）: `https://github.com/owner/repo` 形式
- **--dir**（省略可）: クローン先の親ディレクトリ。省略時はカレントディレクトリ

## 実行手順

### Phase 1: メタデータ収集

以下を **並列** で実行する:

1. `gh repo view <owner/repo> --json name,description,visibility,defaultBranchRef,languages,licenseInfo,pushedAt,stargazerCount,forkCount` でリポ概要を取得
2. `gh api repos/<owner/repo>/contents` でルート直下のファイル一覧を取得
3. `gh api repos/<owner/repo>/contents/README.md --jq '.content' | base64 -d` で README を取得

### Phase 2: セキュリティチェック

以下の観点で中身を精査する。必要に応じて追加ファイルを `gh api` で取得する。

#### 2-1. 依存関係の確認
- `package.json`, `requirements.txt`, `Pipfile`, `Gemfile`, `go.mod`, `Cargo.toml`, `Package.swift`, `build.gradle`, `pom.xml` 等のパッケージマニフェストを読み取る
- 外部依存ライブラリの一覧を確認し、不審なパッケージがないかチェック
- 既知の悪意あるパッケージ名（typosquatting 等）に注意

#### 2-2. スクリプト・フックの確認
- `scripts/`, `hooks/`, `.husky/` 等のディレクトリ内のシェルスクリプトを確認
- `postinstall`, `preinstall` 等のライフサイクルフックに不審なコマンドがないか確認
- `Makefile`, `Dockerfile`, `docker-compose.yml`, CI 設定ファイル（`.github/workflows/`）を確認

#### 2-3. 危険パターンの検出
以下のパターンがないか注意する:
- 外部 URL への `curl | sh` や `wget | bash` パターン
- 環境変数やクレデンシャルの外部送信
- 難読化されたコード（base64 エンコードされた実行コード等）
- `eval()`, `exec()` の不審な使用
- ネットワークアクセスを行うインストールスクリプト

#### 2-4. ライセンス確認
- ライセンスの種類を確認（MIT, Apache, GPL 等）
- ライセンスなしの場合はユーザーに警告

### Phase 3: セキュリティ判定・報告

チェック結果をユーザーに報告する。以下の形式で出力:

```
**セキュリティチェック結果:**
- ライセンス: [ライセンス名]
- 外部依存: [依存パッケージの概要と懸念の有無]
- スクリプト: [ビルド/インストールスクリプトの安全性]
- 危険パターン: [検出の有無]
- 総合判定: ✅ 問題なし / ⚠️ 注意点あり / ❌ 危険
```

**❌ 危険** の場合はクローンせず、理由を説明してユーザーに判断を委ねる（`AskUserQuestion` で確認）。

### Phase 4: クローン

セキュリティチェックに問題がなければ:

1. `--dir` が指定されていればそのディレクトリに `cd` してからクローン
2. `git clone <URL>` を実行
3. クローン完了を確認

### Phase 5: 内容説明

README、ソースコード構造、依存関係の情報をもとに、以下を日本語で説明:

1. **概要**: リポジトリが何をするものか（1-2 文）
2. **主な機能**: 箇条書きで主要機能を列挙
3. **技術スタック**: 使用言語・フレームワーク・主要依存
4. **使い方**: セットアップ手順の要約（README ベース）
5. **アーキテクチャ**: ディレクトリ構造や設計の概要（分かる範囲で）
6. **特徴・差別化ポイント**: 類似ツールとの違い（README に記載があれば）

説明は技術者でなくても理解できる程度に噛み砕きつつ、技術的な正確さは保つ。

## 注意事項

- クローン前に必ずセキュリティチェックを完了すること（順序を入れ替えない）
- `gh` CLI が利用可能であること（`gh auth status` で認証済みであること）
- プライベートリポジトリの場合は `gh` の認証スコープに `repo` が必要
- クローン先に同名ディレクトリが既に存在する場合は `AskUserQuestion` で上書き確認する
