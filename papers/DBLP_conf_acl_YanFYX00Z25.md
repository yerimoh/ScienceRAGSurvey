---
title: "SurveyForge: On the Outline Heuristics, Memory-Driven Generation, and Multi-dimensional Evaluation for Automated Survey Writing"
bib_key: "DBLP:conf/acl/YanFYX00Z25"
year: 2025
domain: general
type: Method
venue: ACL
paper_link: https://arxiv.org/abs/2503.04629
---
# SurveyForge: Outline-Heuristic, Memory-Driven Survey Generation
> ACL 2025 | Method | general

## TL;DR
SurveyForge is a framework that automatically writes academic surveys: it heuristically learns the structure of human-written surveys to generate an outline, secures high-quality references with a memory-based retrieval agent (SANA), and then generates and refines sections in parallel.

## Architecture (SurveyForge Architecture)
It uses two knowledge bases: a Research Paper DB of about 600,000 arXiv CS papers (titles and abstracts), and a Survey Outline DB of hierarchical outlines extracted from about 20,000 reviews.

- **(A) Outline Heuristics — learning structure from human surveys:** For a topic T, it retrieves relevant papers together with human survey outlines, provides the human outlines as demonstrations to generate a first-pass outline → re-retrieves per section to generate a second-pass outline → merges them. (Outline quality: without heuristics 81.78 → with domain-specific outlines 86.67.)
- **(B) Memory-driven Scholar Navigation Agent (SANA):** ① Memory for Sub-query (MS) — decomposes a complex query into sub-queries using memory as context, ② Memory for Retrieval (MR) — retrieves candidates from outline-associated memory rather than the entire DB (preventing cross-section isolation and duplication), ③ Temporal-aware Reranking (TRE) — balances relevance, citation influence, and recency via 2-year buckets for reranking.
- **Section generation:** Generates subsections in parallel from the reranked literature → combines drafts → LLM refinement to remove duplication and integrate.

## Pipeline (inference)
1. Topic input → retrieve papers and human outlines.
2. First-pass outline via heuristics → re-retrieve per section for the second-pass outline → merge.
3. SANA: sub-query decomposition (MS) → memory-based retrieval (MR) → temporal/citation/relevance reranking (TRE).
4. Parallel subsection generation → combine → refine → final survey.
- Efficiency (GPT-4o mini): about $0.43/survey, about 10 minutes.

## Main Results
Evaluation benchmark **SurveyBench** (10 CS topics, ~100 human surveys), metrics SAM-R/O/C.

| Model | Method | Reference Cov. | Outline | Content Avg |
|---|---|---|---|---|
| GPT-4o mini | AutoSurvey | 0.2035 | 83.10 | 75.05 |
| GPT-4o mini | **SurveyForge** | **0.4236** | **86.62** | **77.06** |
| Human | — | 0.6294 | 87.62 | — |

Win-rate (vs AutoSurvey): Outline 73~75%, Content 69~70% (evaluated by 20 PhDs, Cohen's κ 0.65~0.72). Ablation: MR+MS+TRE is best (Reference Cov. 0.397).

## Limitations
- Weak at analyzing and synthesizing relationships across multiple sources (strong at summarization but weak at comparative and evolutionary analysis).
- Inaccurate citations and claims occasionally arise due to LLM hallucination.
- Lacks the critical thinking and originality characteristic of human authors.

## Related links
- arXiv: 2503.04629 (https://arxiv.org/abs/2503.04629) · ACL 2025
- Code: https://github.com/Alpha-Innovator/SurveyForge · Data SurveyBench (HuggingFace U4R/SurveyBench)
