---
name: quality-harness
description: 任意のPythonプロジェクトに品質ハーネス（eval評価・実行隔離・CI/CD・Git hooks）を一括セットアップするスキル。
user_invocable: true
---

# Quality Harness — プロジェクト品質基盤の自動セットアップ

任意の Python プロジェクトに対して、以下の品質基盤を一括で導入する:

- **評価ハーネス（eval）**: YAML でテストケースを定義し、grader で自動採点・スコア記録
- **実行ハーネス（runner）**: 実行ごとに workspace を隔離し、ログ・成果物・再現コマンドを自動保存
- **CI/CD**: GitHub Actions で lint / typecheck / test を自動実行
- **Git hooks**: pre-commit（fmt/lint）、commit-msg（形式検証）、pre-push（テスト）
- **統一コマンド**: `make ci` で全チェック一発実行

## 使い方

```
/quality-harness              → カレントディレクトリのプロジェクトにセットアップ
/quality-harness ./my-project → 指定パスのプロジェクトにセットアップ
```

## 実行手順

### Phase 0: 現状監査（読み取り専用）

1. `Glob` と `Read` でプロジェクト構造を確認:
   - `pyproject.toml` or `setup.py` or `setup.cfg` — パッケージ名・依存・Python バージョンを検出
   - `src/` or プロジェクトルート — ソースコードのパッケージ構造を検出
   - `tests/` — 既存テスト構造を確認
   - `Makefile` / `justfile` — 既存コマンド体系を確認
   - `.github/workflows/` — 既存 CI 確認
   - `.pre-commit-config.yaml` — 既存 hooks 確認
   - `.claude/` — 既存 Claude Code 設定確認

2. 検出結果をもとに以下の変数を確定:
   - `PROJECT_NAME`: パッケージ名（pyproject.toml の `[project].name`）
   - `SRC_DIR`: ソースディレクトリ（`src/{PROJECT_NAME}/` or `{PROJECT_NAME}/`）
   - `PYTHON_VERSION`: 必要な Python バージョン
   - `PACKAGE_MANAGER`: `uv` / `pip` / `poetry`（pyproject.toml, uv.lock, poetry.lock 等から判定。uv.lock があれば `uv`）
   - `EXISTING_TOOLS`: 既に存在するツール一覧

3. **既に存在するものは上書きしない**。不足分のみ追加する。衝突がある場合はユーザーに確認する。

### Phase 1: 評価ハーネス（eval）の導入

以下のファイルを生成する。`{SRC_DIR}` はPhase 0で検出したパスに置換する。

#### `{SRC_DIR}/harness/__init__.py`

```python
"""品質ハーネス: eval（評価）+ runner（実行隔離）の基盤"""
```

#### `{SRC_DIR}/harness/eval.py`

