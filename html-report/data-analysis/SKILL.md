---
name: data-analysis
description: |
  读取 Excel 数据，自动执行对比分析，生成零依赖单文件 HTML 报告。
  适用于两期数据对比、经营复盘、销售分析、KPI 自动生成。
  触发词：Excel分析、经营复盘、两期对比、销售分析、数据分析报告
category: data
---

# 数据驱动报告生成器

读取两期 Excel 数据，自动执行对比分析，输出零依赖单文件 HTML 报告。

## 触发条件

当用户有以下需求时，加载此子技能：
- 已有 Excel 数据需要分析
- 需要两期数据对比（同比/环比）
- 需要生成经营复盘报告
- 需要自动生成 KPI、门店、人员、品类分析

## 依赖

```bash
pip install pandas openpyxl pyyaml
```

## 使用方法

### 1. 配置

复制配置模板并修改：

```bash
cp config/template.yaml my-project.yaml
```

编辑 `my-project.yaml`，配置数据源和业务规则。

### 2. 运行

```bash
python3 scripts/generate_report.py --config my-project.yaml
```

### 3. 输出

报告生成在配置文件指定的目录中，零依赖、离线可用。

## 文件结构

```
data-analysis/
├── SKILL.md              # 本文件
├── scripts/
│   ├── generate_report.py  # 主脚本
│   └── category_mapper.py  # 品类映射引擎
└── config/
    └── template.yaml       # 配置模板
```

## 配置说明

详见 `config/template.yaml` 中的注释。

关键配置项：
- `data.period1_file` / `data.period2_file`：两期数据文件路径
- `data.columns`：Excel 列名映射
- `business_rules`：排除规则
- `categories`：品类映射规则
- `output`：输出目录和文件名

## 报告章节

1. **数据概览** — 数据源信息、覆盖范围统计
2. **执行摘要** — 核心指标概览、两期 KPI 对比明细
3. **门店与个人排名** — 按门店及个人维度的毛利对比
4. **环比诊断与预警** — 上升明星、下滑预警、门店环比变化
5. **品类销量与毛利迁移** — 六大品类的结构性迁移趋势
6. **战略矩阵诊断** — 人员健康度矩阵、品类 BCG 矩阵
7. **行动计划** — 立即行动、中期优化建议

## 数据校验

脚本内置 5 项强制校验：
1. 门店销售额加总 = 总销售额
2. 门店毛利加总 = 总毛利
3. 人员销售额加总 = 总销售额
4. 品类销售额加总 = 总销售额
5. 品类毛利加总 = 总毛利

校验失败会报错，确保数据准确性。

## 扩展用法

复制配置模板为不同项目的配置文件，修改数据路径和规则后运行：

```bash
python3 scripts/generate_report.py --config 国庆促销.yaml
python3 scripts/generate_report.py --config 双11复盘.yaml
```

## 注意事项

- Excel 中的销售金额通常为负数（销售出库单），脚本会自动取反
- `exclude_staff` 按姓名精确匹配
- 品类规则按 `priority` 从小到大依次匹配，第一个命中的规则生效
- 必须保留一条 `match_mode: "default"` 的兜底规则

## 自定义报告样式

如需修改报告视觉风格，可编辑 `scripts/generate_report.py` 中的 CSS 变量：

```css
:root {
    --bg-primary: #0a0a0a;     /* 主背景 */
    --bg-card: #141414;        /* 卡片背景 */
    --accent: #4361ee;         /* 强调色 */
    --font-display: 'Manrope'; /* 标题字体 */
    --font-body: 'Manrope';    /* 正文字体 */
}
```

当前默认使用 Electric Studio 预设风格（深色 + 蓝 #4361ee）。
