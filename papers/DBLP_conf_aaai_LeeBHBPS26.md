---
title: "RAG-Enhanced Collaborative LLM Agents for Drug Discovery"
bib_key: "DBLP:conf/aaai/LeeBHBPS26"
year: 2026
domain: chem, medical
type: Method
venue: AAAI 2026
paper_link: https://doi.org/10.1609/aaai.v40i1.37020
---
# RAG-Enhanced Collaborative LLM Agents for Drug Discovery (CLADD)

DBLP:conf/aaai/LeeBHBPS26 | 2026 | AAAI 2026 | Method | [chem, medical] | [paper](https://doi.org/10.1609/aaai.v40i1.37020)

**Retriever**: RAG from biomedical knowledge bases (Drug Repurposing Hub, DrugBank, STITCH v5.0)
**Eval Task**: Drug-target interaction prediction, molecular property prediction (BBBP, Sider, ClinTox, BACE), property-specific molecular captioning
**Eval Metric**: Precision (top-5 protein prediction), AUROC
**Method Name**: CLADD (Collaborative LLM Agents for Drug Discovery)
**Modality**: Text, Molecular structures (SMILES)

> AAAI 2026 | 2026 | Method | chem · medical
#### 📌 TL;DR
This is a RAG-based agentic system in which, without domain-specific fine-tuning, multiple LLM agents collaborate to dynamically retrieve from biomedical knowledge bases such as Drug Repurposing Hub, DrugBank, and STITCH, and perform drug discovery tasks (drug-target interaction, toxicity classification).

#### 🎯 Background
**Limitations of existing approaches**
- Domain-specific LLM fine-tuning is costly, and rapid integration of new experimental data is difficult
- Real scientific questions are complex and open-ended, so static knowledge retrieval alone is insufficient
- The heterogeneity, ambiguity, and multi-source integration of biochemical data are major obstacles to applying RAG

**Why this system is needed**
- In drug discovery tasks, there is a need to rapidly integrate continuously generated experimental data
- A flexible framework is needed to leverage general-purpose LLMs for drug discovery in a zero-shot setting

#### 🔨 Architecture
Multiple LLM agents collaborate to dynamically retrieve information from Drug Repurposing Hub, DrugBank (13,688 molecules), and STITCH v5.0, contextualize the query molecule, and integrate relevant evidence. The system introduces specialized handling methods that address the heterogeneity and ambiguity problems of biochemical data in the RAG workflow. It operates in a zero-shot setting without fine-tuning.

#### 📊 Key results
| Item | Value |
|---|---|
| Drug-target interaction dataset | Drug Repurposing Hub, DrugBank, STITCH v5.0 (13,688 molecules in total) |
| Toxicity dataset | BBBP, Sider, ClinTox, BACE |
| BBBP AUROC | 72.28 (±1.04) — best performance |
| Sider AUROC | 66.42 (±1.31) — best performance |
| ClinTox AUROC | 93.80 (±2.30) — best performance |
| BACE AUROC | 77.74 (±3.15) |
| Comparison | Outperforms GPT-4o, domain LLMs (MolT5, BioT5), and GNNs (GraphMVP, MoleculeSTM) alike |

#### ⚠️ Limitations
- Some performance degradation for molecules not present in external databases (the "No Overlap" scenario)
- Increased inference latency due to the collaboration among multiple agents
- A gap with domain-specific fine-tuned models remains on some tasks

## Related links
- **Paper (AAAI)**: [https://doi.org/10.1609/aaai.v40i1.37020](https://doi.org/10.1609/aaai.v40i1.37020)
- **arXiv preprint**: [https://arxiv.org/abs/2502.17506](https://arxiv.org/abs/2502.17506)
