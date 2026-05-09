# 设计规范库 — 汇报类型 × 设计选择映射

本文件是 html-report 技能的设计决策中枢。生成任何汇报 HTML 前，必须先根据汇报类型查表，
确定对应的：布局模式、色彩方向、字体配对、组件优先级、信息密度、视觉层级。

---

## 一、汇报类型分类

### 1. 周例会 / 月例会汇报 (Weekly/Monthly Meeting)
**场景**: 团队内部同步，议程驱动，状态追踪
**受众**: 团队成员、直属领导
**核心需求**: 快速扫描、状态识别、待办追踪

| 维度 | 选择 |
|------|------|
| 布局模式 | 单栏滚动 + 分区卡片 |
| 色彩方向 | 深色底 + 强功能色（红/黄/绿状态标识） |
| 字体配对 | 现代无衬线 display + 可读正文 |
| 组件优先级 | status-badge > callout > step-flow > summary-grid > table |
| 信息密度 | 中（每屏 3-5 个信息单元） |
| 视觉层级 | 议题编号 → 议题标题 → 状态/结论 → 详情 |
| 推荐预设 | Bold Signal, Electric Studio |

### 2. 数据分析报告 (Data Analysis Report)
**场景**: 数据驱动决策，趋势展示，KPI 追踪
**受众**: 管理层、业务负责人
**核心需求**: 数据可视化、对比突出、趋势标注

| 维度 | 选择 |
|------|------|
| 布局模式 | 单栏滚动 + 数据卡片网格 + 表格区 |
| 色彩方向 | 深色或极简白底 + 数据强调色（一个主色+对比色） |
| 字体配对 | 等宽数字 + 清晰无衬线正文 |
| 组件优先级 | stat-card > table > trend-indicator > chart-area > summary |
| 信息密度 | 高（每屏 5-8 个数据点） |
| 视觉层级 | KPI 概览 → 分类数据 → 明细表格 → 结论 |
| 推荐预设 | Electric Studio, Swiss Modern |

### 3. 项目提案 / 立项报告 (Project Proposal)
**场景**: 说服决策者，展示愿景与可行性
**受众**: 高管、投资方、决策委员会
**核心需求**: 冲击力、信任感、清晰的路线图

| 维度 | 选择 |
|------|------|
| 布局模式 | 全幅封面 + 分区滚动 + 强调区块 |
| 色彩方向 | 深色高级感 或 品牌色主导 |
| 字体配对 | 强展示字 display + 优雅正文 |
| 组件优先级 | hero-cover > stat-card > step-flow > callout > table |
| 信息密度 | 低-中（每屏 2-3 个核心信息） |
| 视觉层级 | 愿景 → 问题 → 方案 → 路线图 → 团队/资源 |
| 推荐预设 | Dark Botanical, Bold Signal |

### 4. 年度总结报告 (Annual Summary)
**场景**: 全面回顾，里程碑展示，数据汇总
**受众**: 全员或管理层
**核心需求**: 叙事感、成就感、数据支撑

| 维度 | 选择 |
|------|------|
| 布局模式 | 分区长卷 + 时间线 + 数据亮点 |
| 色彩方向 | 温暖或稳重色调（金色、暖灰、品牌色） |
| 字体配对 | 优雅衬体标题 + 清晰无衬线正文 |
| 组件优先级 | stat-card > timeline > image-showcase > summary-grid > table |
| 信息密度 | 中-高（丰富但不拥挤） |
| 视觉层级 | 年度数字 → 里程碑时间线 → 分类成果 → 展望 |
| 推荐预设 | Dark Botanical, Vintage Editorial, Paper & Ink |

### 5. 竞品分析报告 (Competitive Analysis)
**场景**: 横向对比，优劣势分析
**受众**: 产品团队、战略部门
**核心需求**: 对比表格、维度评分、差异标注

| 维度 | 选择 |
|------|------|
| 布局模式 | 对比表格区 + 维度分析卡片 |
| 色彩方向 | 专业中性色 + 对比高亮色 |
| 字体配对 | 清晰无衬线（确保表格可读） |
| 组件优先级 | comparison-table > score-card > summary > callout |
| 信息密度 | 高（表格承载大量对比数据） |
| 视觉层级 | 总览结论 → 分维度对比 → 详细表格 → 建议 |
| 推荐预设 | Swiss Modern, Electric Studio |

