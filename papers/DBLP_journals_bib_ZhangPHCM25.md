---
notion_id: 355f2dcd-4912-8184-b91f-c14fce4ca21b
title: Rag2Mol: structure-based drug design based on RAG
bib_key: DBLP:journals/bib/ZhangPHCM25
year: 2025
domain: bio, medical, chem
type: Method
venue: Briefings in Bioinformatics (Oxford)
paper_link: https://doi.org/10.1093/bib/bbaf265
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Rag2Mol: structure-based drug design based on RAG

> Briefings in Bioinformatics (Oxford) | 2025 | Method | bio, medical, chem
## 📌 TL;DR
Rag2Mol is a RAG-based structure-based drug design (SBDD) framework that uses a two-stage retriever (Global + Molecular Retriever) to dynamically pull purchasable reference molecules from the ZINC DB, guiding the molecule generation of a GVP-based autoregressive model, and simultaneously improving synthesizability and binding affinity.
## 🎯 Research Background and Motivation
**Limitations of existing SBDD methods**
- Existing AI SBDD models ignore synthesizability, so generated molecules often lie outside the actually synthesizable chemical space
- Data bias problem: the training data (CrossDocked2020) covers only an extremely small fraction of the entire protein-ligand complex space
- Existing virtual screening uses 3 AI models sequentially (screening, docking, binding-affinity prediction) → false positives from each stage accumulate, lowering success rate
- The extensive downstream validation process for generated molecules (docking calculations, wet-lab experiments) is complex and accumulates uncertainty

**Why this research is needed**
- Applying RAG to SBDD dynamically leverages an external purchasable molecule DB (ZINC) → can resolve the synthesizability problem
- A single model integrates screening, docking, and generation → reduces error accumulation of the sequential AI-model pipeline
- Two workflows (G: de novo generation, R: similar-molecule retrieval) can address diverse real-world drug development scenarios
## 🏗️ System Architecture
```javascript
[Input: protein pocket 3D structure]
        ↓
┌─────────────────────────────────────┐
│  Step 1: Global Retriever            │
│  ZINC → virtual screening + Vina docking │
│  → build pocket-specific small-molecule DB │
└─────────────────┬───────────────────┘
                  ↓
┌─────────────────────────────────────┐
│  Step 2: autoregressive molecule generation (iterative) │
│  Molecular Retriever:               │
│    per-pocket DB → select reference molecule │
│  cross-KNN message passing →        │
│    reference molecule info → fused into fragment │
│  GVP-based model: predict next atom │
└─────────────────┬───────────────────┘
                  ↓
    ┌─────────────┴─────────────┐
    ↓                           ↓
[Rag2Mol-G]              [Rag2Mol-R]
use generated molecule directly   cluster generated molecules
                          select scaffold
                          ZINC similarity search
                          → output purchasable molecules
                  ↓
┌─────────────────────────────────────┐
│  Step 3: filtering + validation     │
│  Vina/QED/SA/Lipinski/LogP criteria │
│  → recompute Vina docking → wet-lab experiments │
└─────────────────────────────────────┘
```
## 🔑 Detailed Description of Core Modules
### 1. Global Retriever (building the pocket-specific DB)
- Input: protein pocket 3D coordinates
- First-pass filtering of small molecules with binding potential from ZINC using a virtual screening model
- Dock the filtered molecules into the pocket with AutoDock Vina → jointly consider binding affinity + synthesizability
- Result: per-pocket small-molecule DB (set of bindable + purchasable molecules)

### 2. Molecular Retriever (selecting reference molecules)
- At each step of molecule generation, compare the currently generated fragment with the molecules in the per-pocket DB
- Select the most relevant reference molecule via a cross-KNN graph
- Fuse the structural information of the reference molecule into the generated fragment through message passing in hidden space

### 3. GVP-based autoregressive generator
- E(3)-equivariant GVP (Graph Vector Perceptron) architecture
- Sequentially predicts atoms conditioned on protein pocket residues + reference molecules
- At each step predicts atom type, 3D coordinates, and bond type
- Trained on CrossDocked2020 (retriever active even during training)

