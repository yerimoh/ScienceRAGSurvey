---
title: "f-RAG: Molecule Generation with Fragment Retrieval Augmentation"
bib_key: "DBLP:conf/nips/LeeKV0RPVN24"
year: 2024
domain: chem
type: Method
venue: NeurIPS 2024
paper_link: https://arxiv.org/abs/2411.12078
---
# f-RAG: Molecule Generation with Fragment Retrieval Augmentation

> NeurIPS 2024 | Method (docking-verified hypothesis) | chem
> Seul Lee, Karsten Kreis, Srimukh Prasad Veccham, Meng Liu, Danny Reidenbach, Saee Paliwal, Arash Vahdat, Weili Nie — KAIST / NVIDIA / AstraZeneca
> DBLP: `conf/nips/LeeKV0RPVN24` · arXiv: [2411.12078](https://arxiv.org/abs/2411.12078)

## TL;DR
A fragment-RAG method that combines **fragment retrieval augmentation** (hard fragments + soft fragments) with a pretrained molecule generation model and extrapolates the fragment vocabulary through **iterative refinement + genetic fragment modification**, achieving top-10 AUC on 12 of the **23 tasks in the PMO benchmark** and the best synthesizability on 19 tasks.

---

## How It Was Built (System Architecture)

```
[pretrained molecule generation model (LSTM, etc.)]
              │
              ▼
┌──────────────────────────────────────┐
│ Fragment Vocabulary V                 │ ← extracted from ZINC 250K, etc.
│  - hard fragments: directly included  │
│    in the molecule                    │
│  - soft fragments: referenced via the │
│    injection module to guide new      │
│    fragment generation                │
└──────────┬───────────────────────────┘
           │ retrieve top-k fragments
           ▼
┌──────────────────────────────────────┐
│ Hard Fragment Retrieval               │
│   prioritize fragments with high      │
│   property scores                     │
│   → directly include in generated     │
│     molecule                          │
│                                       │
│ Soft Fragment Retrieval               │
│   trainable fragment injection module │
│   → guide novel fragment generation   │
└──────────┬───────────────────────────┘
           ▼
[molecule generation (SMILES) + property prediction]
           │
           ▼
┌──────────────────────────────────────┐
│ Iterative Refinement (closed loop):    │
│   1. compute property score           │
│   2. extract new fragments from        │
│      superior molecules                │
│   3. update V (vocabulary expansion)  │
│   4. use in next round of retrieval   │
└──────────┬───────────────────────────┘
           ▼
[Post-hoc Genetic Fragment Modification]
   explore additional chemical space via crossover/mutation
```

---

## Direct Quotes from the Original (arXiv:2411.12078 §main text)

> **Use of the PMO benchmark** (§4.1): *"We demonstrate the efficacy of f-RAG on the **23 tasks** from the **PMO benchmark**. Following the standard setting of the benchmark, we set the maximum number of oracle calls to 10,000 and evaluate optimization performance with the area under the curve (AUC) of the average property score versus oracle calls."*

> **Results** (§4.1): *"f-RAG ... achieves the highest **AUC top-10 values in 12 out of 23 tasks**, demonstrating that the proposed combination of hard fragment retrieval, soft fragment retrieval, and genetic fragment modification is highly effective"*

> **Diversity / Synthesizability**: *"f-RAG shows the highest **diversity in 12 out of 23 tasks**, and the highest **synthesizability in 19 out of 23 tasks**"*

> **Docking score evaluation (§4.2)**: *"we use docking score calculated by **QuickVina 2** with five protein targets, **parp1, fa7, 5ht1b, braf, and jak2**, to measure binding affinity. We use quantitative estimates of drug-likeness (**QED**) and **SA** to measure drug-likeness and synthesizability"*

---

## Evaluation Setup

### Setup 1 — PMO Benchmark (Gao et al. 2022, NeurIPS)
- **Tasks**: 23 molecular optimization tasks (TDC oracle based)
- **Oracle budget**: 10,000 calls limit
- **Primary metric**: AUC top-10 (average property score cumulative vs oracle calls)
- **Auxiliary metric**: Diversity, Novelty, Synthesizability (SA score)

### Setup 2 — Docking Score Optimization under QED/SA/Novelty constraints (§4.2)
- **Docking program**: QuickVina 2
- **Protein targets**: parp1, fa7, 5ht1b, braf, jak2 (5 total)
- **Constraint**: target property y = c_DS × c_QED × c_SA × c_Novelty (normalized product)
- **Baseline comparison**: Lee et al. (DECOMPDIFF), DST, and other SBDD methods

---

## Main Evaluation Results (paper main text Table 1)

| Comparison system | Top-7 PMO baselines + 2 SOTA | AUC top-10 sum |
|---|---|---|
| Graph GA | classical GA fragment crossover | – |
| Mol GA | hyperparameter-tuned Graph GA | (baseline) |
| Genetic GFN | recent SOTA | (baseline) |
| **f-RAG** | hard + soft + genetic | **highest sum across all PMO baselines** |

Key performance numbers (paper main text):
- AUC top-10 highest in **12/23 tasks**
- Synthesizability highest in **19/23 tasks**
- Diversity highest in **12/23 tasks**

---

## Key Contributions
1. **Fragment retrieval as RAG for molecules** — extends the text RAG paradigm to molecule generation
2. **Hard + Soft dual retrieval** — combines explicit inclusion (hard) with an injection module (soft)
3. **Vocabulary extrapolation via iterative refinement** — explores fragments outside the database
4. **Post-hoc genetic modification** — secures additional diversity via crossover/mutation
5. **New SOTA on the PMO benchmark** — 1st in AUC top-10 on 12/23 tasks

---

## Limitations
- **Dependence on fragment vocabulary size**: small DB → degraded performance
- **Docking score is a proxy**: an approximation of actual binding affinity
- **Linear increase in computational cost**: proportional to the number of refinement iterations
- **Only 5 protein targets evaluated**: generalization across diverse protein families unverified
- **Synthetic feasibility**: the SA score is a reaction-template-based estimate that differs from actual synthetic realizability

---

## Related Links
- **Paper (arXiv)**: [2411.12078](https://arxiv.org/abs/2411.12078)
- **NeurIPS 2024 OpenReview**: search "Molecule Generation with Fragment Retrieval Augmentation"
- **DBLP**: [conf/nips/LeeKV0RPVN24](https://dblp.org/rec/conf/nips/LeeKV0RPVN24.html)
- **Author affiliations**: KAIST, NVIDIA, AstraZeneca
- **Benchmark used**: **PMO** (Wenhao Gao et al., NeurIPS 2022, [arXiv:2206.12411](https://arxiv.org/abs/2206.12411))
- **Docking tool used**: [QuickVina 2](https://qvina.github.io/) (Alhossary et al. 2015, Bioinformatics)