```python
"""eval ハーネス: スキル/エージェント/関数の品質を定量的に評価する仕組み

eval ケース（入力 + 期待条件）を YAML で定義し、
grader（採点器）で自動採点し、スコアを記録・比較する。
"""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class EvalCase:
    """1つの評価ケース"""

    name: str
    input_data: dict[str, Any]
    expected: dict[str, Any]


@dataclass
class GradeResult:
    """採点結果"""

    case_name: str
    score: float  # 0.0 ~ 1.0
    passed: bool
    details: str


class BaseGrader(ABC):
    """grader の基底クラス（採点ルールを定義する）"""

    @abstractmethod
    def grade(self, output: dict[str, Any], expected: dict[str, Any]) -> GradeResult:
        """出力を採点する"""
        ...


class ExactMatchGrader(BaseGrader):
    """完全一致 grader: 出力が期待値と完全に一致するか判定する"""

    def grade(self, output: dict[str, Any], expected: dict[str, Any]) -> GradeResult:
        passed = output == expected
        return GradeResult(
            case_name="",
            score=1.0 if passed else 0.0,
            passed=passed,
            details="完全一致" if passed else "不一致あり",
        )


class ContainsGrader(BaseGrader):
    """部分一致 grader: 出力に期待値の文字列が含まれるか判定する"""

    def grade(self, output: dict[str, Any], expected: dict[str, Any]) -> GradeResult:
        target = expected.get("contains", "")
        output_str = json.dumps(output, ensure_ascii=False)
        passed = str(target) in output_str
        return GradeResult(
            case_name="",
            score=1.0 if passed else 0.0,
            passed=passed,
            details=f"'{target}' を含む" if passed else f"'{target}' が見つからない",
        )


class KeyExistsGrader(BaseGrader):
    """キー存在 grader: 出力に指定されたキーが全て存在するか判定する"""

    def grade(self, output: dict[str, Any], expected: dict[str, Any]) -> GradeResult:
        required_keys = expected.get("required_keys", [])
        if not isinstance(required_keys, list):
            required_keys = [required_keys]

        missing = [k for k in required_keys if k not in output]
        passed = len(missing) == 0
        score = 1.0 - (len(missing) / max(len(required_keys), 1))

        return GradeResult(
            case_name="",
            score=score,
            passed=passed,
            details=f"不足キー: {missing}" if missing else "全キー存在",
        )


class SchemaGrader(BaseGrader):
    """スキーマ grader: 出力が期待された型構造を持つか判定する"""

    def grade(self, output: dict[str, Any], expected: dict[str, Any]) -> GradeResult:
        schema = expected.get("schema", {})
        errors: list[str] = []
        for key, expected_type in schema.items():
            if key not in output:
                errors.append(f"キー '{key}' が存在しない")
            elif expected_type == "str" and not isinstance(output[key], str):
                errors.append(f"'{key}' が str でない（実際: {type(output[key]).__name__}）")
            elif expected_type == "int" and not isinstance(output[key], int):
                errors.append(f"'{key}' が int でない（実際: {type(output[key]).__name__}）")
            elif expected_type == "list" and not isinstance(output[key], list):
                errors.append(f"'{key}' が list でない（実際: {type(output[key]).__name__}）")
            elif expected_type == "dict" and not isinstance(output[key], dict):
                errors.append(f"'{key}' が dict でない（実際: {type(output[key]).__name__}）")

        total = max(len(schema), 1)
        passed = len(errors) == 0
        score = 1.0 - (len(errors) / total)

        return GradeResult(
            case_name="",
            score=score,
            passed=passed,
            details="; ".join(errors) if errors else "スキーマ準拠",
        )


class EvalRunner:
    """eval 実行器: ケースを読み込み、grader で採点する"""

    def load_cases(self, path: Path) -> list[EvalCase]:
        """YAML からケースを読み込む"""
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        cases: list[EvalCase] = []
        for case_data in data.get("cases", []):
            cases.append(
                EvalCase(
                    name=case_data["name"],
                    input_data=case_data.get("input", {}),
                    expected=case_data.get("expected", {}),
                )
            )
        return cases

    def run_grader(
        self,
        cases: list[EvalCase],
        grader: BaseGrader,
        executor: Any = None,
    ) -> list[GradeResult]:
        """全ケースを grader で採点する

        Args:
            cases: 評価ケースのリスト
            grader: 採点器
            executor: 実行関数（callable）。指定時は executor(input_data) の結果を採点する。
                      未指定時は input_data をそのまま出力として扱う（テスト用）。
        """
        results: list[GradeResult] = []
        for case in cases:
            if executor is not None:
                output = executor(case.input_data)
            else:
                output = case.input_data
            result = grader.grade(output, case.expected)
            result.case_name = case.name
            results.append(result)
        return results

    def save_results(self, results: list[GradeResult], output_path: Path) -> None:
        """結果を JSON ファイルに保存する"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        data = [
            {
                "case_name": r.case_name,
                "score": r.score,
                "passed": r.passed,
                "details": r.details,
            }
            for r in results
        ]
        output_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def summary(self, results: list[GradeResult]) -> dict[str, Any]:
        """結果のサマリーを返す"""
        total = len(results)
        passed = sum(1 for r in results if r.passed)
        avg_score = sum(r.score for r in results) / max(total, 1)
        return {
            "total": total,
            "passed": passed,
            "failed": total - passed,
            "avg_score": round(avg_score, 3),
        }
```

#### `{SRC_DIR}/harness/runner.py`

