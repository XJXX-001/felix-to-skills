# Report HTML Template

报告 HTML 参考架构。每个报告都遵循此结构。所有 CSS/JS 内联，零依赖。

---

## 基础 HTML 结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>报告标题</title>

    <!-- 字体：Fontshare 或 Google Fonts，禁止系统字体 -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <!-- 根据选择的风格预设替换字体 link -->

    <style>
        /* ===========================================
           CSS CUSTOM PROPERTIES (THEME)
           修改这些变量即可全局换肤
           =========================================== */
        :root {
            /* 色彩 — 来自风格预设 */
            --bg-primary: #0a0a0a;
            --bg-card: #141414;
            --bg-section-alt: #1a1a1a;
            --text-primary: #ffffff;
            --text-secondary: #9ca3af;
            --accent: #4361ee;
            --accent-glow: rgba(67, 97, 238, 0.3);
            --success: #2ed573;
            --warning: #ffa502;
            --danger: #ff4757;
            --info: #3498db;

            /* 排版 */
            --font-display: 'Manrope', 'Noto Sans SC', sans-serif;
            --font-body: 'Manrope', 'Noto Sans SC', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;

            /* 间距体系 */
            --space-xs: clamp(0.25rem, 0.5vw, 0.5rem);
            --space-sm: clamp(0.5rem, 1vw, 0.75rem);
            --space-md: clamp(0.75rem, 1.5vw, 1.25rem);
            --space-lg: clamp(1rem, 2vw, 2rem);
            --space-xl: clamp(2rem, 4vw, 4rem);
            --space-2xl: clamp(3rem, 6vw, 6rem);

            /* 圆角 */
            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-lg: 16px;
            --radius-xl: 24px;

            /* 阴影 */
            --shadow-card: 0 2px 8px rgba(0,0,0,0.08);
            --shadow-elevated: 0 8px 32px rgba(0,0,0,0.12);

            /* 过渡 */
            --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
            --duration-fast: 0.2s;
            --duration-normal: 0.4s;

            /* 图表色 */
            --chart-1: var(--accent);
            --chart-2: var(--info);
            --chart-3: var(--warning);
            --chart-4: var(--success);
            --chart-5: #e056a0;
            --chart-neutral: var(--bg-card);
        }

        /* ===========================================
           RESPONSIVE BASE (from viewport-base.css)
           =========================================== */

        /* Base Reset */
        *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
        body { font-family: var(--font-body); background: var(--bg-primary); color: var(--text-primary); line-height: 1.6; min-height: 100vh; }

        /* Content Container */
        .report-container { max-width: min(90vw, 1200px); margin: 0 auto; }
        .report-container.reading { max-width: min(90vw, 800px); }

        /* Section Spacing */
        .report-section { padding: var(--space-xl) var(--slide-padding); position: relative; }
        .report-section.alt { background: var(--bg-section-alt); }
        .report-cover { min-height: 100vh; min-height: 100dvh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: var(--slide-padding); position: relative; overflow: hidden; }

        /* Typography Scale */
        :root {
            --title-size: clamp(2rem, 5vw, 4.5rem);
            --h2-size: clamp(1.5rem, 3.5vw, 2.5rem);
            --h3-size: clamp(1.1rem, 2.5vw, 1.75rem);
            --h4-size: clamp(0.95rem, 1.8vw, 1.25rem);
            --body-size: clamp(0.85rem, 1.5vw, 1.1rem);
            --small-size: clamp(0.7rem, 1vw, 0.9rem);
            --caption-size: clamp(0.65rem, 0.9vw, 0.8rem);
            --slide-padding: clamp(1rem, 4vw, 4rem);
            --content-gap: clamp(0.75rem, 2vw, 2rem);
            --element-gap: clamp(0.5rem, 1.5vw, 1.25rem);
        }
        h1 { font-family: var(--font-display); font-size: var(--title-size); font-weight: 700; line-height: 1.1; }
        h2 { font-family: var(--font-display); font-size: var(--h2-size); font-weight: 600; line-height: 1.2; }
        h3 { font-family: var(--font-display); font-size: var(--h3-size); font-weight: 500; line-height: 1.3; }
        h4 { font-family: var(--font-display); font-size: var(--h4-size); font-weight: 500; line-height: 1.3; }
        p, li { font-size: var(--body-size); color: var(--text-secondary); }

        /* Card & Container */
        .card { background: var(--bg-card); border-radius: var(--radius-md); padding: clamp(1rem, 2vw, 1.5rem); }
        .card-elevated { box-shadow: var(--shadow-card); }

        /* Images */
        img, .image-container { max-width: 100%; height: auto; border-radius: var(--radius-sm); }

        /* Tables */
        table { width: 100%; border-collapse: collapse; font-size: var(--body-size); }
        th, td { padding: clamp(0.5rem, 1vw, 0.75rem) clamp(0.75rem, 1.5vw, 1rem); text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.2); }
        th { font-family: var(--font-display); font-weight: 600; font-size: var(--small-size); text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-secondary); background: var(--bg-card); }

        /* Grid Systems */
        .grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: var(--content-gap); }
        .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: var(--content-gap); }
        .grid-4 { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: var(--element-gap); }

        /* Lists */
        .bullet-list { display: flex; flex-direction: column; gap: var(--element-gap); list-style: none; }
        .bullet-list li { display: flex; align-items: flex-start; gap: 0.75rem; }

        /* Horizontal Rule */
        hr { border: none; border-top: 1px solid rgba(128, 128, 128, 0.2); margin: var(--content-gap) 0; }

        /* Responsive Breakpoints */
        @media (max-height: 700px) { :root { --slide-padding: clamp(0.75rem, 3vw, 2rem); --content-gap: clamp(0.5rem, 1.5vw, 1rem); --title-size: clamp(1.5rem, 4.5vw, 3rem); --h2-size: clamp(1.1rem, 3vw, 1.75rem); } }
        @media (max-width: 768px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } .report-cover { min-height: 80vh; min-height: 80dvh; } }
        @media (max-width: 480px) { :root { --slide-padding: clamp(0.75rem, 3vw, 1.25rem); --title-size: clamp(1.5rem, 7vw, 2.5rem); } }

        /* Reduced Motion */
        @media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.2s !important; } html { scroll-behavior: auto; } }

        /* Print Styles */
        @media print { :root { --slide-padding: 1.5cm; --title-size: 24pt; --h2-size: 18pt; --body-size: 11pt; } .report-section { page-break-inside: avoid; } .report-cover { min-height: auto; page-break-after: always; } body { background: white !important; color: black !important; } .card { box-shadow: none !important; border: 1px solid #ccc; } }

        /* ===========================================
           SCROLL REVEAL ANIMATIONS
           =========================================== */
        .reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.5s var(--ease-out-expo), transform 0.5s var(--ease-out-expo); }
        .reveal.visible { opacity: 1; transform: translateY(0); }
        .reveal:nth-child(1) { transition-delay: 0.05s; }
        .reveal:nth-child(2) { transition-delay: 0.1s; }
        .reveal:nth-child(3) { transition-delay: 0.15s; }
        .reveal:nth-child(4) { transition-delay: 0.2s; }
        .reveal:nth-child(5) { transition-delay: 0.25s; }
        .reveal:nth-child(6) { transition-delay: 0.3s; }

        /* Background Effects (optional) */
        .cover-gradient { background: radial-gradient(ellipse at 20% 80%, rgba(120, 0, 255, 0.15) 0%, transparent 50%), radial-gradient(ellipse at 80% 20%, rgba(0, 255, 200, 0.1) 0%, transparent 50%), var(--bg-primary); }
        .grid-bg { background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 50px 50px; }

        /* ===========================================
           COVER SECTION
           =========================================== */
        .report-cover {
            background: linear-gradient(135deg, var(--bg-primary) 0%, color-mix(in srgb, var(--accent) 15%, var(--bg-primary)) 100%);
        }
        .cover-title {
            font-family: var(--font-display);
            font-size: var(--title-size);
            font-weight: 700;
            margin-bottom: var(--space-md);
        }
        .cover-subtitle {
            font-size: clamp(1rem, 2vw, 1.5rem);
            color: var(--text-secondary);
            margin-bottom: var(--space-lg);
        }
        .cover-meta {
            font-size: var(--small-size);
            color: var(--text-secondary);
            opacity: 0.7;
        }
        .cover-accent-line {
            width: clamp(3rem, 8vw, 6rem);
            height: 3px;
            background: var(--accent);
            margin: var(--space-lg) auto;
            border-radius: 2px;
        }

        /* ===========================================
           SECTION HEADING
           =========================================== */
        .section-heading {
            margin-bottom: var(--space-xl);
        }
        .section-number {
            font-family: var(--font-mono);
            font-size: var(--small-size);
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: var(--space-xs);
        }
        .section-heading h2 {
            margin-bottom: var(--space-sm);
        }
        .section-desc {
            font-size: var(--body-size);
            color: var(--text-secondary);
            max-width: min(90vw, 600px);
        }

        /* ===========================================
           STAT CARDS
           =========================================== */
        .stat-card {
            background: var(--bg-card);
            border-radius: var(--radius-md);
            padding: var(--space-lg);
            text-align: center;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .stat-value {
            font-family: var(--font-display);
            font-size: var(--h2-size);
            font-weight: 700;
            color: var(--accent);
            line-height: 1;
            margin-bottom: var(--space-xs);
        }
        .stat-label {
            font-size: var(--small-size);
            color: var(--text-secondary);
        }
        .stat-trend {
            font-size: var(--caption-size);
            margin-top: var(--space-xs);
        }
        .stat-trend.up { color: var(--success); }
        .stat-trend.down { color: var(--danger); }

        /* ===========================================
           SUMMARY GRID
           =========================================== */
        .summary-item {
            display: flex;
            align-items: flex-start;
            gap: var(--space-md);
            padding: var(--space-md);
            background: var(--bg-card);
            border-radius: var(--radius-sm);
            border-left: 3px solid var(--accent);
        }
        .summary-icon {
            width: 2.5rem;
            height: 2.5rem;
            background: var(--accent-glow);
            border-radius: var(--radius-sm);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            flex-shrink: 0;
        }
        .summary-text h4 {
            margin-bottom: var(--space-xs);
        }
        .summary-text p {
            font-size: var(--small-size);
        }

        /* ===========================================
           CALLOUT BOXES
           =========================================== */
        .callout {
            padding: var(--space-md) var(--space-lg);
            border-radius: var(--radius-sm);
            display: flex;
            align-items: flex-start;
            gap: var(--space-sm);
            font-size: var(--body-size);
            margin-bottom: var(--space-md);
        }
        .callout-icon {
            font-size: 1.2rem;
            flex-shrink: 0;
            margin-top: 0.15em;
        }
        .callout-danger {
            background: rgba(255, 71, 87, 0.1);
            border: 1px solid rgba(255, 71, 87, 0.25);
            color: var(--danger);
        }
        .callout-warning {
            background: rgba(255, 165, 2, 0.1);
            border: 1px solid rgba(255, 165, 2, 0.25);
            color: var(--warning);
        }
        .callout-info {
            background: rgba(52, 152, 219, 0.1);
            border: 1px solid rgba(52, 152, 219, 0.25);
            color: var(--info);
        }
        .callout-success {
            background: rgba(46, 213, 115, 0.1);
            border: 1px solid rgba(46, 213, 115, 0.25);
            color: var(--success);
        }

        /* ===========================================
           STEP FLOW
           =========================================== */
        .step-flow {
            display: flex;
            flex-direction: column;
            gap: var(--space-md);
        }
        .step {
            display: flex;
            align-items: flex-start;
            gap: var(--space-md);
        }
        .step-number {
            width: clamp(2rem, 4vw, 2.5rem);
            height: clamp(2rem, 4vw, 2.5rem);
            background: var(--accent);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-display);
            font-weight: 700;
            font-size: var(--body-size);
            color: var(--bg-primary);
            flex-shrink: 0;
        }
        .step-content h4 {
            margin-bottom: var(--space-xs);
        }
        .step-content p {
            font-size: var(--small-size);
        }

        /* ===========================================
           COMPARISON TABLE
           =========================================== */
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            font-size: var(--body-size);
        }
        .comparison-table thead th {
            background: var(--bg-card);
            position: sticky;
            top: 0;
            z-index: 1;
        }
        .comparison-table .highlight-col {
            background: rgba(67, 97, 238, 0.05);
        }
        .comparison-table .cell-best {
            color: var(--success);
            font-weight: 600;
        }
        .comparison-table .cell-worst {
            color: var(--danger);
        }
        .table-responsive {
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }

        /* ===========================================
           BULLET LIST
           =========================================== */
        .bullet-list li::before {
            content: '';
            width: 6px;
            height: 6px;
            background: var(--accent);
            border-radius: 50%;
            margin-top: 0.6em;
            flex-shrink: 0;
        }

        /* ===========================================
           STATUS BADGE
           =========================================== */
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.2rem 0.6rem;
            border-radius: 100px;
            font-size: var(--caption-size);
            font-weight: 500;
        }
        .status-badge.done  { background: rgba(46, 213, 115, 0.15); color: var(--success); }
        .status-badge.wip   { background: rgba(255, 165, 2, 0.15);  color: var(--warning); }
        .status-badge.todo  { background: rgba(128, 128, 128, 0.15); color: var(--text-secondary); }
        .status-badge.urgent { background: rgba(255, 71, 87, 0.15);  color: var(--danger); }

        /* ===========================================
           QUOTE BLOCK
           =========================================== */
        .quote-block {
            border-left: 3px solid var(--accent);
            padding: var(--space-md) var(--space-lg);
            margin: var(--space-lg) 0;
            font-style: italic;
            font-size: var(--h4-size);
            color: var(--text-primary);
        }
        .quote-attribution {
            font-size: var(--small-size);
            color: var(--text-secondary);
            font-style: normal;
            margin-top: var(--space-sm);
        }

        /* ===========================================
           CODE BLOCK (for product docs)
           =========================================== */
        .code-block {
            background: var(--bg-card);
            border-radius: var(--radius-sm);
            padding: var(--space-md);
            font-family: var(--font-mono);
            font-size: var(--small-size);
            overflow-x: auto;
            white-space: pre;
            border: 1px solid rgba(255,255,255,0.05);
        }

        /* ===========================================
           ENDING SECTION
           =========================================== */
        .ending-section {
            min-height: 60vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: var(--space-2xl) var(--slide-padding);
        }
        .ending-section h2 {
            margin-bottom: var(--space-md);
        }
        .ending-meta {
            font-size: var(--small-size);
            color: var(--text-secondary);
            opacity: 0.6;
            margin-top: var(--space-lg);
        }

        /* ===========================================
           TABLE OF CONTENTS (optional)
           =========================================== */
        .toc {
            list-style: none;
            counter-reset: toc;
        }
        .toc li {
            counter-increment: toc;
            padding: var(--space-sm) 0;
            border-bottom: 1px solid rgba(128,128,128,0.1);
            font-size: var(--body-size);
        }
        .toc li::before {
            content: "0" counter(toc);
            font-family: var(--font-mono);
            color: var(--accent);
            margin-right: var(--space-md);
            font-size: var(--small-size);
        }
    </style>
