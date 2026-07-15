---
notion_id: 355f2dcd-4912-81ca-94c7-d04120963836
title: Three-Dimensional Convolutional Neural Networks and a Cross-Docked Data Set for Structure-Based Drug Design
bib_key: DBLP:journals/jcisd/FrancoeurMSJISK20
year: 2020
domain: bio, medical, chem
type: benchmark
venue: J. Chem. Inf. Model.
paper_link: https://doi.org/10.1021/acs.jcim.0c00411
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Three-Dimensional Convolutional Neural Networks and a Cross-Docked Data Set for Structure-Based Drug Design

> J. Chem. Inf. Model. (ACS) | 2020 | Benchmark | bio, medical, chem

## TL;DR
CrossDocked2020 is a structure-based drug design (SBDD) ML benchmark composed of 22.5 million poses obtained by cross-docking protein-ligand complexes from the PDB. It has become the de facto standard for evaluating protein-ligand binding affinity prediction and SBDD generative models.

## Background
**Limitations of existing benchmarks**
- PDBbind-based approaches dominate: they emphasize re-docking the same ligand back into the same structure, leading to overly optimistic evaluation of scalability in real drug discovery
- ML model comparisons relied on method-specific individual datasets, making it impossible to gauge algorithm quality
- There was no evaluation of the generalization ability to predict new ligands for a given target (non-cognate)

**Why this benchmark is needed**
- Provides large-scale cross-docking (non-cognate ligand-pocket pair) pose data, enabling evaluation closer to real drug discovery conditions
- Supports stricter and fairer generalization evaluation through cluster-based splits
- Enables fair comparison across methods with standardized train/val/test splits plus multiple split methods
- Established as the de facto standard training and evaluation dataset for SBDD generative models (Pocket2Mol, TargetDiff, ResGen, etc.)

## Construction Methodology
**Step 1 — Selecting data sources**
- Collected experimentally determined protein-ligand complex structures from the PDB (Protein Data Bank)
- Leveraged similar-pocket cluster information from the Pocketome DB
- Preprocessing: clustered each pocket using a ProBiS z-score threshold of 3.5

**Step 2 — Construction pipeline (Cross-docking)**
```
Collect PDB protein-ligand complexes
    ↓
Cluster similar pockets (ProBiS algorithm, z-score 3.5)
    ↓
Cross-dock ligands within the same cluster ↔ non-cognate pockets
(AutoDock Vina / Gnina)
    ↓
Pose filtering (RMSD, binding energy criteria)
    ↓
Counter-example generation (add incorrect poses)
    ↓
Completed 22.5M-pose dataset
```

- Ligands are docked into similar pockets (non-cognate) rather than only their own original pocket (cognate) → a more realistic virtual screening scenario
- Counter-example poses are added via iterative training-set construction → improves model robustness

**Step 3 — Quality validation**
- Evaluated binding affinity prediction and pose selection performance using known CNN models (Def2018, etc.)
- Confirmed data quality via cross-validation against the PDBbind Core/General sets
- Quantified artificial bias through ligand-only (excluding protein structure) model evaluation

**Step 4 — Dataset composition and release**
- Total: 22.5M poses (13,780 unique ligands, 2,922 pockets, 18,450 complexes)
- Proportion including binding affinity data: 41.9%
- Splits: provides cluster-based cross-validation splits
- Preprocessed subset used in follow-up papers such as Pocket2Mol: ~100,000 training complexes, 100 test pockets
- Data, model weights, and code released on GitHub (gnina/models)

## Input
Input format: protein 3D structure (PDB coordinates) + ligand SMILES/3D coordinates

| Component | Content | Scale |
|---|---|---|
| Total poses | Cross-docked protein-ligand poses | 22,584,102 |
| Unique ligands | Unique small-molecule ligands | 13,780 |
| Pockets | Protein binding pockets | 2,922 |
| Complexes | Pocket-ligand pairs | 18,450 |
| Binding affinity data | Proportion of complexes with experimental affinity | 41.9% |
| Counter-examples | Incorrect poses (for iterative training) | 11,892,173 |

