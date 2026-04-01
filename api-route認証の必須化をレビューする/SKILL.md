# API Route認証の必須化をレビューする

> Next.jsなどのAPI Routeで、認証チェックなしにSupabaseクエリを実行していないかを確認する

- 出典: https://x.com/shocolt/status/2035554524832911759
- 投稿者: 安藤奨馬 | シード特化VC 「TRUST SMITH & CAPITAL」代表
- カテゴリ: other

## なぜ使うのか

認証なしのAPIエンドポイントが存在すると、URLを知っているだけで誰でもDB情報を取得できてしまう

## いつ使うのか

新規APIエンドポイントを追加する時、既存APIのセキュリティレビュー時、PR承認前のチェックリスト実行時

### 具体的な適用場面

- Next.js + Supabaseで社内CRMやダッシュボードを構築する時
- APIルートを追加する際のセキュリティレビュー
- 外部ユーザーのサインアップ機能を実装する時
- RLS (Row Level Security) ポリシーを設定・変更する時
- シード期スタートアップで最小限のセキュリティ体制を整える時

## やり方

1. pages/api/ または app/api/ 配下の全ファイルをリストアップ 2. 各ファイル冒頭で session チェックや JWT 検証が実装されているか確認 3. 実装されていない場合、`const { data: { session } } = await supabase.auth.getSession()` と `if (!session) return res.status(401).json({ error: 'Unauthorized' })` を追加 4. PR時にAPI Routeの変更があれば認証チェックを必須レビュー項目にする

### 入力

- API Route実装ファイル (pages/api/*.ts, app/api/*/route.ts)
- Supabaseクライアント初期化コード

### 出力

- 認証チェック実装済みのAPIエンドポイント
- PRレビューチェックリスト

## 使うツール・ライブラリ

- @supabase/supabase-js
- Next.js API Routes

## コード例

```
const { data: { session } } = await supabase.auth.getSession()
if (!session) return res.status(401).json({ error: 'Unauthorized' })
```

## 前提知識

- Supabaseの基本的な使い方 (プロジェクト作成、テーブル作成、クライアントライブラリ利用)
- RLS (Row Level Security) の概念
- Next.js API Routesの基本構造
- JWT認証の仕組み
- PRレビューフローの運用経験

## 根拠

> ①API Routeに認証がなく、APIを叩くだけでDB情報が取れる

> ②クライアントから直接Supabaseを叩き、RLS不備で情報漏洩

> ③サインアップ可能で、外部ユーザーが内部情報へアクセス

> 気づかないうちに「誰でも見れてしまうDB」になってしまう

> シード期で自社CRM運用をする場合でも、この3点をレビューする仕組みは入れておいた方が良い
