---
title: "SciFinder-n"
bib_key: "scifinder"
year: 1995
domain: chem
type: dataset
venue: CAS (misc)
paper_link: https://scifinder-n.cas.org
---
# SciFinder-n

scifinder | 1995 | CAS | dataset | [chem] | [paper](https://scifinder-n.cas.org)

**DB**: SciFinder-n (CAS, a division of the American Chemical Society)
**DB size**: Subscription-based (no public figures disclosed)
**DB Open/Private**: Subscription
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: SciFinder-n web platform

> CAS | 1995 | dataset | chem
#### 📌 TL;DR
SciFinder-n is a subscription-based chemical literature and substance DB operated by the CAS division of the American Chemical Society (ACS). It is the commercial infrastructure most widely used by synthetic chemists for reaction search, substance discovery, and patent information access.

#### 🎯 Background
**Limitations of existing infrastructure**
- There was no standard commercial tool that provided integrated search across chemical reactions, substances, and literature information
**Why this system is needed**
- Demand from synthetic chemists for everyday reaction search, prior-art investigation, and verification of substance properties
- Integrated access to patent and journal chemical information

#### 🔨 Architecture
It integrates compound, reaction, and literature data that CAS extracts and curates from the chemical literature and patents. The CAS Registry Number (CAS number) is the standard identifier for each compound. It supports various search modes such as structure, substructure, reaction, researcher, and topic.

#### 📥 Access
| Method | Description |
|---|---|
| Subscription platform | scifinder-n.cas.org (institutional subscription required) |
| Structure search | Search based on SMILES / structure drawing |
| Reaction search | Search based on reaction type and conditions |

#### 📤 Data formats
- Compound records (CAS number, structure, properties)
- Reaction records (reactants, products, conditions, yield)
- Literature and patent references
- CAS number (standard identifier)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Release | 1995 (SciFinder), 2019 SciFinder-n relaunch |
| Data scope | Subscription-based; no public figures released by CAS |

#### ⚠️ Limitations
- Being subscription-based, it cannot be directly accessed by open-science RAG systems
- High cost limits access for small institutions and researchers in developing countries
- A representative example of the largest gap with chemical RAG infrastructure

## Related links
- **Official page**: [SciFinder-n](https://scifinder-n.cas.org)
