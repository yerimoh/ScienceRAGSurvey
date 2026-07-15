---
title: "Patho-AgenticRAG: Towards Multimodal Agentic Retrieval-Augmented Generation for Pathology VLMs via Reinforcement Learning"
bib_key: DBLP:conf/aaai/ZhangGZZCZZYB26
year: 2026
domain: medical
type: Method
venue: AAAI 2026
paper_link: https://arxiv.org/abs/2508.02258
---
# Patho-AgenticRAG

> AAAI 2026 (vol. 40, no. 35, pp. 29921–29929) | Method | medical (pathology)
> Zhang, Guo, H.Zhang, P.Zhang, Chen, S.Zhang, Z.Zhang, Yi, Bu
> DBLP: `conf/aaai/ZhangGZZCZZYB26` · arXiv:2508.02258

## TL;DR
A multimodal RAG system that suppresses hallucination in pathology VLMs by combining a **200K+ page-scale knowledge base** built from over 600 authoritative pathology textbooks using **page-level multimodal embeddings (ColQwen2)** with a 4-stage decision-making agentic router (Qwen3-4B) trained via **GRPO reinforcement learning**. Achieves 78.32% on PathMMU-test and **60.00% on MedXpertQA (+38pp vs base Patho-R1-7B)**.

## Background
**Limitations of pathology VLMs** (excerpt from paper §2)
> "Reinforcement learning (RL) provides a promising paradigm for aligning the outputs of VLMs with clinical accuracy requirements, especially in high-risk medical domains where hallucinated descriptions can lead to severe consequences."

Problems with existing medical RAG:
- **Text-only RAG**: cannot reduce to text the **visual cues** that are core to pathology diagnosis, such as H&E staining patterns, cellular morphology, and spatial arrangement
- **Static RAG pipeline**: indiscriminately retrieves for every query → retrieving even for general common-knowledge questions ("What stain is used for nuclei?") increases latency and noise
- **Existing medical RAG such as MMed-RAG and MedRAG**: general-medicine-oriented and lacking pathology expertise, with retrieval targets limited to paper abstracts/journals

**How Patho-AgenticRAG is different**:
1. **Page-level multimodal indexing** (ColQwen2): represents a textbook page as a single integrated image-text vector → preserves visual patterns compared to text-only chunks
2. **Agentic Router**: dynamically decides per query whether to invoke RAG, the retrieval depth, the anatomical partition, and whether to activate the tissue classifier
3. **GRPO RL training**: fine-tunes with reinforcement learning the decision accuracy that SFT alone is insufficient for

## Construction Methodology

