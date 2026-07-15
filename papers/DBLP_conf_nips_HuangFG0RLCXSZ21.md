---
title: "TDC: Therapeutics Data Commons — Machine Learning Datasets and Tasks for Drug Discovery and Development"
bib_key: "DBLP:conf/nips/HuangFG0RLCXSZ21"
year: 2021
domain: medical, bio, chem
type: benchmark
venue: NeurIPS Datasets and Benchmarks 2021
paper_link: https://arxiv.org/abs/2102.09548
---
# TDC (Therapeutics Data Commons): 66 AI-ready Datasets × 22 Learning Tasks Umbrella Benchmark

> NeurIPS 2021 Datasets and Benchmarks Track | Benchmark Suite | medical · bio · chem
> Kexin Huang, Tianfan Fu, Wenhao Gao, Yue Zhao, Yusuf H. Roohani, Jure Leskovec, Connor W. Coley, Cao Xiao, Jimeng Sun, Marinka Zitnik — Harvard / Stanford / MIT / Georgia Tech / IBM / UIUC
> DBLP: `conf/nips/HuangFG0RLCXSZ21` · arXiv: [2102.09548](https://arxiv.org/abs/2102.09548) · Web: [tdcommons.ai](https://tdcommons.ai)

## TL;DR
An integrated evaluation platform spanning the full range of drug discovery and development (small molecule → biologics → clinical trial), with **66 AI-ready datasets × 22 learning tasks**. It provides **29 public leaderboards**, **17 molecule generation oracles**, **23 evaluation strategies**, **33 data splits/functions**, and an open Python library. It is effectively the standard evaluation hub for Database-verified Prediction systems (e.g., CLADD).

---

## Construction Methodology

```
Structure: 3 learning paradigms × 22 tasks × 66 datasets

┌──────────────────────────────────────────────────────────────┐
│ 1. single_pred (single-instance prediction) — 9 tasks       │
│    └─ ADME (Absorption·Distribution·Metabolism·Excretion) Property Prediction │
│    └─ Tox (Toxicity) Prediction                             │
│    └─ HTS (high-throughput screening) Prediction             │
│    └─ QM (quantum-mechanical properties)                    │
│    └─ Yields (reaction yield) Prediction                    │
│    └─ Paratope / Epitope Prediction (antibody binding site) │
│    └─ Antibody Developability Prediction                     │
│    └─ CRISPR Repair Outcome Prediction                       │
│                                                               │
│ 2. multi_pred (multi-instance prediction) — 7 tasks         │
│    └─ DTI (Drug-Target Interaction)                          │
│    └─ DDI (Drug-Drug Interaction)                            │
│    └─ PPI (Protein-Protein Interaction)                      │
│    └─ GDA (Gene-Disease Association)                         │
│    └─ DrugRes (Drug Response on cell lines, GDSC)            │
│    └─ DrugSyn (Drug Synergy)                                 │
│    └─ Peptide MHC binding / TCR-Epitope                      │
│                                                               │
│ 3. generation — 6 tasks                                       │
│    └─ Molecule Generation (de novo design)                   │
│    └─ Reaction / Retrosynthesis Prediction                   │
│    └─ Forward Synthesis Prediction                           │
│    └─ Paratope Antibody Sequence Generation                  │
│    └─ MolOpt (Molecule Optimization with 17 oracles)         │
└──────────────────────────────────────────────────────────────┘

Step 1 — Dataset collection + curation
  Download raw data from 66 public clinical/biochemical DBs
  → Normalize into a unified schema (standardize SMILES, sequence, label formats)
  → Remove missing values/duplicates, standardize train/val/test splits

Step 2 — Standardize the evaluation protocol
  · 33 data functions/splits: random/scaffold/cold-start/temporal/etc.
  · 23 evaluation strategies: AUROC/AUPRC/RMSE/MAE/Top-K/etc.
  · 17 molecule generation oracles: QED/SA/LogP/JNK3/GSK3β/DRD2/etc.
                                    (the oracle collection from the PMO benchmark)

Step 3 — 29 Public Leaderboards
  · ADMET Group Leaderboard
  · Docking Group Leaderboard
  · Time-trackable public comparisons (reproducibility guaranteed)

Step 4 — Python Library + Documentation
  └─ pip install PyTDC
  └─ Unified API in the style of `from tdc.single_pred import ADME`
  └─ tdcommons.ai official documentation + Tutorial
```

---

## Direct quotations from the original (arXiv:2102.09548 §Abstract body)

> *"Therapeutics machine learning is an emerging field with incredible opportunities for innovation and impact ... we introduce **Therapeutics Data Commons (TDC), the first unifying platform** to systematically access and evaluate machine learning across the entire range of therapeutics. To date, TDC includes **66 AI-ready datasets spread across 22 learning tasks** and spanning the discovery and development of safe and effective medicines."*

> *"TDC also provides an ecosystem of tools and community resources, including **33 data functions and types of meaningful data splits**, **23 strategies for systematic model evaluation**, **17 molecule generation oracles**, and **29 public leaderboards**. All resources are integrated and accessible via an open Python library."*

> *"We carry out extensive experiments on selected datasets, demonstrating that even the strongest algorithms **fall short of solving key therapeutics challenges**, including real dataset distributional shifts, multi-scale modeling of heterogeneous data, and robust generalization to novel data points."*

---

## Input / Output (by learning paradigm)

| Paradigm | Input | Output | Representative task |
|---|---|---|---|
| **single_pred** | single molecule/protein (SMILES, sequence) | scalar/class label | ADMET, Toxicity (includes Tox21, SIDER, ClinTox, etc.) |
| **multi_pred** | (drug, target) or (drug, drug) pair | interaction score / class | DTI (includes BindingDB, DAVIS, KIBA), DDI |
| **generation** | constraint / oracle score | novel molecule SMILES | MolOpt, retrosynthesis |

**Examples when using oracles**:
- QED / SA → molecular druglikeness
- DRD2 / JNK3 / GSK3β → bioactivity prediction
- Docking module → Vina score (PMO subset)

---

## Key evaluation results (paper §body + Table)

### Evaluation setup
- Operates **29 public leaderboards** (ADMET Group, Docking Group, etc.)
- **23 evaluation strategies** (AUROC, AUPRC, RMSE, MAE, Top-K Recall, Spearman, etc.)
- **33 data splits** (random, scaffold, cold-start, temporal, lo-shot, etc.)

### Core findings (quoted from paper §body)
- "even the **strongest algorithms fall short** of solving key therapeutics challenges"
- Lack of robustness to **Distribution shift** (across time and across labs)
- Immature integration of **Multi-scale modeling** (small molecule ↔ protein ↔ disease)
- Generalization limits on **Novel data points**

---

## Dataset statistics (representative subset)

| Category | Representative datasets |
|---|---|
| ADMET | Caco2, HIA, Pgp, Bioavailability, Lipophilicity, Solubility, BBBP, PAMPA, Half-Life, Clearance, hERG, AMES, DILI |
| Toxicity | ClinTox, Tox21, ToxCast, LD50 |
| HTS | SARS-CoV-2 in vitro, HIV |
| DTI | BindingDB (Kd/Ki/IC50/EC50), DAVIS, KIBA |
| DDI | DrugBank DDI, TWOSIDES |
| GDA | DisGeNET |
| DrugRes | GDSC cell-line response |
| Generation | MOSES, ZINC 250K, ChEMBL, USPTO retrosynthesis |

→ Frequently used when evaluating Database-verified Prediction RAG systems (e.g., CLADD).

---

## Limitations (paper §Limitations + points raised by follow-up work)
- **Dataset quality variance**: some small-scale datasets lack sufficient variation statistics
- **Distribution shift** evaluation is insufficient (assumes uniformity across time/lab/domain)
- **Time-dependent data**: newly discovered drug-targets are reflected slowly in the leaderboards
- **Benchmark gaming**: leaderboard optimization can become decoupled from real medical value
- **Balance across dataset types**: skewed toward small molecules, with a low proportion of biologics/macromolecules
- **Closed-set evaluation**: cannot measure generalization to undiscovered molecules/proteins

---

## Related links
- **Paper (arXiv)**: [2102.09548](https://arxiv.org/abs/2102.09548)
- **NeurIPS 2021 Datasets and Benchmarks Track**: [Round 1 paper](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/4c7a167bb329bd92580a99ce422d6fa6-Abstract-round1.html)
- **DBLP**: [conf/nips/HuangFG0RLCXSZ21](https://dblp.org/rec/conf/nips/HuangFG0RLCXSZ21.html)
- **Official homepage**: [tdcommons.ai](https://tdcommons.ai)
- **PyPI**: `pip install PyTDC`
- **Follow-up RAG work using this benchmark**: CLADD (Database-verified Prediction), PMO (MolOpt subset reuse), Patho-AgenticRAG (Pathology subset), etc. — a standard evaluation hub for pharmaceutical RAG
