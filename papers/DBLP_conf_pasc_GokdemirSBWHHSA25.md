---
title: "HiPerRAG: High-Performance Retrieval Augmented Generation for Scientific Insights"
bib_key: "DBLP:conf/pasc/GokdemirSBWHHSA25"
year: 2025
domain: bio, medical, chem, physics
type: Method
venue: PASC
paper_link: https://arxiv.org/abs/2505.04846
---
# HiPerRAG: HPC-Scale RAG for Scientific QA
> PASC 2025 | Method | bio · medical · chem · physics

## TL;DR
HiPerRAG is a RAG infrastructure that uses high-performance computing (HPC) to index and search over 3.6 million scientific papers in order to answer multiple-choice scientific QA. Built around Oreo, a multimodal document parser, and ColTrast, a query-aware encoder fine-tuning method, it makes million-document-scale RAG possible using thousands of GPUs on the Polaris, Sunspot, and Frontier supercomputers. (Because the output is retrieval-answer closed-form QA rather than synthesis, it is classified as K1.O1.)

## Architecture (HiPerRAG Architecture)
- **Corpus:** Indexes and searches over 3.6 million scientific papers.
- **Oreo (multimodal document parsing):** A model that parses large-scale scientific literature at high throughput. About 4.5x faster than existing parsers.
- **ColTrast (retriever fine-tuning):** An algorithm that fine-tunes a query-aware encoder using contrastive + late-interaction methods to improve retrieval accuracy.
- **Generator:** Passes retrieved passages to an LLM to generate multiple-choice answers.
- **HPC stack:** Infrastructure that scales to thousands of GPUs on Polaris, Sunspot, and Frontier (not a standalone model, but a software stack that underpins million-document-scale RAG).

## Pipeline (inference)
1. Question input → retrieve relevant passages from the 3.6M+ paper index using the ColTrast-fine-tuned encoder.
2. Pass the retrieved passages to the LLM generator.
3. Generate answers in multiple-choice/short-answer form and evaluate by accuracy.

## Key results
- **90% accuracy on SciQ and 76% on PubMedQA** on existing scientific QA benchmarks.
- Introduces self-built protein QA benchmarks (ProteinInteractionQA, ProteinFunctionQA).
- Key contributions: scaling RAG to the million-document level (solving parsing and embedding cost problems) and improving retrieval accuracy.

## Limitations
- The output is limited to multiple-choice QA, so it does not address multi-source integration (synthesis) or long-form synthesis.
- Because the infrastructure presupposes supercomputer-class resources, reproducibility and accessibility are limited.
- The protein QA benchmarks are created by LLM generation, so quality bias is possible.

## Related links
- arXiv: 2505.04846 (https://arxiv.org/abs/2505.04846)
- DOI: https://doi.org/10.1145/3732775.3733586 (PASC 2025)
- Argonne National Laboratory · University of Chicago et al.
