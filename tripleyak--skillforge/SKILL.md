---
name: skillforge
description: "Intelligent skill router and creator. Analyzes ANY input to recommend existing skills, improve them, or create new ones. Uses deep iterative analysis with 11 thinking models, regression questioning, evolution lens, multi-agent synthesis panel, and Master Supervisor final review. Phase 0 triage ensures you never duplicate existing functionality."
license: MIT
metadata:
  version: 5.0.0
  model: claude-sonnet-4-6
  subagent_model: claude-sonnet-4-6
  domains: [meta-skill, automation, skill-creation, orchestration, agentic, routing]
  type: orchestrator
  inputs: [any-input, user-goal, domain-hints]
  outputs: [SKILL.md, references/, scripts/, SKILL_SPEC.md, recommendations]
---

# SkillForge 5.0 - Intelligent Skill Router & Creator

Analyzes ANY input to find, improve, or create the right skill.
v5.0 adds a **Master Supervisor Agent** for final quality control and a **6-dimensional Quality Scorecard** for rigorous evaluation.

---

## Quick Start

**Any input works.** SkillForge will intelligently route to the right action:

```
SkillForge: create a skill for automated code review
→ Creates new skill (after checking no duplicates exist)

help me debug this TypeError
→ Recommends ErrorExplainer skill (existing)

improve the testgen skill to handle React components better
→ Enters improvement mode for TestGen

do I have a skill for database migrations?
→ Recommends DBSchema, database-migration skills
```

---

## Triggers

### Creation Triggers
- `SkillForge: {goal}` - Full autonomous skill creation
- `create skill` - Natural language activation
- `design skill for {purpose}` - Purpose-first creation
- `ultimate skill` - Emphasize maximum quality
- `skillforge --plan-only` - Generate specification without execution

### Routing Triggers
- `{any input}` - Analyzes and routes automatically
- `do I have a skill for` - Searches existing skills
- `which skill` / `what skill` - Recommends matching skills
- `improve {skill-name} skill` - Enters improvement mode
- `help me with` / `I need to` - Detects task and routes

| Input | Output | Quality Gate |
|-------|--------|--------------|
| Any input | Triage → Route → Action | Phase 0 analysis |
| Explicit create | New skill | Master Supervisor approval |
| Task/question | Skill recommendation | Match confidence ≥60% |

---

## Process Overview

```
ANY USER INPUT
(prompt, error, code, URL, question, task request)
    │
    ▼
┌─────────────────────────────────────────────────────┐
│ Phase 0: SKILL TRIAGE                               │
│ • Classify input type (create/improve/question/task)│
│ • Scan 250+ skills in ecosystem                     │
│ • Match against existing skills with confidence %   │
│ • Route to: USE | IMPROVE | CREATE | COMPOSE        │
├─────────────────────────────────────────────────────┤
│         ↓ USE_EXISTING    ↓ IMPROVE      ↓ CREATE   │
│      [Recommend]      [Load & Enhance] [Continue]   │
└─────────────────────────────────────────────────────┘
    │ (if CREATE_NEW or IMPROVE_EXISTING)
    ▼
┌─────────────────────────────────────────────────────┐
│ Phase 1: DEEP ANALYSIS                              │
│ • Expand requirements (explicit, implicit, unknown) │
│ • Apply 11 thinking models + Automation Lens        │
│ • Question until no new insights (3 empty rounds)   │
│ • Identify automation/script opportunities          │
├─────────────────────────────────────────────────────┤
│ Phase 2: SPECIFICATION                              │
│ • Generate XML spec with all decisions + WHY        │
│ • Include scripts section (if applicable)           │
│ • Validate timelessness score ≥ 7                   │
│ ★ QUALITY GATE: Spec must pass before Phase 3      │
├─────────────────────────────────────────────────────┤
│ Phase 3: GENERATION                                 │
│ • Write SKILL.md with fresh context                 │
│ • Generate references/, assets/, and scripts/       │
├─────────────────────────────────────────────────────┤
│ Phase 4: SYNTHESIS PANEL                            │
│ • 3-4 agents review independently                   │
│ • All agents must approve (unanimous)               │
│ • If rejected → loop back with feedback             │
│ ★ QUALITY GATE: Unanimity required before Phase 5  │
├─────────────────────────────────────────────────────┤
│ Phase 5: MASTER SUPERVISOR REVIEW [NEW in v5.0]    │
│ • Single independent supervisor agent               │
│ • 6-dimensional Quality Scorecard (100 points)      │
│ • Final APPROVE / REVISE / REJECT decision          │
│ • Overrides panel if critical issues found          │
│ ★ QUALITY GATE: Score ≥75 + all dimension gates    │
└─────────────────────────────────────────────────────┘
    │
    ▼
Production-Ready Agentic Skill
```

