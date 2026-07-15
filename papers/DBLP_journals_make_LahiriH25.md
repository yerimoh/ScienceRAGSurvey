---
title: "AlzheimerRAG: Multimodal Retrieval-Augmented Generation for Clinical Use Cases"
bib_key: "DBLP:journals/make/LahiriH25"
year: 2025
domain: medical
type: Method
venue: Mach. Learn. Knowl. Extr.
paper_link: https://doi.org/10.3390/make7030089
---
# AlzheimerRAG: Cross-modal Attention Fusion for Alzheimer Clinical RAG

> Mach. Learn. Knowl. Extr. (MDPI) | 2025 | Method | medical
> Aritra Kumar Lahiri, Qinmin Vivian Hu — Toronto Metropolitan University (Canada)
> DBLP: `journals/make/LahiriH25` · arXiv: [2412.16701](https://arxiv.org/abs/2412.16701)

## TL;DR
A multimodal RAG system that performs Alzheimer clinical question answering by integrating the text of PubMed papers with extracted visual materials (figures and diagrams) via **cross-modal attention fusion**. It fine-tunes Llama-2-7b-pubmed using QLoRA-based PEFT and, on the **BioASQ + PubMedQA** benchmarks, improves retrieval and synthesis quality over text-only RAG.

---

## Construction Methodology

```
Step 1 — Data source (multimodal PubMed)
  Extracted from PubMed Alzheimer's-related papers:
    • Text chunks (introduction, methods, results, discussion)
    • Visual elements: figure images, table images
  Visual elements are automatically captioned with a Vision Language Model

Step 2 — Cross-modal embedding generation
  ┌────────────┐                ┌──────────────┐
  │ Text chunks │ ─ tokenize ─►  │ Text encoder │ ─► text emb
  └────────────┘                └──────────────┘
  ┌────────────┐                ┌──────────────┐
  │ Figure imgs │ ─ caption  ─►  │ VLM encoder  │ ─► visual emb
  └────────────┘                └──────────────┘
                       │
                       ▼
          Cross-modal embedding fusion (attention)
                       │
                       ▼
                FAISS Vector Store + Object Store

Step 3 — PEFT-based fine-tuning
  Base model: Llama-2-7b-pubmed
  Training: QLoRA + PubMedQA dataset
  Purpose: medical domain specialization + multimodal input handling

Step 4 — Inference pipeline (Cross-modal Attention Fusion)
  User query → similarity search (text + visual simultaneously) →
    Align retrieved context via cross-modal attention →
    Fine-tuned LLM generates the answer

Step 5 — Evaluation
  Benchmarks: BioASQ, PubMedQA
  Comparison: text-only RAG baseline + non-RAG LLM
  Metric: retrieval accuracy, hallucination rate, human comparison
```

---

## Direct quotes from the source (arXiv:2412.16701)

> "incorporates **cross-modal attention fusion techniques** to integrate textual and visual data processing by efficiently indexing and accessing vast amounts of biomedical literature"

> "Our experimental results, compared to benchmarks such as **BioASQ and PubMedQA**, yield improved performance in the retrieval and synthesis of domain-specific information"

> "These processed elements are then converted into embeddings through a **cross-modal embedding fusion method** and stored in an object store and a vector database"

> "fine-tuned the **'Llama-2-7b-pubmed'** model by training it with the PubMedQA dataset from HuggingFace. The fine-tuning used parameter-efficient fine-tuning (PEFT) techniques like **QLoRA**"

---

## Key evaluation results

| Item | Value |
|---|---|
| Domain | Alzheimer's disease (clinical use cases) |
| Backbone LLM | Llama-2-7b-pubmed (PEFT/QLoRA fine-tuned) |
| Evaluation benchmarks | BioASQ, PubMedQA |
| Modalities | Text + Image (PubMed articles + extracted figures) |
| Accuracy | Human-level non-inferior |
| Hallucination rate | Low (reduced relative to text-only baseline) |

→ Consistently superior to both text-only RAG and non-RAG LLMs.

---

## Case Study (paper §Discussion)
- Alzheimer diagnosis assistance scenario
- Clinical decision support
- Integration of drug interaction + side-effect information
- Generation of patient education materials

---

## Limitations
- Specialized to the single Alzheimer domain → limited generalization scope
- Increased computational cost of large-scale image indexing
- Quantitative performance figures (F1, exact accuracy) are not provided in explicit table form in the paper (mostly qualitative comparison)
- Being Llama-2-7b-based, there are limitations relative to the latest frontier LLMs
- Image captioning quality has a large impact on the fusion results

---

## Related links
- **Paper (MDPI)**: [doi.org/10.3390/make7030089](https://doi.org/10.3390/make7030089)
- **arXiv preprint**: [arXiv:2412.16701](https://arxiv.org/abs/2412.16701)
- **DBLP**: [journals/make/LahiriH25](https://dblp.org/rec/journals/make/LahiriH25.html)
- **GitHub**: public code not confirmed
