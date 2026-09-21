#!/usr/bin/env python3
"""Deterministic bo-zh raw-bilingual-glossary builder, adapted from this
vault's own build_raw_glossary.py (the bo-en version, itself adapted from
glossary-extract-raw's reference script for this vault's 2-tier \gla/\glb
Tibetan gloss data).

The only things that change between the bo-en and bo-zh versions are the
target-language frontmatter fields and the output/input file paths --
the keyword tally is still by *source* (Tibetan) lemma, so the same
Tibetan function-word skiplist applies unchanged regardless of which
target language the renderings are in.

Follows SKILL.md steps 3-6: tally by source token (= lemma, since no
separate morphology line exists), keep tokens attested in >=3 distinct
blocks, discard grammatical function words/particles/pronouns, order
renderings by frequency (ties by first-attestation block), and emit
2-4 sample pairings per keyword quoting the source token in its \gla
context and the \glb rendering.
"""
import csv
import re
from collections import defaultdict
from pathlib import Path

CSV_PATH = Path("0-INBOX/temp/bo-zh-pairs.csv")
GLOSS_PATH = Path("2-RAILS/Bilingual-Glossaries/Raw/bo-zh-gloss.md")
OUT_PATH = Path("2-RAILS/Bilingual-Glossaries/Raw/bo-zh.md")
MIN_FREQ = 3

# Same Tibetan-side skiplist as build_raw_glossary.py (bo-en) -- these are
# pure grammatical particles / case markers / connectives / pronouns on the
# SOURCE side, unrelated to which target language the renderings are in.
SKIP_LEMMAS = {
    "དང་", "ལ", "ལས", "ཐམས་ཅད", "ཁྱོད", "ཁྱོད་ལ", "ཡང", "ཁྱད་པར",
    "ཀུན་ཏུ", "མདོར་ན", "མ་ལུས", "རྣམ་པར", "བདག",
}

def block_sort_key(bid):
    parts = re.split(r"[-]", bid)
    out = []
    for p in parts:
        m = re.match(r"^(\d+)([A-Za-z]*)$", p)
        out.append((int(m.group(1)), m.group(2)) if m else (0, p))
    return out

# ---- pass 1: tally from CSV ----
rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
lemma_data = defaultdict(lambda: {
    "renderings": defaultdict(lambda: {"blocks": set(), "first_block": None}),
})
for r in rows:
    lemma = r["source_lemma"]
    rendering = r["target_rendering"]
    bid = r["block_id"]
    entry = lemma_data[lemma]["renderings"][rendering]
    entry["blocks"].add(bid)
    if entry["first_block"] is None or block_sort_key(bid) < block_sort_key(entry["first_block"]):
        entry["first_block"] = bid

keep = {}
for lemma, data in lemma_data.items():
    if lemma in SKIP_LEMMAS:
        continue
    total = sum(len(r["blocks"]) for r in data["renderings"].values())
    if total >= MIN_FREQ:
        keep[lemma] = data

# ---- pass 2: gather gla-context snippets per (lemma, block) for samples ----
BLOCK_HEADING_RE = re.compile(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", re.MULTILINE)
GLOSS_BLOCK_RE = re.compile(r"```gloss\s*\n(.*?)```", re.DOTALL)
text = GLOSS_PATH.read_text(encoding="utf-8")
parts = re.split(BLOCK_HEADING_RE, text)
gla_by_block = {}
glb_by_block = {}
for i in range(1, len(parts), 2):
    bid = parts[i]
    section = parts[i + 1] if i + 1 < len(parts) else ""
    m = GLOSS_BLOCK_RE.search(section)
    if not m:
        continue
    body = m.group(1)
    gm = re.search(r"^\\gla\s+(.*)$", body, re.MULTILINE)
    bm = re.search(r"^\\glb\s+(.*)$", body, re.MULTILINE)
    gla_by_block[bid] = gm.group(1).split() if gm else []
    glb_by_block[bid] = bm.group(1).split() if bm else []

def context_snippet(bid, token):
    gla = gla_by_block.get(bid, [])
    if token not in gla:
        return token
    idx = gla.index(token)
    lo = max(0, idx - 2)
    hi = min(len(gla), idx + 3)
    return " ".join(gla[lo:hi])

# ---- write output ----
lines = []
lines.append("---")
lines.append(f"gloss_file: 2-RAILS/Bilingual-Glossaries/Raw/{GLOSS_PATH.name}")
lines.append("source_file: 1-SOURCES/Text/bo-ཟབ་ཏིག་སྒྲོལ་ཆོག.md")
lines.append("target_file: 1-SOURCES/Translations/bo-ཟབ་ཏིག་སྒྲོལ་ཆོག-zh.md")
lines.append("source_language: bo")
lines.append("target_language: zh")
lines.append("language_pair: bo-zh")
lines.append("target_lang_tag: zh")
lines.append("translator: dharmamitra cat-translate v1")
lines.append(f"total_keywords: {len(keep)}")
lines.append("status: draft")
lines.append("ordering: renderings within each keyword are ordered by frequency descending; ties broken by first-attestation block order (rendering first attested in an earlier block wins).")
lines.append("---")
lines.append("")
lines.append("# Raw bilingual glossary — dharmamitra cat-translate v1 (machine-baseline)")
lines.append("")
lines.append(f"Extracted from the interlinear gloss file ({len(keep)} keywords with occurrence >= {MIN_FREQ} distinct blocks, function words/particles/pronouns excluded per SKILL.md).")
lines.append("")

for lemma in sorted(keep.keys(), key=lambda s: (s, s)):
    data = keep[lemma]
    lines.append(f"## {lemma}")
    lines.append("")
    lines.append("**Renderings attested in this source:**")
    lines.append("")
    lines.append("| Rendering | Frequency | First seen | Notes |")
    lines.append("|-----------|-----------|------------|-------|")
    ordered = sorted(
        data["renderings"].items(),
        key=lambda kv: (-len(kv[1]["blocks"]), block_sort_key(kv[1]["first_block"])),
    )
    for rendering, r in ordered:
        n = len(r["blocks"])
        fb = r["first_block"]
        lines.append(f"| {rendering.replace('_', ' ')} | {n} | ^{fb} | — |")
    lines.append("")
    lines.append("**Sample pairings:**")
    lines.append("")
    seen_blocks = set()
    picks = []
    for rendering, r in ordered:
        blocks_sorted = sorted(r["blocks"], key=block_sort_key)
        for b in blocks_sorted:
            if b in seen_blocks:
                continue
            picks.append((b, rendering))
            seen_blocks.add(b)
            break
        if len(picks) >= 3:
            break
    for b, rendering in picks:
        snippet = context_snippet(b, lemma)
        lines.append(f"> **^{b}** — *{snippet}*")
        lines.append(f'> → "{rendering.replace("_", " ")}"')
        lines.append(">")
    while lines and lines[-1] == ">":
        lines.pop()
    lines.append("")
    lines.append("---")
    lines.append("")

OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUT_PATH}: {len(keep)} keywords kept, {len(lemma_data)} lemmas seen before filter, skiplist={len(SKIP_LEMMAS)}")
