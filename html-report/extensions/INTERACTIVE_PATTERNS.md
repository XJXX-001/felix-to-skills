# Interactive & Dynamic Patterns

动态图表、交互动画、实时数据可视化扩展。遵循主技能的零依赖原则，所有实现内联在单文件中。

---

## 一、动态数据刷新（无需重载页面）

适用于需要实时更新数据的看板类报告。

### 数据轮询刷新

```javascript
// 定时更新指定元素的数值（模拟实时数据）
function startDataRefresh(selector, intervalMs = 5000) {
    const elements = document.querySelectorAll(selector);
    setInterval(() => {
        elements.forEach(el => {
            const target = parseFloat(el.dataset.target || el.textContent.replace(/,/g, ''));
            const variance = target * (Math.random() * 0.1 - 0.05); // ±5% 波动
            const newVal = Math.round(target + variance);
            animateValue(el, parseInt(el.textContent.replace(/,/g, '')), newVal, 800);
        });
    }, intervalMs);
}

// 用法：<div class="stat-value" data-target="15420">15,420</div>
// startDataRefresh('.stat-value[data-target]', 5000);
```

### 进度条动态更新

```javascript
// 动态更新进度条到新目标值
function updateProgress(fillEl, newPercent, duration = 800) {
    const current = parseFloat(fillEl.style.width) || 0;
    fillEl.style.width = current + '%';
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            fillEl.style.transition = `width ${duration}ms var(--ease-out-expo)`;
            fillEl.style.width = newPercent + '%';
        });
    });
}

// 用法：updateProgress(document.querySelector('.progress-fill'), 92);
```

### 环形图动态更新

```javascript
// 动态更新环形图到新百分比
function updateDonut(donutEl, newPercent, duration = 800) {
    const current = parseFloat(donutEl.style.getPropertyValue('--donut-pct')) || 0;
    const start = performance.now();
    function animate(now) {
        const progress = Math.min((now - start) / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);
        const val = current + (newPercent - current) * ease;
        donutEl.style.setProperty('--donut-pct', val);
        if (progress < 1) requestAnimationFrame(animate);
    }
    requestAnimationFrame(animate);
}

// 用法：updateDonut(document.querySelector('.chart-donut'), 85);
```

---

## 二、交互式图表组件

### 可点击柱状图（点击显示详情）

```css
.hbar-item.interactive { cursor: pointer; transition: transform 0.2s ease; }
.hbar-item.interactive:hover { transform: translateX(4px); }
.hbar-detail {
    max-height: 0; overflow: hidden; transition: max-height 0.3s ease;
    font-size: var(--small-size); color: var(--text-secondary);
    padding: 0 var(--space-md); opacity: 0;
}
.hbar-detail.open { max-height: 200px; opacity: 1; padding-top: var(--space-xs); }
```

```html
<div class="hbar-item interactive" onclick="this.querySelector('.hbar-detail').classList.toggle('open')">
    <div class="hbar-label">渠道 A</div>
    <div class="hbar-track"><div class="hbar-fill" style="width: 85%;"></div></div>
    <div class="hbar-value">85%</div>
</div>
<div class="hbar-detail">详细数据：转化率 12.3%，环比 +5.2%</div>
```

### Tab 切换数据视图

```css
.tab-group { display: flex; gap: 0; margin-bottom: var(--content-gap); }
.tab-btn {
    padding: var(--space-xs) var(--space-md); border: none; cursor: pointer;
    font-size: var(--small-size); color: var(--text-secondary);
    background: var(--bg-card); transition: all 0.2s ease;
}
.tab-btn:first-child { border-radius: var(--radius-sm) 0 0 var(--radius-sm); }
.tab-btn:last-child { border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }
.tab-btn.active { background: var(--accent); color: var(--bg-primary); font-weight: 600; }
.tab-panel { display: none; }
.tab-panel.active { display: block; animation: fadeIn 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
```

```html
<div class="tab-group">
    <button class="tab-btn active" onclick="switchTab(this, 'tab-overview')">概览</button>
    <button class="tab-btn" onclick="switchTab(this, 'tab-detail')">明细</button>
    <button class="tab-btn" onclick="switchTab(this, 'tab-trend')">趋势</button>
</div>
<div id="tab-overview" class="tab-panel active"><!-- 概览内容 --></div>
<div id="tab-detail" class="tab-panel"><!-- 明细内容 --></div>
<div id="tab-trend" class="tab-panel"><!-- 趋势内容 --></div>

<script>
function switchTab(btn, panelId) {
    btn.parentElement.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    btn.closest('.slide, .report-section').querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    document.getElementById(panelId).classList.add('active');
}
</script>
```

### 折叠/展开面板

