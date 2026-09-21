#!/usr/bin/env python3
"""Apply the manually word-segmented \gla/\glb tokens in answers.json back
into the interlinear gloss file, using the same column_align/
compute_column_widths formatting logic as scaffold_gloss.py itself so the
output stays in the format that script's own --validate expects.

This does NOT call scaffold()/tokenise_source() (those regenerate \gla at
line-level from the source text) -- it replaces the \gla/\glb pair for
each block with the word/phrase-level tokens produced by the manual
segmentation pass, which is the step the interlinear-gloss skill itself
describes as the LLM-driven half.
"""
import json
import re
import sys
from pathlib import Path

SCRIPTS_DIR = Path(sys.argv[1])
sys.path.insert(0, str(SCRIPTS_DIR))
from scaffold_gloss import column_align, compute_column_widths  # noqa: E402

ANSWERS_PATH = Path(sys.argv[2])
GLOSS_PATH = Path(sys.argv[3])

answers = json.loads(ANSWERS_PATH.read_text(encoding="utf-8"))
text = GLOSS_PATH.read_text(encoding="utf-8")

pattern = re.compile(r"(^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$)", re.MULTILINE)
parts = pattern.split(text)

applied = []
missing = []
out = [parts[0]]
i = 1
while i < len(parts):
    heading = parts[i]
    block_id = parts[i + 1]
    section = parts[i + 2]
    if block_id in answers:
        entry = answers[block_id]
        gla_tokens = entry["gla"]
        glb_tokens = entry["glb"]
        assert len(gla_tokens) == len(glb_tokens), block_id
        widths = compute_column_widths([gla_tokens, glb_tokens])
        gla_line = column_align(gla_tokens, widths)
        glb_line = column_align(glb_tokens, widths)
        new_section, n1 = re.subn(
            r"^\\gla\s+.*$", "\\\\gla    " + gla_line.replace("\\", "\\\\"), section, count=1, flags=re.MULTILINE
        )
        new_section, n2 = re.subn(
            r"^\\glb\s+.*$", "\\\\glb    " + glb_line.replace("\\", "\\\\"), new_section, count=1, flags=re.MULTILINE
        )
        if n1 != 1 or n2 != 1:
            print(f"WARNING: could not find \\gla/\\glb lines to replace for {block_id}", file=sys.stderr)
        else:
            applied.append(block_id)
        section = new_section
    else:
        missing.append(block_id)
    out.append(heading)
    out.append(section)
    i += 3

GLOSS_PATH.write_text("".join(out), encoding="utf-8")
print(f"applied={len(applied)} missing_from_answers={len(missing)}")
if missing:
    print("blocks in gloss file but not in answers.json:", missing, file=sys.stderr)
