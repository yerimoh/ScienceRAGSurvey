---
title: "AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences"
bib_key: "varadi2024alphafold"
year: 2024
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad1011
---
# AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences

varadi2024alphafold | 2024 | Nucleic Acids Res. | dataset | [bio] | [paper](https://doi.org/10.1093/nar/gkad1011)

**DB**: AlphaFold DB (AlphaFold Protein Structure Database) — 2024 update
**DB size**: Predicted structures for over 214 million protein sequences (a 500-fold expansion from the initial 300,000 in 2021)
**DB Open/Private**: Open (alphafold.ebi.ac.uk)
**Modality**: Structured Table (atomic coordinates, per-residue/pairwise confidence)
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: AlphaFold DB / EBI (alphafold.ebi.ac.uk)

> Nucleic Acids Res. | 2024 | dataset | bio

#### 📌 TL;DR
This work reports the latest status of AlphaFold DB, which expanded roughly 500-fold from the initial 300,000 entries in 2021 to over 214 million in 2024, and introduces the integration of model organisms, global-health proteomes, and Swiss-Prot, along with advanced Google Cloud-based data access methods.

#### 🎯 Background
**Limitations of the existing infrastructure**
- The initial 2022 release of AlphaFold DB was limited to 21 model organisms
- Insufficient coverage of global-health pathogen proteomes and the full Swiss-Prot
- Lack of large-scale advanced query methods beyond direct FTP download

**Why this system is needed**
- Need to expand structure coverage to the full scale of the UniProt database
- Need to address researchers' diverse data-access demands (cloud, API, viewer)

#### 🔨 Architecture
A joint update by EMBL-EBI, Google DeepMind, and Seoul National University. Roughly a 500-fold expansion from the initial 300,000 entries in 2021 to over 214 million. Integrated with major data resources such as PDB, UniProt, Ensembl, InterPro, and MobiDB. Includes model organism proteomes, global-health proteomes, Swiss-Prot integration, and curated protein datasets. Direct FTP file access + Google Cloud Public Datasets advanced queries + REST API endpoints. PAE viewer, 3D viewer customization, and search-engine improvements.

#### 📥 Access
| Method | Description |
|---|---|
| AlphaFold DB portal | https://alphafold.ebi.ac.uk — free public access |
| FTP | Direct file download |
| Google Cloud | Google Cloud Public Datasets advanced queries |
| REST API | Programmatic access endpoints |

#### 📤 Data formats
- mmCIF/PDB format (predicted atomic coordinates)
- pLDDT scores (per-residue confidence)
- PAE matrix (Predicted Aligned Error)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total predicted structures | **over 214,000,000** |
| Expansion factor relative to initial 2021 | **~500-fold** |
| Integrated data resources | **PDB, UniProt, Ensembl, InterPro, MobiDB** |

#### ⚠️ Limitations
- Predicted structures with incomplete experimental validation (especially low-pLDDT regions)
- Sequence-based predictions that do not reflect binding-partner or ligand context
- Limited representation of protein dynamics and polymorphism

## Related links
- **Paper**: [AlphaFold Protein Structure Database in 2024](https://doi.org/10.1093/nar/gkad1011)
