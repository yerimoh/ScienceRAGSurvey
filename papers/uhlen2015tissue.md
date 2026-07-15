---
title: "Tissue-based map of the human proteome"
bib_key: "uhlen2015tissue"
year: 2015
domain: medical, bio
type: dataset
venue: Science
paper_link: https://doi.org/10.1126/science.1260419
---
# Tissue-based map of the human proteome

uhlen2015tissue | 2015 | Science | dataset | [medical, bio] | [paper](https://doi.org/10.1126/science.1260419)

**DB**: Human Protein Atlas (HPA)
**DB size**: 32 tissues and organs; over 90% of estimated protein-coding genes detected
**DB Open/Private**: Open (proteinatlas.org)
**Modality**: Image (immunohistochemistry), Genomic (transcriptome), Structured Table (protein expression data)
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Human Protein Atlas (proteinatlas.org)

> Science | 2015 | dataset | medical, bio

#### 📌 TL;DR
An interactive web database that integrates quantitative transcriptomics and tissue-microarray-based immunohistochemistry across 32 human tissues and organs to build a spatial protein expression map down to the single-cell level, detecting over 90% of the human proteome.

#### 🎯 Background
**Limitations of existing infrastructure**
- Lack of spatial protein localization information at the tissue and organ level
- Transcriptomic data alone cannot capture protein expression patterns and subcellular localization
- No integrated resource for the human secretome, membrane proteome, and cancer proteome

**Why this system is needed**
- A spatial protein expression map is needed to understand human biology and disease
- An integrated omics platform is needed for drug target and biomarker discovery

#### 🔨 Architecture
An integrated omics approach led by KTH Royal Institute of Technology (Sweden). Integrates quantitative transcriptomics (mRNA) + tissue-microarray-based immunohistochemistry across 32 tissues and organs. Captures spatial protein localization at the single-cell level. Explores the human secretome, membrane proteome, druggable proteome, cancer proteome, and metabolic functions. All data is integrated and provided through an interactive web-based database (proteinatlas.org).

#### 📥 Access
| Method | Description |
|---|---|
| Human Protein Atlas portal | https://www.proteinatlas.org — free public access |
| DOI | https://doi.org/10.1126/science.1260419 |

#### 📤 Data formats
- Immunohistochemistry images (tissue microarray)
- RNA expression data (TPM, per tissue)
- Protein expression levels (per tissue/cell type)
- Antibody specificity information

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| Number of tissues/organs analyzed | **32** |
| Proportion of protein-coding genes detected | **over 90%** |

#### ⚠️ Limitations
- Antibody-based detection methods are subject to potential cross-reactivity
- Protein expression levels are semi-quantitative
- Cell lines and some rare tissues are not included

## Related links
- **Paper**: [Tissue-based map of the human proteome](https://doi.org/10.1126/science.1260419)
