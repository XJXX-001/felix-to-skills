# Information Design Patterns

纯 CSS 信息图表组件库。零 JS 依赖（除动画触发），所有图表由 CSS flexbox/grid/conic-gradient/SVG 实现。
生成数据报告时，从此库中选择匹配的图表类型。

> **注意**: 所有图表的 CSS 定义已整合到 [html-template.md](html-template.md) 中。本文件主要用于：
> - 查阅图表选择指南（哪种数据用哪种图表）
> - 参考 HTML 用法示例
> - 了解数据绑定方式
>
> 生成报告时，**只需读取 html-template.md** 即可获得完整 CSS。

## 核心原则

1. **数据先行** — 图表服务于数据理解，装饰不喧宾夺主
2. **纯 CSS** — 无 Chart.js / D3 / Canvas，确保零依赖
3. **CSS 变量驱动** — 所有数据尺寸、颜色通过 CSS 变量和内联 style 绑定
4. **响应式** — 所有图表在移动端可读（flex-wrap、min-width）
5. **语义色** — 复用 `:root` 中的 `--success/warning/danger/info/accent`

---

## 图表选择指南

| 数据类型 | 推荐图表 | 不推荐 |
|----------|----------|--------|
| 类别对比（3-8项） | Bar Chart (水平/垂直) | Pie（项数多难读） |
| 占比分布（2-5项） | Donut/Ring Chart | Bar（看不出整体关系） |
| 时间趋势（5-20点） | Sparkline | Bar（太占空间） |
| 进度/达成率 | Progress Bar | Donut（单值浪费空间） |
| 目标vs实际 | Bullet Chart | 两个独立 Bar |
| 多项评分对比 | Heatmap Grid | Radar（CSS 难实现） |
| 里程碑/事件序列 | Timeline | Bar（无时间方向感） |
| 构成分解 | Stacked Bar | 多个独立 Bar |
| 累积变化 | Waterfall Chart | 普通 Bar（看不出增量） |
| 多维度 KPI 概览 | Dashboard Grid | 单项罗列 |

---

## 一、Bar Chart（柱状图）

### 1A. 垂直柱状图

**适用**: 类别对比、排名展示
**数据限制**: 3-8 项，标签不长

```html
<div class="chart-bar-vertical">
    <div class="bar-item">
        <div class="bar-value" style="height: 85%; --bar-color: var(--accent);">85%</div>
        <div class="bar-label">类别A</div>
    </div>
    <div class="bar-item">
        <div class="bar-value" style="height: 62%; --bar-color: var(--info);">62%</div>
        <div class="bar-label">类别B</div>
    </div>
    <!-- more items... -->
</div>
```

```css
.chart-bar-vertical {
    display: flex;
    align-items: flex-end;
    justify-content: space-around;
    gap: var(--space-md);
    height: clamp(200px, 40vh, 350px);
    padding: var(--space-md) 0;
    border-bottom: 1px solid rgba(128,128,128,0.2);
}
.bar-item {
    flex: 1;
    max-width: 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-xs);
    height: 100%;
    justify-content: flex-end;
}
.bar-value {
    width: 100%;
    background: var(--bar-color, var(--accent));
    border-radius: var(--radius-sm) var(--radius-sm) 0 0;
    min-height: 4px;
    transition: height 0.8s var(--ease-out-expo);
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding-top: var(--space-xs);
    font-size: var(--caption-size);
    font-weight: 600;
    color: white;
    /* 柱太短时数字移外面：用 JS 或 min-height 保证可读 */
}
.bar-label {
    font-size: var(--caption-size);
    color: var(--text-secondary);
    text-align: center;
    white-space: nowrap;
}
```

### 1B. 水平柱状图

**适用**: 标签较长的类别对比、排行榜

```html
<div class="chart-bar-horizontal">
    <div class="hbar-item">
        <div class="hbar-label">平台A</div>
        <div class="hbar-track">
            <div class="hbar-fill" style="width: 92%; --bar-color: var(--accent);"></div>
        </div>
        <div class="hbar-value">92%</div>
    </div>
    <!-- more... -->
</div>
```

