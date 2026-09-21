---
title: TF-IDF Vocabulary Analysis — bo-ཟབ་ཏིག་སྒྲོལ་ཆོག-en
source: /sessions/rcw-011mhyqwtxjhdxwizpw481gz/mnt/tara-sadhana-rails/3-TRANSFORMATIONS/Translations/Dharmamitra/en/bo-ཟབ་ཏིག་སྒྲོལ་ཆོག-en.md
corpus: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth_idf=True)
method: TF × IDF — term frequency in translation vs. inverse document frequency in Reuters corpus
generated: 2026-09-21
unique_terms: 1095
total_content_tokens: 2,293
status: draft
---

# TF-IDF Vocabulary Analysis — bo-ཟབ་ཏིག་སྒྲོལ་ཆོག-en

Generated **2026-09-21** · source: `bo-ཟབ་ཏིག་སྒྲོལ་ཆོག-en.md` · **1,095 unique content terms** ranked.

This report answers two questions:

1. **Which words in this translation are most frequent here but rare in everyday English?**  
   → High TF-IDF score. These are the lexical signatures of the text.
2. **Which words appear in the text but are also very common in general English?**  
   → Low TF-IDF score. These look familiar but carry specialist meaning here.

---

## Methodology

**Term Frequency (TF)** — count of each word in the translation, normalised by total content-token count.
Frontmatter, verse markers (`^1-2`), numbers and markdown syntax are stripped before counting.

**Inverse Document Frequency (IDF)** — computed from the Reuters-21578 newswire corpus
(10,788 documents, ~1.3 M tokens) using sklearn's smooth IDF formula:
`idf(t) = log((1 + N) / (1 + df(t))) + 1`. Corpus maximum ≈ 9.59. Scale:

| IDF range | Meaning |
|-----------|---------|
| 1.0 – 1.5 | Function word — present in virtually every document |
| 1.5 – 3.0 | Common content word — high general-English frequency |
| 3.0 – 6.0 | Moderately rare — limited domain or register |
| 6.0 – 9.0 | Uncommon / archaic — rare in Reuters |
| 9.59 (max) | Absent from Reuters — domain-exclusive, coined, or Pāli |

**TF-IDF score** = TF × IDF × 10⁶ (scaled for readability).

**Colour bands** used in the table:

| Band | Score range | Interpretation |
|------|-------------|----------------|
| 🔴 | ≥ 50,000 | Text-exclusive — word essentially does not exist outside this translation |
| 🟠 | 10,000 – 49,999 | Domain-specific — Buddhist / Abhidhamma vocabulary |
| 🟡 | 3,000 – 9,999 | Specialist register — unusual in general English |
| 🟢 | 500 – 2,999 | Moderately distinctive — identifiable domain presence |
| 🔵 | 50 – 499 | Moderately common — has general English presence |
| ⚪ | 0 – 49 | Universal / function word |

---

## Distribution by Band

| Band | Terms | % of vocabulary |
|------|-------|----------------|
| 🔴 extremely high — text-exclusive | 10 | 0.9% |
| 🟠 very high — domain-specific | 152 | 13.9% |
| 🟡 high — specialist register | 786 | 71.8% |
| 🟢 medium — moderately distinctive | 147 | 13.4% |
| 🔵 low — common in general English | 0 | 0.0% |
| ⚪ very low — function / universal word | 0 | 0.0% |

---

## Most Distinctive Words (highest TF-IDF)

Words that appear **frequently in this text** yet are **rare or absent in general English**.

**1. translated** — count: 142, TF-IDF: 488,509, IDF: 7.888387 🔴 extremely high — text-exclusive
**2. jetsunma** — count: 33, TF-IDF: 138,016, IDF: 9.59 🔴 extremely high — text-exclusive
**3. homage** — count: 26, TF-IDF: 108,740, IDF: 9.59 🔴 extremely high — text-exclusive
**4. teachings** — count: 24, TF-IDF: 100,375, IDF: 9.59 🔴 extremely high — text-exclusive
**5. beings** — count: 20, TF-IDF: 83,646, IDF: 9.59 🔴 extremely high — text-exclusive
**6. prostrate** — count: 17, TF-IDF: 71,099, IDF: 9.59 🔴 extremely high — text-exclusive
**7. please** — count: 18, TF-IDF: 66,682, IDF: 8.494523 🔴 extremely high — text-exclusive
**8. supreme** — count: 20, TF-IDF: 62,371, IDF: 7.150788 🔴 extremely high — text-exclusive
**9. noble** — count: 15, TF-IDF: 60,103, IDF: 9.18767 🔴 extremely high — text-exclusive
**10. enlightenment** — count: 12, TF-IDF: 50,188, IDF: 9.59 🔴 extremely high — text-exclusive
**11. grant** — count: 16, TF-IDF: 47,814, IDF: 6.852295 🟠 very high — domain-specific
**12. dharma** — count: 11, TF-IDF: 46,005, IDF: 9.59 🟠 very high — domain-specific
**13. mother** — count: 11, TF-IDF: 46,005, IDF: 9.59 🟠 very high — domain-specific
**14. pray** — count: 10, TF-IDF: 41,823, IDF: 9.59 🟠 very high — domain-specific
**15. happiness** — count: 10, TF-IDF: 41,823, IDF: 9.59 🟠 very high — domain-specific
**16. lotus** — count: 10, TF-IDF: 40,068, IDF: 9.18767 🟠 very high — domain-specific
**17. wish-fulfilling** — count: 9, TF-IDF: 37,641, IDF: 9.59 🟠 very high — domain-specific
**18. lady** — count: 9, TF-IDF: 37,641, IDF: 9.59 🟠 very high — domain-specific
**19. wheel** — count: 8, TF-IDF: 33,469, IDF: 9.593135 🟠 very high — domain-specific
**20. hosts** — count: 8, TF-IDF: 33,458, IDF: 9.59 🟠 very high — domain-specific
**21. like** — count: 14, TF-IDF: 31,703, IDF: 5.192532 🟠 very high — domain-specific
**22. existence** — count: 9, TF-IDF: 30,015, IDF: 7.647225 🟠 very high — domain-specific
**23. wisdom** — count: 8, TF-IDF: 29,636, IDF: 8.494523 🟠 very high — domain-specific
**24. ten** — count: 11, TF-IDF: 29,547, IDF: 6.159148 🟠 very high — domain-specific
**25. victors** — count: 7, TF-IDF: 29,286, IDF: 9.593135 🟠 very high — domain-specific
**26. compassion** — count: 7, TF-IDF: 29,286, IDF: 9.593135 🟠 very high — domain-specific
**27. buddha** — count: 7, TF-IDF: 29,276, IDF: 9.59 🟠 very high — domain-specific
**28. realms** — count: 7, TF-IDF: 29,276, IDF: 9.59 🟠 very high — domain-specific
**29. attained** — count: 7, TF-IDF: 28,048, IDF: 9.18767 🟠 very high — domain-specific
**30. perfect** — count: 7, TF-IDF: 28,048, IDF: 9.18767 🟠 very high — domain-specific
**31. every** — count: 11, TF-IDF: 27,813, IDF: 5.797646 🟠 very high — domain-specific
**32. refuge** — count: 7, TF-IDF: 25,932, IDF: 8.494523 🟠 very high — domain-specific
**33. gods** — count: 6, TF-IDF: 25,094, IDF: 9.59 🟠 very high — domain-specific
**34. possess** — count: 6, TF-IDF: 25,094, IDF: 9.59 🟠 very high — domain-specific
**35. mind** — count: 8, TF-IDF: 24,948, IDF: 7.150788 🟠 very high — domain-specific
**36. ocean** — count: 8, TF-IDF: 24,948, IDF: 7.150788 🟠 very high — domain-specific
**37. benefit** — count: 10, TF-IDF: 24,166, IDF: 5.54135 🟠 very high — domain-specific
**38. accomplishments** — count: 6, TF-IDF: 24,041, IDF: 9.18767 🟠 very high — domain-specific
**39. profound** — count: 6, TF-IDF: 24,041, IDF: 9.18767 🟠 very high — domain-specific
**40. directions** — count: 6, TF-IDF: 23,288, IDF: 8.899988 🟠 very high — domain-specific
**41. sake** — count: 6, TF-IDF: 22,704, IDF: 8.676844 🟠 very high — domain-specific
**42. accomplished** — count: 6, TF-IDF: 22,227, IDF: 8.494523 🟠 very high — domain-specific
**43. age** — count: 6, TF-IDF: 21,824, IDF: 8.340372 🟠 very high — domain-specific
**44. life** — count: 9, TF-IDF: 21,616, IDF: 5.507159 🟠 very high — domain-specific
**45. perfectly** — count: 6, TF-IDF: 21,475, IDF: 8.206841 🟠 very high — domain-specific
**46. light** — count: 9, TF-IDF: 21,422, IDF: 5.457969 🟠 very high — domain-specific
**47. completely** — count: 7, TF-IDF: 21,122, IDF: 6.918987 🟠 very high — domain-specific
**48. liberation** — count: 5, TF-IDF: 20,918, IDF: 9.593135 🟠 very high — domain-specific
**49. flourish** — count: 5, TF-IDF: 20,918, IDF: 9.593135 🟠 very high — domain-specific
**50. degenerate** — count: 5, TF-IDF: 20,918, IDF: 9.593135 🟠 very high — domain-specific

---

## Least Distinctive Words (lowest TF-IDF)

Words that appear in this text but are also extremely common in general English.

