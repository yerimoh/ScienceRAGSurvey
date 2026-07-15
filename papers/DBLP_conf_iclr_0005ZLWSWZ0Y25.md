---
title: "MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models"
bib_key: "DBLP:conf/iclr/0005ZLWSWZ0Y25"
year: 2025
domain: medical
type: Method
venue: ICLR 2025
paper_link: https://arxiv.org/abs/2410.13085
---
# MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models

> ICLR | 2025 | Method | medical

## TL;DR
A versatile RAG system in which a medical LVLM, rather than being tied to a single retriever, automatically identifies the imaging domain (radiology, ophthalmology, pathology) to select a domain-specific retriever, blocks noise through adaptive top-k truncation, and simultaneously corrects **cross-modality misalignment** and **ground truth misalignment** via RAG-based DPO preference learning. It reports an average **factual accuracy +43.8%** across 5 datasets × 3 medical imaging domains.

## Background
**Limitations of existing Med-LVLMs (paper §1, §3)**
- Med-LVLMs frequently produce **factual hallucination** where the text output contradicts the input image
- Existing medical RAG (RULE, FactMM-RAG) is specialized to a single dataset (e.g., chest X-ray) only → fails to generalize to ophthalmology and pathology
- Introducing RAG causes two new misalignments
  - **Cross-modality misalignment**: the "Copy-Reference" phenomenon where the model ignores the image and merely copies the retrieved text
  - **Overall misalignment**: the "Over-Reliance" phenomenon of following retrieved results even when they are wrong

**Why it is needed**
- Diagnostic errors are directly linked to patient safety → reliability is critical
- Operating diverse imaging modalities within a single system is required for clinical applicability
- Author quote: "MMed-RAG can achieve an average improvement of **43.8%** in the factual accuracy of Med-LVLMs" (Abstract)
- "achieving improvements of **18.5%** and **69.1%** on Medical VQA and report generation tasks, respectively" (§1)

## Architecture
```
                    [Medical Image (xv) + Clinical Query (xt)]
                                    │
                                    ▼
                  ┌─────────────────────────────────┐
                  │   ① Domain-Aware Retrieval      │
                  │   ─────────────────────────     │
                  │   Domain Identification         │
                  │   (BiomedCLIP / ResNet-50 +     │
                  │    BioClinicalBERT, InfoNCE)    │
                  │       │                         │
                  │       ▼                         │
                  │   Domain label ∈ {Radiology,    │
                  │     Pathology, Ophthalmology}   │
                  │       │                         │
                  │       ▼                         │
                  │   Domain-specific Retriever     │
                  │   (a separate model trained     │
                  │    per domain)                  │
                  └────────────┬────────────────────┘
                               │
                  ┌────────────▼────────────────────┐
                  │   ② Adaptive Retrieved Context  │
                  │      Selection                  │
                  │   ─────────────────────────     │
                  │   Similarity score ratio of     │
                  │   Top-k results                 │
                  │   log(S_i / S_{i+1}) analysis   │
                  │   → truncate k just before the  │
                  │     score drops sharply         │
                  │     (Gap Statistic based)       │
                  └────────────┬────────────────────┘
                               │
                  ┌────────────▼────────────────────┐
                  │   ③ Med-LVLM + RAG-PT (DPO)     │
                  │   ─────────────────────────     │
                  │   3-stage preference data:      │
                  │   ①Direct-Copy-Homework→correct │
                  │   ②Cannot-Solve-by-Self→correct │
                  │   ③Wrong-Homework-Interference  │
                  │       →correct                  │
                  └────────────┬────────────────────┘
                               │
                               ▼
                        [Factual answer]
```

## Detailed Description of Core Modules
### Domain-Aware Retrieval
- Instead of a single general-purpose retriever, deploys per-domain expert retrievers (similar to MoE but with domain routing)
- The image is first passed through the domain identification module → only the appropriate retriever is invoked
- Each retriever is trained with **InfoNCE contrastive loss** on ResNet-50 (vision) + BioClinicalBERT (text)
- Large margin advantage over a single retriever on Recall@1, R@5 (Table 20)

### Adaptive Truncation
- Exploits the trend that the similarity score decreases as the retrieval result rank goes deeper
- When `log(S_i / S_{i+1})` exceeds a certain threshold, results beyond that point are regarded as noise and truncated
- Instead of a fixed k, selects a different k per query → blocks noise insertion

### RAG-Based Preference Tuning (RAG-PT)
Three preference pairs are designed (paper Figure 1):
1. **"Think it by Self"** — outputting the correct answer with an irrelevant image + the correct retrieved text = dispreferred (the case of getting it right by copying without looking at the image → negative reinforcement)
2. **"Learn How to Copy"** — unable to solve by self-reasoning but outputting the correct answer using the retrieved information = preferred (the case of making good use of retrieval → positive reinforcement)
3. **"Avoid Wrong Homework"** — outputting the correct answer from the original image despite wrong retrieval = preferred (the case of overcoming interference from retrieval noise → positive reinforcement)

DPO loss:
> L_DPO(πθ; πref) = −E[log σ(α log(πθ(yw|x)/πref(yw|x)) − α log(πθ(yl|x)/πref(yl|x)))]  (Eq. 1)

