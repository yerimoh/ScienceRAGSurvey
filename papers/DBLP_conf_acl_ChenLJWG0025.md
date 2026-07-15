---
title: "Towards Omni-RAG: Comprehensive Retrieval-Augmented Generation for Large Language Models in Medical Applications"
bib_key: "DBLP:conf/acl/ChenLJWG0025"
year: 2025
domain: medical
type: Method
venue: ACL 2025 (Vienna, Austria), pp. 15285–15309
paper_link: https://aclanthology.org/2025.acl-long.742/
---
# Omni-RAG: Comprehensive Multi-Source RAG for Medical Applications via Source Planning Optimisation (SPO)

> ACL 2025 | 2025 | Method | medical

## TL;DR
A **Source Planning Optimisation (SPO)** approach that builds **MedOmniKB**, which simultaneously covers 8 broad medical QA datasets (Reasoning/Research/Clinical/Open-ended) with 5 heterogeneous knowledge sources — **Book, Guideline, Research(PubMed), Wiki, Graph(UMLS+DrugBank)** — and, using an expert LLM (Qwen2.5-72B-AWQ), trains a small planner (Qwen2.5-7B) via SFT+DPO to learn "which source to query, with what query, and how many times." With an average accuracy gain of **+4.6 ~ +7.0**%, it surpasses SOTA baselines (Reflexion, SeRTS, Trainable Planning, RaFe) across the board.

## Background
**Limitations of existing medical RAG (paper §1)**
- Existing systems rely on a single source, either PubMed or Wikipedia
- Although the optimal source differs by query type (diagnosis, drug interaction, latest research, consumer health), they use the same retrieval strategy
- The model is not aligned with expectations about "what exists in each source" → inappropriate source calls
- Author quote: "Existing methods typically treat all sources uniformly, using the original question to retrieve without tailoring the search strategy to different sources" (§1)

**Why it is needed**
- Medical AI is directly tied to patient safety → "correctness and trustworthiness are paramount" (§1)
- Clinical applicability requires covering medical scenarios such as diagnosis, clinical decision-making, research knowledge, and consumer health
- A single source misses the long-tail (rare diseases, latest drugs, clinical guideline updates)

## Construction Methodology
### Step 1 — Building MedOmniKB with 5 sources (paper §3)
**Unstructured Sources**
| Source | #Docs | #Chunks | #Words/Chunk |
|---|---|---|---|
| **Book** (textbooks) | 27.7k | 13.1M | 150.1 |
| **Guideline** (clinical guidelines) | 45.7k | 647.7k | 106.7 |
| **Research** (PubMed 2024 baseline) | 25.3M | 48.0M | 128.7 |
| **Wiki** (English Wikipedia) | 6.4M | 29.7M | 112.1 |

**Structured Source**
| Source | #Concepts | #Definitions | #Relations |
|---|---|---|---|
| **Graph** (UMLS + DrugBank) | 1.7M | 317.9k | 2.9M |

- Book: 18,182 PDFs (medicine, surgery, radiology) + StatPearls + MedRAG textbooks
- Guideline: 45,679 articles from 13 guideline sources
- Research: full 2024 PubMed snapshot (title+abstract)
- Wiki: processed HuggingFace English Wikipedia
- Graph: UMLS Metathesaurus Full Subset + DrugBank's description/indication/pharmacodynamics/absorption/drug interaction integrated into node definitions. Stored in SQLite (avoiding online UMLS API latency)

**Retrieval infrastructure**
- Unstructured: MedCPT-article-encoder → Qdrant vector DB
- Graph: extract concept definitions + 1-hop relations from SQLite, then filter with a reranker