```
Step 1 — Building the pathology textbook knowledge base
  600+ authoritative pathology textbooks → ~300,000 pages collected
  Remove covers, prefaces, tables of contents, references → 200,000+ high-quality pages retained
  Partition into 19 anatomical categories:
    1. Bone and soft tissue        11. Histology
    2. Cytology                    12. Pediatric pathology
    3. Gastrointestinal (GI)       13. Skin
    4. Hematology                  14. Central nervous system (CNS)
    5. Infectious diseases         15. Female reproductive system
    6. Oral / Head / Neck (ENT)    16. Gross sampling
    7. Urinary / male reproductive 17. Immunohistochemistry (IHC)
    8. Breast                      18. Ophthalmology
    9. Endocrine system            19. Respiratory
   10. General pathology
  Embedding: ColQwen2 — integrated text+image multi-vector representation (page-level)
  Vector DB: Milvus + HNSW indexing, 150M+ vectors

Step 2 — Designing the Patho-Fusion reranking algorithm
  Combine the two similarity matrices produced by ColQwen2:
    - S_t ∈ R^{Nt × Nd} : query text token ↔ page document token
    - S_v ∈ R^{Nv × Nd} : query image patch ↔ page document patch
  Patho-Fusion Score (unique to this paper):
    Score = α · mean(max(S_t[i, :]))    ← CoPaLi-style text relevance
          + β · κ(S_v[i, :])              ← image kurtosis (concentrated visual attention)
  Design intent: ignore the average similarity of the visual modality,
            award bonus points only for "attention concentrated in a specific region"
            → penalize uniform (noisy) visual matching

Step 3 — Constructing the Agentic Router training data
  Select questions from the Quilt-VQA + Path-VQA training sets
  ┌─ Patho-R1-7B correct → 2,200 (learning signal: RAG unnecessary)
  └─ Patho-R1-7B incorrect → 2,200 (learning signal: RAG necessary)
  Total: 4,400 samples

  Using QwenMax, generate a ground-truth 4-stage decision path for each sample
  based on an expert-designed prompt:
    Decision 1: Whether to invoke RAG (Yes/No)
    Decision 2: Number of query decompositions (1, 2, 3, ...)
    Decision 3: Whether to activate the tissue-specific classifier
    Decision 4: Choose the retrieval anatomical partition (out of 19)

  Split into SFT 400 / GRPO RL 4,000

Step 4 — Router training (Qwen3-4B)
  Phase A — SFT: 400 samples, 3 epochs, LR=1e-5 (vision tower frozen)
  Phase B — GRPO: 4,000 samples, 3 epochs
                  actor LR=1e-6 / critic LR=1e-5
  Hardware: 8× NVIDIA RTX 4090

  Hierarchical reward function (max 4 points):
  ┌─ Decision 1 error: 0 points (early termination)
  ├─ Decision 1 correct (RAG unnecessary): 4 points (since it is a simple question)
  ├─ Decision 1 correct (RAG necessary): 1 point → Decision 2 correct: +1 point
  └─ Decision 3+4 correct: additional 1~2 points → maximum 4 points

Step 5 — Inference pipeline (Multi-agent Workflow)
  User input [image+text]
       ↓
  Agentic Router (Qwen3-4B)
    → RAG needed? No → Patho-R1-7B answers directly
    → RAG needed? Yes → decompose into per-candidate sub-tasks, choose anatomical partition
       ↓
  VRAG Agent — multi-turn retrieval + summarization
    - text-based retrieval (keyword per candidate)
    - Patho-Fusion reranking (text-doc × image-doc kurtosis)
    - iterative evidence sufficiency evaluation
       ↓
  Top-1 page evidence + original query + comparative instructions
       ↓
  Patho-R1-7B (specialized pathology VLM)
    → contrastive reasoning constrained to evidence
    → diagnosis + interpretable justification

Step 6 — 7 evaluation benchmarks
  ┌─────────────────────────┬──────────┬───────────────┐
  │ Benchmark                │ # items  │ Type          │
  ├─────────────────────────┼──────────┼───────────────┤
  │ PathMMU-test            │ 8,454    │ MC (5 subset) │
  │  └─ Atlas               │    799   │               │
  │  └─ EduContent          │  1,683   │               │
  │  └─ PathCLS             │  1,632   │               │
  │  └─ PubMed              │  2,787   │               │
  │  └─ SocialPath          │  1,553   │               │
  │ PathMMU-test-tiny       │  1,139   │ MC            │
  │ Path-VQA (YorN)         │  3,362   │ Yes/No        │
  │ Quilt-VQA               │    343   │ Yes/No        │
  │ MedXpertQA (pathology)  │     90   │ expert-curated│
  │ OmniMedVQA BRIGHT       │    890   │ VQA           │
  └─────────────────────────┴──────────┴───────────────┘
```

## Input / Output

**Input**: pathology image (H&E stained slide, etc.) + natural-language question (multiple-choice or Y/N)
**Output**: correct answer option + (optionally) evidence-grounded justification

**Knowledge base**: 200,000+ pathology textbook pages, indexed in Milvus + HNSW
**Vision encoder for routing**: Qwen3-4B (multimodal)
**Vision encoder for retrieval**: ColQwen2 (page-level multi-vector)
**Final VLM (inference engine)**: Patho-R1-7B (pathology-specialized)

