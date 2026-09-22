---
title: TF-IDF Vocabulary Analysis — en-clean-scoped
source: /sessions/rcw-011mhyqwtxjhdxwizpw481gz/mnt/tara-sadhana-rails/0-INBOX/temp/keyword-work/en-clean-scoped.md
corpus: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth_idf=True)
method: TF × IDF — term frequency in translation vs. inverse document frequency in Reuters corpus
generated: 2026-09-21
unique_terms: 1094
total_content_tokens: 2,151
status: draft
---

# TF-IDF Vocabulary Analysis — en-clean-scoped

Generated **2026-09-21** · source: `en-clean-scoped.md` · **1,094 unique content terms** ranked.

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

| IDF range  | Meaning                                                 |
| ---------- | ------------------------------------------------------- |
| 1.0 – 1.5  | Function word — present in virtually every document     |
| 1.5 – 3.0  | Common content word — high general-English frequency    |
| 3.0 – 6.0  | Moderately rare — limited domain or register            |
| 6.0 – 9.0  | Uncommon / archaic — rare in Reuters                    |
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
| 🟠 very high — domain-specific | 155 | 14.2% |
| 🟡 high — specialist register | 808 | 73.9% |
| 🟢 medium — moderately distinctive | 121 | 11.1% |
| 🔵 low — common in general English | 0 | 0.0% |
| ⚪ very low — function / universal word | 0 | 0.0% |

---

## Most Distinctive Words (highest TF-IDF)

Words that appear **frequently in this text** yet are **rare or absent in general English**.

**1. jetsunma** — count: 33, TF-IDF: 147,127, IDF: 9.59 🔴 extremely high — text-exclusive
**2. homage** — count: 26, TF-IDF: 115,918, IDF: 9.59 🔴 extremely high — text-exclusive
**3. teachings** — count: 24, TF-IDF: 107,001, IDF: 9.59 🔴 extremely high — text-exclusive
**4. beings** — count: 20, TF-IDF: 89,168, IDF: 9.59 🔴 extremely high — text-exclusive
**5. prostrate** — count: 17, TF-IDF: 75,793, IDF: 9.59 🔴 extremely high — text-exclusive
**6. please** — count: 18, TF-IDF: 71,084, IDF: 8.494523 🔴 extremely high — text-exclusive
**7. supreme** — count: 20, TF-IDF: 66,488, IDF: 7.150788 🔴 extremely high — text-exclusive
**8. noble** — count: 15, TF-IDF: 64,070, IDF: 9.18767 🔴 extremely high — text-exclusive
**9. enlightenment** — count: 12, TF-IDF: 53,501, IDF: 9.59 🔴 extremely high — text-exclusive
**10. grant** — count: 16, TF-IDF: 50,970, IDF: 6.852295 🔴 extremely high — text-exclusive
**11. dharma** — count: 11, TF-IDF: 49,042, IDF: 9.59 🟠 very high — domain-specific
**12. mother** — count: 11, TF-IDF: 49,042, IDF: 9.59 🟠 very high — domain-specific
**13. pray** — count: 10, TF-IDF: 44,584, IDF: 9.59 🟠 very high — domain-specific
**14. happiness** — count: 10, TF-IDF: 44,584, IDF: 9.59 🟠 very high — domain-specific
**15. lotus** — count: 10, TF-IDF: 42,713, IDF: 9.18767 🟠 very high — domain-specific
**16. wish-fulfilling** — count: 9, TF-IDF: 40,126, IDF: 9.59 🟠 very high — domain-specific
**17. lady** — count: 9, TF-IDF: 40,126, IDF: 9.59 🟠 very high — domain-specific
**18. wheel** — count: 8, TF-IDF: 35,679, IDF: 9.593135 🟠 very high — domain-specific
**19. hosts** — count: 8, TF-IDF: 35,667, IDF: 9.59 🟠 very high — domain-specific
**20. like** — count: 14, TF-IDF: 33,796, IDF: 5.192532 🟠 very high — domain-specific
**21. existence** — count: 9, TF-IDF: 31,997, IDF: 7.647225 🟠 very high — domain-specific
**22. wisdom** — count: 8, TF-IDF: 31,593, IDF: 8.494523 🟠 very high — domain-specific
**23. ten** — count: 11, TF-IDF: 31,497, IDF: 6.159148 🟠 very high — domain-specific
**24. victors** — count: 7, TF-IDF: 31,219, IDF: 9.593135 🟠 very high — domain-specific
**25. compassion** — count: 7, TF-IDF: 31,219, IDF: 9.593135 🟠 very high — domain-specific
**26. buddha** — count: 7, TF-IDF: 31,209, IDF: 9.59 🟠 very high — domain-specific
**27. realms** — count: 7, TF-IDF: 31,209, IDF: 9.59 🟠 very high — domain-specific
**28. attained** — count: 7, TF-IDF: 29,899, IDF: 9.18767 🟠 very high — domain-specific
**29. perfect** — count: 7, TF-IDF: 29,899, IDF: 9.18767 🟠 very high — domain-specific
**30. every** — count: 11, TF-IDF: 29,649, IDF: 5.797646 🟠 very high — domain-specific
**31. refuge** — count: 7, TF-IDF: 27,644, IDF: 8.494523 🟠 very high — domain-specific
**32. gods** — count: 6, TF-IDF: 26,750, IDF: 9.59 🟠 very high — domain-specific
**33. possess** — count: 6, TF-IDF: 26,750, IDF: 9.59 🟠 very high — domain-specific
**34. mind** — count: 8, TF-IDF: 26,595, IDF: 7.150788 🟠 very high — domain-specific
**35. ocean** — count: 8, TF-IDF: 26,595, IDF: 7.150788 🟠 very high — domain-specific
**36. benefit** — count: 10, TF-IDF: 25,762, IDF: 5.54135 🟠 very high — domain-specific
**37. accomplishments** — count: 6, TF-IDF: 25,628, IDF: 9.18767 🟠 very high — domain-specific
**38. profound** — count: 6, TF-IDF: 25,628, IDF: 9.18767 🟠 very high — domain-specific
**39. directions** — count: 6, TF-IDF: 24,826, IDF: 8.899988 🟠 very high — domain-specific
**40. sake** — count: 6, TF-IDF: 24,203, IDF: 8.676844 🟠 very high — domain-specific
**41. accomplished** — count: 6, TF-IDF: 23,695, IDF: 8.494523 🟠 very high — domain-specific
**42. age** — count: 6, TF-IDF: 23,265, IDF: 8.340372 🟠 very high — domain-specific
**43. life** — count: 9, TF-IDF: 23,043, IDF: 5.507159 🟠 very high — domain-specific
**44. perfectly** — count: 6, TF-IDF: 22,892, IDF: 8.206841 🟠 very high — domain-specific
**45. light** — count: 9, TF-IDF: 22,837, IDF: 5.457969 🟠 very high — domain-specific
**46. completely** — count: 7, TF-IDF: 22,516, IDF: 6.918987 🟠 very high — domain-specific
**47. liberation** — count: 5, TF-IDF: 22,299, IDF: 9.593135 🟠 very high — domain-specific
**48. flourish** — count: 5, TF-IDF: 22,299, IDF: 9.593135 🟠 very high — domain-specific
**49. degenerate** — count: 5, TF-IDF: 22,299, IDF: 9.593135 🟠 very high — domain-specific
**50. adorned** — count: 5, TF-IDF: 22,292, IDF: 9.59 🟠 very high — domain-specific

---

## Least Distinctive Words (lowest TF-IDF)

Words that appear in this text but are also extremely common in general English.

