# Changelog

## 2026-05-05

### 速度优化重构

**目标**：减少 Hermes 生成 HTML 报告时的文件读取次数和 context 占用，加快生成速度。

#### SKILL.md 精简

- 391 行 → 175 行（-55%）
- 新增三级工作流：极速路径（读模板）/ 标准路径（读 html-template.md）/ 复杂路径（按需读取）
- 内联汇报类型→模板映射表、预设速查表，省去必读 DESIGN_STANDARDS.md
- 删除原 Phase 0（强制读 DESIGN_STANDARDS.md）和误导性"零文件读取"快速模板

#### 文件合并

- viewport-base.css（237 行）→ 合并入 html-template.md
- animation-patterns.md（96 行）→ 合并入 html-template.md
- html-template.md 底部重复图表动画脚本 → 删除（已合并到主 script 块）

#### CSS 变量补全

html-template.md `:root` 新增：
- `--radius-xl: 24px`
- `--shadow-elevated: 0 8px 32px rgba(0,0,0,0.12)`
- `--duration-fast: 0.2s`
- `--chart-1` ~ `--chart-5` + `--chart-neutral`（图表色彩令牌）

#### 组件目录补全

新增 4 个组件引用：
- `screenshot-box`（R8 产品文档）
- `image-showcase`（R4 年度总结）
- `trend-indicator`（R2 数据分析）
- `code-block`（R8 产品文档）

#### 对抗性审查修复

- 快速模板空壳问题：CSS 只有占位注释，删除整个骨架
- 缺失 13 个关键 :root 变量（排版/间距）：已补全
- 缺失 animateValue() 函数：已补入 html-template.md
- INFOGRAPHIC_PATTERNS.md 添加 CSS 合并说明

---

### 模板创建

创建 9 个自包含 HTML 模板，每个包含完整 CSS + JS + 占位内容。

#### 滚动报告模板（5 个）

| 文件 | 预设 | 字体 | 行数 |
|------|------|------|------|
| bold-signal.html | Bold Signal | Archivo Black + Space Grotesk | 1256 |
| electric-studio.html | Electric Studio | Manrope + JetBrains Mono | 566 |
| dark-botanical.html | Dark Botanical | Cormorant + IBM Plex Sans | 1843 |
| swiss-modern.html | Swiss Modern | Archivo + Nunito | 1315 |
| paper-ink.html | Paper & Ink | Cormorant Garamond + Source Serif 4 | 1641 |

#### 全屏 PPT 模板（3 个 + 1 个原始）

| 文件 | 预设 | 字体 | 行数 |
|------|------|------|------|
| full-ppt-test.html | 原始参考 | Clash Display + Satoshi | 603 |
| ppt-bold-signal.html | Bold Signal | Archivo Black + Space Grotesk | 483 |
| ppt-electric-studio.html | Electric Studio | Manrope | 481 |
| ppt-dark-botanical.html | Dark Botanical | Cormorant + IBM Plex Sans | 495 |

所有模板特点：
- 单文件自包含，零外部依赖（仅 Google Fonts）
- 包含全部 12 种图表组件 CSS
- 包含 IntersectionObserver 滚动动画 + 图表入场动画
- PPT 模板包含完整的 SlidePresentation 类（键盘/滚轮/触摸导航、进度条、导航点）

---

### 扩展模块

创建 `extensions/INTERACTIVE_PATTERNS.md`（428 行），包含：

- 数据轮询刷新（数值/进度条/环形图动态更新）
- 交互组件（可点击柱状图、Tab 切换、折叠面板）
- 入场动画增强（数字滚动自动触发、打字机效果、翻牌效果）
- 数据可视化增强（实时时间戳、SVG sparkline 动态生成、表格排序）
- PPT 交互扩展（画笔标注、演讲计时器）

---

### 项目文档

- `README.md`：目录结构、使用规范、扩展机制、文件依赖关系

---

## 文件大小对比

| 文件 | 优化前 | 优化后 |
|------|--------|--------|
| SKILL.md | 391 行 | 175 行（-55%） |
| html-template.md | 639 行 | 734 行（+15%，合并了 viewport-base.css + animation-patterns） |
| 模板文件 | 0 个 | 9 个 |
| 扩展文件 | 0 个 | 1 个（428 行） |
| 总文件数 | 7 | 18 |
