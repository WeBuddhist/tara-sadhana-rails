---
title: English-Tibetan term list — TF-IDF top 60 (corrected)
source: 0-INBOX/temp/keyword-work/en-clean-scoped-tfidf.md
method: generate_en_translation_idf.py (english-keyword-extraction skill), scoped to the 122 in-scope translated blocks only
cutoff: top 60 terms by TF-IDF score, mirroring the final list size used in 21-taras-rails/.../ranked_keywords_top60.md
status: draft
supersedes: 0-INBOX/temp/keyword-work/en-bo-term-list.md (manually curated 24-term list, rejected)
---

# English-Tibetan term list — TF-IDF top 60

This replaces the earlier manually-filtered 24-term list. Selection is now purely mechanical: rank 1-60 by TF-IDF score against the Reuters-21578 baseline (see `en-clean-scoped-tfidf.md`), computed on the placeholder-stripped, scope-only English text. No term was added or dropped by hand.

**Important limitation, stated plainly:** the real 21-taras-rails methodology's dominant signal is commentary claim-density (60% of the composite score) — not available here since no commentaries are ingested into this vault. What follows is TF-IDF alone (their weakest signal, 'Presence'). One mechanical side-effect: several imperative/comparative English function words (please, like, every, possess, sake, perfectly, completely, without) score artificially high because Reuters news prose almost never uses second-person devotional imperatives — not a judgment call on my part, just what IDF-against-a-news-corpus does to devotional register. These are flagged below (category = grammar) rather than removed. **Your call whether to keep them in the Chinese glossary pass or drop them.**

## Content vocabulary (51 terms)