```css
.collapsible-header {
    display: flex; align-items: center; justify-content: space-between;
    cursor: pointer; padding: var(--space-md); background: var(--bg-card);
    border-radius: var(--radius-sm); transition: background 0.2s ease;
}
.collapsible-header:hover { background: var(--bg-section-alt); }
.collapsible-arrow { transition: transform 0.3s ease; }
.collapsible-header.open .collapsible-arrow { transform: rotate(180deg); }
.collapsible-body {
    max-height: 0; overflow: hidden; transition: max-height 0.4s ease;
    padding: 0 var(--space-md);
}
.collapsible-body.open { max-height: 1000px; padding-top: var(--space-md); }
```

```html
<div class="collapsible-header" onclick="this.classList.toggle('open'); this.nextElementSibling.classList.toggle('open')">
    <h3>展开查看详情</h3>
    <span class="collapsible-arrow">▼</span>
</div>
<div class="collapsible-body">
    <p>详细内容在这里...</p>
</div>
```

---

## 三、入场动画增强

### 数字滚动（带千分位格式化）

```javascript
function animateValue(el, start, end, duration = 1500) {
    const startTime = performance.now();
    const isFloat = String(end).includes('.');
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);
        const current = start + (end - start) * ease;
        el.textContent = isFloat ? current.toFixed(1) : Math.floor(current).toLocaleString();
        if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
}

// IntersectionObserver 自动触发
const numObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const el = entry.target;
            const target = parseFloat(el.dataset.value || el.textContent.replace(/,/g, ''));
            animateValue(el, 0, target);
            numObserver.unobserve(el);
        }
    });
}, { threshold: 0.5 });
document.querySelectorAll('[data-value]').forEach(el => numObserver.observe(el));
```

```html
<!-- 用法：data-value 设置目标值，进入视口时自动从 0 滚动到目标 -->
<div class="stat-value" data-value="15420">0</div>
<div class="stat-value" data-value="92.5">0</div>
```

### 打字机效果

```css
.typewriter { overflow: hidden; border-right: 2px solid var(--accent); white-space: nowrap; }
.typewriter.visible { animation: typing 2s steps(30) forwards, blink 0.7s step-end infinite; }
@keyframes typing { from { width: 0; } to { width: 100%; } }
@keyframes blink { 50% { border-color: transparent; } }
```

### 进度条入场动画

```css
.progress-fill { transition: width 1.2s var(--ease-out-expo); }

// JS：先设为 0，进入视口后设为目标值
document.querySelectorAll('.progress-fill').forEach(el => {
    const target = el.style.width;
    el.style.width = '0';
    new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting) {
            requestAnimationFrame(() => requestAnimationFrame(() => { el.style.width = target; }));
        }
    }, { threshold: 0.5 }).observe(el);
});
```

### 翻牌效果（数字卡）

```css
.flip-card { perspective: 600px; }
.flip-inner {
    position: relative; transition: transform 0.6s var(--ease-out-expo);
    transform-style: preserve-3d;
}
.flip-card:hover .flip-inner { transform: rotateY(180deg); }
.flip-front, .flip-back { backface-visibility: hidden; }
.flip-back { position: absolute; inset: 0; transform: rotateY(180deg); }
```

---

## 四、数据可视化增强

### 实时时间戳

```javascript
// 更新元素显示当前时间
function startClock(selector, format = 'HH:mm:ss') {
    const el = document.querySelector(selector);
    setInterval(() => {
        const now = new Date();
        el.textContent = now.toLocaleTimeString('zh-CN', { hour12: false });
    }, 1000);
}
// 用法：startClock('#live-clock');
```

### 迷你图表（内联 SVG 动态生成）

```javascript
// 根据数组数据生成 sparkline SVG
function createSparkline(container, data, color = 'var(--accent)') {
    const width = 100, height = 30, padding = 2;
    const min = Math.min(...data), max = Math.max(...data);
    const range = max - min || 1;
    const points = data.map((v, i) => {
        const x = padding + (width - 2 * padding) * i / (data.length - 1);
        const y = height - padding - (height - 2 * padding) * (v - min) / range;
        return `${x.toFixed(1)},${y.toFixed(1)}`;
    }).join(' ');
    container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" style="width:100%;height:100%;">
            <polyline fill="none" stroke="${color}" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round" points="${points}"/>
            <circle cx="${width - padding}" cy="${height - padding - (height - 2 * padding) * (data[data.length-1] - min) / range}" r="3" fill="${color}"/>
        </svg>`;
}