**1. increase** — count: 1, TF-IDF: 1,643.51, IDF: 3.535181 🟢 medium — moderately distinctive
**2. made** — count: 1, TF-IDF: 1,673.84, IDF: 3.600421 🟢 medium — moderately distinctive
**3. offer** — count: 1, TF-IDF: 1,731.87, IDF: 3.725252 🟢 medium — moderately distinctive
**4. common** — count: 1, TF-IDF: 1,733.85, IDF: 3.729504 🟢 medium — moderately distinctive
**5. lower** — count: 1, TF-IDF: 1,816.76, IDF: 3.907856 🟢 medium — moderately distinctive
**6. next** — count: 1, TF-IDF: 1,819.14, IDF: 3.912963 🟢 medium — moderately distinctive
**7. cut** — count: 1, TF-IDF: 1,859.73, IDF: 4.000284 🟢 medium — moderately distinctive
**8. during** — count: 1, TF-IDF: 1,862.34, IDF: 4.005887 🟢 medium — moderately distinctive
**9. central** — count: 1, TF-IDF: 1,875.58, IDF: 4.034378 🟢 medium — moderately distinctive
**10. including** — count: 1, TF-IDF: 1,901.37, IDF: 4.089838 🟢 medium — moderately distinctive
**11. results** — count: 1, TF-IDF: 1,919.71, IDF: 4.129303 🟢 medium — moderately distinctive
**12. second** — count: 1, TF-IDF: 2,012.02, IDF: 4.327858 🟢 medium — moderately distinctive
**13. following** — count: 1, TF-IDF: 2,030.40, IDF: 4.367389 🟢 medium — moderately distinctive
**14. levels** — count: 1, TF-IDF: 2,048.23, IDF: 4.405749 🟢 medium — moderately distinctive
**15. subject** — count: 1, TF-IDF: 2,060.07, IDF: 4.43121 🟢 medium — moderately distinctive
**16. union** — count: 1, TF-IDF: 2,104.78, IDF: 4.527381 🟢 medium — moderately distinctive
**17. according** — count: 1, TF-IDF: 2,106.25, IDF: 4.53054 🟢 medium — moderately distinctive
**18. later** — count: 1, TF-IDF: 2,118.17, IDF: 4.556183 🟢 medium — moderately distinctive
**19. raised** — count: 1, TF-IDF: 2,136.64, IDF: 4.595923 🟢 medium — moderately distinctive
**20. currently** — count: 1, TF-IDF: 2,136.64, IDF: 4.595923 🟢 medium — moderately distinctive
**21. support** — count: 1, TF-IDF: 2,141.38, IDF: 4.60611 🟢 medium — moderately distinctive
**22. systems** — count: 1, TF-IDF: 2,157.52, IDF: 4.640835 🟢 medium — moderately distinctive
**23. reached** — count: 1, TF-IDF: 2,164.14, IDF: 4.655071 🟢 medium — moderately distinctive
**24. see** — count: 1, TF-IDF: 2,174.25, IDF: 4.676811 🟢 medium — moderately distinctive
**25. raise** — count: 1, TF-IDF: 2,184.58, IDF: 4.699034 🟢 medium — moderately distinctive
**26. line** — count: 1, TF-IDF: 2,184.58, IDF: 4.699034 🟢 medium — moderately distinctive
**27. among** — count: 1, TF-IDF: 2,189.83, IDF: 4.710333 🟢 medium — moderately distinctive
**28. need** — count: 1, TF-IDF: 2,191.60, IDF: 4.714128 🟢 medium — moderately distinctive
**29. saying** — count: 1, TF-IDF: 2,213.31, IDF: 4.760829 🟢 medium — moderately distinctive
**30. way** — count: 1, TF-IDF: 2,215.17, IDF: 4.764821 🟢 medium — moderately distinctive
**31. work** — count: 1, TF-IDF: 2,224.56, IDF: 4.785024 🟢 medium — moderately distinctive
**32. meet** — count: 1, TF-IDF: 2,226.46, IDF: 4.789114 🟢 medium — moderately distinctive
**33. reduced** — count: 1, TF-IDF: 2,228.37, IDF: 4.793221 🟢 medium — moderately distinctive
**34. rising** — count: 1, TF-IDF: 2,228.37, IDF: 4.793221 🟢 medium — moderately distinctive
**35. offered** — count: 1, TF-IDF: 2,232.21, IDF: 4.801485 🟢 medium — moderately distinctive
**36. term** — count: 1, TF-IDF: 2,274.60, IDF: 4.892655 🟢 medium — moderately distinctive
**37. base** — count: 1, TF-IDF: 2,280.98, IDF: 4.906385 🟢 medium — moderately distinctive
**38. holders** — count: 1, TF-IDF: 2,300.67, IDF: 4.948744 🟢 medium — moderately distinctive
**39. small** — count: 1, TF-IDF: 2,309.70, IDF: 4.968162 🟢 medium — moderately distinctive
**40. gave** — count: 1, TF-IDF: 2,323.58, IDF: 4.998015 🟢 medium — moderately distinctive
**41. again** — count: 1, TF-IDF: 2,355.15, IDF: 5.065927 🟢 medium — moderately distinctive
**42. taking** — count: 1, TF-IDF: 2,383.65, IDF: 5.127227 🟢 medium — moderately distinctive
**43. marks** — count: 1, TF-IDF: 2,394.46, IDF: 5.150484 🟢 medium — moderately distinctive
**44. local** — count: 1, TF-IDF: 2,405.53, IDF: 5.174295 🟢 medium — moderately distinctive
**45. force** — count: 1, TF-IDF: 2,414.01, IDF: 5.192532 🟢 medium — moderately distinctive
**46. makes** — count: 1, TF-IDF: 2,422.64, IDF: 5.211109 🟢 medium — moderately distinctive
**47. similar** — count: 1, TF-IDF: 2,431.44, IDF: 5.230037 🟢 medium — moderately distinctive
**48. able** — count: 1, TF-IDF: 2,458.89, IDF: 5.28907 🟢 medium — moderately distinctive
**49. maintain** — count: 1, TF-IDF: 2,474.87, IDF: 5.323438 🟢 medium — moderately distinctive
**50. remains** — count: 1, TF-IDF: 2,474.87, IDF: 5.323438 🟢 medium — moderately distinctive

---

## Full Ranked Table

All 1,094 content terms, sorted by TF-IDF descending.