### 4. Two workflows
| Workflow | Mode of operation | Suitable situation |
| **Rag2Mol-G** | Directly generate de novo molecules using the per-pocket DB as reference | Targets requiring multiple binding templates, exploring high-affinity de novo candidates |
| **Rag2Mol-R** | Generated molecules → clustering → scaffold → ZINC similarity search | Exploring synthesizable analogs, undruggable targets, replacing virtual screening |

### Tool/DB Integration Table
| Module | DB/tool used | Role |
| Global Retriever | ZINC (230M+ compounds) | Source of purchasable molecules |
| Global Retriever | AutoDock Vina | Docking score calculation |
| Molecular Retriever | CrossDocked2020 per-pocket DB | Reference molecules during training/inference |
| Evaluation | GNINA | CNN affinity calculation |
| Evaluation | PoseBusters | Physical validity verification |
| Real-world application | PDB (RCSB) | Download target protein 3D structures |

## 🧪 Experiments and Evaluation
### Evaluation tasks and datasets
- **Benchmark**: CrossDocked2020 test set (100 protein pockets)
- **Comparison models (SBDD)**: Pocket2Mol, ResGen, AR, GraphBP, FLAG, TargetDiff, Pocket2MolRL, Decomp-o, Decomp-r
- **Comparison models (virtual screening, vs. Rag2Mol-R)**: ConPLex, DrugBAN, UdanDTI
- **Real-world case**: PTPN2 (protein tyrosine phosphatase, undruggable target, no clinically completed inhibitor)

### Evaluation metrics
| Metric | Description |
| Vina Dock (kcal/mol) | Vina binding energy before docking |
| Vina Score (kcal/mol) | Binding energy after redocking |
| %↑ Vina | Fraction with higher Vina score than the native ligand |
| PB-Valid | Fraction of physically valid molecules verified by PoseBusters |
| CNN Affinity | GNINA-based CNN binding affinity |
| Clash | Number of steric clashes |
| QED | Quantitative estimate of drug-likeness |
| SA | Synthetic accessibility score |
| Lipinski | Compliance with Lipinski's rule of 5 |
| LogP | Lipophilicity |

### Main results
- Rag2Mol achieves the best or near-best performance on almost all metrics
- In particular, the top 1/3 molecules by Vina Dock/Score consistently achieve lower (better) binding energy than the native ligand
- Rag2Mol-R: broader chemical-space coverage and higher target specificity than ConPLex/DrugBAN/UdanDTI
- PTPN2 case: both workflows discover promising inhibitor candidates (surpassing existing active inhibitors)
## 💡 Core Contributions
1. **Applying RAG to SBDD**: extends the text RAG paradigm to 3D structure-based molecule generation
2. **Two-stage retriever**: Global Retriever (building per-pocket DB) + Molecular Retriever (per-step reference selection during generation) jointly guarantee synthesizability + affinity
3. **Two workflows**: de novo generation (Rag2Mol-G) and similar-molecule retrieval (Rag2Mol-R) address diverse practical scenarios
4. **Extensible framework**: modular design that can also swap in SBDD backbone models other than GVP
5. **Real-world validation**: discovery of promising inhibitors for the undruggable PTPN2 target
## ⚠️ Limitations
- Performance depends on the quality and coverage of the ZINC DB
- High computational cost of the Global Retriever (virtual screening + docking)
- No LLM used → natural-language-based interaction or knowledge integration not possible
- Inherent bias of the CrossDocked2020 training data (centered on ligand-pocket pairs already known in PDB)
- Rag2Mol-R's similarity search is Morgan fingerprint-based → limited in reflecting 3D structural similarity
## 🔗 Related Research and Related Links
- **Paper link**: [https://doi.org/10.1093/bib/bbaf265](https://doi.org/10.1093/bib/bbaf265)
- **RECOMB 2025 version**: [https://doi.org/10.1007/978-3-031-90252-9_15](https://doi.org/10.1007/978-3-031-90252-9_15)
- **GitHub**: [https://github.com/CQ-zhang-2016/Rag2Mol](https://github.com/CQ-zhang-2016/Rag2Mol)
- **Main baselines**: Pocket2Mol (ICML 2022), TargetDiff (ICLR 2023), ResGen (Nature Machine Intelligence 2023)
- **Similar methodologies**: PocketCrafter (Novartis, Shen et al. 2024), FLAG (ICLR 2023)
- **Datasets used**: CrossDocked2020 (Francoeur et al., J. Chem. Inf. Model. 2020)
