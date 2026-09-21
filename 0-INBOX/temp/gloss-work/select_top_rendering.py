#!/usr/bin/env python3
"""Pick the single most-frequent attested rendering per keyword from the
consolidated bilingual glossary.

This is NOT a run of the glossary-select skill: that skill requires a
track folder with requirements.md (a style/register rubric) under
3-TRANSFORMATIONS/Translation/<track-name>/, which does not exist yet for
this vault's bo-zh pair. Per the user's explicit choice ("just take the
most frequent attested rendering") this script instead applies only the
frequency-ordering half of glossary-select's step 3 procedure -- "sorted
by total frequency descending, the top row is the default candidate" --
with no rubric-based override/rejection logic, and writes a clearly-
labelled standalone table rather than the skill's real output artefact.
"""
import re
from pathlib import Path

IN_PATH = Path("2-RAILS/Bilingual-Glossaries/bo-zh.md")
OUT_PATH = Path("0-INBOX/temp/gloss-work/bo-zh-top-rendering.md")

text = IN_PATH.read_text(encoding="utf-8")
parts = re.split(r"(?m)^##\s+(.+?)\s*$", text)

def parse_table_rows(body):
    """Line-based markdown table row parser -- avoids '.' matching literal
    '|' characters inside cells, which a single cross-line regex is prone
    to (it will backtrack through cell boundaries looking for a digits
    match and silently swallow the header/separator rows)."""
    rows = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        cells = [c.strip() for c in line[1:-1].split("|")]
        if len(cells) != 4:
            continue
        if cells[0] == "Rendering":
            continue  # header row
        if set(cells[0]) <= {"-"}:
            continue  # separator row
        if not cells[2].isdigit():
            continue  # not a data row (defensive)
        rows.append(cells)
    return rows

rows = []
for i in range(1, len(parts), 2):
    kw = parts[i].strip()
    body = parts[i + 1] if i + 1 < len(parts) else ""
    data_rows = parse_table_rows(body)
    if not data_rows:
        continue
    top_rendering, sources, freq, _wiki = data_rows[0]
    rows.append((kw, top_rendering, sources, int(freq), len(data_rows)))

lines = []
lines.append("---")
lines.append("derived_from: 2-RAILS/Bilingual-Glossaries/bo-zh.md")
lines.append("method: most-frequent-attested-rendering (no requirements.md exists for a bo-zh track; this is NOT a glossary-select run)")
lines.append(f"total_keywords: {len(rows)}")
lines.append("status: draft")
lines.append("---")
lines.append("")
lines.append("# bo-zh top rendering per keyword (frequency-only pick)")
lines.append("")
lines.append("Not a per-track bilingual glossary in the rails sense -- no requirements.md/glossary-select rubric was applied, just the top-frequency row per keyword from the consolidated glossary.")
lines.append("")
lines.append("| Keyword (bo) | Chosen rendering (zh) | Frequency | Alternatives attested |")
lines.append("|---|---|---|---|")
for kw, rendering, sources, freq, n_alt in rows:
    lines.append(f"| {kw} | {rendering} | {freq} | {n_alt - 1} |")

OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {OUT_PATH}: {len(rows)} keywords")
