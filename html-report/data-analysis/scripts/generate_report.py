#!/usr/bin/env python3
"""
通用数据分析报告生成器
========================
读取两期 Excel 数据，执行对比分析，输出零依赖单文件 HTML 报告。

用法：
    python3 generate_report.py
    # 或指定配置文件：
    python3 generate_report.py --config my-config.yaml

依赖：pandas, openpyxl, pyyaml
安装：pip install pandas openpyxl pyyaml
"""

import argparse
import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime

from category_mapper import CategoryMapper, load_rules_from_config


def load_config(path: str = None) -> dict:
    """加载配置文件。优先级：参数 > 环境变量 > 默认值。"""
    import os
    if path is None:
        path = os.environ.get("REPORT_CONFIG", "config.yaml")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_css() -> str:
    """加载外部 CSS 文件并压缩。"""
    import re
    css_path = Path(__file__).parent.parent / "styles" / "base.css"
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    # 移除注释
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # 移除换行和多余空格
    css = re.sub(r'\s+', ' ', css)
    # 移除空格 around special characters
    css = re.sub(r'\s*([{:;])\s*', r'\1', css)
    # 移除逗号前后的空格
    css = re.sub(r'\s*,\s*', ',', css)
    # 移除 } 前的分号（CSS 规范中最后一个属性后面的分号是可选的）
    css = re.sub(r';}', '}', css)
    # 移除开头和结尾的空格
    css = css.strip()
    return css


def load_and_clean(file_path: str, year_label: str, cfg: dict) -> pd.DataFrame:
    """加载 Excel 并执行数据清洗。"""
    cols = cfg["data"]["columns"]
    exclude_staff = cfg["business_rules"].get("exclude_staff", [])
    exclude_stores = cfg["business_rules"].get("exclude_stores", [])

    df = pd.read_excel(file_path)

    # 排除指定员工和门店
    if exclude_staff:
        df = df[~df[cols["staff"]].isin(exclude_staff)]
    if exclude_stores:
        df = df[~df[cols["store"]].isin(exclude_stores)]

    # 数值清洗
    df["销售额"] = -df[cols["discounted_amount"]].astype(float)
    df["销量"] = df[cols["quantity"]].abs().astype(int)
    df["成本金额"] = df[cols["cost_amount"]].astype(float)
    df["毛利"] = df[cols["gross_margin"]].astype(float)
    df["年份"] = year_label

    # 品类映射
    rules = load_rules_from_config(cfg)
    mapper = CategoryMapper(rules)
    df["品类"] = mapper.map_series(df[cols["product"]])

    return df


def compute_kpi(df: pd.DataFrame) -> dict:
    total_sales = df["销售额"].sum()
    total_margin = df["毛利"].sum()
    total_qty = int(df["销量"].sum())
    return {
        "总销售额": total_sales,
        "总毛利": total_margin,
        "总销量": total_qty,
        "毛利率": round(total_margin / total_sales * 100, 2) if total_sales else 0,
        "客单价": round(total_sales / len(df), 2) if len(df) else 0,
        "单均毛利": round(total_margin / len(df), 2) if len(df) else 0,
        "交易笔数": len(df),
    }


def pct_change(new, old):
    if old == 0 or old is None:
        return None
    return round((new - old) / old * 100, 1)