## Input/Output
**Input**
- xv: medical image (chest X-ray / retinal photo / pathology slide / OCT)
- xt: clinical query (e.g., "Is there any focal airspace opacity present?")

**Output**
- Yes/No diagnosis, free-text report (report generation), or multi-choice answer

## Example Cases
### Example ① — Chest X-ray VQA (paper Figure 4, left)
> **Question**: "Can focal airspace consolidation be seen on the image?"
>
> **Reference (Ground Truth)**:
> > "No, focal airspace consolidation cannot be seen on the image."
>
> **LLaVA-Med-1.5 (baseline) output**:
> > "Yes, there seems to be a focal airspace consolidation. The heart is normal in size… There appears to be a focal airspace consolidation on the right side of the lung…"
>
> **MMed-RAG (Ours) output**:
> > "No, focal airspace consolidation cannot be seen on the image."
>
> **Interpretation**: LLaVA-Med hallucinated additional irrelevant "right side of the lung" information → MMed-RAG faithfully answers No based on the image. Attention map analysis shows that MMed-RAG assigns strengthened attention to the lung region (red box).

### Example ② — Operational flow (Figure 1)
> **Question**: "Is there any focal airspace opacity present?"
>
> 1) Input chest X-ray → Domain Identification → "Radiology"
> 2) Radiology Retriever → Top-k reports from the IU-Xray report corpus
> 3) Adaptive-k: after analyzing the similarity graph, keep only k=3
> 4) Med-LVLM combines reports + image → final answer

## Key Evaluation Results
**Table 1 — Medical VQA Accuracy (LLaVA-Med-1.5 backbone, %)**
| Method | IU-Xray | MIMIC-CXR | Harvard-FairVLMed | Quilt-1M | PMC-OA |
|---|---|---|---|---|---|
| LLaVA-Med-1.5 (base) | 75.47 | 75.79 | 63.03 | 62.80 | 59.28 |
| + Greedy decoding | 76.88 | 78.32 | 82.54 | 64.72 | 58.61 |
| + DoLa | 78.00 | 81.35 | 76.87 | 63.47 | 57.71 |
| + OPERA | 70.59 | 69.34 | 71.41 | 60.51 | 55.32 |
| + VCD | 68.99 | 70.89 | 65.88 | 61.43 | 55.10 |
| + MedDr | 83.33 | 55.16 | 70.17 | 68.15 | 59.97 |
| + FactMM-RAG | 84.51 | 77.58 | 83.67 | 69.25 | 60.49 |
| + RULE | 87.84 | 83.92 | 87.12 | 68.97 | 61.41 |
| **+ MMed-RAG (Ours)** | **89.54** | 83.57 | **87.94** | **72.95** | **64.54** |

**Table 1 — F1 (selected)**
| Method | IU-Xray | MIMIC-CXR | PMC-OA |
|---|---|---|---|
| LLaVA-Med-1.5 | 64.04 | 80.49 | 71.98 |
| RULE | 78.00 | 87.49 | 70.36 |
| **MMed-RAG** | **80.72** | **88.49** | **73.09** |

**Contribution summary (Abstract + §1)**
- Average factual accuracy improvement: **+43.8%**
- **+18.5%** over the base Med-LVLM on Medical VQA
- **+69.1%** over the base on report generation
- Table 14: both Copy-Reference Rate and Over-Reliance Rate significantly decreased (first attempt at quantitative measurement)

## Key Contributions
1. **Versatile multimodal RAG** — covers all domains of radiology/pathology/ophthalmology with a single system
2. **Theoretical guarantee** — proof based on mild assumptions for mitigating cross-modality and overall misalignment (§4)
3. **Introduction of Copy-Reference / Over-Reliance diagnostic metrics** — quantifies the side effects brought about by RAG

## Limitations
- As domains increase, the training cost of per-domain retrievers grows linearly; a "single general-purpose retriever" is still difficult to realize (paper §6 conclusion)
- If the base Med-LVLM has weak few-shot learning ability, the RAG-PT effect is limited
- Misclassification at the Domain Identification stage leads to selecting the wrong retriever → cascade error
- Constructing preference pairs for DPO training requires an external LLM such as GPT-4 (prompt in Table 9)

## Related links
- **Paper**: [ICLR 2025](https://openreview.net/forum?id=...)
- **arXiv**: [arXiv:2410.13085](https://arxiv.org/abs/2410.13085)
- **GitHub**: [https://github.com/richard-peng-xia/MMed-RAG](https://github.com/richard-peng-xia/MMed-RAG)
- **Authors**: UNC-Chapel Hill, Brown, CMU, Rutgers, Washington, Stanford (Peng Xia, Kangyu Zhu, Haoran Li, Tianze Wang, Weijia Shi, Sheng Wang, Linjun Zhang, James Zou, Huaxiu Yao)
- **Evaluation datasets**: IU-Xray, MIMIC-CXR (radiology), Harvard-FairVLMed (ophthalmology, OCT), Quilt-1M (pathology), PMC-OA (pathology)
- **K×O classification**: K1.O1 (medical image corpus retrieval) — the retrieval target is not text but image-report pairs
