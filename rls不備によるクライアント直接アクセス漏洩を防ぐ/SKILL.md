# RLS不備によるクライアント直接アクセス漏洩を防ぐ

> クライアント側からSupabaseを直接叩く場合、RLS (Row Level Security) ポリシーが全テーブルで正しく設定されているかを検証する

- 出典: https://x.com/shocolt/status/2035554524832911759
- 投稿者: 安藤奨馬 | シード特化VC 「TRUST SMITH & CAPITAL」代表
- カテゴリ: data-processing

## なぜ使うのか

RLSが未設定または不備があると、クライアントから直接DBを操作でき、他ユーザーのデータも取得できてしまう

## いつ使うのか

新規テーブルを作成する時、クライアントから直接Supabaseクエリを実行するコードを書く時、セキュリティ監査時

### 具体的な適用場面

- Next.js + Supabaseで社内CRMやダッシュボードを構築する時
- APIルートを追加する際のセキュリティレビュー
- 外部ユーザーのサインアップ機能を実装する時
- RLS (Row Level Security) ポリシーを設定・変更する時
- シード期スタートアップで最小限のセキュリティ体制を整える時

## やり方

1. Supabaseダッシュボード > Authentication > Policies で全テーブルを確認 2. 各テーブルに SELECT/INSERT/UPDATE/DELETE用のポリシーが存在するか確認 3. ポリシーが `auth.uid() = user_id` のような条件で自分のデータのみアクセス可能になっているか検証 4. テーブル追加時は必ずRLSを有効化 (`ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;`) 5. ポリシー例: `CREATE POLICY "Users can only access their own data" ON table_name FOR SELECT USING (auth.uid() = user_id);` 6. クライアント側で意図しないデータが取得できないか、開発環境で異なるユーザーIDでテストする

### 入力

- Supabaseテーブル定義
- クライアント側Supabaseクエリコード
- 認証済みユーザーのUID

### 出力

- RLSポリシー設定済みテーブル
- 他ユーザーデータへのアクセス不可を確認したテスト結果

## 使うツール・ライブラリ

- Supabase Dashboard
- PostgreSQL RLS
- @supabase/supabase-js

## コード例

```
ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can only access their own data" ON table_name FOR SELECT USING (auth.uid() = user_id);
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
