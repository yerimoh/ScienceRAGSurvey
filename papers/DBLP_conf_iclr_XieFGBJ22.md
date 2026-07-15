---
title: "Crystal Diffusion Variational Autoencoder for Periodic Material Generation"
bib_key: "DBLP:conf/iclr/XieFGBJ22"
year: 2022
domain: material, chem, physics
type: benchmark
venue: ICLR 2022
paper_link: https://arxiv.org/abs/2110.06197
---
# CDVAE: 3-Dataset Crystal Generation Benchmark (Perov-5 / Carbon-24 / MP-20)

> ICLR 2022 | Benchmark (periodic material generation) + Method | material · chem · physics
> Tian Xie, Xiang Fu, Octavian-Eugen Ganea, Regina Barzilay, Tommi Jaakkola — MIT CSAIL
> arXiv: [2110.06197](https://arxiv.org/abs/2110.06197) · OpenReview: [03RLpj-tc_](https://openreview.net/forum?id=03RLpj-tc_)

## TL;DR
Proposes a **3-dataset standard benchmark** (Perov-5 18,928[^perov] / Carbon-24 10,153[^carbon] / MP-20) and a **3-task evaluation suite** (Reconstruction, Generation, Property Optimization) for periodic material generation. Introduces **Validity, Coverage (COV-R / COV-P), Property statistics (EMD)**[^metrics] as evaluation metrics, addressing the incomparability problem of prior methods.

[^perov]: arXiv:2110.06197 §5: "**Perov-5** (Castelli et al., 2012) includes **18928 perovskite materials** that share the same structure but differ in composition. There are **56 elements** and all materials have **5 atoms in the unit cell**."
[^carbon]: arXiv:2110.06197 §5: "**Carbon-24** (Pickard, 2020) includes **10153 materials** that are all made up of carbon atoms but differ in structures. There is **1 element** and the materials have **6 - 24 atoms** in the unit cells."
[^metrics]: arXiv:2110.06197 §5.2: "1) **Validity**. ... shortest distance between any pair of atoms is larger than 0.5 Å ... 2) **Coverage (COV)**. ... **COV-R (Recall) and COV-P (Precision)** ... 3) **Property statistics**. We compute the **earth mover's distance (EMD)** ... density (ρ), energy (E), and number of unique elements (# elem.)"

---

## How It Was Built (Construction Methodology)

```
Step 1 — Problem identification: non-standardization of material generation evaluation
  ┌──────────────────────────────────────────────┐
  │ "Past studies in this field used very       │
  │  different tasks and metrics, making it     │
  │  difficult to compare different methods"     │
  │  → need standard tasks / datasets / metrics │
  └──────────────────────────────────────────────┘

Step 2 — Curation of 3 standard datasets (based on QM simulations)
  ┌──────────────┬─────────┬──────────────────────────┐
  │ Dataset      │ # mater │ Characteristics          │
  ├──────────────┼─────────┼──────────────────────────┤
  │ Perov-5      │ 18,928  │ 56 elements / 5 atoms/cell │
  │              │         │ same structure (perovskite)│
  │ Carbon-24    │ 10,153  │ 1 element (C) / 6–24 atoms│
  │              │         │ different structures       │
  │ MP-20        │ ~45,000 │ Materials Project ≤ 20 atoms│
  │              │         │ diverse compositions       │
  └──────────────┴─────────┴──────────────────────────┘

Step 3 — 3 standard tasks
  ┌─────────────────────────┬───────────────────────────────┐
  │ Task                    │ Evaluation target             │
  ├─────────────────────────┼───────────────────────────────┤
  │ 1. Reconstruction       │ latent z → recover original structure │
  │ 2. Generation           │ generate novel valid structures │
  │ 3. Property Optimization│ generate structures optimized for target property │
  └─────────────────────────┴───────────────────────────────┘

Step 4 — Evaluation metrics (avoiding actual QM computation cost)
  · Validity:
    - structure: min pairwise distance > 0.5 Å
    - composition: SMACT charge neutrality
  · Coverage (COV-R / COV-P): distribution match of generated vs test set
  · Property statistics (EMD):
    - density (g/cm³), GNN-predicted energy (eV/atom), # elements
  · Property optimization: top-5/10/15 percentile success rate
  · Sample size: 10,000 random generations for validity/coverage
                 1,000 valid for property statistics

Step 5 — Baseline comparison
  · Cond-DFC-VAE (Court 2020): only cubic perovskite possible
  · FTCP (Ren 2020): direct encoding of absolute coordinates
  · G-SchNet (Gebauer 2019): autoregressive, for molecules
  · P-G-SchNet: adds periodicity to G-SchNet
```

---

## Actual Data Format Examples (Paper §5 + Figure 3)

### Type A — Perov-5 (perovskite 5-atom unit cell)

> **Composition**: ABX₃ perovskite structure (all the same cubic perovskite structure, differing only in composition)
>
> **Example entry** (Paper Figure 3 Ground Truth):
> ```
> Formula:    F-N-V-Rh-O-O      (5 atoms)
> Structure:  cubic perovskite (5-atom unit cell)
> # elements: 4  (4 of F, N, V, Rh, O)
> ```
>
> Total **18,928 materials × 56 elements** — all the same structure, evaluating composition diversity only.

### Type B — Carbon-24 (carbon-only allotrope)

> **Composition**: uses pure carbon (1 element) only
>
> **Example entry** (Paper Figure 3 Ground Truth):
> ```
> Formula:    C₂₄        (or 6 ≤ N ≤ 24 atoms)
> Structure:  various allotropes such as diamond, graphite, lonsdaleite
> Constraint: all carbon, various 3D bonding networks
> ```
>
> Total **10,153 materials × 1 element** — same composition, evaluating structural diversity only.

### Type C — MP-20 (Materials Project ≤ 20 atoms)

> **Composition**: entries with unit cell ≤ 20 atoms from the entire Materials Project
>
> **Example entries** (Paper Figure 3 Ground Truth):
> ```
> Sn-Zr-O-F-O              (5 atoms, mixed cation+anion)
> Ba-Ru-O                  (3 atoms, perovskite-like)
> Ti-V-S × N (TiTiS + Na-S) (multi-cation sulfide)
> Eu-O-Sb-O × N            (rare-earth oxide)
> Mg-Al-Si-Si-Al-Al        (intermetallic)
> ```
>
> Total **~45,000 materials** — evaluating composition, structure, and element diversity all together (the most challenging dataset).

### Evaluation sample sizes (validity / coverage / property statistics)

> **Validity & Coverage measurement**:
> ```
> Sample: 10,000 materials randomly sampled from N(0, I) latent
> Validity criteria:
>   - Structure: min pairwise atom distance > 0.5 Å
>   - Composition: SMACT charge neutrality
> ```
>
> **Property statistics measurement**:
> ```
> Sample: 1,000 valid materials (randomly from those passing the validity test)
> EMD over: density ρ (g/cm³), GNN-predicted E (eV/atom), # elements
> ```
>
> Ground truth validity baseline:
> - structure: 100.0% (all datasets)
> - composition: Perov-5 98.60%, Carbon-24 100.0%, MP-20 91.13%

---

## Evaluation Framework Summary

| Metric | Meaning | Unit |
|---|---|---|
| **Validity (structure)** | min pairwise distance > 0.5 Å | binary (%) |
| **Validity (composition)** | SMACT charge neutrality | binary (%) |
| **COV-R (Recall)** | fraction of the test set covered by the generated samples | % |
| **COV-P (Precision)** | fraction of high-quality samples among the generated | % |
| **EMD (density)** | distributional difference in g/cm³ | Earth Mover's Distance |
| **EMD (energy)** | distributional difference in independent GNN E (eV/atom) | EMD |
| **EMD (# elements)** | distributional difference in number of elements | EMD |
| **Property optimization SR** | reach rate of top-5/10/15 percentile | % (over 100 generations) |
| **Reconstruction match rate** | pymatgen StructureMatcher pass | % (stol=0.5, angle_tol=10, ltol=0.3) |
| **Reconstruction RMSE** | RMSE of matched structures, normalized by ∛(V/N) | normalized |

→ ground truth 100% validity vs Perov-5 98.60% / Carbon-24 100.0% / MP-20 91.13% composition validity (training distribution).

---

## Main Results (Paper §5)

| Task | CDVAE result | Meaning |
|---|---|---|
| Reconstruction | lowest RMSE among all models | most accurate latent → structure reconstruction |
| Generation (Validity) | significantly higher than baselines | NCSN diffusion learns stable structures |
| Generation (Coverage) | better COV-R + COV-P | matches the test distribution well |
| Property optimization | surpasses FTCP, comparable to Cond-DFC-VAE on Perov-5 | Carbon-24 is the hardest |

→ "Both G-SchNet and P-G-SchNet are incapable of property optimization" — exposes the limits of molecular adaptation.

---

## Limitations
- **Weak validity criterion**: the "0.5 Å" pairwise distance is a "relative weak criterion" (the paper's own wording)
- **EMD-based property statistics**: GNN proxy energy, no actual DFT verification included
- **Limited to 3 datasets**: oxides, alloys, surfaces, etc. not covered
- **VAE-based**: subsequent diffusion-based models (DiffCSP, MatterGen, etc.) have emerged
- **Time**: 2022 cutoff, evaluation of the latest foundation MLIPs not included

---

## Related Links
- **OpenReview**: [03RLpj-tc_](https://openreview.net/forum?id=03RLpj-tc_)
- **arXiv**: [2110.06197](https://arxiv.org/abs/2110.06197)
- **GitHub**: [txie-93/cdvae](https://github.com/txie-93/cdvae)
- **Author affiliation**: MIT CSAIL
- **Venue**: ICLR 2022
- **Follow-up work using this benchmark**: DiffCSP (Jiao 2023 NeurIPS), MatterGen (Zeni 2025 Nature), FlowMM (Miller 2024 ICML), SyMat — adopted the Perov-5/Carbon-24/MP-20 standard split
