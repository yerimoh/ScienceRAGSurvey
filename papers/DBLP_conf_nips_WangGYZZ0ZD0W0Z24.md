---
title: "AutoSurvey: Large Language Models Can Automatically Write Surveys"
bib_key: "DBLP:conf/nips/WangGYZZ0ZD0W0Z24"
year: 2024
domain: general
type: Method
venue: NeurIPS
paper_link: https://arxiv.org/abs/2406.10252
---
# AutoSurvey: Automatic Survey Writing with LLMs
> NeurIPS 2024 | Method | general

## TL;DR
AutoSurvey is a system that automatically writes comprehensive academic surveys through a four-stage pipeline of (1) retrieval → (2) outline generation → (3) parallel section drafting → (4) citation-aware integration and refinement, circumventing the LLM's context limitations and lack of expertise.

## Architecture (AutoSurvey Architecture)
- **Retrieval:** RAG approach. Using a corpus of about 530,000 arXiv CS papers, each paper's title and abstract is embedded with `nomic-embed-text-v1.5` and ranked by similarity. 1,200 papers initially, and 60 papers per description at the subsection stage.
- **Outline generation:** The initially retrieved papers are split into 30,000-token chunks, a per-chunk outline is created, and then merged. The number of sections is fixed at 8.
- **Parallel section drafting:** The writing LLM is Claude-3-Haiku (speed and cost). Each subsection is generated in parallel according to the outline, citing reference papers.
- **Integration & Refinement:** Citations are extracted and mapped to arXiv papers, and considering the context of the preceding and following sections, redundancy is removed, readability is improved, and citation accuracy is checked.
- **Evaluation LLM judge:** Candidate surveys are evaluated with a combination of GPT-4, Claude-3-Haiku, and Gemini-1.5-Pro to select the best version (N=2).

## Pipeline (inference)
1. Topic input.
2. Initial retrieval (1,200 papers) + per-chunk outline generation → merge → finalize the 8-section outline.
3. 60 additional papers retrieved per subsection → Claude-3-Haiku writes parallel drafts (including citations).
4. Citation extraction and mapping → section refinement (redundancy removal, citation check).
5. Multi-LLM-as-Judge evaluation → select the best survey among candidates.

## Key results
**Citation Quality (64k tokens)**

| Method | Recall(%) | Precision(%) |
|---|---|---|
| AutoSurvey | 82.25 | 77.41 |
| Naive RAG | 68.79 | 61.97 |
| Human | 86.33 | 77.78 |

**Content Quality (64k, 5-point)**: AutoSurvey Coverage 4.73 / Structure 4.33 / Relevance 4.86 (Human 5.00 / 4.66 / 5.00).
**Speed**: AutoSurvey 73.6 surveys/hour vs Human 0.07. Domain-knowledge question accuracy +9.2% over direct answering.

## Limitations
- Citation recall and content quality fall slightly short of humans (especially recall and structure).
- Fixing the number of sections at 8 limits structural flexibility.
- The retrieval corpus is limited to about 530K arXiv CS papers (domain generalization unverified).
- The initial stage uses only abstracts, and the drafting stage uses only the front part of the body text (~1,500 tokens).

## Related links
- arXiv: 2406.10252 (https://arxiv.org/abs/2406.10252) · NeurIPS 2024
- Writing LLM Claude-3-Haiku / evaluation LLMs GPT-4, Claude-3-Haiku, Gemini-1.5-Pro / embedding nomic-embed-text-v1.5
