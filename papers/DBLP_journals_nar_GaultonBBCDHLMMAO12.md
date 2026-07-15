---
title: "ChEMBL: a large-scale bioactivity database for drug discovery"
bib_key: "DBLP:journals/nar/GaultonBBCDHLMMAO12"
year: 2012
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkr777
---
# ChEMBL: a large-scale bioactivity database for drug discovery

DBLP:journals/nar/GaultonBBCDHLMMAO12 | 2012 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkr777)

**DB**: ChEMBL (EBI, initial description)
**DB size**: 5.4M bioactivity measurements, 1M+ compounds, 5,200 protein targets
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ChEMBL web interface + data download + web services

> Nucleic Acids Research | 2012 | dataset | chem
#### 📌 TL;DR
ChEMBL, built by EBI, is a large-scale open bioactivity database containing binding, functional, and ADMET data manually extracted from journal literature.

#### 🎯 Background
**Limitations of existing infrastructure**
- Bioactivity data needed for drug discovery was scattered across full-text papers, making it hard to access in a computable form
- A standardized public DB integrating compound structures and biological activity data was lacking
**Why this system is needed**
- Chemical biology and drug discovery research require a foundation for large-scale structure-activity relationship (SAR) analysis
- There is demand for curated bioactivity datasets for training computational chemistry and machine learning models

#### 🔨 Architecture
Compound, assay, and bioactivity information is manually extracted from the full text of core medicinal chemistry journals. Compound structures are standardized and assigned Standard InChI-based identifiers. Assay descriptions are mapped to a controlled vocabulary, and activity measurements are converted to standard formats. It is provided through a web interface, data download, and web services.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | https://www.ebi.ac.uk/chembldb text and structure search |
| Data download | Full DB SQL/SDF download |
| Web services (REST) | Structure, target, bioactivity API |

#### 📤 Data formats
- Compound structures (SMILES, InChI, SDF)
- Bioactivity measurements (IC50, Ki, EC50, etc.)
- Target protein information (UniProt integration)
- Assay descriptions (standardized vocabulary)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Bioactivity measurements | 5.4M |
| Compounds | 1M+ |
| Protein targets | 5,200 |

#### ⚠️ Limitations
- Manual curation limits the speed of data additions
- Since full-text papers are required, access is restricted when they are not open access
- As an early version, it does not support direct data deposition

## Related links
- **Paper**: [ChEMBL: a large-scale bioactivity database for drug discovery](https://doi.org/10.1093/nar/gkr777)
