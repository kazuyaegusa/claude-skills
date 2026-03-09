---
title: HTML Slide Generator
description: トピックからHTMLスライドを自動生成し、職種別テンプレートの切り替えが可能
author: Claude
version: 1.0.0
license: MIT
tags: [slides, presentation, html, generator, template]
created: 2026-03-09
updated: 2026-03-09
---

# HTML Slide Generator

トピックを指定するだけでHTMLベースのプレゼンテーションスライドを自動生成します。
エンジニア・PM・人事など職種別のテンプレートを用意し、生成後もワンクリックで切り替え可能。

## 機能

- トピックからスライドコンテンツを自動生成
- 職種別テンプレート（Engineer/PM/HR）
- ブラウザ内でのテンプレート即時切り替え
- レスポンシブデザイン対応
- 外部依存なしのスタンドアロンHTML出力

## 使い方

### 基本コマンド

```bash
# スライド生成（デフォルトはengineerテンプレート）
python slide_generator.py "新機能リリース"

# テンプレート指定
python slide_generator.py "新機能リリース" --template pm

# 利用可能なテンプレート確認
python slide_generator.py --list-templates
```

### Claude Codeコマンド化

`.claude/commands/slides.md` を作成:

```markdown
# Slide Generator

トピック: {{topic}}
テンプレート: {{template:engineer}}

スライドを生成してください。
```

使用例:
```bash
/slides 新機能リリース
```

## 必要パッケージ

標準ライブラリのみ使用（追加インストール不要）

## ファイル構成

```
.
├── slide_generator.py    # メインジェネレーター
├── templates/            # HTMLテンプレート
│   ├── engineer.html    # エンジニア向け（技術的・ダーク）
│   ├── pm.html         # PM向け（ビジネス・明るい）
│   └── hr.html         # 人事向け（親しみやすい・カラフル）
├── static/              # 静的リソース
│   └── switcher.js     # テンプレート切り替えJS
└── slides/             # 出力ディレクトリ
```

## カスタマイズ

### 新しいテンプレート追加

1. `templates/` に新しいHTMLファイルを作成
2. 必須プレースホルダーを含める:
   - `{{SLIDES_CONTENT}}` - スライド本体
   - `{{SWITCHER_JS}}` - 切り替え機能JS
   - `{{TOPIC}}` - トピック名
   - `{{DATE}}` - 生成日
   - `{{CURRENT_TEMPLATE}}` - 現在のテンプレート名

### コンテンツ生成ロジック変更

`slide_generator.py` の `_generate_content()` メソッドを編集。
AI APIを使用する場合は環境変数で設定:

```python
api_key = os.getenv('OPENAI_API_KEY')
```

## 出力例

生成されたHTMLファイルには以下が含まれます:
- タイトルスライド
- 背景と課題
- 主要機能の説明
- 技術的詳細
- ロードマップ
- 期待される成果

各スライドは職種に応じたデザインで表示され、
ブラウザ上部のボタンでいつでも切り替え可能です。