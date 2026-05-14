# HTML Report Skill

零依赖、单文件、浏览器即开即用的汇报类 HTML 页面生成器。

> **AI Agent 请读取 [SKILL.md](SKILL.md)** — 包含完整工作流、模板速查、设计约束。

## 目录结构

```
html-report/
├── SKILL.md                    # 技能入口（AI 读取此文件启动工作流）
├── README.md                   # 本文件 — 人类阅读的项目说明
│
├── templates/                  # 预设模板（极速路径，直接复制替换内容）
│   ├── bold-signal.html        # 深色+橙 · 周例会/提案/摘要
│   ├── electric-studio.html    # 深色+蓝 · 数据分析/竞品
│   ├── dark-botanical.html     # 深色+金 · 年度总结/提案
│   ├── swiss-modern.html       # 白底+红 · 执行摘要/产品文档
│   ├── paper-ink.html          # 暖白+红 · 调研报告/文学风
│   ├── gallery-data.html       # 白底极简 · 数据分析/KPI仪表盘
│   ├── ledger-slate.html       # 暖白财务 · 财务报表/P&L/资产负债表
│   ├── sketch-watercolor.html  # 水彩手绘 · 创意报告/艺术风格
│   ├── full-ppt-test.html      # 全屏PPT · 深色+橙（原始参考）
│   ├── ppt-bold-signal.html    # 全屏PPT · 深色+橙
│   ├── ppt-electric-studio.html# 全屏PPT · 深色+蓝
│   └── ppt-dark-botanical.html # 全屏PPT · 深色+金
│
├── html-template.md            # 标准路径：完整 CSS/JS 参考架构
├── DESIGN_STANDARDS.md         # 设计规范库：类型→设计映射
├── STYLE_PRESETS.md            # 12 套视觉预设完整 CSS
├── INFOGRAPHIC_PATTERNS.md     # 图表使用指南 + HTML 示例
│
├── extensions/                 # 扩展模块（按需引入）
│   └── INTERACTIVE_PATTERNS.md # 动态图表、交互动画、数据可视化扩展
│
└── data-analysis/              # 数据驱动报告子技能
    ├── SKILL.md                # 子技能入口
    ├── README.md               # 使用说明
    ├── scripts/                # Python 脚本
    │   ├── generate_report.py  # 主脚本：读取数据 → 计算指标 → 生成 HTML
    │   └── category_mapper.py  # 品类映射引擎
    ├── tests/                  # 单元测试
    │   ├── test_category_mapper.py
    │   └── test_generate_report.py
    ├── styles/                 # 外置 CSS
    │   └── base.css
    └── config/                 # 配置模板
        └── template.yaml       # 配置模板（修改后使用）
```

## 自定义方式

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

## 数据驱动路径

当有现成的 Excel 数据文件时，使用此路径：

```bash
# 安装依赖
pip install pandas openpyxl pyyaml

# 复制并修改配置
cp data-analysis/config/template.yaml my-config.yaml

# 生成报告
python3 data-analysis/scripts/generate_report.py --config my-config.yaml
```

**环境变量支持：**
- `REPORT_CONFIG`: 配置文件路径（优先级：--config 参数 > 环境变量 > 默认 config.yaml）

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

## 开发指南

### 运行测试

```bash
cd data-analysis
python3 tests/test_category_mapper.py
python3 tests/test_generate_report.py
```

### 文件依赖关系

```
SKILL.md（AI 入口）
  ├── templates/*.html（极速路径，直接用）
  ├── html-template.md（标准路径，完整 CSS/JS）
  ├── INFOGRAPHIC_PATTERNS.md（图表选型指导）
  ├── STYLE_PRESETS.md（预设详情）
  ├── DESIGN_STANDARDS.md（完整设计规范）
  ├── extensions/INTERACTIVE_PATTERNS.md（扩展：动态图表/交互）
  └── data-analysis/（数据驱动路径）
        ├── SKILL.md（子技能入口）
        ├── scripts/generate_report.py（主脚本）
        ├── scripts/category_mapper.py（品类映射引擎）
        ├── styles/base.css（外置 CSS）
        ├── tests/（单元测试）
        └── config/template.yaml（配置模板）
```
