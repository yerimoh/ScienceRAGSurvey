---
title: "Gene Expression Omnibus: NCBI gene expression and hybridization array data repository"
bib_key: "DBLP:journals/nar/EdgarDL03"
year: 2002
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/30.1.207
---
# Gene Expression Omnibus: NCBI gene expression and hybridization array data repository

DBLP:journals/nar/EdgarDL03 | 2002 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/30.1.207)

**DB**: GEO (Gene Expression Omnibus)
**DB size**: Public repository of high-throughput gene expression and genomic hybridization experiment data (3 core entities: Platform, Sample, Series)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NCBI GEO web (http://www.ncbi.nlm.nih.gov/geo)

> Nucleic Acids Research | 2002 | dataset | bio
#### 📌 TL;DR
A public repository built by NCBI in response to the growing demand for high-throughput gene expression data, composed of three core data entities: Platform (probe list), Sample (measurement data), and Series (experiment grouping).

#### 🎯 Background
**Limitations of existing infrastructure**
- Demand for a public repository of high-throughput gene expression data surged, but a centralized public data hub was lacking
- Individual laboratory databases were specialized for particular analysis methods, limiting data sharing and reuse

**Why this system is needed**
- GEO is designed as a tertiary central data distribution hub that complements rather than replaces individual gene expression databases
- A flexible and open design that allows heterogeneous datasets from gene expression and genomic hybridization experiments to be submitted, stored, and retrieved
- Provides a standardized submission platform that meets international public data sharing requirements

#### 🔨 Architecture
GEO's three core data entities: (1) **Platform** — a probe list defining which set of molecules can be detected, (2) **Sample** — molecular abundance data describing the set of molecules being measured and referencing a single Platform, (3) **Series** — meaningful datasets that constitute an experiment, organizing Samples. GEO is publicly accessible through http://www.ncbi.nlm.nih.gov/geo.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | http://www.ncbi.nlm.nih.gov/geo — free browser search |
| SOFT format download | Download of Platform, Sample, and Series data |

#### 📤 Data formats
- SOFT (Simple Omnibus Format in Text) format
- Platform definition files
- Sample molecular abundance data
- Series metadata

#### 📊 Key statistics (per paper)
| Item | Value |
|---|---|
| Core data entities | **3** (Platform, Sample, Series) |
| Founding institutions | NCBI, NLM, NIH |
| Access method | Public web (free) |

#### ⚠️ Limitations
- GEO is designed as a central hub that complements rather than replaces analysis-specialized in-house databases, so its direct analysis capabilities are limited
- Standardization (normalization) across heterogeneous datasets varies by submitter, so care is needed for direct comparison
- As a 2002 founding paper, the number of datasets initially included was very small compared to the present

## Related links
- **Paper**: [Gene Expression Omnibus: NCBI gene expression and hybridization array data repository](https://doi.org/10.1093/nar/30.1.207)
