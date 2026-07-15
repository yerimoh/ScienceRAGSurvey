---
title: "AdsorbML: A Leap in Efficiency for Adsorption Energy Calculations using Generalizable ML Potentials"
bib_key: "lan2023adsorbml"
year: 2023
domain: material, chem
type: benchmark
venue: npj Computational Materials
paper_link: https://doi.org/10.1038/s41524-023-01121-5
---
# AdsorbML: 1,000 Adsorbate-Surface Pairs DFT-Success Benchmark

> npj Computational Materials 9:172 | 2023 | Benchmark (adsorption-energy workflow + Open Catalyst Dense dataset) | material · chem
> Janice Lan, Aini Palizhati, Muhammed Shuaibi, Brandon M. Wood, Brook Wander, Abhishek Das, Matt Uyttendaele, C. Lawrence Zitnick, Zachary W. Ulissi — Meta AI (FAIR) / CMU
> arXiv: [2211.16486](https://arxiv.org/abs/2211.16486) · DOI: [10.1038/s41524-023-01121-5](https://doi.org/10.1038/s41524-023-01121-5)

## TL;DR
An algorithm + benchmark that accelerates **adsorbate-surface binding energy calculation** using ML interatomic potentials. On the **Open Catalyst Dense** dataset (~1,000 surfaces × ~100,000 configurations), it achieves an **87.36% lowest-energy configuration identification rate** and a **~2000× speedup over DFT**.

---

## How It Was Built (Construction Methodology)

```
Step 1 — Task definition
  ┌────────────────────────────────────────────────┐
  │ Input: adsorbate molecule + catalyst surface   │
  │ Output: lowest-energy adsorbate-surface        │
  │         configuration (3D pose) + binding E    │
  │ Verifier: DFT (ground truth)                   │
  └────────────────────────────────────────────────┘

Step 2 — Building the Open Catalyst Dense dataset
  └─ ~1,000 catalyst surfaces (binary alloys, oxides, intermetallics, etc.)
  └─ ~100,000 unique adsorbate-surface configurations
  └─ DFT (PBE) ground truth labels
  └─ standardized benchmark format

Step 3 — AdsorbML algorithm
  ┌──────────────────────────────────────────────┐
  │ 1. Heuristic + random initial configurations │
  │ 2. ML potential (GemNet-OC, etc.) energy pred.│
  │ 3. Low-energy candidates → ML relaxation     │
  │ 4. Top-k candidates → precise DFT validation │
  │ 5. Select lowest-energy configuration        │
  └──────────────────────────────────────────────┘

Step 4 — Evaluation metrics
  · Success rate: fraction of lowest-energy configs found (target)
  · Speedup: vs. DFT-only baseline
  · Energy error: vs DFT ground truth
  · Trade-off curve: accuracy × efficiency
```

---

## Example of Actual Data Format (paper §Methods + Table I + Table II)

### Type A — Input/Output schema

> **Input**: catalyst surface + adsorbate (reaction intermediate, *CHO / *CO / *OH, etc.)
>
> ```
> Surface:    slab with 3D periodic boundary
> Adsorbate:  reaction intermediate (e.g., *CHO for CO2 reduction)
> Initial config: heuristic (symmetry-based) + random sampling
> ```
>
> **Output**: lowest adsorption energy + valid relaxed structure
>
> ```
> E_ads ≡ min over all valid relaxed configs (eV)
> Validity criteria:
>   - adsorbate does not desorb from the surface
>   - no dissociation
>   - no surface mismatch
> Success: predicted E_ads within 0.1 eV of the DFT minimum
> ```

### Type B — OC20-Dense dataset structure

| Split | Unique systems | Unique configs | Adsorbates | Bulks |
|---|---|---|---|---|
| **Validation** | 973 | 85,658 | 74 | 833 |
| **Test** | 989 | 105,714 | 74 | 837 |

>
> Each split is ~250 systems × 4 subsplits = **ID, OOD-Adsorbate, OOD-Catalyst, OOD-Both**

### Type C — Algorithm (ML+SP / ML+RX, top-k)

> ```
> 1. Generate initial configs (heuristic + random sampling)
> 2. ML potential relaxation → rank by energy (lowest first)
> 3. Take best-k candidates:
>    Option A (ML+SP): single-point DFT on each → take min
>    Option B (ML+RX): full DFT relaxation from ML state → take min
> 4. Return: min(DFT outputs)
> ```
>
> Trade-off knob: **k = 1, 2, 3, 4, 5** (k↑ → accuracy↑, speedup↓)

### Type D — Model comparison (Table I, OC20-Dense Test)

| Model | Success Rate ↑ | Energy MAE [eV] ↓ | OC20 S2EF Force MAE [eV/Å] |
|---|---|---|---|
| SchNet | 1.01% | 0.5150 | 0.0496 |
| DimeNet++ | 1.72% | 0.4329 | 0.0446 |
| PaiNN | 10.92% | 0.2994 | 0.0294 |
| GemNet-OC | 46.51% | 0.1849 | 0.0179 |
| GemNet-OC-MD | 50.05% | 0.1966 | 0.0173 |
| GemNet-OC-MD-Large | 48.03% | 0.1935 | 0.0164 |
| SCN-MD-Large | 51.87% | 0.1758 | 0.0160 |
| **eSCN-MD-Large** | **56.52%** | **0.1739** | **0.0139** |

>
> → AdsorbML (eSCN-MD-Large, k=3, ML+SP): **89.28% success × ~2000× speedup** (paper Figure 3 balanced point: 87.36% × 2290×)

---

## Key Evaluation Results

| Configuration | Success Rate | Speedup vs DFT |
|---|---|---|
| Fast (ML only, top-1) | low | ~10,000× |
| **Balanced (ML+DFT top-k)** | **87.36%** | **~2000×** |
| Conservative (ML+DFT top-N) | higher | ~500× |

→ Provides an accuracy-efficiency trade-off spectrum.

---

## Evaluation Setup

| Item | Details |
|---|---|
| Test set | Open Catalyst Dense (~1,000 surfaces) |
| Metric | Success rate + Speedup |
| Baseline | DFT-only structure relaxation |
| ML potential | GemNet-OC, SchNet, eSCN, and other OC family |
| Adsorbates | OC20 reaction intermediates (CO, CHO, OH, NO, etc.) |

---

## Limitations
- **PBE functional dependence**: gap relative to other functionals
- **Limited to OC20-trained models**: transfer limits when applied to other chemistries
- **Initial configuration dependence**: quality of the heuristic starting point affects results
- **Memory / compute cost (large unit cells)**: reduced ML accuracy for large cells
- **Domains beyond catalysts not covered**: bulk/molecular systems not evaluated
- **Time**: 2023 cutoff, does not reflect the latest foundation MLIPs

---

## Related links
- **Paper (npj CompMat)**: [10.1038/s41524-023-01121-5](https://doi.org/10.1038/s41524-023-01121-5)
- **arXiv**: [2211.16486](https://arxiv.org/abs/2211.16486)
- **Data**: Open Catalyst Project Dense subset
- **Official site**: [opencatalystproject.org](https://opencatalystproject.org/)
- **GitHub**: [Open-Catalyst-Project/ocp](https://github.com/Open-Catalyst-Project/ocp)
- **Follow-up work using this benchmark**: Open Catalyst 2022/2024 (OC22, OC24), MLIP Arena (NeurIPS 2025 D&B), foundation MLIP evaluation
