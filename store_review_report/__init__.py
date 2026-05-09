#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Store Review Report Skill
=========================
数据驱动的门店经营复盘 Word 报告生成器。

两种使用模式：
    1. 数据驱动版：填入数据 → 自动生成精美报告
    2. 填空版：生成空白模板 → 供店长手动填写

暴露的主要接口：
    - StoreReviewReport      数据驱动报告生成器
    - StoreReviewData        总数据模型
    - CategoryData           品类数据模型
    - CostItem               费用项目模型
    - OperationMetric        运营指标模型
    - ActionItem             改善动作模型
"""

from .report_generator import (
    StoreReviewReport,
    StoreReviewData,
    CategoryData,
    CostItem,
    OperationMetric,
    ActionItem,
)

__all__ = [
    "StoreReviewReport",
    "StoreReviewData",
    "CategoryData",
    "CostItem",
    "OperationMetric",
    "ActionItem",
]
