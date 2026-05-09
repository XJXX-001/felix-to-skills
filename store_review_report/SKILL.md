---
name: store_review_report
description: |
  Generate professional Word (.docx) business review reports for retail stores.
  Use this skill whenever the user needs to create a monthly/quarterly business review report,
  store performance analysis, sales recap, cost-profit review, or action plan document in Word format.
  Also use when the user mentions "复盘", "经营报告", "门店报告", "销售分析", "成本利润",
  "月度总结", "PDCA", "5个为什么", or wants to convert store data into a formatted Word document.
  Supports both auto-generation from structured data and fill-in-the-blank templates for manual completion.
---

# Store Review Report

Generate professional Word (.docx) business review reports for retail stores.

## Two Modes

| Mode | Use Case | Entry Point |
|------|----------|-------------|
| **Auto** | Structured data → Beautiful report automatically | `StoreReviewReport(data).generate(output_path)` |
| **Fill-in** | Generate blank template for manual filling | `python fill_template.py` |

## Prerequisites

```bash
pip install python-docx
```

## Quick Start — Auto Mode

```python
from store_review_report import StoreReviewReport, StoreReviewData
from store_review_report.examples.sample_data import get_sample_data

data = get_sample_data()  # Replace with your own data
report = StoreReviewReport(data)
report.generate("./report.docx")
```

## Data Model

```python
StoreReviewData(
    store_name="Store Name",
    review_month="2026-05",
    author="Manager Name",
    date="2026-06-01",
    gmv=260000,              # Gross Merchandise Value
    gmv_target=300000,       # GMV target
    gmv_last_month=240000,   # Last month GMV
    profit=5000,             # Net profit (auto-calculated if 0)
    cost_total=18000,        # Total costs
    rebate_amount=26000,     # Rebate amount
    rebate_rate=0.10,        # Rebate rate (e.g. 10%)
    categories=[...],        # List[CategoryData]
    costs=[...],             # List[CostItem]
    operation_metrics=[...], # List[OperationMetric]
    conclusions=[...],       # List[str] — executive summary
    highlights=[...],        # List[str] — what went well
    weaknesses=[...],        # List[str] — what needs improvement
    problems=[...],          # List[str] — problem breakdown
    five_whys=[...],         # List[(question, answer)]
    actions=[...],           # List[ActionItem]
    next_month_goals=[...],  # List[dict]
    reflection="...",        # Manager's reflection diary
)
```

## CategoryData

```python
CategoryData(
    name="Phone",       # Category name
    target=50,          # Monthly target
    actual=45,          # Actual achievement
    last_month=42,      # Last month's actual
    unit="units",       # Unit: "units", "yuan", "%", etc.
    is_highlight=False, # Whether to highlight this row
)
```

## Auto-Calculated Fields

The generator automatically computes:
- **Achievement rate** = `actual / target` (colored: green ≥100%, yellow 75-99%, red <75%)
- **MoM change** = `(actual - last_month) / last_month` (green=up, red=down)
- **Cost rate** = `cost_total / gmv`
- **Cost/rebate ratio** = `cost_total / rebate_amount`

## Design System

| Element | Color | Hex |
|---------|-------|-----|
| Primary (headers) | Deep Indigo | `#1B2A4A` |
| Success (good metrics) | Emerald | `#047857` |
| Warning (fair metrics) | Amber | `#B45309` |
| Danger (bad metrics/loss) | Brick Red | `#BE123C` |
| Background | Light Gray | `#F8FAFC` |

## Fill-in Template Mode

```bash
cd store_review_report
python fill_template.py
# Output: 苹果门店月度复盘模板_店长填写版.docx
```

## Files

```
store_review_report/
├── SKILL.md                  # This file
├── AGENTS.md                 # AI agent guidelines
├── README.md                 # User documentation (Chinese)
├── __init__.py               # Package exports
├── report_generator.py       # Core engine (auto mode)
├── fill_template.py          # Fill-in-blank template generator
├── data_template.py          # Blank data template for users
├── examples/
│   └── sample_data.py        # Sample data (Demo Store, Apr 2026)
```
