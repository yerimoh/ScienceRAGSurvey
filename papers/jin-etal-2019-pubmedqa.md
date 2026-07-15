---
title: "PubMedQA: A Dataset for Biomedical Research Question Answering"
bib_key: "jin-etal-2019-pubmedqa"
year: 2019
domain: medical
type: benchmark
venue: EMNLP-IJCNLP 2019
paper_link: https://aclanthology.org/D19-1259/
---
# PubMedQA: A Dataset for Biomedical Research Question Answering

> EMNLP-IJCNLP 2019 | Benchmark | medical

## TL;DR
A yes/no/maybe QA benchmark constructed automatically/manually from PubMed abstracts that have a **question-form title + structured abstract**. With a 3-way split of **PQA-L (1k expert-annotated) + PQA-U (61.2k unannotated) + PQA-A (211.3k automatically generated)**, it is the first biomedical QA dataset in which quantitative reasoning is essential.

---

## How It Was Built (Construction Methodology)

```
Step 1 — Extract PubMed candidates (25M references)
  └─ Filter 1: title contains a question mark (?) → ~760k articles
  └─ Filter 2: has a structured abstract (Methods/Results/Conclusions) → ~120k
  └─ Result: pre-PQA-U (candidates potentially answerable by yes/no/maybe)

Step 2 — Build instance 4-tuples
  From each article:
  ┌────────────────┬───────────────────────────────────────┐
  │ Question       │ original paper title (e.g. "Do statins...?")│
  │ Context        │ structured abstract − Conclusion section │
  │ Long Answer    │ Conclusion section itself             │
  │ Yes/No/Maybe   │ single label summarizing the Long Answer │
  └────────────────┴───────────────────────────────────────┘

Step 3 — PQA-L 1,000 instances (expert-annotated, Algorithm 1)
  └─ Of 2,173 candidates, 1,091 (50.2%) were removed as not answerable by yes/no/maybe
     (wh-question / multiple-choice format, etc.)
  └─ Two M.D. candidate annotators:
     · Annotator 1: question + context + long answer → label (reasoning-free)
     · Annotator 2: question + context only → label (reasoning-required)
     · both labels identical → accepted / disagreement → resolved by consensus (instance removed if not possible)
  └─ 500 = 10-fold cross-validation, remaining 500 = test set

Step 4 — PQA-U 61.2k (unannotated, for semi-supervised learning)
  yes/no/maybe-answerable instances from pre-PQA-U not included in PQA-L.
  Identified by rule-based filters (removing wh-words / multi-entity selection)
  → validated with 93% agreement against Annotator 1

Step 5 — PQA-A 211.3k (automatically generated, for pre-training)
  └─ Statement title (POS tag NP-(VBP/VBZ), Stanford CoreNLP)
  └─ Converted into a question by adding a copula/auxiliary verb
     · "Statins reduce AF." → "Do statins reduce AF?"
  └─ Yes/No assigned automatically from the VB's negation status (no Maybe)
  └─ 200k = training / 11.3k = validation
```

---

## Dataset Statistics

| Item | PQA-L | PQA-U | PQA-A |
|---|---|---|---|
| Number of QA pairs | 1.0k | 61.2k | 211.3k |
| Yes (%) | **55.2** | – | **92.8** |
| No (%) | **33.8** | – | **7.2** |
| Maybe (%) | **11.0** | – | 0.0 |
| Avg. question length (tok) | 14.4 | 15.0 | 16.3 |
| Avg. context length (tok) | 238.9 | 237.3 | 238.0 |
| Avg. long answer length (tok) | 43.2 | 45.9 | 41.0 |

---

## Example Item Format (paper Figure 1, Sakamoto et al. 2011, verbatim)

### Representative instance (PQA-L, Annals of Thoracic & Cardiovascular Surgery 17(4):376-382)
> **Question.** *"Do preoperative statins reduce atrial fibrillation after coronary artery bypass grafting?"*
>
> **Context.**
> *(Objective)* Recent studies have demonstrated that statins have pleiotropic effects, including anti-inflammatory effects and atrial fibrillation (AF) preventive effects [...]
> *(Methods)* 221 patients underwent CABG in our hospital from 2004 to 2007. 14 patients with preoperative AF and 4 patients with concomitant valve surgery [...]
> *(Results)* The overall incidence of postoperative AF was 26%. Postoperative AF was significantly lower in the **Statin group compared with the Non-statin group (16% versus 33%, p=0.005)**. Multivariate analysis demonstrated that independent predictors of AF [...]
>
> **Long Answer.** *(Conclusion)* "Our study indicated that preoperative statin therapy seems to reduce AF development after CABG."
>
> **Answer:** **yes**