```python
"""実行ハーネス: 実行を workspace で隔離し、ログと成果物を保存する

runs/<timestamp>_<run_id>/ にワークスペースを作り、
実行ログ・入出力・成果物・再現コマンドを自動保存する。
"""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


@dataclass
class RunConfig:
    """実行設定"""

    base_dir: Path = field(default_factory=lambda: Path("runs"))
    run_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class RunResult:
    """実行結果"""

    run_id: str
    workspace: Path
    success: bool
    log_path: Path
    reproduce_command: str


class HarnessRunner:
    """実行ハーネスのメインクラス

    実行をワークスペースで隔離し、ログと成果物を保存する。
    失敗時には再現コマンドを出力する。
    """

    def create_workspace(self, config: RunConfig) -> tuple[Path, str]:
        """隔離されたワークスペースを作成する

        Returns:
            (workspace_path, run_id) のタプル
        """
        run_id = config.run_id or uuid.uuid4().hex[:12]
        timestamp = datetime.now(tz=UTC).strftime("%Y%m%d_%H%M%S")
        workspace = config.base_dir / f"{timestamp}_{run_id}"
        workspace.mkdir(parents=True, exist_ok=True)

        (workspace / "logs").mkdir(exist_ok=True)
        (workspace / "artifacts").mkdir(exist_ok=True)

        meta = {
            "run_id": run_id,
            "timestamp": timestamp,
            "created_at": datetime.now(tz=UTC).isoformat(),
            **config.metadata,
        }
        (workspace / "meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        return workspace, run_id

    def save_log(self, workspace: Path, name: str, content: str) -> Path:
        """実行ログを保存する"""
        log_path = workspace / "logs" / f"{name}.log"
        log_path.write_text(content, encoding="utf-8")
        return log_path

    def save_artifact(self, workspace: Path, name: str, data: bytes) -> Path:
        """成果物を保存する"""
        artifact_path = workspace / "artifacts" / name
        artifact_path.write_bytes(data)
        return artifact_path

    def generate_reproduce_command(self, config: RunConfig, command: str) -> str:
        """再現コマンドを生成する"""
        run_id = config.run_id or "unknown"
        return f"# 再現コマンド (run_id={run_id})\n{command}"
```

### Phase 2: テストの導入

#### `tests/unit/test_harness_eval.py`

```python
"""eval ハーネスのテスト"""

from __future__ import annotations

from pathlib import Path

import pytest

from {PROJECT_NAME}.harness.eval import (
    EvalCase,
    EvalRunner,
    ExactMatchGrader,
    ContainsGrader,
    KeyExistsGrader,
    SchemaGrader,
    GradeResult,
)

SAMPLE_YAML = Path(__file__).resolve().parents[2] / "evals" / "cases" / "sample.yaml"


@pytest.fixture
def runner() -> EvalRunner:
    return EvalRunner()


class TestExactMatchGrader:
    def test_pass(self) -> None:
        result = ExactMatchGrader().grade({"a": 1}, {"a": 1})
        assert result.passed is True
        assert result.score == 1.0

    def test_fail(self) -> None:
        result = ExactMatchGrader().grade({"a": 1}, {"a": 2})
        assert result.passed is False
        assert result.score == 0.0


class TestContainsGrader:
    def test_pass(self) -> None:
        result = ContainsGrader().grade({"text": "hello world"}, {"contains": "hello"})
        assert result.passed is True

    def test_fail(self) -> None:
        result = ContainsGrader().grade({"text": "hello"}, {"contains": "xyz"})
        assert result.passed is False


class TestKeyExistsGrader:
    def test_pass(self) -> None:
        result = KeyExistsGrader().grade(
            {"a": 1, "b": 2}, {"required_keys": ["a", "b"]}
        )
        assert result.passed is True
        assert result.score == 1.0

    def test_partial(self) -> None:
        result = KeyExistsGrader().grade({"a": 1}, {"required_keys": ["a", "b"]})
        assert result.passed is False
        assert result.score == 0.5


class TestSchemaGrader:
    def test_pass(self) -> None:
        result = SchemaGrader().grade(
            {"name": "test", "count": 1},
            {"schema": {"name": "str", "count": "int"}},
        )
        assert result.passed is True

    def test_fail(self) -> None:
        result = SchemaGrader().grade(
            {"name": 123},
            {"schema": {"name": "str"}},
        )
        assert result.passed is False


class TestEvalRunner:
    def test_load_cases(self, runner: EvalRunner) -> None:
        cases = runner.load_cases(SAMPLE_YAML)
        assert len(cases) >= 1
        assert cases[0].name != ""

    def test_run_grader(self, runner: EvalRunner) -> None:
        cases = [EvalCase(name="t1", input_data={"a": 1}, expected={"a": 1})]
        results = runner.run_grader(cases, ExactMatchGrader())
        assert len(results) == 1
        assert results[0].passed is True

    def test_run_grader_with_executor(self, runner: EvalRunner) -> None:
        cases = [EvalCase(name="t1", input_data={"x": 1}, expected={"x": 2})]
        results = runner.run_grader(
            cases, ExactMatchGrader(), executor=lambda d: {"x": d["x"] + 1}
        )
        assert results[0].passed is True

    def test_save_results(self, runner: EvalRunner, tmp_path: Path) -> None:
        results = [GradeResult(case_name="t1", score=1.0, passed=True, details="OK")]
        path = tmp_path / "results.json"
        runner.save_results(results, path)
        assert path.exists()

    def test_summary(self, runner: EvalRunner) -> None:
        results = [
            GradeResult(case_name="t1", score=1.0, passed=True, details=""),
            GradeResult(case_name="t2", score=0.0, passed=False, details=""),
        ]
        s = runner.summary(results)
        assert s["total"] == 2
        assert s["passed"] == 1
        assert s["avg_score"] == 0.5
```

