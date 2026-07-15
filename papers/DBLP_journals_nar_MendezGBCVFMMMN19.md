---
title: "ChEMBL: towards direct deposition of bioassay data"
bib_key: "DBLP:journals/nar/MendezGBCVFMMMN19"
year: 2019
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gky1075
---
# ChEMBL: towards direct deposition of bioassay data

DBLP:journals/nar/MendezGBCVFMMMN19 | 2019 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gky1075)

**DB**: ChEMBL Release 24
**DB size**: 15M+ bioactivity measurements, 1.8M compounds, 8,200+ protein targets
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ChEMBL web interface + REST API + data deposition system

> Nucleic Acids Research | 2019 | dataset | chem
#### 📌 TL;DR
ChEMBL Release 24 introduces a direct bioassay deposition system, a completely redesigned web interface, and enhanced assay-detail capture, providing 15M+ bioactivity measurements.

#### 🎯 Background
**Limitations of existing infrastructure**
- Datasets that were not journal articles had no deposition pathway, making public access difficult
- Capture of assay details (cell line, tissue, organism) was incomplete
**Why this system is needed**
- Need to integrate non-literature data such as patent bioactivity data (BindingDB exchange) and open-source malaria data
- Improve data reusability through standardization of assay metadata

#### 🔨 Architecture
It integrates data extracted from over 67,000 publications and patents with directly deposited datasets. Assays are annotated with 1,600 cell lines, 500 tissues/organs, and 3,600 organisms. The new deposition system enables submission of supplementary datasets. The new web interface supports interactive filtering, Heatmap, and Sunburst visualizations.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | Redesigned interactive search/filtering UI |
| REST API | JSON/XML-based query of structures, targets, and bioactivities |
| Data download | Oracle, PostgreSQL, SQLite, RDF, SDF, FASTA |
| Deposition system | Direct upload of datasets with assigned DOIs |

#### 📤 Data formats
- Compound structures (SMILES, InChI)
- Bioactivity measurements (including IC50, Ki, EC50, kd, kon, koff)
- Target sequences (FASTA)
- RDF format

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Bioactivity measurements | 15M+ |
| Compounds | 1.8M |
| Protein targets | 8,200+ (3,569 human proteins) |
| Assay-annotated cell lines | 1,600+ |
| Publications/patents for data extraction | 67,000+ |

#### ⚠️ Limitations
- Quality-verification procedures for directly deposited data may be less rigorous than for literature-extracted data
- The database schema was designed around literature extraction, limiting representation of some aspects of deposited data

## Related links
- **Paper**: [ChEMBL: towards direct deposition of bioassay data](https://doi.org/10.1093/nar/gky1075)