```css
.chart-bar-horizontal {
    display: flex;
    flex-direction: column;
    gap: var(--space-sm);
}
.hbar-item {
    display: flex;
    align-items: center;
    gap: var(--space-sm);
}
.hbar-label {
    width: clamp(60px, 15vw, 120px);
    font-size: var(--small-size);
    color: var(--text-secondary);
    text-align: right;
    flex-shrink: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.hbar-track {
    flex: 1;
    height: clamp(16px, 2.5vh, 24px);
    background: var(--bg-card);
    border-radius: var(--radius-sm);
    overflow: hidden;
}
.hbar-fill {
    height: 100%;
    background: var(--bar-color, var(--accent));
    border-radius: var(--radius-sm);
    transition: width 0.8s var(--ease-out-expo);
    min-width: 4px;
}
.hbar-value {
    width: 3rem;
    font-size: var(--small-size);
    font-weight: 600;
    color: var(--text-primary);
    text-align: left;
}
```

### 1C. 堆叠柱状图

**适用**: 构成分解（如「各平台 = 自营+第三方」）

```html
<div class="chart-bar-stacked">
    <div class="sbar-item">
        <div class="sbar-label">平台A</div>
        <div class="sbar-track">
            <div class="sbar-segment" style="width: 60%; --seg-color: var(--accent);"></div>
            <div class="sbar-segment" style="width: 25%; --seg-color: var(--info);"></div>
            <div class="sbar-segment" style="width: 15%; --seg-color: var(--warning);"></div>
        </div>
    </div>
</div>
```

```css
.chart-bar-stacked { display: flex; flex-direction: column; gap: var(--space-sm); }
.sbar-item { display: flex; align-items: center; gap: var(--space-sm); }
.sbar-label { width: clamp(60px, 15vw, 120px); font-size: var(--small-size); color: var(--text-secondary); text-align: right; flex-shrink: 0; }
.sbar-track { flex: 1; height: clamp(20px, 3vh, 28px); background: var(--bg-card); border-radius: var(--radius-sm); overflow: hidden; display: flex; }
.sbar-segment { height: 100%; background: var(--seg-color); transition: width 0.8s var(--ease-out-expo); }
.sbar-segment:first-child { border-radius: var(--radius-sm) 0 0 var(--radius-sm); }
.sbar-segment:last-child { border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }
```

---

## 二、Donut / Ring Chart（环形图）

**适用**: 占比分布（2-5 项）、完成率
**核心**: `conic-gradient()`

### 单值环形图（完成率）

```html
<div class="chart-donut" style="--donut-pct: 73;">
    <div class="donut-center">
        <span class="donut-value">73%</span>
        <span class="donut-label">目标完成率</span>
    </div>
</div>
```

```css
.chart-donut {
    --donut-pct: 0;
    --donut-size: clamp(120px, 25vw, 200px);
    --donut-thickness: clamp(10px, 2vw, 16px);
    width: var(--donut-size);
    height: var(--donut-size);
    border-radius: 50%;
    background: conic-gradient(
        var(--accent) calc(var(--donut-pct) * 1%),
        var(--bg-card) calc(var(--donut-pct) * 1%)
    );
    /* 中间挖空 */
    mask: radial-gradient(
        circle,
        transparent calc(50% - var(--donut-thickness)),
        black calc(50% - var(--donut-thickness) + 1px)
    );
    -webkit-mask: radial-gradient(
        circle,
        transparent calc(50% - var(--donut-thickness)),
        black calc(50% - var(--donut-thickness) + 1px)
    );
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}
.donut-center {
    text-align: center;
    /* 位于 mask 挖空区域 */
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.donut-value {
    font-family: var(--font-display);
    font-size: clamp(1.5rem, 4vw, 2.5rem);
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
}
.donut-label {
    font-size: var(--caption-size);
    color: var(--text-secondary);
    margin-top: var(--space-xs);
}
```