#### `tests/unit/test_harness_runner.py`

```python
"""実行ハーネスのテスト"""

from __future__ import annotations

from pathlib import Path

import pytest

from {PROJECT_NAME}.harness.runner import HarnessRunner, RunConfig


@pytest.fixture
def harness() -> HarnessRunner:
    return HarnessRunner()


@pytest.fixture
def tmp_config(tmp_path: Path) -> RunConfig:
    return RunConfig(base_dir=tmp_path, run_id="test-run-001")


class TestCreateWorkspace:
    def test_creates_directory(self, harness: HarnessRunner, tmp_config: RunConfig) -> None:
        workspace, _ = harness.create_workspace(tmp_config)
        assert workspace.exists() and workspace.is_dir()

    def test_creates_subdirs(self, harness: HarnessRunner, tmp_config: RunConfig) -> None:
        workspace, _ = harness.create_workspace(tmp_config)
        assert (workspace / "logs").is_dir()
        assert (workspace / "artifacts").is_dir()

    def test_creates_meta(self, harness: HarnessRunner, tmp_config: RunConfig) -> None:
        workspace, _ = harness.create_workspace(tmp_config)
        assert (workspace / "meta.json").exists()

    def test_returns_run_id(self, harness: HarnessRunner, tmp_config: RunConfig) -> None:
        _, run_id = harness.create_workspace(tmp_config)
        assert run_id == "test-run-001"

    def test_auto_generates_run_id(self, harness: HarnessRunner, tmp_path: Path) -> None:
        config = RunConfig(base_dir=tmp_path)
        _, run_id = harness.create_workspace(config)
        assert len(run_id) == 12


class TestSaveLog:
    def test_saves(self, harness: HarnessRunner, tmp_config: RunConfig) -> None:
        workspace, _ = harness.create_workspace(tmp_config)
        log_path = harness.save_log(workspace, "test", "ログ内容")
        assert log_path.exists()
        assert log_path.read_text(encoding="utf-8") == "ログ内容"


class TestSaveArtifact:
    def test_saves(self, harness: HarnessRunner, tmp_config: RunConfig) -> None:
        workspace, _ = harness.create_workspace(tmp_config)
        path = harness.save_artifact(workspace, "out.bin", b"data")
        assert path.exists()
        assert path.read_bytes() == b"data"


class TestReproduceCommand:
    def test_generates(self, harness: HarnessRunner, tmp_config: RunConfig) -> None:
        cmd = harness.generate_reproduce_command(tmp_config, "make test")
        assert "test-run-001" in cmd
        assert "make test" in cmd
```

#### `evals/cases/sample.yaml`

```yaml
# eval ケースのサンプル: grader の動作確認用
name: sample_grader_test
description: grader の基本動作を確認するテストケース

cases:
  - name: exact_match_pass
    input:
      purpose: "テスト"
    expected:
      purpose: "テスト"

  - name: exact_match_fail
    input:
      purpose: "テスト"
    expected:
      purpose: "別の値"

  - name: key_exists_check
    input:
      purpose: "テスト"
      target_users: "全員"
    expected:
      required_keys:
        - purpose
        - target_users
```

### Phase 3: CI/CD の導入

#### `.github/workflows/ci.yml`（存在しない場合のみ生成）

