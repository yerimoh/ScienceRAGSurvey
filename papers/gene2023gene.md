---
title: "The Gene Ontology knowledgebase in 2023"
bib_key: "gene2023gene"
year: 2023
domain: bio
type: dataset
venue: Genetics
paper_link: https://doi.org/10.1093/genetics/iyad031
---
# The Gene Ontology knowledgebase in 2023

gene2023gene | 2023 | Genetics | dataset | [bio] | [paper](https://doi.org/10.1093/genetics/iyad031)

**DB**: Gene Ontology (GO) Knowledgebase
**DB size**: 3 components: GO ontology, GO annotations, GO Causal Activity Models (GO-CAMs)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: GO REST API / file download (http://geneontology.org)

> Genetics | 2023 | dataset | bio
#### 📌 TL;DR
A 2023 status report on the GO knowledgebase, which describes the functions of genes and gene products (proteins, non-coding RNAs), introducing its three components—the GO ontology, GO annotations, and GO-CAM—along with methods for continuous expansion and validation.

#### 🎯 Background
**Limitations of existing infrastructure**
- Since its founding in 2000, new biological discoveries have required continuous updating of GO terms and annotations
- Beyond simple gene-to-GO-term mapping, there was a need to represent causal activity models of molecular pathways (GO-CAM)

**Why this system is needed**
- To build a comprehensive resource of gene function knowledge spanning the entire tree of life (including viruses)
- To provide mechanistic pathway models that connect multiple GO annotations through GO-CAM
- To maintain quality through QA checks, reviews, and user feedback from a broad international consortium

#### 🔨 Architecture
The GO knowledgebase consists of three components: (1) **GO** — a computational knowledge structure that describes the functional characteristics of genes, (2) **GO annotations** — evidence-based statements that a particular gene product has a particular functional characteristic, and (3) **GO Causal Activity Models (GO-CAMs)** — mechanistic models of molecular 'pathways' that connect multiple GO annotations using defined relations. Each component is continuously expanded, revised, and updated as new discoveries are made.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | http://geneontology.org — browse the ontology and annotations |
| REST API | programmatic data access |
| File download | various formats such as OBO, OWL, GAF |

#### 📤 Data formats
- GO ontology (OBO/OWL format)
- GO annotation files (GAF format, including evidence codes)
- GO-CAM models (causal activity models)
- Species-specific gene-to-GO mappings

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Number of components | **3** (GO ontology, GO annotations, GO-CAM) |
| Scope of application | all organisms across the tree of life + viruses |
| Primary source of information | experimental results from a small number of model organisms (most knowledge sources) |

#### ⚠️ Limitations
- Most gene function knowledge derives from experiments performed in a small number of model organisms
- Genes of non-model organisms are annotated primarily by computational inference, which may be of lower reliability
- GO-CAM models are still in the early stages of development and have limitations in fully representing complete biological pathways

## Related links
- **Paper**: [The Gene Ontology knowledgebase in 2023](https://doi.org/10.1093/genetics/iyad031)
