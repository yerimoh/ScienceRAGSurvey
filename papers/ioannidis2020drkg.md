---
title: "DRKG - Drug Repurposing Knowledge Graph for COVID-19"
bib_key: "ioannidis2020drkg"
year: 2020
domain: chem
type: dataset
venue: arXiv preprint
paper_link: https://arxiv.org/abs/2010.09600
---
# DRKG - Drug Repurposing Knowledge Graph for COVID-19

ioannidis2020drkg | 2020 | arXiv preprint | dataset | [chem] | [paper](https://arxiv.org/abs/2010.09600)

**DB**: DRKG (Drug Repurposing Knowledge Graph)
**DB size**: 97,238 entities, 5,874,261 triples (integration of 6 existing DBs)
**DB Open/Private**: Open
**Modality**: ['Structured', 'Network']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: DRKG (knowledge-graph-completion-based drug repurposing)

> arXiv preprint | 2020 | dataset | chem
#### 📌 TL;DR
DRKG is a biomedical knowledge graph that integrates 6 DBs, including DrugBank, Hetionet, GNBR, String, IntAct, and DGIdb, for COVID-19 drug repurposing, and it supports candidate drug discovery based on knowledge graph embeddings.

#### 🎯 Background
**Limitations of existing infrastructure**
- There was no integrated drug repurposing knowledge graph specialized for COVID-19
- Existing biomedical DBs existed separately, making cross-resource analysis difficult
**Why this system is needed**
- Rapid derivation of drug candidates is needed for pandemic response
- Prediction of previously unknown drug-target relationships via knowledge graph completion (KGC) methods

#### 🔨 Architecture
It integrates 6 biomedical DBs, including DrugBank, Hetionet, GNBR, String, IntAct, and DGIdb. Entity types: drugs, genes, diseases, compounds, biological processes, anatomical structures, cellular components, molecular functions, etc. Drug repurposing candidate scoring with KGE models such as TransE and RotatE.

#### 📥 Access
| Method | Description |
|---|---|
| GitHub | DRKG graph data and embeddings publicly available |
| Direct download | Node/edge TSV files |

#### 📤 Data formats
- Knowledge graph triples (head, relation, tail)
- KGE embedding vectors
- Drug-target prediction results

#### 📊 Key statistics (per paper)
| Item | Value |
|---|---|
| Entities | 97,238 |
| Triples | 5,874,261 |
| Integrated DBs | 6 |

#### ⚠️ Limitations
- Built for COVID-19 response purposes, so coverage of other disease domains is uneven
- Possibility of entity alignment errors during the integration process
- Based on a non-peer-reviewed (preprint) paper, so methodological validation is limited

## Related links
- **Paper**: [DRKG - Drug Repurposing Knowledge Graph for COVID-19](https://arxiv.org/abs/2010.09600)
