---
title: LLaMP - Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation
bib_key: DBLP:conf/emnlp/ChiangHCR25
year: 2025
domain: material
type: Method
venue: EMNLP 2025
paper_link: https://arxiv.org/abs/2401.17244
---
# LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation

> EMNLP 2025 | Method + Benchmark | material
> Chiang, Chou, Riebesell — UC Berkeley / Cambridge / LBNL · arXiv:2401.17244

## TL;DR
A RAG agent system that wraps the Materials Project (MP) API in a ReAct-based hierarchical multi-agent architecture so that the LLM directly queries and verifies DFT-computed values, and measures response variability with a **Self-Consistency of Response (SCoR)** metric. It reduces the bulk modulus MAE from GPT-4's 41.225 **to 14.574, a 65% reduction**, and improves magnetic ordering classification accuracy from GPT-4's 0.48 **to 0.98**.

## Background
- **The hallucination problem of LLMs**: GPT-3.5 hallucinates C₁₁=289.2 GPa for the NaCl elastic tensor (~4× the DFT value of 76 GPa), and omits the C₂₂·C₃₃·C₅₅·C₆₆ values (paper p.7).
- **Reproducibility of numerical data**: in high-stakes self-driving labs, responses to the same query must be consistent, yet a vanilla LLM generates different numbers on every call.
- Existing prompt-based approaches (fine-tuning methods such as StructChem, Darwin) suffer from (a) overfitting to specific edge cases, leading to poor reproducibility, and (b) difficulty combining diverse data sources.
- **Materials Project** provides DFT-based properties of ~150,000 inorganic compounds through a public API → ground truth can be fetched in real time.

## Construction Methodology

```
Step 1 — Materials Project (MP) API
  ┌─ DFT (PBE-GGA) based DB of ~150,000 inorganic compounds
  ├─ Bulk/shear modulus, bandgap, formation energy, magnetic ordering,
  │  3D crystal structure, elastic tensor, synthesis recipes, ...
  └─ MAPI wrapped as langchain Tools (MPThermoExpert, MPElasticityExpert, …)

Step 2 — Hierarchical ReAct Agent (Fig. 1)
  ┌─────────── Supervisor ReAct Agent (GPT-4) ───────────┐
  │  · Action space Â = A ∪ L (action + language)        │
  │  · Decompose user query → delegate to appropriate Assistant │
  │  · Integrate each assistant response as episodic memory for reasoning │
  └───────────────────────────────────────────────────────┘
           ↓                       ↓
  ┌─ MPThermoExpert ──┐    ┌─ MPElasticityExpert ─┐
  │  Formation energy  │    │  Bulk/shear modulus  │
  │  Phase diagram     │    │  Young's modulus     │
  └────────────────────┘    └──────────────────────┘
           ↓                       ↓
  ┌─ MPStructureExpert ┐    ┌─ MPMagnetismExpert ──┐
  │  Crystal structure │    │  Magnetic ordering   │
  │  Lattice params    │    │  Magnetization       │
  └────────────────────┘    └──────────────────────┘
  └─ MPSynthesisExpert ── experimental synthesis recipes + DOI

Step 3 — SCoR metric definition (Sec 4.2)
  Over N repeated calls, n valid responses, ˆσ = standard deviation
  ┌─ Precision = (1/n) · |median ± ˆσ|     [numerical uncertainty]
  ├─ Coefficient of Precision (CoP)
  │   = exp(-Precision)  ∈ [0,1]
  ├─ Confidence = n / N                     [response availability]
  └─ SCoR = CoP × Confidence  ∈ [0, 1]
            ↑                         ↑
        SCoR=1: always the same response   SCoR=0: highly inconsistent

Step 4 — Evaluation targets
  ┌──────────────────────┬────────────────────────────┐
  │ Task                │ Sampling                    │
  ├──────────────────────┼────────────────────────────┤
  │ Bulk Modulus (GPa)  │ 10 3d transition metals (Sc-Zn) │
  │ Formation Energy    │ Common compounds (Si, Ge,  │
  │  (eV/atom)         │  InSe, MoS₂, BaTiO₃, CsPbI₃)│
  │ Electronic Bandgap  │ Common semiconductors +     │
  │  (eV)              │  Multi-element (Ba(PdS₂)₂,  │
  │                    │  FePO₄, DyBi₂IO₄, ...)      │
  │ Magnetic Ordering   │ 800 random unary/binary/    │
  │  (FM/AFM/FiM/NM)   │  ternary compounds          │
  └──────────────────────┴────────────────────────────┘
  N=5 repetitions per task → compute SCoR + MAE

Step 5 — Baseline comparison
  · StructChem (chemistry prompting)
  · Darwin (Materials fine-tuned)
  · GPT-4+Serp (web search augmented)
  · Vanilla GPT-4, Gemini-Pro, Llama 3-8B, GPT-3.5
```

## Input
- **User query**: natural language (e.g., "What's the stiffest material with the lowest formation energy in Si-O system?")
- **Available modalities**: single compound, chemical system (e.g., Si-O), simultaneous querying of multiple properties

## Output (Output / Answer Format)
- **Numerical response**: single value or dict (e.g., `{"Sc": {"Voigt": 45.715, "Reuss": 45.34, "VRH": 45.528}}`)
- **Classification response**: FM / AFM / FiM / NM (magnetic ordering)
- **Higher-order data**: 3D crystal structure, 6×6 elastic tensor matrix
- **Reference information**: MP material ID (mp-XXXXX), DOI of the experimental synthesis paper

## Example Evaluation Questions (paper body + Fig. A.1 / Table B5)

