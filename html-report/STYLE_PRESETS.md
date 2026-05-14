# Style Presets Reference

12 套视觉预设，每套包含完整的设计令牌。生成报告时从中选择。
**仅使用抽象形状，不使用插图。**

## Dark Themes

### 1. Bold Signal
**氛围**: 自信、高冲击力、现代
**适用**: 周例会、项目提案、执行摘要

```css
:root {
    --bg-primary: #1a1a1a;
    --bg-card: #2d2d2d;
    --bg-section-alt: #222222;
    --text-primary: #ffffff;
    --text-secondary: #b0b0b0;
    --accent: #FF5722;
    --accent-glow: rgba(255, 87, 34, 0.3);
    --font-display: 'Archivo Black', 'Noto Sans SC', sans-serif;
    --font-body: 'Space Grotesk', 'Noto Sans SC', sans-serif;
    --font-mono: 'Space Grotesk', monospace;
}
```
**特征**: 彩色卡片焦点、大号章节编号、网格对齐

### 2. Electric Studio
**氛围**: 干净、专业、高对比
**适用**: 数据分析、竞品分析

```css
:root {
    --bg-primary: #0a0a0a;
    --bg-card: #141414;
    --bg-section-alt: #1a1a1a;
    --text-primary: #ffffff;
    --text-secondary: #9ca3af;
    --accent: #4361ee;
    --accent-secondary: #7209b7;
    --font-display: 'Manrope', 'Noto Sans SC', sans-serif;
    --font-body: 'Manrope', 'Noto Sans SC', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}
```
**特征**: 分区面板、强调色条、数据友好

### 3. Dark Botanical
**氛围**: 优雅、精致、高级感
**适用**: 年度总结、项目提案

```css
:root {
    --bg-primary: #0f0f0f;
    --bg-card: #1a1a1a;
    --bg-section-alt: #141414;
    --text-primary: #e8e4df;
    --text-secondary: #9a9590;
    --accent: #d4a574;
    --accent-pink: #e8b4b8;
    --accent-gold: #c9b896;
    --font-display: 'Cormorant', 'Noto Serif SC', serif;
    --font-body: 'IBM Plex Sans', 'Noto Sans SC', sans-serif;
    --font-mono: 'IBM Plex Mono', monospace;
}
```
**特征**: 抽象柔和渐变圆、暖色点缀、竖线分隔

### 4. Neon Cyber
**氛围**: 未来感、科技风
**适用**: 技术提案、数据看板

```css
:root {
    --bg-primary: #0a0f1c;
    --bg-card: #111827;
    --bg-section-alt: #0f1729;
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --accent: #00ffcc;
    --accent-secondary: #ff00aa;
    --font-display: 'Clash Display', 'Noto Sans SC', sans-serif;
    --font-body: 'Satoshi', 'Noto Sans SC', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}
```
**特征**: 霓虹发光、网格背景、粒子效果（可选）

---

## Light Themes

### 5. Gallery Data
**氛围**: 白底极简、数据画廊、学术感
**适用**: 数据分析、KPI 仪表盘、可视化报告

```css
:root {
    --bg-primary: #ffffff;
    --bg-card: #ffffff;
    --bg-section-alt: #f8f9fa;
    --text-primary: #111111;
    --text-secondary: #4a4a4a;
    --accent: #4263eb;
    --accent-glow: rgba(66, 99, 235, 0.08);
    --font-display: 'Inter', 'Noto Sans SC', sans-serif;
    --font-body: 'Inter', 'Noto Sans SC', sans-serif;
    --font-data: 'Lora', 'Noto Serif SC', serif;
    --font-mono: 'JetBrains Mono', monospace;
}
```
**特征**: Lora 衬线数字、无品牌色（颜色仅来自数据）、极简 1px 边框、4px 圆角、大量留白

### 6. Ledger Slate
**氛围**: 暖白纸张、财务专业、信任感
**适用**: 财务报表、利润表、资产负债表、现金流分析

```css
:root {
    --bg-primary: #fcfcf9;
    --bg-card: #ffffff;
    --bg-section-alt: #f7f6f3;
    --text-primary: #1a1a1a;
    --text-secondary: #3d3d3d;
    --accent: #4ade80;
    --accent-deep: #22c55e;
    --font-display: 'DM Sans', 'Noto Sans SC', sans-serif;
    --font-body: 'DM Sans', 'Noto Sans SC', sans-serif;
    --font-finance: 'Playfair Display', 'Noto Serif SC', serif;
    --font-mono: 'JetBrains Mono', monospace;
}
```
**特征**: Playfair Display 衬线财务数字、12px 统一圆角、双划线总计行、正负行着色、暖灰中性色

