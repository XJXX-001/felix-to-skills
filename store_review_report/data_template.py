#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据模板（空白版）
==================
复制此文件，修改 get_my_data() 中的内容，即可生成任意门店的复盘报告。

使用方式：
    from 经营复盘报告生成器 import StoreReviewReport
    from 数据模板_空白 import get_my_data

    data = get_my_data()
    report = StoreReviewReport(data)
    report.generate("输出路径.docx")
"""

from store_review_report import (
    StoreReviewData, CategoryData, CostItem,
    OperationMetric, ActionItem
)


def get_my_data() -> StoreReviewData:
    """填入你的门店数据，下方为示例结构，请全部替换为真实数据"""

    # ==================== 品类数据 ====================
    # 根据你的实际经营品类增删，不限数量
    # 示例：CategoryData("品类名", 目标, 实际, 上月, "单位", 是否核心)
    categories = [
        CategoryData("GMV", 0, 0, 0, "元", True),
        CategoryData("非手机销额", 0, 0, 0, "元"),
        CategoryData("手机", 0, 0, 0, "台", True),
        CategoryData("高端机", 0, 0, 0, "台"),
        CategoryData("主推", 0, 0, 0, "台"),
        CategoryData("笔记本", 0, 0, 0, "台"),
        CategoryData("平板", 0, 0, 0, "台"),
        CategoryData("黑白厨", 0, 0, 0, "元"),
        CategoryData("可穿戴", 0, 0, 0, "元"),
        CategoryData("生态链", 0, 0, 0, "元"),
    ]

    # ==================== 费用明细 ====================
    costs = [
        CostItem("固定费用", "房租", 0, "刚性支出，关注坪效"),
        CostItem("固定费用", "水电费", 0, "节能空间自查"),
        CostItem("固定费用", "装修摊销", 0, "一次性投入分摊"),
        CostItem("人力费用", "人员薪资", 0, "人均产出是否匹配"),
        CostItem("资金费用", "资金成本+贷款利息", 0, "库存资金代价，需加速周转"),
        CostItem("运营费用", "手续费", 0, "多渠道收款必要成本"),
        CostItem("运营费用", "后台摊销+其他", 0, "检视是否为必要支出"),
        CostItem("变动费用", "样机买断+少价", 0, "促销损耗，需控制"),
        CostItem("运营杂费", "运费/物品/保险等", 0, "小额费用亦不可忽视"),
    ]

    # ==================== 运营指标 ====================
    operation_metrics = [
        OperationMetric("客流量（人）", "上月值", "本月值", "诊断说明"),
        OperationMetric("转化率", "上月值", "本月值", "诊断说明"),
        OperationMetric("连带率", "上月值", "本月值", "诊断说明"),
        OperationMetric("融合订单", "上月值", "本月值", "诊断说明"),
        OperationMetric("新增粉", "上月值", "本月值", "诊断说明"),
    ]

    # ==================== 分析结论 ====================
    conclusions = [
        "结论1：请填写本月最核心的经营结论",
        "结论2：请填写第二重要的发现",
        "结论3：请填写第三项关键洞察",
    ]

    highlights = [
        "亮点1：达成率XX%，环比+XX%，成功经验...",
        "亮点2：...",
    ]

    weaknesses = [
        "短板1：达成率XX%，环比下滑XX%，原因...",
        "短板2：...",
    ]

    problems = [
        "问题1：核心问题描述",
        "问题2：次要问题描述",
    ]

    five_whys = [
        ("第1问：问题现象是什么？", "描述具体数据和事实"),
        ("第2问：为什么会发生？", "表面原因"),
        ("第3问：为什么会这样？", "中间层原因"),
        ("第4问：更深一层的原因是什么？", "接近本质的原因"),
        ("第5问：根本真因是什么？", "可执行、可改善的根本原因"),
    ]

    actions = [
        ActionItem("手机板块（重点补救）", "改善动作名称", "量化标准", "责任人", "期限"),
        ActionItem("短板品类攻坚", "改善动作名称", "量化标准", "责任人", "期限"),
        ActionItem("优势品类守住", "改善动作名称", "量化标准", "责任人", "期限"),
        ActionItem("过程管理", "改善动作名称", "量化标准", "责任人", "期限"),
    ]

    next_month_goals = [
        {"维度": "GMV", "基础目标": "≥XXX元", "挑战目标": "XXX元", "策略": "策略简述"},
        {"维度": "手机销量", "基础目标": "≥XX台", "挑战目标": "XX台", "策略": "策略简述"},
        {"维度": "利润", "基础目标": "扭亏为盈", "挑战目标": "≥X,000元", "策略": "策略简述"},
    ]

    reflection = (
        "请在此处填写经营者心灵日记，"
        "诚实面对经营结果，感谢团队付出，坚定下月决心。"
    )

    # ==================== 核心数据汇总 ====================
    # 请计算或从系统中提取以下核心指标
    gmv = 0                  # 本月GMV
    gmv_target = 0           # 目标GMV
    gmv_last_month = 0       # 上月GMV
    cost_total = sum(c.amount for c in costs)  # 费用合计（自动求和）
    rebate_rate = 0.10       # 返利率，如 10%
    rebate_amount = gmv * rebate_rate          # 返利金额（自动计算）
    profit = rebate_amount - cost_total        # 净利润（自动计算，如需手动填写请覆盖）

    return StoreReviewData(
        store_name="XX门店",
        review_month="2026年X月",
        author="店长姓名",
        date="2026年X月",
        gmv=gmv,
        gmv_target=gmv_target,
        gmv_last_month=gmv_last_month,
        profit=profit,
        cost_total=cost_total,
        rebate_amount=rebate_amount,
        rebate_rate=rebate_rate,
        categories=categories,
        costs=costs,
        operation_metrics=operation_metrics,
        conclusions=conclusions,
        highlights=highlights,
        weaknesses=weaknesses,
        problems=problems,
        five_whys=five_whys,
        actions=actions,
        next_month_goals=next_month_goals,
        reflection=reflection,
    )


if __name__ == "__main__":
    # 测试：生成空白模板报告
    from store_review_report import StoreReviewReport
    data = get_my_data()
    report = StoreReviewReport(data)
    report.generate("./门店经营复盘报告_空白模板.docx")