→ The key supporting fact is the statistical comparison in Results (16% vs 33%, p=0.005). The reasoning type is *Inter-group comparison* (the most common in PQA-L, at 57.5%).

### Additional verbatim question examples (paper body Table, p.5)

**Type 1: Does a factor influence the output? (36.5%)**
> · *"Does reducing spasticity translate into functional benefit?"*
> · *"Does ibuprofen increase perioperative blood loss during hip arthroplasty?"*

**Type 2: Is a therapy good/necessary? (26.0%)**
> · *"Should circumcision be performed in childhood?"*
> · *"Is external palliative radiotherapy for gallbladder carcinoma effective?"*

**Type 3: Is a statement true? (18.0%)**
> · *"Sternal fracture in growing children: a rare and often overlooked fracture?"*
> · *"Xanthogranulomatous cholecystitis: a premalignant condition?"*

**Type 4: Is a factor related to the output? (18.0%)**
> · *"Can PRISM predict length of PICU stay?"*
> · *"Is trabecular bone related to primary stability of miniscrews?"*

### Examples of supporting evidence by Reasoning Type (paper body, p.5–6 verbatim)

> **Inter-group comparison (57.5%)**
> > *"Postoperative AF was significantly lower in the Statin group compared with the Non-statin group (16% versus 33%, p=0.005)."*

> **Interpreting subgroup statistics (16.5%)**
> > *"57% of patients were of lower socioeconomic status and they had more health problems, less functioning, and more symptoms."*

> **Interpreting (single) group statistics (16.0%)**
> > *"A total of 4 children aged 5-14 years with a sternal fracture were treated in 2 years, 2 children were hospitalized for pain management..."*

> **No interpretations (numbers only, 21.0%)**
> > *"30-day mortality was 12.4% in those aged<70 years and 22% in [...] those ≥70 years"*

---

## Question/Reasoning Type Distribution (analysis of 200 PQA-L samples)

| Question type | % | Example |
|---|---|---|
| Does a factor influence the output? | 36.5 | "Does ibuprofen increase perioperative blood loss?" |
| Is a therapy good/necessary? | 26.0 | "Should circumcision be performed in childhood?" |
| Is a statement true? | 18.0 | "Sternal fracture in growing children: a rare and overlooked fracture?" |
| Is a factor related to the output? | 18.0 | "Can PRISM predict length of PICU stay?" |

| Reasoning type | % |
|---|---|
| Inter-group comparison | **57.5** |
| Interpreting subgroup statistics | 16.5 |
| Interpreting (single) group statistics | 16.0 |
| **Proportion requiring quantitative content reasoning** | **96.5%** |

---

## Main Evaluation Results (on the 500 PQA-L test instances)

| Model | Accuracy | Macro F1 |
|---|---|---|
| Majority baseline | 55.2% | – |
| BioBERT multi-phase fine-tuning + LongAnswer BoW supervision | **68.1%** | 52.8% |
| Human single performance | 78.0% | 72.2% |

**Key finding:** Even the best-performing model is **9.9%p lower** than humans → quantitative reasoning remains an unsolved challenge for RAG / LLMs.

---

## Limitations
- **Clinical study topic skew**: In the MeSH distribution, Pregnancy Outcome / Socioeconomic Factors / Risk Assessment / Survival Analysis and others are over-represented relative to general PubMed (p < 0.05, two-proportion z-test).
- **PQA-A has no Maybe**: the automatic generation rule (based on negation status) supports only binary answers → lack of uncertainty learning signal.
- ~50% of question-titled PubMed papers cannot be answered with yes/no/maybe (wh-question / multi-choice) → narrow candidate pool.
- Annotation error rate ~1% (cases where both annotators made the same mistake, i.e. the square of the 22% error rate of human single performance).

---

## Related links
- **Paper**: [aclanthology.org/D19-1259](https://aclanthology.org/D19-1259/) (Jin et al., EMNLP-IJCNLP 2019, pp.2567–2577)
- **arXiv**: [1909.06146](https://arxiv.org/abs/1909.06146)
- **Dataset**: [pubmedqa.github.io](https://pubmedqa.github.io)
- **Major follow-up work using this benchmark**: MIRAGE/MEDRAG (Xiong et al., ACL 2024) — reconstructed PQA-L for RAG evaluation by removing the context
