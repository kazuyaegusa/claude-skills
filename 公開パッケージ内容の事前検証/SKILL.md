# 公開パッケージ内容の事前検証

> npm公開前に`npm pack`でパッケージをローカル生成し、意図しないファイルが含まれていないか検証する

- 出典: https://github.com/Kuberwastaken/claurst
- 投稿者: Kuberwastaken
- カテゴリ: other

## なぜ使うのか

`.gitignore`と`.npmignore`は別物であり、開発時に問題なくても公開時に機密ファイルが含まれる可能性がある。実際のパッケージ内容を事前確認することで漏洩を防ぐ

## いつ使うのか

npmパッケージを公開する直前、特に初回公開時や`.npmignore`を変更した後

## やり方

1. `npm pack`を実行してtarballを生成
2. `tar -tzf <package-name>-<version>.tgz`で内容一覧を表示
3. `.map`ファイル、`.env`、認証情報、内部ドキュメント等が含まれていないか確認
4. 問題があれば`.npmignore`やpackage.jsonの`files`を修正
5. 再度`npm pack`して検証
6. 確認後`npm publish`

### 入力

- ビルド済みプロジェクト
- package.json
- .npmignore

### 出力

- パッケージ内容の確認済みtarball
- 機密情報漏洩リスクの検証

## 使うツール・ライブラリ

- npm
- tar

## コード例

```
# パッケージ内容を事前確認
npm pack
tar -tzf my-package-1.0.0.tgz | grep -E '\.(map|env|key)$'

# 問題なければ公開
npm publish my-package-1.0.0.tgz
```

## 前提知識

- npm/JavaScriptパッケージングの基礎知識
- sourcemapの仕組み（mappings, sourcesContent）
- バンドラー（webpack/Rollup/Bun）の基本設定
- 著作権法の基本原則（表現と アイデアの区別）

## 根拠

> 「`npm pack`でtarballを生成し、`tar -tzf`で内容を検証する」（一般的なベストプラクティス、投稿で暗に推奨）