### 6. 调研报告 / 研究文档 (Research Report)
**场景**: 深度分析，文献综述，方法论展示
**受众**: 专业读者、同行
**核心需求**: 文本舒适、层次清晰、引用规范

| 维度 | 选择 |
|------|------|
| 布局模式 | 单栏阅读优化 + 侧边目录 |
| 色彩方向 | 暖白/奶油底 + 低调学术强调色 |
| 字体配对 | 衬体正文 + 无衬线标题（或全衬体） |
| 组件优先级 | toc > section-heading > quote-block > table > footnote |
| 信息密度 | 低-中（以阅读舒适度为优先） |
| 视觉层级 | 摘要 → 目录 → 章节正文 → 结论 → 参考 |
| 推荐预设 | Paper & Ink, Notebook Tabs |

### 7. 执行摘要 / 一页纸报告 (Executive Summary)
**场景**: 高层快速决策，关键信息浓缩
**受众**: C-level，时间极度有限
**核心需求**: 一屏概览、结论先行、行动清晰

| 维度 | 选择 |
|------|------|
| 布局模式 | 单页分区（A4 比例优化） |
| 色彩方向 | 极简白或深色高级感 |
| 字体配对 | 强 display + 极致简洁正文 |
| 组件优先级 | big-number > callout > summary-grid > action-items |
| 信息密度 | 低（只保留决策关键信息） |
| 视觉层级 | 核心结论 → 关键数字 → 风险/机会 → 待决策项 |
| 推荐预设 | Swiss Modern, Bold Signal |

### 8. 产品文档 / 操作手册 (Product Documentation)
**场景**: 功能说明、操作步骤、FAQ
**受众**: 终端用户或运营人员
**核心需求**: 步骤清晰、易扫描、代码/截图嵌入

| 维度 | 选择 |
|------|------|
| 布局模式 | 单栏 + 侧边锚点导航 |
| 色彩方向 | 浅色干净底 + 功能色（蓝=信息，绿=成功） |
| 字体配对 | 高可读性无衬线 + 等宽代码 |
| 组件优先级 | step-flow > code-block > screenshot-box > callout-info > table |
| 信息密度 | 中（按步骤分布） |
| 视觉层级 | 概述 → 前置条件 → 操作步骤 → FAQ |
| 推荐预设 | Swiss Modern, Notebook Tabs |

---

## 二、布局模式库

### L1: 单栏阅读流 (Single Column Flow)
- 内容居中线宽 `max-width: min(90vw, 800px)`
- 章节间大间距分隔
- 适用于：调研报告、产品文档、执行摘要

### L2: 分区卡片流 (Section Card Flow)
- 每个章节为独立卡片，深色/浅色区分
- 卡片间交替背景或微阴影
- 适用于：周例会、数据分析、年度总结

### L3: 全幅区块流 (Full-width Block Flow)
- 每个章节全幅背景（可交替色）
- 内容区居中限宽
- 适用于：项目提案、年度总结

### L4: 对比网格流 (Comparison Grid)
- 多列对比布局
- 表头固定可滚动
- 适用于：竞品分析、数据对比

### L5: 一页仪表盘 (One-Page Dashboard)
- 所有内容压缩到一屏
- 网格分区，无滚动
- 适用于：执行摘要

---

## 三、色彩语义规范

| 语义 | 色域 | Hex 示例 |
|------|------|----------|
| 强调/主色 | 品牌橙、电蓝、深绿 | #ff6b00, #4361ee, #0d9488 |
| 成功/正向 | 绿色系 | #2ed573, #10b981 |
| 警告/注意 | 琥珀/黄色系 | #ffa502, #f59e0b |
| 危险/紧急 | 红色系 | #ff4757, #ef4444 |
| 信息/说明 | 蓝色系 | #3498db, #3b82f6 |
| 中性/正文 | 灰阶 | #b0b0b0, #6b7280 |
| 背景深色 | 暗色阶 | #0d0d0d, #1a1a1a, #1f1f1f |
| 背景浅色 | 暖白/冷白 | #faf9f7, #f8f6f1, #ffffff |