### Multi-domain ReAct query (Fig. A.1, p.13)
> **Q:** *"What's the stiffest material with the lowest formation energy in Si-O system?"*
>
> **LLaMP supervisor trace (paper p.13 verbatim):**
> > "To answer this question, I need to find materials in the Si-O system with the lowest formation energy and the highest stiffness. I will use the MPThermoExpert tool to search for materials in the Si-O system and sort them by formation energy. After finding candidates, I will need to use the MPElasticityExpert tool to determine the stiffness of these materials."
>
> ```json
> { "action": "MPThermoExpert",
>   "action_input": { "input": "What are the materials with the lowest formation energy in the Si-O system?" } }
> ```
> ↓ (retrieves several polymorph candidates of Si₂O₅, SiO₂)
> ```json
> { "action": "MPElasticityExpert",
>   "action_input": { "input": "What are the bulk and Young's moduli for Si2O5 (mp-862998), SiO2 (mp-733790), SiO2 (mp-6922), SiO2 (mp-556985), and SiO2 (mp-556994)?" } }
> ```
> ↓ final: "The material with the highest bulk modulus would be considered the stiffest."

### Bulk Modulus query (Table 1, 3d transition metals)
> **Q:** *"What are the bulk moduli of Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn?"*
>
> LLaMP returns all three values Voigt / Reuss / VRH for each element (MP DFT based).
> Vanilla GPT-4 generates a single estimate as a hallucination.

### Higher-order data — Elastic Tensor (paper p.7)
> **Q:** *"What is the full elastic tensor of NaCl?"*
>
> - **DFT ground truth**: C₁₁ ≈ 76 GPa, 6×6 full tensor matrix
> - **GPT-3.5 (vanilla) response**: "C₁₁ = 289.2 GPa" (~4× error), omits the C₂₂·C₃₃·C₅₅·C₆₆ values, ignores matrix format
> - **LLaMP**: retrieves the exact 6×6 tensor from the MP API

### Magnetic ordering classification (800 random compounds, Fig. 3)
> **Q:** *"What is the magnetic ordering of [compound]?"* → FM / AFM / FiM / NM
>
> Confusion matrix (LLaMP w/ GPT-4): nearly all of the 136 FM-class compounds are correct → accuracy 0.98.

## Main Evaluation Results

### Table 1 — Bulk Modulus & Formation Energy (average of 5 runs)
| Model | **Bulk K (GPa) MAE↓** | SCoR↑ | **ΔH_f (eV) MAE↓** | SCoR↑ |
|---|---|---|---|---|
| **LLaMP** | **14.574** | **0.900** | **0.009** | **0.953** |
| StructChem | 41.017 | 0.200 | 3.146 | 0.200 |
| Darwin | 156.266 | 0.499 | 2.245 | 0.997 |
| GPT-4 + Serp | 41.742 | 0.352 | 8.214 | 0.745 |
| GPT-4 | 41.225 | 0.910 | 1.680 | 0.180 |
| Gemini-Pro | 43.429 | 0.169 | 1.630 | 0.737 |
| Llama 3 | 41.874 | 0.010 | 4.501 | 0.153 |

→ **LLaMP reduces the K MAE by 65% versus GPT-4 (41→15) and the ΔH_f MAE by 99% (1.68→0.009)**, while also achieving the highest SCoR.

### Table 2 — Magnetic Ordering & Magnetization (800 compounds)
| Model | Mag. Ordering Acc. | F1 | Magnetization MAE | R² |
|---|---|---|---|---|
| **LLaMP (GPT-4)** | **0.98** | **0.89** | **0.045** | **0.992** |
| GPT-4 | 0.48 | 0.26 | 1.611 | -0.201 |
| LLaMP (GPT-3.5) | 0.96 | 0.88 | 1.896 | 0.407 |
| GPT-3.5 | 0.23 | 0.18 | 1.988 | -0.024 |

→ **Classification accuracy 0.23 → 0.96 (GPT-3.5) / 0.48 → 0.98 (GPT-4)** — RAG virtually eliminates parametric hallucination.

### Key Findings
- **LLaMP improves magnetic ordering accuracy by +50pp over vanilla GPT-4** (confirming that lack of domain knowledge is the LLM's main bottleneck).
- Responses close to SCoR=1 can be integrated into **reproducible scientific workflows** (a prerequisite for autonomous lab integration).
- Hierarchical multi-agent (supervisor + assistants) is **superior to flat planning** — a single agent frequently violates the API schema when it sees too much information at once.

## Limitations
- **Systematic error of MP DFT**: PBE-GGA underestimates the bandgap by 30~50% → the ground truth itself may differ from experimental values.
- **Limited MP coverage**: only some experimentally synthesized compounds are registered in MP → some classes such as MOFs, COFs, and polymers are absent.
- **Dependence on function-calling**: directly affected by the backend LLM's tool-use ability (GPT-3.5 violates the schema in some cases).
- **No fallback when the ReAct loop fails**: degrades into hallucination if API response parsing fails.
- **Interactive latency**: with 5 repetitions plus multi-agent calls, a single query takes tens of seconds.

## Related links
- **Paper**: [arXiv:2401.17244](https://arxiv.org/abs/2401.17244)
- **EMNLP 2025 Anthology**: [ACL Anthology](https://aclanthology.org/2025.emnlp-main)
- **Materials Project**: [materialsproject.org](https://materialsproject.org)
- **DBLP**: [conf/emnlp/ChiangHCR25](https://dblp.org/rec/conf/emnlp/ChiangHCR25)
- **Papers that use this system as a comparison target**: HoneyComb (EMNLP Findings 2024) — compared under the same protocol on MaScQA + LLaMP MP property tasks
