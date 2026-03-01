#!/usr/bin/env python3
"""TextGrad: LLMフィードバックによるテキスト反復最適化スクリプト.

claude -p を使い、評価→フィードバック→改善のループでテキストを最適化する。
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class OptimizationStep:
    step: int
    text_before: str
    feedback: str
    text_after: str


@dataclass
class OptimizationResult:
    original: str
    final: str
    criteria: str
    steps: list[OptimizationStep] = field(default_factory=list)


def call_llm(prompt: str) -> str:
    """claude -p でLLMを呼び出す."""
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "CLAUDECODE")}
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY が設定されていません", file=sys.stderr)
        sys.exit(1)
    env["ANTHROPIC_API_KEY"] = api_key

    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    if result.returncode != 0:
        print(f"LLM呼び出しエラー: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return result.stdout.strip()


def evaluate(text: str, criteria: str) -> str:
    """テキストを評価基準に基づいて評価し、フィードバックを返す."""
    prompt = (
        f"以下のテキストを評価基準に基づいて評価し、具体的な改善点を箇条書きで挙げてください。\n\n"
        f"## 評価基準\n{criteria}\n\n"
        f"## 対象テキスト\n```\n{text}\n```\n\n"
        f"## 出力形式\n"
        f"各改善点を `- [改善点]: [具体的な修正提案]` の形式で出力してください。"
    )
    return call_llm(prompt)


def apply_gradient(text: str, feedback: str, criteria: str) -> str:
    """フィードバック(勾配)を適用してテキストを改善する."""
    prompt = (
        f"以下のフィードバックに基づいて、テキストを改善してください。\n"
        f"改善後のテキストのみを出力してください（説明不要）。\n\n"
        f"## 評価基準\n{criteria}\n\n"
        f"## 現在のテキスト\n```\n{text}\n```\n\n"
        f"## フィードバック（改善すべき点）\n{feedback}\n\n"
        f"## 改善後のテキスト"
    )
    return call_llm(prompt)


def optimize(
    text: str,
    criteria: str,
    max_steps: int = 3,
    dry_run: bool = False,
    verbose: bool = False,
) -> OptimizationResult:
    """テキスト最適化のメインループ."""
    result = OptimizationResult(original=text, final=text, criteria=criteria)
    current = text

    for i in range(max_steps):
        if verbose:
            print(f"\n--- Step {i + 1}/{max_steps} ---", file=sys.stderr)

        feedback = evaluate(current, criteria)
        if verbose:
            print(f"Feedback: {feedback[:200]}...", file=sys.stderr)

        if dry_run:
            result.steps.append(
                OptimizationStep(step=i + 1, text_before=current, feedback=feedback, text_after=current)
            )
            continue

        improved = apply_gradient(current, feedback, criteria)

        result.steps.append(
            OptimizationStep(step=i + 1, text_before=current, feedback=feedback, text_after=improved)
        )
        current = improved

    result.final = current
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="TextGrad: LLMフィードバックによるテキスト反復最適化")
    parser.add_argument("--input", "-i", required=True, help="最適化対象のテキストファイル")
    parser.add_argument("--criteria", "-c", default="明確さ、具体性、簡潔さ、実行可能性", help="評価基準")
    parser.add_argument("--steps", "-s", type=int, default=3, help="最適化ステップ数")
    parser.add_argument("--output", "-o", help="出力ファイル（省略時は標準出力）")
    parser.add_argument("--json", action="store_true", help="全ステップをJSON形式で出力")
    parser.add_argument("--dry-run", action="store_true", help="評価のみ実行（テキスト変更なし）")
    parser.add_argument("--verbose", "-v", action="store_true", help="詳細出力")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} が見つかりません", file=sys.stderr)
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    result = optimize(text, args.criteria, args.steps, args.dry_run, args.verbose)

    if args.json:
        output = json.dumps(
            {
                "original": result.original,
                "final": result.final,
                "criteria": result.criteria,
                "steps": [
                    {
                        "step": s.step,
                        "feedback": s.feedback,
                        "text_before": s.text_before[:200],
                        "text_after": s.text_after[:200],
                    }
                    for s in result.steps
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    else:
        output = result.final

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"出力: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
