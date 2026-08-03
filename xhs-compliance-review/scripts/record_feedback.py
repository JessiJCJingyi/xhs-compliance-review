#!/usr/bin/env python3
"""Append Xiaohongshu review feedback and optionally promote a phrase to feedback terms."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FEEDBACK_PATH = ROOT / "data" / "review_feedback.jsonl"


def now_iso() -> str:
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).isoformat(timespec="seconds")


def append_event(event: dict, path: Path = FEEDBACK_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Record Xiaohongshu compliance feedback.")
    parser.add_argument("--type", choices=["limited_case", "passed_case", "false_positive", "note"], required=True)
    parser.add_argument("--text", help="Full copy text from Feishu/user feedback.")
    parser.add_argument("--phrase", help="Risk phrase to add or correct.")
    parser.add_argument("--severity", choices=["red", "yellow"], default="yellow")
    parser.add_argument("--category", default="账号反馈")
    parser.add_argument("--reason", default="团队反馈中出现过限流/审核风险")
    parser.add_argument("--suggestion", default="发布前人工复核，并改成更中性的表达。")
    parser.add_argument("--replacement", default="")
    parser.add_argument("--source", default="user-feedback")
    args = parser.parse_args()

    if args.type in {"limited_case", "false_positive"} and not (args.text or args.phrase):
        parser.error("--text or --phrase is required for limited_case/false_positive")

    event = {
        "created_at": now_iso(),
        "type": args.type,
        "text": args.text,
        "phrase": args.phrase,
        "severity": args.severity,
        "category": args.category,
        "reason": args.reason,
        "suggestion": args.suggestion,
        "replacement": args.replacement,
        "source": args.source,
    }
    append_event(event)
    print(json.dumps({"ok": True, "event": event, "path": str(FEEDBACK_PATH)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
