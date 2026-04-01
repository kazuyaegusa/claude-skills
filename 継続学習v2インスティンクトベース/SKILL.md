# 継続学習v2（インスティンクトベース）

> セッションから抽出したパターンを「インスティンクト」として保存し、信頼度スコアリング・クラスタリング・スキル昇格を自動実行する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動でスキル作成すると知見が埋もれる。セッション終了時に自動抽出し、繰り返し出現するパターンをスキルに昇格させることで、学習ループを回せる

## いつ使うのか

プロジェクト固有のパターンを自動蓄積したい、チーム知見を形式知化したい、長期プロジェクトで学習ループを回したいとき

## やり方

1. セッション終了時に scripts/hooks/evaluate-session.js が LLM でパターン抽出 2. ~/.claude/instincts/<project>/ に JSON 保存（confidence/evidence/context 付き） 3. /instinct-status で一覧表示 4. /evolve で関連インスティンクトをクラスタリングしスキル候補生成 5. /instinct-export でチーム共有

### 入力

- セッション履歴（.claude/sessions/）
- LLM（claude -p）

### 出力

- ~/.claude/instincts/<project>/*.json（インスティンクト）
- スキル候補（/evolve 実行時）

## 使うツール・ライブラリ

- Node.js
- claude -p
- JSON

## コード例

```
// セッション終了時の自動抽出（hooks.json）
{
  "event": "Stop",
  "hooks": [{
    "type": "command",
    "command": "node scripts/hooks/evaluate-session.js"
  }]
}

// コマンド例
/instinct-status        // 学習済みパターン一覧
/instinct-import file.json // 他プロジェクトから取り込み
/evolve                 // クラスタリング→スキル化
/instinct-export        // チーム共有用エクスポート
```

## 前提知識

- Claude Code CLI v2.1.0以上のインストール
- Node.js環境（フックスクリプト実行用）
- Git（リポジトリクローン用）
- 対象言語の開発環境（TypeScript/Python/Go等）
- Claude Codeのサブスクリプション（トークン消費制限緩和のため推奨）
- AIエージェント・プロンプトエンジニアリングの基礎知識
