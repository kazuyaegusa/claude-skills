#!/usr/bin/env python3
"""
evaluate_skill_quality.py - SkillForge v5.0 Quality Scorecard

スキルの品質を6次元で自動評価し、Master Supervisor向けのレポートを生成する。

Exit codes:
  0  - APPROVED (score ≥75, all dimension minimums met)
  1  - Error (cannot evaluate)
  10 - REVISE (score 60-74 or 1 dimension below minimum)
  11 - REJECT (score <60 or multiple critical failures)

Usage:
  python evaluate_skill_quality.py ~/.claude/skills/my-skill/
  python evaluate_skill_quality.py ~/.claude/skills/my-skill/ --summary
  python evaluate_skill_quality.py --batch ~/.claude/skills/ --output report.json
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


@dataclass
class DimensionResult:
    score: int
    max: int
    minimum: int
    issues: list[str] = field(default_factory=list)

    @property
    def passed_minimum(self) -> bool:
        return self.score >= self.minimum


@dataclass
class EvaluationResult:
    skill: str
    skill_path: str
    total_score: int
    max_score: int = 100
    dimensions: dict = field(default_factory=dict)
    verdict: str = ""
    gates_passed: bool = False
    recommendations: list[str] = field(default_factory=list)
    critical_failures: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "skill": self.skill,
            "skill_path": self.skill_path,
            "total_score": self.total_score,
            "max_score": self.max_score,
            "dimensions": {k: asdict(v) for k, v in self.dimensions.items()},
            "verdict": self.verdict,
            "gates_passed": self.gates_passed,
            "recommendations": self.recommendations,
            "critical_failures": self.critical_failures,
        }


def read_skill_md(skill_dir: Path) -> Optional[str]:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None
    return skill_md.read_text(encoding="utf-8")


def evaluate_structural_quality(content: str, skill_dir: Path) -> DimensionResult:
    """Structural Quality (15 pts): frontmatter validity, naming, format compliance."""
    score = 0
    issues = []

    # Frontmatter uses only allowed properties (3pts)
    allowed = {"name", "description", "license", "allowed-tools", "metadata"}
    fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        keys = re.findall(r"^(\w[\w-]*):", fm_text, re.MULTILINE)
        invalid = [k for k in keys if k not in allowed]
        if not invalid:
            score += 3
        else:
            issues.append(f"Invalid frontmatter properties: {invalid}")
    else:
        issues.append("No frontmatter found")

    # Name is hyphen-case, ≤64 chars (2pts)
    name_match = re.search(r"^name:\s*(.+)$", content, re.MULTILINE)
    if name_match:
        name = name_match.group(1).strip().strip('"')
        if re.match(r"^[a-z][a-z0-9-]*$", name) and len(name) <= 64:
            score += 2
        else:
            if not re.match(r"^[a-z][a-z0-9-]*$", name):
                issues.append(f"Name '{name}' is not hyphen-case")
            if len(name) > 64:
                issues.append(f"Name exceeds 64 chars: {len(name)}")
    else:
        issues.append("No 'name' field in frontmatter")

    # Description ≤1024 chars, no angle brackets (2pts)
    desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', content, re.MULTILINE)
    if desc_match:
        desc = desc_match.group(1)
        if len(desc) <= 1024 and "<" not in desc and ">" not in desc:
            score += 2
        else:
            if len(desc) > 1024:
                issues.append(f"Description exceeds 1024 chars: {len(desc)}")
            if "<" in desc or ">" in desc:
                issues.append("Description contains angle brackets")
    else:
        issues.append("No 'description' field in frontmatter")

    # Directory structure follows convention (4pts)
    dir_score = 0
    if (skill_dir / "SKILL.md").exists():
        dir_score += 2
    if (skill_dir / "scripts").exists() or (skill_dir / "references").exists():
        dir_score += 1
    if len(list(skill_dir.iterdir())) > 1:
        dir_score += 1
    score += dir_score

    # Sections complete, no placeholder text (4pts)
    placeholders = ["TODO", "PLACEHOLDER", "FILL IN", "YOUR_", "TBD", "..."]
    has_placeholders = any(p in content.upper() for p in placeholders)
    has_quick_start = "## Quick Start" in content or "# Quick Start" in content
    has_verification = "## Verification" in content or "## Anti-Patterns" in content
    section_score = 0
    if not has_placeholders:
        section_score += 2
    else:
        issues.append("Contains placeholder text")
    if has_quick_start:
        section_score += 1
    else:
        issues.append("Missing Quick Start section")
    if has_verification:
        section_score += 1
    else:
        issues.append("Missing Verification or Anti-Patterns section")
    score += section_score

    return DimensionResult(score=score, max=15, minimum=10, issues=issues)


def evaluate_functional_completeness(content: str) -> DimensionResult:
    """Functional Completeness (20 pts): triggers, phases, verification, commands."""
    score = 0
    issues = []

    # 3-5 distinct trigger phrases (4pts)
    trigger_patterns = [
        r"^- `.*`.*\n",
        r"^\- [A-Z`].*\n",
    ]
    triggers_section = re.search(r"## Triggers?(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if triggers_section:
        trigger_items = re.findall(r"^- .+", triggers_section.group(1), re.MULTILINE)
        count = len(trigger_items)
        if 3 <= count <= 10:
            score += 4
        elif count >= 1:
            score += 2
            issues.append(f"Only {count} trigger phrases (recommend 3-5)")
        else:
            issues.append("No trigger phrases found")
    else:
        issues.append("No Triggers section found")

    # All phases clearly defined (4pts)
    phase_count = len(re.findall(r"Phase \d+:", content, re.IGNORECASE))
    if phase_count >= 3:
        score += 4
    elif phase_count >= 1:
        score += 2
        issues.append(f"Only {phase_count} phases defined (recommend 3+)")
    else:
        issues.append("No phases defined")

    # Verification criteria are measurable (4pts)
    verification_section = re.search(
        r"## Verification.*?(?=\n##|\Z)", content, re.DOTALL | re.IGNORECASE
    )
    if verification_section:
        checklist_items = re.findall(r"- \[[ x]\]", verification_section.group())
        if len(checklist_items) >= 3:
            score += 4
        elif len(checklist_items) >= 1:
            score += 2
            issues.append("Verification checklist has fewer than 3 items")
        else:
            issues.append("Verification section has no checklist items")
    else:
        issues.append("No Verification section found")

    # Commands section present (4pts)
    if "## Commands" in content or "| Command" in content:
        score += 4
    else:
        issues.append("No Commands section found")

    # Anti-patterns documented (4pts)
    if "## Anti-Patterns" in content or "Anti-Pattern" in content:
        anti_items = re.findall(r"\| .+ \| .+ \| .+ \|", content)
        if len(anti_items) >= 3:
            score += 4
        elif len(anti_items) >= 1:
            score += 2
            issues.append("Anti-patterns table has fewer than 3 entries")
        else:
            score += 2
            issues.append("Anti-patterns section exists but lacks table format")
    else:
        issues.append("No Anti-Patterns section found")

    return DimensionResult(score=score, max=20, minimum=14, issues=issues)


def evaluate_agentic_capability(content: str, skill_dir: Path) -> DimensionResult:
    """Agentic Capability (15 pts): automation, self-verification, autonomous operation."""
    score = 0
    issues = []

    scripts_dir = skill_dir / "scripts"

    # Scripts present when artifact-producing (5pts)
    is_artifact_producing = any(
        keyword in content.lower()
        for keyword in ["generate", "create", "produce", "output", "artifact", "write"]
    )
    has_scripts = scripts_dir.exists() and any(
        f.suffix == ".py" for f in scripts_dir.iterdir()
    ) if scripts_dir.exists() else False

    if has_scripts:
        score += 5
    elif is_artifact_producing:
        issues.append("Artifact-producing skill lacks scripts/ directory")
    else:
        score += 3  # not artifact-producing, scripts optional

    # Scripts include self-verification (5pts)
    if has_scripts:
        script_content = ""
        for script in scripts_dir.glob("*.py"):
            script_content += script.read_text(encoding="utf-8", errors="ignore")
        if "verify" in script_content.lower() or "validate" in script_content.lower():
            score += 5
        else:
            issues.append("Scripts lack self-verification logic")
            score += 2
    else:
        # Check if SKILL.md references verification
        if "self-verif" in content.lower() or "verify" in content.lower():
            score += 3
        else:
            issues.append("No self-verification mentioned")

    # Can run autonomously (overnight test) (5pts)
    autonomy_signals = [
        "autonomous", "automatically", "without human", "overnight",
        "agentic", "self-", "automated"
    ]
    autonomy_count = sum(1 for s in autonomy_signals if s in content.lower())
    if autonomy_count >= 3:
        score += 5
    elif autonomy_count >= 1:
        score += 3
        issues.append("Limited autonomous operation signals")
    else:
        issues.append("No autonomous operation capability documented")

    return DimensionResult(score=score, max=15, minimum=10, issues=issues)


def evaluate_timelessness(content: str) -> DimensionResult:
    """Timelessness (20 pts): evolution score, extension points, obsolescence resistance."""
    score = 0
    issues = []

    # Timelessness score ≥7 mentioned (8pts)
    ts_match = re.search(r"timelessness[^0-9]*(\d+)\s*/\s*10", content, re.IGNORECASE)
    if ts_match:
        ts = int(ts_match.group(1))
        if ts >= 7:
            score += 8
        elif ts >= 5:
            score += 4
            issues.append(f"Timelessness score {ts}/10 below required 7")
        else:
            issues.append(f"Timelessness score {ts}/10 too low")
    else:
        # Check for timelessness mentions even without explicit score
        if "timeless" in content.lower() or "evolution" in content.lower():
            score += 5
            issues.append("Timelessness mentioned but no explicit score (add score ≥7)")
        else:
            issues.append("No timelessness evaluation found")

    # ≥2 extension points documented (4pts)
    ext_section = re.search(r"## Extension Points?(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if ext_section:
        ext_items = re.findall(r"^\d+\.", ext_section.group(1), re.MULTILINE)
        if len(ext_items) >= 2:
            score += 4
        else:
            score += 2
            issues.append(f"Only {len(ext_items)} extension points (need ≥2)")
    else:
        issues.append("No Extension Points section")

    # Obsolescence triggers identified (4pts)
    obsolescence_signals = ["obsolete", "obsolescence", "deprecat", "future", "temporal"]
    if any(s in content.lower() for s in obsolescence_signals):
        score += 4
    else:
        issues.append("No obsolescence/future-proofing discussion")

    # Principles-based, not implementation-locked (4pts)
    version_pins = re.findall(r"v\d+\.\d+\.\d+|==\s*\d|\d+\.\d+\.\d+", content)
    if len(version_pins) <= 2:
        score += 4
    else:
        score += 2
        issues.append(f"Possible implementation lock: {len(version_pins)} version pins found")

    return DimensionResult(score=score, max=20, minimum=14, issues=issues)


def evaluate_documentation_quality(content: str) -> DimensionResult:
    """Documentation Quality (15 pts): clarity, examples, anti-patterns, WHY."""
    score = 0
    issues = []

    # Quick Start section present and useful (3pts)
    qs_match = re.search(r"## Quick Start(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if qs_match:
        qs_content = qs_match.group(1)
        has_code = "```" in qs_content
        has_examples = len(qs_content.strip()) > 100
        if has_code and has_examples:
            score += 3
        elif has_examples:
            score += 2
            issues.append("Quick Start lacks code examples")
        else:
            score += 1
            issues.append("Quick Start section is too brief")
    else:
        issues.append("No Quick Start section")

    # Concrete examples for all triggers (3pts)
    code_blocks = re.findall(r"```.*?```", content, re.DOTALL)
    trigger_examples = [b for b in code_blocks if "→" in b or "->" in b]
    if len(trigger_examples) >= 2:
        score += 3
    elif len(trigger_examples) >= 1:
        score += 2
        issues.append("Only 1 set of trigger examples")
    else:
        issues.append("No trigger examples with expected outputs (→)")

    # Anti-patterns with WHY (3pts)
    ap_section = re.search(r"## Anti-Patterns?(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if ap_section:
        ap_content = ap_section.group(1)
        if "why" in ap_content.lower() or "| Why |" in ap_content or "instead" in ap_content.lower():
            score += 3
        else:
            score += 2
            issues.append("Anti-patterns lack WHY explanation")
    else:
        issues.append("No Anti-Patterns section")

    # Deep Dive sections for complex topics (3pts)
    deep_dives = re.findall(r"<details>", content, re.IGNORECASE)
    if len(deep_dives) >= 2:
        score += 3
    elif len(deep_dives) >= 1:
        score += 2
        issues.append("Only 1 Deep Dive section (recommend 2+)")
    else:
        # Check for ## Deep Dive alternative
        if "Deep Dive" in content:
            score += 2
        else:
            issues.append("No Deep Dive sections for complex topics")

    # Changelog maintained (3pts)
    if "## Changelog" in content:
        changelog_entries = re.findall(r"### v\d+\.\d+", content)
        if len(changelog_entries) >= 2:
            score += 3
        else:
            score += 2
            issues.append("Changelog has only 1 entry")
    else:
        issues.append("No Changelog section")

    return DimensionResult(score=score, max=15, minimum=10, issues=issues)


def evaluate_ecosystem_fit(content: str, skill_dir: Path) -> DimensionResult:
    """Ecosystem Fit (15 pts): uniqueness, integration, discoverability."""
    score = 0
    issues = []

    # Confirmed unique (no >80% overlap) — heuristic check (5pts)
    # We check if Phase 0 triage or duplicate check is mentioned
    if "phase 0" in content.lower() or "triage" in content.lower() or "duplicate" in content.lower():
        score += 5
    else:
        # Check if the skill has a clear unique purpose
        if "unique" in content.lower() or "distinct" in content.lower():
            score += 3
            issues.append("Uniqueness asserted but no triage evidence documented")
        else:
            issues.append("No duplicate/uniqueness check documented")

    # Related skills listed (5pts)
    if "## Related Skills" in content or "Related Skill" in content:
        related = re.findall(r"\| .+ \| .+ \|", content)
        if len(related) >= 2:
            score += 5
        else:
            score += 3
            issues.append("Related Skills section has fewer than 2 entries")
    else:
        issues.append("No Related Skills section")

    # Discoverability: description is index-ready (5pts)
    desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', content, re.MULTILINE)
    if desc_match:
        desc = desc_match.group(1)
        word_count = len(desc.split())
        has_use_when = "use when" in desc.lower() or "when" in desc.lower()
        if word_count >= 20 and has_use_when:
            score += 5
        elif word_count >= 10:
            score += 3
            issues.append("Description could be more discoverable (add 'use when' context)")
        else:
            score += 1
            issues.append(f"Description too short ({word_count} words)")
    else:
        issues.append("No description for discoverability check")

    return DimensionResult(score=score, max=15, minimum=10, issues=issues)


def determine_verdict(result: EvaluationResult) -> tuple[str, bool, list[str]]:
    """Determine APPROVED/REVISE/REJECT verdict and critical failures."""
    critical_failures = []
    failed_minimums = [
        dim for dim, r in result.dimensions.items() if not r.passed_minimum
    ]

    if failed_minimums:
        for dim in failed_minimums:
            r = result.dimensions[dim]
            critical_failures.append(
                f"{dim}: {r.score}/{r.max} (minimum {r.minimum})"
            )

    if result.total_score >= 75 and not failed_minimums:
        return "APPROVED", True, critical_failures
    elif result.total_score >= 60 and len(failed_minimums) <= 1:
        return "REVISE", False, critical_failures
    else:
        return "REJECT", False, critical_failures


def evaluate_skill(skill_dir: Path) -> EvaluationResult:
    """Run full quality evaluation on a skill directory."""
    content = read_skill_md(skill_dir)
    if content is None:
        print(f"Error: SKILL.md not found in {skill_dir}", file=sys.stderr)
        sys.exit(1)

    skill_name = skill_dir.name

    dimensions = {
        "structural_quality": evaluate_structural_quality(content, skill_dir),
        "functional_completeness": evaluate_functional_completeness(content),
        "agentic_capability": evaluate_agentic_capability(content, skill_dir),
        "timelessness": evaluate_timelessness(content),
        "documentation_quality": evaluate_documentation_quality(content),
        "ecosystem_fit": evaluate_ecosystem_fit(content, skill_dir),
    }

    total_score = sum(d.score for d in dimensions.values())
    all_issues = [issue for d in dimensions.values() for issue in d.issues]
    recommendations = sorted(set(all_issues))[:10]  # top 10 unique

    result = EvaluationResult(
        skill=skill_name,
        skill_path=str(skill_dir),
        total_score=total_score,
        dimensions=dimensions,
        recommendations=recommendations,
    )

    verdict, gates_passed, critical_failures = determine_verdict(result)
    result.verdict = verdict
    result.gates_passed = gates_passed
    result.critical_failures = critical_failures

    return result


def print_summary(result: EvaluationResult) -> None:
    """Print human-readable summary."""
    print(f"\n{'='*60}")
    print(f"  SkillForge Quality Scorecard: {result.skill}")
    print(f"{'='*60}")
    print(f"  Total Score: {result.total_score}/100")
    print(f"  Verdict:     {result.verdict}")
    print(f"  Gates:       {'PASSED' if result.gates_passed else 'FAILED'}")
    print(f"\n  Dimensions:")
    for dim, r in result.dimensions.items():
        status = "OK" if r.passed_minimum else "FAIL"
        print(f"    [{status}] {dim:30s} {r.score:2d}/{r.max}")

    if result.critical_failures:
        print(f"\n  Critical Failures:")
        for cf in result.critical_failures:
            print(f"    - {cf}")

    if result.recommendations:
        print(f"\n  Top Recommendations:")
        for i, rec in enumerate(result.recommendations[:5], 1):
            print(f"    {i}. {rec}")
    print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="SkillForge v5.0 - 6-Dimensional Quality Evaluator"
    )
    parser.add_argument("skill_path", nargs="?", help="Path to skill directory")
    parser.add_argument("--summary", action="store_true", help="Print human-readable summary")
    parser.add_argument(
        "--compare", metavar="PATH", help="Compare with another skill version"
    )
    parser.add_argument(
        "--batch", metavar="DIR", help="Batch evaluate all skills in directory"
    )
    parser.add_argument("--output", metavar="FILE", help="Write JSON output to file")
    args = parser.parse_args()

    if args.batch:
        batch_dir = Path(args.batch)
        results = []
        for skill_dir in sorted(batch_dir.iterdir()):
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                try:
                    r = evaluate_skill(skill_dir)
                    results.append(r.to_dict())
                except Exception as e:
                    results.append({"skill": skill_dir.name, "error": str(e)})
        output = json.dumps(results, indent=2, ensure_ascii=False)
        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
            print(f"Batch report written to {args.output}")
        else:
            print(output)
        return

    if not args.skill_path:
        parser.print_help()
        sys.exit(1)

    skill_dir = Path(args.skill_path)
    if not skill_dir.exists():
        print(f"Error: {skill_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    result = evaluate_skill(skill_dir)

    if args.compare:
        compare_dir = Path(args.compare)
        compare_result = evaluate_skill(compare_dir)
        comparison = {
            "baseline": result.to_dict(),
            "comparison": compare_result.to_dict(),
            "delta": compare_result.total_score - result.total_score,
        }
        output = json.dumps(comparison, indent=2, ensure_ascii=False)
    else:
        output = json.dumps(result.to_dict(), indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Report written to {args.output}")

    if args.summary or not args.output:
        print_summary(result)

    if not args.summary and not args.output:
        print(output)

    # Exit codes for CI integration
    if result.verdict == "APPROVED":
        sys.exit(0)
    elif result.verdict == "REVISE":
        sys.exit(10)
    else:
        sys.exit(11)


if __name__ == "__main__":
    main()
