---
title: "DrugBank 6.0: the DrugBank Knowledgebase for 2024"
bib_key: "knox2024drugbank"
year: 2024
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad976
---
# DrugBank 6.0: the DrugBank Knowledgebase for 2024

knox2024drugbank | 2024 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkad976)

**DB**: DrugBank 6.0
**DB size**: 4,563 FDA-approved drugs, 6,231 clinical-trial drugs, 1,413,413 drug-drug interactions
**DB Open/Private**: Open (basic) / Subscription (extended features)
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: DrugBank web interface (go.drugbank.com)

> Nucleic Acids Research | 2024 | dataset | chem
#### 📌 TL;DR
DrugBank 6.0 is a "gold-standard" knowledge resource for drug, drug-target, and pharmacokinetic information, containing 4,563 FDA-approved drugs and more than 1.4 million drug-drug interaction records.

#### 🎯 Background
**Limitations of the existing infrastructure**
- Since the last update in 2018, a substantial expansion of the FDA-approved drug list and interaction data was needed
- Visual representation of drug mechanisms and metabolic pathways was lacking
**Why this system is needed**
- As a major drug-information resource with over 30 million views per year, it requires continuous updates
- An integrated knowledge graph is needed for AI-driven drug repurposing, side-effect prediction, and target discovery

#### 🔨 Architecture
It is a drug-information knowledge base that has been continuously expanded since its launch in 2006. It integrates drug chemical structures, pharmacokinetics, pharmacodynamics, mechanisms of action, metabolic pathways, target proteins, and drug-drug/drug-food interactions. Newly added drug mechanisms and metabolic pathways with color-rich annotations.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | Search at go.drugbank.com |
| Data download | XML, CSV formats (free after registration) |
| API | DrugBank API (commercial license option) |

#### 📤 Data formats
- Drug chemical structures (SMILES, InChI, SDF)
- Pharmacokinetic and pharmacodynamic data
- Protein target sequences
- Drug-drug interaction lists
- Pathway information (including visualization)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| FDA-approved drugs | 4,563 (72% increase vs. 2018) |
| Clinical-trial drugs | 6,231 (38% increase) |
| Drug-drug interactions | 1,413,413 (300% increase) |
| Drug-food interactions | 2,475 (200% increase) |
| Annual views | 30M+ |

#### ⚠️ Limitations
- Advanced API features require a commercial license
- Some drug mechanisms are prediction-based rather than expert-curated
- Updates to information on withdrawn drugs may be delayed

## Related links
- **Paper**: [DrugBank 6.0: the DrugBank Knowledgebase for 2024](https://doi.org/10.1093/nar/gkad976)
