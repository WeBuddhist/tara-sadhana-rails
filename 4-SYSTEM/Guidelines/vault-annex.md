# Vault Annex — Zabtig Drolchok conventions

The methodology guidelines (`0-VAULT-Structure.md`, `../../1-SOURCES/About Sources.md`, `../../2-RAILS/About Rails.md`, `../../3-TRANSFORMATIONS/About Transformations.md`) are **text-agnostic** — they apply to any Railroads vault built on any classical text. This annex records the conventions that are specific to *this* vault: **ཟབ་ཏིག་སྒྲོལ་ཆོག (Zabtig Drolchok)**.

When the Guidelines and this annex disagree on a vault-specific detail, this annex wins.

---

## 1. The text

This vault serves **ཟབ་ཏིག་སྒྲོལ་ཆོག (Zabtig Drolchok)** — full title **དགོངས་གཏེར་སྒྲོལ་མའི་ཟབ་ཏིག་ལས། མཎྜལ་ཆོ་ག་ཚོགས་གཉིས་སྙིང་པོ** ("The Essence of the Two Accumulations Mandala Ritual, from the Profound Essence of Tārā's Mind-Treasure"), a Tārā sadhana/liturgy from the Gongter (mind-treasure) revelation tradition — combining supplications, a mandala offering ritual, praises to Tārā, and dedication practices.

Source-text files in `1-SOURCES/Text/` correspond to the following books / volumes:

| Order | Book / Volume | Filename |
| ----- | ------------- | -------- |
| 1 | ཟབ་ཏིག་སྒྲོལ་ཆོག (full liturgy, 10 sections) | `bo-ཟབ་ཏིག་སྒྲོལ་ཆོག.md` |

Only books that have been ingested are present in the folder. The primary text currently being railed out is the full liturgy.

A translation scope note — recording which blocks fall inside the current
translation job's verse-only scope, matched against a user-supplied excerpt —
is kept at `0-INBOX/temp/translation-scope.md`.

---

## 2. Addressing scheme

Standard `chapter-verse` scheme (see `CONVENTIONS.md` §1a in the shared skill library). Each of the 10 major sections of the liturgy is one "chapter"; verses/prose blocks within a section are numbered from 1, restarting at each section boundary.

**`verse_id_format`:** `chapter-verse`

**Format example:** `^1-1`, `^4-34`, `^10-3`

### Heading hierarchy

| Markdown | Role | Anchor |
| -------- | ---- | ------ |
| `#` | Whole-text title | `^0` |
| `##` | Section (1 of 10 major liturgy components) | `^N-0` |

No `###` / `####` levels are used — this text has a flat, single level of sections.

### Verse numbering rule

Verse/block numbers restart at 1 at the start of each of the 10 sections. Content before the first numbered verse of a section (rare) uses `^N-0`-style headings only, not a separate zero-block.

---

## 3. Registered commentary IDs

No commentaries have been ingested for this vault yet. When one is added, register it here with a `registered_id`, title, tier, language, and file path before it is cited in any rail.

---

## 4. Language tracks

| Tag | Language | Translation track | Plan stream |
| --- | -------- | ----------------- | ----------- |
| `bo` | Tibetan | — (source) | — |
| `en` | English | `3-TRANSFORMATIONS/Translations/Dharmamitra/en/` (machine-baseline zero-shot, scaffolding for keyword extraction) | — |
| `zh` | Chinese | `3-TRANSFORMATIONS/Translations/Dharmamitra/zh/` (final, standardized-vocabulary translation) | — |