| # | English | Tibetan | Wylie | Note |
|---|---|---|---|---|
| 1 | jetsunma | རྗེ་བཙུན་མ | rje btsun ma | Core epithet of Tārā throughout §5 refrains |
| 2 | homage | ཕྱག་འཚལ / འདུད | phyag 'tshal / 'dud | SAME root verb as #5 'prostrate' — merge candidate |
| 3 | teachings | བསྟན་པ | bstan pa |  |
| 4 | beings | འགྲོ་བ / སེམས་ཅན | 'gro ba / sems can | two near-synonyms: 'migrators' vs 'sentient beings' |
| 5 | prostrate | ཕྱག་འཚལ | phyag 'tshal | SAME root verb as #2 'homage' — merge candidate |
| 7 | supreme | མཆོག | mchog |  |
| 8 | noble | འཕགས་མ | 'phags ma | SAME word as #17 'lady' — merge candidate |
| 9 | enlightenment | བྱང་ཆུབ | byang chub | distinct from #50 'enlightened (activity)' = ཕྲིན་ལས — do not conflate |
| 10 | grant | སྩོལ | stsol | refrain verb 'bestow'; 2-6 uses different verb གསོལ (request) |
| 11 | dharma | ཆོས | chos |  |
| 12 | mother | ཡུམ | yum |  |
| 13 | happiness | བདེ / བདེ་བ | bde / bde ba |  |
| 14 | pray | གསོལ་བ་འདེབས | gsol ba 'debs |  |
| 15 | lotus | པདྨ / ཆུ་སྐྱེས | pad+ma / chu skyes | two words: Skt. loanword vs. native 'water-born' kenning |
| 16 | wish-fulfilling | ཡིད་བཞིན | yid bzhin |  |
| 17 | lady | འཕགས་མ | 'phags ma | SAME word as #8 'noble' — merge candidate |
| 18 | wheel | འཁོར་ལོ | 'khor lo |  |
| 19 | hosts | སྡེ / ཚོགས | sde / tshogs | sde for Māra's forces, tshogs for general assemblies |
| 21 | existence | སྲིད་པ / འཁོར་བ | srid pa / 'khor ba | two senses: plain 'existence' vs 'cyclic existence' (samsara) — do not conflate |
| 22 | wisdom | ཤེས་རབ | shes rab | distinct from #53 'primordial wisdom' = ཡེ་ཤེས — do not conflate |
| 23 | ten | བཅུ | bcu | numeral |
| 24 | compassion | སྙིང་རྗེ / ཐུགས་རྗེ | snying rje / thugs rje | ordinary vs. honorific register |
| 25 | victors | རྒྱལ་བ | rgyal ba |  |
| 26 | realms | ཁམས | khams | cf. འཇིག་རྟེན ('jig rten, 'world') also sometimes glossed 'realm' |
| 27 | buddha | སངས་རྒྱས | sangs rgyas |  |
| 28 | perfect | རྫོགས་པ | rdzogs pa |  |
| 29 | attained | བརྙེས / ཐོབ་པ | brnyes / thob pa |  |
| 31 | refuge | སྐྱབས | skyabs |  |
| 32 | gods | ལྷ | lha |  |
| 34 | ocean | རྒྱ་མཚོ / ཆུ་གཏེར | rgya mtsho / chu gter | two words: standard 'ocean' vs. poetic 'water-treasury' |
| 35 | mind | སེམས / ཐུགས | sems / thugs | ordinary vs. honorific register; cf. བློ (blo) 'intellect' once |
| 36 | benefit | ཕན / དོན | phan / don | shares root དོན with #40 'sake' |
| 37 | profound | ཟབ(་མོ) | zab (mo) |  |
| 38 | accomplishments | དངོས་གྲུབ | dngos grub | siddhi |
| 39 | directions | ཕྱོགས | phyogs |  |
| 41 | accomplished | གྲུབ་པ | grub pa | shares root གྲུབ with #38 དངོས་གྲུབ |
| 42 | age | དུས | dus |  |
| 43 | life | སྲོག / ཚེ | srog / tshe | srog = life-force (often honorific སྐུ་སྲོག), tshe = lifespan |
| 45 | light | འོད | 'od |  |
| 47 | flourish | རྒྱས་པ | rgyas pa | shares root རྒྱས with #60 'vast' |
| 48 | liberation | ཐར་པ / སྨིན་གྲོལ | thar pa / smin grol | smin grol = compound 'ripening-and-liberation' |
| 49 | degenerate | སྙིགས་མ | snyigs ma |  |
| 50 | enlightened | ཕྲིན་ལས | phrin las | 'enlightened activity' — distinct from #9 'enlightenment' = བྱང་ཆུབ — do not conflate |
| 51 | adorned | བརྒྱན་པ | brgyan pa |  |
| 52 | cyclic | འཁོར་བ | 'khor ba | duplicate of #21's second sense (cyclic existence) — merge |
| 53 | primordial | ཡེ་ཤེས | ye shes | 'primordial wisdom' — distinct from #22 'wisdom' = ཤེས་རབ — do not conflate |
| 54 | moon | ཟླ་བ | zla ba |  |
| 56 | power | དབང / སྟོབས | dbang / stobs |  |
| 58 | eyes | སྤྱན | spyan | honorific register |
| 59 | infinite | མཐའ་ཡས | mtha' yas |  |
| 60 | vast | རྒྱས / རྒྱ་ཆེན | rgyas / rgya chen | shares root རྒྱས with #47 'flourish' |

## Grammatical / functional items (8 terms) — flagged, not removed

| # | English | Tibetan | Wylie | Note |
|---|---|---|---|---|
| 6 | please | ཤིག / ཅིག / ཞིག | shig / cig / zhig | imperative particle, not a lexical item |
| 20 | like | ལྟར / འདྲ | ltar / 'dra | comparative particle |
| 30 | every | ཐམས་ཅད / ཀུན | thams cad / kun | quantifier |
| 33 | possess | ལྡན(་པ) | ldan (pa) | possessive/endowment suffix, very high-frequency pattern |
| 40 | sake | དོན་སླད / ཕྱིར | don slad / phyir | postposition, shares root དོན with #36 'benefit' |
| 44 | perfectly | ལེགས་པར | legs par | adverb |
| 46 | completely | མ་ལུས | ma lus | lit. 'without remainder' — same formula as #57 'without' |
| 57 | without | མེད་པ / མ་ལུས | med pa / ma lus | negation; overlaps #46 'completely' |

## Proper names / untranslated epithets (1 term)

| # | English | Tibetan | Wylie | Note |
|---|---|---|---|---|
| 55 | ture | ཏུ་རེ | tu re | Skt. epithet of Tārā, transliterated not translated |

## Standardization findings surfaced by this pass

These are real one-Tibetan-word-to-two-English-glosses (or vice versa) cases the mechanical process surfaced, relevant to the original 'vocabulary standardization' goal:

- **homage (#2) and prostrate (#5)** both translate the same verb ཕྱག་འཚལ — the English draft alternates the gloss depending on context; the Chinese pass should pick one consistent rendering.
- **noble (#8) and lady (#17)** both translate འཕགས་མ — same situation.
- **existence (#21)** covers two distinct Tibetan words: སྲིད་པ (plain existence/becoming) and འཁོར་བ (cyclic existence / samsara, also ranked separately at #52 'cyclic'). These should NOT collapse to one Chinese term.
- **wisdom (#22)** = ཤེས་རབ (prajñā) is a different word from **primordial (#53, 'primordial wisdom')** = ཡེ་ཤེས (jñāna). Common conflation risk; keep distinct in Chinese (e.g. 智慧 vs. 智/本智).
- **enlightenment (#9)** = བྱང་ཆུབ (bodhi, the attainment) is a different word from **enlightened (#50, 'enlightened activity')** = ཕྲིན་ལས (the Buddha's/deity's deeds). Same English root, unrelated Tibetan words.
- **ocean (#34)** covers two words: རྒྱ་མཚོ (standard) and ཆུ་གཏེར (poetic 'water-treasury', used for 'ocean of compassion').
- **flourish (#47) and vast (#60)** share the root རྒྱས — worth a consistent Chinese rendering strategy for that root across contexts.