### 多段环形图（占比分布）

```html
<div class="chart-donut multi"
     style="--seg1: 45; --seg2: 30; --seg3: 15; --seg4: 10;
            --c1: var(--accent); --c2: var(--info); --c3: var(--warning); --c4: var(--text-secondary);">
    <div class="donut-center">
        <span class="donut-value">4项</span>
    </div>
</div>
```

```css
.chart-donut.multi {
    background: conic-gradient(
        var(--c1) 0% calc(var(--seg1) * 1%),
        var(--c2) calc(var(--seg1) * 1%) calc((var(--seg1) + var(--seg2)) * 1%),
        var(--c3) calc((var(--seg1) + var(--seg2)) * 1%) calc((var(--seg1) + var(--seg2) + var(--seg3)) * 1%),
        var(--c4) calc((var(--seg1) + var(--seg2) + var(--seg3)) * 1%) 100%
    );
}
```

**图例（配合多段环形图）**：

```html
<div class="donut-legend">
    <div class="legend-item"><span class="legend-dot" style="--dot-color: var(--accent);"></span> 平台A 45%</div>
    <div class="legend-item"><span class="legend-dot" style="--dot-color: var(--info);"></span> 平台B 30%</div>
    <div class="legend-item"><span class="legend-dot" style="--dot-color: var(--warning);"></span> 平台C 15%</div>
    <div class="legend-item"><span class="legend-dot" style="--dot-color: var(--text-secondary);"></span> 其他 10%</div>
</div>
```

```css
.donut-legend { display: flex; flex-wrap: wrap; gap: var(--space-md); margin-top: var(--space-md); }
.legend-item { display: flex; align-items: center; gap: var(--space-xs); font-size: var(--small-size); color: var(--text-secondary); }
.legend-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--dot-color); flex-shrink: 0; }
```

---

## 三、Progress Bar（进度条）

**适用**: 单指标完成率、多指标并行进度

```html
<div class="progress-group">
    <div class="progress-item">
        <div class="progress-header">
            <span class="progress-label">销售目标</span>
            <span class="progress-pct">85%</span>
        </div>
        <div class="progress-track">
            <div class="progress-fill" style="width: 85%; --fill-color: var(--success);"></div>
        </div>
    </div>
</div>
```

```css
.progress-group { display: flex; flex-direction: column; gap: var(--space-md); }
.progress-item { display: flex; flex-direction: column; gap: var(--space-xs); }
.progress-header { display: flex; justify-content: space-between; font-size: var(--small-size); }
.progress-label { color: var(--text-secondary); }
.progress-pct { font-weight: 600; color: var(--text-primary); }
.progress-track { height: clamp(8px, 1.5vh, 12px); background: var(--bg-card); border-radius: 100px; overflow: hidden; }
.progress-fill { height: 100%; background: var(--fill-color, var(--accent)); border-radius: 100px; transition: width 0.8s var(--ease-out-expo); }
```

---

## 四、Sparkline（迷你趋势线）

**适用**: 紧凑的趋势展示，嵌入表格或卡片内
**核心**: 内联 SVG `<polyline>`

```html
<!-- 数据点用空格分隔的 y 坐标（0-100 归一化） -->
<svg class="sparkline" viewBox="0 0 100 30" aria-label="趋势: 上升">
    <polyline
        fill="none"
        stroke="var(--accent)"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        points="0,25 20,22 40,18 60,15 80,8 100,5"
    />
    <!-- 终点圆点 -->
    <circle cx="100" cy="5" r="3" fill="var(--accent)"/>
</svg>
```

```css
.sparkline {
    width: clamp(80px, 15vw, 150px);
    height: clamp(24px, 4vh, 40px);
    display: inline-block;
    vertical-align: middle;
}
```

**数据绑定**: 将数据归一化到 0-30 范围，生成 `x,y` 坐标字符串。

