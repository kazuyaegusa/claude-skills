---
name: html-arch-visualizer
description: プロジェクトのアーキテクチャをSVGベースのインタラクティブなHTMLダイアグラムとして可視化するスキル。
user_invocable: true
---

# HTML Architecture Visualizer

プロジェクトのシステム構成・データフロー・依存関係を、単一HTMLファイルのSVGダイアグラムとして生成する。

## 起動条件

以下のいずれかに該当する場合に使用する:
- `/visualize-arch` コマンドが実行された
- 「アーキテクチャを可視化」「構成図を作って」「システム図を生成」等の依頼

## 処理フロー（4フェーズ）

### Phase 1: プロジェクト分析

コード・設定・ドキュメントを読み、以下を特定する:

1. **コンポーネント**: サービス・モジュール・レイヤーの一覧
2. **データフロー**: コンポーネント間のデータ・API呼び出しの方向
3. **依存関係**: 外部サービス・DB・ライブラリ
4. **技術スタック**: 言語・フレームワーク・インフラ

```bash
# 調査コマンド例
ls -la && cat package.json 2>/dev/null || cat pyproject.toml 2>/dev/null
find . -name "*.md" -maxdepth 2 | head -5
```

### Phase 2: ダイアグラム設計

分析結果をもとに以下を設計する:

- **viewBox**: コンポーネント数に応じて決定（例: `0 0 1200 700`）
- **レイアウト**: 左から右（入力→処理→出力）または上から下（フロント→バック→DB）
- **色割り当て**:
  - データソース・外部入力: `#3b82f6`（青）
  - 処理・コアロジック: `#8b5cf6`（紫）
  - DB・ストレージ: `#6b7280`（グレー）
  - 外部サービス: `#f59e0b`（オレンジ）
  - UI・フロントエンド: `#10b981`（緑）

### Phase 3: HTML生成

単一HTMLファイルを生成する。外部依存なし・ダーク/ライトテーマ対応・レスポンシブ。

#### SVG基本構造テンプレート

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Architecture Diagram</title>
<style>
  :root {
    --bg: #ffffff;
    --text: #1f2937;
    --card-bg: #f9fafb;
    --border: #e5e7eb;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #111827;
      --text: #f9fafb;
      --card-bg: #1f2937;
      --border: #374151;
    }
  }
  body { margin: 0; padding: 16px; background: var(--bg); color: var(--text); font-family: sans-serif; }
  .diagram-container { width: 100%; min-height: 500px; }
  svg { width: 100%; height: auto; }
  .theme-toggle { position: fixed; top: 12px; right: 12px; cursor: pointer; padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border); background: var(--card-bg); color: var(--text); }
</style>
</head>
<body>
<button class="theme-toggle" onclick="toggleTheme()">テーマ切替</button>
<div class="diagram-container">
<svg viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- 矢印マーカー -->
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#6b7280"/>
    </marker>
    <marker id="arrow-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6"/>
    </marker>
  </defs>

  <!-- 背景 -->
  <rect width="1200" height="700" fill="#111827" rx="8"/>

  <!-- コンポーネント例（生成時は実際の構造に合わせて変更） -->
  <!-- 角丸矩形: rx=12 で統一 -->
  <g id="component-frontend">
    <rect x="50" y="100" width="180" height="80" rx="12" fill="#10b981" opacity="0.9"/>
    <text x="140" y="135" text-anchor="middle" fill="white" font-size="13" font-weight="bold">Frontend</text>
    <text x="140" y="155" text-anchor="middle" fill="white" font-size="9" opacity="0.85">React / Next.js</text>
  </g>

  <!-- 接続線 -->
  <line x1="230" y1="140" x2="320" y2="140" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="275" y="132" text-anchor="middle" fill="#9ca3af" font-size="10">HTTP/REST</text>

</svg>
</div>

<!-- 補足情報テーブル（任意） -->
<div style="overflow-x:auto; margin-top:24px;">
  <table style="border-collapse:collapse; width:100%; font-size:14px;">
    <thead>
      <tr style="background:var(--card-bg);">
        <th style="padding:8px 12px; border:1px solid var(--border); text-align:left;">コンポーネント</th>
        <th style="padding:8px 12px; border:1px solid var(--border); text-align:left;">役割</th>
        <th style="padding:8px 12px; border:1px solid var(--border); text-align:left;">技術</th>
      </tr>
    </thead>
    <tbody>
      <!-- 行を追加 -->
    </tbody>
  </table>
</div>

<script>
function toggleTheme() {
  const root = document.documentElement;
  const isDark = root.style.getPropertyValue('--bg') === '#111827';
  root.style.setProperty('--bg', isDark ? '#ffffff' : '#111827');
  root.style.setProperty('--text', isDark ? '#1f2937' : '#f9fafb');
  root.style.setProperty('--card-bg', isDark ? '#f9fafb' : '#1f2937');
  root.style.setProperty('--border', isDark ? '#e5e7eb' : '#374151');
}
</script>
</body>
</html>
```

#### デザインルール

- SVGはインライン埋め込み（外部ファイル参照禁止）
- `preserveAspectRatio="xMidYMid meet"` で画面幅に追従
- コンポーネントは角丸矩形 `rx=10〜12`
- フォントサイズ: タイトル12-13px、説明8-9px、ラベル10-11px
- 矢印は `<marker>` で定義し、`marker-end` で参照
- ダイアグラム背景は `#111827`（ダークグレー）固定で視認性を確保
- テーブルは `overflow-x:auto` 付きHTMLで表現（SVG内に無理に収めない）

### Phase 4: 検証

生成したHTMLファイルをブラウザで開いて確認する:

```bash
open ./docs/architecture.html
# または
open <指定パス>
```

表示崩れがあれば SVG の viewBox・座標を調整して再生成する。

## 出力先

- 指定パスがある場合: そのパスにHTMLを生成
- 指定なし: `./docs/architecture.html`（`docs/` ディレクトリがなければ作成）

## 注意事項

- コンポーネントが多い場合（10以上）はグルーピング（`<g>` タグ）でまとめる
- 矢印が交差しすぎる場合はレイアウトを縦型に変更する
- 実際のプロジェクト構造を読んでから生成する（推測で書かない）
