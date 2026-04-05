# クリーンルーム再実装によるライセンスリスク回避

> 漏洩したソースコードから2段階プロセスで仕様を抽出し、オリジナルコードを参照せずに再実装することで著作権侵害を回避する

- 出典: https://github.com/Kuberwastaken/claurst
- 投稿者: Kuberwastaken
- カテゴリ: agent-orchestration

## なぜ使うのか

ソースコードの「表現」は著作権で保護されるが「アイデア・動作」は保護されない。仕様書を介在させることで、動作は再現しつつ表現は独立させ、Baker v. Selden判例の原則に従う

## いつ使うのか

漏洩または公開されたプロプライエタリコードの機能を合法的に再現したい場合

## やり方

1. **Phase 1（仕様抽出）**: 元コードを分析し、動作・アーキテクチャ・データフロー・API契約を網羅的に文書化。コード自体はコピーしない
2. **Phase 2（再実装）**: 別の実装者が仕様書のみを参照し、元のTypeScriptコードを一切見ずにRust等で実装
3. 実装者は仕様書に記載された動作を再現するが、表現（変数名、ロジックの書き方、ファイル構成）は独自に設計
4. 法的根拠: Phoenix Technologies v. IBM (1984) のBIOSクリーンルーム判例

### 入力

- 元ソースコード（仕様抽出フェーズのみ）
- 動作仕様書

### 出力

- 動作互換だが表現が独立した再実装コード
- 著作権侵害リスクの最小化

## 使うツール・ライブラリ

- AI（仕様抽出・実装支援）
- 異なるプログラミング言語（TypeScript→Rust等）

## コード例

```
# Phase 1: 仕様抽出（AI Agent A）
元コード → 分析 → spec/architecture.md, spec/tool-contracts.md

# Phase 2: 再実装（AI Agent B、元コードを見ない）
spec/*.md → 実装 → src-rust/main.rs （独自の表現）
```

## 前提知識

- npm/JavaScriptパッケージングの基礎知識
- sourcemapの仕組み（mappings, sourcesContent）
- バンドラー（webpack/Rollup/Bun）の基本設定
- 著作権法の基本原則（表現と アイデアの区別）

## 根拠

> 「クリーンルーム再実装: Phase 1で仕様抽出、Phase 2で元コードを参照せず実装。Phoenix Technologies v. IBM (1984) 判例に基づく」（GitHub README）
