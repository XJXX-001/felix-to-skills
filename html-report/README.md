# HTML Report Skill

零依赖、单文件、浏览器即开即用的汇报类 HTML 页面生成器。

## 目录结构

```
html-report/
├── SKILL.md                    # 技能入口（Hermes 读取此文件启动工作流）
├── README.md                   # 本文件 — 项目说明与使用规范
│
├── templates/                  # 预设模板（极速路径，直接复制替换内容）
│   ├── bold-signal.html        # 深色+橙 · 周例会/提案/摘要
│   ├── electric-studio.html    # 深色+蓝 · 数据分析/竞品
│   ├── dark-botanical.html     # 深色+金 · 年度总结/提案
│   ├── swiss-modern.html       # 白底+红 · 执行摘要/产品文档
│   ├── paper-ink.html          # 暖白+红 · 调研报告/文学风
│   ├── full-ppt-test.html      # 全屏PPT · 深色+橙（原始参考）
│   ├── ppt-bold-signal.html    # 全屏PPT · 深色+橙
│   ├── ppt-electric-studio.html# 全屏PPT · 深色+蓝
│   └── ppt-dark-botanical.html # 全屏PPT · 深色+金
│
├── html-template.md            # 标准路径：完整 CSS/JS 参考架构
├── DESIGN_STANDARDS.md         # 设计规范库：类型→设计映射
├── STYLE_PRESETS.md            # 12 套视觉预设完整 CSS
├── INFOGRAPHIC_PATTERNS.md     # 图表使用指南 + HTML 示例
├── animation-patterns.md       # 动画参考（已合并入 html-template.md）
├── viewport-base.css           # 响应式基座 CSS（已合并入 html-template.md）
│
└── extensions/                 # 扩展模块（按需引入）
    └── INTERACTIVE_PATTERNS.md # 动态图表、交互动画、数据可视化扩展
```

## 使用规范

### 工作流选择

| 场景 | 推荐路径 | 文件读取 | 速度 |
|------|----------|----------|------|
| 用户催促 / demo / 简单报告 | 极速路径 | 读 1 个模板文件 | 最快 |
| 大多数报告 | 标准路径 | 读 html-template.md | 快 |
| 数据密集 / 需要图表指导 | 复杂路径 | 读 html-template.md + 按需读其余 | 中 |
| 需要动态图表/交互 | 扩展路径 | 标准路径 + 读 extensions/ | 按需 |

### 模板使用方式

1. 根据报告类型从 SKILL.md 速查表选模板
2. 读取模板文件，获取完整 CSS + HTML 结构
3. 替换占位内容为实际报告内容
4. 保存为 `{type}-{date-or-topic}.html`

### 自定义方式

- **换色**: 修改 `:root` 中的 `--accent`、`--bg-primary` 等变量
- **换字体**: 修改 `<link>` 标签中的字体名 + `--font-display`、`--font-body` 变量
- **增减组件**: 从 html-template.md 中选取需要的组件 CSS

### CSS 变量体系

所有样式通过 `:root` 变量控制，修改一处即可全局换肤：

```css
:root {
    --bg-primary: #0a0a0a;     /* 主背景 */
    --bg-card: #141414;        /* 卡片背景 */
    --accent: #4361ee;         /* 强调色 */
    --font-display: 'Manrope'; /* 标题字体 */
    --font-body: 'Manrope';    /* 正文字体 */
}
```

## 扩展机制

本技能预留了扩展空间，详见 `extensions/` 目录：

| 扩展文件 | 用途 | 引入时机 |
|----------|------|----------|
| `INTERACTIVE_PATTERNS.md` | 动态图表、交互动画、数据刷新 | 用户需要动态/可交互图表时 |

扩展文件遵循与主技能相同的设计原则：
- 零外部依赖（图表库、动画库内联）
- CSS 变量驱动
- 响应式兼容
- 尊重 `prefers-reduced-motion`

## 设计约束

- 禁止 Inter/Roboto/Arial 作为 display 字体
- 禁止紫色渐变白底（`#6366f1`）
- 禁止全内容居中对齐（封面除外）
- 字号必须 `clamp()`，禁止固定 px
- 负值必须 `calc(-1 * ...)`，禁止 `-clamp()`

## 文件依赖关系

```
SKILL.md（入口）
  ├── templates/*.html（极速路径，直接用）
  ├── html-template.md（标准路径，完整 CSS/JS）
  │     ├── 已内含 viewport-base.css（响应式基座）
  │     └── 已内含 animation-patterns.md（动画）
  ├── INFOGRAPHIC_PATTERNS.md（图表选型指导）
  ├── STYLE_PRESETS.md（预设详情）
  ├── DESIGN_STANDARDS.md（完整设计规范）
  └── extensions/INTERACTIVE_PATTERNS.md（扩展：动态图表/交互）
```
