---
notion_id: 355f2dcd-4912-8113-a854-f25bfbf12882
title: TaLiRAGen: target-aware ligand generation via RAG LLMs
bib_key: nan2026taliragen
year: 2026
domain: chem, bio, medical
type: Method
venue: Molecular Diversity
paper_link: https://doi.org/10.1007/s11030-026-11483-9
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# TaLiRAGen: target-aware ligand generation via RAG LLMs

> Molecular Diversity (Springer Nature) | 2026 | Method | chem · bio · medical
## 📌 TL;DR
A no-training framework that combines RAG and LLMs to generate ligands matched to a protein target without any target-specific training.

Background: ligand - a ligand is a small molecule that binds to a specific protein (typically a receptor or enzyme). It is a core concept in drug development: when there is a protein associated with a disease, the goal is to design a molecule that binds precisely to that protein to inhibit or activate its function. The TaLiRAGen paper aims exactly at designing such ligands with AI. Given a specific target protein, it generates a molecular structure (in SMILES format) that is likely to bind well to it, using an LLM+RAG. Whether the binding is good is scored by simulation with docking software called AutoDock Vina.

## 🎯 Background and Motivation
**Limitations of existing methods:**
- Generative models such as VAEs and diffusion models depend heavily on target-specific training data, making them difficult to apply to new targets where data is scarce.
- Existing methods do not sufficiently leverage the vast biochemical knowledge already embedded in LLMs.

**Why this research is needed:**
- In Structure-Based Drug Design (SBDD), generating ligands with high binding affinity to a specific protein target is a core challenge.
- Even without training, combining an LLM's general chemistry knowledge with retrieval from external databases enables ligand generation that can be flexibly applied to diverse targets.
## 🏗️ Architecture
```javascript
[Input: protein target structure / sequence]
        ↓
[Retriever] retrieves protein-ligand context from diverse repositories
        ↓
[CoT-augmented Multi-turn Prompting] — integrates the retrieved context into the LLM
        ↓
[LLM Generator] — generates ligand candidates in SMILES format
        ↓
[Docking Feedback (AutoDock Vina)] — computes binding affinity, filters out low candidates
        ↓
[Evidence-Theoretic Normalization integrated evaluation] — integrates QED + SA + Vina score
        ↓
[Output: optimal ligand candidates satisfying structural constraints]
```
[image]
## 🔑 Detailed Description of Core Modules
**① RAG-based Retrieval**
- Retrieves protein-ligand context from diverse repositories.
- The retrieved context includes information on similar protein-ligand pairs to guide the LLM's generation direction.

**② CoT-augmented Multi-turn Prompting**
- Combines Chain-of-Thought reasoning with a multi-turn conversation format so that the LLM processes biochemical context step by step.
- Structural constraints such as LogP and ring count are specified in the prompt to enable customized ligand generation.

**③ Docking Feedback-based Refinement**
- Docks the generated SMILES ligands to the protein target using AutoDock Vina.
- Uses the docking score (Vina score) as feedback to iteratively refine the molecules.

**④ Evidence-Theoretic Normalization Integrated Evaluation Metric**
- Integrates binding affinity and drug-like properties via evidence-theoretic normalization.
- Combines QED (quantitative estimation of drug-likeness), SA (synthetic accessibility), and Vina docking score into a single integrated evaluation metric.
## 🧪 Experiments and Evaluation
**Evaluation tasks and datasets:**
- Uses the **CrossDocked2020** test set. After filtering the 969 target IDs by adequacy and reliability criteria, **908 targets** are used in the end.
- Generates **5 ligands** per target and evaluates them.
- Docking score-based evaluation via AutoDock Vina.

**Main evaluation metrics:**
| Metric | Description |
| Vina docking score | Binding affinity (lower is better, kcal/mol) |
| QED | Quantitative estimation of drug-likeness (0~1, higher is better) |
| SA | Synthetic accessibility (0~1, higher is better) |
| Integrated metric | Applies evidence-theoretic normalization, integrating the three metrics above |
| LogP, ring count, etc. | Whether structural constraints are satisfied |

**Comparison targets:**
- Compares binding affinity and drug-likeness against existing VAE-based and diffusion model-based SBDD methods (specific numbers not confirmed as the full text is unavailable).
## 💡 Key Contributions
- **No-training framework**: generates ligands using the LLM's built-in chemistry knowledge + RAG without target-specific training → applicable even to data-scarce targets.
- **Evidence-theoretic normalization integrated metric**: integrates binding affinity + drug-likeness into a single metric, improving the consistency of evaluating generated ligands.
- **Prompt-based structural customization**: structural constraints such as LogP and ring count can be flexibly reflected via prompts.
## ⚠️ Limitations
- The specific DB names and LLM model names used cannot be confirmed because the full paper is not publicly available.
- Verification of SMILES validity and synthetic accessibility (SA) remains at a computational level, with no experimental validation.
- Docking-based binding affinity evaluation may differ from actual wet-lab binding affinity.
- It is unclear whether diversity and novelty metrics of the generated ligands are reported in detail.
## 🔗 Related Research and Related Links
- **Paper link**: [https://doi.org/10.1007/s11030-026-11483-9](https://doi.org/10.1007/s11030-026-11483-9)
- **Code/Data**: GitHub ([https://github.com/yxjacksonyyds/T](https://github.com/yxjacksonyyds/T)), Google Drive supplementary materials
- **PubMed**: [https://pubmed.ncbi.nlm.nih.gov/41723766/](https://pubmed.ncbi.nlm.nih.gov/41723766/)
- **Keywords**: Structure-Based Drug Design (SBDD), Retrieval-Augmented Generation, Chain-of-Thought, AutoDock Vina, evidence-theoretic normalization, no-training ligand generation
