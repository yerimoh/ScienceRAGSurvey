---
title: "ZINC-22—A Free Multi-Billion-Scale Database of Tangible Compounds for Ligand Discovery"
bib_key: "DBLP:journals/jcisd/TingleTCGKDMI23"
year: 2023
domain: chem
type: dataset
venue: Journal of Chemical Information and Modeling
paper_link: https://doi.org/10.1021/acs.jcim.2c01253
---
# ZINC-22—A Free Multi-Billion-Scale Database of Tangible Compounds for Ligand Discovery

DBLP:journals/jcisd/TingleTCGKDMI23 | 2023 | Journal of Chemical Information and Modeling | dataset | [chem] | [paper](https://doi.org/10.1021/acs.jcim.2c01253)

**DB**: ZINC-22
**DB size**: tens of billions scale make-on-demand compounds
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CartBlanche (GUI), Globus, Amazon AWS, Oracle OCI

> Journal of Chemical Information and Modeling | 2023 | dataset | chem
#### 📌 TL;DR
ZINC-22 is a multi-billion-scale ligand discovery DB built on a make-on-demand compound library of tens of billions in scale, provided together with CartBlanche, a similarity search tool that scales sublinearly with size.

#### 🎯 Background
**Limitations of existing infrastructure**
- The purchasable chemical space has expanded rapidly to a scale of tens of billions of molecules, causing slowdown issues with existing DB organization methods
- There was no fast similarity search tool at the billion-molecule scale
**Why this system is needed**
- Rapid lookup of the conformation, charge, LogP, solvation energy, etc. required for molecular docking of make-on-demand libraries
- A scalable DB architecture is needed to prepare for the era of trillion-scale molecules

#### 🔨 Architecture
It is a compound DB derived from a multi-billion scale make-on-demand library. Similar molecule search is possible through the CartBlanche GUI, using a similarity method that scales sublinearly with the number of molecules. Molecular diversity analysis shows that as the DB size increases, the Bemis-Murcko scaffold count also increases log-linearly. It is also accessible on the Amazon AWS and Oracle OCI clouds.

#### 📥 Access
| Method | Description |
|---|---|
| CartBlanche GUI | cartblanche22.docking.org similarity search |
| Globus | large-scale data transfer |
| Amazon AWS | cloud access |
| Oracle OCI | cloud access |

#### 📤 Data formats
- 3D conformations
- partial atomic charges
- cLogP values
- solvation energy
- SMILES

#### 📊 Key statistics (per paper)
| Item | Value |
|---|---|
| DB scale | tens of billions make-on-demand compounds |
| Scaffold diversity | log increase in Bemis-Murcko scaffolds per 100x increase in DB size |

#### ⚠️ Limitations
- Due to the make-on-demand nature, the actual synthesis success rate varies by compound
- Considerable computational resources are also required for preprocessing before docking
- The limitations of the current methodology need to be discussed when reaching the trillion scale

## Related links
- **Paper**: [ZINC-22 — A Free Multi-Billion-Scale Database of Tangible Compounds](https://doi.org/10.1021/acs.jcim.2c01253)
