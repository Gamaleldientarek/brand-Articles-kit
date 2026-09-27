#!/usr/bin/env python3
"""Read-only copy checks. Findings are editorial signals, not authorship scores."""
import argparse
from collections import Counter
import json
import re
from pathlib import Path

ARABIC = r"؀-ۿݐ-ݿ"


def body_text(text):
    text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
    text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)
    text = re.sub(r"^\s*#{1,6}\s+.*$", "", text, flags=re.M)
    text = re.sub(r"^(?:By |بقلم ).*$", "", text, flags=re.M)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    # Citation labels are excluded; a linked body phrase is also excluded.
    # Therefore this is a reproducible estimate, not a linguistic word count.
    text = re.sub(r"\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text


# Each check is a regex over the full text. "_review" kinds need human judgment:
# quotations, calibration samples and legitimate uses can match.
CHECKS = {
    "presentation_forms": r"[\ufb50-\ufdff\ufe70-\ufeff]",
    "tatweel": r"\u0640",
    "bidi_controls_review": r"[\u202a-\u202e\u2066-\u2069]",
    "em_dash": r"[\u2014\u2015]",
    "emoji_review": r"[\U0001F300-\U0001FAFF\u2600-\u26ff\u2700-\u27bf]",
    "dialect_or_heavy_word_review": r"(?<!\w)(?:وش|إيش|عشان|نصون)(?!\w)",
    "english_stock_phrase_review": r"\b(?:seamless(?:ly)?|effortless(?:ly)?|cutting-edge|revolutionary|"
                                   r"game-chang(?:er|ing)|world-class|robust|truly|delve|leverag(?:e|es|ed|ing)|"
                                   r"empower(?:s|ed|ing)?|elevat(?:e|es|ed|ing)|unlock(?:s|ed|ing)?|tapestry)\b",
    "english_ai_pattern_review": r"\bin today'?s (?:fast-paced|rapidly|ever-changing|digital)\b"
                                 r"|\bnot (?:just|only|merely) [^.\n]{1,60}?,? but\b"
                                 r"|\bit'?s not (?:just |only )?[^.\n]{1,40}?[,;] it'?s\b"
                                 r"|\b(?:in conclusion|in summary|at the end of the day)\b"
                                 r"|\bnavigat(?:e|ing) the complexit",
    "arabic_ai_pattern_review": "|".join([
        "في عالم اليوم", "في ظل التطورات المتسارعة", "في عصر(?:نا)? الحالي",
        "(?:ليس|ليست|لم يعد|لم تعد)[^.،\n]{0,40}?مجرد", "لا يقتصر", "تجدر الإشارة",
        "من الجدير بالذكر", "مما لا شك فيه", "في الختام", "وختام(?:ًا|اً|ا)",
        "يلعب دور(?:ًا|اً|ا) (?:محوري|حيوي|مهم)", "نقلة نوعية"]),
}

RANGE_DASH = re.compile(r"[0-9\u0660-\u0669]\s*\u2013\s*[0-9\u0660-\u0669]")
SENTENCE_END = re.compile(r"(?<=[.!?؟])\s+")
FIRST_WORD = re.compile(r"[^\W\d_]+", re.UNICODE)


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def arabic_range_dashes(text):
    """An en dash is bidi class ON: in Arabic lines it can render 25-34 as 34-25."""
    issues = []
    for number, line in enumerate(text.split("\n"), start=1):
        if re.search(f"[{ARABIC}]", line):
            for match in RANGE_DASH.finditer(line):
                issues.append({"kind": "arabic_range_dash", "line": number, "text": match.group()})
    return issues


def repeated_openers(text, run=3):
    """Flag `run` or more consecutive sentences in one paragraph that start with the same word."""
    issues, offset = [], 0
    for paragraph in re.split(r"(\n\s*\n)", text):
        if paragraph.strip() and not paragraph.lstrip().startswith(("#", "-", "*", "|", ">")):
            openers = []
            for sentence in SENTENCE_END.split(paragraph.strip()):
                match = FIRST_WORD.search(sentence)
                openers.append(match.group().casefold() if match else None)
            streak = 1
            for previous, current in zip(openers, openers[1:]):
                streak = streak + 1 if current and current == previous else 1
                if streak == run:
                    issues.append({"kind": "repeated_opener_review",
                                   "line": line_of(text, offset + len(paragraph) - len(paragraph.lstrip())),
                                   "text": current})
        offset += len(paragraph)
    return issues


def review(text, minimum=None, maximum=None):
    body = body_text(text)
    words = re.findall(r"[^\W_]+(?:['\u2019-][^\W_]+)*", body, flags=re.UNICODE)
    issues = []
    for name, pattern in CHECKS.items():
        for match in re.finditer(pattern, text, flags=re.I):
            issues.append({"kind": name, "line": line_of(text, match.start()), "text": match.group()})
    issues.extend(arabic_range_dashes(text))
    issues.extend(repeated_openers(text))
    if minimum is not None and len(words) < minimum:
        issues.append({"kind": "below_requested_length", "minimum": minimum})
    if maximum is not None and len(words) > maximum:
        issues.append({"kind": "above_requested_length", "maximum": maximum})
    issues.sort(key=lambda issue: issue.get("line", float("inf")))
    return {"estimated_body_words": len(words),
            "issue_counts": dict(Counter(issue["kind"] for issue in issues)),
            "issues": issues,
            "limitations": "Excludes headings/byline/Markdown citation labels. Keep metadata and briefs in separate files. "
                           "Does not verify facts, SEO quality, originality or authorship. Kinds ending in _review can "
                           "match quotations or legitimate uses; judge them in context."}


def as_text(result):
    lines = [f"Estimated body words: {result['estimated_body_words']}"]
    if not result["issues"]:
        lines.append("No flags.")
    for issue in result["issues"]:
        where = f"line {issue['line']}: " if "line" in issue else ""
        detail = issue.get("text", issue.get("minimum", issue.get("maximum", "")))
        lines.append(f"- {where}{issue['kind']} {detail!r}")
    lines.append(result["limitations"])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--min-words", type=int)
    parser.add_argument("--max-words", type=int)
    parser.add_argument("--format", choices=["json", "text"], default="json")
    args = parser.parse_args()
    if any(v is not None and v < 0 for v in (args.min_words, args.max_words)):
        parser.error("Word limits cannot be negative")
    if args.min_words is not None and args.max_words is not None and args.min_words > args.max_words:
        parser.error("Minimum cannot exceed maximum")
    try:
        result = review(args.file.read_text(encoding="utf-8-sig"), args.min_words, args.max_words)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot read copy: {exc}\n")
    print(as_text(result) if args.format == "text" else json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
