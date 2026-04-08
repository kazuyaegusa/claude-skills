# 複数スキルをプラグイン・コレクションとして配布する

> 関連するスキルをまとめて1つのリポジトリ・npm パッケージとして提供し、ワンコマンドでインストール可能にする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーが個別にスキルを探す手間を省き、ドメイン全体のワークフローをセットで導入できるため

## いつ使うのか

特定領域（例: セキュリティ、プロダクトマネジメント）の一連のスキルを提供したい時

## やり方

1. リポジトリに `skills/` ディレクトリを作成
2. 各スキルを `skills/{skill-name}/SKILL.md` として配置
3. `package.json` または `pyproject.toml` で依存関係を宣言
4. README に `npx pawmode` 等のインストールコマンドを記載
5. リリース後、awesome-claude-skills に登録

### 入力

- スキル群の対象ドメイン
- 各SKILL.mdファイル

### 出力

- パッケージ化されたリポジトリ
- インストールコマンド

## 使うツール・ライブラリ

- npm
- pip
- GitHub
- Claude Code plugin spec

## コード例

```
npx pawmode  # OpenPaw: 38スキルバンドルをインストール
```

## 前提知識

- Claude Codeの基本操作（スキルのインストール・実行方法）
- Markdown・YAML frontmatterの基礎知識
- GitHubリポジトリのクローン・PR操作
- Python/Node.js等のパッケージマネージャ利用経験（スキルによる）