### 7. Swiss Modern
**氛围**: 极简、精确、包豪斯
**适用**: 执行摘要、产品文档、竞品分析

```css
:root {
    --bg-primary: #ffffff;
    --bg-card: #f5f5f5;
    --bg-section-alt: #fafafa;
    --text-primary: #1a1a1a;
    --text-secondary: #666666;
    --accent: #ff3300;
    --accent-secondary: #000000;
    --font-display: 'Archivo', 'Noto Sans SC', sans-serif;
    --font-body: 'Nunito', 'Noto Sans SC', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}
```
**特征**: 可见网格、非对称布局、几何形状

### 8. Notebook Tabs
**氛围**: 编辑感、有条理、有温度
**适用**: 调研报告、产品文档

```css
:root {
    --bg-primary: #2d2d2d;
    --bg-card: #f8f6f1;
    --bg-section-alt: #f0ede6;
    --text-primary: #1a1a1a;
    --text-secondary: #555555;
    --accent: #98d4bb;
    --tab-mint: #98d4bb;
    --tab-lavender: #c7b8ea;
    --tab-pink: #f4b8c5;
    --tab-sky: #a8d8ea;
    --font-display: 'Bodoni Moda', 'Noto Serif SC', serif;
    --font-body: 'DM Sans', 'Noto Sans SC', sans-serif;
    --font-mono: 'DM Mono', monospace;
}
```
**特征**: 纸质卡片、彩色侧标签、装订孔装饰

### 9. Paper & Ink
**氛围**: 文学感、深度、思考
**适用**: 调研报告、年度总结

```css
:root {
    --bg-primary: #faf9f7;
    --bg-card: #ffffff;
    --bg-section-alt: #f5f2ed;
    --text-primary: #1a1a1a;
    --text-secondary: #4a4a4a;
    --accent: #c41e3a;
    --accent-secondary: #2a2a2a;
    --font-display: 'Cormorant Garamond', 'Noto Serif SC', serif;
    --font-body: 'Source Serif 4', 'Noto Serif SC', serif;
    --font-mono: 'Source Code Pro', monospace;
}
```
**特征**: 首字下沉、引用块、优雅水平线

### 10. Vintage Editorial
**氛围**: 个性、编辑风、有态度
**适用**: 年度总结、项目提案

```css
:root {
    --bg-primary: #f5f3ee;
    --bg-card: #ffffff;
    --bg-section-alt: #ede8e0;
    --text-primary: #1a1a1a;
    --text-secondary: #555555;
    --accent: #e8d4c0;
    --accent-secondary: #c4a882;
    --font-display: 'Fraunces', 'Noto Serif SC', serif;
    --font-body: 'Work Sans', 'Noto Sans SC', sans-serif;
    --font-mono: 'Space Mono', monospace;
}
```
**特征**: 几何抽象形状、粗边框 CTA、个性排版

---

## Specialty Themes

### 11. Terminal Green
**氛围**: 开发者向、极客风
**适用**: 技术文档、数据分析

```css
:root {
    --bg-primary: #0d1117;
    --bg-card: #161b22;
    --bg-section-alt: #12171e;
    --text-primary: #e6edf3;
    --text-secondary: #8b949e;
    --accent: #39d353;
    --accent-secondary: #58a6ff;
    --font-display: 'JetBrains Mono', 'Noto Sans SC', monospace;
    --font-body: 'JetBrains Mono', 'Noto Sans SC', monospace;
    --font-mono: 'JetBrains Mono', monospace;
}
```
**特征**: 扫描线、闪烁光标、代码语法风格

### 12. Creative Voltage
**氛围**: 大胆、创意、有活力
**适用**: 项目提案、创意报告

```css
:root {
    --bg-primary: #0066ff;
    --bg-card: #1a1a2e;
    --bg-section-alt: #112255;
    --text-primary: #ffffff;
    --text-secondary: #b0c4ff;
    --accent: #d4ff00;
    --accent-secondary: #00ffff;
    --font-display: 'Syne', 'Noto Sans SC', sans-serif;
    --font-body: 'Space Mono', 'Noto Sans SC', sans-serif;
    --font-mono: 'Space Mono', monospace;
}
```
**特征**: 电蓝+霓虹黄对比、半色调纹理、霓虹标签

### 13. Split Pastel
**氛围**: 活泼、友好、现代
**适用**: 内部汇报、团队文档

