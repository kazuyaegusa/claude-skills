# npx copilotkit initで既存プロジェクトに統合

> 既存のReact/Angularアプリに対してCopilotKitの依存インストール・Provider設定・エージェント接続を自動セットアップ

- 出典: https://github.com/CopilotKit/CopilotKit
- 投稿者: CopilotKit
- カテゴリ: agent-orchestration

## なぜ使うのか

手動でパッケージ・設定を追加するとミス・設定漏れが起きやすい。CLIで一括セットアップすることで即座に動作する状態を作れる

## いつ使うのか

既存アプリに最小コストでエージェント機能を追加したい場合

## やり方

1. プロジェクトルートで `npx copilotkit@latest init` を実行
2. フレームワーク検出→必要なパッケージインストール
3. CopilotKitProviderをルートコンポーネントに自動追加
4. エージェント接続の初期設定を生成
5. デプロイ可能な状態になる

### 入力

- 既存のReact/Angularプロジェクト

### 出力

- CopilotKitセットアップ完了済みプロジェクト
- 動作可能なProvider設定

## 使うツール・ライブラリ

- npx
- @copilotkit/react-core

## コード例

```
npx copilotkit@latest init
```

## 前提知識

- React/Angularの基礎知識
- Hooksの理解（useStateなど）
- エージェント・LLMアプリケーションの基本概念
- 非同期処理・ストリーミングの理解

## 根拠

> npx copilotkit@latest init ... **CopilotKit installed** – Core packages are fully set up in your app