| Rank | Word | Count | TF-IDF | IDF | Band |
|------|------|-------|--------|-----|------|
| 1 | **jetsunma** | 33 | 147,126.92 | 9.59 | 🔴 extremely high — text-exclusive |
| 2 | **homage** | 26 | 115,918.18 | 9.59 | 🔴 extremely high — text-exclusive |
| 3 | **teachings** | 24 | 107,001.39 | 9.59 | 🔴 extremely high — text-exclusive |
| 4 | **beings** | 20 | 89,167.83 | 9.59 | 🔴 extremely high — text-exclusive |
| 5 | **prostrate** | 17 | 75,792.65 | 9.59 | 🔴 extremely high — text-exclusive |
| 6 | **please** | 18 | 71,083.87 | 8.494523 | 🔴 extremely high — text-exclusive |
| 7 | **supreme** | 20 | 66,488.03 | 7.150788 | 🔴 extremely high — text-exclusive |
| 8 | **noble** | 15 | 64,070.22 | 9.18767 | 🔴 extremely high — text-exclusive |
| 9 | **enlightenment** | 12 | 53,500.70 | 9.59 | 🔴 extremely high — text-exclusive |
| 10 | **grant** | 16 | 50,970.12 | 6.852295 | 🔴 extremely high — text-exclusive |
| 11 | **dharma** | 11 | 49,042.31 | 9.59 | 🟠 very high — domain-specific |
| 12 | **mother** | 11 | 49,042.31 | 9.59 | 🟠 very high — domain-specific |
| 13 | **pray** | 10 | 44,583.91 | 9.59 | 🟠 very high — domain-specific |
| 14 | **happiness** | 10 | 44,583.91 | 9.59 | 🟠 very high — domain-specific |
| 15 | **lotus** | 10 | 42,713.48 | 9.18767 | 🟠 very high — domain-specific |
| 16 | **wish-fulfilling** | 9 | 40,125.52 | 9.59 | 🟠 very high — domain-specific |
| 17 | **lady** | 9 | 40,125.52 | 9.59 | 🟠 very high — domain-specific |
| 18 | **wheel** | 8 | 35,678.79 | 9.593135 | 🟠 very high — domain-specific |
| 19 | **hosts** | 8 | 35,667.13 | 9.59 | 🟠 very high — domain-specific |
| 20 | **like** | 14 | 33,796.12 | 5.192532 | 🟠 very high — domain-specific |
| 21 | **existence** | 9 | 31,996.76 | 7.647225 | 🟠 very high — domain-specific |
| 22 | **wisdom** | 8 | 31,592.83 | 8.494523 | 🟠 very high — domain-specific |
| 23 | **ten** | 11 | 31,497.27 | 6.159148 | 🟠 very high — domain-specific |
| 24 | **victors** | 7 | 31,218.94 | 9.593135 | 🟠 very high — domain-specific |
| 25 | **compassion** | 7 | 31,218.94 | 9.593135 | 🟠 very high — domain-specific |
| 26 | **buddha** | 7 | 31,208.74 | 9.59 | 🟠 very high — domain-specific |
| 27 | **realms** | 7 | 31,208.74 | 9.59 | 🟠 very high — domain-specific |
| 28 | **attained** | 7 | 29,899.44 | 9.18767 | 🟠 very high — domain-specific |
| 29 | **perfect** | 7 | 29,899.44 | 9.18767 | 🟠 very high — domain-specific |
| 30 | **every** | 11 | 29,648.58 | 5.797646 | 🟠 very high — domain-specific |
| 31 | **refuge** | 7 | 27,643.73 | 8.494523 | 🟠 very high — domain-specific |
| 32 | **gods** | 6 | 26,750.35 | 9.59 | 🟠 very high — domain-specific |
| 33 | **possess** | 6 | 26,750.35 | 9.59 | 🟠 very high — domain-specific |
| 34 | **mind** | 8 | 26,595.21 | 7.150788 | 🟠 very high — domain-specific |
| 35 | **ocean** | 8 | 26,595.21 | 7.150788 | 🟠 very high — domain-specific |
| 36 | **benefit** | 10 | 25,761.74 | 5.54135 | 🟠 very high — domain-specific |
| 37 | **accomplishments** | 6 | 25,628.09 | 9.18767 | 🟠 very high — domain-specific |
| 38 | **profound** | 6 | 25,628.09 | 9.18767 | 🟠 very high — domain-specific |
| 39 | **directions** | 6 | 24,825.63 | 8.899988 | 🟠 very high — domain-specific |
| 40 | **sake** | 6 | 24,203.19 | 8.676844 | 🟠 very high — domain-specific |
| 41 | **accomplished** | 6 | 23,694.62 | 8.494523 | 🟠 very high — domain-specific |
| 42 | **age** | 6 | 23,264.64 | 8.340372 | 🟠 very high — domain-specific |
| 43 | **life** | 9 | 23,042.51 | 5.507159 | 🟠 very high — domain-specific |
| 44 | **perfectly** | 6 | 22,892.16 | 8.206841 | 🟠 very high — domain-specific |
| 45 | **light** | 9 | 22,836.69 | 5.457969 | 🟠 very high — domain-specific |
| 46 | **completely** | 7 | 22,516.46 | 6.918987 | 🟠 very high — domain-specific |
| 47 | **liberation** | 5 | 22,299.24 | 9.593135 | 🟠 very high — domain-specific |
| 48 | **flourish** | 5 | 22,299.24 | 9.593135 | 🟠 very high — domain-specific |
| 49 | **degenerate** | 5 | 22,299.24 | 9.593135 | 🟠 very high — domain-specific |
| 50 | **adorned** | 5 | 22,291.96 | 9.59 | 🟠 very high — domain-specific |
| 51 | **enlightened** | 5 | 22,291.96 | 9.59 | 🟠 very high — domain-specific |
| 52 | **tārā** | 5 | 22,291.96 | 9.59 | 🟠 very high — domain-specific |
| 53 | **primordial** | 5 | 22,291.96 | 9.59 | 🟠 very high — domain-specific |
| 54 | **ture** | 5 | 22,291.96 | 9.59 | 🟠 very high — domain-specific |
| 55 | **moon** | 5 | 22,291.96 | 9.59 | 🟠 very high — domain-specific |
| 56 | **cyclic** | 5 | 22,291.96 | 9.59 | 🟠 very high — domain-specific |
| 57 | **power** | 9 | 22,073.84 | 5.275647 | 🟠 very high — domain-specific |
| 58 | **without** | 10 | 21,951.47 | 4.721762 | 🟠 very high — domain-specific |
| 59 | **eyes** | 5 | 21,356.74 | 9.18767 | 🟠 very high — domain-specific |
| 60 | **infinite** | 5 | 21,356.74 | 9.18767 | 🟠 very high — domain-specific |
| 61 | **vast** | 6 | 21,331.17 | 7.647225 | 🟠 very high — domain-specific |
| 62 | **heirs** | 5 | 20,688.02 | 8.899988 | 🟠 very high — domain-specific |
| 63 | **peace** | 5 | 20,169.33 | 8.676844 | 🟠 very high — domain-specific |
| 64 | **space** | 6 | 19,713.83 | 7.067407 | 🟠 very high — domain-specific |
| 65 | **having** | 7 | 18,329.27 | 5.632322 | 🟠 very high — domain-specific |
| 66 | **blazing** | 4 | 17,839.40 | 9.593135 | 🟠 very high — domain-specific |
| 67 | **joy** | 4 | 17,839.40 | 9.593135 | 🟠 very high — domain-specific |
| 68 | **essence** | 4 | 17,839.40 | 9.593135 | 🟠 very high — domain-specific |
| 69 | **dispel** | 4 | 17,839.40 | 9.593135 | 🟠 very high — domain-specific |
| 70 | **glory** | 4 | 17,839.40 | 9.593135 | 🟠 very high — domain-specific |
| 71 | **bloom** | 4 | 17,839.40 | 9.593135 | 🟠 very high — domain-specific |
| 72 | **devotion** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 73 | **māra** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 74 | **protector** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 75 | **mantra** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 76 | **endowed** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 77 | **tuttāre** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 78 | **jewels** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 79 | **demons** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 80 | **syllable** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 81 | **hūṁ** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 82 | **possessing** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 83 | **karma** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 84 | **buddhas** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 85 | **compassionate** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 86 | **blessings** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 87 | **bodhisattvas** | 4 | 17,833.57 | 9.59 | 🟠 very high — domain-specific |
| 88 | **hundred** | 5 | 17,324.66 | 7.453069 | 🟠 very high — domain-specific |
| 89 | **worlds** | 4 | 17,085.39 | 9.18767 | 🟠 very high — domain-specific |
| 90 | **forth** | 4 | 17,085.39 | 9.18767 | 🟠 very high — domain-specific |
| 91 | **precious** | 5 | 17,066.12 | 7.341843 | 🟠 very high — domain-specific |
| 92 | **suffering** | 5 | 16,833.47 | 7.24176 | 🟠 very high — domain-specific |
| 93 | **exception** | 5 | 16,725.34 | 7.19524 | 🟠 very high — domain-specific |
| 94 | **peaceful** | 4 | 16,550.42 | 8.899988 | 🟠 very high — domain-specific |
| 95 | **clouds** | 4 | 16,550.42 | 8.899988 | 🟠 very high — domain-specific |
| 96 | **heart** | 5 | 16,249.29 | 6.990446 | 🟠 very high — domain-specific |
| 97 | **merit** | 4 | 15,509.76 | 8.340372 | 🟠 very high — domain-specific |
| 98 | **desired** | 4 | 15,261.44 | 8.206841 | 🟠 very high — domain-specific |
| 99 | **gathered** | 4 | 15,042.41 | 8.089058 | 🟠 very high — domain-specific |
| 100 | **qualities** | 4 | 14,846.48 | 7.983697 | 🟠 very high — domain-specific |
| 101 | **moment** | 5 | 14,512.39 | 6.243231 | 🟠 very high — domain-specific |
| 102 | **victor** | 4 | 14,358.59 | 7.721333 | 🟠 very high — domain-specific |
| 103 | **swift** | 4 | 14,358.59 | 7.721333 | 🟠 very high — domain-specific |
| 104 | **lord** | 4 | 14,092.48 | 7.578232 | 🟠 very high — domain-specific |
| 105 | **secret** | 4 | 14,092.48 | 7.578232 | 🟠 very high — domain-specific |
| 106 | **feet** | 5 | 13,424.97 | 5.775423 | 🟠 very high — domain-specific |
| 107 | **virtue** | 3 | 13,379.55 | 9.593135 | 🟠 very high — domain-specific |
| 108 | **guru** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 109 | **mañjugho** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 110 | **meditative** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 111 | **brahmā** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 112 | **wondrous** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 113 | **victorious** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 114 | **ripening** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 115 | **vajra** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 116 | **protectors** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 117 | **syllables** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 118 | **svāhā** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 119 | **yak** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 120 | **destroys** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 121 | **enemies** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 122 | **ornament** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 123 | **liberate** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 124 | **dwell** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 125 | **bliss** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 126 | **nectar** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 127 | **obscurations** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 128 | **lamp** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 129 | **lifespan** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 130 | **sentient** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 131 | **bestow** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 132 | **sacred** | 3 | 13,375.17 | 9.59 | 🟠 very high — domain-specific |
| 133 | **wheels** | 3 | 12,814.04 | 9.18767 | 🟠 very high — domain-specific |
| 134 | **constantly** | 3 | 12,814.04 | 9.18767 | 🟠 very high — domain-specific |
| 135 | **complete** | 5 | 12,687.05 | 5.457969 | 🟠 very high — domain-specific |
| 136 | **practice** | 4 | 12,626.27 | 6.789775 | 🟠 very high — domain-specific |
| 137 | **uphold** | 3 | 12,412.81 | 8.899988 | 🟠 very high — domain-specific |
| 138 | **stainless** | 3 | 12,412.81 | 8.899988 | 🟠 very high — domain-specific |
| 139 | **until** | 6 | 12,145.15 | 4.354037 | 🟠 very high — domain-specific |
| 140 | **wealth** | 3 | 12,101.60 | 8.676844 | 🟠 very high — domain-specific |
| 141 | **earth** | 3 | 11,847.31 | 8.494523 | 🟠 very high — domain-specific |
| 142 | **concentration** | 3 | 11,847.31 | 8.494523 | 🟠 very high — domain-specific |
| 143 | **lives** | 3 | 11,847.31 | 8.494523 | 🟠 very high — domain-specific |
| 144 | **let** | 4 | 11,745.22 | 6.31599 | 🟠 very high — domain-specific |
| 145 | **relief** | 4 | 11,745.22 | 6.31599 | 🟠 very high — domain-specific |
| 146 | **filled** | 3 | 11,632.32 | 8.340372 | 🟠 very high — domain-specific |
| 147 | **full** | 6 | 11,590.11 | 4.155056 | 🟠 very high — domain-specific |
| 148 | **short** | 5 | 11,525.82 | 4.958406 | 🟠 very high — domain-specific |
| 149 | **defeated** | 3 | 11,446.08 | 8.206841 | 🟠 very high — domain-specific |
| 150 | **death** | 3 | 11,446.08 | 8.206841 | 🟠 very high — domain-specific |
| 151 | **pure** | 3 | 11,281.81 | 8.089058 | 🟠 very high — domain-specific |
| 152 | **fears** | 4 | 11,254.63 | 6.052176 | 🟠 very high — domain-specific |
| 153 | **throughout** | 4 | 11,254.63 | 6.052176 | 🟠 very high — domain-specific |
| 154 | **sovereign** | 3 | 11,134.86 | 7.983697 | 🟠 very high — domain-specific |
| 155 | **faith** | 3 | 11,134.86 | 7.983697 | 🟠 very high — domain-specific |
| 156 | **fortune** | 3 | 11,134.86 | 7.983697 | 🟠 very high — domain-specific |
| 157 | **bow** | 3 | 11,001.93 | 7.888387 | 🟠 very high — domain-specific |
| 158 | **causes** | 3 | 11,001.93 | 7.888387 | 🟠 very high — domain-specific |
| 159 | **ordinary** | 4 | 10,933.64 | 5.879563 | 🟠 very high — domain-specific |
| 160 | **time** | 6 | 10,717.30 | 3.842151 | 🟠 very high — domain-specific |
| 161 | **victory** | 3 | 10,665.59 | 7.647225 | 🟠 very high — domain-specific |
| 162 | **others** | 4 | 10,509.63 | 5.651553 | 🟠 very high — domain-specific |
| 163 | **activity** | 4 | 10,337.32 | 5.558895 | 🟠 very high — domain-specific |
| 164 | **head** | 4 | 10,149.64 | 5.457969 | 🟠 very high — domain-specific |
| 165 | **forms** | 3 | 10,035.20 | 7.19524 | 🟠 very high — domain-specific |
| 166 | **thousand** | 3 | 9,973.20 | 7.150788 | 🟡 high — specialist register |
| 167 | **crown** | 3 | 9,856.91 | 7.067407 | 🟡 high — specialist register |
| 168 | **golden** | 3 | 9,802.21 | 7.028186 | 🟡 high — specialist register |
| 169 | **free** | 4 | 9,577.84 | 5.150484 | 🟡 high — specialist register |
| 170 | **form** | 4 | 9,566.93 | 5.144619 | 🟡 high — specialist register |
| 171 | **fall** | 5 | 9,360.07 | 4.026701 | 🟡 high — specialist register |
| 172 | **become** | 4 | 9,284.94 | 4.992978 | 🟡 high — specialist register |
| 173 | **spread** | 3 | 9,201.40 | 6.597403 | 🟡 high — specialist register |
| 174 | **rain** | 3 | 9,100.53 | 6.525082 | 🟡 high — specialist register |
| 175 | **hold** | 4 | 9,081.55 | 4.883605 | 🟡 high — specialist register |
| 176 | **fire** | 3 | 9,006.47 | 6.457641 | 🟡 high — specialist register |
| 177 | **born** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 178 | **dawn** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 179 | **friend** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 180 | **praise** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 181 | **authoritative** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 182 | **renunciation** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 183 | **intensely** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 184 | **garland** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 185 | **thoughts** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 186 | **saffron** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 187 | **sixteen** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 188 | **continuity** | 2 | 8,919.70 | 9.593135 | 🟡 high — specialist register |
| 189 | **hand** | 3 | 8,918.36 | 6.394462 | 🟡 high — specialist register |
| 190 | **fear** | 3 | 8,918.36 | 6.394462 | 🟡 high — specialist register |
| 191 | **obstruct** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 192 | **generosity** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 193 | **perfections** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 194 | **non-buddhist** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 195 | **extremists** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 196 | **terrified** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 197 | **teaching** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 198 | **kinsman** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 199 | **scriptural** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 200 | **craving** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 201 | **countless** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 202 | **deeds** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 203 | **maitreya** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 204 | **brilliance** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 205 | **lineage** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 206 | **bhagavatī** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 207 | **ḍākinīs** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 208 | **tsal** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 209 | **gurus** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 210 | **twofold** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 211 | **namo** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 212 | **tāre** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 213 | **heroic** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 214 | **dispels** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 215 | **brilliant** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 216 | **beautifully** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 217 | **sphere** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 218 | **perfection** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 219 | **trampling** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 220 | **summon** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 221 | **zombies** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 222 | **shatter** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 223 | **guardians** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 224 | **frown** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 225 | **wrathful** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 226 | **virtuous** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 227 | **reciting** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 228 | **majesty** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 229 | **dreams** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 230 | **avalokite** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 231 | **vara** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 232 | **pacify** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 233 | **conceptual** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 234 | **robes** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 235 | **sever** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 236 | **mothers** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 237 | **afflictions** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 238 | **birth** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 239 | **mandala** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 240 | **awakening** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 241 | **beginningless** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 242 | **sublime** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 243 | **delight** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 244 | **virtues** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 245 | **longevity** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 246 | **ornaments** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 247 | **splendor** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 248 | **tame** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 249 | **excellence** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 250 | **expanse** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 251 | **beautiful** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 252 | **masters** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 253 | **sūtra** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 254 | **lineages** | 2 | 8,916.78 | 9.59 | 🟡 high — specialist register |
| 255 | **body** | 3 | 8,835.48 | 6.335039 | 🟡 high — specialist register |
| 256 | **since** | 5 | 8,732.83 | 3.756864 | 🟡 high — specialist register |
| 257 | **therefore** | 3 | 8,683.18 | 6.225839 | 🟡 high — specialist register |
| 258 | **intention** | 3 | 8,567.85 | 6.143148 | 🟡 high — specialist register |
| 259 | **patience** | 2 | 8,542.70 | 9.18767 | 🟡 high — specialist register |
| 260 | **strife** | 2 | 8,542.70 | 9.18767 | 🟡 high — specialist register |
| 261 | **inconceivable** | 2 | 8,542.70 | 9.18767 | 🟡 high — specialist register |
| 262 | **festival** | 2 | 8,542.70 | 9.18767 | 🟡 high — specialist register |
| 263 | **lords** | 2 | 8,542.70 | 9.18767 | 🟡 high — specialist register |
| 264 | **speech** | 3 | 8,343.40 | 5.982217 | 🟡 high — specialist register |
| 265 | **truly** | 2 | 8,275.21 | 8.899988 | 🟡 high — specialist register |
| 266 | **leg** | 2 | 8,275.21 | 8.899988 | 🟡 high — specialist register |
| 267 | **love** | 2 | 8,275.21 | 8.899988 | 🟡 high — specialist register |
| 268 | **accumulations** | 2 | 8,275.21 | 8.899988 | 🟡 high — specialist register |
| 269 | **prosperity** | 2 | 8,275.21 | 8.899988 | 🟡 high — specialist register |
| 270 | **protect** | 3 | 8,269.98 | 5.929574 | 🟡 high — specialist register |
| 271 | **land** | 3 | 8,150.11 | 5.843631 | 🟡 high — specialist register |
| 272 | **surrounded** | 2 | 8,067.73 | 8.676844 | 🟡 high — specialist register |
| 273 | **destroy** | 2 | 8,067.73 | 8.676844 | 🟡 high — specialist register |
| 274 | **vows** | 2 | 7,898.21 | 8.494523 | 🟡 high — specialist register |
| 275 | **times** | 3 | 7,816.11 | 5.604151 | 🟡 high — specialist register |
| 276 | **enjoy** | 2 | 7,754.88 | 8.340372 | 🟡 high — specialist register |
| 277 | **rest** | 3 | 7,740.70 | 5.550084 | 🟡 high — specialist register |
| 278 | **cause** | 3 | 7,646.11 | 5.482261 | 🟡 high — specialist register |
| 279 | **swiftly** | 2 | 7,630.72 | 8.206841 | 🟡 high — specialist register |
| 280 | **weapons** | 2 | 7,630.72 | 8.206841 | 🟡 high — specialist register |
| 281 | **fruits** | 2 | 7,630.72 | 8.206841 | 🟡 high — specialist register |
| 282 | **extended** | 3 | 7,557.53 | 5.418748 | 🟡 high — specialist register |
| 283 | **tree** | 2 | 7,521.21 | 8.089058 | 🟡 high — specialist register |
| 284 | **learned** | 2 | 7,521.21 | 8.089058 | 🟡 high — specialist register |
| 285 | **reach** | 3 | 7,464.17 | 5.351808 | 🟡 high — specialist register |
| 286 | **attain** | 2 | 7,423.24 | 7.983697 | 🟡 high — specialist register |
| 287 | **diminish** | 2 | 7,423.24 | 7.983697 | 🟡 high — specialist register |
| 288 | **banner** | 2 | 7,423.24 | 7.983697 | 🟡 high — specialist register |
| 289 | **bring** | 3 | 7,414.88 | 5.316469 | 🟡 high — specialist register |
| 290 | **root** | 2 | 7,334.62 | 7.888387 | 🟡 high — specialist register |
| 291 | **human** | 2 | 7,334.62 | 7.888387 | 🟡 high — specialist register |
| 292 | **eye** | 2 | 7,334.62 | 7.888387 | 🟡 high — specialist register |
| 293 | **world** | 4 | 7,257.60 | 3.902776 | 🟡 high — specialist register |
| 294 | **path** | 2 | 7,253.72 | 7.801376 | 🟡 high — specialist register |
| 295 | **discipline** | 2 | 7,179.30 | 7.721333 | 🟡 high — specialist register |
| 296 | **right** | 3 | 7,175.20 | 5.144619 | 🟡 high — specialist register |
| 297 | **seeing** | 2 | 7,110.39 | 7.647225 | 🟡 high — specialist register |
| 298 | **offerings** | 2 | 7,110.39 | 7.647225 | 🟡 high — specialist register |
| 299 | **obstacles** | 2 | 7,110.39 | 7.647225 | 🟡 high — specialist register |
| 300 | **mass** | 2 | 7,046.24 | 7.578232 | 🟡 high — specialist register |
| 301 | **engage** | 2 | 6,986.23 | 7.513694 | 🟡 high — specialist register |
| 302 | **names** | 2 | 6,986.23 | 7.513694 | 🟡 high — specialist register |
| 303 | **diligence** | 2 | 6,929.86 | 7.453069 | 🟡 high — specialist register |
| 304 | **grace** | 2 | 6,929.86 | 7.453069 | 🟡 high — specialist register |
| 305 | **arising** | 2 | 6,876.72 | 7.395911 | 🟡 high — specialist register |
| 306 | **lead** | 3 | 6,855.85 | 4.915644 | 🟡 high — specialist register |
| 307 | **fruit** | 2 | 6,826.45 | 7.341843 | 🟡 high — specialist register |
| 308 | **grants** | 2 | 6,826.45 | 7.341843 | 🟡 high — specialist register |
| 309 | **powerful** | 2 | 6,778.75 | 7.29055 | 🟡 high — specialist register |
| 310 | **because** | 4 | 6,695.34 | 3.600421 | 🟡 high — specialist register |
| 311 | **whatever** | 2 | 6,609.23 | 7.108229 | 🟡 high — specialist register |
| 312 | **conditions** | 3 | 6,601.57 | 4.733323 | 🟡 high — specialist register |
| 313 | **conduct** | 2 | 6,571.28 | 7.067407 | 🟡 high — specialist register |
| 314 | **accumulated** | 2 | 6,534.81 | 7.028186 | 🟡 high — specialist register |
| 315 | **nature** | 2 | 6,534.81 | 7.028186 | 🟡 high — specialist register |
| 316 | **abandoned** | 2 | 6,465.90 | 6.954078 | 🟡 high — specialist register |
| 317 | **excellent** | 2 | 6,371.26 | 6.852295 | 🟡 high — specialist register |
| 318 | **decline** | 3 | 6,332.05 | 4.540079 | 🟡 high — specialist register |
| 319 | **desire** | 2 | 6,313.13 | 6.789775 | 🟡 high — specialist register |
| 320 | **play** | 2 | 6,313.13 | 6.789775 | 🟡 high — specialist register |
| 321 | **restore** | 2 | 6,313.13 | 6.789775 | 🟡 high — specialist register |
| 322 | **autumn** | 2 | 6,285.38 | 6.759922 | 🟡 high — specialist register |
| 323 | **vessel** | 2 | 6,285.38 | 6.759922 | 🟡 high — specialist register |
| 324 | **holder** | 2 | 6,258.42 | 6.730934 | 🟡 high — specialist register |
| 325 | **under** | 4 | 6,229.55 | 3.34994 | 🟡 high — specialist register |
| 326 | **realized** | 2 | 6,206.75 | 6.675364 | 🟡 high — specialist register |
| 327 | **respect** | 2 | 6,157.81 | 6.622721 | 🟡 high — specialist register |
| 328 | **twice** | 2 | 6,134.27 | 6.597403 | 🟡 high — specialist register |
| 329 | **ever** | 2 | 6,111.31 | 6.57271 | 🟡 high — specialist register |
| 330 | **regarding** | 2 | 6,067.02 | 6.525082 | 🟡 high — specialist register |
| 331 | **sun** | 2 | 6,045.65 | 6.502093 | 🟡 high — specialist register |
| 332 | **state** | 3 | 5,965.79 | 4.277469 | 🟡 high — specialist register |
| 333 | **kind** | 2 | 5,890.32 | 6.335039 | 🟡 high — specialist register |
| 334 | **never** | 2 | 5,872.61 | 6.31599 | 🟡 high — specialist register |
| 335 | **established** | 2 | 5,757.26 | 6.191938 | 🟡 high — specialist register |
| 336 | **most** | 3 | 5,689.97 | 4.079706 | 🟡 high — specialist register |
| 337 | **declining** | 2 | 5,668.65 | 6.096628 | 🟡 high — specialist register |
| 338 | **make** | 3 | 5,629.44 | 4.036307 | 🟡 high — specialist register |
| 339 | **particular** | 2 | 5,613.93 | 6.037787 | 🟡 high — specialist register |
| 340 | **single** | 2 | 5,587.74 | 6.009616 | 🟡 high — specialist register |
| 341 | **take** | 3 | 5,459.79 | 3.914671 | 🟡 high — specialist register |
| 342 | **away** | 2 | 5,401.16 | 5.808946 | 🟡 high — specialist register |
| 343 | **signs** | 2 | 5,339.83 | 5.742988 | 🟡 high — specialist register |
| 344 | **benefits** | 2 | 5,329.99 | 5.732405 | 🟡 high — specialist register |
| 345 | **night** | 2 | 5,329.99 | 5.732405 | 🟡 high — specialist register |
| 346 | **especially** | 2 | 5,329.99 | 5.732405 | 🟡 high — specialist register |
| 347 | **look** | 2 | 5,291.64 | 5.691163 | 🟡 high — specialist register |
| 348 | **activities** | 2 | 5,273.05 | 5.671162 | 🟡 high — specialist register |
| 349 | **source** | 2 | 5,219.39 | 5.613454 | 🟡 high — specialist register |
| 350 | **face** | 2 | 5,202.17 | 5.594934 | 🟡 high — specialist register |
| 351 | **clear** | 2 | 5,168.66 | 5.558895 | 🟡 high — specialist register |
| 352 | **end** | 3 | 5,143.34 | 3.687773 | 🟡 high — specialist register |
| 353 | **entered** | 2 | 5,136.32 | 5.524108 | 🟡 high — specialist register |
| 354 | **fully** | 2 | 5,128.40 | 5.515598 | 🟡 high — specialist register |
| 355 | **left** | 2 | 5,097.41 | 5.482261 | 🟡 high — specialist register |
| 356 | **food** | 2 | 4,690.41 | 5.044535 | 🟡 high — specialist register |
| 357 | **trust** | 2 | 4,610.33 | 4.958406 | 🟡 high — specialist register |
| 358 | **come** | 2 | 4,557.68 | 4.901787 | 🟡 high — specialist register |
| 359 | **gold** | 2 | 4,524.17 | 4.865747 | 🟡 high — specialist register |
| 360 | **sky** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 361 | **subduing** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 362 | **miraculous** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 363 | **displays** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 364 | **perfected** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 365 | **anxiety** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 366 | **rendered** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 367 | **teachers** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 368 | **sacrificed** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 369 | **hair** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 370 | **phenomena** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 371 | **roots** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 372 | **dedicate** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 373 | **momentary** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 374 | **flash** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 375 | **stars** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 376 | **palms** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 377 | **utterly** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 378 | **stamp** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 379 | **meru** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 380 | **contagious** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 381 | **loving** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 382 | **nurse** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 383 | **famine** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 384 | **miserable** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 385 | **evil** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 386 | **cultivate** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 387 | **courage** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 388 | **wander** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 389 | **teach** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 390 | **purified** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 391 | **condensing** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 392 | **myself** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 393 | **truth** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 394 | **dense** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 395 | **flames** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 396 | **enduring** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 397 | **finger** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 398 | **secrets** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 399 | **distress** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 400 | **maturation** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 401 | **auspicious** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 402 | **emerald** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 403 | **attainment** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 404 | **parted** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 405 | **flower** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 406 | **successors** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 407 | **ati** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 408 | **lama** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 409 | **invoke** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 410 | **rampant** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 411 | **dregs** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 412 | **indifferent** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 413 | **manifest** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 414 | **lit** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 415 | **misfortune** | 1 | 4,459.85 | 9.593135 | 🟡 high — specialist register |
| 416 | **dharmamitra** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 417 | **zero-shot** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 418 | **bodhi** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 419 | **pervaded** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 420 | **rained** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 421 | **shower** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 422 | **vajras** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 423 | **spears** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 424 | **snow-peaks** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 425 | **flower-arrows** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 426 | **strove** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 427 | **loving-kindness** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 428 | **buddhahood** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 429 | **trembled** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 430 | **ethical** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 431 | **culmination** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 432 | **rejoiced** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 433 | **possesses** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 434 | **unerring** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 435 | **lion** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 436 | **roar** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 437 | **proclaimed** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 438 | **speechless** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 439 | **foxes** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 440 | **sages** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 441 | **apāda** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 442 | **vālmīki** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 443 | **vyāsa** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 444 | **ne-jok** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 445 | **renown** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 446 | **cared** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 447 | **liberated** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 448 | **disciples** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 449 | **hearers** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 450 | **prophecies** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 451 | **aspiring** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 452 | **disciple** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 453 | **āradvatīputra** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 454 | **ākya** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 455 | **vāku** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 456 | **bhagavan** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 457 | **omniscience** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 458 | **dharmakāya** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 459 | **prajñāpāramitā** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 460 | **samantabhadrī** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 461 | **sambhogakāya** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 462 | **vajravārāhī** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 463 | **emanation-display** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 464 | **venerable** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 465 | **padmākara** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 466 | **bodhisattva** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 467 | **rolpa** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 468 | **chokgyur** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 469 | **dechen** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 470 | **lingpa** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 471 | **treasures** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 472 | **dorje** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 473 | **ziji** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 474 | **pema** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 475 | **garwang** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 476 | **goddess** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 477 | **moistened** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 478 | **sprouts** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 479 | **altruistic** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 480 | **lush** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 481 | **spontaneous** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 482 | **ārya-tārāye** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 483 | **confess** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 484 | **rejoice** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 485 | **exhort** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 486 | **liberatress** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 487 | **stamens** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 488 | **lotus-face** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 489 | **moons** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 490 | **water-born** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 491 | **tathāgatas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 492 | **tuttāra** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 493 | **hūṃ** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 494 | **fills** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 495 | **indra** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 496 | **agni** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 497 | **vāyu** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 498 | **varas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 499 | **worship** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 500 | **gandharvas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 501 | **traṭ** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 502 | **phaṭ** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 503 | **magical** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 504 | **adversaries** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 505 | **swirling** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 506 | **fearful** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 507 | **champions** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 508 | **mara** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 509 | **frowning** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 510 | **slays** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 511 | **mudrā** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 512 | **symbolizing** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 513 | **adorn** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 514 | **radiating** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 515 | **turbulent** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 516 | **majestic** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 517 | **garlands** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 518 | **laughter** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 519 | **vibrating** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 520 | **destitution** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 521 | **crescent** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 522 | **blazes** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 523 | **matted** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 524 | **amitābha** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 525 | **radiates** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 526 | **magnificent** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 527 | **eon** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 528 | **bent** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 529 | **armies** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 530 | **trample** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 531 | **blissful** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 532 | **nirvāṇa** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 533 | **negativity** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 534 | **shatters** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 535 | **ten-syllable** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 536 | **wisdom-tara** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 537 | **seed-syllable** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 538 | **mandara** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 539 | **vindhya** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 540 | **tremble** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 541 | **deer-marked** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 542 | **celestial** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 543 | **tāra** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 544 | **phat** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 545 | **kinnaras** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 546 | **hara** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 547 | **suchnesses** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 548 | **blooming** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 549 | **darkness** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 550 | **torment** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 551 | **tormented** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 552 | **wherever** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 553 | **sickness** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 554 | **afflict** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 555 | **sufferings** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 556 | **mire** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 557 | **misery** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 558 | **habitual** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 559 | **ripples** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 560 | **never-ending** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 561 | **boast** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 562 | **karmic** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 563 | **beast** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 564 | **impermanent** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 565 | **unaccomplished** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 566 | **noose** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 567 | **epidemics** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 568 | **poisons** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 569 | **habituated** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 570 | **self-grasping** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 571 | **lifetimes** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 572 | **spiritual** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 573 | **demonic** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 574 | **insight** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 575 | **mindfulness** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 576 | **mind-stream** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 577 | **cessation** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 578 | **bardo** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 579 | **fleeting** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 580 | **emanation** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 581 | **reabsorption** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 582 | **prophesy** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 583 | **oceans** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 584 | **holy** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 585 | **life-force** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 586 | **aspirations** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 587 | **misdeeds** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 588 | **downfalls** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 589 | **cleansed** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 590 | **siddhi** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 591 | **deathless** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 592 | **life-empowerment** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 593 | **distractions** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 594 | **worldly** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 595 | **ever-greater** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 596 | **ears** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 597 | **nāgas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 598 | **heaven** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 599 | **unhappiness** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 600 | **reverence** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 601 | **jewel** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 602 | **thickets** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 603 | **non-humans** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 604 | **untimely** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 605 | **perfects** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 606 | **deity** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 607 | **prayers** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 608 | **fruition** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 609 | **one-pointed** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 610 | **longing** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 611 | **youthful** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 612 | **vajra-bliss** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 613 | **rites** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 614 | **gift** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 615 | **anoint** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 616 | **thumb** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 617 | **lovely** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 618 | **blossomed** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 619 | **nets** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 620 | **pearls** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 621 | **bells** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 622 | **displaying** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 623 | **graceful** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 624 | **divine** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 625 | **molten** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 626 | **seated** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 627 | **indestructible** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 628 | **proclaiming** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 629 | **melody** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 630 | **uninterrupted** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 631 | **webs** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 632 | **throne** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 633 | **giver** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 634 | **bodhicitta** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 635 | **drolma** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 636 | **tormenting** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 637 | **protectress** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 638 | **remembers** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 639 | **misfortunes** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 640 | **embodiment** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 641 | **heartfelt** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 642 | **practicing** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 643 | **ārya** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 644 | **tārāye** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 645 | **churned** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 646 | **moon-like** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 647 | **respite** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 648 | **singular** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 649 | **lapis** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 650 | **lazuli** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 651 | **lute** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 652 | **melodic** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 653 | **radiance** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 654 | **dharma-heaps** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 655 | **heart-mind** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 656 | **non-dual** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 657 | **elaborations** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 658 | **boundless** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 659 | **sixty-four** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 660 | **inexhaustible** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 661 | **captivates** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 662 | **all-pervading** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 663 | **spontaneously** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 664 | **perfecting** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 665 | **supplication** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 666 | **wisdom-vision** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 667 | **liberates** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 668 | **captivated** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 669 | **single-pointed** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 670 | **particles** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 671 | **radiant** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 672 | **moods** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 673 | **smiles** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 674 | **mundane** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 675 | **supramundane** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 676 | **treasure** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 677 | **vidyā-mantra** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 678 | **supremely** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 679 | **partiality** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 680 | **dissolve** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 681 | **fourfold** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 682 | **indivisible** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 683 | **kāyas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 684 | **joyful** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 685 | **sidelong** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 686 | **glance** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 687 | **distinguished** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 688 | **fortunate** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 689 | **aeon** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 690 | **uḍumbara** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 691 | **realm** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 692 | **fulfiller** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 693 | **rāvakas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 694 | **pratyekabuddhas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 695 | **mañju** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 696 | **jambudvīpa** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 697 | **eighty-four** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 698 | **yoga** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 699 | **incomparably** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 700 | **padmasambhava** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 701 | **āntarak** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 702 | **trisong** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 703 | **detsen** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 704 | **vairotsana** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 705 | **sakya** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 706 | **patriarchs** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 707 | **marpa** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 708 | **milarepa** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 709 | **gampopa** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 710 | **tibetan** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 711 | **vidyādharas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 712 | **yidams** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 713 | **vinaya** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 714 | **abhidharma** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 715 | **tantras** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 716 | **pillars** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 717 | **chariots** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 718 | **behold** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 719 | **unfeigned** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 720 | **altruism** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 721 | **mantra-holders** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 722 | **samaya** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 723 | **drosses** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 724 | **shackles** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 725 | **jealousy** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 726 | **agitated** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 727 | **asuras** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 728 | **barbarians** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 729 | **abound** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 730 | **alas** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 731 | **sorrows** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 732 | **masteries** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 733 | **tibet** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 734 | **non-sectarian** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 735 | **throngs** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 736 | **aspire** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 737 | **sangha** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 738 | **pervade** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 739 | **drum** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 740 | **resound** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 741 | **loudly** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 742 | **shattering** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 743 | **skulls** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 744 | **heretical** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 745 | **elephants** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 746 | **patrons** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 747 | **demigods** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 748 | **bowing** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 749 | **captivating** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 750 | **flavors** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 751 | **wandering** | 1 | 4,458.39 | 9.59 | 🟡 high — specialist register |
| 752 | **name** | 2 | 4,311.77 | 4.637308 | 🟡 high — specialist register |
| 753 | **treasury** | 2 | 4,308.50 | 4.633793 | 🟡 high — specialist register |
| 754 | **many** | 2 | 4,282.76 | 4.60611 | 🟡 high — specialist register |
| 755 | **wise** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 756 | **regent** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 757 | **rays** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 758 | **transmissions** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 759 | **clarified** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 760 | **rows** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 761 | **accomplishment** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 762 | **amidst** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 763 | **fingers** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 764 | **midst** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 765 | **armor** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 766 | **tendencies** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 767 | **instant** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 768 | **accumulate** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 769 | **uproot** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 770 | **mistaken** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 771 | **dust** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 772 | **extremes** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 773 | **array** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 774 | **faults** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 775 | **harmony** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 776 | **heights** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 777 | **obstructing** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 778 | **engagement** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 779 | **trained** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 780 | **blessing** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 781 | **decay** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 782 | **painted** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 783 | **contention** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 784 | **strengths** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 785 | **disciplined** | 1 | 4,271.35 | 9.18767 | 🟡 high — specialist register |
| 786 | **within** | 2 | 4,251.56 | 4.57255 | 🟡 high — specialist register |
| 787 | **practiced** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 788 | **son** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 789 | **expression** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 790 | **locks** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 791 | **waves** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 792 | **prey** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 793 | **ignite** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 794 | **vigilance** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 795 | **blend** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 796 | **perceptions** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 797 | **forests** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 798 | **wilderness** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 799 | **humans** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 800 | **helm** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 801 | **pillar** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 802 | **touching** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 803 | **ring** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 804 | **pour** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 805 | **self** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 806 | **abundance** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 807 | **arises** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 808 | **emergence** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 809 | **awareness** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 810 | **abandonment** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 811 | **sage** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 812 | **snows** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 813 | **certainty** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 814 | **transformed** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 815 | **temples** | 1 | 4,137.60 | 8.899988 | 🟡 high — specialist register |
| 816 | **freed** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 817 | **speak** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 818 | **understands** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 819 | **violent** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 820 | **sword** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 821 | **exhausted** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 822 | **absent** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 823 | **accompany** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 824 | **tip** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 825 | **mere** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 826 | **wonder** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 827 | **flowers** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 828 | **assemblies** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 829 | **exert** | 1 | 4,033.87 | 8.676844 | 🟡 high — specialist register |
| 830 | **day** | 2 | 4,002.67 | 4.304868 | 🟡 high — specialist register |
| 831 | **firm** | 2 | 3,961.34 | 4.260416 | 🟡 high — specialist register |
| 832 | **mountains** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 833 | **overcome** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 834 | **preceded** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 835 | **experiencing** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 836 | **lands** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 837 | **fulfilling** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 838 | **posture** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 839 | **music** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 840 | **depths** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 841 | **grove** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 842 | **minds** | 1 | 3,949.10 | 8.494523 | 🟡 high — specialist register |
| 843 | **beneath** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 844 | **shrank** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 845 | **subdued** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 846 | **prince** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 847 | **abundant** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 848 | **lightning** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 849 | **diseases** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 850 | **medicine** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 851 | **accumulation** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 852 | **gateway** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 853 | **exchanging** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 854 | **naturally** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 855 | **wishes** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 856 | **backdrop** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 857 | **display** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 858 | **perform** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 859 | **beauty** | 1 | 3,877.44 | 8.340372 | 🟡 high — specialist register |
| 860 | **arose** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 861 | **acts** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 862 | **deeply** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 863 | **arisen** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 864 | **realization** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 865 | **merits** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 866 | **ita** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 867 | **genuine** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 868 | **generation** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 869 | **pollution** | 1 | 3,815.36 | 8.206841 | 🟡 high — specialist register |
| 870 | **fulfilled** | 1 | 3,760.60 | 8.089058 | 🟡 high — specialist register |
| 871 | **spreads** | 1 | 3,760.60 | 8.089058 | 🟡 high — specialist register |
| 872 | **remote** | 1 | 3,760.60 | 8.089058 | 🟡 high — specialist register |
| 873 | **hear** | 1 | 3,760.60 | 8.089058 | 🟡 high — specialist register |
| 874 | **burned** | 1 | 3,760.60 | 8.089058 | 🟡 high — specialist register |
| 875 | **steer** | 1 | 3,760.60 | 8.089058 | 🟡 high — specialist register |
| 876 | **object** | 1 | 3,760.60 | 8.089058 | 🟡 high — specialist register |
| 877 | **discouraged** | 1 | 3,760.60 | 8.089058 | 🟡 high — specialist register |
| 878 | **english** | 1 | 3,711.62 | 7.983697 | 🟡 high — specialist register |
| 879 | **blue** | 1 | 3,711.62 | 7.983697 | 🟡 high — specialist register |
| 880 | **unwanted** | 1 | 3,711.62 | 7.983697 | 🟡 high — specialist register |
| 881 | **harmful** | 1 | 3,711.62 | 7.983697 | 🟡 high — specialist register |
| 882 | **granting** | 1 | 3,711.62 | 7.983697 | 🟡 high — specialist register |
| 883 | **driven** | 1 | 3,711.62 | 7.983697 | 🟡 high — specialist register |
| 884 | **austerity** | 1 | 3,667.31 | 7.888387 | 🟡 high — specialist register |
| 885 | **recognize** | 1 | 3,667.31 | 7.888387 | 🟡 high — specialist register |
| 886 | **rescue** | 1 | 3,667.31 | 7.888387 | 🟡 high — specialist register |
| 887 | **mount** | 1 | 3,626.86 | 7.801376 | 🟡 high — specialist register |
| 888 | **meaningful** | 1 | 3,626.86 | 7.801376 | 🟡 high — specialist register |
| 889 | **sons** | 1 | 3,589.65 | 7.721333 | 🟡 high — specialist register |
| 890 | **relied** | 1 | 3,589.65 | 7.721333 | 🟡 high — specialist register |
| 891 | **intense** | 1 | 3,589.65 | 7.721333 | 🟡 high — specialist register |
| 892 | **sole** | 1 | 3,589.65 | 7.721333 | 🟡 high — specialist register |
| 893 | **reaches** | 1 | 3,589.65 | 7.721333 | 🟡 high — specialist register |
| 894 | **doors** | 1 | 3,589.65 | 7.721333 | 🟡 high — specialist register |
| 895 | **classes** | 1 | 3,589.65 | 7.721333 | 🟡 high — specialist register |
| 896 | **moreover** | 1 | 3,555.20 | 7.647225 | 🟡 high — specialist register |
| 897 | **spirits** | 1 | 3,555.20 | 7.647225 | 🟡 high — specialist register |
| 898 | **words** | 1 | 3,555.20 | 7.647225 | 🟡 high — specialist register |
| 899 | **furthermore** | 1 | 3,555.20 | 7.647225 | 🟡 high — specialist register |
| 900 | **extreme** | 1 | 3,555.20 | 7.647225 | 🟡 high — specialist register |
| 901 | **down** | 2 | 3,550.52 | 3.818584 | 🟡 high — specialist register |
| 902 | **ones** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 903 | **bodies** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 904 | **poison** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 905 | **pull** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 906 | **aggregates** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 907 | **training** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 908 | **guide** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 909 | **fulfill** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 910 | **wind** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 911 | **undermine** | 1 | 3,523.12 | 7.578232 | 🟡 high — specialist register |
| 912 | **bearing** | 1 | 3,493.12 | 7.513694 | 🟡 high — specialist register |
| 913 | **surface** | 1 | 3,493.12 | 7.513694 | 🟡 high — specialist register |
| 914 | **firmly** | 1 | 3,493.12 | 7.513694 | 🟡 high — specialist register |
| 915 | **stream** | 1 | 3,493.12 | 7.513694 | 🟡 high — specialist register |
| 916 | **meaning** | 1 | 3,493.12 | 7.513694 | 🟡 high — specialist register |
| 917 | **channel** | 1 | 3,493.12 | 7.513694 | 🟡 high — specialist register |
| 918 | **exist** | 1 | 3,464.93 | 7.453069 | 🟡 high — specialist register |
| 919 | **seed** | 1 | 3,464.93 | 7.453069 | 🟡 high — specialist register |
| 920 | **sudden** | 1 | 3,464.93 | 7.453069 | 🟡 high — specialist register |
| 921 | **heat** | 1 | 3,464.93 | 7.453069 | 🟡 high — specialist register |
| 922 | **stages** | 1 | 3,464.93 | 7.453069 | 🟡 high — specialist register |
| 923 | **bound** | 1 | 3,464.93 | 7.453069 | 🟡 high — specialist register |
| 924 | **constant** | 1 | 3,438.36 | 7.395911 | 🟡 high — specialist register |
| 925 | **understand** | 1 | 3,413.22 | 7.341843 | 🟡 high — specialist register |
| 926 | **merely** | 1 | 3,413.22 | 7.341843 | 🟡 high — specialist register |
| 927 | **millions** | 1 | 3,413.22 | 7.341843 | 🟡 high — specialist register |
| 928 | **elders** | 1 | 3,413.22 | 7.341843 | 🟡 high — specialist register |
| 929 | **universal** | 1 | 3,366.69 | 7.24176 | 🟡 high — specialist register |
| 930 | **harm** | 1 | 3,366.69 | 7.24176 | 🟡 high — specialist register |
| 931 | **continuous** | 1 | 3,345.07 | 7.19524 | 🟡 high — specialist register |
| 932 | **door** | 1 | 3,324.40 | 7.150788 | 🟡 high — specialist register |
| 933 | **introduce** | 1 | 3,324.40 | 7.150788 | 🟡 high — specialist register |
| 934 | **served** | 1 | 3,304.62 | 7.108229 | 🟡 high — specialist register |
| 935 | **foundation** | 1 | 3,304.62 | 7.108229 | 🟡 high — specialist register |
| 936 | **spirit** | 1 | 3,285.64 | 7.067407 | 🟡 high — specialist register |
| 937 | **stem** | 1 | 3,285.64 | 7.067407 | 🟡 high — specialist register |
| 938 | **intelligence** | 1 | 3,285.64 | 7.067407 | 🟡 high — specialist register |
| 939 | **arranged** | 1 | 3,267.40 | 7.028186 | 🟡 high — specialist register |
| 940 | **repeatedly** | 1 | 3,267.40 | 7.028186 | 🟡 high — specialist register |
| 941 | **finally** | 1 | 3,267.40 | 7.028186 | 🟡 high — specialist register |
| 942 | **essential** | 1 | 3,249.86 | 6.990446 | 🟡 high — specialist register |
| 943 | **ultimately** | 1 | 3,249.86 | 6.990446 | 🟡 high — specialist register |
| 944 | **physical** | 1 | 3,232.95 | 6.954078 | 🟡 high — specialist register |
| 945 | **generated** | 1 | 3,216.64 | 6.918987 | 🟡 high — specialist register |
| 946 | **drawn** | 1 | 3,216.64 | 6.918987 | 🟡 high — specialist register |
| 947 | **brief** | 1 | 3,216.64 | 6.918987 | 🟡 high — specialist register |
| 948 | **branches** | 1 | 3,185.63 | 6.852295 | 🟡 high — specialist register |
| 949 | **momentum** | 1 | 3,170.87 | 6.820546 | 🟡 high — specialist register |
| 950 | **destroyed** | 1 | 3,170.87 | 6.820546 | 🟡 high — specialist register |
| 951 | **experience** | 1 | 3,156.57 | 6.789775 | 🟡 high — specialist register |
| 952 | **withdrawn** | 1 | 3,156.57 | 6.789775 | 🟡 high — specialist register |
| 953 | **gradually** | 1 | 3,142.69 | 6.759922 | 🟡 high — specialist register |
| 954 | **powers** | 1 | 3,142.69 | 6.759922 | 🟡 high — specialist register |
| 955 | **reaching** | 1 | 3,142.69 | 6.759922 | 🟡 high — specialist register |
| 956 | **works** | 1 | 3,129.21 | 6.730934 | 🟡 high — specialist register |
| 957 | **finding** | 1 | 3,129.21 | 6.730934 | 🟡 high — specialist register |
| 958 | **aims** | 1 | 3,129.21 | 6.730934 | 🟡 high — specialist register |
| 959 | **purpose** | 1 | 3,116.11 | 6.702763 | 🟡 high — specialist register |
| 960 | **adverse** | 1 | 3,116.11 | 6.702763 | 🟡 high — specialist register |
| 961 | **indian** | 1 | 3,116.11 | 6.702763 | 🟡 high — specialist register |
| 962 | **settle** | 1 | 3,103.38 | 6.675364 | 🟡 high — specialist register |
| 963 | **favorable** | 1 | 3,103.38 | 6.675364 | 🟡 high — specialist register |
| 964 | **views** | 1 | 3,103.38 | 6.675364 | 🟡 high — specialist register |
| 965 | **lake** | 1 | 3,090.98 | 6.648696 | 🟡 high — specialist register |
| 966 | **bear** | 1 | 3,090.98 | 6.648696 | 🟡 high — specialist register |
| 967 | **doubt** | 1 | 3,078.90 | 6.622721 | 🟡 high — specialist register |
| 968 | **living** | 1 | 3,078.90 | 6.622721 | 🟡 high — specialist register |
| 969 | **presence** | 1 | 3,078.90 | 6.622721 | 🟡 high — specialist register |
| 970 | **slight** | 1 | 3,055.65 | 6.57271 | 🟡 high — specialist register |
| 971 | **million** | 1 | 3,055.65 | 6.57271 | 🟡 high — specialist register |
| 972 | **always** | 1 | 3,033.51 | 6.525082 | 🟡 high — specialist register |
| 973 | **arrangement** | 1 | 3,022.82 | 6.502093 | 🟡 high — specialist register |
| 974 | **appear** | 1 | 2,992.16 | 6.436135 | 🟢 medium — moderately distinctive |
| 975 | **red** | 1 | 2,992.16 | 6.436135 | 🟢 medium — moderately distinctive |
| 976 | **depend** | 1 | 2,982.37 | 6.415081 | 🟢 medium — moderately distinctive |
| 977 | **crowns** | 1 | 2,954.19 | 6.354457 | 🟢 medium — moderately distinctive |
| 978 | **care** | 1 | 2,945.16 | 6.335039 | 🟢 medium — moderately distinctive |
| 979 | **alone** | 1 | 2,945.16 | 6.335039 | 🟢 medium — moderately distinctive |
| 980 | **except** | 1 | 2,927.61 | 6.297298 | 🟢 medium — moderately distinctive |
| 981 | **concerns** | 1 | 2,927.61 | 6.297298 | 🟢 medium — moderately distinctive |
| 982 | **center** | 1 | 2,927.61 | 6.297298 | 🟢 medium — moderately distinctive |
| 983 | **ranges** | 1 | 2,919.08 | 6.278949 | 🟢 medium — moderately distinctive |
| 984 | **palm** | 1 | 2,919.08 | 6.278949 | 🟢 medium — moderately distinctive |
| 985 | **hearing** | 1 | 2,910.71 | 6.260931 | 🟢 medium — moderately distinctive |
| 986 | **hostile** | 1 | 2,910.71 | 6.260931 | 🟢 medium — moderately distinctive |
| 987 | **status** | 1 | 2,902.48 | 6.243231 | 🟢 medium — moderately distinctive |
| 988 | **circumstances** | 1 | 2,894.39 | 6.225839 | 🟢 medium — moderately distinctive |
| 989 | **why** | 1 | 2,894.39 | 6.225839 | 🟢 medium — moderately distinctive |
| 990 | **stand** | 1 | 2,886.45 | 6.208745 | 🟢 medium — moderately distinctive |
| 991 | **river** | 1 | 2,886.45 | 6.208745 | 🟢 medium — moderately distinctive |
| 992 | **side** | 1 | 2,886.45 | 6.208745 | 🟢 medium — moderately distinctive |
| 993 | **application** | 1 | 2,870.95 | 6.175409 | 🟢 medium — moderately distinctive |
| 994 | **bad** | 1 | 2,870.95 | 6.175409 | 🟢 medium — moderately distinctive |
| 995 | **fallen** | 1 | 2,870.95 | 6.175409 | 🟢 medium — moderately distinctive |
| 996 | **enter** | 1 | 2,863.39 | 6.159148 | 🟢 medium — moderately distinctive |
| 997 | **direction** | 1 | 2,848.63 | 6.127399 | 🟢 medium — moderately distinctive |
| 998 | **forces** | 1 | 2,841.42 | 6.111895 | 🟢 medium — moderately distinctive |
| 999 | **india** | 1 | 2,841.42 | 6.111895 | 🟢 medium — moderately distinctive |
| 1000 | **turn** | 1 | 2,834.32 | 6.096628 | 🟢 medium — moderately distinctive |
| 1001 | **placed** | 1 | 2,827.33 | 6.08159 | 🟢 medium — moderately distinctive |
| 1002 | **resolve** | 1 | 2,827.33 | 6.08159 | 🟢 medium — moderately distinctive |
| 1003 | **developed** | 1 | 2,820.44 | 6.066775 | 🟢 medium — moderately distinctive |
| 1004 | **royal** | 1 | 2,813.66 | 6.052176 | 🟢 medium — moderately distinctive |
| 1005 | **brings** | 1 | 2,813.66 | 6.052176 | 🟢 medium — moderately distinctive |
| 1006 | **possibly** | 1 | 2,806.97 | 6.037787 | 🟢 medium — moderately distinctive |
| 1007 | **appears** | 1 | 2,806.97 | 6.037787 | 🟢 medium — moderately distinctive |
| 1008 | **original** | 1 | 2,806.97 | 6.037787 | 🟢 medium — moderately distinctive |
| 1009 | **effects** | 1 | 2,800.37 | 6.023602 | 🟢 medium — moderately distinctive |
| 1010 | **thought** | 1 | 2,800.37 | 6.023602 | 🟢 medium — moderately distinctive |
| 1011 | **upward** | 1 | 2,793.87 | 6.009616 | 🟢 medium — moderately distinctive |
| 1012 | **newly** | 1 | 2,793.87 | 6.009616 | 🟢 medium — moderately distinctive |
| 1013 | **nothing** | 1 | 2,793.87 | 6.009616 | 🟢 medium — moderately distinctive |
| 1014 | **water** | 1 | 2,781.13 | 5.982217 | 🟢 medium — moderately distinctive |
| 1015 | **intended** | 1 | 2,768.74 | 5.955549 | 🟢 medium — moderately distinctive |
| 1016 | **toward** | 1 | 2,756.66 | 5.929574 | 🟢 medium — moderately distinctive |
| 1017 | **entire** | 1 | 2,756.66 | 5.929574 | 🟢 medium — moderately distinctive |
| 1018 | **hopes** | 1 | 2,733.41 | 5.879563 | 🟢 medium — moderately distinctive |
| 1019 | **once** | 1 | 2,727.77 | 5.867442 | 🟢 medium — moderately distinctive |
| 1020 | **forward** | 1 | 2,711.27 | 5.831935 | 🟢 medium — moderately distinctive |
| 1021 | **quickly** | 1 | 2,705.89 | 5.820374 | 🟢 medium — moderately distinctive |
| 1022 | **actions** | 1 | 2,700.58 | 5.808946 | 🟢 medium — moderately distinctive |
| 1023 | **ways** | 1 | 2,695.33 | 5.797646 | 🟢 medium — moderately distinctive |
| 1024 | **field** | 1 | 2,645.82 | 5.691163 | 🟢 medium — moderately distinctive |
| 1025 | **opening** | 1 | 2,636.52 | 5.671162 | 🟢 medium — moderately distinctive |
| 1026 | **basic** | 1 | 2,636.52 | 5.671162 | 🟢 medium — moderately distinctive |
| 1027 | **together** | 1 | 2,631.94 | 5.66131 | 🟢 medium — moderately distinctive |
| 1028 | **grow** | 1 | 2,627.41 | 5.651553 | 🟢 medium — moderately distinctive |
| 1029 | **various** | 1 | 2,614.06 | 5.622843 | 🟢 medium — moderately distinctive |
| 1030 | **flow** | 1 | 2,605.37 | 5.604151 | 🟢 medium — moderately distinctive |
| 1031 | **formed** | 1 | 2,601.09 | 5.594934 | 🟢 medium — moderately distinctive |
| 1032 | **strike** | 1 | 2,592.63 | 5.576752 | 🟢 medium — moderately distinctive |
| 1033 | **along** | 1 | 2,592.63 | 5.576752 | 🟢 medium — moderately distinctive |
| 1034 | **completion** | 1 | 2,592.63 | 5.576752 | 🟢 medium — moderately distinctive |
| 1035 | **opened** | 1 | 2,588.46 | 5.567784 | 🟢 medium — moderately distinctive |
| 1036 | **needs** | 1 | 2,576.17 | 5.54135 | 🟢 medium — moderately distinctive |
| 1037 | **study** | 1 | 2,556.39 | 5.498791 | 🟢 medium — moderately distinctive |
| 1038 | **definitive** | 1 | 2,526.38 | 5.434252 | 🟢 medium — moderately distinctive |
| 1039 | **took** | 1 | 2,526.38 | 5.434252 | 🟢 medium — moderately distinctive |
| 1040 | **city** | 1 | 2,522.77 | 5.42647 | 🟢 medium — moderately distinctive |
| 1041 | **prepared** | 1 | 2,519.18 | 5.418748 | 🟢 medium — moderately distinctive |
| 1042 | **view** | 1 | 2,505.09 | 5.388443 | 🟢 medium — moderately distinctive |
| 1043 | **difficult** | 1 | 2,494.79 | 5.366301 | 🟢 medium — moderately distinctive |
| 1044 | **act** | 1 | 2,478.13 | 5.330455 | 🟢 medium — moderately distinctive |
| 1045 | **remains** | 1 | 2,474.87 | 5.323438 | 🟢 medium — moderately distinctive |
| 1046 | **maintain** | 1 | 2,474.87 | 5.323438 | 🟢 medium — moderately distinctive |
| 1047 | **able** | 1 | 2,458.89 | 5.28907 | 🟢 medium — moderately distinctive |
| 1048 | **similar** | 1 | 2,431.44 | 5.230037 | 🟢 medium — moderately distinctive |
| 1049 | **makes** | 1 | 2,422.64 | 5.211109 | 🟢 medium — moderately distinctive |
| 1050 | **force** | 1 | 2,414.01 | 5.192532 | 🟢 medium — moderately distinctive |
| 1051 | **local** | 1 | 2,405.53 | 5.174295 | 🟢 medium — moderately distinctive |
| 1052 | **marks** | 1 | 2,394.46 | 5.150484 | 🟢 medium — moderately distinctive |
| 1053 | **taking** | 1 | 2,383.65 | 5.127227 | 🟢 medium — moderately distinctive |
| 1054 | **again** | 1 | 2,355.15 | 5.065927 | 🟢 medium — moderately distinctive |
| 1055 | **gave** | 1 | 2,323.58 | 4.998015 | 🟢 medium — moderately distinctive |
| 1056 | **small** | 1 | 2,309.70 | 4.968162 | 🟢 medium — moderately distinctive |
| 1057 | **holders** | 1 | 2,300.67 | 4.948744 | 🟢 medium — moderately distinctive |
| 1058 | **base** | 1 | 2,280.98 | 4.906385 | 🟢 medium — moderately distinctive |
| 1059 | **term** | 1 | 2,274.60 | 4.892655 | 🟢 medium — moderately distinctive |
| 1060 | **offered** | 1 | 2,232.21 | 4.801485 | 🟢 medium — moderately distinctive |
| 1061 | **rising** | 1 | 2,228.37 | 4.793221 | 🟢 medium — moderately distinctive |
| 1062 | **reduced** | 1 | 2,228.37 | 4.793221 | 🟢 medium — moderately distinctive |
| 1063 | **meet** | 1 | 2,226.46 | 4.789114 | 🟢 medium — moderately distinctive |
| 1064 | **work** | 1 | 2,224.56 | 4.785024 | 🟢 medium — moderately distinctive |
| 1065 | **way** | 1 | 2,215.17 | 4.764821 | 🟢 medium — moderately distinctive |
| 1066 | **saying** | 1 | 2,213.31 | 4.760829 | 🟢 medium — moderately distinctive |
| 1067 | **need** | 1 | 2,191.60 | 4.714128 | 🟢 medium — moderately distinctive |
| 1068 | **among** | 1 | 2,189.83 | 4.710333 | 🟢 medium — moderately distinctive |
| 1069 | **line** | 1 | 2,184.58 | 4.699034 | 🟢 medium — moderately distinctive |
| 1070 | **raise** | 1 | 2,184.58 | 4.699034 | 🟢 medium — moderately distinctive |
| 1071 | **see** | 1 | 2,174.25 | 4.676811 | 🟢 medium — moderately distinctive |
| 1072 | **reached** | 1 | 2,164.14 | 4.655071 | 🟢 medium — moderately distinctive |
| 1073 | **systems** | 1 | 2,157.52 | 4.640835 | 🟢 medium — moderately distinctive |
| 1074 | **support** | 1 | 2,141.38 | 4.60611 | 🟢 medium — moderately distinctive |
| 1075 | **currently** | 1 | 2,136.64 | 4.595923 | 🟢 medium — moderately distinctive |
| 1076 | **raised** | 1 | 2,136.64 | 4.595923 | 🟢 medium — moderately distinctive |
| 1077 | **later** | 1 | 2,118.17 | 4.556183 | 🟢 medium — moderately distinctive |
| 1078 | **according** | 1 | 2,106.25 | 4.53054 | 🟢 medium — moderately distinctive |
| 1079 | **union** | 1 | 2,104.78 | 4.527381 | 🟢 medium — moderately distinctive |
| 1080 | **subject** | 1 | 2,060.07 | 4.43121 | 🟢 medium — moderately distinctive |
| 1081 | **levels** | 1 | 2,048.23 | 4.405749 | 🟢 medium — moderately distinctive |
| 1082 | **following** | 1 | 2,030.40 | 4.367389 | 🟢 medium — moderately distinctive |
| 1083 | **second** | 1 | 2,012.02 | 4.327858 | 🟢 medium — moderately distinctive |
| 1084 | **results** | 1 | 1,919.71 | 4.129303 | 🟢 medium — moderately distinctive |
| 1085 | **including** | 1 | 1,901.37 | 4.089838 | 🟢 medium — moderately distinctive |
| 1086 | **central** | 1 | 1,875.58 | 4.034378 | 🟢 medium — moderately distinctive |
| 1087 | **during** | 1 | 1,862.34 | 4.005887 | 🟢 medium — moderately distinctive |
| 1088 | **cut** | 1 | 1,859.73 | 4.000284 | 🟢 medium — moderately distinctive |
| 1089 | **next** | 1 | 1,819.14 | 3.912963 | 🟢 medium — moderately distinctive |
| 1090 | **lower** | 1 | 1,816.76 | 3.907856 | 🟢 medium — moderately distinctive |
| 1091 | **common** | 1 | 1,733.85 | 3.729504 | 🟢 medium — moderately distinctive |
| 1092 | **offer** | 1 | 1,731.87 | 3.725252 | 🟢 medium — moderately distinctive |
| 1093 | **made** | 1 | 1,673.84 | 3.600421 | 🟢 medium — moderately distinctive |
| 1094 | **increase** | 1 | 1,643.51 | 3.535181 | 🟢 medium — moderately distinctive |

---

*Corpus reference: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth\_idf=True, lowercase=True).*  
*Generated 2026-09-21 by `generate_termbase.py`.*