```css
:root {
    --bg-primary: #f5e6dc;
    --bg-card: #ffffff;
    --bg-section-alt: #e4dff0;
    --text-primary: #1a1a1a;
    --text-secondary: #555555;
    --accent: #c8f0d8;
    --accent-secondary: #f0f0c8;
    --accent-pink: #f0d4e0;
    --font-display: 'Outfit', 'Noto Sans SC', sans-serif;
    --font-body: 'Outfit', 'Noto Sans SC', sans-serif;
    --font-mono: 'Space Mono', monospace;
}
```
**特征**: 双色分屏背景、趣味徽章、网格叠加

### 14. Pastel Geometry
**氛围**: 有条理、友好、现代
**适用**: 周例会、数据分析（轻量）

```css
:root {
    --bg-primary: #c8d9e6;
    --bg-card: #faf9f7;
    --bg-section-alt: #dce6f0;
    --text-primary: #1a1a1a;
    --text-secondary: #555555;
    --accent: #f0b4d4;
    --accent-secondary: #a8d4c4;
    --accent-dark: #5a7c6a;
    --font-display: 'Plus Jakarta Sans', 'Noto Sans SC', sans-serif;
    --font-body: 'Plus Jakarta Sans', 'Noto Sans SC', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}
```
**特征**: 圆角卡片、垂直侧边 pill、柔和阴影

### 15. Sketch Watercolor
**氛围**: 手绘、温暖、非正式、亲切
**适用**: 内部周报、创意提案、团队复盘、手绘风信息图

```css
:root {
    --paper: #faf8f3;
    --ink: #2d2d2d;
    --ink-light: #5a5a5a;
    --wc-blue: #7eb8da;
    --wc-blue-deep: #5a9fd4;
    --wc-blue-light: #b8d9f0;
    --wc-orange: #f4a261;
    --wc-orange-deep: #e76f51;
    --wc-orange-light: #fcd5b5;
    --wc-green: #90c6a1;
    --marker-yellow: rgba(255, 234, 150, 0.45);
    --hand-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    --font-display: 'ZCOOL KuaiLe', 'Patrick Hand', cursive;
    --font-body: 'ZCOOL KuaiLe', 'Noto Sans SC', cursive;
    --font-hand: 'Patrick Hand', 'Ma Shan Zheng', cursive;
}
```
**特征**: 不规则圆角手绘卡片、马克笔高亮标题、水彩晕染渐变背景、胶带标签、便签小卡、黑板结论条。SVG 噪点纸张纹理，CSS 手绘箭头，hover 微旋转。需配合完整组件库（sketch-card / sketch-node / sketch-note / sketch-badge / sketch-conclusion 等），详见 `templates/sketch-watercolor.html`。

---

## 字体来源速查

| 预设 | Display | Body | 来源 |
|------|---------|------|------|
| Bold Signal | Archivo Black | Space Grotesk | Google Fonts |
| Electric Studio | Manrope | Manrope | Google Fonts |
| Gallery Data | Inter | Lora (数字) | Google Fonts |
| Ledger Slate | DM Sans | Playfair Display (财务数字) | Google Fonts |
| Dark Botanical | Cormorant | IBM Plex Sans | Google Fonts |
| Neon Cyber | Clash Display | Satoshi | Fontshare |
| Swiss Modern | Archivo | Nunito | Google Fonts |
| Notebook Tabs | Bodoni Moda | DM Sans | Google Fonts |
| Paper & Ink | Cormorant Garamond | Source Serif 4 | Google Fonts |
| Vintage Editorial | Fraunces | Work Sans | Google Fonts |
| Terminal Green | JetBrains Mono | JetBrains Mono | JetBrains |
| Creative Voltage | Syne | Space Mono | Google Fonts |
| Split Pastel | Outfit | Outfit | Google Fonts |
| Pastel Geometry | Plus Jakarta Sans | Plus Jakarta Sans | Google Fonts |
| Sketch Watercolor | ZCOOL KuaiLe | ZCOOL KuaiLe + Patrick Hand | Google Fonts |

---

## CSS 陷阱

### 否定 CSS 函数

**错误 — 浏览器静默忽略：**
```css
right: -clamp(28px, 3.5vw, 44px);
margin-left: -min(10vw, 100px);
```

**正确 — 用 calc() 包裹：**
```css
right: calc(-1 * clamp(28px, 3.5vw, 44px));
margin-left: calc(-1 * min(10vw, 100px));
```
