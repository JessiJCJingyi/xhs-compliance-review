#!/usr/bin/env python3
"""Quick Xiaohongshu/Rednote compliance scanner for Chinese social copy."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TERMS_PATH = ROOT / "data" / "xhs_terms.json"
FEEDBACK_PATH = ROOT / "data" / "review_feedback.jsonl"


@dataclass(frozen=True)
class Rule:
    severity: str
    category: str
    phrase: str
    reason: str
    suggestion: str
    replacement: str = ""
    source: str = "terms"


def load_terms(path: Path = DEFAULT_TERMS_PATH) -> tuple[list[Rule], list[str], list[str], dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rules = [
        Rule(
            severity=item["severity"],
            category=item["category"],
            phrase=item["phrase"],
            reason=item["reason"],
            suggestion=item["suggestion"],
            replacement=item.get("replacement", ""),
            source=item.get("source", "terms"),
        )
        for item in payload.get("terms", [])
    ]
    return rules, payload.get("disclaimers", []), payload.get("finance_hints", []), payload


def load_feedback_rules(path: Path = FEEDBACK_PATH) -> list[Rule]:
    if not path.exists():
        return []
    rules: list[Rule] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if item.get("type") != "limited_case":
            continue
        phrase = item.get("phrase")
        if not phrase:
            continue
        rules.append(
            Rule(
                severity=item.get("severity", "yellow"),
                category=item.get("category", "账号反馈"),
                phrase=phrase,
                reason=item.get("reason", "团队反馈中出现过限流/审核风险"),
                suggestion=item.get("suggestion", "发布前人工复核，并改成更中性的表达。"),
                replacement=item.get("replacement", ""),
                source="feedback",
            )
        )
    return rules


def normalize(text: str) -> str:
    return text.casefold()


def find_hits(text: str, rules: list[Rule]) -> list[dict]:
    normalized = normalize(text)
    hits = []
    occupied: list[tuple[int, int]] = []
    severity_rank = {"red": 0, "yellow": 1, "green": 2}
    sorted_rules = sorted(
        rules,
        key=lambda item: (-len(item.phrase), severity_rank.get(item.severity, 9), item.phrase),
    )
    for rule in sorted_rules:
        pattern = re.escape(rule.phrase.casefold())
        for match in re.finditer(pattern, normalized):
            start, end = match.span()
            if any(start < used_end and end > used_start for used_start, used_end in occupied):
                continue
            occupied.append((start, end))
            hits.append({**asdict(rule), "start": start, "end": end, "match": text[start:end]})
    hits.sort(key=lambda item: (item["start"], severity_rank.get(item["severity"], 9)))
    return hits


def infer_notes(text: str, hits: list[dict], disclaimers: list[str], finance_hints: list[str]) -> list[str]:
    notes = []
    has_finance = any(hint in text for hint in finance_hints)
    has_disclaimer = any(pattern in text for pattern in disclaimers)
    if has_finance and not has_disclaimer:
        notes.append("涉及投资/股票/收益语境，但没有看到“不构成投资建议”或等价免责声明。")
    if "AI" in text or "工具" in text or "产品" in text:
        notes.append("如作者与相关产品/公司有员工、创始人、投资人、联盟或合作关系，发布前确认是否需要披露。")
    if any(hit["category"] in {"未批准指标", "产品硬声称"} for hit in hits):
        notes.append("产品能力、准确率、收益率等指标需有内部批准来源；没有批准时不要发布。")
    if any(hit.get("source") == "feedback" for hit in hits):
        notes.append("命中了团队反馈沉淀词，说明历史上可能出现过限流、误解或人工审核风险。")
    return notes


def verdict(hits: list[dict], notes: list[str]) -> str:
    if any(hit["severity"] == "red" for hit in hits):
        return "禁止发"
    if hits or notes:
        return "修改后发"
    return "可以发"


def rewrite(text: str, rules: list[Rule]) -> str:
    rewritten = text
    replacements = {rule.phrase: rule.replacement for rule in rules if rule.replacement is not None}
    for phrase in sorted(replacements, key=len, reverse=True):
        replacement = replacements[phrase]
        if replacement == phrase:
            continue
        rewritten = re.sub(re.escape(phrase), replacement, rewritten, flags=re.IGNORECASE)
    return re.sub(r"\s{2,}", " ", rewritten).strip()


def format_markdown(result: dict) -> str:
    meta = result["terms_meta"]
    lines = [
        "# 小红书合规快审",
        "",
        f"结论：{result['verdict']}",
        f"词库版本：{meta.get('version', 'unknown')}（更新：{meta.get('updated_at', 'unknown')}）",
        "",
    ]
    if result["hits"]:
        lines.append("## 命中项")
        for hit in result["hits"]:
            source = "｜反馈词" if hit.get("source") == "feedback" else ""
            lines.append(
                f"- [{hit['severity']}] {hit['match']}｜{hit['category']}{source}｜{hit['reason']}｜建议：{hit['suggestion']}"
            )
        lines.append("")
    else:
        lines.extend(["## 命中项", "- 未命中内置高风险词。", ""])
    if result["notes"]:
        lines.append("## 人工复核")
        lines.extend(f"- {note}" for note in result["notes"])
        lines.append("")
    lines.extend(["## 建议改写", result["rewritten_text"].strip() or "(空)", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Review Xiaohongshu copy for risky words and compliance issues.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Copy text to review.")
    source.add_argument("--file", type=Path, help="Path to a UTF-8 text file.")
    parser.add_argument("--terms", type=Path, default=DEFAULT_TERMS_PATH, help="Path to terms JSON.")
    parser.add_argument("--include-feedback", action="store_true", default=True, help="Include feedback-derived terms.")
    parser.add_argument("--no-feedback", dest="include_feedback", action="store_false", help="Ignore feedback-derived terms.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of Markdown.")
    args = parser.parse_args()

    text = args.text if args.text is not None else args.file.read_text(encoding="utf-8")
    rules, disclaimers, finance_hints, meta = load_terms(args.terms)
    if args.include_feedback:
        rules = rules + load_feedback_rules()
    hits = find_hits(text, rules)
    notes = infer_notes(text, hits, disclaimers, finance_hints)
    result = {
        "verdict": verdict(hits, notes),
        "hits": hits,
        "notes": notes,
        "rewritten_text": rewrite(text, rules),
        "terms_meta": meta,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_markdown(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
