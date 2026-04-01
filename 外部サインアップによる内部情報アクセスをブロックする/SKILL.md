# 外部サインアップによる内部情報アクセスをブロックする

> サインアップ機能が有効な場合、外部ユーザーが登録して内部情報にアクセスできないかを検証する

- 出典: https://x.com/shocolt/status/2035554524832911759
- 投稿者: 安藤奨馬 | シード特化VC 「TRUST SMITH & CAPITAL」代表
- カテゴリ: data-processing

## なぜ使うのか

誰でもサインアップ可能な状態で、RLSやロール管理が不十分だと、外部の第三者が登録後に社内CRMデータ等を閲覧できてしまう

## いつ使うのか

社内CRMやダッシュボードなど限定ユーザー向けシステムを構築する時、サインアップ機能を追加・変更する時、セキュリティ監査時

### 具体的な適用場面

- Next.js + Supabaseで社内CRMやダッシュボードを構築する時
- APIルートを追加する際のセキュリティレビュー
- 外部ユーザーのサインアップ機能を実装する時
- RLS (Row Level Security) ポリシーを設定・変更する時
- シード期スタートアップで最小限のセキュリティ体制を整える時

## やり方

1. Supabaseダッシュボード > Authentication > Providers でEmail/Password等のサインアップが有効か確認 2. 社内専用システムなら、サインアップを無効化するか、Email Domain制限 (例: `@company.com` のみ許可) を設定 3. サインアップ後のデフォルトロールが `authenticated` の場合、RLSポリシーで `user_id` や `role` による制限が正しく機能しているか確認 4. 必要ならカスタムクレーム (例: `is_internal: true`) をJWTに追加し、ポリシーで `(auth.jwt() ->> 'is_internal')::boolean = true` を条件にする 5. 外部テストアカウントで実際にサインアップし、内部データが見えないことを確認

### 入力

- Supabase Authenticationプロバイダー設定
- ユーザーロール・カスタムクレーム定義
- RLSポリシー

### 出力

- Email Domain制限またはサインアップ無効化設定
- 外部ユーザーが内部情報にアクセスできないことを確認したテスト結果

## 使うツール・ライブラリ

- Supabase Authentication
- PostgreSQL RLS
- JWT Custom Claims

## コード例

```
-- RLSポリシーでカスタムクレームを利用
CREATE POLICY "Only internal users" ON internal_table FOR SELECT USING ((auth.jwt() ->> 'is_internal')::boolean = true);
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