**Provided fields**
| Field name | Description |
|---|---|
| Protein PDB file | Receptor 3D coordinates |
| Ligand SDF/mol2 | Ligand 3D pose coordinates |
| Vina score | Docking binding energy (kcal/mol) |
| RMSD | Pose deviation relative to the crystal structure |
| Binding affinity (pKi/pKd) | Experimental value (when included) |
| Cluster ID | Similar-pocket cluster membership |

## Output (Evaluation format)
**Original-paper evaluation tasks (CNN model evaluation)**
- Binding affinity prediction: RMSE, Pearson R
- Binding pose classification (correct pose vs. counter-example): AUC
- Pose selection accuracy: accuracy of selecting the lowest-RMSD pose

**SBDD generative model evaluation (per follow-up papers)**
- Vina Dock / Vina Score: binding energy (lower is better)
- %↑ Vina: proportion superior to the native ligand
- QED: drug-likeness
- SA: synthetic accessibility
- Lipinski Rule of 5 compliance
- LogP: lipophilicity
- PB-Valid (PoseBusters): physical validity
- CNN Affinity (GNINA): CNN-based binding affinity

## Example items (by SBDD task type)
**Binding affinity prediction example**
- Q: Given the 3D coordinates of a protein pocket + the 3D pose of a docked ligand, predict the binding affinity (pKd) of this complex.
- A: pKd ≈ 7.2 (around IC50 ≈ 63 nM) | Basis: experimental measurement

**Pose selection example**
- Q: Among 5 docking poses of the same ligand, select the pose closest to the crystal structure (RMSD < 2Å).
- A: Pose 3 (RMSD = 1.43Å) | Basis: CNN affinity score

**SBDD generation evaluation example (Pocket2Mol, Rag2Mol, etc.)**
- Q: Given the 3D structure of a protein pocket, generate a small molecule with high binding affinity and good drug-likeness.
- A: Evaluation: check Vina Dock < -8.0 kcal/mol, QED > 0.5, SA > 0.5, and Lipinski compliance

## Key evaluation results (original paper)
**CNN model performance (CrossDocked2020 test)**
| Model | Task | Performance |
|---|---|---|
| Dense CNN (5-model ensemble) | Affinity prediction (RMSE) | 1.42 |
| Dense CNN (5-model ensemble) | Affinity prediction (Pearson R) | 0.612 |
| Dense CNN (5-model ensemble) | Pose classification (AUC) | 0.956 |
| Dense CNN (5-model ensemble) | Pose selection accuracy | 68.4% |

**SBDD generative model performance (per the Rag2Mol paper)**
| Model | Vina Dock | QED | SA | Note |
|---|---|---|---|---|
| AR | Baseline | Baseline | Baseline | Autoregressive |
| Pocket2Mol | Improved | Improved | Improved | Autoregressive + graph |
| TargetDiff | Improved | Reference | Reference | Diffusion-based |
| **Rag2Mol** | **Best** | **Best** | **Improved** | RAG-based |

## Limitations
- Inherent PDB data bias: centered on already-known ligand-pocket pairs → does not cover the entire chemical space
- Low accuracy of cross-docking poses relative to experimental structures
- Binding affinity data included for only 41.9% of the total (the rest are unlabeled)
- Protein flexibility not considered (rigid receptor docking)
- Inherent scoring-function bias of the docking software (Vina/Gnina)

## Related links
- **Paper link**: [https://doi.org/10.1021/acs.jcim.0c00411](https://doi.org/10.1021/acs.jcim.0c00411)
- **GitHub (gnina/models)**: [https://github.com/gnina/models](https://github.com/gnina/models)
- **Papers using this benchmark**: Pocket2Mol (ICML 2022), TargetDiff (ICLR 2023), ResGen (Nature MI 2023), FLAG (ICLR 2023), Rag2Mol (Briefings in Bioinformatics 2025)