</head>
<body>

    <!-- ===========================================
         COVER
         =========================================== -->
    <section class="report-cover">
        <div class="cover-content">
            <h1 class="cover-title reveal">报告标题</h1>
            <div class="cover-accent-line reveal"></div>
            <p class="cover-subtitle reveal">副标题或一句话概述</p>
            <p class="cover-meta reveal">日期 · 作者 · 部门</p>
        </div>
    </section>

    <!-- ===========================================
         EXECUTIVE SUMMARY
         =========================================== -->
    <section class="report-section">
        <div class="report-container reading">
            <div class="section-heading reveal">
                <div class="section-number">01 / 摘要</div>
                <h2>执行摘要</h2>
                <p class="section-desc">本报告的简要概述，让读者快速了解核心结论。</p>
            </div>
            <div class="summary-grid grid-2">
                <!-- summary-item × N -->
            </div>
        </div>
    </section>

    <!-- ===========================================
         CONTENT SECTIONS
         =========================================== -->
    <section class="report-section alt">
        <div class="report-container">
            <div class="section-heading reveal">
                <div class="section-number">02 / 章节名</div>
                <h2>章节标题</h2>
            </div>
            <!-- 内容组件在此 -->
        </div>
    </section>

    <!-- More sections... -->

    <!-- ===========================================
         ENDING
         =========================================== -->
    <section class="ending-section">
        <h2 class="reveal">感谢阅读</h2>
        <p class="reveal" style="color: var(--text-secondary);">问题与建议，欢迎随时沟通</p>
        <div class="ending-meta reveal">报告生成于 YYYY-MM-DD</div>
    </section>

    <!-- ===========================================
         SCROLL ANIMATION
         =========================================== -->
    <script>
        // Scroll reveal animation
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -30px 0px' });
        document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

        // Chart bar/fill entrance animation
        document.querySelectorAll('.hbar-fill, .bar-value, .progress-fill, .score-bar').forEach(el => {
            const w = el.style.width, h = el.style.height;
            if (w) { el.style.width = '0'; requestAnimationFrame(() => requestAnimationFrame(() => { el.style.width = w; })); }
            if (h && h !== '100%') { el.style.height = '0'; requestAnimationFrame(() => requestAnimationFrame(() => { el.style.height = h; })); }
        });

        // Number counter animation (call: animateValue(el, 0, 15420, 1500))
        function animateValue(el, start, end, duration) {
            const startTime = performance.now();
            function update(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const ease = 1 - Math.pow(1 - progress, 3);
                el.textContent = Math.floor(start + (end - start) * ease).toLocaleString();
                if (progress < 1) requestAnimationFrame(update);
            }
            requestAnimationFrame(update);
        }
    </script>
