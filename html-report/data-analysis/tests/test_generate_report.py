#!/usr/bin/env python3
"""
generate_report.py 的单元测试。
"""

import sys
from pathlib import Path

# 添加 scripts 目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from generate_report import fmt_money, fmt_pct, fmt_pp, trend_class


def test_fmt_money():
    """测试金额格式化函数。"""
    assert fmt_money(1234567) == "¥1,234,567"
    assert fmt_money(0) == "¥0"
    assert fmt_money(100.6) == "¥101"  # 四舍五入到整数
    assert fmt_money(-500) == "¥-500"
    print("✓ test_fmt_money passed")


def test_fmt_pct():
    """测试百分比格式化函数。"""
    assert fmt_pct(0.1234) == "+0.1%"
    assert fmt_pct(-0.0567) == "-0.1%"
    assert fmt_pct(0) == "+0.0%"
    assert fmt_pct(None) == "—"
    print("✓ test_fmt_pct passed")


def test_fmt_pp():
    """测试百分点格式化函数。"""
    assert fmt_pp(0.1234) == "+0.12pp"
    assert fmt_pp(-0.0567) == "-0.06pp"
    assert fmt_pp(0) == "+0.00pp"
    print("✓ test_fmt_pp passed")


def test_trend_class():
    """测试趋势类名函数。"""
    assert trend_class(1.5) == "cell-up"
    assert trend_class(-0.5) == "cell-down"
    assert trend_class(0) == "cell-down"  # 0 被视为非正数
    assert trend_class(None) == "cell-neutral"
    print("✓ test_trend_class passed")


if __name__ == "__main__":
    test_fmt_money()
    test_fmt_pct()
    test_fmt_pp()
    test_trend_class()
    print("\n✓ All tests passed!")
