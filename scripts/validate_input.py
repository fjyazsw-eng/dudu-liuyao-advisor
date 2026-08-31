#!/usr/bin/env python3
"""Basic completeness checker for human-readable Liu Yao chart text.

This script does not cast a chart or judge correctness. It reports whether the
text contains the minimum fields expected by the interpretation skill.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LINE_NAMES = ("初", "二", "三", "四", "五", "上")


def has_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def analyze(text: str) -> dict[str, object]:
    checks = {
        "question": has_any(text, (r"所问事项", r"所問事項", r"问题\s*[:：]", r"問.*何", r"问.*何")),
        "month": has_any(text, (r"月柱", r"月建", r"[寅卯辰巳午未申酉戌亥子丑]月")),
        "day": has_any(text, (r"日柱", r"日辰", r"[甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]日")),
        "void": has_any(text, (r"旬空", r"空亡")),
        "base_hexagram": has_any(text, (r"本卦", r"[乾坤震巽坎离離艮兑兌].*[乾坤震巽坎离離艮兑兌]")),
        "changed_hexagram": has_any(text, (r"变卦", r"變卦", r"之卦")),
        "shi": has_any(text, (r"世爻", r"[（(]?世[）)]?")),
        "ying": has_any(text, (r"应爻", r"應爻", r"[（(]?[应應][）)]?")),
        "moving_lines": has_any(text, (r"动爻", r"動爻", r"[〇○×ㄨ]", r"---\s*[oO]")),
    }

    detailed_lines = sorted(set(re.findall(r"【(初|二|三|四|五|上)爻】", text)))
    numbered_lines = sorted(set(re.findall(r"(?m)^\s*([1-6])[.、．]\s*【?(?:初|二|三|四|五|上)?爻", text)))
    six_lines_present = len(detailed_lines) == 6 or len(numbered_lines) == 6
    checks["six_lines"] = six_lines_present

    missing = [name for name, present in checks.items() if not present]
    warnings: list[str] = []

    if not checks["void"]:
        warnings.append("缺旬空：可做粗略判断，但空实与近端应期受限。")
    if not checks["six_lines"]:
        warnings.append("未稳定识别六条详细爻位；请确认初爻至上爻资料完整。")
    if checks["moving_lines"] and not checks["changed_hexagram"]:
        warnings.append("识别到动爻但未识别变卦，动变链可能不完整。")

    critical = {"question", "month", "day", "base_hexagram", "shi", "ying", "moving_lines", "six_lines"}
    ready = not any(item in critical for item in missing)

    return {
        "ready_for_full_analysis": ready,
        "checks": checks,
        "missing": missing,
        "warnings": warnings,
        "recognized_detailed_lines": detailed_lines,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Liu Yao chart text completeness.")
    parser.add_argument("input", type=Path, help="UTF-8 text file containing the chart")
    args = parser.parse_args()

    try:
        text = args.input.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"error": "read_failed", "message": str(exc)}, ensure_ascii=False))
        return 2

    print(json.dumps(analyze(text), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