### Step 2 — Source Planning Optimisation (SPO, paper §4, Figure 2)
```
       ┌─────────────────────────────────────────────────┐
       │  Training Q (with gold answer)                  │
       └────────────────────┬────────────────────────────┘
                            │
                            ▼
       ┌─────────────────────────────────────────────────┐
       │  ① Planning Exploration                         │
       │  ───────────────────────────────                │
       │  Expert LLM (Qwen2.5-72B-Instruct-AWQ)          │
       │  → generate multiple queries per source         │
       │     Plan P = {(i, j, q_ij)} where i=source,     │
       │              j=query index                      │
       │     Per-source queries ≤ 4 (context limit)      │
       └────────────────────┬────────────────────────────┘
                            │
                            ▼
       ┌─────────────────────────────────────────────────┐
       │  ② Planning Judging                             │
       │  ───────────────────────────────                │
       │  retrieve with each query → document d_ij       │
       │  Expert LLM judges "does this document          │
       │  support the gold answer?"                      │
       │  → positive plan (support) / negative plan      │
       └────────────────────┬────────────────────────────┘
                            │
                            ▼
       ┌─────────────────────────────────────────────────┐
       │  ③ Planning Learning                            │
       │  ───────────────────────────────                │
       │  small planner (Qwen2.5-7B) on positive plans:  │
       │   (1) SFT (supervised fine-tuning)              │
       │   (2) DPO with (positive, negative) pairs       │
       └────────────────────┬────────────────────────────┘
                            │
                            ▼
                  [Trained Planner Mθ]
                            │
       (Inference) ─────────┼─────────
                            ▼
       For new question x → 5 sources × ≤4 queries each
                            ▼
              MedOmniKB → Top-k documents D
                            ▼
                  Reader (frozen Qwen/Llama/Mistral)
                            ▼
                       Answer y
```

## Input/Output
**Input**: medical query x (MCQ or open-ended)

**Output**: Source plan P + final answer y. P takes the following form:
> `<book>seborrheic dermatitis symptoms and signs; greasy yellow scales skin condition; ...</book>`
> `<guideline>clinical approach to infantile skin conditions; pediatric dermatology best practices; ...</guideline>`
> `<research>recent studies on seborrheic vs atopic dermatitis; pathophysiology of greasy scale formation; ...</research>`
> `<wiki>atopic dermatitis; infant skin rashes; allergic contact dermatitis triggers; ...</wiki>`
> `<graph>Psoriasis, genetic transmission and skin manifestations; Skin scaling, underlying dermatological conditions; ...</graph>`

## Example cases
### Example ① — Seborrheic Dermatitis (paper Figure 2 — core case study)
> **Original Question (MedQA-style MCQ)**:
> > "A 3-month-old boy is brought to the physician by his parents for the evaluation of a rash on his scalp and forehead. The parents report that the rash has been present for several weeks. They state that the rash is sometimes red and scaly... Some patches are covered by greasy yellow scales. Which of the following is the most likely diagnosis?
> > A. Atopic dermatitis  B. Seborrheic keratosis  C. Allergic contact dermatitis  D. Seborrheic dermatitis"
>
> **Gold Answer**: D. Seborrheic dermatitis
>
> **SPO Planner output (5-source plan)**:
> > `<book>seborrheic dermatitis symptoms and signs; greasy yellow scales skin condition; ...</book>`
> > `<guideline>clinical approach to infantile skin conditions; pediatric dermatology best practices; ...</guideline>`
> > `<research>recent studies on seborrheic vs atopic dermatitis; pathophysiology of greasy scale formation; ...</research>`
> > `<wiki>atopic dermatitis; infant skin rashes; allergic contact dermatitis triggers; ...</wiki>`
> > `<graph>Psoriasis, genetic transmission and skin manifestations; Skin scaling, underlying dermatological conditions; ...</graph>`
>
> **Planning Judging stage comparison**:
> - "Support Gold Answer" plan → reinforced as positive in DPO
> - "Not Support Gold Answer" plan → suppressed as negative
>
> **Result**: Pulling information from different semantic layers across the 5 sources leads to deriving the correct answer D. A single-source PubMed RAG might only pull general "infant skin rash" information and confuse D vs A

## Key evaluation results
**Table 4 — Accuracy on 8 datasets, Reader = Frozen Qwen2.5-7B-Instruct**
| Method | MedQA | MedMCQA | MMLU-Med | PubMedQA | BioASQ | SEER | DDXPlus | MIMIC-IV | **Avg** |
|---|---|---|---|---|---|---|---|---|---|
| No Retrieval | 60.80 | 56.17 | 76.95 | 34.60 | 74.81 | 51.00 | 42.80 | 58.50 | 56.95 |
| Original Question | 62.45 | 63.25 | 80.90 | 47.00 | 89.00 | 58.40 | 42.80 | 57.90 | 62.71 |
| Query2Doc | 62.92 | 66.42 | 80.26 | 46.40 | 88.24 | 58.80 | 42.40 | 56.90 | 62.79 |
| Frozen 72B Prompting | 72.11 | 65.33 | 81.73 | 53.80 | 89.64 | 57.10 | 48.70 | 62.00 | 66.30 |
| Reflexion (72B) | 73.13 | 66.00 | 79.06 | 52.60 | 89.64 | 57.90 | 49.40 | 62.60 | 66.29 |
| SeRTS (72B) | 70.70 | 66.83 | 82.55 | 55.60 | 90.03 | 57.10 | 51.20 | 62.50 | 67.06 |
| Trainable Planning (7B) | 72.03 | 66.42 | 82.19 | 54.80 | 89.90 | 57.20 | 46.40 | 60.30 | 66.16 |
| RaFe Planning (7B) | 70.86 | 66.50 | 78.70 | 53.40 | 89.77 | 55.20 | 50.30 | 63.70 | 66.05 |
| **SPO Planning (7B, Ours)** | **76.98** | **71.08** | **85.49** | **60.20** | 89.77 | **61.90** | **52.40** | **69.60** | **70.93** |

