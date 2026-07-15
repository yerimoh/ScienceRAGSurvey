---
title: "CG-RAG: Research Question Answering by Citation Graph Retrieval-Augmented LLMs"
bib_key: "DBLP:conf/sigir/HuLD0A0025"
year: 2025
domain: general
type: Method
venue: SIGIR
paper_link: https://doi.org/10.1145/3726302.3729920
---
# CG-RAG: Citation-Graph Retrieval-Augmented LLMs for Research QA
> SIGIR 2025 | Method | general (scientific research)

## TL;DR
A research QA framework that decomposes research papers into chunks and links them by citation relationships to build a hierarchical citation graph, and proposes the retriever **LeSeGR**, which performs entangled fusion of sparse (lexical) and dense (semantic) signals over the graph, so that the LLM is provided not only with retrieved evidence chunks but also with their contextual neighbors to generate grounded answers.

## Architecture (CG-RAG Architecture)
CG-RAG consists of three parts: (1) hierarchical citation graph construction, (2) the LeSeGR retriever, and (3) the context-aware answer generator.

**Hierarchical citation graph (paper chunk nodes + citation edges).** Because the body of a paper contains heterogeneous information whose role differs by section, such as related work / method / experiment, it is decomposed not at the paper level but at the level of fixed-length chunks (maximum chunk length 8,192 tokens). There are two kinds of edges.
- **Intra-document edges:** sequential adjacency and explicit cross-reference.
- **Inter-document edges:** when two papers have a citation relationship, for a given chunk the Top-n most relevant chunks from the counterpart paper are connected (relevance is the sum of the sparse and dense scores).

**LeSeGR (Lexical-Semantic Graph Retrieval) — integration of sparse+dense over the graph.** Unlike existing hybrid retrieval that simply combines the two signals after retrieval (post-retrieval), LeSeGR entangles and fuses the two signals within the graph topology.
- **Sparse signal:** query–chunk lexical relevance (cosine/inner product).
- **Dense signal:** semantic similarity between chunks (an MLP transforms the difference of chunk embeddings).
- **GNN message passing:** at each layer, the product "query–chunk sparse score × chunk-to-chunk dense score" gates the message flow so that only relevant information propagates to neighbors. After K layers, all chunks are scored using the final entangled representation.
- **Theoretical generality:** when there are no neighbors and aggregation is mean/sum, the LeSeGR score reduces to "log(sparse) + log(dense)", showing that existing post-retrieval hybrid fusion is a special case of LeSeGR (generalizing hybrid retrieval to a graph DB).

## Pipeline (inference)
1. Construct the hierarchical citation graph.
2. Encode the query and chunks with the sparse and dense encoders, and compute query–chunk lexical relevance and chunk-to-chunk semantic similarity.
3. Entangle and propagate the two signals through K layers of message passing, and score chunks with the final representation.
4. **Subgraph retrieval:** combine the Top-N chunks and their contextual neighbors to extract an induced subgraph.
5. **Grounded generation:** the LLM summarizes each contextual subgraph, then generates the final answer together with the query.

Implementation: the generation LLM is GPT-4o (2024-05-13), the sparse signal uses BGE-M3, the dense signal uses MiniLM, and the graph encoder is a Graph Transformer with 2 layers, 4 heads, and hidden dimension 1024.

## Key Results
**Datasets:** PubMedQA-1k (1,000 QA pairs, 7,849 papers), PapersWithCodeQA (924 questions, 12,171 papers).

PapersWithCodeQA

| Method | Acc | F1 | MRR | Hit@1 |
|---|---|---|---|---|
| BM25 | 0.689 | 0.617 | 0.765 | 0.736 |
| ColBERT (best hybrid) | 0.769 | 0.661 | 0.827 | 0.778 |
| **LeSeGR (ours)** | **0.835** | **0.703** | **0.884** | **0.827** |

PubMedQA — QA / retrieval (Hit@1)

| Method | Acc | F1 | Hit@1 |
|---|---|---|---|
| BM25 | 0.662 | 0.604 | 0.835 |
| ColBERT | 0.724 | 0.642 | 0.913 |
| **LeSeGR** | **0.778** | **0.685** | **0.961** |

Efficiency (PapersWithCodeQA): LeSeGR, with 1,921MB of GPU memory / 403.94ms query latency, outperforms ColBERT (12,674MB / 561.91ms) in both memory and latency. Ablation: a contextual neighbor count of n=4 is optimal, and among graph encoders Graph Transformer > GCN > GAT.

## Limitations
The paper has no explicit Limitations section. (Summarizer's note: the validation domains are limited to two scientific corpora, PubMed and PapersWithCode; generation relies on the GPT-4o API; and the sensitivity to graph-construction hyperparameters such as Top-n is addressed only in the ablation.)

## Related links
- arXiv: 2501.15067 (https://arxiv.org/abs/2501.15067)
- DOI: https://doi.org/10.1145/3726302.3729920 (SIGIR 2025, pp. 678–687)
- Authors: Yuntong Hu, Zhihan Lei, Zhongjie Dai, Allen Zhang, Abhinav Angirekula, Zhengwu Zhang, Liang Zhao
