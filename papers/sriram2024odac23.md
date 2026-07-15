---
title: "The Open DAC 2023 Dataset and Challenges for Sorbent Discovery in Direct Air Capture"
bib_key: "sriram2024odac23"
year: 2024
domain: material, chem
type: benchmark
venue: ACS Central Science
paper_link: https://doi.org/10.1021/acscentsci.3c01629
---
# ODAC23: 8,400 MOFs × 38M DFT for Direct-Air-Capture Sorbent Discovery

> ACS Central Science 10:923–941 | 2024 | Benchmark + Dataset (DFT-verified MOF sorbent screening) | material · chem
> Anuroop Sriram, Sihoon Choi, Xiaohan Yu, Logan M. Brabson, Abhishek Das, Zachary Ulissi, Matt Uyttendaele, Andrew J. Medford, David S. Sholl — Meta FAIR / Georgia Tech / ORNL
> arXiv: [2311.00341](https://arxiv.org/abs/2311.00341) · DOI: [10.1021/acscentsci.3c01629](https://doi.org/10.1021/acscentsci.3c01629)

## TL;DR
A **38M+ DFT calculation × 8,400+ MOF benchmark** for exploring **metal-organic framework (MOF)** candidates for **Direct Air Capture (DAC)**. The inputs are MOF + adsorbate (CO₂, H₂O) structures, and ML models are evaluated with the **same 3-task definition as OC20 (S2EF / IS2RE / IS2RS)**. It is currently the **largest public dataset** of MOF adsorption DFT data.

---

## Construction Methodology

```
Step 1 — Scientific motivation
  ┌──────────────────────────────────────────────┐
  │ - Annual CO₂ emission ~36B tonnes (2020)     │
  │ - Atmospheric CO₂ +50% since preindustrial   │
  │   → ~420 ppm                                 │
  │ - DAC: ambient-condition negative emissions  │
  │ - MOFs: modular, tunable, high porosity      │
  │   → ideal customizable sorbents              │
  │ - Problem: vast chemical space + humidity/   │
  │   temp dependence → efficient screening needed│
  └──────────────────────────────────────────────┘

Step 2 — Building the MOF corpus (8,400+ frameworks)
  ┌──────────────┬────────┬───────────────────────┐
  │ Set          │ Count  │ Source                │
  ├──────────────┼────────┼───────────────────────┤
  │ Pristine MOFs│ 4,942  │ CoRE MOF + curated    │
  │ Defective MOFs│ 3,470  │ defect 1–16% conc.    │
  │ Ultrastable   │   114  │ Nandy fragmented +   │
  │              │        │ recombined            │
  └──────────────┴────────┴───────────────────────┘
  · 57 metals (Zn / Cu / Cd most common)
  · monometallic 89% / bimetallic 10.7% / 
    trimetallic <1%

Step 3 — Adsorbate placement
  · Classical FF + Monte Carlo sampling
  · ~2–6 placements per framework
  · CO₂ only / H₂O only / CO₂ + H₂O / CO₂ + 2H₂O

Step 4 — DFT computation scale
  ┌──────────────────────────────────────────────┐
  │ - 38M+ single-point DFT calculations         │
  │ - 170K converged adsorption energies          │
  │ - ~400M core-hours compute                    │
  │ - largest MOF-adsorption DFT dataset to date │
  └──────────────────────────────────────────────┘

Step 5 — Benchmark task definition (OC20-style)
  ┌─────────────────────────────────────────────┐
  │ S2EF (Structure → Energy + Forces)           │
  │  · Input: MOF+adsorbate single structure     │
  │  · Output: Ẽ_ads + per-atom forces           │
  │                                              │
  │ IS2RE (Initial Structure → Relaxed Energy)  │
  │  · Input: initial placement (non-relaxed)    │
  │  · Output: final relaxed adsorption energy   │
  │                                              │
  │ IS2RS (Initial Structure → Relaxed Struct)  │
  │  · Input: initial placement                   │
  │  · Output: final relaxed 3D coordinates      │
  └─────────────────────────────────────────────┘

Step 6 — Adsorption energy definition
  Ẽ_ads = E_system − E_MOF − n_CO2·E_CO2 − n_H2O·E_H2O
  (tilde = not necessarily relaxed)

Step 7 — Identifying promising MOFs (downstream verification)
  · Directly discover promising MOFs within ODAC23
  · Single + co-adsorption energy analysis
  · Adsorbate-adsorbate interaction energy calculation
```

---

## Real Data Format Examples (paper §Tasks + §Results + Table S3)

### Type A — S2EF input/output (Structure → Energy + Forces)

> **Input** (periodic unit cell):
> ```
> MOF (e.g., CoRE-MOF codes ZIDBEV, IMAGAG, IPIDUH)
>   + adsorbate placement: 1 × CO2 or 1 × H2O or 1 × CO2 + 1 × H2O
>   + initial positions from classical FF + Monte Carlo
> ```
>
> **Output** (DFT ground truth, PBE-D3 functional):
> ```
> Ẽ_ads (non-relaxed adsorption energy, eV)
> Forces per atom (eV/Å, 3D vector)
> ```
>
> **Adsorption energy definition**:
> ```
> Ẽ_ads = E_system − E_MOF − n_CO2·E_CO2 − n_H2O·E_H2O
> ```

### Type B — IS2RE / IS2RS (Initial → Relaxed)

> **IS2RE**: initial placement → final relaxed adsorption energy E_ads
> **IS2RS**: initial placement → final relaxed 3D coordinates of all atoms
>
> Standard OC20-style train/test split, stratified by MOF framework
> (a pristine structure and its defective version are placed in the same split)

### Type C — Promising DAC MOF examples (paper Table S3 / Fig. 3)

> Top promising MOFs identified directly in ODAC23 by DFT:

| CSD code | E_ads(CO₂) − E_ads(H₂O) | Adsorbate-adsorbate E |
|---|---|---|
| **ZIDBEV** | strong CO₂ binding | E_inter_mol ≈ 0 eV (separate adsorption OK) |
| **IMAGAG** | favors CO₂+H₂O coexistence | E_inter_mol = −0.64 eV |
| **IPIDUH** | CO₂+H₂O incompatible | E_inter_mol = +1.04 eV |
| **TUGTAR** | CO₂+H₂O incompatible | E_inter_mol = +0.51 eV |
| **KOQLUZ** | strong MOF rearrangement | E_inter_mol = −2.31 eV |
| **LEWZET** | distortion upon second H₂O adsorption | 2nd E_inter_mol = −5.48 eV |

>
> **Selection criteria** (Findley & Sholl):
> - E_ads(CO₂) < −0.5 eV (sufficient binding at dilute DAC conditions)
> - E_ads(CO₂) is more favorable than E_ads(H₂O) (CO₂ over water)
>
> → Out of 5,079 pristine MOFs, **135** satisfy both criteria (0 with classical FF)

### Type D — Dataset scale distribution (paper §Methods)

> ```
> ┌──────────────────────────┬───────────┐
> │ Pristine MOFs            │   4,942   │
> │ Defective MOFs (1–16%)   │   3,470   │
> │ Ultrastable (Nandy frag) │     114   │
> ├──────────────────────────┼───────────┤
> │ Total MOFs               │   8,400+  │
> │ Adsorbate placements/MOF │   2–6     │
> │ Converged adsorption E   │ 170,000+  │
> │ Single-point DFT calc    │  38M+     │
> │ Compute (core-hours)     │ 400M+     │
> └──────────────────────────┴───────────┘
> ```
>
> Metals: 57 species · monometallic 89% / bimetallic 10.7% / trimetallic <1%
> Most common: Zn, Cu, Cd

---

## Evaluation framework

| Task | Input | Output | Primary Metric |
|---|---|---|---|
| **S2EF** | MOF+adsorbate single config | Ẽ_ads + forces | Energy MAE + Force MAE |
| **IS2RE** | initial (non-relaxed) | relaxed E_ads | Energy MAE within 20 meV/atom |
| **IS2RS** | initial (non-relaxed) | relaxed 3D structure | RMSD vs DFT-relaxed |
| **Adsorbate-adsorbate interaction** | CO₂+H₂O combined | E_inter_mol | qualitative ranking |
| **Co-adsorption energy** | CO₂+H₂O joint vs separate | favorability ranking | DFT ground truth |

→ OC20/OC22 with the **same evaluation protocol** → extended to the MOF/DAC domain

---

## Key Results (paper §Results)

| Finding | Meaning |
|---|---|
| MOFs with various adsorbate-adsorbate interactions identified | ZIDBEV (E=0), IMAGAG (-0.64 eV), IPIDUH (1.04 eV), etc. |
| Co-adsorption distortion effect | LEWZET -5.48 eV upon 2nd H₂O (MOF distortion) |
| Direct identification of promising DAC MOFs | downstream FF screening unnecessary |
| Exposed limitations of FF-based screening | FF is inaccurate at open-metal sites / defects |
| ML models trained on ODAC23 | high-throughput screening possible via DFT-level approximation |

→ **Conclusion**: ML + ODAC23 = a **scalable in-silico verification platform** for DAC sorbent discovery

---

## Limitations
- **DFT functional dependence**: PBE-based, with a gap to other functionals
- **OC20-style framework**: limited to confined geometry, beyond liquid/gas phase
- **Adsorbate limitation**: only CO₂, H₂O (other gases not covered)
- **Compute cost**: 400M core-hours not reproducible
- **Class imbalance**: monometallic 89% → bimetallic/trimetallic data sparse
- **Defect concentration 1–16%**: amorphous / heavily-defective MOFs not covered
- **Time**: 2023 cutoff, comparison needed when successors like ODAC24/25 appear

---

## Related links
- **Paper (ACS Central Sci.)**: [10.1021/acscentsci.3c01629](https://doi.org/10.1021/acscentsci.3c01629)
- **arXiv**: [2311.00341](https://arxiv.org/abs/2311.00341)
- **Official site**: [opencatalystproject.org](https://opencatalystproject.org/) (Open DAC subset)
- **GitHub**: [Open-Catalyst-Project/ocp](https://github.com/Open-Catalyst-Project/ocp)
- **Author affiliations**: Meta FAIR / Georgia Tech / ORNL
- **Follow-up work using this dataset**: OMat24 (Meta 2024, referencing OpenDAC's design), MLIP Arena gas-adsorption task
- **Related datasets**: OC20 (Chanussot 2021), OC22 (Tran 2023), OMat24 (Barroso-Luque 2024), CoRE MOF database (Chung 2014)
