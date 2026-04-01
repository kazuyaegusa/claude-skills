# 単一リポジトリ・マルチスキル構成の採用

> 1つのGitHubリポジトリに複数のスキルを `skills/` ディレクトリ配下に格納し、それぞれ独立したSKILL.mdを持たせる

- 出典: https://github.com/JimLiu/baoyu-skills
- 投稿者: JimLiu
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキルごとにリポジトリを分けるとメンテナンスコストが増大し、共通の依存関係やドキュメントが重複する。単一リポジトリにまとめることで、一括管理・一括更新が可能になり、READMEも統一できる

## いつ使うのか

3つ以上のスキルを開発・公開する場合、または関連スキル群をパッケージとして配布したい場合

## やり方

1. リポジトリルートに `skills/` ディレクトリを作成
2. 各スキルを `skills/baoyu-スキル名/SKILL.md` として配置
3. ルートの `plugin-marketplace.json` で全スキルを1つのプラグインとして定義
4. README.mdで全スキルのドキュメントを統合的に記述

### 入力

- 複数のスキル定義(SKILL.md)
- 共通の依存関係(package.json等)

### 出力

- 単一リポジトリで管理される複数スキル
- 統一されたREADMEとバージョン管理

## 使うツール・ライブラリ

- Git
- GitHub

## 前提知識

- Claude Codeの基本的な使い方とスキルの概念
- GitHubリポジトリの作成・管理
- JSON形式の理解(plugin-marketplace.json作成のため)
- 環境変数と.envファイルの扱い方
- Bashスクリプトの基本(ClawHub公開スクリプト利用時)