// 用法：
// createSparkline(document.getElementById('spark1'), [20, 35, 28, 42, 38, 55, 48]);
```

### 热力网格动态高亮

```css
.hm-cell { transition: transform 0.2s ease, box-shadow 0.2s ease; cursor: pointer; }
.hm-cell:hover { transform: scale(1.1); box-shadow: 0 0 12px var(--accent-glow); z-index: 1; }
```

### 数据表格排序

```javascript
// 点击表头排序表格
function sortTable(table, colIndex, type = 'string') {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const dir = table.dataset.sortDir === 'asc' ? 'desc' : 'asc';
    table.dataset.sortDir = dir;
    rows.sort((a, b) => {
        let aVal = a.cells[colIndex].textContent.trim();
        let bVal = b.cells[colIndex].textContent.trim();
        if (type === 'number') { aVal = parseFloat(aVal.replace(/[^0-9.-]/g, '')); bVal = parseFloat(bVal.replace(/[^0-9.-]/g, '')); }
        if (dir === 'asc') return aVal > bVal ? 1 : -1;
        return aVal < bVal ? 1 : -1;
    });
    rows.forEach(r => tbody.appendChild(r));
}
```

```html
<table class="comparison-table" onclick="sortTable(this, event)">
    <thead><tr>
        <th onclick="sortTable(this.closest('table'), 0, 'string')">指标</th>
        <th onclick="sortTable(this.closest('table'), 1, 'number')">Q1</th>
        <th onclick="sortTable(this.closest('table'), 2, 'number')">Q2</th>
    </tr></thead>
</table>
```

---

## 五、全屏 PPT 交互扩展

### 画笔标注（PPT 演示模式）

```javascript
class SlideAnnotation {
    constructor() {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.drawing = false;
        this.color = 'var(--accent)';
        this.setup();
    }
    setup() {
        Object.assign(this.canvas.style, {
            position: 'fixed', inset: '0', zIndex: '9999',
            pointerEvents: 'none', cursor: 'crosshair'
        });
        document.body.appendChild(this.canvas);
        this.resize();
        window.addEventListener('resize', () => this.resize());
    }
    enable() {
        this.canvas.style.pointerEvents = 'auto';
        this.canvas.addEventListener('mousedown', this.startDraw.bind(this));
        this.canvas.addEventListener('mousemove', this.draw.bind(this));
        this.canvas.addEventListener('mouseup', () => this.drawing = false);
    }
    disable() {
        this.canvas.style.pointerEvents = 'none';
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
    startDraw(e) { this.drawing = true; this.ctx.beginPath(); this.ctx.moveTo(e.clientX, e.clientY); }
    draw(e) {
        if (!this.drawing) return;
        this.ctx.lineTo(e.clientX, e.clientY);
        this.ctx.strokeStyle = '#ff4757';
        this.ctx.lineWidth = 3;
        this.ctx.lineCap = 'round';
        this.ctx.stroke();
    }
    resize() { this.canvas.width = window.innerWidth; this.canvas.height = window.innerHeight; }
}

// 用法：按 D 键切换画笔模式
// const annotator = new SlideAnnotation();
// document.addEventListener('keydown', e => { if (e.key === 'd') annotator.enable(); else annotator.disable(); });
```

### 演讲者计时器

```css
.speaker-timer {
    position: fixed; bottom: clamp(1rem, 2vw, 2rem); left: clamp(1rem, 2vw, 2rem);
    font-family: var(--font-mono); font-size: var(--small-size);
    color: var(--text-secondary); opacity: 0.6; z-index: 100;
    background: var(--bg-card); padding: 0.25rem 0.5rem; border-radius: 4px;
}
```

```javascript
// 演讲计时器：显示已用时间
function startTimer(selector) {
    const el = document.querySelector(selector);
    const start = Date.now();
    setInterval(() => {
        const elapsed = Math.floor((Date.now() - start) / 1000);
        const min = Math.floor(elapsed / 60);
        const sec = elapsed % 60;
        el.textContent = `${String(min).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;
    }, 1000);
}
// 用法：<div class="speaker-timer" id="timer">00:00</div> + startTimer('#timer');
```

---

## 六、扩展引入方式

在模板的 `<script>` 块末尾按需添加：

```html
<script>
    // ... SlidePresentation 或其他基础脚本 ...

    // === 扩展模块（按需启用） ===
    // 数字滚动自动触发
    // document.querySelectorAll('[data-value]').forEach(el => numObserver.observe(el));

    // Tab 切换
    // 已在 HTML 中内联 onclick

    // 数据轮询刷新
    // startDataRefresh('.stat-value[data-target]', 5000);
</script>
```

---

## 设计约束

所有扩展遵循主技能原则：
- **零外部依赖** — 不引入 Chart.js、D3、GSAP 等库
- **CSS 变量驱动** — 复用 `:root` 中的颜色和间距变量
- **响应式兼容** — 移动端可用
- **尊重 reduced-motion** — 所有动画服从 `prefers-reduced-motion`
- **性能优先** — 使用 `requestAnimationFrame`，避免布局抖动