## Example cases (paper Figure 2, Figure 3 — direct citation of the actual multimodal retrieval workflow)

### 🔬 Case 1: Multi-turn Retrieval — Monophasic Synovial Sarcoma (excerpt from Figure 2)

Figure 2 of the paper shows step by step how an actual query is processed inside the system.

> **Original Text Query (PathMMU multiple-choice question, Ground Truth: A)**:
> > "This image shows monophasic synovial sarcoma. What are its key histologic features?
> > A. Dense, uniform spindle cells with scant cytoplasm in short, intersecting fascicles.
> > B. Biphasic: glandular epithelium with spindle cell stroma.
> > C. Scattered adipocytes in fibrous stroma with atypia.
> > D. Large polygonal cells with coarse eosinophilic granules."
>
> **VRAG Agent Rewritten Search Query**:
> > "What are the histological features of monophasic synovial sarcoma?"
>
> **Multi-turn Retrieval results** (Patho-Fusion score):
> - "Cytologic appearance of Ewing sarcoma/PNET..." (score 0.6638 → text retrieval top1 but a distractor)
> - "Monophasic synovial sarcoma. The tumor..." (0.6558)
> - "...monophasic synovial sarcoma with..." (0.6190)
> - **Final Top1 (after Patho-Fusion rerank)**: "Synovial sarcoma with an adenocarcinoma-like appearance of the epithelial component." (0.6602, highest image attention concentration)
>
> **Sub-VRAG agent thought process (paper Figure 2)**: text retrieval incorrectly brought up *Ewing sarcoma* as top1, but the image kurtosis term reranked the *synovial sarcoma* page accurately → arriving at the correct answer A.

### 🧬 Case 2: Training-data labeling example (Appendix, excerpt of Q1-Q2)

Example ground-truth answers from the training data:
> **Q1**: "Histological features of invasive lobular carcinoma of the breast, including Indian-file pattern"
> **A1**: "Histological features of invasive lobular carcinoma of the breast include uniform small round tumor cells infiltrating the stroma in a single-file (Indian-file) arrangement and circumferentially around ducts in a target-like pattern."
>
> **Q2**: "How to differentiate ductal, papillary, and mucinous breast carcinoma histologically"
> **A2**: "Histologically, ductal carcinoma shows glandular, papillary, cribriform, or diffuse growth patterns, often forming nests, trabeculae, or cords. Papillary carcinoma is characterized by prom[inent papillary structures...]"

### 🧠 Case 3: RAG-skip decision guideline (excerpt from Appendix prompt)
> "If the question reflects common knowledge in pathology or histology, such as 'What stain is used for nuclei?' or 'Which cell secretes collagen?', a `<think>` is sufficient, and no tool needs to be called."

→ The router handles *common-knowledge-level questions* without invoking RAG, and only searches the vector DB for **rare/complex questions** (e.g., differentiating rare tumors).

## Main evaluation results

### Patho-Fusion reranking performance (Table 1)
Based on 100 expert-curated image-question-answer pairs:
| Method | Rec@1 | Rec@5 | MRR@5 | NDCG@5 | NDCG@20 |
|---|---:|---:|---:|---:|---:|
| CoPaLi (Text) | 0.640 | **0.900** | 0.734 | 0.804 | 0.796 |
| CoPaLi (Image) | 0.060 | 0.220 | 0.112 | 0.174 | 0.359 |
| WeiMoCIR | 0.060 | 0.200 | 0.102 | 0.163 | 0.342 |
| **Patho-Fusion (ours)** | **0.720** | 0.880 | **0.777** | **0.824** | **0.827** |