**Table 4 (cont.) — Reader = Frozen Llama3.1-8B**
| Method | MedQA | MedMCQA | MMLU-Med | PubMedQA | BioASQ | SEER | DDXPlus | MIMIC-IV | **Avg** |
|---|---|---|---|---|---|---|---|---|---|
| No Retrieval | 65.99 | 59.50 | 76.58 | 56.20 | 81.97 | 57.00 | 38.80 | 58.60 | 61.83 |
| Original Question | 60.57 | 57.50 | 72.18 | 74.20 | 87.47 | 57.60 | 39.00 | 58.10 | 63.33 |
| Frozen 72B Prompting | 71.17 | 62.08 | 75.94 | 71.40 | 89.00 | 57.50 | 41.10 | 58.60 | 65.85 |
| SeRTS | 71.88 | 63.25 | 77.13 | 71.60 | 89.51 | 57.00 | 42.90 | 60.10 | 66.67 |
| **SPO Planning (Ours)** | **77.45** | **69.25** | **78.97** | **75.60** | 89.64 | **60.70** | **45.70** | **64.10** | **70.18** |

**Key observations**
- The SPO 7B planner surpasses frozen 72B prompting and SeRTS·Reflexion (both 72B)
- Qwen2.5-7B reader: average 56.95 (No-RAG) → 70.93 (SPO) = **+13.98** vs baseline
- **+4.6 ~ +7.0%** average improvement over SOTA baselines
- Largest gains: PubMedQA (+5.6 over SeRTS, 60.20 vs 55.60), MIMIC-IV (+7.1, 69.60 vs 62.50)

## Key contributions
1. **MedOmniKB** — a 5-source (Book/Guideline/Research/Wiki/Graph) integrated medical knowledge base, of a fundamentally different scale than existing single-source KBs (Table 1)
2. **Source Planning Optimisation (SPO)** — trains the planner in 3 stages, Plan Exploration → Plan Judging → Plan Learning; secures training data without gold annotation via the LLM-as-judge paradigm
3. **SOTA with a small planner** — the 7B planner surpasses 72B baselines on 11 datasets (efficiency)
4. **5-source structured plan output** — explicit source-aware queries in the `<book>...</book><guideline>...</guideline>...` format

## Limitations
- All 5 sources are of the K1 (literature) and K2 (curated DB) families — K4 (personal/clinical experience) is not included
- MedOmniKB construction is costly (processing 25.3M PubMed entries)
- SPO training requires repeated inference by the expert LLM (72B) → increased training cost
- Adaptability to out-of-distribution data (outside the source distribution) requires additional validation (paper §6)
- Per-source queries limited to 4 → may be insufficient for complex multi-hop queries

## Related links
- **Paper**: [ACL Anthology 2025.acl-long.742](https://aclanthology.org/2025.acl-long.742/)
- **arXiv preprint**: [arXiv:2501.02460](https://arxiv.org/abs/2501.02460)
- **Code/project**: [GitHub: Jack-ZC8/Omni-RAG-Medical](https://github.com/Jack-ZC8/Omni-RAG-Medical)
- **Author affiliations**: Shanghai Jiao Tong University / Fudan University / Shanghai AI Lab
- **Evaluation datasets (11)**: MedQA, MedMCQA, MMLU-Med, PubMedQA, BioASQ, SEER, DDXPlus, MIMIC-IV-ED, LiveQA, MedicationQA, ExpertQA-Biomed (total 24,199 train / 4,837 dev / 8,248 test)
- **Comparison baselines**: No Retrieval, Original Question, Query2Doc, Reflexion, SeRTS, Trainable Planning, RaFe Planning
- **K×O classification**: K1.O1 (literature+guidelines) + K2.O1 (UMLS+DrugBank KG) — a representative case of the multi-source K1+K2 integration pattern
