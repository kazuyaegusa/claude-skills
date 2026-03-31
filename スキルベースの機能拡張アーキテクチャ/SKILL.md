# スキルベースの機能拡張アーキテクチャ

> 新機能をコアコードベースにマージせず、Claude Codeスキル（`/add-whatsapp`等のコマンド）として配布し、ユーザーが各自のフォークに適用する

- 出典: https://github.com/qwibitai/nanoclaw
- 投稿者: qwibitai
- カテゴリ: claude-code-workflow

## なぜ使うのか

全ユーザーが使わない機能をコアに含めるとコードが肥大化し理解困難になる。ユーザーごとに必要な機能だけを適用すれば、シンプルかつカスタマイズ可能な状態を維持できる

## いつ使うのか

フレームワークの汎用性を高めたいが、全ユーザーに全機能を押し付けたくない時。コードベースのサイズを小さく保ちたい時

## やり方

1. 新機能をフォーク上のブランチで実装
2. PRを開き、メンテナーが`skill/{feature}`ブランチを作成
3. ユーザーはClaude Code内で`/add-{feature}`コマンドを実行
4. Claude Codeが該当スキルを読み込み、ユーザーのフォークに機能を適用
5. 結果として、ユーザーは自分に必要な機能だけを持つクリーンなコードベースを得る

### 入力

- スキル定義（SKILL.md）
- 機能実装ブランチ
- ユーザーのフォーク

### 出力

- ユーザーごとにカスタマイズされた機能セット
- コアは最小限のまま維持

## 使うツール・ライブラリ

- Claude Code CLI
- Claude Code Skills

## コード例

```
// スキル例: /add-telegram
// Claude Codeがskill/telegramブランチをマージし、
// Telegram対応コードをユーザーのフォークに追加
```

## 前提知識

- Claude Codeの基本的な使い方（スキル実行、自然言語でのコード変更依頼）
- Dockerまたはコンテナ技術の基礎知識（なぜファイルシステム分離がセキュリティに有効か）
- Node.js基礎（このプロジェクトはNode.js 20+で実装）
- Claude Agent SDKの概要（Anthropic公式のAgent実行ハーネス）
- フォーク＆ブランチベースのGitワークフロー

## 根拠

> NanoClaw provides that same core functionality, but in a codebase small enough to understand: one process and a handful of files. Claude agents run in their own Linux containers with filesystem isolation, not merely behind permission checks.

> Skills over features. Instead of adding features (e.g. support for Telegram) to the codebase, contributors submit claude code skills like /add-telegram that transform your fork.

> AI-native: No installation wizard; Claude Code guides setup. No monitoring dashboard; ask Claude what's happening. No debugging tools; describe the problem and Claude fixes it.
