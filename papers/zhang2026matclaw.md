---
title: "MatClaw: An Autonomous Code-First LLM Agent for End-to-End Materials Exploration"
bib_key: "zhang2026matclaw"
year: 2026
domain: material
type: Method
venue: arXiv 2026
paper_link: https://arxiv.org/abs/2604.02688
---
# MatClaw: An Autonomous Code-First LLM Agent for End-to-End Materials Exploration

zhang2026matclaw | 2026 | arXiv 2026 | Method | [material] | [paper](https://arxiv.org/abs/2604.02688)

**Retriever**: RAG over domain source code (pymatgen, atomate2, jobflow, dpdata, DeePMD-kit)
**Eval Task**: Machine-learning force field training (active learning), Curie temperature prediction, heuristic parameter-space search
**Eval Metric**: Per-step API-call accuracy (~99%), end-to-end task completion
**Method Name**: MatClaw
**Modality**: Code, Text, Computational materials data

> arXiv 2026 | 2026 | Method | material
#### 📌 TL;DR
A code-first LLM agent that directly writes and executes Python code. It is an autonomous agent for materials exploration that combines RAG over domain source code with a four-layer memory architecture to achieve ~99% API-call accuracy and HPC-cluster-based multi-code workflow orchestration.

#### 🎯 Background
**Limitations of existing approaches**
- Existing LLM agents for computational materials science rely on pipeline architectures fixed to specific simulation codes and on manually written tool functions
- A scalability problem in which the number of tool functions surges as the task scope expands

**Why this system is needed**
- The need to automate multi-code workflows that freely combine multiple domain libraries (pymatgen, atomate2, etc.)
- The need for memory management that prevents context loss in long, multi-day workflows

#### 🔨 Architecture
MatClaw directly generates and executes Python without predefined tool functions, freely combining installed domain libraries. **Four-layer memory architecture**: prevents context loss during progress. **RAG over domain source code**: retrieves pymatgen, atomate2, jobflow, dpdata, and DeePMD-kit source code to improve per-step API-call accuracy to ~99%. It orchestrates workflows on remote HPC clusters.

#### 📊 Key Results
| Item | Value |
|---|---|
| API-call accuracy | ~99% (RAG over domain source code) |
| Supported libraries | pymatgen, atomate2, jobflow, dpdata, DeePMD-kit |
| Demonstration task 1 | CuInP2S6 machine-learning force field training (active learning) |
| Demonstration task 2 | Curie temperature prediction |
| Demonstration task 3 | Heuristic parameter-space search |
| Code-generation reliability | High (strength confirmed) |
| Tacit domain knowledge handling | Insufficient (limitation confirmed) |

#### ⚠️ Limitations
- Struggles with tacit domain knowledge (appropriate simulation timescales, equilibration protocols, sampling strategies)
- Literature self-learning and expert constraint specification partially compensate for this gap, but full autonomy is not yet achieved
- Intermediate error recovery in multi-day workflows remains a challenge

## Related links
- **Paper (arXiv)**: [https://arxiv.org/abs/2604.02688](https://arxiv.org/abs/2604.02688)
