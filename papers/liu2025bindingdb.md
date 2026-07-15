---
title: "BindingDB in 2024: a FAIR knowledgebase of protein-small molecule binding data"
bib_key: "liu2025bindingdb"
year: 2025
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkae1075
---
# BindingDB in 2024: a FAIR knowledgebase of protein-small molecule binding data

liu2025bindingdb | 2025 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkae1075)

**DB**: BindingDB (2024 update)
**DB size**: 2.9M binding measurements, 1.3M compounds, thousands of protein targets
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: BindingDB web interface + FAIR data services

> Nucleic Acids Research | 2025 | dataset | chem
#### 📌 TL;DR
The 2024 update of BindingDB strengthens compliance with FAIR principles, includes 2.9M binding measurements and 1.3M compounds, and establishes a long-term data archive replicated across distributed sites.

#### 🎯 Background
**Limitations of existing infrastructure**
- Lacked a system to guarantee long-term data preservation and reproducibility
- Needed to integrate the US patent bioactivity data that has grown rapidly since 2016
**Why this system is needed**
- Large-scale FAIR data is required for AI model training, computational chemistry method development, and medicinal chemistry support
- Distributed replicated archives ensure data sustainability

#### 🔨 Architecture
Since 2016, growth has been driven primarily by a focus on curating US patent data, achieving large-scale expansion. The website was fully redesigned with responsive web design. Enhanced search and filtering, new download options, and web services were added. A long-term data archive replicated across distributed sites was built. Compliance with FAIR data-sharing policies is maintained.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | bindingdb.org improved responsive search UI |
| Web service | Data query API |
| Download | Various format download options |
| Distributed archive | Replicated sites for long-term preservation |

#### 📤 Data formats
- Binding affinity (Ki, IC50, Kd, EC50)
- Compound structures (SMILES, SDF)
- Protein target information

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Binding measurements | 2.9M |
| Compounds | 1.3M |
| Protein targets | thousands |

#### ⚠️ Limitations
- Growth driven mainly by patent data extraction may introduce bias toward certain compound types
- Data-duplication management is needed relative to related resources (ChEMBL, PubChem)

## Related links
- **Paper**: [BindingDB in 2024: a FAIR knowledgebase](https://doi.org/10.1093/nar/gkae1075)
