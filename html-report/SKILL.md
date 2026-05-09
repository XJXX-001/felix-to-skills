---
name: html-report
description: Generate typographically rich, structurally sound HTML report pages. Zero-dependency single-file output. For business reports, meeting summaries, data analysis, project proposals, and internal documents. Load this skill whenever the user asks to create a report, meeting summary, data page, or structured HTML document.
category: creative
---

# HTML Report

零依赖、单文件、浏览器即开即用的汇报类 HTML 页面。

## 核心原则

1. **零依赖** — 单个 HTML 文件，CSS/JS 全部内联。
2. **反 AI-slop** — 禁止 Inter/Roboto/Arial 作 display 字体、紫色渐变白底、全居中布局。
3. **排版优先** — 字体质量 > 装饰效果。字号必须 `clamp()`，禁止固定 px。
4. **宁少勿糙** — 精选 4-6 个组件打磨，不要面面俱到但每个平庸。

---

## 三级工作流

### 极速路径（最快，推荐）

**读 0 文件**，直接用模板：

1. 从下方「类型→模板」表选模板文件
2. 读取对应 `templates/*.html` 模板
3. 替换内容，输出完整 HTML

### 标准路径

**读 1 文件**：[html-template.md](html-template.md) — 包含完整 CSS/JS，适用于需要自定义的场景。

### 复杂路径

在标准路径基础上按需读取：
- [INFOGRAPHIC_PATTERNS.md](INFOGRAPHIC_PATTERNS.md) — 图表选型指导
- [STYLE_PRESETS.md](STYLE_PRESETS.md) — 预设详情（用户要看风格预览时）

---

## 类型→模板速查

| 类型 | 触发词 | 模板文件 | 组件优先级 |
|------|--------|----------|------------|
| R1 周例会 | 周报、例会、月会、同步 | `bold-signal.html` | status-badge > callout > step-flow > summary-grid > table |
| R2 数据分析 | 数据、分析、KPI、趋势、指标 | `electric-studio.html` | stat-card > table > trend-indicator > chart > summary |
| R3 项目提案 | 提案、立项、方案、计划 | `dark-botanical.html` | hero-cover > stat-card > step-flow > callout > table |
| R4 年度总结 | 年度、年终、总结、回顾 | `dark-botanical.html` | stat-card > timeline > image-showcase > summary-grid > table |
| R5 竞品分析 | 竞品、对比、竞对 | `swiss-modern.html` | comparison-table > score-card > summary > callout |
| R6 调研报告 | 调研、研究、文献 | `paper-ink.html` | toc > section-heading > quote-block > table |
| R7 执行摘要 | 摘要、一页纸、executive summary | `swiss-modern.html` | big-number > callout > summary-grid > action-items |
| R8 产品文档 | 文档、手册、指南 | `swiss-modern.html` | step-flow > code-block > screenshot-box > callout-info > table |

---

## 预设速查（5 套常用）

| 预设 | 氛围 | Display 字体 | Body 字体 | 色调 |
|------|------|-------------|-----------|------|
| Bold Signal | 自信高冲击 | Archivo Black | Space Grotesk | 深色 + 橙 #FF5722 |
| Electric Studio | 干净专业 | Manrope | Manrope | 深色 + 蓝 #4361ee |
| Dark Botanical | 优雅精致 | Cormorant | IBM Plex Sans | 深色 + 暖金 #d4a574 |
| Swiss Modern | 极简包豪斯 | Archivo | Nunito | 白底 + 红 #ff3300 |
| Paper & Ink | 文学深度 | Cormorant Garamond | Source Serif 4 | 暖白 + 深红 #c41e3a |

> 其余 7 套预设见 [STYLE_PRESETS.md](STYLE_PRESETS.md)（Neon Cyber, Notebook Tabs, Vintage Editorial, Terminal Green, Creative Voltage, Split Pastel, Pastel Geometry）

---

## Phase 1: 确定类型与结构

1. 从速查表匹配报告类型
2. 用 clarify 一次性询问：内容状态（完整内容/大纲/主题）、数据需求、篇幅预期
3. 输出结构草案让用户确认

## Phase 2: 风格选择

- **「帮我选」**（推荐）— 自动匹配预设
- **「让我看看」** — 读 STYLE_PRESETS.md 生成 2-3 个预览

## Phase 3: 生成 HTML

### 生成规则

1. 单文件自包含，所有 CSS/JS 内联
2. 使用 CSS 变量（`:root`）
3. 每个 section 用 `<!-- === SECTION NAME === -->` 标注
4. 中英文混排时，西文 display 字体 + Noto Sans SC 回退
5. 图表数据通过内联 `style` 绑定（`width: N%`, `--donut-pct: N` 等）
6. 装饰元素必须有：网格背景、渐变光晕、微妙边框光效
7. 每个 section 至少一个视觉亮点（glowing accent line、hover 发光卡片、渐变进度条）

### 组件目录