def group_stats(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    g = df.groupby(group_col).agg({"销售额": "sum", "毛利": "sum", "销量": "sum"}).reset_index()
    g["毛利率"] = (g["毛利"] / g["销售额"] * 100).round(2)
    g["毛利排名"] = g["毛利"].rank(ascending=False, method="min").astype(int)
    g["销售额排名"] = g["销售额"].rank(ascending=False, method="min").astype(int)
    return g


def merge_comparison(df1: pd.DataFrame, df2: pd.DataFrame, group_col: str, label1: str, label2: str):
    """两期对比，返回含环比、排名变化的 DataFrame。"""
    rename1 = {"销售额": f"{label1}销售额", "毛利": f"{label1}毛利", "毛利率": f"{label1}毛利率",
               "毛利排名": f"{label1}毛利排名", "销售额排名": f"{label1}销售额排名"}
    rename2 = {"销售额": f"{label2}销售额", "毛利": f"{label2}毛利", "毛利率": f"{label2}毛利率",
               "毛利排名": f"{label2}毛利排名", "销售额排名": f"{label2}销售额排名"}

    merged = pd.merge(
        df1[[group_col] + list(rename1.keys())].rename(columns=rename1),
        df2[[group_col] + list(rename2.keys())].rename(columns=rename2),
        on=group_col, how="outer"
    ).fillna(0)

    merged["销售额环比"] = merged.apply(lambda r: pct_change(r[f"{label2}销售额"], r[f"{label1}销售额"]), axis=1)
    merged["毛利环比"] = merged.apply(lambda r: pct_change(r[f"{label2}毛利"], r[f"{label1}毛利"]), axis=1)
    merged["毛利排名变化"] = merged[f"{label1}毛利排名"] - merged[f"{label2}毛利排名"]
    merged["新"] = merged[f"{label1}销售额"] == 0
    return merged.sort_values(f"{label2}毛利", ascending=False)


def classify_health(df: pd.DataFrame, margin_col: str, growth_col: str, new_col: str):
    """人员健康度分类（过滤新员工后按中位数划分）。"""
    valid = df[~df[new_col]].copy()
    median_margin = valid[margin_col].median()
    median_growth = valid[growth_col].median()

    def _classify(row):
        if row[new_col]:
            return "新人"
        high_y = row[margin_col] >= median_margin
        high_x = row[growth_col] >= median_growth if row[growth_col] is not None else False
        if high_y and high_x: return "明星"
        if high_y and not high_x: return "预警"
        if not high_y and high_x: return "潜力"
        return "危险"

    df["健康度"] = df.apply(_classify, axis=1)
    return df


def classify_bcg(df: pd.DataFrame, share_col: str, growth_col: str):
    """品类 BCG 矩阵分类。"""
    median_share = df[share_col].median()
    median_growth = df[growth_col].median()

    def _classify(row):
        high_y = row[share_col] >= median_share
        high_x = row[growth_col] >= median_growth if row[growth_col] is not None else False
        if high_y and high_x: return "明星"
        if high_y and not high_x: return "现金牛"
        if not high_y and high_x: return "问题"
        return "瘦狗"

    df["战略定位"] = df.apply(_classify, axis=1)
    return df


# ==================== HTML 生成 ====================

def fmt_money(n):
    return f"¥{n:,.0f}"


def fmt_pct(n):
    if n is None:
        return "—"
    return f"{n:+.1f}%"


def fmt_pp(n):
    return f"{n:+.2f}pp"


def trend_class(n):
    if n is None:
        return "cell-neutral"
    return "cell-up" if n > 0 else "cell-down"


def trend_arrow(n):
    if n is None:
        return "—"
    return "▲" if n > 0 else "▼"


def build_html(cfg: dict, kpi1: dict, kpi2: dict, kpi_cmp: dict,
               store_chg: pd.DataFrame, person_chg: pd.DataFrame, cat_chg: pd.DataFrame,
               p1_label: str, p2_label: str) -> str:
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    report_cfg = cfg.get("report", {})
    title = report_cfg.get("title", "经营复盘报告")
    subtitle = report_cfg.get("subtitle", "")
    author = report_cfg.get("author", "数据分析部")

    # CSS
    css = load_css()

    parts = [f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>"""]

    def add(s): parts.append(s)

    # Cover
    add(f'''<section class="report-cover"><div class="cover-content">
<h1 class="cover-title reveal">{title}</h1>
<div class="cover-accent-line reveal"></div>
<p class="cover-subtitle reveal">{subtitle}</p>
<p class="cover-meta reveal">{datetime.now().strftime("%Y-%m")} · {author}</p>
</div></section>''')

    # 00 Overview
    store_col_name = cfg["data"]["columns"]["store"]
    staff_col_name = cfg["data"]["columns"]["staff"]
    add(f'''<section class="report-section"><div class="report-container reading">
<div class="section-heading reveal"><div class="section-number">00 / 数据概览</div><h2>分析基础</h2><p class="section-desc">数据来源、覆盖范围及基础统计信息。</p></div>
<div class="grid-2">
<div class="card reveal"><h4 style="color:var(--accent);margin-bottom:var(--space-md)">数据源信息</h4>
<table style="width:100%;border-collapse:collapse">
<tr style="border-bottom:1px solid rgba(128,128,128,0.1)"><td style="padding:var(--space-sm) var(--space-md);color:var(--text-secondary);font-size:var(--small-size);width:40%">分析周期</td><td style="padding:var(--space-sm) var(--space-md);color:var(--text-primary);font-weight:600">{report_cfg.get("period_label","")}</td></tr>
<tr style="border-bottom:1px solid rgba(128,128,128,0.1)"><td style="padding:var(--space-sm) var(--space-md);color:var(--text-secondary);font-size:var(--small-size)">{p1_label} 数据</td><td style="padding:var(--space-sm) var(--space-md);color:var(--text-primary)">{cfg["data"]["period1_file"]}</td></tr>
<tr style="border-bottom:1px solid rgba(128,128,128,0.1)"><td style="padding:var(--space-sm) var(--space-md);color:var(--text-secondary);font-size:var(--small-size)">{p2_label} 数据</td><td style="padding:var(--space-sm) var(--space-md);color:var(--text-primary)">{cfg["data"]["period2_file"]}</td></tr>
<tr><td style="padding:var(--space-sm) var(--space-md);color:var(--text-secondary);font-size:var(--small-size)">报告生成</td><td style="padding:var(--space-sm) var(--space-md);color:var(--text-primary)">{now_str}</td></tr>
</table></div>
<div class="card reveal"><h4 style="color:var(--accent);margin-bottom:var(--space-md)">覆盖范围统计</h4>
<div class="grid-2" style="margin-bottom:0">
<div class="stat-card reveal"><div class="stat-value" style="color:var(--accent)">{store_chg[store_col_name].nunique()}</div><div class="stat-label">对比门店</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--accent)">{person_chg[staff_col_name].nunique()}</div><div class="stat-label">对比人员</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--accent)">{cat_chg["品类"].nunique()}</div><div class="stat-label">分析品类</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--accent)">{kpi2["交易笔数"]}</div><div class="stat-label">总交易笔数</div></div>
</div></div>
</div>
</div></section>''')

    # 01 Executive Summary
    def tc(n): return trend_class(n)
    def ta(n): return trend_arrow(n)

    add(f'''<section class="report-section alt"><div class="report-container reading">
<div class="section-heading reveal"><div class="section-number">01 / 执行摘要</div><h2>核心指标概览</h2><p class="section-desc">{p2_label}期间关键经营指标与{p1_label}同期的对比分析。</p></div>
<div class="grid-3" style="margin-bottom:var(--space-xl)">
<div class="stat-card reveal"><div class="stat-value">{fmt_money(kpi2["总销售额"])}</div><div class="stat-label">本期总销售额</div><div class="stat-trend {'up' if (kpi_cmp['销售额变化'] or 0)>0 else 'down'}">{fmt_pct(kpi_cmp['销售额变化'])} vs {p1_label}</div></div>
<div class="stat-card reveal"><div class="stat-value">{fmt_money(kpi2["总毛利"])}</div><div class="stat-label">本期总毛利</div><div class="stat-trend {'up' if (kpi_cmp['毛利变化'] or 0)>0 else 'down'}">{fmt_pct(kpi_cmp['毛利变化'])} vs {p1_label}</div></div>
<div class="stat-card reveal"><div class="stat-value">{kpi2["总销量"]} 件</div><div class="stat-label">本期总销量</div><div class="stat-trend {'up' if (kpi_cmp['销量变化'] or 0)>0 else 'down'}">{fmt_pct(kpi_cmp['销量变化'])} vs {p1_label}</div></div>
<div class="stat-card reveal"><div class="stat-value">{kpi2["毛利率"]}%</div><div class="stat-label">本期毛利率</div><div class="stat-trend {'up' if kpi_cmp['毛利率变化']>0 else 'down'}">{fmt_pp(kpi_cmp['毛利率变化'])} vs {p1_label}</div></div>
<div class="stat-card reveal"><div class="stat-value">¥{kpi2["客单价"]:,.0f}</div><div class="stat-label">客单价</div><div class="stat-trend {'up' if (kpi_cmp['客单价变化'] or 0)>0 else 'down'}">{fmt_pct(kpi_cmp['客单价变化'])} vs {p1_label}</div></div>
<div class="stat-card reveal"><div class="stat-value">¥{kpi2["单均毛利"]:,.0f}</div><div class="stat-label">单均毛利</div><div class="stat-trend {'up' if (kpi_cmp['单均毛利变化'] or 0)>0 else 'down'}">{fmt_pct(kpi_cmp['单均毛利变化'])} vs {p1_label}</div></div>
</div>

<div class="card reveal" style="margin-bottom:var(--space-lg)">
<h4 style="color:var(--text-primary);margin-bottom:var(--space-md)">两期 KPI 对比明细</h4>
<div class="table-responsive">
<table class="comparison-table">
<thead><tr><th style="text-align:left">指标</th><th style="text-align:right">{p1_label}</th><th style="text-align:right">{p2_label}</th><th style="text-align:right">变化</th><th style="text-align:center">趋势</th></tr></thead>
<tbody>
<tr><td style="text-align:left;font-weight:600">总销售额</td><td style="text-align:right">{fmt_money(kpi1["总销售额"])}</td><td style="text-align:right">{fmt_money(kpi2["总销售额"])}</td><td style="text-align:right" class="{tc(kpi_cmp['销售额变化'])}">{fmt_pct(kpi_cmp['销售额变化'])}</td><td style="text-align:center">{ta(kpi_cmp['销售额变化'])}</td></tr>
<tr><td style="text-align:left;font-weight:600">总毛利</td><td style="text-align:right">{fmt_money(kpi1["总毛利"])}</td><td style="text-align:right">{fmt_money(kpi2["总毛利"])}</td><td style="text-align:right" class="{tc(kpi_cmp['毛利变化'])}">{fmt_pct(kpi_cmp['毛利变化'])}</td><td style="text-align:center">{ta(kpi_cmp['毛利变化'])}</td></tr>
<tr><td style="text-align:left;font-weight:600">总销量</td><td style="text-align:right">{kpi1["总销量"]} 件</td><td style="text-align:right">{kpi2["总销量"]} 件</td><td style="text-align:right" class="{tc(kpi_cmp['销量变化'])}">{fmt_pct(kpi_cmp['销量变化'])}</td><td style="text-align:center">{ta(kpi_cmp['销量变化'])}</td></tr>
<tr><td style="text-align:left;font-weight:600">毛利率</td><td style="text-align:right">{kpi1["毛利率"]}%</td><td style="text-align:right">{kpi2["毛利率"]}%</td><td style="text-align:right" class="{tc(kpi_cmp['毛利率变化'])}">{fmt_pp(kpi_cmp['毛利率变化'])}</td><td style="text-align:center">{ta(kpi_cmp['毛利率变化'])}</td></tr>
<tr><td style="text-align:left;font-weight:600">客单价</td><td style="text-align:right">¥{kpi1["客单价"]:,.0f}</td><td style="text-align:right">¥{kpi2["客单价"]:,.0f}</td><td style="text-align:right" class="{tc(kpi_cmp['客单价变化'])}">{fmt_pct(kpi_cmp['客单价变化'])}</td><td style="text-align:center">{ta(kpi_cmp['客单价变化'])}</td></tr>
</tbody>
</table>
</div>
</div>

<div class="callout callout-warning reveal">
<span class="callout-icon">&#9888;</span>
<div><strong>核心风险：毛利率承压。</strong>{p2_label}年销售额同比增长 <strong>{fmt_pct(kpi_cmp['销售额变化'])}</strong>，但毛利率从 <strong>{kpi1['毛利率']}%</strong> 下滑至 <strong>{kpi2['毛利率']}%</strong>（降幅 {abs(kpi_cmp['毛利率变化']):.2f} 个百分点）。销量基本持平（{fmt_pct(kpi_cmp['销量变化'])}），增长主要由高客单价驱动，但产品结构向低毛利品类倾斜。</div>
</div>
</div></section>''')

    # 02 Store & Person
    store_col = cfg["data"]["columns"]["store"]
    staff_col = cfg["data"]["columns"]["staff"]

    srows = ""
    for i, (_, r) in enumerate(store_chg.iterrows(), 1):
        badge = ""
        if i == 1: badge = '<span class="rank-badge rank-1">1</span> '
        elif i == 2: badge = '<span class="rank-badge rank-2">2</span> '
        elif i == 3: badge = '<span class="rank-badge rank-3">3</span> '
        new_tag = ' <span style="color:var(--warning);font-size:var(--caption-size)">[新店]</span>' if r["新"] else ""
        rc = "—" if r["新"] else f'<span class="{tc(r["毛利排名变化"])}">{ta(r["毛利排名变化"])} {r["毛利排名变化"]:+.0f}</span>'
        srows += f'<tr><td style="text-align:left;font-weight:600">{badge}{r[store_col]}{new_tag}</td><td style="text-align:right">{fmt_money(r[f"{p1_label}销售额"])}</td><td style="text-align:right">{fmt_money(r[f"{p2_label}销售额"])}</td><td style="text-align:right">{fmt_money(r[f"{p1_label}毛利"])}</td><td style="text-align:right">{fmt_money(r[f"{p2_label}毛利"])}</td><td style="text-align:right">{r[f"{p1_label}毛利率"]:.2f}%</td><td style="text-align:right">{r[f"{p2_label}毛利率"]:.2f}%</td><td style="text-align:center">{rc}</td></tr>'

    prows = ""
    for i, (_, r) in enumerate(person_chg.iterrows(), 1):
        badge = ""
        if i == 1: badge = '<span class="rank-badge rank-1">1</span> '
        elif i == 2: badge = '<span class="rank-badge rank-2">2</span> '
        elif i == 3: badge = '<span class="rank-badge rank-3">3</span> '
        new_tag = ' <span style="color:var(--warning);font-size:var(--caption-size)">[新]</span>' if r["新"] else ""
        rc = f'<span class="{tc(r["毛利排名变化"])}">{ta(r["毛利排名变化"])} {r["毛利排名变化"]:+.0f}</span>'
        mc = "—" if r["新"] else f'<span class="{tc(r["毛利环比"])}">{fmt_pct(r["毛利环比"])}</span>'
        rank_display = badge if badge else f'<span style="color:var(--text-secondary)">{i}</span>'
        prows += f'<tr><td style="text-align:center">{rank_display}</td><td style="text-align:left;font-weight:600">{r[staff_col]}{new_tag}</td><td style="text-align:right">{fmt_money(r[f"{p2_label}毛利"])}</td><td style="text-align:right">{fmt_money(r[f"{p2_label}销售额"])}</td><td style="text-align:right">{r[f"{p2_label}毛利率"]:.2f}%</td><td style="text-align:right">{mc}</td><td style="text-align:center">{rc}</td></tr>'

    add(f'''<section class="report-section"><div class="report-container">
<div class="section-heading reveal"><div class="section-number">02 / 门店与个人排名</div><h2>门店与个人排名</h2><p class="section-desc">按门店及个人维度统计毛利额、销售额、毛利率，并在两期间进行排名对比。</p></div>
<h3 class="reveal" style="margin-bottom:var(--space-md);color:var(--text-primary)">门店毛利对比</h3>
<div class="card reveal" style="margin-bottom:var(--space-xl)">
<div class="table-responsive"><table class="comparison-table">
<thead><tr><th style="text-align:left">门店</th><th style="text-align:right">{p1_label}销售额</th><th style="text-align:right">{p2_label}销售额</th><th style="text-align:right">{p1_label}毛利</th><th style="text-align:right">{p2_label}毛利</th><th style="text-align:right">{p1_label}毛利率</th><th style="text-align:right">{p2_label}毛利率</th><th style="text-align:center">毛利排名变化</th></tr></thead>
<tbody>{srows}</tbody>
</table></div>
</div>
<h3 class="reveal" style="margin-bottom:var(--space-md);color:var(--text-primary)">个人排名榜单（按{p2_label}毛利额降序）</h3>
<div class="card reveal">
<div class="table-responsive"><table class="comparison-table">
<thead><tr><th style="text-align:center">排名</th><th style="text-align:left">职员名称</th><th style="text-align:right">{p2_label}毛利</th><th style="text-align:right">{p2_label}销售额</th><th style="text-align:right">{p2_label}毛利率</th><th style="text-align:right">毛利环比</th><th style="text-align:center">排名变化</th></tr></thead>
<tbody>{prows}</tbody>
</table></div>
</div>
</div></section>''')

    # 03 Diagnosis
    rising = person_chg[person_chg["毛利排名变化"] > 0].nlargest(3, "毛利排名变化")
    falling = person_chg[(person_chg[f"{p1_label}毛利"] > 0) & (person_chg["毛利排名变化"] < 0)].nsmallest(3, "毛利排名变化")

    rhtml = ""
    for _, r in rising.iterrows():
        rhtml += f'<li style="padding:var(--space-sm) 0;border-bottom:1px solid rgba(128,128,128,0.1)"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:var(--space-xs)"><span style="color:var(--text-primary);font-weight:600;font-size:var(--body-size)">{r[staff_col]}</span><span style="color:var(--success);font-weight:600;font-size:var(--small-size)">排名上升 {int(r["毛利排名变化"])} 位</span></div><div style="display:flex;gap:var(--space-md);font-size:var(--caption-size);color:var(--text-secondary)"><span>{p2_label}毛利: <strong style="color:var(--text-primary)">{fmt_money(r[f"{p2_label}毛利"])}</strong></span><span>环比: <strong style="color:var(--success)">{fmt_pct(r["毛利环比"])}</strong></span></div></li>'

    fhtml = ""
    for _, r in falling.iterrows():
        fhtml += f'<li style="padding:var(--space-sm) 0;border-bottom:1px solid rgba(128,128,128,0.1)"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:var(--space-xs)"><span style="color:var(--text-primary);font-weight:600;font-size:var(--body-size)">{r[staff_col]}</span><span style="color:var(--danger);font-weight:600;font-size:var(--small-size)">排名下降 {abs(int(r["毛利排名变化"]))} 位</span></div><div style="display:flex;gap:var(--space-md);font-size:var(--caption-size);color:var(--text-secondary)"><span>{p2_label}毛利: <strong style="color:var(--text-primary)">{fmt_money(r[f"{p2_label}毛利"])}</strong></span><span>环比: <strong style="color:var(--danger)">{fmt_pct(r["毛利环比"])}</strong></span></div></li>'

    strows = ""
    for _, r in store_chg.iterrows():
        st = "—" if r["新"] else fmt_pct(r["销售额环比"])
        mt = "—" if r["新"] else fmt_pct(r["毛利环比"])
        sc = "cell-neutral" if r["新"] else tc(r["销售额环比"])
        mc = "cell-neutral" if r["新"] else tc(r["毛利环比"])
        if r["新"]: status = '<span class="badge badge-star">新开业</span>'
        elif (r["销售额环比"] or 0) > 0 and (r["毛利环比"] or 0) > 0: status = '<span class="badge badge-star">增长</span>'
        else: status = '<span class="badge badge-warn">下滑</span>'
        nt = ' <span style="color:var(--warning);font-size:var(--caption-size)">[新店]</span>' if r["新"] else ""
        strows += f'<tr><td style="text-align:left;font-weight:600">{r[store_col]}{nt}</td><td style="text-align:right" class="{sc}">{st}</td><td style="text-align:right" class="{mc}">{mt}</td><td style="text-align:right">{r[f"{p2_label}毛利率"]:.2f}%</td><td style="text-align:center">{status}</td></tr>'

    best_s = store_chg.loc[store_chg["毛利环比"].idxmax()] if not store_chg.empty else None
    worst_s = store_chg.loc[store_chg["毛利环比"].idxmin()] if not store_chg.empty else None
    bs_name = best_s[store_col] if best_s is not None else "—"
    ws_name = worst_s[store_col] if worst_s is not None else "—"

    add(f'''<section class="report-section alt"><div class="report-container">
<div class="section-heading reveal"><div class="section-number">03 / 环比诊断与预警</div><h2>环比诊断与预警</h2><p class="section-desc">识别两期间变化趋势，定位上升明星与下滑预警人员及门店。</p></div>
<div class="grid-2" style="margin-bottom:var(--space-xl)">
<div class="card reveal"><h3 style="color:var(--success);margin-bottom:var(--space-md)">&#9650; 上升明星 TOP3</h3><ul class="bullet-list">{rhtml}</ul></div>
<div class="card reveal"><h3 style="color:var(--danger);margin-bottom:var(--space-md)">&#9660; 下滑预警 TOP3</h3><ul class="bullet-list">{fhtml}</ul></div>
</div>
<h3 class="reveal" style="margin-bottom:var(--space-md);color:var(--text-primary)">门店环比变化</h3>
<div class="card reveal" style="margin-bottom:var(--space-lg)">
<div class="table-responsive"><table class="comparison-table">
<thead><tr><th style="text-align:left">门店</th><th style="text-align:right">销售额环比</th><th style="text-align:right">毛利环比</th><th style="text-align:right">{p2_label}毛利率</th><th style="text-align:center">状态</th></tr></thead>
<tbody>{strows}</tbody>
</table></div>
</div>
<div class="callout callout-info reveal">
<span class="callout-icon">&#9432;</span>
<div><strong>门店诊断结论：</strong>本期增长最优门店为 <strong>{bs_name}</strong>，下滑最严重为 <strong>{ws_name}</strong>。建议重点跟进 {ws_name} 的客流转化、产品结构及周边竞争环境变化。</div>
</div>
</div></section>''')

    # 04 Category
    cat_cards = ""
    for cat in ["iPhone", "配件", "iPad", "Watch", "Mac", "服务"]:
        row = cat_chg[cat_chg["品类"] == cat]
        if row.empty: continue
        r = row.iloc[0]
        color = "var(--accent)" if cat=="iPhone" else "var(--info)" if cat=="配件" else "var(--warning)" if cat=="iPad" else "var(--success)" if cat=="Watch" else "#e056a0" if cat=="Mac" else "var(--bg-card)"
        cat_cards += f'<div class="card reveal" style="border-top:3px solid {color}"><h4 style="color:var(--text-primary);margin-bottom:var(--space-xs);font-size:var(--body-size)">{cat}</h4><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:var(--space-xs)"><span style="font-size:var(--h3-size);font-weight:700;color:var(--text-primary)">{fmt_money(r["本期毛利"])}</span><span style="font-size:var(--caption-size);color:var(--text-secondary)">{p2_label}毛利</span></div><div style="display:flex;gap:var(--space-sm);font-size:var(--caption-size);color:var(--text-secondary)"><span>毛利环比: <span class="{tc(r["毛利环比"])}">{fmt_pct(r["毛利环比"])}</span></span><span>毛利率: {r["本期毛利率"]:.2f}%</span></div><div style="margin-top:var(--space-sm);height:6px;background:rgba(255,255,255,0.05);border-radius:3px;overflow:hidden"><div style="height:100%;width:{min(r["本期毛利份额"]*2,100)}%;background:{color};border-radius:3px"></div></div><div style="font-size:var(--caption-size);color:var(--text-secondary);margin-top:var(--space-xs)">毛利份额: {r["本期毛利份额"]:.1f}%</div></div>'

    cat_rows = ""
    for i, (_, r) in enumerate(cat_chg.iterrows(), 1):
        badge = ""
        if i == 1: badge = '<span class="rank-badge rank-1">1</span> '
        elif i == 2: badge = '<span class="rank-badge rank-2">2</span> '
        elif i == 3: badge = '<span class="rank-badge rank-3">3</span> '
        cat_rows += f'<tr><td style="text-align:left;font-weight:600">{badge}{r["品类"]}</td><td style="text-align:right">{int(r["上期销量"])}</td><td style="text-align:right">{int(r["本期销量"])}</td><td style="text-align:right" class="{tc(r["销量环比"])}">{fmt_pct(r["销量环比"])}</td><td style="text-align:right">{fmt_money(r["上期销售额"])}</td><td style="text-align:right">{fmt_money(r["本期销售额"])}</td><td style="text-align:right" class="{tc(r["销售额环比"])}">{fmt_pct(r["销售额环比"])}</td><td style="text-align:right">{fmt_money(r["上期毛利"])}</td><td style="text-align:right">{fmt_money(r["本期毛利"])}</td><td style="text-align:right" class="{tc(r["毛利环比"])}">{fmt_pct(r["毛利环比"])}</td><td style="text-align:right" class="{tc(r["毛利率变化"])}">{fmt_pp(r["毛利率变化"])}</td></tr>'

    best_c = cat_chg.loc[cat_chg["毛利环比"].idxmax()] if not cat_chg.empty else None
    worst_c = cat_chg.loc[cat_chg["毛利环比"].idxmin()] if not cat_chg.empty else None
    bc_name = best_c["品类"] if best_c is not None else "—"
    wc_name = worst_c["品类"] if worst_c is not None else "—"

    add(f'''<section class="report-section"><div class="report-container">
<div class="section-heading reveal"><div class="section-number">04 / 品类销量与毛利迁移</div><h2>品类销量与毛利迁移</h2><p class="section-desc">按六大品类分析两期销量、销售额及毛利贡献的结构性迁移趋势。</p></div>
<div class="grid-3" style="margin-bottom:var(--space-xl)">{cat_cards}</div>
<h3 class="reveal" style="margin-bottom:var(--space-md);color:var(--text-primary)">品类数据明细</h3>
<div class="card reveal" style="margin-bottom:var(--space-xl)">
<div class="table-responsive"><table class="comparison-table">
<thead><tr><th style="text-align:left">品类</th><th style="text-align:right">{p1_label}销量</th><th style="text-align:right">{p2_label}销量</th><th style="text-align:right">销量环比</th><th style="text-align:right">{p1_label}销售额</th><th style="text-align:right">{p2_label}销售额</th><th style="text-align:right">销售额环比</th><th style="text-align:right">{p1_label}毛利</th><th style="text-align:right">{p2_label}毛利</th><th style="text-align:right">毛利环比</th><th style="text-align:right">毛利率变化</th></tr></thead>
<tbody>{cat_rows}</tbody>
</table></div>
</div>
<div class="callout callout-success reveal">
<span class="callout-icon">&#10003;</span>
<div><strong>品类迁移结论：</strong>{bc_name}品类毛利增长最为强劲（环比 {fmt_pct(best_c["毛利环比"]) if best_c is not None else "—"}），是本期利润贡献的主要增长引擎；{wc_name}品类毛利明显下滑（环比 {fmt_pct(worst_c["毛利环比"]) if worst_c is not None else "—"}），需重点审视其定价策略与销售转化效率。</div>
</div>
</div></section>''')

    # 05 Matrix
    hdist = person_chg["健康度"].value_counts().to_dict()
    bdist = cat_chg["战略定位"].value_counts().to_dict()

    hrows = ""
    for _, r in person_chg.iterrows():
        bc = {"明星": "badge-star", "预警": "badge-warn", "潜力": "badge-potential", "危险": "badge-danger", "新人": "badge-info"}.get(r["健康度"], "badge-neutral")
        mc = "—" if r["新"] else fmt_pct(r["毛利环比"])
        cc = "cell-neutral" if r["新"] else tc(r["毛利环比"])
        hrows += f'<tr><td style="text-align:left;font-weight:600">{r[staff_col]}</td><td style="text-align:right">{fmt_money(r[f"{p2_label}毛利"])}</td><td style="text-align:right">{r[f"{p2_label}毛利率"]:.2f}%</td><td style="text-align:right" class="{cc}">{mc}</td><td style="text-align:left"><span class="badge {bc}">{r["健康度"]}</span></td></tr>'

    brows = ""
    for _, r in cat_chg.iterrows():
        bc = {"明星": "badge-star", "现金牛": "badge-potential", "问题": "badge-danger", "瘦狗": "badge-warn"}.get(r["战略定位"], "badge-neutral")
        brows += f'<tr><td style="text-align:left;font-weight:600">{r["品类"]}</td><td style="text-align:right">{fmt_money(r["本期毛利"])}</td><td style="text-align:right">{r["本期毛利份额"]:.1f}%</td><td style="text-align:right" class="{tc(r["毛利环比"])}">{fmt_pct(r["毛利环比"])}</td><td style="text-align:left"><span class="badge {bc}">{r["战略定位"]}</span></td></tr>'

    add(f'''<section class="report-section alt"><div class="report-container">
<div class="section-heading reveal"><div class="section-number">05 / 战略矩阵诊断</div><h2>战略矩阵诊断</h2><p class="section-desc">运用健康度矩阵与波士顿矩阵双模型，定位人员与品类的战略价值象限。</p></div>
<h3 class="reveal" style="margin-bottom:var(--space-md);color:var(--text-primary)">人员健康度矩阵（毛利率 × 毛利环比）</h3>
<div class="grid-4" style="margin-bottom:var(--space-xl)">
<div class="stat-card reveal"><div class="stat-value" style="color:var(--success)">{hdist.get("明星",0)}</div><div class="stat-label">&#9733; 明星（高毛利 + 增长）</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--warning)">{hdist.get("预警",0)}</div><div class="stat-label">&#9888; 预警（高毛利 + 下滑）</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--info)">{hdist.get("潜力",0)}</div><div class="stat-label">&#9733; 潜力（低毛利 + 增长）</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--danger)">{hdist.get("危险",0)}</div><div class="stat-label">&#9762; 危险（低毛利 + 下滑）</div></div>
</div>
<h4 class="reveal" style="margin-bottom:var(--space-md);color:var(--text-primary)">人员健康度明细</h4>
<div class="card reveal" style="margin-bottom:var(--space-xl)">
<div class="table-responsive"><table class="comparison-table">
<thead><tr><th style="text-align:left">职员名称</th><th style="text-align:right">{p2_label}毛利</th><th style="text-align:right">{p2_label}毛利率</th><th style="text-align:right">毛利环比</th><th style="text-align:left">健康度</th></tr></thead>
<tbody>{hrows}</tbody>
</table></div>
</div>
<h3 class="reveal" style="margin-bottom:var(--space-md);color:var(--text-primary)">品类战略定位矩阵（毛利份额 × 毛利环比）</h3>
<div class="grid-4" style="margin-bottom:var(--space-xl)">
<div class="stat-card reveal"><div class="stat-value" style="color:var(--success)">{bdist.get("明星",0)}</div><div class="stat-label">&#9733; 明星（高增长 + 高份额）</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--info)">{bdist.get("现金牛",0)}</div><div class="stat-label">&#9822; 现金牛（低增长 + 高份额）</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--warning)">{bdist.get("问题",0)}</div><div class="stat-label">? 问题（高增长 + 低份额）</div></div>
<div class="stat-card reveal"><div class="stat-value" style="color:var(--danger)">{bdist.get("瘦狗",0)}</div><div class="stat-label">&#9762; 瘦狗（低增长 + 低份额）</div></div>
</div>
<h4 class="reveal" style="margin-bottom:var(--space-md);color:var(--text-primary)">品类战略定位明细</h4>
<div class="card reveal" style="margin-bottom:var(--space-xl)">
<div class="table-responsive"><table class="comparison-table">
<thead><tr><th style="text-align:left">品类</th><th style="text-align:right">{p2_label}毛利</th><th style="text-align:right">毛利份额</th><th style="text-align:right">毛利环比</th><th style="text-align:left">战略定位</th></tr></thead>
<tbody>{brows}</tbody>
</table></div>
</div>
<div class="callout callout-info reveal">
<span class="callout-icon">&#9432;</span>
<div><strong>战略诊断结论：</strong>人员层面：明星 {hdist.get("明星",0)} 人 / 危险 {hdist.get("危险",0)} 人，需对预警类人员开展专项辅导、对危险类人员关注流失风险。品类层面：现金牛 {bdist.get("现金牛",0)} 个 + 明星 {bdist.get("明星",0)} 个构成利润基本盘；问题品类 {bdist.get("问题",0)} 个具备增长潜力，瘦狗品类 {bdist.get("瘦狗",0)} 个需重新评估资源配置效率。</div>
</div>
</div></section>''')

    # 06 Action + Ending
    add(f'''<section class="report-section"><div class="report-container reading">
<div class="section-heading reveal"><div class="section-number">06 / 行动计划</div><h2>执行建议</h2><p class="section-desc">基于四层分析结论，聚焦毛利率修复和结构优化，制定可落地、可追踪的改进措施。</p></div>
<div class="grid-2" style="margin-bottom:var(--space-xl)">
<div>
<div class="card reveal" style="border-left:3px solid var(--success);margin-bottom:var(--space-lg)">
<h4 style="color:var(--success);margin-bottom:var(--space-sm)">&#9650; 立即行动</h4>
<ul style="list-style:none;display:flex;flex-direction:column;gap:var(--space-sm)">
<li style="font-size:var(--body-size);color:var(--text-secondary);line-height:1.6"><span style="color:var(--success);margin-right:0.5rem;font-weight:600">01</span><strong style="color:var(--text-primary)">毛利率修复：</strong>优化产品组合，提升高毛利品类主推权重，控制低毛利配件搭售比例。目标：毛利率回升至 9% 以上。</li>
<li style="font-size:var(--body-size);color:var(--text-secondary);line-height:1.6"><span style="color:var(--success);margin-right:0.5rem;font-weight:600">02</span><strong style="color:var(--text-primary)">人员复盘：</strong>对下滑预警人员开展一对一业绩复盘，分析客户结构与成交转化漏斗。</li>
<li style="font-size:var(--body-size);color:var(--text-secondary);line-height:1.6"><span style="color:var(--success);margin-right:0.5rem;font-weight:600">03</span><strong style="color:var(--text-primary)">门店诊断：</strong>对销售额环比下滑门店启动专项调研：周边竞争环境、客流变化、团队状态。</li>
</ul>
</div>
</div>
<div>
<div class="card reveal" style="border-left:3px solid var(--info);margin-bottom:var(--space-lg)">
<h4 style="color:var(--info);margin-bottom:var(--space-sm)">&#9733; 中期优化</h4>
<ul style="list-style:none;display:flex;flex-direction:column;gap:var(--space-sm)">
<li style="font-size:var(--body-size);color:var(--text-secondary);line-height:1.6"><span style="color:var(--info);margin-right:0.5rem;font-weight:600">01</span><strong style="color:var(--text-primary)">健康度看板：</strong>建立人员健康度周度追踪，标记明星/预警/潜力/危险四象限变化趋势。</li>
<li style="font-size:var(--body-size);color:var(--text-secondary);line-height:1.6"><span style="color:var(--info);margin-right:0.5rem;font-weight:600">02</span><strong style="color:var(--text-primary)">品类策略：</strong>评估服务品类定价策略、销售话术及客户推荐流程的优化空间。</li>
<li style="font-size:var(--body-size);color:var(--text-secondary);line-height:1.6"><span style="color:var(--info);margin-right:0.5rem;font-weight:600">03</span><strong style="color:var(--text-primary)">成功复制：</strong>提炼表现亮眼门店的开业主推策略，形成标准化 SOP 并在其他门店推广。</li>
</ul>
</div>
</div>
</div>
</div></section>

<section class="ending-section">
<h2 class="reveal">报告结束</h2>
<p class="reveal" style="color:var(--text-secondary)">本报告基于{p1_label}年与{p2_label}年销售明细数据生成</p>
<div class="cover-accent-line reveal" style="margin:var(--space-lg) auto"></div>
<div class="ending-meta reveal">{author} · 报告生成于 {now_str}</div>
</section>

<script>
(function(){{
  const observer=new IntersectionObserver((entries)=>{{
    entries.forEach(entry=>{{if(entry.isIntersecting){{entry.target.classList.add('visible')}}}})
  }},{{threshold:0.15,rootMargin:'0px 0px -30px 0px'}});
  document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
}})();
</script>
</body>
</html>
''')

    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description="通用数据分析报告生成器")
    parser.add_argument("--config", default=None, help="配置文件路径（默认：环境变量 REPORT_CONFIG 或 config.yaml）")
    args = parser.parse_args()

    cfg = load_config(args.config)
    base_dir = Path(args.config).parent if Path(args.config).parent != Path(".") else Path(".")

    p1_file = base_dir / cfg["data"]["period1_file"]
    p2_file = base_dir / cfg["data"]["period2_file"]
    p1_label = cfg["data"]["period1_label"]
    p2_label = cfg["data"]["period2_label"]

    print(f"📊 加载 {p1_label} 数据: {p1_file}")
    df1 = load_and_clean(str(p1_file), p1_label, cfg)
    print(f"   记录数: {len(df1)}")

    print(f"📊 加载 {p2_label} 数据: {p2_file}")
    df2 = load_and_clean(str(p2_file), p2_label, cfg)
    print(f"   记录数: {len(df2)}")

    # KPI
    kpi1 = compute_kpi(df1)
    kpi2 = compute_kpi(df2)
    kpi_cmp = {
        "销售额变化": pct_change(kpi2["总销售额"], kpi1["总销售额"]),
        "毛利变化": pct_change(kpi2["总毛利"], kpi1["总毛利"]),
        "销量变化": pct_change(kpi2["总销量"], kpi1["总销量"]),
        "毛利率变化": round(kpi2["毛利率"] - kpi1["毛利率"], 2),
        "客单价变化": pct_change(kpi2["客单价"], kpi1["客单价"]),
        "单均毛利变化": pct_change(kpi2["单均毛利"], kpi1["单均毛利"]),
    }

    # Group stats
    store_col = cfg["data"]["columns"]["store"]
    staff_col = cfg["data"]["columns"]["staff"]

    store1 = group_stats(df1, store_col)
    store2 = group_stats(df2, store_col)
    store_chg = merge_comparison(store1, store2, store_col, p1_label, p2_label)

    person1 = group_stats(df1, staff_col)
    person2 = group_stats(df2, staff_col)
    person_chg = merge_comparison(person1, person2, staff_col, p1_label, p2_label)

    cat1 = df1.groupby("品类").agg({"销售额": "sum", "毛利": "sum", "销量": "sum"}).reset_index()
    cat1["毛利率"] = (cat1["毛利"] / cat1["销售额"] * 100).round(2)
    cat2 = df2.groupby("品类").agg({"销售额": "sum", "毛利": "sum", "销量": "sum"}).reset_index()
    cat2["毛利率"] = (cat2["毛利"] / cat2["销售额"] * 100).round(2)

    cat_chg = pd.merge(
        cat1.rename(columns={"销售额": "上期销售额", "毛利": "上期毛利", "销量": "上期销量", "毛利率": "上期毛利率"}),
        cat2.rename(columns={"销售额": "本期销售额", "毛利": "本期毛利", "销量": "本期销量", "毛利率": "本期毛利率"}),
        on="品类", how="outer",
    ).fillna(0)
    cat_chg["销售额环比"] = cat_chg.apply(lambda r: pct_change(r["本期销售额"], r["上期销售额"]), axis=1)
    cat_chg["毛利环比"] = cat_chg.apply(lambda r: pct_change(r["本期毛利"], r["上期毛利"]), axis=1)
    cat_chg["销量环比"] = cat_chg.apply(lambda r: pct_change(r["本期销量"], r["上期销量"]), axis=1)
    cat_chg["毛利率变化"] = cat_chg["本期毛利率"] - cat_chg["上期毛利率"]
    cat_chg["本期毛利份额"] = (cat_chg["本期毛利"] / cat_chg["本期毛利"].sum() * 100).round(1)
    cat_chg = cat_chg.sort_values("本期毛利", ascending=False)

    # Classify
    person_chg = classify_health(person_chg, f"{p2_label}毛利率", "毛利环比", "新")
    cat_chg = classify_bcg(cat_chg, "本期毛利份额", "毛利环比")

    # Validate
    assert abs(store_chg[f"{p2_label}销售额"].sum() - kpi2["总销售额"]) < 0.01
    assert abs(store_chg[f"{p2_label}毛利"].sum() - kpi2["总毛利"]) < 0.01
    assert abs(person_chg[f"{p2_label}销售额"].sum() - kpi2["总销售额"]) < 0.01
    assert abs(cat_chg["本期销售额"].sum() - kpi2["总销售额"]) < 0.01
    assert abs(cat_chg["本期毛利"].sum() - kpi2["总毛利"]) < 0.01
    print("✅ 全部数据校验通过")

    # Build HTML
    html = build_html(cfg, kpi1, kpi2, kpi_cmp, store_chg, person_chg, cat_chg, p1_label, p2_label)

    out_dir = base_dir / cfg["output"]["report_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / cfg["output"]["report_filename"]
    out_path.write_text(html, encoding="utf-8")
    print(f"✅ 报告已生成: {out_path}")
    print(f"   文件大小: {out_path.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
