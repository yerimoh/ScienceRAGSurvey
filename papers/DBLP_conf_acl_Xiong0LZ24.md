---
title: "Benchmarking Retrieval-Augmented Generation for Medicine"
bib_key: "DBLP:conf/acl/Xiong0LZ24"
year: 2024
domain: medical, bio
type: Method
venue: ACL (Findings)
paper_link: https://aclanthology.org/2024.findings-acl.372
---

# MEDRAG: Benchmarking Retrieval-Augmented Generation for Medicine
> ACL Findings 2024 | Method | medical · bio

## TL;DR
**MEDRAG** is a first-stage RAG toolkit/pipeline for medical QA. On **MedCorp**, which bundles corpora from four domains, it retrieves relevant snippets using four retrievers (BM25/Contriever/SPECTER/MedCPT) with RRF fusion, then injects them into the chain-of-thought prompts of six LLMs to generate answers. It is a modular system in which corpus, retriever, and LLM can be freely combined and swapped, designed to enable systematic comparison of how each component affects medical RAG performance.

## Architecture (MEDRAG Architecture)
MEDRAG is a modular pipeline made of three layers, **corpus → retriever → LLM**, and the components of each layer can be swapped in a plug-and-play fashion.

### (1) Corpora — MedCorp
A corpus that integrates four heterogeneous collections of medical documents. Each document is split into **snippets**, the unit of retrieval, for use.

| Corpus | Documents | Snippets | Average length | Character |
|---|---|---|---|---|
| PubMed | 23.9M | 23.9M | 296 tokens | Biomedical paper abstracts |
| StatPearls | 9.3k | 301.2k | 119 tokens | Clinical decision-support material (NCBI Bookshelf) |
| Textbooks | 18 | 125.8k | 182 tokens | Medical textbooks |
| Wikipedia | 6.5M | 29.9M | 162 tokens | General encyclopedia |
| **MedCorp (total)** | **30.4M** | **54.2M** | **221 tokens** | Integrated corpus |

- StatPearls is a corpus that this paper is the **first to evaluate** in the biomedical NLP community.
- By mixing different domains (papers/clinical/textbooks/general), it makes it possible to compare which source is effective for each question type.

### (2) Retrievers (4 types)
Retrievers with different matching strategies are provided under a single unified interface.

- **BM25** — lexical retriever (bag-of-words + TF-IDF, Pyserini). Strong at exact term matching.
- **Contriever** — dense retriever. A general-purpose semantic embedding pretrained with contrastive learning on Wikipedia and CCNet.
- **SPECTER** — dense retriever for the scientific-literature domain. Encodes similar documents close together in the embedding space.
- **MedCPT** — biomedical-specialized dense retriever. Trained on 255M PubMed user click data, SOTA in biomedical IR.

### (3) RRF — Reciprocal Rank Fusion
A fusion technique that combines the rankings of multiple retrievers, favoring snippets that commonly rank near the top.
- **RRF-2**: BM25 + MedCPT (the best pairing of one lexical and one dense retriever)
- **RRF-4**: all four retrievers combined (the broadest coverage)
- Improves average performance on MedCorp by **+1.4% ~ +10.7%** over a single retriever.

### (4) LLMs (6 types)
The reader that takes the retrieved context and generates the answer. Spanning general-purpose/biomedical and proprietary/open-source.

| Model | Size | Type | Domain |
|---|---|---|---|
| GPT-4 | proprietary | Proprietary | General |
| GPT-3.5 | proprietary | Proprietary | General |
| Mixtral | 8×7B | Open-source | General |
| Llama2 | 70B | Open-source | General |
| MEDITRON | 70B | Open-source | Biomedical |
| PMC-LLaMA | 13B | Open-source | Biomedical |

## Pipeline (inference)
When a single question comes in, it goes through the following steps.

1. **Question input** — takes a multiple-choice medical question as the query.
2. **Retrieval (Question-Only Retrieval)** — passes only the question text to the retriever (see the setting below).
3. **Ranking / RRF fusion** — the selected retriever ranks snippets, and if multiple retrievers are used, their rankings are merged with RRF.
4. **Context construction** — prepends the top **k snippets (default k=32)** to the front of the prompt.
5. **Generation** — the LLM reasons with **chain-of-thought** based on the retrieved context.
6. **Output** — produces JSON containing the step-by-step reasoning process and the selected answer.

### Two core evaluation settings
- **Zero-shot (ZSL)**: operates without few-shot examples. Reflects real-world medical situations where examples are hard to obtain.
- **Question-Only Retrieval (QOR)**: uses **only the question, without giving the answer options as input** during retrieval. This setting blocks the leakage in prior RAG evaluations where exposing the options to the retriever let the answer leak through, and this paper is the first to propose and adopt it in medical QA evaluation.

## Key methodological findings

| Finding | Content (verified figures) |
|---|---|
| **Overall MEDRAG improvement** | Up to **+18%** improvement over CoT across six LLMs. GPT-3.5 shows the largest at **+17.9%**, while PMC-LLaMA shows the smallest at about **+0.52%**. |
| **A good retriever substitutes for LLM size** | GPT-3.5 + MEDRAG(MedCorp + RRF-4) = **71.57%**, GPT-4 + CoT = **73.44%** (gap of 1.87pp). Lifts GPT-3.5/Mixtral to GPT-4-level. |
| **RRF-4 is the optimal fusion** | Combining all 4 retrievers (RRF-4) gives the best MIRAGE average (71.57% for GPT-3.5). **+1.4~10.7%** over a single retriever. For tasks where individual retrievers are weak, such as BioASQ-Y/N, RRF-2 (BM25+MedCPT) is favorable. |
| **log-linear scaling** | On MMLU-Med, MedQA-US, and MedMCQA, performance increases roughly log-linearly over the snippet-count range k≤32, then declines afterward due to increased noise. |
| **"lost-in-the-middle"** | A U-shaped pattern where accuracy is highest when the ground-truth snippet is at the front or back of the context, and drops sharply when it sits in the **middle**. The ordering of snippet placement affects performance. |

## The jointly proposed benchmark: MIRAGE
A medical QA benchmark released together for evaluating MEDRAG.
- **5 datasets, 7,663 multiple-choice questions in total**: MMLU-Med(1,089), MedQA-US(1,273), MedMCQA(4,183), PubMedQA(500), BioASQ-Y/N(618).
- All evaluated under the zero-shot · question-only retrieval setting.
- (The detailed construction process is omitted from this summary — this summary centers on the MEDRAG system.)

## Limitations
The content the authors explicitly stated in Limitations.
1. Focuses on the **vanilla RAG** structure rather than the latest RAG variants.
2. Corpus coverage is incomplete (e.g., PubMed full-text, FAQs, etc. not included).
3. Ground-truth snippet evaluation is possible **only on two datasets**.
4. The constraint of the **multiple-choice** format — the absence of evaluation of the generated rationale (the reasoning description).

## Related links
- Paper: <https://aclanthology.org/2024.findings-acl.372> · arXiv: <https://arxiv.org/abs/2402.13178> (HTML: <https://arxiv.org/html/2402.13178>)
- MedRAG toolkit: <https://github.com/Teddy-XiongGZ/MedRAG>
- MIRAGE benchmark: <https://github.com/Teddy-XiongGZ/MIRAGE>
