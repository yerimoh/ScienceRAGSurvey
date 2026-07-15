---
title: "Repurposing non-pharmacological interventions for Alzheimer's disease through link prediction on biomedical literature"
bib_key: "xiao2024repurposing"
year: 2024
domain: medical
type: Method
venue: Scientific Reports
paper_link: https://doi.org/10.1038/s41598-024-59537-6
---
# Repurposing non-pharmacological interventions for Alzheimer's disease through link prediction on biomedical literature

xiao2024repurposing | 2024 | Scientific Reports | Method | [medical] | [paper](https://doi.org/10.1038/s41598-024-59537-6)

**Retriever**: Literature-based knowledge graph construction (biomedical literature retrieval)
**Eval Task**: Link prediction-based drug/intervention repurposing for Alzheimer's disease
**Eval Metric**: Downstream task accuracy (repurposing candidate validation)
**Method Name**: Literature-based link prediction for AD repurposing
**Modality**: Text (biomedical literature)

> Scientific Reports | 2024 | Method | medical
#### 📌 TL;DR
A system that repurposes non-pharmacological interventions as candidate treatments for Alzheimer's disease through link prediction on a knowledge graph built from biomedical literature, presenting a case of weakly-verified hypothesis generation based on literature retrieval.

#### 🎯 Background
**Limitations of existing approaches**
- Alzheimer's drug discovery has a high failure rate and long development timelines, bringing the search for non-pharmacological interventions to the fore
- There is no system that systematically connects knowledge dispersed across large-scale biomedical literature

**Why this system is needed**
- Existing drug repurposing methods mainly focus on pharmacological compounds; systematic evaluation of non-pharmacological interventions (exercise, cognitive training, etc.) is needed
- An evaluation framework is needed that generates literature-derived hypotheses without a strong external verifier (docking, direct database lookup)

#### 🔨 Architecture
Entities (diseases, interventions, genes, biological processes) and their relations are extracted from biomedical literature to build a knowledge graph. A graph-based link prediction model generates potential connections (candidate hypotheses) between Alzheimer's disease and non-pharmacological interventions. Evaluation is performed by comparison against existing literature-based evidence.

#### 📊 Key Results
| Item | Value |
|---|---|
| Publication journal | Scientific Reports, vol.14, p.8693, 2024 |
| Evaluation method | Downstream task accuracy, expert validation |
| Verification type | Weak verification (weak verification — literature-based) |
| Application domain | Alzheimer's non-pharmacological intervention repurposing |

#### ⚠️ Limitations
- Without a strong external verifier (experiments, DFT, direct database lookup), novelty and validity bear the main evaluation burden
- Evaluation results are sensitive to literature quality and bias
- Experimental validation of the predicted connections is separately required

## Related links
- **Paper**: [https://doi.org/10.1038/s41598-024-59537-6](https://doi.org/10.1038/s41598-024-59537-6)
- **PubMed**: https://pubmed.ncbi.nlm.nih.gov/38615044/
