---
title: "The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods"
bib_key: "zdrazil2024chembl"
year: 2024
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad1004
---
# The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods

zdrazil2024chembl | 2024 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkad1004)

**DB**: ChEMBL (2023 release)
**DB size**: Deposited data exceeds the volume of literature-extracted data (specific figures not stated in the abstract)
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ChEMBL web interface + REST API

> Nucleic Acids Research | 2024 | dataset | chem
#### 📌 TL;DR
A paper describing the 2023 state of ChEMBL, in which deposited data exceeds literature-extracted data for the first time, and anti-SARS-CoV-2 compound screening data, patent bioactivity data, Chemical Probe flags, and more have been added.

#### 🎯 Background
**Limitations of existing infrastructure**
- Since ChEMBL's launch in 2009, literature-extracted data had been dominant, but the need for non-literature deposited data increased
- Rapid integration of antiviral compound data was required for the COVID-19 response
**Why this system is needed**
- Established a regular deposition scheme for Chemical Probe data in collaboration with the EUbOPEN consortium
- Added new annotation features such as Natural Product characteristic scores and Chemical Probe flags

#### 🔨 Architecture
Regular deposition of EUbOPEN Chemical Probe data. Integration of anti-SARS-CoV-2 activity screening data in Release 27. Addition of patent bioactivity data. Introduction of Natural Product likeness scores and Chemical Probe flags. Initial annotation of action type performed on approximately 270,000 bioactivity measurements.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | https://www.ebi.ac.uk/chembl/ |
| REST API | Structure, target, and bioactivity queries |
| Data download | Full dumps in SQL, SDF, FASTA |

#### 📤 Data formats
- Compound structures (SMILES, InChI)
- Bioactivity measurements
- Chemical Probe / Natural Product flags
- Action type annotations

#### 📊 Key statistics (per the paper)
| Item | Figure |
|---|---|
| Action type annotated bioactivities | ~270,000 |
| Data composition | Deposited > literature-extracted (for the first time) |

#### ⚠️ Limitations
- Increasing proportion of deposited data raises the complexity of managing quality consistency
- Commercial patent bioactivity data may have restrictions on full redistribution

## Related links
- **Paper**: [The ChEMBL Database in 2023](https://doi.org/10.1093/nar/gkad1004)