```python
# 归一化示例（生成 points 属性）
def to_sparkline(values, width=100, height=30, padding=2):
    vmin, vmax = min(values), max(values)
    vrange = vmax - vmin or 1
    points = []
    for i, v in enumerate(values):
        x = padding + (width - 2*padding) * i / (len(values)-1)
        y = height - padding - (height - 2*padding) * (v - vmin) / vrange
        points.append(f"{x:.1f},{y:.1f}")
    return " ".join(points)
```

---

## 五、Timeline（时间线）

**适用**: 里程碑、事件序列、版本历史

```html
<div class="timeline">
    <div class="tl-item">
        <div class="tl-marker" style="--marker-color: var(--accent);"></div>
        <div class="tl-content">
            <div class="tl-date">2026-Q1</div>
            <h4>项目启动</h4>
            <p>完成需求调研与技术选型</p>
        </div>
    </div>
    <div class="tl-item">
        <div class="tl-marker" style="--marker-color: var(--info);"></div>
        <div class="tl-content">
            <div class="tl-date">2026-Q2</div>
            <h4>MVP 上线</h4>
            <p>核心功能开发完成，内部灰度</p>
        </div>
    </div>
</div>
```

```css
.timeline {
    position: relative;
    padding-left: var(--space-xl);
}
.timeline::before {
    content: '';
    position: absolute;
    left: 12px;
    top: 8px;
    bottom: 8px;
    width: 2px;
    background: rgba(128,128,128,0.2);
}
.tl-item {
    position: relative;
    margin-bottom: var(--space-lg);
}
.tl-item:last-child { margin-bottom: 0; }
.tl-marker {
    position: absolute;
    left: calc(-1 * var(--space-xl) + 4px);
    top: 6px;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--marker-color, var(--accent));
    border: 3px solid var(--bg-primary);
    box-shadow: 0 0 0 2px var(--marker-color, var(--accent));
}
.tl-content {
    background: var(--bg-card);
    border-radius: var(--radius-md);
    padding: var(--space-md);
}
.tl-date {
    font-family: var(--font-mono);
    font-size: var(--caption-size);
    color: var(--accent);
    margin-bottom: var(--space-xs);
}
.tl-content h4 {
    margin-bottom: var(--space-xs);
}
.tl-content p {
    font-size: var(--small-size);
}
```

---

## 六、Heatmap Grid（热力网格）

**适用**: 多维交叉数据（如「各平台×各指标」评分矩阵）

```html
<div class="heatmap">
    <!-- 表头行 -->
    <div class="hm-cell hm-header">指标</div>
    <div class="hm-cell hm-header">平台A</div>
    <div class="hm-cell hm-header">平台B</div>
    <div class="hm-cell hm-header">平台C</div>

    <!-- 数据行 -->
    <div class="hm-cell hm-row-label">流量</div>
    <div class="hm-cell" style="--hm-intensity: 0.9;">92</div>
    <div class="hm-cell" style="--hm-intensity: 0.6;">64</div>
    <div class="hm-cell" style="--hm-intensity: 0.3;">38</div>
</div>
```

```css
.heatmap {
    display: grid;
    grid-template-columns: auto repeat(auto-fit, minmax(60px, 1fr));
    gap: 2px;
    background: var(--bg-card);
    border-radius: var(--radius-md);
    overflow: hidden;
    padding: 2px;
}
.hm-cell {
    padding: var(--space-sm) var(--space-md);
    text-align: center;
    font-size: var(--small-size);
    border-radius: var(--radius-sm);
    /* 热力色：从背景色到强调色 */
    background: color-mix(in srgb, var(--accent) calc(var(--hm-intensity, 0) * 100%), var(--bg-card));
    color: var(--text-primary);
}
.hm-header {
    font-weight: 600;
    color: var(--text-secondary);
    background: transparent;
}
.hm-row-label {
    text-align: left;
    font-weight: 500;
    color: var(--text-secondary);
    background: transparent;
}
/* 高强度格文字变白 */
.hm-cell[style*="--hm-intensity: 0.7"],
.hm-cell[style*="--hm-intensity: 0.8"],
.hm-cell[style*="--hm-intensity: 0.9"],
.hm-cell[style*="--hm-intensity: 1"] {
    color: white;
}
```