**Key principles:**
- **Phase 0 prevents duplicates** - Always checks existing skills first
- **Phase 5 ensures final quality** - Master Supervisor has ultimate authority
- Evolution/timelessness is the core lens (score ≥ 7 required)
- Every decision includes WHY
- Quality gates enforce standards between phases
- Scripts enable self-verification and agentic operation

---

## Commands

| Command | Action |
|---------|--------|
| `SkillForge: {goal}` | Full autonomous execution |
| `SkillForge --plan-only {goal}` | Generate specification only |
| `SkillForge --quick {goal}` | Reduced depth (not recommended) |
| `SkillForge --triage {input}` | Run Phase 0 triage only |
| `SkillForge --improve {skill}` | Enter improvement mode for existing skill |
| `SkillForge --evaluate {path}` | Run Quality Scorecard on existing skill |

---

## Phase 5: Master Supervisor Review [NEW in v5.0]

The Master Supervisor is an independent agent with authority over the entire creation pipeline.

### Role

| Dimension | Responsibility |
|-----------|----------------|
| **Independence** | No prior involvement in Phases 1-4 |
| **Authority** | Can APPROVE, REVISE, or REJECT regardless of panel result |
| **Scope** | Reviews all phases, not just the final output |
| **Focus** | Quality gaps the panel may have normalized over iterations |

### 6-Dimensional Quality Scorecard

| Dimension | Weight | Description | Minimum |
|-----------|--------|-------------|---------|
| **Structural Quality** | 15 pts | Frontmatter validity, naming, format compliance | 10/15 |
| **Functional Completeness** | 20 pts | Triggers, phases, verification, commands | 14/20 |
| **Agentic Capability** | 15 pts | Automation, self-verification, autonomous operation | 10/15 |
| **Timelessness** | 20 pts | Evolution score, extension points, obsolescence resistance | 14/20 |
| **Documentation Quality** | 15 pts | Clarity, examples, anti-patterns, WHY documented | 10/15 |
| **Ecosystem Fit** | 15 pts | Uniqueness, integration, discoverability | 10/15 |
| **Total** | **100 pts** | | **≥75** |

### Scoring Details

**Structural Quality (15 pts)**

| Criteria | Points |
|----------|--------|
| Frontmatter uses only allowed properties | 3 |
| Name is hyphen-case, ≤64 chars | 2 |
| Description ≤1024 chars, no `<>` | 2 |
| Directory structure follows convention | 4 |
| Sections complete, no placeholder text | 4 |

**Functional Completeness (20 pts)**

| Criteria | Points |
|----------|--------|
| 3-5 distinct trigger phrases | 4 |
| All phases clearly defined | 4 |
| Verification criteria are measurable | 4 |
| Commands section present | 4 |
| Anti-patterns documented | 4 |

**Agentic Capability (15 pts)**

| Criteria | Points |
|----------|--------|
| Scripts present when artifact-producing | 5 |
| Scripts include self-verification | 5 |
| Can run autonomously (overnight test) | 5 |

**Timelessness (20 pts)**

| Criteria | Points |
|----------|--------|
| Phase 1 timelessness score ≥7 | 8 |
| ≥2 extension points documented | 4 |
| Obsolescence triggers identified | 4 |
| Principles-based, not implementation-locked | 4 |

**Documentation Quality (15 pts)**

| Criteria | Points |
|----------|--------|
| Quick Start section present and useful | 3 |
| Concrete examples for all triggers | 3 |
| Anti-patterns with WHY | 3 |
| Deep Dive sections for complex topics | 3 |
| Changelog maintained | 3 |

**Ecosystem Fit (15 pts)**

| Criteria | Points |
|----------|--------|
| Confirmed unique (no >80% overlap) | 5 |
| Related skills listed | 5 |
| Discoverability (index-ready description) | 5 |

### Supervisor Decision Protocol

