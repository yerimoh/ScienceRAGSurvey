---
title: "LitLLM: A Toolkit for Scientific Literature Review"
bib_key: "DBLP:journals/corr/abs-2402-01788"
year: 2024
domain: general
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2402.01788
---
# LitLLM: A RAG Toolkit for Scientific Literature Review
> arXiv 2024 | Method | general

## TL;DR
LitLLM is a modular RAG toolkit that takes a user abstract as input and performs candidate reference retrieval → re-ranking → related work generation. By combining retrieval-based grounding with plan-based controlled generation, it mitigates hallucination and outdated-information problems, helping authors draft literature reviews.

## Architecture (LitLLM Architecture)
It consists of three modules, and the LLM in each component can be freely swapped.
- **(1) Retrieval:** Uses the Semantic Scholar API and OpenAlex API. The LLM summarizes the input abstract into search keywords (the user can add keywords or a seed paper). Results are sorted by relevance, citation count, and year.
- **(2) Re-ranking:** Compensates for the low precision of abstract-based retrieval. The core is instructional permutation generation (RankGPT family) — the candidate list is given all at once and the LLM generates a permutation in descending order of relevance. As an auxiliary approach, debate-style ranking (pro/con arguments for inclusion + probability) is used.
- **(3) Plan-based Generation:** Supports zero-shot RAG generation as well as plan-based generation that controls output structure via a "plan" (number of sentences + per-line citation descriptions).
- **(4) Toolkit/UI:** A React interface (abstract input, keyword display, re-ranking results, sentence plan input, related work output). The LLM is GPT-3.5-turbo or GPT-4 (swappable).

## Pipeline (inference)
1. The user inputs an abstract.
2. The LLM summarizes it into search keywords (+ user keywords/seed paper).
3. Candidate retrieval via Semantic Scholar/OpenAlex.
4. Re-ranking via LLM permutation (or debate-style).
5. (Optional) sentence plan input.
6. Related work draft generation via zero-shot or plan-based generation.

## Key Results/Features
- No quantitative benchmark numbers are reported. A preliminary user study was conducted with 5 researchers.
- Qualitative feedback: zero-shot output is richer, while plan-based output is more tailored to one's own paper and more accessible.
- Modular design allowing LLM swapping at each of the retrieval, re-ranking, and generation stages, with sorting options provided.

## Limitations
- Both the query and the retrieved papers use only abstracts (full-text ingestion is future work).
- Limited coverage of the retrieval APIs (expansion to Google Scholar and others is needed).
- Only a small preliminary study with 5 participants; no quantitative benchmark against competing systems.
- Caution regarding hallucination in the generated output, and a recommendation to disclose LLM usage.

## Related links
- arXiv: 2402.01788 (https://arxiv.org/abs/2402.01788)
- Project: https://litllm.github.io · Demo video https://youtu.be/E2ggOZBAFw0
