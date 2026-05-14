#!/usr/bin/env python3
"""
category_mapper.py 的单元测试。
"""

import sys
from pathlib import Path

# 添加 scripts 目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from category_mapper import CategoryRule, CategoryMapper, load_rules_from_config


def test_category_rule():
    """测试 CategoryRule 类。"""
    rule = CategoryRule(name="Mac", keywords=["mac", "macbook"], match_mode="contains_ci", priority=2)
    assert rule.name == "Mac"
    assert rule.keywords == ["mac", "macbook"]
    assert rule.match_mode == "contains_ci"
    assert rule.priority == 2
    print("✓ test_category_rule passed")


def test_category_mapper_contains():
    """测试 contains 匹配模式。"""
    rules = [
        CategoryRule(name="服务", keywords=["维修", "碎屏保"], match_mode="contains", priority=1),
        CategoryRule(name="其他", keywords=[], match_mode="default", priority=999),
    ]
    mapper = CategoryMapper(rules)
    
    assert mapper.map_single("iPhone 维修服务") == "服务"
    assert mapper.map_single("碎屏保套餐") == "服务"
    assert mapper.map_single("iPhone 15 Pro") == "其他"
    print("✓ test_category_mapper_contains passed")


def test_category_mapper_contains_ci():
    """测试 contains_ci 匹配模式（不区分大小写）。"""
    rules = [
        CategoryRule(name="Mac", keywords=["mac", "macbook"], match_mode="contains_ci", priority=2),
        CategoryRule(name="其他", keywords=[], match_mode="default", priority=999),
    ]
    mapper = CategoryMapper(rules)
    
    assert mapper.map_single("MacBook Pro 14") == "Mac"
    assert mapper.map_single("MAC Studio") == "Mac"
    assert mapper.map_single("iMac 24") == "Mac"
    assert mapper.map_single("iPhone 15 Pro") == "其他"
    print("✓ test_category_mapper_contains_ci passed")


def test_category_mapper_regex():
    """测试 regex 匹配模式。"""
    rules = [
        CategoryRule(name="Watch", keywords=["手表", "watch", "^(25|24)款 S"], match_mode="regex", priority=6),
        CategoryRule(name="其他", keywords=[], match_mode="default", priority=999),
    ]
    mapper = CategoryMapper(rules)
    
    # 注意：regex 匹配是区分大小写的
    assert mapper.map_single("Apple watch Series 9") == "Watch"
    assert mapper.map_single("25款 S9") == "Watch"
    assert mapper.map_single("24款 S8") == "Watch"
    assert mapper.map_single("iPhone 15 Pro") == "其他"
    print("✓ test_category_mapper_regex passed")


def test_category_mapper_priority():
    """测试优先级排序。"""
    rules = [
        CategoryRule(name="iPhone", keywords=["iphone"], match_mode="contains_ci", priority=4),
        CategoryRule(name="Mac", keywords=["mac"], match_mode="contains_ci", priority=2),
        CategoryRule(name="其他", keywords=[], match_mode="default", priority=999),
    ]
    mapper = CategoryMapper(rules)
    
    # Mac 优先级高于 iPhone
    assert mapper.map_single("MacBook Pro") == "Mac"
    assert mapper.map_single("iPhone 15 Pro") == "iPhone"
    print("✓ test_category_mapper_priority passed")


def test_category_mapper_default_required():
    """测试必须有 default 规则。"""
    rules = [
        CategoryRule(name="Mac", keywords=["mac"], match_mode="contains_ci", priority=2),
    ]
    
    try:
        mapper = CategoryMapper(rules)
        assert False, "应该抛出 ValueError"
    except ValueError as e:
        assert "至少需要一条 default 规则" in str(e)
    print("✓ test_category_mapper_default_required passed")


def test_load_rules_from_config():
    """测试从配置加载规则。"""
    cfg = {
        "categories": [
            {"name": "服务", "keywords": ["维修"], "match_mode": "contains", "priority": 1},
            {"name": "Mac", "keywords": ["mac"], "match_mode": "contains_ci", "priority": 2},
            {"name": "其他", "keywords": [], "match_mode": "default", "priority": 999},
        ]
    }
    
    rules = load_rules_from_config(cfg)
    assert len(rules) == 3
    assert rules[0].name == "服务"
    assert rules[1].name == "Mac"
    assert rules[2].name == "其他"
    print("✓ test_load_rules_from_config passed")


def test_category_mapper_invalid_regex():
    """测试无效正则表达式处理。"""
    rules = [
        CategoryRule(name="测试", keywords=["[invalid"], match_mode="regex", priority=1),
        CategoryRule(name="其他", keywords=[], match_mode="default", priority=999),
    ]
    mapper = CategoryMapper(rules)
    
    # 无效正则应该被忽略
    assert mapper.map_single("test") == "其他"
    print("✓ test_category_mapper_invalid_regex passed")


if __name__ == "__main__":
    test_category_rule()
    test_category_mapper_contains()
    test_category_mapper_contains_ci()
    test_category_mapper_regex()
    test_category_mapper_priority()
    test_category_mapper_default_required()
    test_load_rules_from_config()
    test_category_mapper_invalid_regex()
    print("\n✓ All tests passed!")
