# feature flagによる内部機能の実行時ゲーティング

> コンパイル時feature flagを使い、内部専用機能を外部ビルドから完全に除去する

- 出典: https://github.com/Kuberwastaken/claurst
- 投稿者: Kuberwastaken
- カテゴリ: ui-ux

## なぜ使うのか

環境変数による実行時分岐ではコード自体は残るため、sourcemap経由で実装が漏洩する。コンパイル時の定数畳み込みとデッドコード削除により、外部ビルドにはコード自体が含まれなくなる

## いつ使うのか

内部専用機能と外部公開機能が同一コードベースに混在し、ビルド成果物を分離したい場合

## やり方

1. Bunの`feature()`関数や他バンドラーの`define`オプションでコンパイル時定数を定義
2. 内部機能を`if (feature('INTERNAL_FEATURE')) { ... }`でラップ
3. 外部ビルドでは`feature('INTERNAL_FEATURE')`が`false`に定数畳み込みされる
4. バンドラーのデッドコード削除が`if (false) { ... }`ブロックを完全除去
5. **ただしsourcemapを除外しないと無意味**（sourcemapには除去前のコードが残る）

### 入力

- feature flag定義（ビルド設定）
- 内部機能コード

### 出力

- 内部機能コードを含まない外部ビルド
- デッドコード削除による小さいバンドルサイズ

## 使うツール・ライブラリ

- Bun (feature())
- webpack (DefinePlugin)
- Rollup (@rollup/plugin-replace)
- esbuild (define)

## コード例

```
// Bun example
import { feature } from 'bun:bundle';

if (feature('KAIROS')) {
  // 内部専用の常時起動アシスタント機能
  // 外部ビルドではこのブロック全体がデッドコード削除される
}

// bun.config.ts
export default {
  define: {
    'feature("KAIROS")': 'false' // 外部ビルド用
  }
}
```

## 前提知識

- npm/JavaScriptパッケージングの基礎知識
- sourcemapの仕組み（mappings, sourcesContent）
- バンドラー（webpack/Rollup/Bun）の基本設定
- 著作権法の基本原則（表現と アイデアの区別）

## 根拠

> 「feature flagによるデッドコード削除に依存していたが、sourcemapには削除前のコードが残っていた」（投稿本文）