```
STEP 1: Run automated evaluation
  python scripts/evaluate_skill_quality.py ~/.claude/skills/{name}/
  → JSON report with per-dimension scores

STEP 2: Manual inspection of high-risk areas
  • Read Phase 1 spec: were 11 lenses applied?
  • Read Phase 4 panel: were all rejections addressed?
  • Scan scripts: do they include self-verification?
  • Test: does Quick Start make sense to a first-time user?

STEP 3: Decision matrix

  Score ≥75 AND all dimension minimums met
    → APPROVED: Finalize and register

  Score 60-74 OR 1 dimension below minimum
    → REVISE: Return to Phase 3 with targeted feedback
    → Supervisor writes specific improvement tasks
    → Panel re-review is skipped (supervisor handles)

  Score <60 OR multiple critical failures
    → REJECT: Return to Phase 1 with full reset
    → Supervisor documents root cause
    → Flag iteration count for human review if >3

STEP 4: Approval record
  → Write supervisor verdict to SKILL.md Changelog
  → Include score breakdown
  → Note any accepted exceptions
```

### Supervisor vs Panel Relationship

```
Panel (Phase 4):          Supervisor (Phase 5):
─────────────────         ────────────────────────
3-4 specialist agents     1 generalist agent
Domain-focused review     Cross-domain final check
Unanimous required        Single authority
Iterative feedback        One-shot with priority list
Can miss forest for trees Catches what panel normalizes
```

---

## Quality Gates Summary

| Gate | Location | Requirement | Failure Action |
|------|----------|-------------|----------------|
| Spec Gate | Phase 2 → Phase 3 | Timelessness ≥7, no placeholders | Revise spec |
| Panel Gate | Phase 4 → Phase 5 | Unanimous approval | Loop Phase 1-4 |
| Supervisor Gate | Phase 5 → Final | Score ≥75, all mins met | REVISE or REJECT |

---

## Automated Evaluation

Run the quality scorecard on any skill:

```bash
# Full evaluation with JSON output
python scripts/evaluate_skill_quality.py ~/.claude/skills/my-skill/

# Evaluate and display summary
python scripts/evaluate_skill_quality.py ~/.claude/skills/my-skill/ --summary

# Compare two versions of a skill
python scripts/evaluate_skill_quality.py ~/.claude/skills/my-skill/ \
  --compare ~/.claude/skills/my-skill-v2/

# Batch evaluate all skills
python scripts/evaluate_skill_quality.py --batch ~/.claude/skills/ \
  --output report.json
```

Output format:
```json
{
  "skill": "my-skill",
  "total_score": 82,
  "dimensions": {
    "structural_quality": {"score": 13, "max": 15, "issues": []},
    "functional_completeness": {"score": 17, "max": 20, "issues": ["Missing anti-patterns"]},
    "agentic_capability": {"score": 10, "max": 15, "issues": ["No self-verification in scripts"]},
    "timelessness": {"score": 16, "max": 20, "issues": ["Only 1 extension point documented"]},
    "documentation_quality": {"score": 13, "max": 15, "issues": []},
    "ecosystem_fit": {"score": 13, "max": 15, "issues": []}
  },
  "verdict": "APPROVED",
  "gates_passed": true,
  "recommendations": ["Add scripts/verify.py with self-verification"]
}
```

---

## Phase 0: Skill Triage

Before creating anything, SkillForge intelligently analyzes your input to determine the best action.

### Decision Matrix

| Match | Intent | Action |
|-------|--------|--------|
| ≥80% | explicit create | CLARIFY (duplicate warning) |
| ≥80% | other | USE_EXISTING |
| 50-79% | any | IMPROVE_EXISTING |
| <50% | explicit create | CREATE_NEW |
| Multi-domain | any | COMPOSE |
| Ambiguous | any | CLARIFY |

---

## Validation & Packaging

```bash
# Automated quality evaluation (v5.0)
python scripts/evaluate_skill_quality.py ~/.claude/skills/my-skill/

# Structural validation
python scripts/validate-skill.py ~/.claude/skills/my-skill/

# Package for distribution
python scripts/package_skill.py ~/.claude/skills/my-skill/ ./dist
```

### Frontmatter Requirements

| Property | Required | Description |
|----------|----------|-------------|
| `name` | Yes | Hyphen-case, max 64 chars |
| `description` | Yes | Max 1024 chars, no angle brackets |
| `license` | No | MIT, Apache-2.0, etc. |
| `allowed-tools` | No | Restrict tool access |
| `metadata` | No | Custom fields |

---

## Skill Output Structure

```
~/.claude/skills/{skill-name}/
├── SKILL.md                       # Main entry point (required)
├── references/                    # Deep documentation (optional)
│   ├── patterns.md
│   └── examples.md
├── assets/                        # Templates (optional)
│   └── templates/
└── scripts/                       # Automation scripts (optional)
    ├── evaluate_skill_quality.py  # Quality scorecard [NEW v5.0]
    ├── validate.py                # Validation/verification
    ├── generate.py                # Artifact generation
    └── state.py                   # State management
```

