---
title: "Chemical reactions from US patents (1976-Sep2016)"
bib_key: "lowe2017chemical"
year: 2017
domain: chem
type: dataset
venue: figshare
paper_link: https://figshare.com/articles/dataset/Chemical_reactions_from_US_patents_1976-Sep2016_/5104873
---
# Chemical reactions from US patents (1976-Sep2016)

lowe2017chemical | 2017 | figshare | dataset | [chem] | [paper](https://figshare.com/articles/dataset/Chemical_reactions_from_US_patents_1976-Sep2016_/5104873)

**DB**: USPTO chemical reaction dataset (Lowe 2017)
**DB size**: Chemical reactions extracted from US patents from 1976 to September 2016 (exact figures listed on figshare)
**DB Open/Private**: Open (CC0)
**Modality**: ['Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: USPTO reaction dataset (text mining / structure extraction)

> figshare | 2017 | dataset | chem
#### 📌 TL;DR
A chemical reaction dataset extracted by text mining from US patents spanning 1976 to September 2016, widely used as a standard training resource for computer-aided synthesis planning and reaction prediction models.

#### 🎯 Background
**Limitations of existing infrastructure**
- Chemical reaction data was embedded as unstructured text within full patent documents, making it difficult to use for machine learning
- There was no public dataset available for training large-scale reaction prediction models
**Why this system is needed**
- A large-scale reaction corpus is needed to develop computational chemistry models such as synthesis route prediction (retrosynthesis) and reaction condition prediction
- Patents contain far more synthetic reaction information than journals

#### 🔨 Architecture
Text mining tools such as ChemDataExtractor and OSCAR4 are used to extract reactant, reagent, and product structures from full-text US patents. Reactions are encoded in SMILES format. The pipeline includes reaction entity recognition and structure parsing.

#### 📥 Access
| Method | Description |
|---|---|
| figshare download | Public download under CC0 license |

#### 📤 Data formats
- Reaction SMILES (reactants>reagents>products)
- Reaction data in XML format
- Patent identifier metadata

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Coverage period | 1976 ~ September 2016 |
| Data source | Full-text US patents |

#### ⚠️ Limitations
- Because it is based on patent text mining, it may contain structure extraction errors
- Reactions reported in patents may differ from actual optimal conditions
- Lacks quantitative data such as reaction yield and purity

## Related links
- **Paper**: [Chemical reactions from US patents (1976-Sep2016)](https://figshare.com/articles/dataset/Chemical_reactions_from_US_patents_1976-Sep2016_/5104873)
