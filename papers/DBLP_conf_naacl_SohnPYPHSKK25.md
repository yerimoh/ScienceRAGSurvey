---
notion_id: 355f2dcd-4912-8153-8151-d3b4e52f86da
title: Rationale-Guided Retrieval Augmented Generation for Medical Question Answering
bib_key: DBLP:conf/naacl/SohnPYPHSKK25
year: 2025
domain: medical
type: Method
venue: NAACL 2025 (Long Paper)
paper_link: https://aclanthology.org/2025.naacl-long.635/
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Rationale-Guided Retrieval Augmented Generation for Medical Question Answering (RAG²)

> NAACL | 2025 | Method | medical

## TL;DR
The LLM first generates a chain-of-thought rationale and uses it as the retrieval query, retrieves evenly from 4 corpora — **PubMed/PMC/Textbooks/Clinical Guidelines** — and trains a Flan-T5-large 770M filtering model on data automatically labeled by perplexity change, so that only informative snippets are passed to the LLM. While using only single-stage retrieval, it improves Llama-3-8B by an average of **+6.1%** and GPT-4o by **+0.9%** on MedQA, MedMCQA, and MMLU-Med.

## Background
**Limitations of existing medical RAG**
- Including broad context such as patient information in a medical query confuses the retriever, while a query that is too short requires relying on implicit medical knowledge
- PubMed-biased retrievers like MedCPT marginalize clinical guidelines/textbooks → retriever bias
- Self-BioRAG requires full fine-tuning of the LLM (training Llama-2 7B/13B) → high training cost
- Adaptive-RAG uses only correct/incorrect as labels → ignores the fine-grained signal of document usefulness

**Why it is needed**
- An efficient medical RAG that approaches SOTA using only a single pass + a 770M small filtering model is needed
- Since annotation is very costly in the medical domain, automatic labeling by perplexity difference is attractive
- Author quote: "These rationale-based queries help identify key... and they refine poorly targeted retrieval results" (§1)

## Architecture (paper Figure 1)
```
                       [Initial Query x]
                            │
                            ▼
        ┌──────────────────────────────────────┐
        │  ① Rationale-Based Query Formulation │
        │  ────────────────────────────────    │
        │  Base LLM (Llama-3-8B / Meerkat-7B / │
        │            GPT-4o) at temp=0         │
        │  Generate rationale via Chain-of-Thought │
        │  → the rationale text itself is the new query │
        │    (initial query excluded — token limit) │
        └──────────────┬───────────────────────┘
                       │
        ┌──────────────▼───────────────────────┐
        │  ② Balanced Retrieval                │
        │  ────────────────────────────────    │
        │  Retrieve in equal proportion from each of 4 corpora │
        │  - PubMed (large, MedCPT training source) │
        │  - PMC (large, open access)          │
        │  - Medical Textbooks (small, specialized) │
        │  - Clinical Guidelines (small, up-to-date) │
        │  → MedCPT cross-encoder reranks based on │
        │    the initial query                 │
        └──────────────┬───────────────────────┘
                       │
        ┌──────────────▼───────────────────────┐
        │  ③ Rationale-Guided Filtering        │
        │  ────────────────────────────────    │
        │  Flan-T5-large (770M, single RTX 3090) │
        │  Trained based on ΔPPL = PPL(x) − PPL(x, d) │
        │  → judges each snippet Helpful / Not Helpful │
        │    then feeds only Helpful ones to the LLM │
        └──────────────┬───────────────────────┘
                       │
                       ▼
                [Final LLM Answer]
```

## Detailed description of core modules
### Rationale-Guided Filtering (core innovation)
- Training data generation:
  - x: query, d: retrieved document, r: rationale
  - Label: `ΔPPL = PPL(x) − PPL(x, d)`
  - Top 25% ΔPPL → "Helpful" (the document greatly lowers the perplexity of the rationale = useful)
  - Bottom 25% → "Not Helpful"
- SFT Flan-T5-large (770M) as a binary classifier
- At inference, apply the filter to each snippet → keep only Helpful ones

### Rationale-Based Query
- The base LLM generates a rationale with a CoT prompt (temperature=0)
- The rationale itself is the retrieval query (the initial query is used only in the reranker)
- Reason: "the initial query and the rationale exceeds the maximum length of MedCPT"
- Short queries are automatically expanded, and long queries have only the key reasoning steps extracted

### Balanced Retrieval
| Corpus | Scale | Characteristics |
|---|---|---|
| PubMed | large (MedCorp) | biomedical paper abstracts |
| PMC | large | open access full text |
| Medical Textbooks | small | standard textbooks such as StatPearls |
| Clinical Guidelines | small | up-to-date clinical practice guidelines |

- Retrieve an equal number from each corpus → mitigates MedCPT bias
- "balanced approach consistently outperforms others, highlighting the..." (Appendix Figure A3 caption)

## Input/Output
**Input**
- USMLE/AIIMS/MMLU-style multi-choice medical queries (4-5 options)

**Output**
- Correct-answer option + reasoning process (rationale)