---

## 七、Bullet Chart（子弹图）

**适用**: 目标 vs 实际对比，Stephen Few 风格

```html
<div class="bullet-chart">
    <div class="bullet-label">销售额</div>
    <div class="bullet-track">
        <!-- 定性区间（差/一般/好） -->
        <div class="bullet-range bad" style="width: 60%;"></div>
        <div class="bullet-range ok" style="width: 25%;"></div>
        <div class="bullet-range good" style="width: 15%;"></div>
        <!-- 实际值 -->
        <div class="bullet-actual" style="width: 73%;"></div>
        <!-- 目标线 -->
        <div class="bullet-target" style="left: 80%;"></div>
    </div>
    <div class="bullet-value">73%</div>
</div>
```

```css
.bullet-chart {
    display: flex;
    align-items: center;
    gap: var(--space-sm);
    margin-bottom: var(--space-sm);
}
.bullet-label {
    width: clamp(60px, 15vw, 100px);
    font-size: var(--small-size);
    color: var(--text-secondary);
    text-align: right;
    flex-shrink: 0;
}
.bullet-track {
    flex: 1;
    height: clamp(16px, 2.5vh, 24px);
    background: var(--bg-card);
    border-radius: var(--radius-sm);
    position: relative;
    overflow: hidden;
    display: flex;
}
.bullet-range {
    height: 100%;
}
.bullet-range.bad  { background: rgba(255,71,87,0.15); }
.bullet-range.ok   { background: rgba(255,165,2,0.15); }
.bullet-range.good { background: rgba(46,213,115,0.15); }
.bullet-actual {
    position: absolute;
    top: 3px;
    bottom: 3px;
    left: 0;
    background: var(--accent);
    border-radius: var(--radius-sm);
    transition: width 0.8s var(--ease-out-expo);
}
.bullet-target {
    position: absolute;
    top: -2px;
    bottom: -2px;
    width: 3px;
    background: var(--text-primary);
    border-radius: 2px;
    /* left 由内联 style 设置 */
}
.bullet-value {
    width: 3rem;
    font-size: var(--small-size);
    font-weight: 600;
    color: var(--text-primary);
    text-align: left;
}
```

---

## 八、Waterfall Chart（瀑布图）

**适用**: 累积变化展示（如月度营收分解）

```html
<div class="waterfall">
    <div class="wf-item">
        <div class="wf-label">起始</div>
        <div class="wf-bar" style="height: 40px; --wf-color: var(--info); margin-top: auto;">100</div>
        <div class="wf-value">100</div>
    </div>
    <div class="wf-item">
        <div class="wf-label">+增长</div>
        <div class="wf-bar" style="height: 30px; --wf-color: var(--success); margin-top: 0;">+30</div>
        <div class="wf-value">130</div>
    </div>
    <div class="wf-item">
        <div class="wf-label">-减少</div>
        <div class="wf-bar" style="height: 20px; --wf-color: var(--danger); margin-top: 20px;">-20</div>
        <div class="wf-value">110</div>
    </div>
</div>
```

```css
.waterfall {
    display: flex;
    align-items: flex-end;
    gap: var(--space-md);
    height: clamp(200px, 35vh, 300px);
    padding: var(--space-md) 0;
    border-bottom: 1px solid rgba(128,128,128,0.2);
}
.wf-item {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100%;
}
.wf-bar {
    width: 100%;
    max-width: 60px;
    background: var(--wf-color, var(--accent));
    border-radius: var(--radius-sm) var(--radius-sm) 0 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--caption-size);
    font-weight: 600;
    color: white;
    transition: height 0.8s var(--ease-out-expo);
}
.wf-label {
    font-size: var(--caption-size);
    color: var(--text-secondary);
    margin-top: var(--space-xs);
    order: 1;
}
.wf-value {
    font-size: var(--small-size);
    font-weight: 600;
    margin-bottom: var(--space-xs);
}
```

