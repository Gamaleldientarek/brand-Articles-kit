#!/usr/bin/env python3
"""Read-only copy checks. Findings are editorial signals, not authorship scores."""
import argparse
import json
import re
from pathlib import Path


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


def review(text, minimum=None, maximum=None):
    body = body_text(text)
    words = re.findall(r"[^\W_]+(?:['’-][^\W_]+)*", body, flags=re.UNICODE)
    issues = []
    checks = {
        "presentation_forms": r"[\ufb50-\ufdff\ufe70-\ufeff]",
        "tatweel": r"\u0640",
        "bidi_controls_review": r"[\u202a-\u202e\u2066-\u2069]",
        "dialect_or_heavy_word_review": r"(?<!\w)(?:وش|إيش|عشان|نصون)(?!\w)",
        "english_stock_phrase_review": r"\b(?:seamlessly|cutting-edge|revolutionary|delve|leverage|empower|elevate)\b",
    }
    for name, pattern in checks.items():
        for match in re.finditer(pattern, text, flags=re.I):
            issues.append({"kind": name, "line": text.count("\n", 0, match.start()) + 1,
                           "text": match.group()})
    if minimum is not None and len(words) < minimum:
        issues.append({"kind": "below_requested_length", "minimum": minimum})
    if maximum is not None and len(words) > maximum:
        issues.append({"kind": "above_requested_length", "maximum": maximum})
    return {"estimated_body_words": len(words), "issues": issues,
            "limitations": "Excludes headings/byline/Markdown citation labels. Keep metadata and briefs in separate files. Does not verify facts, SEO quality, originality or authorship. Review flags in quotations manually."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--min-words", type=int)
    parser.add_argument("--max-words", type=int)
    args = parser.parse_args()
    if any(v is not None and v < 0 for v in (args.min_words, args.max_words)):
        parser.error("Word limits cannot be negative")
    if args.min_words is not None and args.max_words is not None and args.min_words > args.max_words:
        parser.error("Minimum cannot exceed maximum")
    try:
        result = review(args.file.read_text(encoding="utf-8-sig"), args.min_words, args.max_words)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot read copy: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