---

## Anti-Patterns

| Avoid | Why | Instead |
|-------|-----|---------|
| Skipping Phase 5 | No final quality check | Always run Supervisor Review |
| Panel approving too easily | Groupthink over iterations | Supervisor provides fresh eyes |
| Score gaming | Passes gates but unusable | Supervisor checks real usability |
| Duplicate skills | Bloats registry | Phase 0 triage first |
| Single trigger | Hard to discover | 3-5 varied phrases |
| No verification | Can't confirm success | Measurable outcomes |
| Missing WHY | Can't evolve | Document rationale |

---

## Verification Checklist

After creation:

- [ ] Phase 0 triage confirmed no duplicates
- [ ] Phase 2 spec validated (timelessness ≥7)
- [ ] Phase 4 panel unanimous approval
- [ ] Phase 5 supervisor score ≥75, all gates pass
- [ ] `python scripts/evaluate_skill_quality.py` passes
- [ ] Frontmatter valid (only allowed properties)
- [ ] Changelog updated with supervisor verdict

---

<details>
<summary><strong>Deep Dive: Phase 1 - Analysis</strong></summary>

### 1A: Input Expansion

```
USER INPUT: "Create a skill for X"
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│ EXPLICIT REQUIREMENTS                                    │
│ IMPLICIT REQUIREMENTS                                    │
│ UNKNOWN UNKNOWNS                                         │
│ DOMAIN CONTEXT                                          │
└─────────────────────────────────────────────────────────┘
```

### 1B: Multi-Lens Analysis (11 models)

| Lens | Core Question |
|------|---------------|
| First Principles | What's fundamentally needed? |
| Inversion | What guarantees failure? |
| Second-Order | What happens after the obvious? |
| Pre-Mortem | Why did this fail? |
| Systems Thinking | How do parts interact? |
| Devil's Advocate | Strongest counter-argument? |
| Constraints | What's truly fixed? |
| Pareto | Which 20% delivers 80%? |
| Root Cause | Why is this needed? (5 Whys) |
| Comparative | How do options compare? |
| Opportunity Cost | What are we giving up? |

**Minimum requirement:** All 11 lenses scanned, at least 5 applied in depth.

### 1C: Regression Questioning

Iterative until 3 consecutive rounds produce no new insights.

### 1D: Automation Analysis

Identify script opportunities for each operation in the skill.

</details>

<details>
<summary><strong>Deep Dive: Phase 2 - Specification</strong></summary>

```xml
<skill_specification>
  <metadata>
    <name>skill-name</name>
    <analysis_iterations>N</analysis_iterations>
    <timelessness_score>X/10</timelessness_score>
  </metadata>
  <context>...</context>
  <requirements>
    <explicit>...</explicit>
    <implicit>...</implicit>
    <discovered>...</discovered>
  </requirements>
  <architecture>...</architecture>
  <scripts>...</scripts>
  <evolution_analysis>...</evolution_analysis>
  <anti_patterns>...</anti_patterns>
  <success_criteria>...</success_criteria>
</skill_specification>
```

### Spec Gate (before Phase 3)

- [ ] All sections present, no placeholders
- [ ] Every decision includes WHY
- [ ] Timelessness score ≥ 7
- [ ] ≥2 extension points documented
- [ ] Scripts section complete

</details>

<details>
<summary><strong>Deep Dive: Phase 4 - Synthesis Panel</strong></summary>

### Panel Composition

| Agent | Focus | When Active |
|-------|-------|-------------|
| Design/Architecture | Structure, patterns | Always |
| Audience/Usability | Clarity, discoverability | Always |
| Evolution/Timelessness | Future-proofing, extension | Always |
| Script/Automation | Agentic capability | When scripts present |

### Consensus Protocol

```
IF all agents APPROVED:
    → Pass to Phase 5 (Master Supervisor)

ELSE:
    → Collect all issues
    → Return to Phase 1 with feedback
    → Max 5 iterations

IF 5 iterations without consensus:
    → Flag for human review
```

**Note:** Panel approval is necessary but NOT sufficient. Phase 5 Supervisor may still REVISE or REJECT.

</details>

<details>
<summary><strong>Deep Dive: Phase 5 - Master Supervisor</strong></summary>

### Why a Supervisor?

After multiple panel iterations, agents may normalize issues — each small compromise seems reasonable, but the cumulative effect degrades quality. The Supervisor provides fresh-eyes review with no prior context.

### Supervisor Evaluation Workflow