---

## 九、Gauge Chart（仪表盘）

**适用**: 单一 KPI 的状态展示（如 NPS 得分）

```html
<div class="chart-gauge" style="--gauge-pct: 72; --gauge-color: var(--success);">
    <div class="gauge-value">72</div>
    <div class="gauge-label">NPS 得分</div>
</div>
```

```css
.chart-gauge {
    --gauge-pct: 0;
    --gauge-size: clamp(140px, 28vw, 220px);
    --gauge-thickness: clamp(10px, 2vw, 14px);
    width: var(--gauge-size);
    height: calc(var(--gauge-size) * 0.6);
    position: relative;
    overflow: hidden;
}
.chart-gauge::before {
    content: '';
    position: absolute;
    width: var(--gauge-size);
    height: var(--gauge-size);
    border-radius: 50%;
    /* 底部半圆：180deg 的扇形 */
    background: conic-gradient(
        var(--gauge-color, var(--accent)) 0deg calc(var(--gauge-pct) * 1.8deg),
        var(--bg-card) calc(var(--gauge-pct) * 1.8deg) 180deg,
        transparent 180deg 360deg
    );
    /* 挖空中间 */
    mask: radial-gradient(
        circle at 50% 100%,
        transparent calc(50% - var(--gauge-thickness)),
        black calc(50% - var(--gauge-thickness) + 1px)
    );
    -webkit-mask: radial-gradient(
        circle at 50% 100%,
        transparent calc(50% - var(--gauge-thickness)),
        black calc(50% - var(--gauge-thickness) + 1px)
    );
}
.gauge-value {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    font-family: var(--font-display);
    font-size: clamp(1.5rem, 4vw, 2.5rem);
    font-weight: 700;
    color: var(--gauge-color, var(--accent));
    line-height: 1;
}
.gauge-label {
    position: absolute;
    bottom: -1.8rem;
    left: 50%;
    transform: translateX(-50%);
    font-size: var(--caption-size);
    color: var(--text-secondary);
    white-space: nowrap;
}
```

---

## 十、Score Card Grid（评分卡 — 雷达图替代）

**适用**: 多维度评分对比，CSS 雷达图不可行时的替代方案

```html
<div class="score-grid grid-2">
    <div class="score-card">
        <div class="score-header">
            <span class="score-label">流量获取</span>
            <span class="score-value">8.5</span>
        </div>
        <div class="score-bar-track">
            <div class="score-bar" style="width: 85%; --score-color: var(--accent);"></div>
        </div>
    </div>
</div>
```

```css
.score-card {
    background: var(--bg-card);
    border-radius: var(--radius-md);
    padding: var(--space-md);
}
.score-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: var(--space-xs);
}
.score-label { font-size: var(--small-size); color: var(--text-secondary); }
.score-value { font-family: var(--font-display); font-size: var(--h4-size); font-weight: 700; color: var(--score-color, var(--accent)); }
.score-bar-track { height: 6px; background: rgba(128,128,128,0.15); border-radius: 3px; overflow: hidden; }
.score-bar { height: 100%; background: var(--score-color, var(--accent)); border-radius: 3px; transition: width 0.8s var(--ease-out-expo); }
```

---

## 十一、Dashboard Grid（仪表盘网格）

**适用**: 多指标 KPI 概览，在一屏内混合展示多种图表

