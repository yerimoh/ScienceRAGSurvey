---
title: "The Open Catalyst 2020 (OC20) Dataset and Community Challenges"
bib_key: "DBLP:journals/corr/abs-2010-09990"
year: 2020
domain: material
type: dataset
venue: ACS Catalysis (arXiv preprint 2020; published 2021)
paper_link: https://arxiv.org/abs/2010.09990
---
# The Open Catalyst 2020 (OC20) Dataset and Community Challenges

DBLP:journals/corr/abs-2010-09990 | 2020 | ACS Catalysis | dataset | [material] | [paper](https://arxiv.org/abs/2010.09990)

**DB**: Open Catalyst 2020 (OC20)
**DB size**: 1,281,040 DFT relaxations (~264,890,000 single point evaluations, per the paper)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: IS2RE (initial → relaxed energy), S2EF (structure → energy/forces), IS2RS (initial → relaxed structure)
**Eval Metric**: MAE, EwT (Energy within Threshold), Force MAE
**Method Name**: OC20 Dataset, Open Catalyst Project (opencatalystproject.org)

> ACS Catalysis | 2020/2021 | dataset | material
#### 📌 TL;DR
A dataset of 1.28 million DFT relaxation calculations released by Facebook AI Research (now Meta) and Carnegie Mellon University for catalyst discovery used in applications such as solar fuels, long-term energy storage, and renewable fertilizer synthesis; it provides a community benchmark for developing machine-learning potential functions.

#### 🎯 Background
**Limitations of existing infrastructure**
- In computational catalysis, the dataset scale needed for training ML models is markedly smaller than in related fields
- A systematic dataset is needed to accelerate the discovery of catalysts for solar fuels, renewable ammonia synthesis, and long-term energy storage
- There is no large-scale benchmark for developing general-purpose ML models that cover both surface composition and adsorbate-molecule diversity

**Why this system is needed**
- Systematically includes a broad range of material surfaces and adsorbate molecules across nitrogen/carbon/oxygen chemistries
- Establishes a foundation for reproducible ML model development through predefined train/validation/test splits
- Promotes community contributions through a public leaderboard

#### 🔨 Architecture
DFT-based structural relaxation (VASP, RPBE functional) calculations generate adsorption energies and atomic forces for catalyst surfaces. It covers a broad chemical space by systematically combining diverse bulk materials, surface Miller indices, and adsorbate molecules (N, C, O chemistries). It is provided together with GNN-based baselines (CGCNN, SchNet, DimeNet++).

#### 📥 Access
| Method | Description |
|---|---|
| Official website | opencatalystproject.org — data download |
| GitHub | github.com/Open-Catalyst-Project/ocp — code and baselines |
| Leaderboard | public benchmark leaderboard |

#### 📤 Data formats
- DFT relaxation trajectories (initial to final structures, energy/forces at each step)
- Adsorption energy (eV)
- Atomic forces (eV/Å)
- Surface slab structures (ASE Atoms format)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total DFT relaxations | **1,281,040** |
| Single point energy calculations | **~264,890,000** |
| Chemistry | nitrogen (N), carbon (C), oxygen (O) chemistry |
| Core tasks | 3 (IS2RE, S2EF, IS2RS) |
| Baseline GNNs | CGCNN, SchNet, DimeNet++ |

#### ⚠️ Limitations
- Scope limited to nitrogen/carbon/oxygen chemistries (oxide catalysts are expanded in OC22)
- Systematic errors relative to experimental values due to the use of the RPBE functional
- Solvent/electrolyte effects not included (only gas-phase adsorption conditions considered)
- No upper bound on ML model size has been established, so larger models may achieve better performance

## Related links
- **Paper**: [The Open Catalyst 2020 (OC20) Dataset (arXiv:2010.09990)](https://arxiv.org/abs/2010.09990)
- **Published version**: [ACS Catalysis, 2021, DOI:10.1021/acscatal.0c04525](https://doi.org/10.1021/acscatal.0c04525)