```
1. Run evaluate_skill_quality.py for automated baseline
2. Read SKILL.md as a first-time user (no prior context)
3. Check: does Quick Start make sense immediately?
4. Check: are triggers discoverable from natural language?
5. Check: is verification concrete and measurable?
6. Audit scripts for self-verification
7. Score each dimension
8. Write verdict with evidence-backed reasoning
```

### Priority Classification for Feedback

| Priority | Description | Required Action |
|----------|-------------|-----------------|
| P0 Critical | Blocks usability or correctness | Must fix before approval |
| P1 Major | Significantly degrades quality | Must fix in current iteration |
| P2 Minor | Small improvement opportunity | Fix if ≤30min effort |
| P3 Nice-to-have | Optional enhancement | Log for future version |

### Iteration Limits

```
Iteration 1: Full pipeline
Iteration 2: REVISE path (Phase 3+ only)
Iteration 3: REVISE path (Phase 3+ only)
Iteration 4+: Escalate to human review
```

</details>

<details>
<summary><strong>Architecture Pattern Selection</strong></summary>

| Pattern | Use When |
|---------|----------|
| Single-Phase | Simple linear tasks |
| Checklist | Quality/compliance audits |
| Generator | Creating artifacts |
| Multi-Phase | Complex ordered workflows |
| Multi-Agent Parallel | Independent subtasks |
| Multi-Agent Sequential | Dependent subtasks |
| Orchestrator | Coordinating multiple skills |

</details>

<details>
<summary><strong>Configuration</strong></summary>

```yaml
SKILLCREATOR_CONFIG:
  mode: autonomous
  depth: maximum

  analysis:
    min_lens_depth: 5
    max_questioning_rounds: 7
    termination_empty_rounds: 3

  synthesis:
    panel_size: 3
    require_unanimous: true
    max_iterations: 5
    escalate_to_human: true

  supervisor:                     # NEW in v5.0
    enabled: true
    min_score: 75
    dimension_minimums:
      structural_quality: 10
      functional_completeness: 14
      agentic_capability: 10
      timelessness: 14
      documentation_quality: 10
      ecosystem_fit: 10
    max_revise_iterations: 2
    escalate_after_iterations: 3

  evolution:
    min_timelessness_score: 7
    min_extension_points: 2
    require_temporal_projection: true
```

</details>

---

## References

- [Regression Questions](references/regression-questions.md) - Complete question bank
- [Multi-Lens Framework](references/multi-lens-framework.md) - 11 thinking models guide
- [Specification Template](references/specification-template.md) - XML spec structure
- [Evolution Scoring](references/evolution-scoring.md) - Timelessness evaluation
- [Synthesis Protocol](references/synthesis-protocol.md) - Multi-agent panel details
- [Supervisor Protocol](references/supervisor-protocol.md) - Master Supervisor guide (NEW v5.0)
- [Script Integration Framework](references/script-integration-framework.md) - When and how to create scripts
- [Script Patterns Catalog](references/script-patterns-catalog.md) - Standard Python patterns

---

## Related Skills

| Skill | Relationship |
|-------|--------------|
| skill-composer | Can orchestrate created skills |
| codereview | Pattern for multi-agent panels |
| maker-framework | Zero error standard source |

---

## Extension Points

1. **Additional Supervisor Dimensions:** Add new quality dimensions to scorecard
2. **Domain-Specific Gates:** Create gates for specific skill categories (agentic, data, UI)
3. **Regression Testing:** Compare new skill versions against baseline scores
4. **Community Benchmarks:** Use aggregate scores to set minimum bar dynamically
5. **Additional Lenses:** Add thinking models to Phase 1
6. **Custom Synthesis Agents:** Extend panel for specific domains

---

## Changelog

### v5.0.0 (2026-02-23)
- **Added Phase 5: Master Supervisor Review** — independent final quality control
- **Added 6-dimensional Quality Scorecard** (100-point system with minimum thresholds)
- **Added Quality Gates** between Phase 2→3, Phase 4→5, Phase 5→Final
- **Added `evaluate_skill_quality.py`** — automated scoring script
- **Added `--evaluate` command** for evaluating existing skills
- **Added Supervisor Protocol reference** document
- **Updated configuration** with supervisor settings block
- Model updated to claude-sonnet-4-6

### v4.0.0
- Added Phase 0: Skill Triage
- Routing for existing skills
- Improved decision matrix

### v3.2.0
- Added Script Integration Framework
- Added Script Agent to synthesis panel
- Phase 1D: Automation Analysis

### v3.0.0
- Complete redesign as ultimate meta-skill
- 11 thinking models
- Multi-agent synthesis panel
- Evolution/timelessness core lens
