---
title: "UniProt: the Universal Protein Knowledgebase in 2023"
bib_key: "uniprot2023uniprot"
year: 2023
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkac1052
---
# UniProt: the Universal Protein Knowledgebase in 2023

uniprot2023uniprot | 2023 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/gkac1052)

**DB**: UniProt Knowledgebase (UniProtKB = Swiss-Prot + TrEMBL)
**DB size**: 227M+ sequences (per the 2023 paper)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: UniProt REST API / FTP

> Nucleic Acids Research | 2023 | dataset | bio
#### 📌 TL;DR
As the standard infrastructure for protein sequences and functional annotations worldwide, it provides more than 227 million protein sequences free of charge and supports cross-references to over 150 external databases.

#### 🎯 Background
**Limitations of prior infrastructure**
- Existing protein databases kept manually curated data (Swiss-Prot) and automatically annotated data (TrEMBL) separate, making unified access inconvenient
- As advances in sequencing technology caused an explosive increase in the number of protein sequences, the need for automated quality control came to the fore

**Why this system is needed**
- Provides high-quality manually curated entries (Swiss-Prot) and automatically annotated entries (TrEMBL) integrated into a single database
- Complements the quality of unreviewed entries with an automated annotation system leveraging machine learning techniques
- Ongoing effort aimed at building reference proteomes for all taxonomic groups

#### 🔨 Architecture
UniProtKB consists of manually curated Swiss-Prot entries and automatically annotated TrEMBL entries. It includes sequences, functional annotations, taxonomic information, domain information, variants, subcellular location, and cross-references to more than 150 other databases. In the 2023 update, a new website (https://www.uniprot.org/) was released, and AlphaFold structures were linked to more than 85% of all entries.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | https://www.uniprot.org/ — free browser-based search |
| REST API | UniProt REST API — programmatic queries |
| FTP | bulk download of the full dataset |

#### 📤 Data formats
- Protein sequences (FASTA)
- Functional annotations (UniProtKB format)
- XML, TSV, JSON format support
- Cross-references to more than 150 external databases

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total number of sequences | **227M+** (as of 2023) |
| AlphaFold structure link ratio | **85%+** |
| Number of cross-reference databases | **150+** |

#### ⚠️ Limitations
- Manually curated entries (Swiss-Prot) are only a tiny fraction of the total, and most entries rely on automated annotation
- The rapid increase in the number of sequences makes comprehensive scaling of manual curation difficult
- An annotation gap between new sequences and their functions persists continuously

## Related links
- **Paper**: [UniProt: the Universal Protein Knowledgebase in 2023](https://doi.org/10.1093/nar/gkac1052)