</body>
</html>
```

---

## 组件使用对照表

根据 DESIGN_STANDARDS.md 中汇报类型对应的「组件优先级」，选择适用组件：

| 组件 | HTML 标签/类名 | 适用场景 |
|------|---------------|----------|
| Cover | `.report-cover` | 所有报告 |
| Section Heading | `.section-heading` | 所有章节 |
| Stat Card | `.stat-card` | 数据展示、KPI |
| Summary Grid | `.summary-grid` + `.summary-item` | 摘要、结论 |
| Callout | `.callout-{danger,warning,info,success}` | 提示、警告 |
| Step Flow | `.step-flow` + `.step` | 流程、步骤 |
| Comparison Table | `.comparison-table` | 竞品分析、数据对比 |
| Bullet List | `.bullet-list` | 要点罗列 |
| Status Badge | `.status-badge` | 状态标识 |
| Quote Block | `.quote-block` | 引用、重点强调 |
| Code Block | `.code-block` | 技术文档 |
| Table of Contents | `.toc` | 长报告导航 |
| Ending | `.ending-section` | 所有报告 |

---

## 章节交替背景规范

为增强可读性，相邻内容章节应使用交替背景：

```html
<section class="report-section">        <!-- 主背景 -->
<section class="report-section alt">    <!-- 交替背景 -->
<section class="report-section">        <!-- 主背景 -->
<section class="report-section alt">    <!-- 交替背景 -->
```

Cover 和 Ending 区不适用交替规则。

---

## 信息图表组件

以下 CSS 组件与 [INFOGRAPHIC_PATTERNS.md](INFOGRAPHIC_PATTERNS.md) 对应。
生成含数据可视化的报告时，从中选择适用图表。完整说明见 INFOGRAPHIC_PATTERNS.md。

### 水平柱状图 (Horizontal Bar)

```css
.chart-bar-horizontal { display: flex; flex-direction: column; gap: var(--space-sm); }
.hbar-item { display: flex; align-items: center; gap: var(--space-sm); }
.hbar-label { width: clamp(60px, 15vw, 120px); font-size: var(--small-size); color: var(--text-secondary); text-align: right; flex-shrink: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.hbar-track { flex: 1; height: clamp(16px, 2.5vh, 24px); background: var(--bg-card); border-radius: var(--radius-sm); overflow: hidden; }
.hbar-fill { height: 100%; background: var(--bar-color, var(--accent)); border-radius: var(--radius-sm); transition: width 0.8s var(--ease-out-expo); }
.hbar-value { width: 3rem; font-size: var(--small-size); font-weight: 600; color: var(--text-primary); text-align: left; }
```

### 垂直柱状图 (Vertical Bar)

```css
.chart-bar-vertical { display: flex; align-items: flex-end; justify-content: space-around; gap: var(--space-md); height: clamp(200px, 40vh, 350px); padding: var(--space-md) 0; border-bottom: 1px solid rgba(128,128,128,0.2); }
.bar-item { flex: 1; max-width: 80px; display: flex; flex-direction: column; align-items: center; gap: var(--space-xs); height: 100%; justify-content: flex-end; }
.bar-value { width: 100%; background: var(--bar-color, var(--accent)); border-radius: var(--radius-sm) var(--radius-sm) 0 0; min-height: 4px; transition: height 0.8s var(--ease-out-expo); display: flex; align-items: flex-start; justify-content: center; padding-top: var(--space-xs); font-size: var(--caption-size); font-weight: 600; color: white; }
.bar-label { font-size: var(--caption-size); color: var(--text-secondary); text-align: center; }
```

### 堆叠柱状图 (Stacked Bar)

```css
.chart-bar-stacked { display: flex; flex-direction: column; gap: var(--space-sm); }
.sbar-item { display: flex; align-items: center; gap: var(--space-sm); }
.sbar-label { width: clamp(60px, 15vw, 120px); font-size: var(--small-size); color: var(--text-secondary); text-align: right; flex-shrink: 0; }
.sbar-track { flex: 1; height: clamp(20px, 3vh, 28px); background: var(--bg-card); border-radius: var(--radius-sm); overflow: hidden; display: flex; }
.sbar-segment { height: 100%; background: var(--seg-color); transition: width 0.8s var(--ease-out-expo); }
.sbar-segment:first-child { border-radius: var(--radius-sm) 0 0 var(--radius-sm); }
.sbar-segment:last-child { border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }
```

### 环形图 (Donut Chart)

```css
.chart-donut { --donut-pct: 0; --donut-size: clamp(120px, 25vw, 200px); --donut-thickness: clamp(10px, 2vw, 16px); width: var(--donut-size); height: var(--donut-size); border-radius: 50%; background: conic-gradient(var(--accent) calc(var(--donut-pct) * 1%), var(--bg-card) calc(var(--donut-pct) * 1%)); mask: radial-gradient(circle, transparent calc(50% - var(--donut-thickness)), black calc(50% - var(--donut-thickness) + 1px)); -webkit-mask: radial-gradient(circle, transparent calc(50% - var(--donut-thickness)), black calc(50% - var(--donut-thickness) + 1px)); display: flex; align-items: center; justify-content: center; position: relative; }
.donut-center { text-align: center; position: absolute; display: flex; flex-direction: column; align-items: center; }
.donut-value { font-family: var(--font-display); font-size: clamp(1.5rem, 4vw, 2.5rem); font-weight: 700; color: var(--accent); line-height: 1; }
.donut-label { font-size: var(--caption-size); color: var(--text-secondary); margin-top: var(--space-xs); }
.donut-legend { display: flex; flex-wrap: wrap; gap: var(--space-md); margin-top: var(--space-md); }
.legend-item { display: flex; align-items: center; gap: var(--space-xs); font-size: var(--small-size); color: var(--text-secondary); }
.legend-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--dot-color); flex-shrink: 0; }
```

### 进度条组 (Progress Group)

```css
.progress-group { display: flex; flex-direction: column; gap: var(--space-md); }
.progress-item { display: flex; flex-direction: column; gap: var(--space-xs); }
.progress-header { display: flex; justify-content: space-between; font-size: var(--small-size); }
.progress-label { color: var(--text-secondary); }
.progress-pct { font-weight: 600; color: var(--text-primary); }
.progress-track { height: clamp(8px, 1.5vh, 12px); background: var(--bg-card); border-radius: 100px; overflow: hidden; }
.progress-fill { height: 100%; background: var(--fill-color, var(--accent)); border-radius: 100px; transition: width 0.8s var(--ease-out-expo); }
```

### 迷你趋势线 (Sparkline)

```css
.sparkline { width: clamp(80px, 15vw, 150px); height: clamp(24px, 4vh, 40px); display: inline-block; vertical-align: middle; }
```

### 时间线 (Timeline)

```css
.timeline { position: relative; padding-left: var(--space-xl); }
.timeline::before { content: ''; position: absolute; left: 12px; top: 8px; bottom: 8px; width: 2px; background: rgba(128,128,128,0.2); }
.tl-item { position: relative; margin-bottom: var(--space-lg); }
.tl-item:last-child { margin-bottom: 0; }
.tl-marker { position: absolute; left: calc(-1 * var(--space-xl) + 4px); top: 6px; width: 16px; height: 16px; border-radius: 50%; background: var(--marker-color, var(--accent)); border: 3px solid var(--bg-primary); box-shadow: 0 0 0 2px var(--marker-color, var(--accent)); }
.tl-content { background: var(--bg-card); border-radius: var(--radius-md); padding: var(--space-md); }
.tl-date { font-family: var(--font-mono); font-size: var(--caption-size); color: var(--accent); margin-bottom: var(--space-xs); }
```

### 热力网格 (Heatmap)

```css
.heatmap { display: grid; grid-template-columns: auto repeat(auto-fit, minmax(60px, 1fr)); gap: 2px; background: var(--bg-card); border-radius: var(--radius-md); overflow: hidden; padding: 2px; }
.hm-cell { padding: var(--space-sm) var(--space-md); text-align: center; font-size: var(--small-size); border-radius: var(--radius-sm); background: color-mix(in srgb, var(--accent) calc(var(--hm-intensity, 0) * 100%), var(--bg-card)); color: var(--text-primary); }
.hm-header { font-weight: 600; color: var(--text-secondary); background: transparent; }
.hm-row-label { text-align: left; font-weight: 500; color: var(--text-secondary); background: transparent; }
```

### 子弹图 (Bullet Chart)

```css
.bullet-chart { display: flex; align-items: center; gap: var(--space-sm); margin-bottom: var(--space-sm); }
.bullet-label { width: clamp(60px, 15vw, 100px); font-size: var(--small-size); color: var(--text-secondary); text-align: right; flex-shrink: 0; }
.bullet-track { flex: 1; height: clamp(16px, 2.5vh, 24px); background: var(--bg-card); border-radius: var(--radius-sm); position: relative; overflow: hidden; display: flex; }
.bullet-range { height: 100%; }
.bullet-range.bad  { background: rgba(255,71,87,0.15); }
.bullet-range.ok   { background: rgba(255,165,2,0.15); }
.bullet-range.good { background: rgba(46,213,115,0.15); }
.bullet-actual { position: absolute; top: 3px; bottom: 3px; left: 0; background: var(--accent); border-radius: var(--radius-sm); transition: width 0.8s var(--ease-out-expo); }
.bullet-target { position: absolute; top: -2px; bottom: -2px; width: 3px; background: var(--text-primary); border-radius: 2px; }
.bullet-value { width: 3rem; font-size: var(--small-size); font-weight: 600; color: var(--text-primary); text-align: left; }
```

### 评分卡 (Score Card)

```css
.score-card { background: var(--bg-card); border-radius: var(--radius-md); padding: var(--space-md); }
.score-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: var(--space-xs); }
.score-label { font-size: var(--small-size); color: var(--text-secondary); }
.score-value { font-family: var(--font-display); font-size: var(--h4-size); font-weight: 700; color: var(--score-color, var(--accent)); }
.score-bar-track { height: 6px; background: rgba(128,128,128,0.15); border-radius: 3px; overflow: hidden; }
.score-bar { height: 100%; background: var(--score-color, var(--accent)); border-radius: 3px; transition: width 0.8s var(--ease-out-expo); }
```

### 仪表盘网格 (Dashboard Grid)

```css
.dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: var(--space-md); }
.dash-card { background: var(--bg-card); border-radius: var(--radius-md); padding: var(--space-lg); display: flex; flex-direction: column; justify-content: center; }
.dash-big-num { align-items: center; }
.dash-value { font-family: var(--font-display); font-size: var(--h2-size); font-weight: 700; color: var(--accent); line-height: 1; }
.dash-label { font-size: var(--caption-size); color: var(--text-secondary); margin-top: var(--space-xs); }
.dash-trend { font-size: var(--caption-size); margin-top: var(--space-xs); }
.dash-trend.up { color: var(--success); }
.dash-trend.down { color: var(--danger); }
.dash-pct { font-family: var(--font-display); font-size: var(--h4-size); font-weight: 700; color: var(--accent); line-height: 1; margin-bottom: var(--space-xs); }
.mini-bar-group { display: flex; align-items: flex-end; gap: 3px; height: 60px; margin-top: var(--space-sm); }
.mini-bar { flex: 1; background: var(--accent); border-radius: 2px 2px 0 0; min-height: 3px; opacity: 0.7; transition: height 0.6s var(--ease-out-expo); }
.mini-bar:last-child { opacity: 1; }
```

