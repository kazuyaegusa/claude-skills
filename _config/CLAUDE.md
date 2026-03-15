# Claude CLI Global Notes

## 絶対ルール（違反厳禁）

### 嘘をつかない・知ったかぶりしない
- 確認していないことを事実として述べてはいけない
- UIのボタン、メニュー、設定項目について、実際に確認していないものを「ある」と言ってはいけない
- APIの挙動について確証がなければ「わからない」と言う
- 推測で回答する場合は必ず「推測ですが」「確証はありませんが」と明示する
- 「〜のはずです」「〜だと思います」で濁すのも禁止。知らないなら「知りません」と言う

### アプリケーションを勝手に操作しない
- Ghost OS等でブラウザや他のアプリを操作してはいけない
- ユーザーが明示的に「ブラウザで操作して」と指示した場合のみ許可

## 認証方針

- `claude -p` / `claude --resume` を子プロセスから実行するときは、`ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN` / `ANTHROPIC_BASE_URL` を環境から外す
- 理由: Claude CLI は API キーよりも Claude Code の subscription / `setup-token` 認証を優先して使わせたい
- Anthropic API を明示的に使いたい場合のみ、CLI ではなく API クライアント側で `ANTHROPIC_API_KEY` を利用する

## 運用メモ

- `claude -p` が `Credit balance is too low` を返したら、まず API キーが子プロセスへ漏れていないか確認する
- サブスク認証の切り替え確認は、`ANTHROPIC_API_KEY` を外した状態で `claude -p --output-format json` を最小プロンプトで実行して判定する
