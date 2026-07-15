---
title: "The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts"
bib_key: "DBLP:journals/corr/abs-2206-08917"
year: 2022
domain: material
type: dataset
venue: Journal of Chemical Theory and Computation (arXiv preprint 2022)
paper_link: https://arxiv.org/abs/2206.08917
---
# The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts

DBLP:journals/corr/abs-2206-08917 | 2022 | Journal of Chemical Theory and Computation | dataset | [material] | [paper](https://arxiv.org/abs/2206.08917)

**DB**: Open Catalyst 2022 (OC22)
**DB size**: 62,331 DFT relaxations (~9,854,504 single point calculations, per the paper)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: Total energy prediction (S2EF-Total), IS2RE-Total
**Eval Metric**: Energy MAE, Force MAE
**Method Name**: OC22 Dataset, Open Catalyst Project (opencatalystproject.org)

> Journal of Chemical Theory and Computation | 2022 | dataset | material
#### 📌 TL;DR
A dataset of 62,331 DFT relaxations for oxide electrocatalyst (OER catalyst) materials not covered by OC20, which defines a generalized total energy prediction task beyond adsorption energy and demonstrates performance improvements through joint training with OC20.

#### 🎯 Background
**Limitations of existing infrastructure**
- OC20 focuses on nitrogen/carbon/oxygen chemistries, so training data for oxide electrocatalyst materials is lacking
- Oxygen evolution reaction (OER) catalysts are central to renewable energy storage and conversion, yet ML training data is insufficient
- A separate benchmark is needed for oxides where long-range electrostatic and magnetic interactions are important

**Why this system is needed**
- Systematically covers diverse surface coverages and adsorbate combinations of oxide materials
- Extends the applicability of ML models with a generalized total energy prediction task beyond adsorption energy
- Demonstrates the potential for performance improvements on both datasets through joint training with OC20

#### 🔨 Architecture
Structural relaxation of oxide slab structures is performed with VASP-based DFT calculations (RPBE functional). It includes diverse oxide materials, surface coverages, and adsorbates, and through the generalized total energy tasks (S2EF-Total, IS2RE-Total) it focuses on predicting the total system energy rather than only the adsorption energy. It is provided together with GNN baselines such as GemNet-OC.

#### 📥 Access
| Method | Description |
|---|---|
| Official website | opencatalystproject.org — data download |
| GitHub | github.com/Open-Catalyst-Project/ocp — code and baselines |
| Leaderboard | public benchmark for the total energy task |

#### 📤 Data formats
- DFT relaxation trajectories (initial to final structures, energy and forces at each step)
- Total energy (eV)
- Atomic forces (eV/Å)
- Oxide slab structures (ASE Atoms format)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total DFT relaxation calculations | **62,331** |
| Single point energy calculations | **~9,854,504** |
| Energy prediction improvement (joint training, OC20) | **~19%** (based on total energy) |
| Force prediction improvement (joint training, OC22) | **~9%** |
| Best model performance (energy prediction, OC20+OC22) | GemNet-OC ~36% improvement |

#### ⚠️ Limitations
- Smaller data scale compared to OC20 (60K vs 1.28M entries)
- Long-range electrostatic and magnetic interactions are important given the nature of oxides, but current GNNs do not fully capture them
- Solvent and electrolyte effects are not included
- Systematic errors relative to experimental values exist due to the use of the RPBE functional

## Related links
- **Paper**: [The Open Catalyst 2022 (OC22) Dataset (arXiv:2206.08917)](https://arxiv.org/abs/2206.08917)
