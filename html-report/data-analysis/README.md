# 经营复盘报告生成器

读取两期 Excel 销售数据，自动执行对比分析，输出零依赖单文件 HTML 报告。

## 目录结构

```
data-analysis/
├── SKILL.md              # 技能入口
├── README.md             # 本文件
├── scripts/
│   ├── generate_report.py  # 主脚本：读取数据 → 计算指标 → 生成 HTML
│   └── category_mapper.py  # 品类映射引擎（独立模块）
├── config/
│   └── template.yaml       # 配置文件模板（数据源、排除项、品类规则）
└── examples/               # 示例配置（可选）
```

## 依赖安装

```bash
pip install pandas openpyxl pyyaml
```

或使用 uv：

```bash
uv pip install pandas openpyxl pyyaml
```

## 使用方法

### 1. 准备配置

复制配置模板：

```bash
cp config/template.yaml my-project.yaml
```

### 2. 修改配置

编辑 `my-project.yaml`：

```yaml
report:
  title: "报告标题"
  subtitle: "副标题"
  author: "数据分析部"

data:
  period1_file: "data/上期数据.xlsx"
  period2_file: "data/本期数据.xlsx"
  period1_label: "2025"
  period2_label: "2026"

business_rules:
  exclude_staff: ["肖琴", "陈宇"]   # 排除不参与分析的人员
  exclude_stores: []                # 排除不参与分析的门店

categories:
  # 品类映射规则（优先级数字越小越优先）
  - name: "iPhone"
    keywords: ["iphone"]
    match_mode: "contains_ci"
    priority: 1
  - name: "配件"
    keywords: []
    match_mode: "default"          # default 必须存在，作为兜底
    priority: 999

output:
  report_dir: "reports/输出目录"
  report_filename: "report.html"
```

### 3. 生成报告

```bash
python3 scripts/generate_report.py --config my-project.yaml
```

### 4. 查看报告

直接用浏览器打开生成的 HTML 文件，**零依赖，离线可用**。

## 关键特性

| 特性 | 说明 |
|------|------|
| 新员工环比 | 自动处理，显示 `—` 而非离谱数字 |
| 新店环比 | 自动处理，显示 `—` 而非离谱数字 |
| 健康度分类 | 过滤新员工后按真实中位数分类 |
| 数据校验 | 5 项强制校验，确保数据准确 |
| HTML 体积 | ~62 KB / ~350 行，轻量高效 |
| 外部依赖 | 零依赖，离线可用 |

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

## 配置详解

### 报告配置

```yaml
report:
  title: "报告标题"           # 显示在封面和标题
  subtitle: "副标题"          # 显示在封面
  author: "数据分析部"        # 显示在封面和页脚
  period_label: "五一"        # 分析周期标签
```

### 数据配置

```yaml
data:
  period1_file: "data/上期.xlsx"    # 上期数据文件路径
  period2_file: "data/本期.xlsx"    # 本期数据文件路径
  period1_label: "2025"             # 上期标签（用于列名）
  period2_label: "2026"             # 本期标签（用于列名）
  columns:                          # Excel 列名映射
    date: "单据日期"
    store: "分支机构名称"
    staff: "职员名称"
    product: "商品名称"
    quantity: "数量"
    discounted_amount: "折后金额"
    cost_amount: "成本金额"
    gross_margin: "毛利"
```

### 业务规则

```yaml
business_rules:
  exclude_staff: ["姓名1", "姓名2"]  # 排除不参与分析的人员
  exclude_stores: ["门店1", "门店2"]  # 排除不参与分析的门店
```

### 品类映射

```yaml
categories:
  - name: "iPhone"                    # 品类名称
    keywords: ["iphone"]              # 关键词列表
    match_mode: "contains_ci"         # 匹配模式
    priority: 1                       # 优先级（数字越小越优先）
  - name: "配件"
    keywords: []
    match_mode: "default"             # 兜底规则（必须存在）
    priority: 999
```

**匹配模式：**
- `contains`：包含关键词（区分大小写）
- `contains_ci`：包含关键词（不区分大小写）
- `regex`：正则表达式匹配
- `default`：兜底规则（必须存在）

### 输出配置

```yaml
output:
  report_dir: "reports/2026-五一"     # 输出目录
  report_filename: "report.html"      # 输出文件名
```