## Example case
### COPD Exacerbation Case (MedQA, paper Figure 4 — quoted in full)
> **Initial Query (full case)**:
> > "A 62-year-old man presents to the emergency department with shortness of breath. … He feels as if he is unable to take a deep breath. The patient has a past medical history of COPD and a 44-pack-year smoking history. The patient has been admitted before for a similar presentation. Vitals: T 98.7°F, BP 177/118 mmHg, P 123/min, R 33/min, O2 sat 80% on room air. The patient is started on 100% oxygen, albuterol, ipratropium, magnesium, and prednisone. … He is still short of breath. Physical exam: bilateral wheezes, poor air movement.
> > Which of the following is the best next step in management? (A) BiPAP (B) Chest tube placement (C) Intubation (D) Needle Decompression"
>
> **Meerkat-7B without RAG (its own reasoning)**:
> > "...The presence of bilateral wheezes and poor air movement on physical examination suggests exacerbation of COPD with significant airflow obstruction. … (C) Intubation may be necessary for patients who are in respiratory failure and not responding to medical therapy… Therefore, the answer is (C) Intubation." ❌
>
> **RAG with rationale query (no filtering — distractor introduced)**:
> > Top-1 snippet: "...respiratory and hemodynamic signs of tension pneumothorax should be considered a medical emergency and addressed immediately, as this requires urgent needle decompression."
> > Model output: "The presence of bilateral wheezes could also be consistent with a severe COPD exacerbation, but the clinical picture is more suggestive of a tension pneumothorax… Therefore, the answer is (D) Needle decompression." ❌
>
> **RAG² with rationale-guided filtering**:
> > The filter model removes the tension pneumothorax snippet as Not-Helpful → the Top-3 snippet remains:
> > "...Non-invasive positive pressure ventilation is considered to be effective in reversing acute respiratory failure in selected patients with elevated carbon dioxide and no other life-threatening comorbidities…"
> > Model output: "These findings suggest an exacerbation of COPD with respiratory failure. … Non-invasive positive pressure ventilation can be used in COPD exacerbations to decrease the work of breathing and improve oxygenation. … Therefore, the answer is (A) BiPAP." ✓
>
> **Author interpretation (paper §5)**: "the initial error stems from the model's distraction by irrelevant information, but proper filtering lead to the correct diagnosis and management plan."

## Main evaluation results
**Table 2 — Accuracy on 3 medical QA benchmarks**
| Model + RAG | MedQA | MedMCQA | MMLU-Med | Avg |
|---|---|---|---|---|
| **Llama-3-8B-Instruct (base, 0-shot)** | 57.7 | 53.5 | 69.5 | 60.2 |
|   + MedCPT (k=1) | 55.3 | 51.3 | 65.8 | 57.5 |
|   + MedRAG | 56.4 | 56.6 | 69.2 | 60.7 |
|   + query2doc | 54.3 | 50.0 | 58.5 | 54.3 |
|   + Adaptive-RAG | 57.3 | 53.1 | 70.3 | 60.2 |
|   + InstructRAG-ICL (2-shot) | 55.5 | 55.7 | 71.9 | 61.8 |
|   **+ RAG² (Ours)** | **64.6** | **59.4** | **74.8** | **66.3** |
| **Meerkat-7B (base)** | 71.2 | 60.8 | 73.8 | 68.6 |
|   + MedRAG | 67.9 | 60.6 | 76.1 | 68.2 |
|   + Adaptive-RAG | 71.4 | 60.5 | 74.0 | 68.6 |
|   **+ RAG² (Ours)** | **75.6** | **63.0** | **78.7** | **72.4** |
| **GPT-4o (0-shot, base)** | 88.5 | 76.7 | 92.8 | 86.0 |
|   + MedRAG | 88.3 | 75.9 | 92.4 | 85.5 |
|   + Adaptive-RAG | 88.5 | 76.7 | 92.5 | 85.9 |
|   **+ RAG² (Ours)** | **91.1** | **77.2** | **92.5** | **86.9** |

**Key observations**
- Average improvement: Llama-3-8B **+6.1**, Meerkat-7B **+3.8**, GPT-4o **+0.9** (the smaller the model, the larger the RAG² effect)
- MMLU-Med has no training data, but the filter model trained on MedMCQA transfers (Llama +5.3, Meerkat +4.9)
- Some baseline RAGs degrade performance below base → "RAG frameworks do not always guarantee improved performance, especially in the medical domain" (§4.3)
- Filtering model ensemble + GPT-4o on MedQA → 91.6 (not included in the main table as it violates the single-pass principle)

## Key contributions
1. **Rationale-as-query**: bypasses the problem of patient information becoming noise in retrieval by replacing it with the rationale
2. **Perplexity-based automatic labeling**: solves the scarcity problem of medical annotation
3. **Balanced retrieval**: moves away from a PubMed-only approach to use 4 sources equally
4. **Small filtering model**: trainable on a single RTX 3090 GPU with only 770M Flan-T5

## Limitations
- Evaluated only in the closed-book setting (an environment without oracle documents)
- No MMLU-Med training data → transfer learning via MedMCQA (possible domain mismatch)
- The filter model is dependent on the base LLM → requires retraining when the backbone is changed (paper §6 Limitations)
- If the rationale is wrong, retrieval is wrong → though the authors claim "incorrect rationale make up only a small portion"

## Related links
- **ACL Anthology**: [https://aclanthology.org/2025.naacl-long.635/](https://aclanthology.org/2025.naacl-long.635/)
- **arXiv**: [https://arxiv.org/abs/2411.00300](https://arxiv.org/abs/2411.00300)
- **GitHub**: [https://github.com/dmis-lab/RAG2](https://github.com/dmis-lab/RAG2)
- **Author affiliations**: Korea University (DMIS Lab), Kyung Hee University, AIGEN Sciences
- **Comparison baselines**: MedCPT, MedRAG, query2doc, Adaptive-RAG, InstructRAG, Self-BioRAG
- **K×O classification**: K1.O1 (4 sources: PubMed/PMC/textbooks/guidelines) — a representative case of multi-source balanced retrieval