```html
<div class="dashboard-grid">
    <!-- 大数字卡片 -->
    <div class="dash-card dash-big-num">
        <div class="dash-value">12,847</div>
        <div class="dash-label">总访问量</div>
        <div class="dash-trend up">↑ 12.5%</div>
    </div>
    <!-- 迷你柱状图卡片 -->
    <div class="dash-card dash-mini-chart">
        <div class="dash-label">周趋势</div>
        <div class="mini-bar-group">
            <div class="mini-bar" style="height: 60%;"></div>
            <div class="mini-bar" style="height: 75%;"></div>
            <div class="mini-bar" style="height: 55%;"></div>
            <div class="mini-bar" style="height: 90%;"></div>
            <div class="mini-bar" style="height: 70%;"></div>
            <div class="mini-bar" style="height: 85%;"></div>
            <div class="mini-bar" style="height: 80%;"></div>
        </div>
    </div>
    <!-- 进度卡片 -->
    <div class="dash-card dash-progress">
        <div class="dash-label">目标达成</div>
        <div class="dash-pct">73%</div>
        <div class="progress-track">
            <div class="progress-fill" style="width: 73%;"></div>
        </div>
    </div>
</div>
```

```css
.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr));
    gap: var(--space-md);
}
.dash-card {
    background: var(--bg-card);
    border-radius: var(--radius-md);
    padding: var(--space-lg);
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.dash-big-num { align-items: center; }
.dash-value {
    font-family: var(--font-display);
    font-size: var(--h2-size);
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
}
.dash-label {
    font-size: var(--caption-size);
    color: var(--text-secondary);
    margin-top: var(--space-xs);
}
.dash-trend { font-size: var(--caption-size); margin-top: var(--space-xs); }
.dash-trend.up { color: var(--success); }
.dash-trend.down { color: var(--danger); }
.dash-pct {
    font-family: var(--font-display);
    font-size: var(--h4-size);
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
    margin-bottom: var(--space-xs);
}
/* 迷你柱状图 */
.mini-bar-group {
    display: flex;
    align-items: flex-end;
    gap: 3px;
    height: 60px;
    margin-top: var(--space-sm);
}
.mini-bar {
    flex: 1;
    background: var(--accent);
    border-radius: 2px 2px 0 0;
    min-height: 3px;
    opacity: 0.7;
    transition: height 0.6s var(--ease-out-expo);
}
.mini-bar:last-child { opacity: 1; }
```

---

## 数据绑定总则

所有图表通过内联 `style` 属性绑定数据，无需 JS 运行时计算（除 sparkline 的 points 外）。

| 图表类型 | 数据绑定方式 | 示例 |
|----------|-------------|------|
| Bar Chart | `style="height: N%"` 或 `style="width: N%"` | `<div class="hbar-fill" style="width: 73%;">` |
| Donut | `style="--donut-pct: N;"` (CSS 变量) | `<div style="--donut-pct: 73;">` |
| Progress | `style="width: N%;"` | `<div style="width: 85%;">` |
| Sparkline | `points="x1,y1 x2,y2 ..."` | `<polyline points="...">` |
| Heatmap | `style="--hm-intensity: 0.N;"` | `<div style="--hm-intensity: 0.7;">` |
| Bullet | `style="width: N%; left: N%;"` | `<div style="width: 73%;">` |
| Gauge | `style="--gauge-pct: N;"` | `<div style="--gauge-pct: 72;">` |

---

## 动画触发

所有图表使用统一的 Intersection Observer 触发动画。bar/进度条类图表的 `transition` 已内置在 CSS 中，
只需在元素进入视口时通过 JS 更新其 `width`/`height`（如果使用延迟渲染），或直接依赖 CSS transition（推荐：先渲染为 0，进入视口后设置目标值）。

**推荐模式**：HTML 中直接写目标值，利用 CSS transition 的初始状态。页面加载时图表自动从 0 动画到目标值。

```html
<!-- 直接写目标值 + CSS transition = 自动入场动画 -->
<div class="hbar-fill" style="width: 73%;"></div>
```

由于 CSS transition 在元素首次渲染时不会触发（需要属性变更），可在页面底部添加脚本：

```javascript
// 触发所有图表的入场动画
document.querySelectorAll('.hbar-fill, .bar-value, .progress-fill, .bar, .score-bar').forEach(el => {
    const target = el.style.width || el.style.height;
    el.style.width = '0';
    el.style.height = '0';
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            el.style.width = target;
            el.style.height = target;
        });
    });
});
```
