---
title: "COSMIC: the Catalogue Of Somatic Mutations In Cancer"
bib_key: "DBLP:journals/nar/TateBJSBBBCCDFH19"
year: 2019
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gky1015
---
# COSMIC: the Catalogue Of Somatic Mutations In Cancer

DBLP:journals/nar/TateBJSBBBCCDFH19 | 2019 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gky1015)

**DB**: COSMIC (Catalogue Of Somatic Mutations In Cancer)
**DB size**: ~6M coding variants (v86, 2018.8); 1.4M tumor samples; 719-gene Cancer Gene Census
**DB Open/Private**: Open (free for academics) / commercial-organization license required
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: COSMIC website / REST API / FTP download

> Nucleic Acids Research | 2019 | dataset | medical
#### 📌 TL;DR
A catalogue of cancer somatic mutations operated by the Wellcome Sanger Institute, providing approximately 6M coding mutations, 1.4M tumor samples, a 719-gene Cancer Gene Census, and 10 cancer Hallmarks annotations as of v86.

#### 🎯 Background
**Limitations of existing infrastructure**
- Cancer whole-genome and exome analysis results were scattered across individual papers, and there was no repository that integrated them in a comparable format
- There was no authoritative, evidence-based list classifying which genes are cancer drivers
- Beyond somatic mutations, there was a need to integrate diverse somatic changes such as fusion genes, copy-number variants, and methylation

**Why this system is needed**
- As a common reference resource for cancer genomics research, mutation spectra, mutational signatures, and driver genes must be systematically recorded
- Drug development and clinical interpretation require searches that consider the context of somatic mutations (tissue type, cancer type)

#### 🔨 Architecture
COSMIC is composed of several data sections.
- **Somatic Mutations**: somatic variants from manually curated papers plus large-scale whole-exome and genome studies
- **Cancer Gene Census (CGC)**: list of cancer-causing genes; divided into Tier 1 (direct evidence) and Tier 2 (indirect evidence); annotated with 10 cancer Hallmarks
- **COSMIC Signatures**: signatures of somatic mutation patterns (SBS, DBS, ID types)
- **Other variant types**: gene fusions, copy-number variants (CNV), gene expression abnormalities, methylation, drug-resistance mutations

#### 📥 Access
| Method | Description |
|---|---|
| COSMIC website | cancer.sanger.ac.uk/cosmic — free search and visualization |
| FTP download | full dataset files; free academic registration |
| REST API | programmatic queries; cosmic-cancer.org |
| Commercial license | separate contract for corporate and commercial purposes |

#### 📤 Data formats
- Somatic variant TSV/VCF files
- Cancer Gene Census TSV (Tier, Hallmarks, cancer type)
- Mutational signature CSV (SBS/DBS/ID matrices)
- Drug-resistance mutation tables

#### 📊 Key statistics (per paper, v86 / August 2018)
| Item | Value |
|---|---|
| Number of coding variants | **~6,000,000** (5,977,977) |
| Number of tumor samples | **~1,400,000** (1,391,372) |
| Number of Cancer Gene Census genes | **719** |
| Number of curated papers | **26,251** |
| Number of large-scale WGS/WES studies | **457** |
| Number of gene fusions | **19,368** |
| Number of copy-number variants | **1,179,545** |
| Number of drug-resistance mutations | **360 unique alleles** (24 drugs) |
| Cancer Hallmarks annotations | **10** |

#### ⚠️ Limitations
- Free for academics, but commercial-organization use incurs license fees — a constraint for commercial RAG deployment
- Being manually curation-based, there is a lag in reflecting the latest research
- Coverage imbalance across tissue types: breast and colorectal cancer are over-represented
- Somatic-mutation-centric, so germline variant interpretation requires referencing ClinVar and OMIM

## Related links
- **Paper**: [Tate et al., Nucleic Acids Research 2019](https://doi.org/10.1093/nar/gky1015)