**1. increase** — count: 1, TF-IDF: 1,541.73, IDF: 3.535181 🟢 medium — moderately distinctive
**2. made** — count: 1, TF-IDF: 1,570.18, IDF: 3.600421 🟢 medium — moderately distinctive
**3. offer** — count: 1, TF-IDF: 1,624.62, IDF: 3.725252 🟢 medium — moderately distinctive
**4. common** — count: 1, TF-IDF: 1,626.47, IDF: 3.729504 🟢 medium — moderately distinctive
**5. lower** — count: 1, TF-IDF: 1,704.25, IDF: 3.907856 🟢 medium — moderately distinctive
**6. next** — count: 1, TF-IDF: 1,706.48, IDF: 3.912963 🟢 medium — moderately distinctive
**7. cut** — count: 1, TF-IDF: 1,744.56, IDF: 4.000284 🟢 medium — moderately distinctive
**8. during** — count: 1, TF-IDF: 1,747.01, IDF: 4.005887 🟢 medium — moderately distinctive
**9. central** — count: 1, TF-IDF: 1,759.43, IDF: 4.034378 🟢 medium — moderately distinctive
**10. including** — count: 1, TF-IDF: 1,783.62, IDF: 4.089838 🟢 medium — moderately distinctive
**11. results** — count: 1, TF-IDF: 1,800.83, IDF: 4.129303 🟢 medium — moderately distinctive
**12. second** — count: 1, TF-IDF: 1,887.42, IDF: 4.327858 🟢 medium — moderately distinctive
**13. following** — count: 1, TF-IDF: 1,904.66, IDF: 4.367389 🟢 medium — moderately distinctive
**14. levels** — count: 1, TF-IDF: 1,921.39, IDF: 4.405749 🟢 medium — moderately distinctive
**15. subject** — count: 1, TF-IDF: 1,932.49, IDF: 4.43121 🟢 medium — moderately distinctive
**16. union** — count: 1, TF-IDF: 1,974.44, IDF: 4.527381 🟢 medium — moderately distinctive
**17. according** — count: 1, TF-IDF: 1,975.81, IDF: 4.53054 🟢 medium — moderately distinctive
**18. later** — count: 1, TF-IDF: 1,987.00, IDF: 4.556183 🟢 medium — moderately distinctive
**19. raised** — count: 1, TF-IDF: 2,004.33, IDF: 4.595923 🟢 medium — moderately distinctive
**20. currently** — count: 1, TF-IDF: 2,004.33, IDF: 4.595923 🟢 medium — moderately distinctive
**21. support** — count: 1, TF-IDF: 2,008.77, IDF: 4.60611 🟢 medium — moderately distinctive
**22. systems** — count: 1, TF-IDF: 2,023.91, IDF: 4.640835 🟢 medium — moderately distinctive
**23. reached** — count: 1, TF-IDF: 2,030.12, IDF: 4.655071 🟢 medium — moderately distinctive
**24. see** — count: 1, TF-IDF: 2,039.60, IDF: 4.676811 🟢 medium — moderately distinctive
**25. raise** — count: 1, TF-IDF: 2,049.30, IDF: 4.699034 🟢 medium — moderately distinctive
**26. line** — count: 1, TF-IDF: 2,049.30, IDF: 4.699034 🟢 medium — moderately distinctive
**27. among** — count: 1, TF-IDF: 2,054.22, IDF: 4.710333 🟢 medium — moderately distinctive
**28. need** — count: 1, TF-IDF: 2,055.88, IDF: 4.714128 🟢 medium — moderately distinctive
**29. saying** — count: 1, TF-IDF: 2,076.24, IDF: 4.760829 🟢 medium — moderately distinctive
**30. way** — count: 1, TF-IDF: 2,077.99, IDF: 4.764821 🟢 medium — moderately distinctive
**31. work** — count: 1, TF-IDF: 2,086.80, IDF: 4.785024 🟢 medium — moderately distinctive
**32. meet** — count: 1, TF-IDF: 2,088.58, IDF: 4.789114 🟢 medium — moderately distinctive
**33. reduced** — count: 1, TF-IDF: 2,090.37, IDF: 4.793221 🟢 medium — moderately distinctive
**34. rising** — count: 1, TF-IDF: 2,090.37, IDF: 4.793221 🟢 medium — moderately distinctive
**35. offered** — count: 1, TF-IDF: 2,093.98, IDF: 4.801485 🟢 medium — moderately distinctive
**36. term** — count: 1, TF-IDF: 2,133.74, IDF: 4.892655 🟢 medium — moderately distinctive
**37. base** — count: 1, TF-IDF: 2,139.72, IDF: 4.906385 🟢 medium — moderately distinctive
**38. holders** — count: 1, TF-IDF: 2,158.20, IDF: 4.948744 🟢 medium — moderately distinctive
**39. small** — count: 1, TF-IDF: 2,166.66, IDF: 4.968162 🟢 medium — moderately distinctive
**40. gave** — count: 1, TF-IDF: 2,179.68, IDF: 4.998015 🟢 medium — moderately distinctive
**41. again** — count: 1, TF-IDF: 2,209.30, IDF: 5.065927 🟢 medium — moderately distinctive
**42. taking** — count: 1, TF-IDF: 2,236.03, IDF: 5.127227 🟢 medium — moderately distinctive
**43. marks** — count: 1, TF-IDF: 2,246.18, IDF: 5.150484 🟢 medium — moderately distinctive
**44. local** — count: 1, TF-IDF: 2,256.56, IDF: 5.174295 🟢 medium — moderately distinctive
**45. force** — count: 1, TF-IDF: 2,264.51, IDF: 5.192532 🟢 medium — moderately distinctive
**46. makes** — count: 1, TF-IDF: 2,272.62, IDF: 5.211109 🟢 medium — moderately distinctive
**47. similar** — count: 1, TF-IDF: 2,280.87, IDF: 5.230037 🟢 medium — moderately distinctive
**48. able** — count: 1, TF-IDF: 2,306.62, IDF: 5.28907 🟢 medium — moderately distinctive
**49. maintain** — count: 1, TF-IDF: 2,321.60, IDF: 5.323438 🟢 medium — moderately distinctive
**50. remains** — count: 1, TF-IDF: 2,321.60, IDF: 5.323438 🟢 medium — moderately distinctive

---

## Full Ranked Table

All 1,095 content terms, sorted by TF-IDF descending.