### PathMMU Multiple-Choice QA (Table 2 excerpt)
| Model | PathMMU-test | PathMMU-test-tiny |
|---|---:|---:|
| InternVL2-8B | 43.68 | 44.86 |
| InternVL2.5-8B | 50.06 | 50.62 |
| InternVL3-8B | 54.07 | 50.80 |
| Llama-3.2V-11B-cot | 51.81 | 45.45 |
| Qwen2.5VL-7B | 41.18 | 43.20 |
| Patho-R1-7B (base) | 75.34 | 66.43 |
| **Patho-AgenticRAG** | **78.32** | **70.96** |
| Improvement (vs. base) | **+2.98pp** | **+4.53pp** |

Consistently SOTA across the detailed subsets (Atlas / EduContent / PathCLS / PubMed / SocialPath) as well.

### Yes/No VQA and expert QA (Table 3, direct citation from body §4)
> "Patho-AgenticRAG achieves +13.37% improvement on Quilt-VQA (75.80% vs. 64.72%) and +38.00% on MedXpertQA (60.00% vs. 22.00%) over Patho-R1. The largest margin appears on MedXpertQA, highlighting the importance of retrieval-augmented reasoning in knowledge-intensive tasks. On OmniMedVQA Bright Challenge, the model improves from 70.79% (Patho-R1) to 90.11%, a +19.32% increase."

| Model | Path-VQA | Quilt-VQA | MedXpertQA | OmniMedVQA Bright |
|---|---:|---:|---:|---:|
| InternVL2.5-8B | 60.06 | 49.78 | 64.78 | 22.22 |
| Patho-R1-7B (base) | 64.72 | 70.79 | 22.00 | 46.97 |
| **Patho-AgenticRAG** | **75.80** | **90.11** | **60.00** | **80.34** |
| Improvement (vs. base) | **+11.08pp** | **+19.32pp** | **+38.00pp** | **+33.37pp** |

### Ablation — router training strategy (based on Quilt-VQA)
| Configuration | Quilt-VQA |
|---|---:|
| Patho-R1 (no router, no RAG) | 64.72% |
| +Qwen3 (raw router) | 60.93% (actually decreases — overcalling RAG) |
| +GRPO4k only | 60.93% |
| +SFT4k → GRPO400 | marginal improvement |
| **+SFT400 → GRPO4k** | **75.80%** (+14.87% over GRPO-only) |

→ Claim in paper §4:
> "These results suggest that SFT400 provides an effective 'cold start' that guides the policy initialization without compromising flexibility or generalization."

## Limitations
- **Evaluation limited to closed-ended tasks** — mostly Yes/No and multiple-choice, with open-ended diagnostic reasoning (differential diagnosis) not evaluated.
- **Knowledge base is textbook-based** → latest clinical guidelines and research papers are not reflected (e.g., new drugs within the last year).
- **Domain imbalance in textbook coverage** — some of the 19 categories may rely on a small number of books.
- **Retrieval latency and infrastructure cost not reported**: the 150M+ vector Milvus index + multi-turn agentic calls raise latency concerns for practical deployment.
- **Generalization beyond the pathology domain not verified** — not demonstrated whether the same pipeline works in radiology, ophthalmology, or electrocardiography.
- **Stability of GRPO training**: the ablation shows cases where GRPO-only *decreases* performance below base — strong dependence on the SFT cold-start.
- **The number of multi-turn calls by the VRAG Agent is variable** → hard to guarantee consistent latency.

## Related links
- **Paper (arXiv)**: [arXiv:2508.02258](https://arxiv.org/abs/2508.02258)
- **AAAI 2026**: vol. 40, no. 35, pp. 29921–29929
- **GitHub**: [Wenchuan-Zhang/Patho-AgenticRAG](https://github.com/Wenchuan-Zhang/Patho-AgenticRAG)
- **DBLP**: [conf/aaai/ZhangGZZCZZYB26](https://dblp.org/rec/conf/aaai/ZhangGZZCZZYB26)
- **base model**: [Patho-R1-7B (Hugging Face)](https://huggingface.co/blackshow/Patho-R1)
- **Retrieval encoder**: [ColQwen2 (vidore)](https://huggingface.co/vidore/colqwen2-v1.0)
