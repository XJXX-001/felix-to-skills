# felix-to-skills

面向 LLM 辅助开发与设计的五套技能（Skills）合集——让 AI 写得更克制、排得更高级、设计更有参考系、复盘更有深度、提交更干净。

---

## 目录

| 技能 | 类型 | 一句话 |
|------|------|--------|
| [Felix-Agent](#1-felix-agent) | 行为准则 | Karpathy 编码原则 + Agent 执行纪律——先想再写、工具优先、状态持久、原子提交 |
| [HTML Report](#2-html-report) | 创意生成 | 零依赖、单文件 HTML 汇报页面——排版优先，反 AI-slop |
| [Design Refs](#3-design-refs) | 设计参考 | 56 个真实产品设计系统——Apple、Tesla、Stripe、Linear……拿来即用 |
| [Store Review Report](#4-store-review-report) | 业务生成 | 门店经营复盘 Word 报告——数据填入、自动排版、一键生成 .docx |
| [Frontend UI Engineering](#5-frontend-ui-engineering) | 工程规范 | 构建生产级前端 UI——可访问、响应式、反 AI 审美、设计系统遵循 |
| [Profit Statement Analysis](#6-profit-statement-analysis) | 业务分析 | Apple APR 授权经销商利润表财务分析——毛利率/费用率/净利率、门店评分、行业对标、HTML 报告 |

---

## 1. Felix-Agent

> 源自 [Andrej Karpathy 对 LLM 编码陷阱的观察](https://x.com/karpathy/status/2015883857489522876)，融合 Git 工作流纪律与 Agent 执行工程化，形成完整的三层行为规范。

### 三层纪律

| 层级 | 原则 | 解决问题 |
|------|------|----------|
| **思维层** | Think Before Coding | 不要假设、不要隐藏困惑、先讲清楚再动手 |
| **思维层** | Simplicity First | 最小代码解决问题，不过度抽象、不写用不上的扩展 |
| **思维层** | Surgical Changes | 只改必须改的，不顺手"优化"旁边代码 |
| **思维层** | Goal-Driven Execution | 定义可验证的成功标准，循环直到通过 |
| **编码执行层** | Git Discipline | 原子提交、干净历史、可审查、可回退 |
| **Agent 执行层** | Agent Execution Discipline | 工具优先、任务拆解、状态持久、复用发现 |

### 核心映射

**原则 → Git 映射：**

| 原则 | Git 映射 |
|------|----------|
| Think Before Coding | 编码前先规划分支范围、预估 commit 粒度 |
| Simplicity First | 变更小则提交粒度小，不累积 300+ 未提交行 |
| Surgical Changes | 格式化/重构/功能分开 commit，附 Change Summary |
| Goal-Driven Execution | Save Point 模式：测试通过 → commit；失败 → `git reset --hard` |

**Agent 执行映射：**

| 原则 | 执行映射 |
|------|----------|
| Deterministic Operations | 批量操作写脚本，API 调用输出结构化指令，失败时解析错误码 |
| Decompose, Gate, and Flow | 复杂任务拆原子步骤，每步定义完成标准，数据显式传递 |
| Persist, Resume, and Audit | 跨会话任务写入 `.state` 文件，支持断点续跑，保留操作日志 |
| Discover Before Inventing | 执行前先搜现有工具/skill，复用流程固化为模板，批量生成用元编程 |

### 文件结构

```
Felix-Agent/
├── SKILL.md                # 核心准则（4 条原则 + Agent 执行纪律 + Git 执行纪律）
├── references/
│   ├── examples.md         # 详细代码示例（正反对比）
│   └── git-workflow.md     # Git 工作流详细参考（commit 格式、Worktree、调试）
└── README.md               # 安装与使用说明
```

### 怎么判断有效？

- Diffs 里只有真正需要的改动，没有顺手"优化"
- 复杂问题第一版就是简单方案，不用重写
- 提问发生在实现之前，而不是踩坑之后
- 每个 commit 都是原子、有描述、可审查的 save point
- 批量操作优先用脚本/工具，不手动逐行执行
- 跨会话任务能从 `.state` 断点恢复，不丢失进度

---

## 2. HTML Report

> 零依赖、单文件、浏览器即开即用的汇报类 HTML 页面生成器。

### 核心特征

| 特征 | 说明 |
|------|------|
| 零依赖 | 单个 HTML 文件，CSS/JS 全部内联 |
| 反 AI-slop | 禁止 Inter/Roboto/Arial 做 display 字体、紫色渐变白底、全居中 |
| 排版优先 | 字号 `clamp()` 流体，字体质量 > 装饰效果 |
| 宁少勿糙 | 精选 4-6 个组件打磨，不要面面俱到但每个平庸 |

### 12 套视觉预设

| 预设 | 氛围 | Display 字体 | 强调色 |
|------|------|-------------|--------|
| Bold Signal | 自信高冲击 | Archivo Black | #FF5722 橙 |
| Electric Studio | 干净专业 | Manrope | #4361ee 蓝 |
| Dark Botanical | 优雅精致 | Cormorant | #d4a574 暖金 |
| Swiss Modern | 极简包豪斯 | Archivo | #ff3300 红 |
| Paper & Ink | 文学深度 | Cormorant Garamond | #c41e3a 深红 |

（另有 7 套：Neon Cyber、Notebook Tabs、Vintage Editorial、Terminal Green、Creative Voltage、Split Pastel、Pastel Geometry）

### 报告类型匹配

| 类型 | 触发词 | 推荐预设 |
|------|--------|----------|
| 周例会/同步 | 周报、例会、月会 | Bold Signal |
| 数据分析 | 数据、KPI、趋势 | Electric Studio |
| 项目提案 | 提案、立项、方案 | Dark Botanical |
| 年度总结 | 年度、年终、回顾 | Dark Botanical |
| 竞品分析 | 竞品、对比 | Swiss Modern |
| 调研报告 | 调研、研究、文献 | Paper & Ink |
| 执行摘要 | 摘要、一页纸 | Swiss Modern |
| 产品文档 | 文档、手册、指南 | Swiss Modern |

### 内置组件

14 个内容组件（cover、stat-card、comparison-table、timeline 等）+ 12 种图表（柱状图、环形图、热力网格、瀑布图等），全部内联 CSS 实现，无需 Chart.js 等外部库。

### 文件结构

```
html-report/
├── SKILL.md                       # 技能入口（三级工作流 + 速查表）
├── templates/                     # 9 个预设模板（极速路径直接用）
├── html-template.md               # 标准路径：完整 CSS/JS 参考架构
├── DESIGN_STANDARDS.md            # 完整设计规范库
├── STYLE_PRESETS.md               # 12 套视觉预设完整 CSS
├── INFOGRAPHIC_PATTERNS.md        # 图表使用指南 + HTML 示例
└── extensions/
    └── INTERACTIVE_PATTERNS.md    # 动态图表、交互动画扩展
```

---

## 3. Design Refs

> 56 个真实产品设计系统参考，提取自主流产品官网、约 16,000 行设计规范。

### 覆盖范围

| 类别 | 数量 | 代表品牌 |
|------|------|----------|
| 开发者工具 | 14 | Linear、Vercel、Stripe、Supabase、Raycast |
| AI 产品 | 15 | Claude、Cursor、xAI、ElevenLabs、NVIDIA |
| 设计/创意 | 6 | Figma、Framer、Webflow、Miro |
| SaaS/企业 | 7 | Notion、Airtable、Intercom、Zapier |
| 电商/品牌 | 7 | Apple、Nike、Tesla、Airbnb、Shopify |
| 汽车/硬件 | 4 | BMW、Ferrari、SpaceX、PlayStation |
| 金融 | 4 | Coinbase、Revolut、Wise、Kraken |
| 传统/企业 | 2 | IBM、Spotify |

### 快速选择

| 想要... | 参考 |
|---------|------|
| 高级感 | Apple / Tesla / Linear / Ferrari |
| 温暖人文 | Claude / Notion / Airbnb / Cal |
| 性能/速度感 | Linear / Superhuman / Warp / Raycast |
| 未来科技 | Cursor / xAI / PlayStation / SpaceX |
| 极简留白 | Apple / Tesla / Vercel / xAI |
| 暗色专业 | Linear / Cursor / Stripe / Sentry |
| 多彩活泼 | Figma / Airtable / Zapier / PostHog |
| 金融信任 | Stripe / Wise / Coinbase |

### 使用方式

1. 先读 `catalog.md`（56 个系统的紧凑摘要）了解全部可选风格
2. 根据项目类型和氛围匹配 1-3 个品牌
3. 读取具体品牌的 `.md` 文件，提取设计令牌（颜色、字体、间距、圆角、阴影）

### 文件结构

```
design-refs/
├── README.md        # 按场景分类的索引
├── AGENTS.md        # LLM 使用指南
├── catalog.md       # 56 个系统紧凑摘要（先读这个）
└── [brand].md × 56  # 每个品牌的完整设计规范
```

---

## 4. Store Review Report

> 数据驱动的门店经营复盘 Word (.docx) 报告生成器。

### 两种模式

| 模式 | 适用场景 | 入口 |
|------|----------|------|
| **数据驱动版** | 已有完整数据，自动生成精美报告 | `StoreReviewReport(data).generate(output_path)` |
| **填空版** | 需要分发给店长手动填写 | `python fill_template.py` |

### 核心特征

| 特征 | 说明 |
|------|------|
| Word 原生 | 基于 `python-docx`，输出标准 .docx 文件 |
| 自动计算 | 达成率、环比变动、费用率、净利润全部自动计算并标色 |
| 七章结构 | 经营结果 → 销售分析 → 成本利润 → 过程指标 → PDCA → 5 Whys → 下月计划 |
| 配色体系 | 深靛蓝（表头）+ 翠绿（达标）+ 琥珀（预警）+ 砖红（亏损） |

### 报告章节

1. **经营结果与成本·净利呈现** — GMV/利润概览表 + 成本结构分解
2. **品类销售深度分析** — 品类达成率/环比，高亮/短板自动标记
3. **成本结构深度分析** — 费用占比饼图 + 费用/返利比率
4. **过程指标诊断** — 客流、转化率、连带率、融合订单、新增粉
5. **PDCA 问题闭环** — 结论 → 亮点 → 短板 → 行动项（含责任人和期限）
6. **5 Whys 根因分析** — 五层追问，从现象到真因
7. **下月经营目标** — 基础目标/挑战目标/策略三位一体

### 快速开始

```bash
pip install python-docx
```

```python
from store_review_report import StoreReviewReport
from store_review_report.examples.sample_data import get_sample_data

data = get_sample_data()
report = StoreReviewReport(data)
report.generate("./report.docx")
```

### 文件结构

```
store_review_report/
├── SKILL.md               # 技能入口
├── AGENTS.md              # AI Agent 操作规范
├── README.md              # 中文用户文档
├── __init__.py            # 包导出
├── report_generator.py    # 核心引擎（数据驱动版）
├── fill_template.py       # 填空版模板生成器
├── data_template.py       # 空白数据模板
└── examples/
    └── sample_data.py     # 示例数据
```

---

## 5. Frontend UI Engineering

> 构建生产级质量的前端用户界面——可访问、响应式、性能优良、视觉精致。

### 核心原则

| 原则 | 说明 |
|------|------|
| **反 AI 审美** | 拒绝紫色渐变、全圆角、通用卡片网格——使用项目真实设计系统 |
| **组合优于配置** | `<Card><CardHeader>...</CardHeader></Card>` 而非 `<Card title="..." headerVariant="..." />` |
| **数据与展示分离** | Container 处理数据获取，Presentation 处理渲染 |
| **WCAG 2.1 AA** | 键盘导航、ARIA 标签、焦点管理、有意义的空/错误状态 |

### 文件结构

```
frontend-ui-engineering/
└── SKILL.md          # 技能入口（组件架构、状态管理、设计系统、a11y、响应式、加载态）
```

### 使用方式

直接加载 `frontend-ui-engineering/SKILL.md` 即可。适用于：
- 新建 UI 组件或页面
- 修改现有用户界面
- 实现响应式布局
- 添加交互或状态管理
- 修复视觉或 UX 问题

---

## 6. Profit Statement Analysis

> 适用于 Apple APR 授权经销商门店利润表的结构化财务分析技能。

### 分析框架

| 模块 | 内容 |
|------|------|
| 收入分析 | 月度趋势 / 各店贡献 / 收入结构诊断 |
| 盈利能力 | 毛利率排名 / 净利率排名 / 月度利润走势 |
| 费用结构 | 费用构成（工资/房租/摊销等）/ 费用率对比 / O2O 手续费分析 |
| 门店诊断 | A-D 级门店评分 / 关键指标汇总 / 专项诊断 |
| 行业对标 | 9 项 Apple APR 行业基准对比（毛利率/净利率/房租占比/人工占比等） |

### 数据要求

固定结构利润表 Excel，包含 `template` 工作表，前两行为表头，第 3 行起为数据行。

### 文件结构

```
profit-statement-analysis/
├── SKILL.md      # 技能入口（完整分析框架 + 行业基准 + 注意事项）
└── README.md     # 本文件
```

---

## 使用方式

六套技能各自独立，可按需加载：

- **写代码 + Git 纪律 + Agent 执行** → 加载 `Felix-Agent/SKILL.md`
- **生成汇报页面** → 加载 `html-report/SKILL.md`
- **做 UI/网页设计** → 查阅 `design-refs/` 目录
- **生成门店复盘报告** → 加载 `store_review_report/SKILL.md`
- **构建生产级前端 UI** → 加载 `frontend-ui-engineering/SKILL.md`
- **利润表财务分析** → 加载 `profit-statement-analysis/SKILL.md`

支持 SkillHub 等技能管理工具，也可直接复制到对应技能目录。

---

## 致谢

- Karpathy Guidelines 改编自 [forrestchang/engineering-discipline](https://github.com/forrestchang/engineering-discipline)
- Design Refs 提取自各品牌官网，仅作设计参考
- HTML Report 为原创技能
- Store Review Report 为原创技能