| 组件 | 用途 |
|------|------|
| report-cover | 封面区（全高、渐变背景） |
| section-heading | 章节标题（编号 + 标题 + 副标题） |
| stat-card | 数据卡片（数字强调） |
| dashboard-grid | KPI 概览（混合卡片） |
| summary-grid | 摘要网格（2-4 列自适应） |
| callout | 提示框（左色条、语义色） |
| step-flow | 步骤流程（圆形编号） |
| comparison-table | 对比表格（响应式） |
| bullet-list | 要点列表 |
| status-badge | 状态标签（圆角 pill） |
| quote-block | 引用块（左竖线） |
| code-block | 代码块（等宽字体） |
| screenshot-box | 截图容器 |
| image-showcase | 图片展示 |
| ending-section | 结尾区（居中致谢） |

### 图表组件

| 图表 | CSS 类名 | 适用场景 |
|------|----------|----------|
| 水平柱状图 | `.chart-bar-horizontal` | 类别对比、排行榜 |
| 垂直柱状图 | `.chart-bar-vertical` | 少量类别对比 |
| 堆叠柱状图 | `.chart-bar-stacked` | 构成分解 |
| 环形图 | `.chart-donut` | 占比分布、完成率 |
| 进度条组 | `.progress-group` | 多指标达成率 |
| 迷你趋势线 | `.sparkline` | 紧凑时间趋势 |
| 时间线 | `.timeline` | 里程碑序列 |
| 热力网格 | `.heatmap` | 多维评分矩阵 |
| 子弹图 | `.bullet-chart` | 目标 vs 实际 |
| 评分卡 | `.score-card` | 多维度评分 |
| 仪表盘网格 | `.dashboard-grid` | KPI 概览 |
| 瀑布图 | `.waterfall` | 累积变化 |

### 图表选择速查

| 数据类型 | 推荐 | 不推荐 |
|----------|------|--------|
| 类别对比 3-8项 | Bar | Pie |
| 占比分布 2-5项 | Donut | Bar |
| 时间趋势 5-20点 | Sparkline | Bar |
| 进度/达成率 | Progress | Donut |
| 目标vs实际 | Bullet | 两个独立 Bar |
| 评分矩阵 | Heatmap | Radar |
| 里程碑序列 | Timeline | Bar |
| 构成分解 | Stacked Bar | 多个独立 Bar |
| 累积变化 | Waterfall | 普通 Bar |
| 多维度 KPI | Dashboard Grid | 单项罗列 |

---

## Phase 3.5: 数据校验（必读）

**在写入 HTML 文件之前，必须先用 Python 校验所有数字。** 不接受手算或记忆填数。

### 校验清单

| 校验项 | 方法 | 示例 |
|--------|------|------|
| 加总校验 | 各分项求和 = 报告合计 | `sum(stores) == report_total` |
| 百分比校验 | 实际/目标 × 100 = 报告百分比 | `actual / target * 100 == reported_pct` |
| 连带率校验 | 附加指标/手机销量 = 连带率 | `acs_qty / phone_qty == attach_rate` |
| 缺口校验 | 月目标 − 已完成 = 剩余缺口 | `target - done == gap` |
| 日均校验 | 已完成/天数 = 日均 | `done / days == daily_avg` |

### 执行方式

```python
# 报告生成前，运行类似如下校验脚本
python3 -c "
stores = {'A': 11524, 'B': 22614, ...}
total = sum(stores.values())
assert total == 75312, f'加总错误: {total} != 75312'
# ... 逐项校验
print('✅ 全部校验通过')
"
```

校验通过后再输出 HTML。校验失败则修正数据后重新校验。

---

## Phase 4: 交付

1. 保存为 `{type}-{date-or-topic}.html`
2. 告知：文件路径、预设名称、章节数、自定义方式（改 `:root` 变量换色，改字体 link 换字体）

---

## 设计禁令

- ❌ Inter, Roboto, Arial 作 display 字体
- ❌ `#6366f1` 通用靛蓝、紫色渐变白底
- ❌ 全内容居中对齐（封面除外）
- ❌ 无意义毛玻璃、无目的阴影
- ❌ 固定 px 字号 — 必须 `clamp()`
- ❌ `-clamp()` / `-min()` — 必须 `calc(-1 * ...)`

---

## 支持文件

| 文件 | 用途 | 何时读取 |
|------|------|----------|
| `templates/*.html` | 预设模板（9 套风格） | 极速路径（推荐） |
| [html-template.md](html-template.md) | 完整架构 + 全部组件 CSS + 动画 JS | 标准路径 |
| [INFOGRAPHIC_PATTERNS.md](INFOGRAPHIC_PATTERNS.md) | 图表使用指南 + HTML 示例 | 需要图表选型时 |
| [STYLE_PRESETS.md](STYLE_PRESETS.md) | 12 套预设完整 CSS | 用户要风格预览时 |
| [DESIGN_STANDARDS.md](DESIGN_STANDARDS.md) | 完整设计规范库 | 速查表不够时 |
| `extensions/INTERACTIVE_PATTERNS.md` | 动态图表、交互动画、数据刷新 | 需要动态/交互功能时 |
