# 门店经营复盘报告生成器

> **Store Review Report** — 数据驱动的门店经营复盘 Word 报告生成工具

## 功能概述

本 Skill 提供两种报告生成模式：

| 模式 | 适用场景 | 说明 |
|-----|---------|------|
| **数据驱动版** | 已有完整数据，自动生成精美报告 | 填入数据 → 一键生成 |
| **填空版** | 需要分发给店长手动填写 | 生成空白模板 → 打印/分发 |

## 环境依赖

```bash
pip install python-docx
```

## 模式一：数据驱动版（推荐）

### 1. 准备数据

复制 `data_template.py` 并重命名（如 `my_store_data.py`），填入真实数据：

```python
from store_review_report import StoreReviewData, CategoryData, CostItem, OperationMetric, ActionItem

def get_my_data():
    return StoreReviewData(
        store_name="示例门店",
        review_month="2026年5月",
        author="店长",
        date="2026年6月",
        gmv=280000,
        gmv_target=300000,
        gmv_last_month=260000,
        profit=8000,
        cost_total=18000,
        rebate_amount=28000,
        rebate_rate=0.10,
        categories=[
            CategoryData("GMV", 300000, 280000, 260000, "元", True),
            CategoryData("手机", 200, 180, 170, "台", True),
            # ... 更多品类
        ],
        costs=[
            CostItem("固定费用", "房租", 5000, "刚性支出"),
            # ... 更多费用
        ],
        # ... 其他字段
    )
```

### 2. 生成报告

```python
from store_review_report import StoreReviewReport
from my_store_data import get_my_data

data = get_my_data()
report = StoreReviewReport(data)
report.generate("./示例门店_5月复盘报告.docx")
```

### 自动计算

脚本会根据原始数据自动计算：
- **达成率** = 实际 / 目标（自动标色：≥100% 绿、75%~100% 黄、<75% 红）
- **环比变动** = (本月 - 上月) / 上月（上涨绿、下跌红）
- **费用率** = 费用合计 / GMV
- **费用占返利比** = 费用合计 / 返利金额

## 模式二：填空版

```bash
cd store_review_report
python fill_template.py
```

输出：`苹果门店月度复盘模板_店长填写版.docx`

填空版特点：
- 表格内填空区域**无下划线**，直接留白或淡灰提示文字
- 非表格的长文本区使用浅色边框卡片，美观且便于填写
- 第一章为「门店经营结果与成本·净利呈现」，含经营结果表、成本结构表、净利润核算表

## 设计说明

### 配色方案

| 颜色 | 色值 | 用途 |
|-----|------|------|
| 深靛蓝 | `#1B2A4A` | 主标题、表头 |
| 翠绿 | `#047857` | 达成优秀、利润为正 |
| 琥珀 | `#B45309` | 达成一般、强调装饰 |
| 砖红 | `#BE123C` | 达成差、亏损、问题项 |
| 极浅灰 | `#F8FAFC` | 表格交替背景 |

### 排版特色

- 标题左侧 `▌` 装饰竖条，强化层级
- 封面含中英文标题 + 装饰线 + 信息卡片
- 页脚含门店信息，便于打印归档
- 表格细边框 + 合适内边距，现代简洁

## 文件结构

```
store_review_report/
├── SKILL.md                  # Skill 清单（触发条件 & 快速开始）
├── AGENTS.md                 # AI 代理规范（API & 约束）
├── README.md                 # 本文档（中文用户说明）
├── __init__.py               # 包导出
├── report_generator.py       # ⭐ 核心引擎（数据驱动版）
├── fill_template.py          # 填空版模板生成器
├── data_template.py          # 空白数据模板（复制修改）
└── examples/
    └── sample_data.py        # 示例数据（示例门店4月）
```

## 常见问题

**Q1：可以管理不同品牌的门店吗？**
> 可以。`categories` 列表不限定品类名称和数量，直接填入实际经营品类即可。

**Q2：报告中的文字分析能自动生成吗？**
> 数据可以自动计算，但经营洞察（`conclusions`、`highlights`、`weaknesses` 等）需要人工填写，确保分析质量。

**Q3：我想修改报告结构或增加章节？**
> 打开 `report_generator.py`，找到 `StoreReviewReport.generate()` 方法，按需增删章节。每个章节都是独立方法，注释清晰。

**Q4：如何适配其他 AI 工具（ClaudeCode、OpenClaw 等）？**
> 本 Skill 已按标准格式编写 `SKILL.md` 和 `AGENTS.md`，各工具读取后即可识别触发条件和使用方式。
