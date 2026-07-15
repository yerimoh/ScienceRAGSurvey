---
title: "pathfinder: A Semantic Framework for Literature Review and Knowledge Discovery in Astronomy"
bib_key: "iyer2024pathfinder"
year: 2024
domain: astronomy
type: Method
venue: ApJS
paper_link: https://doi.org/10.3847/1538-4365/ad7c43
---
# Pathfinder: Semantic RAG Framework for Astronomy Literature
> ApJS 275:38, 2024 | Method | astronomy

## TL;DR
Pathfinder is a system (framework) for astronomy literature review and knowledge discovery that indexes the abstracts of roughly 350,000 astronomy papers (ADS + arXiv astro-ph) via embedding-based semantic search, and combines HyDE query expansion, reranking, and RAG/ReAct generation to produce long-form answers with citations. It is a grounded literature QA tool that replaces conventional keyword-matching search with semantic search, and it is an actually deployed system rather than a benchmark.

## Architecture (Pathfinder Architecture)
- **Corpus:** A total of 352,194 peer-reviewed astronomy papers (roughly 270,000 Kaggle arXiv astro-ph papers augmented with ADS metadata). The current version uses only abstracts, with possible future extension to full text.
- **Embedding / vector search:** Embedded with OpenAI text-embedding-3-small (1536 dimensions), indexed and searched in FAISS using cosine similarity. Visualization uses UMAP 2D reduction.
- **Keyword extraction:** spaCy and pytextrank pre-extract 20 keywords per abstract (used in keyword reranking).
- **Reranking (recency / citation / keyword):**
  - *Recency*: a sigmoid penalty for papers older than roughly 5 years.
  - *Citation*: a sigmoid weighting that favors highly cited literature.
  - *Keyword*: weights documents that match by comparing astronomy jargon, celestial object names, and user-specified strings against the pre-extracted keywords.
- **Two-stage retrieval + neural reranker:** an initial top-k=250 is fetched via HyDE semantic search, then reordered with Cohere rerank-english-v3.0 to select a final 1 to 30 papers.
- **Generator (RAG + ReAct):** RAG is built with LangChain. It synthesizes an answer by passing the retrieved abstract chunks to the LLM, constrained to respond "I don't know" when no relevant source exists. For compound and counterfactual queries, a ReAct agent iterates over reasoning and retrieval. GPT-4 / GPT-4o mini are used for generation and consensus evaluation.
- **Frontend:** Streamlit UI, deployed on HuggingFace Spaces (pathfinder.app). Dataset and code are public.

## Pipeline (inference)
1. Query input → query type classification (single/multi-paper facts, consensus evaluation, compound, What-If/counterfactual, etc.) and determination of NER, jargon, and time-sensitivity flags.
2. **HyDE query expansion:** the LLM, acting as an "expert astronomer," rewrites the query into a domain-specific hypothetical abstract.
3. **Semantic search:** retrieves top-k=250 candidates from FAISS using the expanded query embedding.
4. **Reranking:** recency/citation/keyword weighting + Cohere reranker to select the final 1 to 30 papers.
5. **Answer generation:** RAG answer generation with query-type-specific prompts (single = concise, multi = summary synthesis, broad query = initial answer → self-critique → refinement). Compound and counterfactual queries are handled with ReAct steps.
6. **Output:** answer + top-k paper table + query type + relevance (0-1) estimate. Consensus queries are evaluated on a 7-level scale (Strong Agreement … No Clear Consensus … Strong Disagreement), and outlier papers are also flagged.

## Key features/results
- **Applications:** grounded literature QA workflows such as semantic-based literature review, knowledge discovery, consensus evaluation, and detection of unexpected papers.
- **Single-paper synthesis benchmark** (500 random papers, top-k=10): Bag-of-Words s=0.46, r⁻¹=0.29 → HyDE+reranking s=0.84, r⁻¹=0.74.
- **Multi-paper synthesis benchmark** (200 review papers, top-k=50): Bag-of-Words recall=0.15, nDCG=0.09 → HyDE+reranking recall=0.29, nDCG=0.19.
- **Gold QA dataset:** via a Slack bot, 36 astronomers submitted 370 questions, and expert answers were collected. Positive user interactions and retrieval scores were positively correlated (Spearman ρ=+0.33).

## Limitations
- Only abstracts are indexed → deep data and method-detail queries about the body text are frequently missed.
- Very recent papers and some niche journals are not included (incomplete corpus).
- The citation graph is not used → unsuitable for detailed bibliometric analysis, searches for specific authors or institutions, or performing computations.
- LLM bias and hallucination are possible → answers need to be cross-checked against the top-k papers.
- Compound and counterfactual queries cannot be answered directly without ReAct, and ReAct itself can get stuck in loops.

## Related links
- Iyer, Yunus, O'Neill, Ye, et al., ApJS 275:38, 2024.
- arXiv: 2408.01556 (https://arxiv.org/abs/2408.01556)
- DOI: https://doi.org/10.3847/1538-4365/ad7c43
- Live tool: pathfinder.app (deployed on HuggingFace Spaces), code and dataset public.