| Rank | Word | Count | TF-IDF | IDF | Band |
|------|------|-------|--------|-----|------|
| 1 | **translated** | 142 | 488,508.92 | 7.888387 | 🔴 extremely high — text-exclusive |
| 2 | **jetsunma** | 33 | 138,015.70 | 9.59 | 🔴 extremely high — text-exclusive |
| 3 | **homage** | 26 | 108,739.64 | 9.59 | 🔴 extremely high — text-exclusive |
| 4 | **teachings** | 24 | 100,375.05 | 9.59 | 🔴 extremely high — text-exclusive |
| 5 | **beings** | 20 | 83,645.88 | 9.59 | 🔴 extremely high — text-exclusive |
| 6 | **prostrate** | 17 | 71,099.00 | 9.59 | 🔴 extremely high — text-exclusive |
| 7 | **please** | 18 | 66,681.82 | 8.494523 | 🔴 extremely high — text-exclusive |
| 8 | **supreme** | 20 | 62,370.59 | 7.150788 | 🔴 extremely high — text-exclusive |
| 9 | **noble** | 15 | 60,102.51 | 9.18767 | 🔴 extremely high — text-exclusive |
| 10 | **enlightenment** | 12 | 50,187.53 | 9.59 | 🔴 extremely high — text-exclusive |
| 11 | **grant** | 16 | 47,813.66 | 6.852295 | 🟠 very high — domain-specific |
| 12 | **dharma** | 11 | 46,005.23 | 9.59 | 🟠 very high — domain-specific |
| 13 | **mother** | 11 | 46,005.23 | 9.59 | 🟠 very high — domain-specific |
| 14 | **pray** | 10 | 41,822.94 | 9.59 | 🟠 very high — domain-specific |
| 15 | **happiness** | 10 | 41,822.94 | 9.59 | 🟠 very high — domain-specific |
| 16 | **lotus** | 10 | 40,068.34 | 9.18767 | 🟠 very high — domain-specific |
| 17 | **wish-fulfilling** | 9 | 37,640.65 | 9.59 | 🟠 very high — domain-specific |
| 18 | **lady** | 9 | 37,640.65 | 9.59 | 🟠 very high — domain-specific |
| 19 | **wheel** | 8 | 33,469.29 | 9.593135 | 🟠 very high — domain-specific |
| 20 | **hosts** | 8 | 33,458.35 | 9.59 | 🟠 very high — domain-specific |
| 21 | **like** | 14 | 31,703.20 | 5.192532 | 🟠 very high — domain-specific |
| 22 | **existence** | 9 | 30,015.27 | 7.647225 | 🟠 very high — domain-specific |
| 23 | **wisdom** | 8 | 29,636.36 | 8.494523 | 🟠 very high — domain-specific |
| 24 | **ten** | 11 | 29,546.72 | 6.159148 | 🟠 very high — domain-specific |
| 25 | **victors** | 7 | 29,285.63 | 9.593135 | 🟠 very high — domain-specific |
| 26 | **compassion** | 7 | 29,285.63 | 9.593135 | 🟠 very high — domain-specific |
| 27 | **buddha** | 7 | 29,276.06 | 9.59 | 🟠 very high — domain-specific |
| 28 | **realms** | 7 | 29,276.06 | 9.59 | 🟠 very high — domain-specific |
| 29 | **attained** | 7 | 28,047.84 | 9.18767 | 🟠 very high — domain-specific |
| 30 | **perfect** | 7 | 28,047.84 | 9.18767 | 🟠 very high — domain-specific |
| 31 | **every** | 11 | 27,812.52 | 5.797646 | 🟠 very high — domain-specific |
| 32 | **refuge** | 7 | 25,931.82 | 8.494523 | 🟠 very high — domain-specific |
| 33 | **gods** | 6 | 25,093.76 | 9.59 | 🟠 very high — domain-specific |
| 34 | **possess** | 6 | 25,093.76 | 9.59 | 🟠 very high — domain-specific |
| 35 | **mind** | 8 | 24,948.24 | 7.150788 | 🟠 very high — domain-specific |
| 36 | **ocean** | 8 | 24,948.24 | 7.150788 | 🟠 very high — domain-specific |
| 37 | **benefit** | 10 | 24,166.38 | 5.54135 | 🟠 very high — domain-specific |
| 38 | **accomplishments** | 6 | 24,041.00 | 9.18767 | 🟠 very high — domain-specific |
| 39 | **profound** | 6 | 24,041.00 | 9.18767 | 🟠 very high — domain-specific |
| 40 | **directions** | 6 | 23,288.24 | 8.899988 | 🟠 very high — domain-specific |
| 41 | **sake** | 6 | 22,704.35 | 8.676844 | 🟠 very high — domain-specific |
| 42 | **accomplished** | 6 | 22,227.27 | 8.494523 | 🟠 very high — domain-specific |
| 43 | **age** | 6 | 21,823.91 | 8.340372 | 🟠 very high — domain-specific |
| 44 | **life** | 9 | 21,615.54 | 5.507159 | 🟠 very high — domain-specific |
| 45 | **perfectly** | 6 | 21,474.51 | 8.206841 | 🟠 very high — domain-specific |
| 46 | **light** | 9 | 21,422.47 | 5.457969 | 🟠 very high — domain-specific |
| 47 | **completely** | 7 | 21,122.07 | 6.918987 | 🟠 very high — domain-specific |
| 48 | **liberation** | 5 | 20,918.31 | 9.593135 | 🟠 very high — domain-specific |
| 49 | **flourish** | 5 | 20,918.31 | 9.593135 | 🟠 very high — domain-specific |
| 50 | **degenerate** | 5 | 20,918.31 | 9.593135 | 🟠 very high — domain-specific |
| 51 | **adorned** | 5 | 20,911.47 | 9.59 | 🟠 very high — domain-specific |
| 52 | **enlightened** | 5 | 20,911.47 | 9.59 | 🟠 very high — domain-specific |
| 53 | **tārā** | 5 | 20,911.47 | 9.59 | 🟠 very high — domain-specific |
| 54 | **primordial** | 5 | 20,911.47 | 9.59 | 🟠 very high — domain-specific |
| 55 | **ture** | 5 | 20,911.47 | 9.59 | 🟠 very high — domain-specific |
| 56 | **moon** | 5 | 20,911.47 | 9.59 | 🟠 very high — domain-specific |
| 57 | **cyclic** | 5 | 20,911.47 | 9.59 | 🟠 very high — domain-specific |
| 58 | **power** | 9 | 20,706.86 | 5.275647 | 🟠 very high — domain-specific |
| 59 | **without** | 10 | 20,592.07 | 4.721762 | 🟠 very high — domain-specific |
| 60 | **eyes** | 5 | 20,034.17 | 9.18767 | 🟠 very high — domain-specific |
| 61 | **infinite** | 5 | 20,034.17 | 9.18767 | 🟠 very high — domain-specific |
| 62 | **vast** | 6 | 20,010.18 | 7.647225 | 🟠 very high — domain-specific |
| 63 | **heirs** | 5 | 19,406.86 | 8.899988 | 🟠 very high — domain-specific |
| 64 | **peace** | 5 | 18,920.29 | 8.676844 | 🟠 very high — domain-specific |
| 65 | **space** | 6 | 18,493.00 | 7.067407 | 🟠 very high — domain-specific |
| 66 | **having** | 7 | 17,194.18 | 5.632322 | 🟠 very high — domain-specific |
| 67 | **blazing** | 4 | 16,734.64 | 9.593135 | 🟠 very high — domain-specific |
| 68 | **joy** | 4 | 16,734.64 | 9.593135 | 🟠 very high — domain-specific |
| 69 | **essence** | 4 | 16,734.64 | 9.593135 | 🟠 very high — domain-specific |
| 70 | **dispel** | 4 | 16,734.64 | 9.593135 | 🟠 very high — domain-specific |
| 71 | **glory** | 4 | 16,734.64 | 9.593135 | 🟠 very high — domain-specific |
| 72 | **bloom** | 4 | 16,734.64 | 9.593135 | 🟠 very high — domain-specific |
| 73 | **devotion** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 74 | **māra** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 75 | **protector** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 76 | **mantra** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 77 | **endowed** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 78 | **tuttāre** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 79 | **jewels** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 80 | **demons** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 81 | **syllable** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 82 | **hūṁ** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 83 | **possessing** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 84 | **karma** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 85 | **buddhas** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 86 | **compassionate** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 87 | **blessings** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 88 | **bodhisattvas** | 4 | 16,729.18 | 9.59 | 🟠 very high — domain-specific |
| 89 | **hundred** | 5 | 16,251.79 | 7.453069 | 🟠 very high — domain-specific |
| 90 | **worlds** | 4 | 16,027.34 | 9.18767 | 🟠 very high — domain-specific |
| 91 | **forth** | 4 | 16,027.34 | 9.18767 | 🟠 very high — domain-specific |
| 92 | **precious** | 5 | 16,009.25 | 7.341843 | 🟠 very high — domain-specific |
| 93 | **suffering** | 5 | 15,791.02 | 7.24176 | 🟠 very high — domain-specific |
| 94 | **exception** | 5 | 15,689.58 | 7.19524 | 🟠 very high — domain-specific |
| 95 | **peaceful** | 4 | 15,525.49 | 8.899988 | 🟠 very high — domain-specific |
| 96 | **clouds** | 4 | 15,525.49 | 8.899988 | 🟠 very high — domain-specific |
| 97 | **heart** | 5 | 15,243.01 | 6.990446 | 🟠 very high — domain-specific |
| 98 | **merit** | 4 | 14,549.28 | 8.340372 | 🟠 very high — domain-specific |
| 99 | **desired** | 4 | 14,316.34 | 8.206841 | 🟠 very high — domain-specific |
| 100 | **gathered** | 4 | 14,110.87 | 8.089058 | 🟠 very high — domain-specific |
| 101 | **qualities** | 4 | 13,927.08 | 7.983697 | 🟠 very high — domain-specific |
| 102 | **moment** | 5 | 13,613.67 | 6.243231 | 🟠 very high — domain-specific |
| 103 | **victor** | 4 | 13,469.40 | 7.721333 | 🟠 very high — domain-specific |
| 104 | **swift** | 4 | 13,469.40 | 7.721333 | 🟠 very high — domain-specific |
| 105 | **lord** | 4 | 13,219.77 | 7.578232 | 🟠 very high — domain-specific |
| 106 | **secret** | 4 | 13,219.77 | 7.578232 | 🟠 very high — domain-specific |
| 107 | **feet** | 5 | 12,593.60 | 5.775423 | 🟠 very high — domain-specific |
| 108 | **virtue** | 3 | 12,550.98 | 9.593135 | 🟠 very high — domain-specific |
| 109 | **guru** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 110 | **mañjugho** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 111 | **meditative** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 112 | **brahmā** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 113 | **wondrous** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 114 | **victorious** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 115 | **ripening** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 116 | **vajra** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 117 | **protectors** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 118 | **syllables** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 119 | **svāhā** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 120 | **yak** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 121 | **destroys** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 122 | **enemies** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 123 | **ornament** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 124 | **liberate** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 125 | **dwell** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 126 | **bliss** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 127 | **nectar** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 128 | **obscurations** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 129 | **lamp** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 130 | **lifespan** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 131 | **sentient** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 132 | **bestow** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 133 | **sacred** | 3 | 12,546.88 | 9.59 | 🟠 very high — domain-specific |
| 134 | **wheels** | 3 | 12,020.50 | 9.18767 | 🟠 very high — domain-specific |
| 135 | **constantly** | 3 | 12,020.50 | 9.18767 | 🟠 very high — domain-specific |
| 136 | **complete** | 5 | 11,901.37 | 5.457969 | 🟠 very high — domain-specific |
| 137 | **practice** | 4 | 11,844.35 | 6.789775 | 🟠 very high — domain-specific |
| 138 | **uphold** | 3 | 11,644.12 | 8.899988 | 🟠 very high — domain-specific |
| 139 | **stainless** | 3 | 11,644.12 | 8.899988 | 🟠 very high — domain-specific |
| 140 | **until** | 6 | 11,393.03 | 4.354037 | 🟠 very high — domain-specific |
| 141 | **wealth** | 3 | 11,352.17 | 8.676844 | 🟠 very high — domain-specific |
| 142 | **earth** | 3 | 11,113.64 | 8.494523 | 🟠 very high — domain-specific |
| 143 | **concentration** | 3 | 11,113.64 | 8.494523 | 🟠 very high — domain-specific |
| 144 | **lives** | 3 | 11,113.64 | 8.494523 | 🟠 very high — domain-specific |
| 145 | **let** | 4 | 11,017.86 | 6.31599 | 🟠 very high — domain-specific |
| 146 | **relief** | 4 | 11,017.86 | 6.31599 | 🟠 very high — domain-specific |
| 147 | **filled** | 3 | 10,911.96 | 8.340372 | 🟠 very high — domain-specific |
| 148 | **full** | 6 | 10,872.37 | 4.155056 | 🟠 very high — domain-specific |
| 149 | **short** | 5 | 10,812.05 | 4.958406 | 🟠 very high — domain-specific |
| 150 | **defeated** | 3 | 10,737.25 | 8.206841 | 🟠 very high — domain-specific |
| 151 | **death** | 3 | 10,737.25 | 8.206841 | 🟠 very high — domain-specific |
| 152 | **pure** | 3 | 10,583.15 | 8.089058 | 🟠 very high — domain-specific |
| 153 | **fears** | 4 | 10,557.66 | 6.052176 | 🟠 very high — domain-specific |
| 154 | **throughout** | 4 | 10,557.66 | 6.052176 | 🟠 very high — domain-specific |
| 155 | **sovereign** | 3 | 10,445.31 | 7.983697 | 🟠 very high — domain-specific |
| 156 | **faith** | 3 | 10,445.31 | 7.983697 | 🟠 very high — domain-specific |
| 157 | **fortune** | 3 | 10,445.31 | 7.983697 | 🟠 very high — domain-specific |
| 158 | **bow** | 3 | 10,320.61 | 7.888387 | 🟠 very high — domain-specific |
| 159 | **causes** | 3 | 10,320.61 | 7.888387 | 🟠 very high — domain-specific |
| 160 | **ordinary** | 4 | 10,256.54 | 5.879563 | 🟠 very high — domain-specific |
| 161 | **time** | 6 | 10,053.60 | 3.842151 | 🟠 very high — domain-specific |
| 162 | **victory** | 3 | 10,005.09 | 7.647225 | 🟠 very high — domain-specific |
| 163 | **others** | 4 | 9,858.79 | 5.651553 | 🟡 high — specialist register |
| 164 | **activity** | 4 | 9,697.16 | 5.558895 | 🟡 high — specialist register |
| 165 | **head** | 4 | 9,521.10 | 5.457969 | 🟡 high — specialist register |
| 166 | **forms** | 3 | 9,413.75 | 7.19524 | 🟡 high — specialist register |
| 167 | **thousand** | 3 | 9,355.59 | 7.150788 | 🟡 high — specialist register |
| 168 | **crown** | 3 | 9,246.50 | 7.067407 | 🟡 high — specialist register |
| 169 | **golden** | 3 | 9,195.18 | 7.028186 | 🟡 high — specialist register |
| 170 | **free** | 4 | 8,984.71 | 5.150484 | 🟡 high — specialist register |
| 171 | **form** | 4 | 8,974.48 | 5.144619 | 🟡 high — specialist register |
| 172 | **fall** | 5 | 8,780.42 | 4.026701 | 🟡 high — specialist register |
| 173 | **become** | 4 | 8,709.95 | 4.992978 | 🟡 high — specialist register |
| 174 | **spread** | 3 | 8,631.58 | 6.597403 | 🟡 high — specialist register |
| 175 | **rain** | 3 | 8,536.96 | 6.525082 | 🟡 high — specialist register |
| 176 | **hold** | 4 | 8,519.15 | 4.883605 | 🟡 high — specialist register |
| 177 | **fire** | 3 | 8,448.72 | 6.457641 | 🟡 high — specialist register |
| 178 | **born** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 179 | **dawn** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 180 | **friend** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 181 | **praise** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 182 | **authoritative** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 183 | **renunciation** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 184 | **intensely** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 185 | **garland** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 186 | **thoughts** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 187 | **saffron** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 188 | **sixteen** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 189 | **continuity** | 2 | 8,367.32 | 9.593135 | 🟡 high — specialist register |
| 190 | **hand** | 3 | 8,366.06 | 6.394462 | 🟡 high — specialist register |
| 191 | **fear** | 3 | 8,366.06 | 6.394462 | 🟡 high — specialist register |
| 192 | **obstruct** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 193 | **generosity** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 194 | **perfections** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 195 | **non-buddhist** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 196 | **extremists** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 197 | **terrified** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 198 | **teaching** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 199 | **kinsman** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 200 | **scriptural** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 201 | **craving** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 202 | **countless** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 203 | **deeds** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 204 | **maitreya** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 205 | **brilliance** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 206 | **lineage** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 207 | **bhagavatī** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 208 | **ḍākinīs** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 209 | **tsal** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 210 | **gurus** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 211 | **twofold** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 212 | **namo** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 213 | **tāre** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 214 | **heroic** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 215 | **dispels** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 216 | **brilliant** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 217 | **beautifully** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 218 | **sphere** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 219 | **perfection** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 220 | **trampling** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 221 | **summon** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 222 | **zombies** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 223 | **shatter** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 224 | **guardians** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 225 | **frown** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 226 | **wrathful** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 227 | **virtuous** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 228 | **reciting** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 229 | **majesty** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 230 | **dreams** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 231 | **avalokite** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 232 | **vara** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 233 | **pacify** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 234 | **conceptual** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 235 | **robes** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 236 | **sever** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 237 | **mothers** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 238 | **afflictions** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 239 | **birth** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 240 | **mandala** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 241 | **awakening** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 242 | **beginningless** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 243 | **sublime** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 244 | **delight** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 245 | **virtues** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 246 | **longevity** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 247 | **ornaments** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 248 | **splendor** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 249 | **tame** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 250 | **excellence** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 251 | **expanse** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 252 | **beautiful** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 253 | **masters** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 254 | **sūtra** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 255 | **lineages** | 2 | 8,364.59 | 9.59 | 🟡 high — specialist register |
| 256 | **body** | 3 | 8,288.32 | 6.335039 | 🟡 high — specialist register |
| 257 | **since** | 5 | 8,192.03 | 3.756864 | 🟡 high — specialist register |
| 258 | **therefore** | 3 | 8,145.45 | 6.225839 | 🟡 high — specialist register |
| 259 | **intention** | 3 | 8,037.26 | 6.143148 | 🟡 high — specialist register |
| 260 | **patience** | 2 | 8,013.67 | 9.18767 | 🟡 high — specialist register |
| 261 | **strife** | 2 | 8,013.67 | 9.18767 | 🟡 high — specialist register |
| 262 | **inconceivable** | 2 | 8,013.67 | 9.18767 | 🟡 high — specialist register |
| 263 | **festival** | 2 | 8,013.67 | 9.18767 | 🟡 high — specialist register |
| 264 | **lords** | 2 | 8,013.67 | 9.18767 | 🟡 high — specialist register |
| 265 | **speech** | 3 | 7,826.71 | 5.982217 | 🟡 high — specialist register |
| 266 | **truly** | 2 | 7,762.75 | 8.899988 | 🟡 high — specialist register |
| 267 | **leg** | 2 | 7,762.75 | 8.899988 | 🟡 high — specialist register |
| 268 | **love** | 2 | 7,762.75 | 8.899988 | 🟡 high — specialist register |
| 269 | **accumulations** | 2 | 7,762.75 | 8.899988 | 🟡 high — specialist register |
| 270 | **prosperity** | 2 | 7,762.75 | 8.899988 | 🟡 high — specialist register |
| 271 | **protect** | 3 | 7,757.84 | 5.929574 | 🟡 high — specialist register |
| 272 | **land** | 3 | 7,645.40 | 5.843631 | 🟡 high — specialist register |
| 273 | **surrounded** | 2 | 7,568.12 | 8.676844 | 🟡 high — specialist register |
| 274 | **destroy** | 2 | 7,568.12 | 8.676844 | 🟡 high — specialist register |
| 275 | **vows** | 2 | 7,409.09 | 8.494523 | 🟡 high — specialist register |
| 276 | **times** | 3 | 7,332.08 | 5.604151 | 🟡 high — specialist register |
| 277 | **enjoy** | 2 | 7,274.64 | 8.340372 | 🟡 high — specialist register |
| 278 | **rest** | 3 | 7,261.34 | 5.550084 | 🟡 high — specialist register |
| 279 | **cause** | 3 | 7,172.60 | 5.482261 | 🟡 high — specialist register |
| 280 | **swiftly** | 2 | 7,158.17 | 8.206841 | 🟡 high — specialist register |
| 281 | **weapons** | 2 | 7,158.17 | 8.206841 | 🟡 high — specialist register |
| 282 | **fruits** | 2 | 7,158.17 | 8.206841 | 🟡 high — specialist register |
| 283 | **extended** | 3 | 7,089.51 | 5.418748 | 🟡 high — specialist register |
| 284 | **tree** | 2 | 7,055.44 | 8.089058 | 🟡 high — specialist register |
| 285 | **learned** | 2 | 7,055.44 | 8.089058 | 🟡 high — specialist register |
| 286 | **reach** | 3 | 7,001.93 | 5.351808 | 🟡 high — specialist register |
| 287 | **attain** | 2 | 6,963.54 | 7.983697 | 🟡 high — specialist register |
| 288 | **diminish** | 2 | 6,963.54 | 7.983697 | 🟡 high — specialist register |
| 289 | **banner** | 2 | 6,963.54 | 7.983697 | 🟡 high — specialist register |
| 290 | **bring** | 3 | 6,955.69 | 5.316469 | 🟡 high — specialist register |
| 291 | **root** | 2 | 6,880.41 | 7.888387 | 🟡 high — specialist register |
| 292 | **human** | 2 | 6,880.41 | 7.888387 | 🟡 high — specialist register |
| 293 | **eye** | 2 | 6,880.41 | 7.888387 | 🟡 high — specialist register |
| 294 | **world** | 4 | 6,808.16 | 3.902776 | 🟡 high — specialist register |
| 295 | **path** | 2 | 6,804.51 | 7.801376 | 🟡 high — specialist register |
| 296 | **discipline** | 2 | 6,734.70 | 7.721333 | 🟡 high — specialist register |
| 297 | **right** | 3 | 6,730.86 | 5.144619 | 🟡 high — specialist register |
| 298 | **seeing** | 2 | 6,670.06 | 7.647225 | 🟡 high — specialist register |
| 299 | **offerings** | 2 | 6,670.06 | 7.647225 | 🟡 high — specialist register |
| 300 | **obstacles** | 2 | 6,670.06 | 7.647225 | 🟡 high — specialist register |
| 301 | **mass** | 2 | 6,609.88 | 7.578232 | 🟡 high — specialist register |
| 302 | **engage** | 2 | 6,553.59 | 7.513694 | 🟡 high — specialist register |
| 303 | **names** | 2 | 6,553.59 | 7.513694 | 🟡 high — specialist register |
| 304 | **diligence** | 2 | 6,500.71 | 7.453069 | 🟡 high — specialist register |
| 305 | **grace** | 2 | 6,500.71 | 7.453069 | 🟡 high — specialist register |
| 306 | **arising** | 2 | 6,450.86 | 7.395911 | 🟡 high — specialist register |
| 307 | **lead** | 3 | 6,431.28 | 4.915644 | 🟡 high — specialist register |
| 308 | **fruit** | 2 | 6,403.70 | 7.341843 | 🟡 high — specialist register |
| 309 | **grants** | 2 | 6,403.70 | 7.341843 | 🟡 high — specialist register |
| 310 | **powerful** | 2 | 6,358.96 | 7.29055 | 🟡 high — specialist register |
| 311 | **because** | 4 | 6,280.72 | 3.600421 | 🟡 high — specialist register |
| 312 | **whatever** | 2 | 6,199.94 | 7.108229 | 🟡 high — specialist register |
| 313 | **conditions** | 3 | 6,192.75 | 4.733323 | 🟡 high — specialist register |
| 314 | **conduct** | 2 | 6,164.33 | 7.067407 | 🟡 high — specialist register |
| 315 | **accumulated** | 2 | 6,130.12 | 7.028186 | 🟡 high — specialist register |
| 316 | **nature** | 2 | 6,130.12 | 7.028186 | 🟡 high — specialist register |
| 317 | **abandoned** | 2 | 6,065.48 | 6.954078 | 🟡 high — specialist register |
| 318 | **excellent** | 2 | 5,976.71 | 6.852295 | 🟡 high — specialist register |
| 319 | **decline** | 3 | 5,939.92 | 4.540079 | 🟡 high — specialist register |
| 320 | **desire** | 2 | 5,922.18 | 6.789775 | 🟡 high — specialist register |
| 321 | **play** | 2 | 5,922.18 | 6.789775 | 🟡 high — specialist register |
| 322 | **restore** | 2 | 5,922.18 | 6.789775 | 🟡 high — specialist register |
| 323 | **autumn** | 2 | 5,896.14 | 6.759922 | 🟡 high — specialist register |
| 324 | **vessel** | 2 | 5,896.14 | 6.759922 | 🟡 high — specialist register |
| 325 | **holder** | 2 | 5,870.85 | 6.730934 | 🟡 high — specialist register |
| 326 | **under** | 4 | 5,843.77 | 3.34994 | 🟡 high — specialist register |
| 327 | **realized** | 2 | 5,822.38 | 6.675364 | 🟡 high — specialist register |
| 328 | **respect** | 2 | 5,776.47 | 6.622721 | 🟡 high — specialist register |
| 329 | **twice** | 2 | 5,754.39 | 6.597403 | 🟡 high — specialist register |
| 330 | **ever** | 2 | 5,732.85 | 6.57271 | 🟡 high — specialist register |
| 331 | **regarding** | 2 | 5,691.31 | 6.525082 | 🟡 high — specialist register |
| 332 | **sun** | 2 | 5,671.25 | 6.502093 | 🟡 high — specialist register |
| 333 | **state** | 3 | 5,596.34 | 4.277469 | 🟡 high — specialist register |
| 334 | **kind** | 2 | 5,525.55 | 6.335039 | 🟡 high — specialist register |
| 335 | **never** | 2 | 5,508.93 | 6.31599 | 🟡 high — specialist register |
| 336 | **established** | 2 | 5,400.73 | 6.191938 | 🟡 high — specialist register |
| 337 | **most** | 3 | 5,337.60 | 4.079706 | 🟡 high — specialist register |
| 338 | **declining** | 2 | 5,317.60 | 6.096628 | 🟡 high — specialist register |
| 339 | **make** | 3 | 5,280.82 | 4.036307 | 🟡 high — specialist register |
| 340 | **particular** | 2 | 5,266.28 | 6.037787 | 🟡 high — specialist register |
| 341 | **single** | 2 | 5,241.71 | 6.009616 | 🟡 high — specialist register |
| 342 | **take** | 3 | 5,121.68 | 3.914671 | 🟡 high — specialist register |
| 343 | **away** | 2 | 5,066.68 | 5.808946 | 🟡 high — specialist register |
| 344 | **signs** | 2 | 5,009.15 | 5.742988 | 🟡 high — specialist register |
| 345 | **benefits** | 2 | 4,999.92 | 5.732405 | 🟡 high — specialist register |
| 346 | **night** | 2 | 4,999.92 | 5.732405 | 🟡 high — specialist register |
| 347 | **especially** | 2 | 4,999.92 | 5.732405 | 🟡 high — specialist register |
| 348 | **look** | 2 | 4,963.95 | 5.691163 | 🟡 high — specialist register |
| 349 | **activities** | 2 | 4,946.50 | 5.671162 | 🟡 high — specialist register |
| 350 | **source** | 2 | 4,896.17 | 5.613454 | 🟡 high — specialist register |
| 351 | **face** | 2 | 4,880.01 | 5.594934 | 🟡 high — specialist register |
| 352 | **clear** | 2 | 4,848.58 | 5.558895 | 🟡 high — specialist register |
| 353 | **end** | 3 | 4,824.82 | 3.687773 | 🟡 high — specialist register |
| 354 | **entered** | 2 | 4,818.24 | 5.524108 | 🟡 high — specialist register |
| 355 | **fully** | 2 | 4,810.81 | 5.515598 | 🟡 high — specialist register |
| 356 | **left** | 2 | 4,781.74 | 5.482261 | 🟡 high — specialist register |
| 357 | **food** | 2 | 4,399.94 | 5.044535 | 🟡 high — specialist register |
| 358 | **trust** | 2 | 4,324.82 | 4.958406 | 🟡 high — specialist register |
| 359 | **come** | 2 | 4,275.44 | 4.901787 | 🟡 high — specialist register |
| 360 | **gold** | 2 | 4,244.00 | 4.865747 | 🟡 high — specialist register |
| 361 | **sky** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 362 | **subduing** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 363 | **miraculous** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 364 | **displays** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 365 | **perfected** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 366 | **anxiety** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 367 | **rendered** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 368 | **teachers** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 369 | **sacrificed** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 370 | **hair** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 371 | **phenomena** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 372 | **roots** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 373 | **dedicate** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 374 | **momentary** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 375 | **flash** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 376 | **stars** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 377 | **palms** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 378 | **utterly** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 379 | **stamp** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 380 | **meru** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 381 | **contagious** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 382 | **loving** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 383 | **nurse** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 384 | **famine** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 385 | **miserable** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 386 | **evil** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 387 | **cultivate** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 388 | **courage** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 389 | **wander** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 390 | **teach** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 391 | **purified** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 392 | **condensing** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 393 | **myself** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 394 | **truth** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 395 | **dense** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 396 | **flames** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 397 | **enduring** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 398 | **finger** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 399 | **secrets** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 400 | **distress** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 401 | **maturation** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 402 | **auspicious** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 403 | **emerald** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 404 | **attainment** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 405 | **parted** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 406 | **flower** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 407 | **successors** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 408 | **ati** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 409 | **lama** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 410 | **invoke** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 411 | **rampant** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 412 | **dregs** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 413 | **indifferent** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 414 | **manifest** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 415 | **lit** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 416 | **misfortune** | 1 | 4,183.66 | 9.593135 | 🟡 high — specialist register |
| 417 | **dharmamitra** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 418 | **zero-shot** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 419 | **bodhi** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 420 | **pervaded** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 421 | **rained** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 422 | **shower** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 423 | **vajras** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 424 | **spears** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 425 | **snow-peaks** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 426 | **flower-arrows** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 427 | **strove** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 428 | **loving-kindness** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 429 | **buddhahood** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 430 | **trembled** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 431 | **ethical** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 432 | **culmination** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 433 | **rejoiced** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 434 | **possesses** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 435 | **unerring** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 436 | **lion** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 437 | **roar** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 438 | **proclaimed** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 439 | **speechless** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 440 | **foxes** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 441 | **sages** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 442 | **apāda** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 443 | **vālmīki** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 444 | **vyāsa** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 445 | **ne-jok** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 446 | **renown** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 447 | **cared** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 448 | **liberated** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 449 | **disciples** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 450 | **hearers** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 451 | **prophecies** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 452 | **aspiring** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 453 | **disciple** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 454 | **āradvatīputra** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 455 | **ākya** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 456 | **vāku** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 457 | **bhagavan** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 458 | **omniscience** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 459 | **dharmakāya** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 460 | **prajñāpāramitā** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 461 | **samantabhadrī** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 462 | **sambhogakāya** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 463 | **vajravārāhī** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 464 | **emanation-display** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 465 | **venerable** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 466 | **padmākara** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 467 | **bodhisattva** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 468 | **rolpa** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 469 | **chokgyur** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 470 | **dechen** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 471 | **lingpa** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 472 | **treasures** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 473 | **dorje** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 474 | **ziji** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 475 | **pema** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 476 | **garwang** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 477 | **goddess** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 478 | **moistened** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 479 | **sprouts** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 480 | **altruistic** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 481 | **lush** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 482 | **spontaneous** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 483 | **ārya-tārāye** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 484 | **confess** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 485 | **rejoice** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 486 | **exhort** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 487 | **liberatress** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 488 | **stamens** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 489 | **lotus-face** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 490 | **moons** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 491 | **water-born** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 492 | **tathāgatas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 493 | **tuttāra** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 494 | **hūṃ** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 495 | **fills** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 496 | **indra** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 497 | **agni** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 498 | **vāyu** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 499 | **varas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 500 | **worship** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 501 | **gandharvas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 502 | **traṭ** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 503 | **phaṭ** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 504 | **magical** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 505 | **adversaries** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 506 | **swirling** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 507 | **fearful** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 508 | **champions** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 509 | **mara** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 510 | **frowning** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 511 | **slays** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 512 | **mudrā** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 513 | **symbolizing** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 514 | **adorn** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 515 | **radiating** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 516 | **turbulent** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 517 | **majestic** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 518 | **garlands** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 519 | **laughter** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 520 | **vibrating** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 521 | **destitution** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 522 | **crescent** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 523 | **blazes** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 524 | **matted** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 525 | **amitābha** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 526 | **radiates** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 527 | **magnificent** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 528 | **eon** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 529 | **bent** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 530 | **armies** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 531 | **trample** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 532 | **blissful** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 533 | **nirvāṇa** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 534 | **negativity** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 535 | **shatters** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 536 | **ten-syllable** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 537 | **wisdom-tara** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 538 | **seed-syllable** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 539 | **mandara** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 540 | **vindhya** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 541 | **tremble** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 542 | **deer-marked** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 543 | **celestial** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 544 | **tāra** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 545 | **phat** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 546 | **kinnaras** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 547 | **hara** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 548 | **suchnesses** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 549 | **blooming** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 550 | **darkness** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 551 | **torment** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 552 | **tormented** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 553 | **wherever** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 554 | **sickness** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 555 | **afflict** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 556 | **sufferings** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 557 | **mire** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 558 | **misery** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 559 | **habitual** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 560 | **ripples** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 561 | **never-ending** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 562 | **boast** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 563 | **karmic** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 564 | **beast** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 565 | **impermanent** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 566 | **unaccomplished** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 567 | **noose** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 568 | **epidemics** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 569 | **poisons** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 570 | **habituated** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 571 | **self-grasping** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 572 | **lifetimes** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 573 | **spiritual** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 574 | **demonic** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 575 | **insight** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 576 | **mindfulness** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 577 | **mind-stream** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 578 | **cessation** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 579 | **bardo** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 580 | **fleeting** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 581 | **emanation** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 582 | **reabsorption** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 583 | **prophesy** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 584 | **oceans** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 585 | **holy** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 586 | **life-force** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 587 | **aspirations** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 588 | **misdeeds** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 589 | **downfalls** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 590 | **cleansed** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 591 | **siddhi** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 592 | **deathless** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 593 | **life-empowerment** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 594 | **distractions** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 595 | **worldly** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 596 | **ever-greater** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 597 | **ears** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 598 | **nāgas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 599 | **heaven** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 600 | **unhappiness** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 601 | **reverence** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 602 | **jewel** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 603 | **thickets** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 604 | **non-humans** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 605 | **untimely** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 606 | **perfects** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 607 | **deity** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 608 | **prayers** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 609 | **fruition** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 610 | **one-pointed** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 611 | **longing** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 612 | **youthful** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 613 | **vajra-bliss** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 614 | **rites** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 615 | **gift** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 616 | **anoint** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 617 | **thumb** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 618 | **lovely** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 619 | **blossomed** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 620 | **nets** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 621 | **pearls** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 622 | **bells** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 623 | **displaying** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 624 | **graceful** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 625 | **divine** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 626 | **molten** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 627 | **seated** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 628 | **indestructible** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 629 | **proclaiming** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 630 | **melody** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 631 | **uninterrupted** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 632 | **webs** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 633 | **throne** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 634 | **giver** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 635 | **bodhicitta** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 636 | **drolma** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 637 | **tormenting** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 638 | **protectress** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 639 | **remembers** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 640 | **misfortunes** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 641 | **embodiment** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 642 | **heartfelt** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 643 | **practicing** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 644 | **ārya** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 645 | **tārāye** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 646 | **churned** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 647 | **moon-like** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 648 | **respite** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 649 | **singular** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 650 | **lapis** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 651 | **lazuli** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 652 | **lute** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 653 | **melodic** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 654 | **radiance** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 655 | **dharma-heaps** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 656 | **heart-mind** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 657 | **non-dual** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 658 | **elaborations** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 659 | **boundless** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 660 | **sixty-four** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 661 | **inexhaustible** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 662 | **captivates** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 663 | **all-pervading** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 664 | **spontaneously** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 665 | **perfecting** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 666 | **supplication** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 667 | **wisdom-vision** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 668 | **liberates** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 669 | **captivated** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 670 | **single-pointed** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 671 | **particles** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 672 | **radiant** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 673 | **moods** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 674 | **smiles** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 675 | **mundane** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 676 | **supramundane** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 677 | **treasure** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 678 | **vidyā-mantra** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 679 | **supremely** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 680 | **partiality** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 681 | **dissolve** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 682 | **fourfold** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 683 | **indivisible** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 684 | **kāyas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 685 | **joyful** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 686 | **sidelong** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 687 | **glance** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 688 | **distinguished** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 689 | **fortunate** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 690 | **aeon** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 691 | **uḍumbara** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 692 | **realm** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 693 | **fulfiller** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 694 | **rāvakas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 695 | **pratyekabuddhas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 696 | **mañju** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 697 | **jambudvīpa** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 698 | **eighty-four** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 699 | **yoga** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 700 | **incomparably** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 701 | **padmasambhava** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 702 | **āntarak** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 703 | **trisong** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 704 | **detsen** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 705 | **vairotsana** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 706 | **sakya** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 707 | **patriarchs** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 708 | **marpa** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 709 | **milarepa** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 710 | **gampopa** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 711 | **tibetan** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 712 | **vidyādharas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 713 | **yidams** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 714 | **vinaya** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 715 | **abhidharma** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 716 | **tantras** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 717 | **pillars** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 718 | **chariots** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 719 | **behold** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 720 | **unfeigned** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 721 | **altruism** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 722 | **mantra-holders** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 723 | **samaya** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 724 | **drosses** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 725 | **shackles** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 726 | **jealousy** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 727 | **agitated** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 728 | **asuras** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 729 | **barbarians** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 730 | **abound** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 731 | **alas** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 732 | **sorrows** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 733 | **masteries** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 734 | **tibet** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 735 | **non-sectarian** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 736 | **throngs** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 737 | **aspire** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 738 | **sangha** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 739 | **pervade** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 740 | **drum** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 741 | **resound** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 742 | **loudly** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 743 | **shattering** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 744 | **skulls** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 745 | **heretical** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 746 | **elephants** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 747 | **patrons** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 748 | **demigods** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 749 | **bowing** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 750 | **captivating** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 751 | **flavors** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 752 | **wandering** | 1 | 4,182.29 | 9.59 | 🟡 high — specialist register |
| 753 | **name** | 2 | 4,044.75 | 4.637308 | 🟡 high — specialist register |
| 754 | **treasury** | 2 | 4,041.69 | 4.633793 | 🟡 high — specialist register |
| 755 | **many** | 2 | 4,017.54 | 4.60611 | 🟡 high — specialist register |
| 756 | **wise** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 757 | **regent** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 758 | **rays** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 759 | **transmissions** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 760 | **clarified** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 761 | **rows** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 762 | **accomplishment** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 763 | **amidst** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 764 | **fingers** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 765 | **midst** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 766 | **armor** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 767 | **tendencies** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 768 | **instant** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 769 | **accumulate** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 770 | **uproot** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 771 | **mistaken** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 772 | **dust** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 773 | **extremes** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 774 | **array** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 775 | **faults** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 776 | **harmony** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 777 | **heights** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 778 | **obstructing** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 779 | **engagement** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 780 | **trained** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 781 | **blessing** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 782 | **decay** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 783 | **painted** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 784 | **contention** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 785 | **strengths** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 786 | **disciplined** | 1 | 4,006.83 | 9.18767 | 🟡 high — specialist register |
| 787 | **within** | 2 | 3,988.27 | 4.57255 | 🟡 high — specialist register |
| 788 | **practiced** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 789 | **son** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 790 | **expression** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 791 | **locks** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 792 | **waves** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 793 | **prey** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 794 | **ignite** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 795 | **vigilance** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 796 | **blend** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 797 | **perceptions** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 798 | **forests** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 799 | **wilderness** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 800 | **humans** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 801 | **helm** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 802 | **pillar** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 803 | **touching** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 804 | **ring** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 805 | **pour** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 806 | **self** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 807 | **abundance** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 808 | **arises** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 809 | **emergence** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 810 | **awareness** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 811 | **abandonment** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 812 | **sage** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 813 | **snows** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 814 | **certainty** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 815 | **transformed** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 816 | **temples** | 1 | 3,881.37 | 8.899988 | 🟡 high — specialist register |
| 817 | **freed** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 818 | **speak** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 819 | **understands** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 820 | **violent** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 821 | **sword** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 822 | **exhausted** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 823 | **absent** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 824 | **accompany** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 825 | **tip** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 826 | **mere** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 827 | **wonder** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 828 | **flowers** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 829 | **assemblies** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 830 | **exert** | 1 | 3,784.06 | 8.676844 | 🟡 high — specialist register |
| 831 | **day** | 2 | 3,754.79 | 4.304868 | 🟡 high — specialist register |
| 832 | **firm** | 2 | 3,716.02 | 4.260416 | 🟡 high — specialist register |
| 833 | **mountains** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 834 | **overcome** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 835 | **preceded** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 836 | **experiencing** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 837 | **lands** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 838 | **fulfilling** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 839 | **posture** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 840 | **music** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 841 | **depths** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 842 | **grove** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 843 | **minds** | 1 | 3,704.55 | 8.494523 | 🟡 high — specialist register |
| 844 | **beneath** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 845 | **shrank** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 846 | **subdued** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 847 | **prince** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 848 | **abundant** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 849 | **lightning** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 850 | **diseases** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 851 | **medicine** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 852 | **accumulation** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 853 | **gateway** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 854 | **exchanging** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 855 | **naturally** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 856 | **wishes** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 857 | **backdrop** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 858 | **display** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 859 | **perform** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 860 | **beauty** | 1 | 3,637.32 | 8.340372 | 🟡 high — specialist register |
| 861 | **arose** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 862 | **acts** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 863 | **deeply** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 864 | **arisen** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 865 | **realization** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 866 | **merits** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 867 | **ita** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 868 | **genuine** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 869 | **generation** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 870 | **pollution** | 1 | 3,579.08 | 8.206841 | 🟡 high — specialist register |
| 871 | **fulfilled** | 1 | 3,527.72 | 8.089058 | 🟡 high — specialist register |
| 872 | **spreads** | 1 | 3,527.72 | 8.089058 | 🟡 high — specialist register |
| 873 | **remote** | 1 | 3,527.72 | 8.089058 | 🟡 high — specialist register |
| 874 | **hear** | 1 | 3,527.72 | 8.089058 | 🟡 high — specialist register |
| 875 | **burned** | 1 | 3,527.72 | 8.089058 | 🟡 high — specialist register |
| 876 | **steer** | 1 | 3,527.72 | 8.089058 | 🟡 high — specialist register |
| 877 | **object** | 1 | 3,527.72 | 8.089058 | 🟡 high — specialist register |
| 878 | **discouraged** | 1 | 3,527.72 | 8.089058 | 🟡 high — specialist register |
| 879 | **english** | 1 | 3,481.77 | 7.983697 | 🟡 high — specialist register |
| 880 | **blue** | 1 | 3,481.77 | 7.983697 | 🟡 high — specialist register |
| 881 | **unwanted** | 1 | 3,481.77 | 7.983697 | 🟡 high — specialist register |
| 882 | **harmful** | 1 | 3,481.77 | 7.983697 | 🟡 high — specialist register |
| 883 | **granting** | 1 | 3,481.77 | 7.983697 | 🟡 high — specialist register |
| 884 | **driven** | 1 | 3,481.77 | 7.983697 | 🟡 high — specialist register |
| 885 | **austerity** | 1 | 3,440.20 | 7.888387 | 🟡 high — specialist register |
| 886 | **recognize** | 1 | 3,440.20 | 7.888387 | 🟡 high — specialist register |
| 887 | **rescue** | 1 | 3,440.20 | 7.888387 | 🟡 high — specialist register |
| 888 | **mount** | 1 | 3,402.26 | 7.801376 | 🟡 high — specialist register |
| 889 | **meaningful** | 1 | 3,402.26 | 7.801376 | 🟡 high — specialist register |
| 890 | **sons** | 1 | 3,367.35 | 7.721333 | 🟡 high — specialist register |
| 891 | **relied** | 1 | 3,367.35 | 7.721333 | 🟡 high — specialist register |
| 892 | **intense** | 1 | 3,367.35 | 7.721333 | 🟡 high — specialist register |
| 893 | **sole** | 1 | 3,367.35 | 7.721333 | 🟡 high — specialist register |
| 894 | **reaches** | 1 | 3,367.35 | 7.721333 | 🟡 high — specialist register |
| 895 | **doors** | 1 | 3,367.35 | 7.721333 | 🟡 high — specialist register |
| 896 | **classes** | 1 | 3,367.35 | 7.721333 | 🟡 high — specialist register |
| 897 | **moreover** | 1 | 3,335.03 | 7.647225 | 🟡 high — specialist register |
| 898 | **spirits** | 1 | 3,335.03 | 7.647225 | 🟡 high — specialist register |
| 899 | **words** | 1 | 3,335.03 | 7.647225 | 🟡 high — specialist register |
| 900 | **furthermore** | 1 | 3,335.03 | 7.647225 | 🟡 high — specialist register |
| 901 | **extreme** | 1 | 3,335.03 | 7.647225 | 🟡 high — specialist register |
| 902 | **down** | 2 | 3,330.64 | 3.818584 | 🟡 high — specialist register |
| 903 | **ones** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 904 | **bodies** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 905 | **poison** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 906 | **pull** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 907 | **aggregates** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 908 | **training** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 909 | **guide** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 910 | **fulfill** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 911 | **wind** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 912 | **undermine** | 1 | 3,304.94 | 7.578232 | 🟡 high — specialist register |
| 913 | **bearing** | 1 | 3,276.80 | 7.513694 | 🟡 high — specialist register |
| 914 | **surface** | 1 | 3,276.80 | 7.513694 | 🟡 high — specialist register |
| 915 | **firmly** | 1 | 3,276.80 | 7.513694 | 🟡 high — specialist register |
| 916 | **stream** | 1 | 3,276.80 | 7.513694 | 🟡 high — specialist register |
| 917 | **meaning** | 1 | 3,276.80 | 7.513694 | 🟡 high — specialist register |
| 918 | **channel** | 1 | 3,276.80 | 7.513694 | 🟡 high — specialist register |
| 919 | **exist** | 1 | 3,250.36 | 7.453069 | 🟡 high — specialist register |
| 920 | **seed** | 1 | 3,250.36 | 7.453069 | 🟡 high — specialist register |
| 921 | **sudden** | 1 | 3,250.36 | 7.453069 | 🟡 high — specialist register |
| 922 | **heat** | 1 | 3,250.36 | 7.453069 | 🟡 high — specialist register |
| 923 | **stages** | 1 | 3,250.36 | 7.453069 | 🟡 high — specialist register |
| 924 | **bound** | 1 | 3,250.36 | 7.453069 | 🟡 high — specialist register |
| 925 | **constant** | 1 | 3,225.43 | 7.395911 | 🟡 high — specialist register |
| 926 | **understand** | 1 | 3,201.85 | 7.341843 | 🟡 high — specialist register |
| 927 | **merely** | 1 | 3,201.85 | 7.341843 | 🟡 high — specialist register |
| 928 | **millions** | 1 | 3,201.85 | 7.341843 | 🟡 high — specialist register |
| 929 | **elders** | 1 | 3,201.85 | 7.341843 | 🟡 high — specialist register |
| 930 | **universal** | 1 | 3,158.20 | 7.24176 | 🟡 high — specialist register |
| 931 | **harm** | 1 | 3,158.20 | 7.24176 | 🟡 high — specialist register |
| 932 | **continuous** | 1 | 3,137.92 | 7.19524 | 🟡 high — specialist register |
| 933 | **door** | 1 | 3,118.53 | 7.150788 | 🟡 high — specialist register |
| 934 | **introduce** | 1 | 3,118.53 | 7.150788 | 🟡 high — specialist register |
| 935 | **served** | 1 | 3,099.97 | 7.108229 | 🟡 high — specialist register |
| 936 | **foundation** | 1 | 3,099.97 | 7.108229 | 🟡 high — specialist register |
| 937 | **spirit** | 1 | 3,082.17 | 7.067407 | 🟡 high — specialist register |
| 938 | **stem** | 1 | 3,082.17 | 7.067407 | 🟡 high — specialist register |
| 939 | **intelligence** | 1 | 3,082.17 | 7.067407 | 🟡 high — specialist register |
| 940 | **arranged** | 1 | 3,065.06 | 7.028186 | 🟡 high — specialist register |
| 941 | **repeatedly** | 1 | 3,065.06 | 7.028186 | 🟡 high — specialist register |
| 942 | **finally** | 1 | 3,065.06 | 7.028186 | 🟡 high — specialist register |
| 943 | **essential** | 1 | 3,048.60 | 6.990446 | 🟡 high — specialist register |
| 944 | **ultimately** | 1 | 3,048.60 | 6.990446 | 🟡 high — specialist register |
| 945 | **physical** | 1 | 3,032.74 | 6.954078 | 🟡 high — specialist register |
| 946 | **generated** | 1 | 3,017.44 | 6.918987 | 🟡 high — specialist register |
| 947 | **drawn** | 1 | 3,017.44 | 6.918987 | 🟡 high — specialist register |
| 948 | **brief** | 1 | 3,017.44 | 6.918987 | 🟡 high — specialist register |
| 949 | **branches** | 1 | 2,988.35 | 6.852295 | 🟢 medium — moderately distinctive |
| 950 | **momentum** | 1 | 2,974.51 | 6.820546 | 🟢 medium — moderately distinctive |
| 951 | **destroyed** | 1 | 2,974.51 | 6.820546 | 🟢 medium — moderately distinctive |
| 952 | **experience** | 1 | 2,961.09 | 6.789775 | 🟢 medium — moderately distinctive |
| 953 | **withdrawn** | 1 | 2,961.09 | 6.789775 | 🟢 medium — moderately distinctive |
| 954 | **gradually** | 1 | 2,948.07 | 6.759922 | 🟢 medium — moderately distinctive |
| 955 | **powers** | 1 | 2,948.07 | 6.759922 | 🟢 medium — moderately distinctive |
| 956 | **reaching** | 1 | 2,948.07 | 6.759922 | 🟢 medium — moderately distinctive |
| 957 | **works** | 1 | 2,935.43 | 6.730934 | 🟢 medium — moderately distinctive |
| 958 | **finding** | 1 | 2,935.43 | 6.730934 | 🟢 medium — moderately distinctive |
| 959 | **aims** | 1 | 2,935.43 | 6.730934 | 🟢 medium — moderately distinctive |
| 960 | **purpose** | 1 | 2,923.14 | 6.702763 | 🟢 medium — moderately distinctive |
| 961 | **adverse** | 1 | 2,923.14 | 6.702763 | 🟢 medium — moderately distinctive |
| 962 | **indian** | 1 | 2,923.14 | 6.702763 | 🟢 medium — moderately distinctive |
| 963 | **settle** | 1 | 2,911.19 | 6.675364 | 🟢 medium — moderately distinctive |
| 964 | **favorable** | 1 | 2,911.19 | 6.675364 | 🟢 medium — moderately distinctive |
| 965 | **views** | 1 | 2,911.19 | 6.675364 | 🟢 medium — moderately distinctive |
| 966 | **lake** | 1 | 2,899.56 | 6.648696 | 🟢 medium — moderately distinctive |
| 967 | **bear** | 1 | 2,899.56 | 6.648696 | 🟢 medium — moderately distinctive |
| 968 | **doubt** | 1 | 2,888.23 | 6.622721 | 🟢 medium — moderately distinctive |
| 969 | **living** | 1 | 2,888.23 | 6.622721 | 🟢 medium — moderately distinctive |
| 970 | **presence** | 1 | 2,888.23 | 6.622721 | 🟢 medium — moderately distinctive |
| 971 | **slight** | 1 | 2,866.42 | 6.57271 | 🟢 medium — moderately distinctive |
| 972 | **million** | 1 | 2,866.42 | 6.57271 | 🟢 medium — moderately distinctive |
| 973 | **always** | 1 | 2,845.65 | 6.525082 | 🟢 medium — moderately distinctive |
| 974 | **arrangement** | 1 | 2,835.63 | 6.502093 | 🟢 medium — moderately distinctive |
| 975 | **appear** | 1 | 2,806.86 | 6.436135 | 🟢 medium — moderately distinctive |
| 976 | **red** | 1 | 2,806.86 | 6.436135 | 🟢 medium — moderately distinctive |
| 977 | **depend** | 1 | 2,797.68 | 6.415081 | 🟢 medium — moderately distinctive |
| 978 | **crowns** | 1 | 2,771.24 | 6.354457 | 🟢 medium — moderately distinctive |
| 979 | **care** | 1 | 2,762.77 | 6.335039 | 🟢 medium — moderately distinctive |
| 980 | **alone** | 1 | 2,762.77 | 6.335039 | 🟢 medium — moderately distinctive |
| 981 | **except** | 1 | 2,746.31 | 6.297298 | 🟢 medium — moderately distinctive |
| 982 | **concerns** | 1 | 2,746.31 | 6.297298 | 🟢 medium — moderately distinctive |
| 983 | **center** | 1 | 2,746.31 | 6.297298 | 🟢 medium — moderately distinctive |
| 984 | **ranges** | 1 | 2,738.31 | 6.278949 | 🟢 medium — moderately distinctive |
| 985 | **palm** | 1 | 2,738.31 | 6.278949 | 🟢 medium — moderately distinctive |
| 986 | **hearing** | 1 | 2,730.45 | 6.260931 | 🟢 medium — moderately distinctive |
| 987 | **hostile** | 1 | 2,730.45 | 6.260931 | 🟢 medium — moderately distinctive |
| 988 | **status** | 1 | 2,722.73 | 6.243231 | 🟢 medium — moderately distinctive |
| 989 | **circumstances** | 1 | 2,715.15 | 6.225839 | 🟢 medium — moderately distinctive |
| 990 | **why** | 1 | 2,715.15 | 6.225839 | 🟢 medium — moderately distinctive |
| 991 | **stand** | 1 | 2,707.70 | 6.208745 | 🟢 medium — moderately distinctive |
| 992 | **river** | 1 | 2,707.70 | 6.208745 | 🟢 medium — moderately distinctive |
| 993 | **side** | 1 | 2,707.70 | 6.208745 | 🟢 medium — moderately distinctive |
| 994 | **application** | 1 | 2,693.16 | 6.175409 | 🟢 medium — moderately distinctive |
| 995 | **bad** | 1 | 2,693.16 | 6.175409 | 🟢 medium — moderately distinctive |
| 996 | **fallen** | 1 | 2,693.16 | 6.175409 | 🟢 medium — moderately distinctive |
| 997 | **enter** | 1 | 2,686.07 | 6.159148 | 🟢 medium — moderately distinctive |
| 998 | **direction** | 1 | 2,672.22 | 6.127399 | 🟢 medium — moderately distinctive |
| 999 | **forces** | 1 | 2,665.46 | 6.111895 | 🟢 medium — moderately distinctive |
| 1000 | **india** | 1 | 2,665.46 | 6.111895 | 🟢 medium — moderately distinctive |
| 1001 | **turn** | 1 | 2,658.80 | 6.096628 | 🟢 medium — moderately distinctive |
| 1002 | **placed** | 1 | 2,652.24 | 6.08159 | 🟢 medium — moderately distinctive |
| 1003 | **resolve** | 1 | 2,652.24 | 6.08159 | 🟢 medium — moderately distinctive |
| 1004 | **developed** | 1 | 2,645.78 | 6.066775 | 🟢 medium — moderately distinctive |
| 1005 | **royal** | 1 | 2,639.41 | 6.052176 | 🟢 medium — moderately distinctive |
| 1006 | **brings** | 1 | 2,639.41 | 6.052176 | 🟢 medium — moderately distinctive |
| 1007 | **possibly** | 1 | 2,633.14 | 6.037787 | 🟢 medium — moderately distinctive |
| 1008 | **appears** | 1 | 2,633.14 | 6.037787 | 🟢 medium — moderately distinctive |
| 1009 | **original** | 1 | 2,633.14 | 6.037787 | 🟢 medium — moderately distinctive |
| 1010 | **effects** | 1 | 2,626.95 | 6.023602 | 🟢 medium — moderately distinctive |
| 1011 | **thought** | 1 | 2,626.95 | 6.023602 | 🟢 medium — moderately distinctive |
| 1012 | **upward** | 1 | 2,620.85 | 6.009616 | 🟢 medium — moderately distinctive |
| 1013 | **newly** | 1 | 2,620.85 | 6.009616 | 🟢 medium — moderately distinctive |
| 1014 | **nothing** | 1 | 2,620.85 | 6.009616 | 🟢 medium — moderately distinctive |
| 1015 | **water** | 1 | 2,608.90 | 5.982217 | 🟢 medium — moderately distinctive |
| 1016 | **intended** | 1 | 2,597.27 | 5.955549 | 🟢 medium — moderately distinctive |
| 1017 | **toward** | 1 | 2,585.95 | 5.929574 | 🟢 medium — moderately distinctive |
| 1018 | **entire** | 1 | 2,585.95 | 5.929574 | 🟢 medium — moderately distinctive |
| 1019 | **hopes** | 1 | 2,564.14 | 5.879563 | 🟢 medium — moderately distinctive |
| 1020 | **once** | 1 | 2,558.85 | 5.867442 | 🟢 medium — moderately distinctive |
| 1021 | **forward** | 1 | 2,543.36 | 5.831935 | 🟢 medium — moderately distinctive |
| 1022 | **quickly** | 1 | 2,538.32 | 5.820374 | 🟢 medium — moderately distinctive |
| 1023 | **actions** | 1 | 2,533.34 | 5.808946 | 🟢 medium — moderately distinctive |
| 1024 | **ways** | 1 | 2,528.41 | 5.797646 | 🟢 medium — moderately distinctive |
| 1025 | **field** | 1 | 2,481.97 | 5.691163 | 🟢 medium — moderately distinctive |
| 1026 | **opening** | 1 | 2,473.25 | 5.671162 | 🟢 medium — moderately distinctive |
| 1027 | **basic** | 1 | 2,473.25 | 5.671162 | 🟢 medium — moderately distinctive |
| 1028 | **together** | 1 | 2,468.95 | 5.66131 | 🟢 medium — moderately distinctive |
| 1029 | **grow** | 1 | 2,464.70 | 5.651553 | 🟢 medium — moderately distinctive |
| 1030 | **various** | 1 | 2,452.18 | 5.622843 | 🟢 medium — moderately distinctive |
| 1031 | **flow** | 1 | 2,444.03 | 5.604151 | 🟢 medium — moderately distinctive |
| 1032 | **formed** | 1 | 2,440.01 | 5.594934 | 🟢 medium — moderately distinctive |
| 1033 | **strike** | 1 | 2,432.08 | 5.576752 | 🟢 medium — moderately distinctive |
| 1034 | **along** | 1 | 2,432.08 | 5.576752 | 🟢 medium — moderately distinctive |
| 1035 | **completion** | 1 | 2,432.08 | 5.576752 | 🟢 medium — moderately distinctive |
| 1036 | **opened** | 1 | 2,428.17 | 5.567784 | 🟢 medium — moderately distinctive |
| 1037 | **needs** | 1 | 2,416.64 | 5.54135 | 🟢 medium — moderately distinctive |
| 1038 | **study** | 1 | 2,398.08 | 5.498791 | 🟢 medium — moderately distinctive |
| 1039 | **definitive** | 1 | 2,369.93 | 5.434252 | 🟢 medium — moderately distinctive |
| 1040 | **took** | 1 | 2,369.93 | 5.434252 | 🟢 medium — moderately distinctive |
| 1041 | **city** | 1 | 2,366.54 | 5.42647 | 🟢 medium — moderately distinctive |
| 1042 | **prepared** | 1 | 2,363.17 | 5.418748 | 🟢 medium — moderately distinctive |
| 1043 | **view** | 1 | 2,349.95 | 5.388443 | 🟢 medium — moderately distinctive |
| 1044 | **difficult** | 1 | 2,340.30 | 5.366301 | 🟢 medium — moderately distinctive |
| 1045 | **act** | 1 | 2,324.66 | 5.330455 | 🟢 medium — moderately distinctive |
| 1046 | **remains** | 1 | 2,321.60 | 5.323438 | 🟢 medium — moderately distinctive |
| 1047 | **maintain** | 1 | 2,321.60 | 5.323438 | 🟢 medium — moderately distinctive |
| 1048 | **able** | 1 | 2,306.62 | 5.28907 | 🟢 medium — moderately distinctive |
| 1049 | **similar** | 1 | 2,280.87 | 5.230037 | 🟢 medium — moderately distinctive |
| 1050 | **makes** | 1 | 2,272.62 | 5.211109 | 🟢 medium — moderately distinctive |
| 1051 | **force** | 1 | 2,264.51 | 5.192532 | 🟢 medium — moderately distinctive |
| 1052 | **local** | 1 | 2,256.56 | 5.174295 | 🟢 medium — moderately distinctive |
| 1053 | **marks** | 1 | 2,246.18 | 5.150484 | 🟢 medium — moderately distinctive |
| 1054 | **taking** | 1 | 2,236.03 | 5.127227 | 🟢 medium — moderately distinctive |
| 1055 | **again** | 1 | 2,209.30 | 5.065927 | 🟢 medium — moderately distinctive |
| 1056 | **gave** | 1 | 2,179.68 | 4.998015 | 🟢 medium — moderately distinctive |
| 1057 | **small** | 1 | 2,166.66 | 4.968162 | 🟢 medium — moderately distinctive |
| 1058 | **holders** | 1 | 2,158.20 | 4.948744 | 🟢 medium — moderately distinctive |
| 1059 | **base** | 1 | 2,139.72 | 4.906385 | 🟢 medium — moderately distinctive |
| 1060 | **term** | 1 | 2,133.74 | 4.892655 | 🟢 medium — moderately distinctive |
| 1061 | **offered** | 1 | 2,093.98 | 4.801485 | 🟢 medium — moderately distinctive |
| 1062 | **rising** | 1 | 2,090.37 | 4.793221 | 🟢 medium — moderately distinctive |
| 1063 | **reduced** | 1 | 2,090.37 | 4.793221 | 🟢 medium — moderately distinctive |
| 1064 | **meet** | 1 | 2,088.58 | 4.789114 | 🟢 medium — moderately distinctive |
| 1065 | **work** | 1 | 2,086.80 | 4.785024 | 🟢 medium — moderately distinctive |
| 1066 | **way** | 1 | 2,077.99 | 4.764821 | 🟢 medium — moderately distinctive |
| 1067 | **saying** | 1 | 2,076.24 | 4.760829 | 🟢 medium — moderately distinctive |
| 1068 | **need** | 1 | 2,055.88 | 4.714128 | 🟢 medium — moderately distinctive |
| 1069 | **among** | 1 | 2,054.22 | 4.710333 | 🟢 medium — moderately distinctive |
| 1070 | **line** | 1 | 2,049.30 | 4.699034 | 🟢 medium — moderately distinctive |
| 1071 | **raise** | 1 | 2,049.30 | 4.699034 | 🟢 medium — moderately distinctive |
| 1072 | **see** | 1 | 2,039.60 | 4.676811 | 🟢 medium — moderately distinctive |
| 1073 | **reached** | 1 | 2,030.12 | 4.655071 | 🟢 medium — moderately distinctive |
| 1074 | **systems** | 1 | 2,023.91 | 4.640835 | 🟢 medium — moderately distinctive |
| 1075 | **support** | 1 | 2,008.77 | 4.60611 | 🟢 medium — moderately distinctive |
| 1076 | **currently** | 1 | 2,004.33 | 4.595923 | 🟢 medium — moderately distinctive |
| 1077 | **raised** | 1 | 2,004.33 | 4.595923 | 🟢 medium — moderately distinctive |
| 1078 | **later** | 1 | 1,987.00 | 4.556183 | 🟢 medium — moderately distinctive |
| 1079 | **according** | 1 | 1,975.81 | 4.53054 | 🟢 medium — moderately distinctive |
| 1080 | **union** | 1 | 1,974.44 | 4.527381 | 🟢 medium — moderately distinctive |
| 1081 | **subject** | 1 | 1,932.49 | 4.43121 | 🟢 medium — moderately distinctive |
| 1082 | **levels** | 1 | 1,921.39 | 4.405749 | 🟢 medium — moderately distinctive |
| 1083 | **following** | 1 | 1,904.66 | 4.367389 | 🟢 medium — moderately distinctive |
| 1084 | **second** | 1 | 1,887.42 | 4.327858 | 🟢 medium — moderately distinctive |
| 1085 | **results** | 1 | 1,800.83 | 4.129303 | 🟢 medium — moderately distinctive |
| 1086 | **including** | 1 | 1,783.62 | 4.089838 | 🟢 medium — moderately distinctive |
| 1087 | **central** | 1 | 1,759.43 | 4.034378 | 🟢 medium — moderately distinctive |
| 1088 | **during** | 1 | 1,747.01 | 4.005887 | 🟢 medium — moderately distinctive |
| 1089 | **cut** | 1 | 1,744.56 | 4.000284 | 🟢 medium — moderately distinctive |
| 1090 | **next** | 1 | 1,706.48 | 3.912963 | 🟢 medium — moderately distinctive |
| 1091 | **lower** | 1 | 1,704.25 | 3.907856 | 🟢 medium — moderately distinctive |
| 1092 | **common** | 1 | 1,626.47 | 3.729504 | 🟢 medium — moderately distinctive |
| 1093 | **offer** | 1 | 1,624.62 | 3.725252 | 🟢 medium — moderately distinctive |
| 1094 | **made** | 1 | 1,570.18 | 3.600421 | 🟢 medium — moderately distinctive |
| 1095 | **increase** | 1 | 1,541.73 | 3.535181 | 🟢 medium — moderately distinctive |

---

*Corpus reference: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth\_idf=True, lowercase=True).*  
*Generated 2026-09-21 by `generate_termbase.py`.*