---
title: "Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models"
bib_key: "DBLP:journals/corr/abs-2410-12771"
year: 2024
domain: material, chem, physics
type: benchmark
venue: arXiv (Meta FAIR Tech Report)
paper_link: https://arxiv.org/abs/2410.12771
---
# OMat24: 110M-DFT MLIP Training & Evaluation Suite (Matbench Discovery F1 > 0.9)

> arXiv 2024 (Meta FAIR Technical Report) | Benchmark + Dataset + Models (foundation MLIP) | material · chem · physics
> Luis Barroso-Luque, Muhammed Shuaibi, Xiang Fu, Brandon M. Wood, Misko Dzamba, Meng Gao, Ammar Rizvi, Matt Uyttendaele, C. Lawrence Zitnick, Zachary W. Ulissi — Fundamental AI Research (FAIR) at Meta
> arXiv: [2410.12771](https://arxiv.org/abs/2410.12771) · CoRR: `journals/corr/abs-2410-12771`

## TL;DR
A large-scale training+benchmark suite bundling a **110M+ DFT calculation open dataset** for inorganic materials + **EquiformerV2/eSEN MLIP model checkpoints** + a **Matbench Discovery evaluation protocol**. It is roughly 100x the scale of prior data, and achieves **F1 > 0.9 (stability)** and **MAE 20 meV/atom (formation energy)**. **Every publicly available leaderboard top model adopts OMat24**.

---

## Construction Methodology

```
Step 1 — Problem recognition: shortage of open MLIP training data
  ┌──────────────────────────────────────────────┐
  │ "the state-of-the-art in openly available    │
  │  and reproducible datasets and models        │
  │  lagged behind proprietary models"           │
  │ + existing datasets like MPTrj/MPF are       │
  │   equilibrium-centric, lacking               │
  │   far-from-equilibrium                        │
  └──────────────────────────────────────────────┘

Step 2 — OMat24 dataset composition
  ┌──────────────────────────────────────────────┐
  │ - 110M+ single-point DFT calculations         │
  │ - 118M structures total (energy, forces,      │
  │   cell stress labels)                          │
  │ - 1–100 atoms per structure                    │
  │   (majority < 20 atoms from Alexandria)        │
  │ - Source: Alexandria base + AIMD sampling +   │
  │   non-equilibrium perturbations                │
  │ - DFT settings designed for compatibility     │
  │   with MPtrj/Materials Project                 │
  └──────────────────────────────────────────────┘

Step 3 — Three core design principles
  · Scale: ~2 orders of magnitude > existing open dataset
  · Diversity: entire periodic table + far-from-equilibrium
  · Open-science: CC-by license, full reproducibility

Step 4 — Pretrained MLIP models
  · EquiformerV2 variants (Liao 2023, 2024)
  · eSEN variants (Fu 2024)
  · Pretrained on OMat24, fine-tuned for MPtrj
    DFT-settings compatibility

Step 5 — Evaluation protocol
  ┌──────────────────────────────────────────────┐
  │ 1. Matbench Discovery (WBM 257K structures)   │
  │    → F1, DAF, precision, recall, MAE          │
  │ 2. Thermal conductivity / phonon benchmarks   │
  │    (newly introduced)                          │
  │ 3. Softening bias quantification              │
  │    (energy/force/derivative systematic        │
  │     underestimation correction)                │
  └──────────────────────────────────────────────┘

Step 6 — Open resources
  · Dataset: HuggingFace fairchem/OMAT24 (CC-by-4.0)
  · Models: HuggingFace fairchem/OMAT24
  · Code: github.com/FAIR-Chem/fairchem (MIT)
```

---

## Data Format Examples (paper §2.1 + Table 1)

### Type A — Single-point DFT calculation entry (S2EF training unit)

> **Input** (periodic unit cell):
> ```
> Structure:    1–100 atoms (majority < 20 atoms)
> Composition:  diverse across periodic table
>               (oxides over-represented per open-data prevalence)
> Configuration: mix of equilibrium + far-from-equilibrium
> ```
>
> **Labels (DFT ground truth)**:
> ```
> Energy:       eV (per structure)
> Forces:       eV/Å (per atom, 3D vector)
> Cell stress:  eV/Å³ (3×3 tensor)
> ```

### Type B — Train / validation / test split

> ```
> ┌────────────────────────┬──────────────┐
> │ Split                  │ # structures │
> ├────────────────────────┼──────────────┤
> │ Training               │  100,000,000 │
> │ Validation             │    5,000,000 │
> │ ID test                │    5,000,000 │
> │ WBM Test (OOD)         │    (subset)  │
> │ OOD-Elemental          │      619,000 │
> │ OOD-Stoichiometry      │    (subset)  │
> ├────────────────────────┼──────────────┤
> │ Total OMat24           │  118,000,000 │
> └────────────────────────┴──────────────┘
> ```
>
> The WBM Test split has "highest prediction errors → most informative test of model generalization" (paper §2.1.1)

### Type C — Source dataset comparison (compositional/configurational coverage)

| Dataset | Size (structures) | Configuration | Compositional diversity |
|---|---|---|---|
| **OMat24** | 118M | equilibrium + far-from-eq | entire periodic table, oxide over-represented |
| MPtrj | 1.6M | near-equilibrium | Materials Project subset |
| Alexandria | ~5M | equilibrium-only | hypothetical prototyped |
| OC20 | 130M | catalyst surface only | limited chemistry |

>
> → OMat24 = **2 orders of magnitude larger** than other open datasets

### Type D — Downstream evaluation tasks

> 1. **Matbench Discovery** — WBM 257K structures, F$_1$ + DAF + MAE
> 2. **Phonon prediction** — force-derivative properties (newly added benchmark)
> 3. **Thermal conductivity** — transport properties (newly added benchmark)
> 4. **Softening bias measurement** — quantifying systematic energy/force/phonon underestimation
>
> → OMat24-trained model: F$_1$ > 0.9, formation E MAE = 20 meV/atom, **every Matbench Discovery top model adopts OMat24**.

---

## Evaluation framework

| Benchmark | Metric | Meaning |
|---|---|---|
| **Matbench Discovery** | F$_1$ (stability) | binary stable/unstable WBM 257K |
| **Matbench Discovery** | MAE (formation E) | regression eV/atom |
| **Matbench Discovery** | DAF | discovery acceleration |
| **Phonon prediction** | newly added | force-derivative property |
| **Thermal conductivity** | newly added | transport property |
| **Softening bias** | systematic error magnitude | energy/force/phonon underestimation |

→ OMat24-trained model: F$_1$ > 0.9, MAE = 20 meV/atom (Matbench Discovery top)

---

## Key Results (paper §2 + Tables)

| Metric | OMat24-trained model | Meaning |
|---|---|---|
| Matbench F$_1$ (stability) | **> 0.9** | improvement over previous best |
| Formation E MAE | **20 meV/atom** | DFT-level accuracy |
| Softening bias | eliminated or reduced | effect of non-equilibrium training |
| Phonon prediction | highest accuracy | accurate force-derivative |
| Architecture | EquiformerV2, eSEN | different architectures also improve on the same data |

→ **Conclusion**: dataset diversity (especially far-from-equilibrium) is decisive for MLIP accuracy, and every leaderboard top model adopts OMat24.

---

## Limitations
- **DFT settings compatibility**: functional/parameters differ from MPtrj → fine-tuning required
- **Limited to inorganic bulk materials**: molecules, surfaces, and interfaces not covered
- **License**: dataset CC-by, model checkpoint custom license
- **Compute requirement**: 110M DFT calculations limit reproducibility
- **Static dataset**: comparison needed when successors like OMat25/26 appear
- **Time**: 2024 cutoff (paper states 2026-05-21 revision)

---

## 관련 정보
- **arXiv**: [2410.12771](https://arxiv.org/abs/2410.12771)
- **DBLP**: [journals/corr/abs-2410-12771](https://dblp.org/rec/journals/corr/abs-2410-12771.html)
- **Dataset**: [huggingface.co/datasets/fairchem/OMAT24](https://huggingface.co/datasets/fairchem/OMAT24) (CC-by-4.0)
- **Models**: [huggingface.co/fairchem/OMAT24](https://huggingface.co/fairchem/OMAT24)
- **GitHub**: [FAIR-Chem/fairchem](https://github.com/FAIR-Chem/fairchem) (MIT)
- **저자 소속**: Meta FAIR
- **이 dataset을 사용한 후속 작업**: Matbench Discovery top models (모두 OMat24 채택), MLIP Arena (NeurIPS 2025 D&B)
- **관련 데이터셋**: MPtrj (Deng 2023), Alexandria (Schmidt 2024), Materials Project, OC20 (Chanussot 2021), OC22, ODAC23
