---
title: "MLIP Arena: Open Benchmark Platform for Machine Learning Interatomic Potentials"
bib_key: "DBLP:journals/corr/abs-2509-20630"
year: 2025
domain: material, chem, physics
type: benchmark
venue: NeurIPS 2025 Datasets & Benchmarks
paper_link: https://arxiv.org/abs/2509.20630
---
# MLIP Arena: Physics-aware MLIP Benchmark beyond DFT-error Metrics

> NeurIPS 2025 Datasets & Benchmarks Track | Benchmark (foundation MLIP physics-aware evaluation) | material · chem · physics
> Yuan Chiang, Tobias Kreiman, Christine Zhang, Matthew C. Kuner, Elizabeth Weaver, Ishan Amin, Hyunsoo Park, Yunsung Lim, Jihan Kim, Daryl Chrzan, Aron Walsh, Samuel M. Blau, Mark Asta, Aditi S. Krishnapriyan — UC Berkeley / LBNL / Imperial / KAIST
> DBLP: `journals/corr/abs-2509-20630` · arXiv: [2509.20630](https://arxiv.org/abs/2509.20630)

## TL;DR
An open benchmark platform that evaluates **foundation MLIPs (machine learning interatomic potentials)** on a **physics-aware basis rather than on DFT-error metrics**. It centers on downstream physical tasks such as **dynamical stability, gas adsorption, phase transition, and vacancy migration**. It addresses the weakness of Matbench Discovery (error metrics that are vulnerable to data leakage).

---

## How It Was Built (Construction Methodology)

```
Step 1 — Problem identification: weaknesses of existing MLIP benchmarks
  ┌──────────────────────────────────────────────┐
  │ 1. Data leakage (Matbench Discovery, etc.)    │
  │    → energy overfitting → inaccurate force/finite-T │
  │ 2. Static dataset → useless when new datasets appear │
  │ 3. Error-based metric ≠ practical utility    │
  │    → some MLIPs have low ground-state error   │
  │       but fail on phonon/transport            │
  └──────────────────────────────────────────────┘

Step 2 — Physics-aware task design (4 categories)
  ┌─────────────────────────────────────┐
  │ A. Asymptotic Behaviors             │
  │    - Detecting unphysical force divergence │
  │                                      │
  │ B. Stability & Reactivity           │
  │    - Dynamical stability             │
  │    - Phase transition                │
  │    - Vacancy migration               │
  │    - Gas adsorption                  │
  │                                      │
  │ C. Distribution Shifts              │
  │    - Chemistry outside training data │
  │                                      │
  │ D. Thermodynamic Properties         │
  │    - phonon spectra                  │
  │    - elastic constants               │
  │    - free energy                     │
  └─────────────────────────────────────┘

Step 3 — Platform infrastructure
  ┌──────────────────────────────────────────────┐
  │ - Python package (open source)               │
  │   `pip install mlip-arena`                   │
  │ - Online leaderboard                         │
  │ - Workflow orchestration (Parquet, JSON,     │
  │   ASE DB)                                    │
  │ - Submission via GitHub                      │
  └──────────────────────────────────────────────┘

Step 4 — Evaluation philosophy
  · Respect physics priors (symmetry, conservation)
  · Failure-mode exposure (explicitly visualize failure situations)
  · Reproducibility (random seed, hyperparameter)
  · Multi-DFT reference (compare PBE/SCAN/HSE, etc.)
```

---

## Example of Actual Data Formats (paper §2 + Figure 1 + Table 1)

### Type A — Asymptotic Behaviors (EOS + diatomic PEC)

> **EOS benchmark**: 1,000 WBM crystal structures, V/V₀ scan
>
> ```
> Input:     periodic crystal at varied volumes
> Predict:   E(V/V₀) — should follow Birch–Murnaghan EOS
> Metrics (DFT-agnostic):
>   - Derivative flips ↓  (smooth PEC should have 1)
>   - Tortuosity ↓        (arc-chord ratio, ideal = 1)
>   - Spearman ρ at compression: → -1 (monotonic)
>   - Spearman ρ at tension: → +1
>   - Missing predictions (NaN/divergence) ↓
> ```
>
> **Diatomic PEC**: homonuclear pairs across periodic table
> - Distance range scan of 0.9 × r_cov ~ 3.1 × r_vdw
> - Top Matbench Discovery models often fail → "apparent benchmark success may result from plausible many-body error cancellation"

### Type B — Stability & Reactivity (MD on RM24)

> **NVT MD**: 120 random amorphous mixture structures (RM24)
> ```
> Thermostat: Nosé-Hoover NVT
> Temperature: linear 300 K → 3000 K
> Duration: 10 ps
> Metric: # valid trajectories, MD steps per second (SPS)
>         SPS = a·N^b  (asymptotic scaling)
> ```
>
> **NPT MD**: 80 RM24 structures
> ```
> Thermostat: Nosé-Hoover NPT
> Temperature: 300 K → 3000 K
> Pressure: 0 GPa → 500 GPa (linear ramp)
> Duration: 10 ps
> ```
>
> **Reactivity test** (hydrogen combustion):
> ```
> 1 ns annealing MD (2 × 10⁶ steps, 0.5 fs)
> H + O system: 300 K → 3000 K → 300 K
> Monitor: # H₂O formed, ΔH, bond breaking/formation
> ```

### Type C — EOS Benchmark Results (Table 1)

> 1,000 WBM structures, lower=better (deviation from ideal physics)

| Model | Derivative flips ↓ | Tortuosity ↓ | E compression ρ ↓ | dE/dV compression ρ ↑ | Missing ↓ |
|---|---|---|---|---|---|
| **MACE-MPA** | **1.037** | **1.005** | **-0.999** | **0.996** | **2** |
| eSEN | 1.042 | 1.008 | -0.999 | 0.997 | 5 |
| MACE-MP(M) | 1.042 | 1.009 | -0.999 | 0.994 | 5 |
| MatterSim | 1.045 | 1.006 | -0.997 | 0.993 | 3 |
| CHGNet | 1.105 | 1.015 | -0.996 | 0.993 | 3 |
| SevenNet | 1.109 | 1.019 | -0.998 | 0.989 | 3 |
| M3GNet | 1.175 | 1.018 | -0.996 | 0.990 | 5 |
| ORBv2 | 1.316 | 1.037 | -0.992 | 0.970 | 7 |

>
> → **Top Matbench Discovery models** ≠ top EOS models (force smoothness ≠ energy regression)

### Type D — 4-category benchmark structure

> ```
> ┌─────────────────────────────────────────────────┐
> │ A. Asymptotic Behaviors                          │
> │    · EOS (1,000 WBM crystals)                    │
> │    · Diatomic PEC (homonuclear, periodic table)  │
> │    Metrics: smoothness, repulsion, conservation  │
> │                                                  │
> │ B. Stability & Reactivity                        │
> │    · MD on RM24 (NVT 120 + NPT 80 structures)    │
> │    · H₂ combustion 1 ns annealing                 │
> │    Metrics: valid steps, SPS, ΔH                  │
> │                                                  │
> │ C. Distribution Shifts                           │
> │    · Energy conservation drift                   │
> │    · Force rotational equivariance               │
> │    Metrics: drift/error in differential-entropy bins │
> │                                                  │
> │ D. Thermodynamic Properties                      │
> │    · Phonon spectra                              │
> │    · Equation of state                           │
> │    · Free energy, elastic constants              │
> └─────────────────────────────────────────────────┘
> ```
>
> Models evaluated: **MACE-MP(M), CHGNet, M3GNet, MatterSim, ORBv2, SevenNet, MACE-MPA, eSEN** (Table S4)
> Workflow: Prefect orchestration · Parquet/JSON/ASE DB storage · GitHub submission

---

## Evaluation Framework

| Metric category | Content |
|---|---|
| **Physics awareness** | Symmetry preservation, energy conservation, force smoothness |
| **Chemical reactivity** | Bond breaking, transition state |
| **Stability under extreme conditions** | High T/P, defect, surface |
| **Thermodynamic predictions** | Phonons, elastic, gas adsorption, free energy |
| **Distribution shift** | OOD chemistry generalization |

→ Simple error metrics such as DFT energy MAE/MAEF are **secondary**.

---

## Key Findings (paper body)

| Observation | Meaning |
|---|---|
| Top Matbench Discovery model fails on phonon | limitation of error metrics |
| Foundation MLIPs lack transferability to OOD chemistry | training-data dependence |
| Symmetry-breaking discovered | violation of physical priors |
| Force smoothness vs energy accuracy trade-off | PES landscape quality |

→ **Conclusion**: Evaluation of MLIP foundation models must be based on **physics-aware tasks**.

---

## Limitations
- **2025 NeurIPS D&B submission**: final leaderboard in progress
- **Foundation MLIP only**: classical FF and specific-task MLIPs not covered
- **Limited number of tasks**: ~a few dozen categories, needs further expansion
- **DFT reference diversity**: mostly PBE, advanced functionals insufficient
- **Computational cost**: physics-aware tests are much heavier than simple error metrics
- **CPU/GPU diversity**: accuracy consistency across various hardware needs verification

---

## Related Links
- **arXiv**: [2509.20630](https://arxiv.org/abs/2509.20630)
- **DBLP**: [journals/corr/abs-2509-20630](https://dblp.org/rec/journals/corr/abs-2509-20630.html)
- **GitHub**: [atomind-ai/mlip-arena](https://github.com/atomind-ai/mlip-arena)
- **Python package**: `pip install mlip-arena`
- **Official site**: [atomind.ai/mlip-arena](https://atomind.ai/mlip-arena/) (planned)
- **Venue**: NeurIPS 2025 Datasets & Benchmarks
- **Author affiliations**: UC Berkeley / LBNL / Imperial College London / KAIST
- **Related benchmarks**: Matbench Discovery (Riebesell 2025 NMI, beats), JARVIS-Leaderboard (Choudhary 2024 npj CompMat), AdsorbML (Lan 2023 npj CompMat)
