# felix-to-skills

面向 LLM 辅助开发与设计的三套技能（Skills）合集——让 AI 写得更克制、排得更高级、设计更有参考系。

---

## 目录

| 技能 | 类型 | 一句话 |
|------|------|--------|
| [Karpathy Guidelines](#1-karpathy-guidelines) | 行为准则 | 让 LLM 写代码时少犯蠢——先想再写、只改该改的、用测试闭环 |
| [HTML Report](#2-html-report) | 创意生成 | 零依赖、单文件 HTML 汇报页面——排版优先，反 AI-slop |
| [Design Refs](#3-design-refs) | 设计参考 | 56 个真实产品设计系统——Apple、Tesla、Stripe、Linear……拿来即用 |

---

## 1. Karpathy Guidelines

> 源自 [Andrej Karpathy 对 LLM 编码陷阱的观察](https://x.com/karpathy/status/2015883857489522876)，适配为技能文件。

### 四大原则

| 原则 | 解决问题 |
|------|----------|
| **Think Before Coding** | 不要假设、不要隐藏困惑、先讲清楚再动手 |
| **Simplicity First** | 最小代码解决问题，不过度抽象、不写用不上的扩展 |
| **Surgical Changes** | 只改必须改的，不顺手"优化"旁边代码 |
| **Goal-Driven Execution** | 定义可验证的成功标准，循环直到通过 |

### 文件结构

```
andrej-karpathy-skills/
├── SKILL.md                # 核心准则（4 条原则）
├── references/
│   └── examples.md         # 详细代码示例（正反对比）
└── README.md               # 安装与使用说明
```

### 怎么判断有效？

- Diffs 里只有真正需要的改动，没有顺手"优化"
- 复杂问题第一版就是简单方案，不用重写
- 提问发生在实现之前，而不是踩坑之后

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

## 使用方式

三套技能各自独立，可按需加载：

- **写代码更克制** → 加载 `andrej-karpathy-skills/SKILL.md`
- **生成汇报页面** → 加载 `html-report/SKILL.md`
- **做 UI/网页设计** → 查阅 `design-refs/` 目录

支持 SkillHub 等技能管理工具，也可直接复制到对应技能目录。

---

## 致谢

- Karpathy Guidelines 改编自 [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- Design Refs 提取自各品牌官网，仅作设计参考
- HTML Report 为原创技能
