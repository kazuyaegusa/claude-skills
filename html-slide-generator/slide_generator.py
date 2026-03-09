#!/usr/bin/env python3
"""HTML Slide Generator - トピックからスライドを自動生成"""

import sys
import argparse
import webbrowser
from pathlib import Path
from datetime import datetime

class SlideGenerator:
    def __init__(self):
        self.templates_dir = Path("templates")
        self.output_dir = Path("slides")
        self.output_dir.mkdir(exist_ok=True)
        self.static_dir = Path("static")
        
    def list_templates(self) -> list[str]:
        """利用可能なテンプレート一覧"""
        return [p.stem for p in self.templates_dir.glob("*.html")]
        
    def generate(self, topic: str, template: str = "engineer") -> Path:
        """トピックに基づいてスライドコンテンツを生成"""
        slides_content = self._generate_content(topic)
        template_html = self._load_template(template)
        
        # テンプレートにコンテンツを埋め込み
        final_html = self._embed_content(template_html, topic, slides_content, template)
        
        # 出力ファイル保存
        output_path = self.output_dir / f"{template}_output.html"
        output_path.write_text(final_html, encoding="utf-8")
        
        return output_path
    
    def _generate_content(self, topic: str) -> list[dict]:
        """トピックからスライドコンテンツを生成"""
        # 基本的な構成を生成
        return [
            {
                "title": topic,
                "body": f"{topic}に関する重要なポイントをまとめました。このプレゼンテーションでは、主要な概念、実装方法、期待される効果について詳しく説明していきます。"
            },
            {
                "title": "背景と課題",
                "body": f"{topic}の背景にある課題を分析します。現状の問題点、ユーザーからのフィードバック、市場の要求などを踏まえ、なぜこの取り組みが必要なのかを明確にします。"
            },
            {
                "title": "提案内容",
                "body": f"{topic}の具体的な内容と実装計画について解説します。技術的なアーキテクチャ、必要なリソース、タイムラインを含めた実行可能なプランを提示します。"
            },
            {
                "title": "実装詳細",
                "body": "段階的なロールアウト戦略を採用し、初期テスト、フィードバック収集、改善サイクルを繰り返しながら最適な形での本番展開を目指します。品質保証とリスク管理の方針も含みます。"
            },
            {
                "title": "期待される成果",
                "body": "KPI設定と測定方法を明確にし、継続的な改善プロセスを確立します。ユーザー満足度向上、処理速度改善、ビジネス価値の創出を目指します。"
            },
            {
                "title": "まとめと今後",
                "body": f"{topic}により実現される価値と今後の展望について総括します。チーム全体での成功に向けて、継続的なサポートと改善を行っていきます。"
            }
        ]
    
    def _load_template(self, template: str) -> str:
        """テンプレートHTMLを読み込み"""
        template_path = self.templates_dir / f"{template}.html"
        if not template_path.exists():
            template_path = self.templates_dir / "engineer.html"
        return template_path.read_text(encoding="utf-8")
    
    def _embed_content(self, template: str, topic: str, slides: list[dict], current_template: str) -> str:
        """テンプレートにコンテンツとスイッチャーを埋め込み"""
        # スライドHTML生成
        slides_html = ""
        for i, slide in enumerate(slides):
            slides_html += f"""
        <section class="slide" data-slide="{i+1}">
            <h2>{slide['title']}</h2>
            <div class="content">
                <p>{slide['body']}</p>
            </div>
        </section>
"""
        
        # スイッチャーJS読み込み
        switcher_js = ""
        if self.static_dir.exists():
            switcher_path = self.static_dir / "switcher.js"
            if switcher_path.exists():
                switcher_js = switcher_path.read_text(encoding="utf-8")
        
        # プレースホルダー置換
        result = template.replace("{{SLIDES_CONTENT}}", slides_html)
        result = result.replace("{{SWITCHER_JS}}", switcher_js)
        result = result.replace("{{TOPIC}}", topic)
        result = result.replace("{{DATE}}", datetime.now().strftime("%Y-%m-%d"))
        result = result.replace("{{CURRENT_TEMPLATE}}", current_template)
        
        return result

def main():
    parser = argparse.ArgumentParser(description="HTMLスライド生成ツール")
    parser.add_argument("topic", nargs="?", help="スライドのトピック")
    parser.add_argument("--template", default="engineer", help="使用するテンプレート")
    parser.add_argument("--list-templates", action="store_true", help="利用可能なテンプレート一覧")
    parser.add_argument("--no-open", action="store_true", help="ブラウザで開かない")
    
    args = parser.parse_args()
    
    generator = SlideGenerator()
    
    if args.list_templates:
        print("Available templates:")
        for tmpl in generator.list_templates():
            print(f"  - {tmpl}")
        return 0
    
    if not args.topic:
        print("Error: トピックを指定してください")
        parser.print_help()
        return 1
    
    # スライド生成
    print(f"Generating slides: {args.topic} (template: {args.template})")
    output_path = generator.generate(args.topic, args.template)
    
    # 結果表示
    content = output_path.read_text()
    slide_count = content.count('<section class="slide"')
    print(f"✓ Generated: {output_path} ({slide_count} slides)")
    
    # ブラウザで開く
    if not args.no_open:
        print("Opening in browser...")
        webbrowser.open(f"file://{output_path.absolute()}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())