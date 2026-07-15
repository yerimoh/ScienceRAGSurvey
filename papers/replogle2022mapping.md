---
notion_id: 355f2dcd-4912-8156-9420-cc42270da4bf
title: Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq
bib_key: replogle2022mapping
year: 2022
domain: bio
type: benchmark
venue: Cell
paper_link: https://doi.org/10.1016/j.cell.2022.05.013
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq

> Cell (2022) + bioRxiv (2024) | benchmark | bio
## 📌 TL;DR
A large-scale single-cell Perturb-seq dataset based on CRISPRi. An in silico perturbation prediction benchmark dataset consisting of 4 human cell lines, 2,023 gene-knockdown conditions, and ~0.6M cells.
## 🎯 Background
### Limitations of existing benchmarks
- Previous perturbation prediction datasets (Norman, Adamson, etc.) were limited to a few single cell lines and a small number of perturbations
- There was no dataset that enabled evaluation of cross-cell-type generalization
- Datasets covering only combinatorial perturbations (GEARS) vs. no multi-cell-line evaluation
### Why this dataset was needed
- Genome-scale CRISPRi makes a large-scale attempt possible, covering most of the **essential genes** in the receptor
- Inclusion of **four or more cell lines** enables cell-type-aware model evaluation
- Provides a consistent comparison environment through a unified preprocessing scheme (2,000 HVGs, CRISPRi)
## 🔨 Construction Methodology
**Step 1: Data source selection**
- Replogle et al. (2022, Cell): Genome-scale Perturb-seq experiment. The Weissman lab (UCSF) used CRISPRi to knock down ~10,000 essential genes in the K562 and RPE1 cell lines
- Nadig et al. (2024, bioRxiv): Extended by including additional cell lines (Jurkat, HepG2)

**Step 2: Construction pipeline**
- CRISPRi viral library design → cell capture (pooled CRISPR screen)
- Single-cell RNA sequencing on the 10x Genomics Chromium platform
- Confirmation of gene knockdown based on barcodes, cell assignment
- Distinction between control cells (non-targeting) vs. knockdown cell conditions

**Step 3: Quality validation**
- Cell quality QC: mitochondrial gene markers, doublet filtering
- Barcode QC: filtering for a single access only or two or more active
- Knockdown efficiency validation: checking the number of DE genes and knockdown strength

**Step 4: Dataset composition and release**
- Composition scheme: follows the STATE (Adduri et al. 2025) preprocessing scheme — train/test split
- Test perturbations: 1,635
- Publicly distributed via CellxGene and others (h5ad format)
## 📥 Input
| Item | Content |
| Source | Replogle et al. 2022 (Cell) + Nadig et al. 2024 (bioRxiv) |
| Data type | single-cell RNA-seq (Perturb-seq) |
| Algorithm | CRISPRi (CRISPR interference, gene-expression knockdown) |
| Total cell count | ~0.6M |
| Covered genes | ~2,023 (centered on essential genes such as amino-acid tRNA synthesis) |
| Cell lines | K562 (CML), RPE1 (retinal epithelium), Jurkat (T cell), HepG2 (liver cancer) |
| Feature dimension | 2,000 HVGs (Highly Variable Genes) |
| Format | h5ad (AnnData) |

## 📤 Output (answer format)
- **Output form**: transcriptomic expression profile of cells after perturbation (real-valued numeric [float])
- **Evaluation metrics**: W1, W2 (Wasserstein distance), DE-Spearman, Pearson Δ, MSE, MAE, PDS
- **Notable point**: requires both distribution-level accuracy and individual gene-level accuracy; enables evaluation of cell-type-specific generalization ability
## 📊 Key evaluation results (per the PT-RAG paper)
| Model | W2 (↓) | Notes |
| PT-RAG (proposed) | improvement over STATE | best |
| STATE | 646.1 | previous SOTA |
| Vanilla RAG | 1189.5 | case where retrieval is actually harmful |
| GEARS | — | GNN-based baseline |

## ⚠️ Limitations
- Focused on essential genes — implicitly biased toward only genes within highly upstream transcription
- Only CRISPRi knockdown is evaluated (amplification-based attempts not included)
- No combinatorial perturbations
## 🔗 Related links
- **Original paper (Replogle 2022)**: [https://doi.org/10.1016/j.cell.2022.05.013](https://doi.org/10.1016/j.cell.2022.05.013)
- **Nadig 2024**: [https://doi.org/10.1101/2024.11.22.624843](https://doi.org/10.1101/2024.11.22.624843)
- **Papers using this dataset**:
	- PT-RAG (Di Francesco et al., Gen2 @ ICLR 2026)
	- STATE (Adduri et al. 2025)
	- PerturbDiff (2026)
