#!/usr/bin/env python3
"""
品类映射引擎 — 独立版本，零外部依赖。

用法：
    from category_mapper import CategoryMapper, load_rules_from_config
    mapper = CategoryMapper(rules)
    df['品类'] = mapper.map_series(df['商品名称'])
"""

import re
from typing import List, Dict
import pandas as pd


class CategoryRule:
    """单个品类规则。"""

    def __init__(self, name: str, keywords: List[str], match_mode: str, priority: int = 999):
        self.name = name
        self.keywords = keywords
        self.match_mode = match_mode
        self.priority = priority


class CategoryMapper:
    """优先级排序的品类分类引擎。"""

    def __init__(self, rules: List[CategoryRule]):
        self.rules = sorted(rules, key=lambda r: r.priority)
        self.default_rule = None
        self._compiled_patterns = {}

        for r in self.rules:
            if r.match_mode == "default":
                self.default_rule = r
            elif r.match_mode == "regex":
                for i, kw in enumerate(r.keywords):
                    try:
                        self._compiled_patterns[(id(r), i)] = re.compile(kw)
                    except re.error:
                        pass

        if self.default_rule is None:
            raise ValueError("至少需要一条 default 规则作为兜底")

    def map_single(self, name: str) -> str:
        name = str(name)
        for rule in self.rules:
            if rule.match_mode == "default":
                continue
            if self._match_rule(name, rule):
                return rule.name
        return self.default_rule.name

    def map_series(self, names: pd.Series) -> pd.Series:
        return names.apply(self.map_single)

    def _match_rule(self, product_name: str, rule: CategoryRule) -> bool:
        if rule.match_mode == "contains":
            return any(kw in product_name for kw in rule.keywords)
        if rule.match_mode == "contains_ci":
            name_lower = product_name.lower()
            return any(kw.lower() in name_lower for kw in rule.keywords)
        if rule.match_mode == "regex":
            for i, kw in enumerate(rule.keywords):
                pattern = self._compiled_patterns.get((id(rule), i))
                if pattern is None:
                    try:
                        pattern = re.compile(kw)
                    except re.error:
                        continue
                if pattern.search(product_name):
                    return True
            return False
        return False


def load_rules_from_config(cfg: Dict) -> List[CategoryRule]:
    """从简化版 config dict 加载品类规则。"""
    rules = []
    for item in cfg.get("categories", []):
        rules.append(CategoryRule(
            name=item["name"],
            keywords=item.get("keywords", []),
            match_mode=item.get("match_mode", "default"),
            priority=item.get("priority", 999),
        ))
    return rules
