---
title: "Matbench Discovery: A Framework to Evaluate ML Crystal Stability Predictions"
bib_key: "riebesell2025matbench"
year: 2025
domain: material, chem, physics
type: benchmark
venue: Nature Machine Intelligence
paper_link: https://doi.org/10.1038/s42256-025-01055-1
---
# Matbench Discovery: ML Crystal Stability Benchmark on 257K WBM Structures

> Nature Machine Intelligence 7:836–847 | 2025 | Benchmark (convex-hull stability prediction) | material · chem · physics
> Janosh Riebesell, Rhys E. A. Goodall, Philipp Benner, Yuan Chiang, Bowen Deng, Gerbrand Ceder, Mark Asta, Alpha A. Lee, Anubhav Jain, Kristin A. Persson — Cambridge / LBNL / BAM / UC Berkeley
> arXiv: [2308.14920](https://arxiv.org/abs/2308.14920) · DOI: [10.1038/s42256-025-01055-1](https://doi.org/10.1038/s42256-025-01055-1)

## TL;DR
A task-based benchmark that evaluates ML energy models as a **pre-filter for high-throughput discovery of stable inorganic crystals**. It measures F$_1$, DAF, and precision/recall of the **convex hull distance** over the **257K+ structures of the WBM dataset**, with **UIPs (Universal Interatomic Potentials)** achieving the best performance at F$_1$ 0.57–0.82 and a **discovery acceleration factor up to 6×**.

---

## Construction Methodology

```
Step 1 — Test corpus: WBM dataset
  └─ Wang et al. 2021 npj CompMat
  └─ 257,487 structures (relaxed + unrelaxed)
  └─ Chemistry expansion synthesized from Materials Project

Step 2 — Task definition
  ┌──────────────────────────────────────────┐
  │ Input: unrelaxed candidate crystal       │
  │ Predict: distance from convex hull       │
  │   (relaxed → E_hull < 0 → stable)        │
  │ Threshold: 0 eV/atom above convex hull   │
  │   → binary classification: stable/unstable│
  └──────────────────────────────────────────┘

Step 3 — Primary metrics (classification-focused)
  · F$_1$ score (binary stable/unstable)
  · DAF (Discovery Acceleration Factor):
    "found N stable from K predictions" vs random
  · Precision (P): TP / (TP + FP)
  · Recall (R): TP / (TP + FN)

Step 4 — Secondary: regression metrics
  · MAE on E_hull (eV/atom)
  · Disagreement with classification metric:
    "high false-positive rate near 0 eV/atom decision boundary"

Step 5 — Public leaderboard + Python package
  └─ Submission via Python package
  └─ Online leaderboard maintained
```

---

## Example Data Formats (paper §2 + Table 1)

### Type A — Test input/output schema (IS2RE-style)

> **Input**: **unrelaxed** prototype structure from the WBM dataset (5 batches of elemental substitution, 1–5 substitutions)
>
> ```
> Structure:   periodic unit cell (initial, not DFT-relaxed)
> Prototype:   ICSD-based with elemental substitution
> Batch ID:    1 ~ 5 (substitution depth, OOD progressing)
> ```
>
> **Predict**:
> ```
> E_above_hull (eV/atom) — distance from MP convex hull
> → Classify: stable (E ≤ 0) / unstable (E > 0)
> ```
>
> **Training corpus (compliant)**:
> - Materials Project v2022.10.28 release (~154K crystals)
> - All relaxation frames, energies/forces/stresses allowed
> - Auxiliary tasks (charge, magmom) allowed

### Type B — Test set scale & cleaning

> ```
> ┌────────────────────────────────────────────────┬──────────┐
> │ Source: WBM (Wang et al. 2021 npj CompMat)     │  257,487 │
> │   - Removed pathological (|E| > 5 eV/atom)     │     -524 │
> │   - Removed MP-overlapping protostructures     │  -11,175 │
> │   - Removed duplicated protostructures         │   ...    │
> │ Final unique prototype test set                │  215,488 │
> │   of which thermodynamically stable (E ≤ 0)    │   32,942 │
> └────────────────────────────────────────────────┴──────────┘
> ```

### Type C — Leaderboard model ranking (Table 1)

| Rank | Model | F$_1$ ↑ | DAF ↑ | Prec ↑ | MAE ↓ | Training | Targets |
|---|---|---|---|---|---|---|---|
| 1 | **eqV2 S DeNS** | **0.815** | **5.042** | 0.771 | 0.036 | MPtrj 1.6M | EFSD |
| 2 | ORB MPtrj | 0.765 | 4.702 | 0.719 | 0.045 | MPtrj 1.6M | EFSD |
| 3 | SevenNet | 0.724 | 4.252 | 0.650 | 0.048 | MPtrj 1.6M | EFSG |
| 4 | MACE | 0.669 | 3.777 | 0.577 | 0.057 | MPtrj 1.6M | EFSG |
| 5 | CHGNet | 0.613 | 3.361 | 0.514 | 0.063 | MPtrj 1.6M | EFSGM |
| 6 | M3GNet | 0.569 | 2.882 | 0.441 | 0.075 | MPF 188K | EFSG |
| 7 | ALIGNN | 0.567 | 3.206 | 0.490 | 0.093 | MP 2022 155K | E only |
| 8 | MEGNet | 0.510 | 2.959 | 0.452 | 0.130 | MP Graphs 133K | E only |
| 9 | CGCNN | 0.507 | 2.855 | 0.436 | 0.138 | MP 2022 155K | E only |
| … | Wrenformer, BOWSR, Voronoi RF | 0.466 → 0.333 | … | | | | |
| — | Dummy (random) | 0.185 | 1.000 | 0.154 | 0.124 | — | — |

>
> → UIPs (energy+force+stress) > energy-only one-shot models: a clear gap

### Type D — Regression vs Classification disagreement example

> "Accurate regressors can yield **high false-positive rates near the decision boundary at 0 eV/atom**" — even a small MAE produces many stable/unstable misclassifications near the hull.
>
> Examples: CGCNN+P, Wrenformer, BOWSR — regression MAE is good but F$_1$ is low (demonstrating the need for task-based evaluation)

---

## Evaluation Metric Details

| Metric | Meaning | Priority |
|---|---|---|
| **F$_1$** | binary stable/unstable | Primary |
| **DAF** | discovery acceleration vs random | Primary |
| **Precision** | TP / (TP+FP), reduce wasted DFT calls | Primary |
| **Recall** | TP / (TP+FN), avoid missing stable materials | Primary |
| MAE (E_hull) | regression error | Secondary (misleading) |

→ Emphasizes **task-based evaluation** (regression metrics are secondary). Even a small MAE can produce many false positives near the decision boundary.

---

## Main Evaluation Results (paper body)

| Model | F$_1$ | DAF |
|---|---|---|
| Voronoi RF | (low) | – |
| MEGNet / CGCNN | (medium) | – |
| M3GNet | 0.57+ | ~3× |
| CHGNet, MACE, SevenNet, Orb | (high) | – |
| **EquiformerV2 + DeNS** | **0.82** (top) | **6×** (top, first 10k) |

→ Universal Interatomic Potentials (UIP) > task-specific models > one-shot predictors

---

## Limitations
- **WBM dataset limitation**: synthesized structures → experimental validation not reflected
- **Regression vs classification conflict**: even a small MAE yields false positives near the boundary
- **DFT functional dependence**: PBE-based ground truth, a gap with other functionals
- **Stable ≠ synthesizable**: only thermodynamic stability is evaluated; synthesis pathways/kinetics not reflected
- **Other domains such as Open Catalyst not included**: surfaces and molecules not covered
- **Data leakage risk**: some models may have been trained on structures adjacent to WBM

---

## Related links
- **Paper (Nature MI)**: [10.1038/s42256-025-01055-1](https://doi.org/10.1038/s42256-025-01055-1)
- **arXiv**: [2308.14920](https://arxiv.org/abs/2308.14920)
- **Official site**: [matbench-discovery.materialsproject.org](https://matbench-discovery.materialsproject.org/)
- **Python package**: `pip install matbench-discovery`
- **GitHub**: [janosh/matbench-discovery](https://github.com/janosh/matbench-discovery)
- **WBM dataset**: Wang et al. 2021 npj CompMat (the test corpus of Matbench Discovery)
- **Follow-up work using this benchmark**: MLIP Arena (NeurIPS 2025 D&B), foundation MLIP papers
