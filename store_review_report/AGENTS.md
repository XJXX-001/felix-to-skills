# Store Review Report — Agent Guidelines

## Module Purpose

Generate professional Word (.docx) business review reports for retail stores.
Two modes: **auto-generation from data** and **fill-in-blank template**.

## When to Use This Skill

- User says "复盘", "经营报告", "门店报告", "销售分析", "成本利润"
- User wants to convert store data into a formatted Word document
- User mentions monthly/quarterly business review, PDCA, 5 Whys
- User asks to create a report with tables, metrics, action plans in Word

## Directory Structure

```
store_review_report/
├── report_generator.py       Core engine. Data → Word report
├── fill_template.py          Generate blank template for manual filling
├── data_template.py          Blank data template (copy & modify)
├── examples/sample_data.py   Sample data (Demo Store)
├── SKILL.md                  Skill manifest (triggers & quick start)
├── README.md                 Chinese user documentation
└── AGENTS.md                 This file
```

## Core API

### Auto Mode

```python
from store_review_report import StoreReviewReport, StoreReviewData
from store_review_report.examples.sample_data import get_sample_data

data = get_sample_data()  # Or user-provided data
report = StoreReviewReport(data)
report.generate("/output/path/report.docx")
```

### Fill-in Mode

```bash
python fill_template.py
# Output: 苹果门店月度复盘模板_店长填写版.docx
```

## Data Models

### StoreReviewData (total data package)

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| store_name | str | Yes | Display name |
| review_month | str | Yes | e.g. "2026年4月" |
| author | str | Yes | Report author |
| date | str | Yes | Report date |
| gmv | float | Yes | Gross Merchandise Value |
| gmv_target | float | Yes | Target GMV |
| gmv_last_month | float | Yes | Last month GMV |
| profit | float | Yes | Net profit. If 0, auto = rebate_amount - cost_total |
| cost_total | float | Yes | Sum of all costs |
| rebate_amount | float | Yes | Usually gmv * rebate_rate |
| rebate_rate | float | Yes | e.g. 0.10 for 10% |
| categories | List[CategoryData] | Yes | Product categories |
| costs | List[CostItem] | Yes | Cost breakdown |
| operation_metrics | List[OperationMetric] | Yes | Operation KPIs |
| conclusions | List[str] | Yes | Executive summary bullets |
| highlights | List[str] | Yes | What went well |
| weaknesses | List[str] | Yes | What needs improvement |
| problems | List[str] | Yes | Problem statements |
| five_whys | List[tuple] | Yes | (question, answer) pairs |
| actions | List[ActionItem] | Yes | Improvement actions |
| next_month_goals | List[dict] | Yes | {"维度": str, "基础目标": str, "挑战目标": str, "策略": str} |
| reflection | str | Yes | Manager's diary |

### CategoryData

```python
CategoryData(name, target, actual, last_month, unit="元", is_highlight=False)
```

### CostItem

```python
CostItem(category, name, amount, review="")
# category: "固定费用" | "人力费用" | "资金费用" | "运营费用" | "变动费用" | "运营杂费"
```

### ActionItem

```python
ActionItem(category, action, standard, owner, deadline)
# category examples: "手机板块（重点补救）", "短板品类攻坚", "优势品类守住", "过程管理"
```

## Constraints & Validation

1. **gmv must not be 0** — Cost rate calculation divides by gmv. Code has guard but avoid it.
2. **All monetary values in yuan** — Do not pass strings with ¥ symbol.
3. **rebate_amount consistency** — Should equal `gmv * rebate_rate`, but user override is allowed.
4. **cost_total consistency** — Should equal `sum(c.amount for c in costs)`.
5. **profit auto-calculation** — If profit=0, engine uses `rebate_amount - cost_total`.

## Design System (COLORS dict)

| Key | Hex | Usage |
|-----|-----|-------|
| primary | `#1B2A4A` | Headers, table headers |
| success | `#047857` | Good metrics (≥100%), positive profit |
| warning | `#B45309` | Fair metrics (75-99%) |
| danger | `#BE123C` | Bad metrics (<75%), loss, problems |
| bg_light | `#F8FAFC` | Table alternating rows |
| bg_accent | `#EFF6FF` | Emphasis blocks |
| text | `#1E293B` | Body text |
| text_muted | `#64748B` | Secondary text |

## Code Modification Rules

1. **Data and rendering separated** — Data lives in `StoreReviewData`, rendering in `StoreReviewReport` methods.
2. **Use utility functions** — `set_run_font()`, `set_cell_shading()`, `set_cell_border()` for consistency.
3. **Add colors to COLORS dict** — No hardcoded hex strings outside the dict.
4. **Chinese font support** — Always set both `font.name` and `rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')`.
5. **Each chapter = one method** — `add_summary()`, `add_sales_analysis()`, etc. Add to `generate()` in order.

## Common Pitfalls

- **Import path**: `from store_review_report import ...` (with underscores, not hyphens)
- **Fill-in template**: Do not use underline characters `_` inside table cells. Leave blank or use gray hint text.
- **Sample data**: `examples/sample_data.py` is bound to a specific store (Demo Store, Apr 2026). Always create a new data file for other stores.
- **Output path**: Default output is in the skill directory. Ask user for preferred path if unspecified.

## Multi-Tool Compatibility

This skill is designed to work with:
- **OpenClaw** — Reads SKILL.md front matter for triggers
- **HermesAgent** — Reads AGENTS.md for API specs and constraints
- **ClaudeCode** — Reads SKILL.md + AGENTS.md for usage patterns
- **Kimi CLI** — Standard skill directory structure with SKILL.md

All agents should load this skill when the user asks about store business review, report generation, or Word document creation for retail stores.
