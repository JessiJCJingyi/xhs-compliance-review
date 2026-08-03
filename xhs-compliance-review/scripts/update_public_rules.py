#!/usr/bin/env python3
"""Record a public-source refresh check for the local Xiaohongshu terms file.

This script intentionally does not scrape private databases or submit user copy to
third-party checkers. It keeps the local terms metadata honest and can import
manually reviewed candidate terms from a JSON file.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TERMS_PATH = ROOT / "data" / "xhs_terms.json"


PUBLIC_SOURCES = [
    "https://www.zhanghaobang.cn/tools/word-checker",
    "https://weijincha.com/xhs/",
    "https://xhs.jvxiao.cn/",
    "https://ad.xiaohongshu.com/next_help/docs/8dc5bd9c45c9a90cb9912f3400d43f92",
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def merge_candidates(payload: dict, candidates: list[dict]) -> tuple[dict, int]:
    existing = {item["phrase"] for item in payload.get("terms", [])}
    added = 0
    for item in candidates:
        phrase = item.get("phrase")
        if not phrase or phrase in existing:
            continue
        payload.setdefault("terms", []).append(
            {
                "severity": item.get("severity", "yellow"),
                "category": item.get("category", "公开来源候选"),
                "phrase": phrase,
                "reason": item.get("reason", "公开来源/运营反馈中出现的风险表达"),
                "suggestion": item.get("suggestion", "发布前人工复核，并改成更中性的表达。"),
                "replacement": item.get("replacement", ""),
                "source": item.get("source", "manual-public-source"),
            }
        )
        existing.add(phrase)
        added += 1
    return payload, added


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh Xiaohongshu local terms metadata and import reviewed candidates.")
    parser.add_argument("--terms", type=Path, default=TERMS_PATH)
    parser.add_argument("--candidate-json", type=Path, help="JSON file containing a list of reviewed candidate term objects.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    payload = load_json(args.terms)
    added = 0
    if args.candidate_json:
        candidates_payload = load_json(args.candidate_json)
        candidates = candidates_payload if isinstance(candidates_payload, list) else candidates_payload.get("terms", [])
        payload, added = merge_candidates(payload, candidates)

    today = date.today().isoformat()
    old_version = str(payload.get("version", today))
    payload["updated_at"] = today
    payload["last_public_source_check_at"] = today
    payload["public_sources"] = PUBLIC_SOURCES
    if added:
        payload["version"] = f"{today}.manual-{added}"
    else:
        payload["version"] = old_version

    result = {"ok": True, "terms": str(args.terms), "added": added, "updated_at": today, "dry_run": args.dry_run}
    if not args.dry_run:
        save_json(args.terms, payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
