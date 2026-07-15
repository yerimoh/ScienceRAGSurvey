---
title: "Biomedical knowledge graph-optimized prompt generation for large language models"
bib_key: "DBLP:journals/bioinformatics/SomanRMASPVCSRI24"
year: 2024
domain: bio, medical
type: Method
venue: Bioinformatics
paper_link: https://arxiv.org/abs/2311.17330
---
# KG-RAG: Biomedical Knowledge-Graph-Optimized Prompting (SPOKE)
> Bioinformatics 2024 | Method | bio · medical

## TL;DR
A token-optimized KG-RAG framework that extracts disease-centric subgraphs from the SPOKE biomedical knowledge graph using a minimal graph schema, then, via embedding-based context pruning, selects only the triples most semantically relevant to the prompt to inject into the LLM prompt. Compared to Cypher-RAG, which injects the full schema, it reduces tokens by an average of 54% while improving retrieval accuracy and robustness.

## Architecture (KG-RAG Architecture)
- **SPOKE KG:** A property graph integrating 41 curated biomedical DBs (28 node types, ~42 million nodes; 91 edge types, ~160 million edges). Most of the curation is based on systematic experimental measurements.
- **Minimal-schema subgraph:** Fetches only the neighbor triples (S,P,O) of the disease node and, using SPOKE's predicate naming conventions, converts the triples into English sentences without a schema (e.g., "Disease hypertension associates Gene VHL").
- **Embedding-based pruning:** Embeds the extracted triples and the prompt into the same vector space, and selects only those exceeding the 75th percentile of cosine similarity & ≥0.5. The context embedding uses PubMedBert.
- **Prompt generation:** Converts the refined context into natural language + attaches provenance (optional: evidence such as p-value) to compose an enriched prompt.
- Hyperparameters: context volume (100–200), context embedding model. Entity recognition uses GPT-3.5 extraction + MiniLM to match SPOKE disease nodes (99.7% accurate).

## Pipeline (inference)
1. Disease entity recognition (GPT-3.5 extraction → MiniLM embedding to match SPOKE nodes).
2. Fetch the neighbor triples of the matched nodes.
3. Embed triples & prompt → select prompt-aware context via cosine pruning.
4. Natural-language conversion + provenance attachment → assemble enriched prompt.
5. Generate answer with an LLM (Llama-2-13b/GPT-3.5/GPT-4, temp 0).

## Key results
**RAG comparison (KG-RAG vs Cypher-RAG, 100 questions):** retrieval accuracy 75%→**97%**; under lowercase perturbation of entity names, Cypher-RAG collapses to 0% while KG-RAG maintains 97%; tokens 8006→**3693 (−54%)**.
**True/False·MCQ (accuracy):** on MCQ, Llama-2 0.31→**0.53**, GPT-3.5 0.63→**0.79**, GPT-4 0.68→0.74. Consistent improvement across all three LLMs.

## Limitations
- Currently only disease-centric entities are embedded → limited to disease-centric questions (extension to all nodes is future work).
- Performance depends on the quality of SPOKE information (rigorous evaluation of the KG itself is out of scope).
- Implemented on SPOKE — generalization to other KGs/domains is future work.

## Related links
- arXiv: 2311.17330 · Bioinformatics 2024 (Soman et al., UCSF)
- Code: https://github.com/BaranziniLab/KG_RAG
