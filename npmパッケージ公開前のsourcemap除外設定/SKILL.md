# npmパッケージ公開前のsourcemap除外設定

> npm公開時に`.map`ファイルをパッケージから除外し、ソースコードの意図しない漏洩を防ぐ

- 出典: https://github.com/Kuberwastaken/claurst
- 投稿者: Kuberwastaken
- カテゴリ: other

## なぜ使うのか

sourcemapの`sourcesContent`配列には元のソースコード全体が文字列として埋め込まれており、これが公開されると全ての内部実装・コメント・機密情報が閲覧可能になる

## いつ使うのか

TypeScript/JavaScriptプロジェクトをnpmレジストリに公開する全てのケース、特にプロプライエタリなコードを含む場合

## やり方

1. `.npmignore`ファイルに`*.map`パターンを追加
2. または`package.json`の`files`フィールドで明示的に`.map`を除外
3. バンドラー（Bun/webpack/Rollup）の設定で`sourcemap: false`を本番ビルドに指定
4. `npm pack`で実際のパッケージ内容を事前確認
5. 公開前に`tar -tzf <package>.tgz`で`.map`ファイルが含まれていないことを検証

### 入力

- ビルド済みのnpmパッケージ
- バンドラー設定ファイル（bun.config.ts, webpack.config.js等）
- .npmignoreまたはpackage.jsonのfilesフィールド

### 出力

- sourcemapを含まないnpmパッケージ
- ソースコード漏洩リスクの排除

## 使うツール・ライブラリ

- npm
- Bun
- webpack
- Rollup
- tar

## コード例

```
// .npmignore
*.map

// または package.json
{
  "files": ["dist/**/*.js", "!dist/**/*.map"]
}

// bun.config.ts
export default {
  sourcemap: process.env.NODE_ENV === 'production' ? false : 'inline'
}
```

## 前提知識

- npm/JavaScriptパッケージングの基礎知識
- sourcemapの仕組み（mappings, sourcesContent）
- バンドラー（webpack/Rollup/Bun）の基本設定
- 著作権法の基本原則（表現と アイデアの区別）

## 根拠

> 「`npm pack`でtarballを生成し、`tar -tzf`で内容を検証する」（一般的なベストプラクティス、投稿で暗に推奨）