---

## 四、字体配对规范

| 场景 | 标题字体 | 正文字体 | 数字字体 | 来源 |
|------|----------|----------|----------|------|
| 现代商务 | Archivo Black | Space Grotesk | Space Grotesk | Google |
| 科技/数据 | Clash Display | Satoshi | JetBrains Mono | Fontshare/Google |
| 优雅正式 | Cormorant | IBM Plex Sans | IBM Plex Sans | Google |
| 编辑/阅读 | Bodoni Moda | DM Sans | DM Sans | Google |
| 极简/瑞士 | Archivo | Nunito | Nunito | Google |
| 中文汇报 | Noto Sans SC (标题) | Noto Sans SC (正文) | — | Google |
| 温暖人文 | Fraunces | Work Sans | Work Sans | Google |
| 活泼友好 | Outfit | Outfit | Outfit | Google |
| 开发者向 | JetBrains Mono | JetBrains Mono | JetBrains Mono | JetBrains |

**中文混排原则**: 西文 display 字体 + Noto Sans SC 回退，确保中文不出现缺字。

---

## 五、组件设计令牌

每个组件必须使用以下 CSS 变量，确保全局一致性：

```css
:root {
    /* 间距体系 */
    --space-xs: clamp(0.25rem, 0.5vw, 0.5rem);
    --space-sm: clamp(0.5rem, 1vw, 0.75rem);
    --space-md: clamp(0.75rem, 1.5vw, 1.25rem);
    --space-lg: clamp(1rem, 2vw, 2rem);
    --space-xl: clamp(2rem, 4vw, 4rem);

    /* 圆角体系 */
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 16px;
    --radius-xl: 24px;

    /* 阴影体系 */
    --shadow-card: 0 2px 8px rgba(0,0,0,0.08);
    --shadow-elevated: 0 8px 32px rgba(0,0,0,0.12);

    /* 过渡 */
    --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
    --duration-fast: 0.2s;
    --duration-normal: 0.4s;
}
```

---

## 六、信息图表与数据可视化规范

详见 [INFOGRAPHIC_PATTERNS.md](INFOGRAPHIC_PATTERNS.md)，包含 15 种纯 CSS 图表的完整实现。

### 图表选择速查

| 数据类型 | 推荐图表 | CSS 实现 |
|----------|----------|----------|
| 类别对比（3-8项） | 水平/垂直柱状图 | flexbox + width/height % |
| 占比分布（2-5项） | 环形图 (Donut) | conic-gradient + mask |
| 时间趋势（5-20点） | Sparkline | SVG polyline |
| 进度/达成率 | 进度条 | width % + transition |
| 目标 vs 实际 | 子弹图 (Bullet) | 叠加定位 div |
| 多项评分矩阵 | 热力网格 (Heatmap) | CSS grid + color-mix |
| 里程碑/事件序列 | 时间线 (Timeline) | ::before 竖线 + 定位圆点 |
| 构成分解 | 堆叠柱状图 | flex 嵌套 div |
| 累积变化 | 瀑布图 (Waterfall) | flex-end 对齐 + margin-top 偏移 |
| 多维度 KPI 概览 | 仪表盘网格 | CSS grid 混合卡片 |

### 图表色彩令牌

```css
:root {
    /* 图表专用色（语义色基础上扩展） */
    --chart-1: var(--accent);        /* 主数据色 */
    --chart-2: var(--info);          /* 第二数据色 */
    --chart-3: var(--warning);       /* 第三数据色 */
    --chart-4: var(--success);       /* 第四数据色 */
    --chart-5: #e056a0;              /* 扩展色 */
    --chart-neutral: var(--bg-card); /* 剩余/背景 */
}
```

### 数据绑定原则

所有图表数据通过内联 `style` 属性绑定，零 JS 运行时计算：

| 图表 | 绑定方式 |
|------|----------|
| Bar | `style="width: 73%;"` 或 `style="height: 85%;"` |
| Donut | `style="--donut-pct: 73;"` |
| Progress | `style="width: 85%;"` |
| Heatmap | `style="--hm-intensity: 0.7;"` |
| Bullet | `style="width: 73%;"` + `style="left: 80%;"` |