プロジェクトの `PACKAGE_MANAGER` に合わせて `uv run` / `poetry run` / 直接実行を切り替える。
以下は `uv` の場合のテンプレート:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
      - uses: actions/setup-python@v5
        with:
          python-version: "{PYTHON_VERSION}"
      - run: uv sync --extra dev
      - run: uv run ruff check src/ tests/
      - run: uv run ruff format --check src/ tests/

  typecheck:
    name: Type Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
      - uses: actions/setup-python@v5
        with:
          python-version: "{PYTHON_VERSION}"
      - run: uv sync --extra dev
      - run: uv run mypy src/

  test:
    name: Test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
      - uses: actions/setup-python@v5
        with:
          python-version: "{PYTHON_VERSION}"
      - run: uv sync --extra dev
      - run: uv run pytest
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: coverage-report
          path: htmlcov/
          retention-days: 14
```

#### `Makefile`（存在しない場合のみ生成）

```makefile
.PHONY: fmt lint typecheck test test-unit test-integration eval ci clean install-hooks

fmt:
	{RUN_PREFIX} ruff format src/ tests/

lint:
	{RUN_PREFIX} ruff check src/ tests/

typecheck:
	{RUN_PREFIX} mypy src/

test:
	{RUN_PREFIX} pytest

test-unit:
	{RUN_PREFIX} pytest tests/unit/

test-integration:
	{RUN_PREFIX} pytest tests/integration/

eval:
	{RUN_PREFIX} pytest tests/unit/test_harness_eval.py -v

ci: lint typecheck test

install-hooks:
	{RUN_PREFIX} pre-commit install

clean:
	rm -rf .mypy_cache .pytest_cache .ruff_cache htmlcov .coverage
```

`{RUN_PREFIX}` は `PACKAGE_MANAGER` に応じて `uv run` / `poetry run` / 空文字に置換する。

### Phase 4: Git hooks の導入

#### `.pre-commit-config.yaml`（存在しない場合のみ生成）

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.0
    hooks:
      - id: ruff-format
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: [--maxkb=500]
```

#### `scripts/check_commit_msg.py`（存在しない場合のみ生成）

```python
"""コミットメッセージの形式を検証する: [カテゴリ] 内容"""

from __future__ import annotations

import re
import sys

CATEGORIES = [
    "feat", "fix", "refactor", "test", "docs",
    "chore", "ci", "style", "perf", "build",
]

PATTERN = re.compile(r"^\[(" + "|".join(CATEGORIES) + r")\] .{3,}")


def main() -> int:
    msg_file = sys.argv[1]
    with open(msg_file, encoding="utf-8") as f:
        msg = f.readline().strip()

    if PATTERN.match(msg):
        return 0

    print(f"エラー: コミットメッセージが形式に合いません: {msg}")
    print(f"形式: [カテゴリ] 内容")
    print(f"カテゴリ: {', '.join(CATEGORIES)}")
    print(f"例: [feat] ユーザー認証機能を追加")
    return 1


if __name__ == "__main__":
    sys.exit(main())
```

### Phase 5: pyproject.toml の更新

既存の `pyproject.toml` に以下を**マージ**する（上書きではない）:

**依存追加（`[project.optional-dependencies].dev`）**:
- `pytest>=8.0`
- `pytest-cov>=6.0`
- `ruff>=0.9`
- `mypy>=1.14`
- `pre-commit>=4.0`
- `types-pyyaml>=6.0`（PyYAML の型スタブ）

**本体依存追加（`[project].dependencies`）**:
- `pyyaml>=6.0`（eval ハーネスが YAML を読むため）
- `pydantic>=2.0`（既存になければ）

**設定追加**:
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
addopts = "--cov={PROJECT_NAME} --cov-report=term-missing --cov-report=html"

[tool.mypy]
strict = true

[tool.ruff]
target-version = "py312"
line-length = 100
```

### Phase 6: 検証

1. `make ci`（または `{RUN_PREFIX} pytest`）を実行してテストが通ることを確認
2. 失敗がある場合は修正する
3. 結果をユーザーに報告する

## 注意事項

- **既存ファイルを壊さない**: 既に存在するファイル（Makefile, CI, pre-commit 等）がある場合は、不足分のみ追記する。衝突がある場合はユーザーに確認する。
- **PyYAML が必要**: eval ハーネスは YAML を読むため、`pyyaml` が依存に必要。自動で追加する。
- **`runs/` ディレクトリ**: 実行ハーネスが生成する `runs/` ディレクトリは `.gitignore` に追加する。
- **テンプレート変数**: `{PROJECT_NAME}`, `{SRC_DIR}`, `{PYTHON_VERSION}`, `{RUN_PREFIX}` は Phase 0 の検出結果で置換する。
- **言語**: コメント・docstring は日本語で記述する。
