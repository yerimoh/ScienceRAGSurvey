---
title: "The DisGeNET knowledge platform for disease genomics: 2019 update"
bib_key: "DBLP:journals/nar/GonzalezRSRCSF20"
year: 2020
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkz1021
---
# The DisGeNET knowledge platform for disease genomics: 2019 update

DBLP:journals/nar/GonzalezRSRCSF20 | 2020 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gkz1021)

**DB**: DisGeNET (Disease Genomics Network)
**DB size**: gene-disease associations >1,000,000 pairs; genes 17,000+, diseases/traits 24,000+, variants 117,000+
**DB Open/Private**: Open (free for academic use; commercial-use license required)
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: DisGeNET REST API / disgenet2r (R package) / Python API

> Nucleic Acids Research | 2020 | dataset | medical
#### 📌 TL;DR
A disease genomics platform that integrates expert-curated data and literature text mining to provide over 1,000,000 gene-disease associations and over 117,000 variant-disease associations between more than 17,000 genes and more than 24,000 diseases and traits.

#### 🎯 Background
**Limitations of existing infrastructure**
- Gene-disease associations were scattered across dozens of heterogeneous sources such as OMIM, ClinVar, and the GWAS Catalog, making integrated querying impossible
- Curated databases are accurate but small in scale, while text-mining results are extensive but noisy
- The evidence provenance and confidence scores for associations were absent

**Why this system is needed**
- Integrated gene-disease knowledge is needed for drug target discovery, rare disease diagnosis, pleiotropy analysis, and more
- A standardized scoring scheme (the DisGeNET score) is needed to quantify the confidence of curated and text-mined associations

#### 🔨 Architecture
DisGeNET collects gene-disease and variant-disease associations from multiple sources and classifies them into four evidence types.
- **Curated**: expert curation from OMIM, ClinVar, UniProt, Orphanet, and others
- **Inferred**: inferred from MGD and RGD animal models
- **Literature (text-mined)**: automatically extracted from PubMed abstracts and full texts
- **Animal models**: associations from mouse/rat genome models

**DisGeNET Score**: an evidence-strength index combining source reliability, the number of publications, and curation level

#### 📥 Access
| Method | Description |
|---|---|
| REST API | api.disgenet.com — gene, disease, and variant queries; free registration |
| disgenet2r | R package distributed on CRAN; direct querying within the R environment |
| Python API | pip install disgenet2 — Python integration |
| TSV download | full dataset file download (free for academic use) |

#### 📤 Data formats
- Gene-disease association table (GDA: Gene-Disease Association)
- Variant-disease association table (VDA: Variant-Disease Association)
- DisGeNET score and evidence-type labels
- UMLS CUI-based disease identifiers

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| Number of diseases/traits | **more than 24,000** |
| Number of genes | **more than 17,000** |
| Number of genomic variants | **more than 117,000** |
| Number of gene-disease associations | **more than 1,000,000** (total; curation + literature mining) |
| Number of integrated sources | 12 curated sources + literature mining included |
| Operating institution | IMIM (Institut Hospital del Mar d'Investigacions Mèdiques) |

#### ⚠️ Limitations
- Literature text-mined associations may contain false positives, so using them separately from curated associations is recommended
- Commercial use and large-scale API usage require a separate license
- Because diseases are identified by UMLS CUI, direct mapping to MeSH or ICD requires additional conversion

## Related links
- **Paper**: [Piñero González et al., Nucleic Acids Research 2020](https://doi.org/10.1093/nar/gkz1021)
