---
title: "The Reactome Pathway Knowledgebase 2024"
bib_key: "milacic2024reactome"
year: 2024
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad1025
---
# The Reactome Pathway Knowledgebase 2024

milacic2024reactome | 2024 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/gkad1025)

**DB**: Reactome Pathway Knowledgebase
**DB size**: A curated pathway database aiming for annotation of the entire human proteome (an Elixir and GCBR core data resource)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Reactome REST API / FTP (https://reactome.org)

> Nucleic Acids Research | 2024 | dataset | bio
#### 📌 TL;DR
A manually curated database of human biological pathways that represents both normal and disease-related molecular transformation processes within a single consistent data model, and is designated as an Elixir and GCBR core biological data resource.

#### 🎯 Background
**Limitations of existing infrastructure**
- Existing biological pathway databases either had a low level of molecular detail or were restricted to specific species
- Systematic tools were needed to discover functional relationships in large-scale data such as gene expression profiles or catalogs of somatic mutations in tumor cells

**Why this system is needed**
- Building a digital archive that manually annotates the molecular transformation processes of the entire human proteome
- Serving as an analysis tool for discovering functional relationships from gene expression data and catalogs of somatic mutations
- Strengthening interoperability with related resources such as Gene Ontology

#### 🔨 Architecture
Reactome uses a single consistent data model that represents molecular transformations as ordered networks. Pathways cover both normal biological processes and disease-related processes. The 2024 update emphasizes progress on annotating the entire human proteome, annotation of the pathway context of disease-causing gene variants of proteins and of small-molecule drugs, and support for explicit annotation of cell- and tissue-specific pathways.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | https://reactome.org — pathway browser, analysis tools |
| REST API | Programmatic data access |
| FTP | Bulk download of the full dataset |

#### 📤 Data formats
- Pathway data (BioPAX, SBML, GPML formats)
- Gene-to-pathway mappings
- Molecular details per reaction
- Cross-references to Gene Ontology and external databases

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| Data resource classification | Elixir core data resource, GCBR core biological data resource |
| Target species | Human (Homo sapiens) centric |
| Goal | Completing annotation of the entire human proteome, in progress |

#### ⚠️ Limitations
- Reliance on manual curation means the incorporation of new discoveries may lag after publication
- It is centered on human pathways, with limited direct curation for non-human species
- Achieving full interoperability with other resources such as Gene Ontology is still in progress

## Related links
- **Paper**: [The Reactome Pathway Knowledgebase 2024](https://doi.org/10.1093/nar/gkad1025)
