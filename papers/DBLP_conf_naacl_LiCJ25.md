---
title: "GraPPI: A Retrieve-Divide-Solve GraphRAG Framework for Large-scale Protein-protein Interaction Exploration"
bib_key: "DBLP:conf/naacl/LiCJ25"
year: 2025
domain: bio
type: Method
venue: NAACL
paper_link: https://aclanthology.org/2025.findings-naacl.201/
---
# GraPPI: Retrieve-Divide-Solve GraphRAG over STRING PPI
> NAACL 2025 (Findings) | Method | bio

## TL;DR
GraPPI is a GraphRAG that operates on top of the STRING protein-protein interaction (PPI) knowledge graph, processing large-scale signaling pathways with a Retrieve-Divide-Solve strategy. It splits an enormous pathway into individual PPI edges, explains them in parallel, and then synthesizes and re-ranks at the pathway level, producing explainable and scalable pathway analysis for therapeutic target discovery.

## Architecture (GraPPI Architecture)
- **STRING PPI KG:** 18,767 nodes (human proteins) / 2,955,220 edges. Edges carry combined_score (confidence) and interaction type, and nodes carry protein annotations.
- **Retrieve:** A sliding kNN graph window extracts connected protein nodes to construct an interaction subgraph (FAISS).
- **Divide:** An edge-explanation agent decomposes the whole pathway into individual edges, analyzing each edge in parallel together with the context of its two endpoint proteins.
- **Solve:** A pathway-explanation agent synthesizes the PPI pathway explanations and evaluates therapeutic relevance via LLM zero-shot ranking.
- **Generator:** Embedding text-embedding-3-small, LLM GPT-4o/4o-mini/4-Turbo + expert co-designed CoT.

## Pipeline (inference)
1. Initial protein input → connected-node extraction + kNN window to form the interaction subgraph.
2. Edge Explanation: explain each PPI edge in parallel together with the annotations of its two endpoint proteins (divide).
3. Path Exploration: aggregate the edge explanations to synthesize multiple PPI pathway explanations.
4. Re-rank: order the pathways by LLM relevance score → present the top n pathways.

## Key results
Evaluation: accuracy (semantic and lexical alignment, BERTScore and ROUGE), scalability (graphs of 40–160 paths), and expert case studies. Across 4 settings (Baseline / Zero-shot+CoT / RAG w/o CoT / GraPPI), **GraPPI achieves the best across all LLMs and metrics**. For example, GPT-4-Turbo ROUGE-1 F1 RAG 38.70 → **GraPPI 42.19**, ROUGE-L 31.93 → **37.47**.

## Limitations
- STRING does not cover all known PPIs.
- The case study is based on 2 initial proteins (limited representativeness).
- The benefit diminishes as the graph grows larger, and edge explanations approach the LLM context limit.
- A research prototype (not a deployed system).

## Related links
- arXiv: 2501.16382 · NAACL 2025 Findings (Li, Chen, Jeon)
- Code: https://github.com/AaronLi43/GraPPI
