# -*- coding: utf-8 -*-
import json, os

ANSWERS_PATH = os.path.join(os.path.dirname(__file__), "answers.json")

def load():
    if os.path.exists(ANSWERS_PATH):
        with open(ANSWERS_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}

def save(d):
    with open(ANSWERS_PATH, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)

def add_batch(batch):
    d = load()
    for bid, (gla, glb) in batch.items():
        assert len(gla) == len(glb), f"{bid}: gla={len(gla)} glb={len(glb)}"
        d[bid] = {"gla": gla, "glb": glb}
    save(d)
    print(f"saved batch of {len(batch)} blocks; total so far: {len(d)}")
