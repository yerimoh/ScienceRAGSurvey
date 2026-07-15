---
title: "HoneyComb: A Flexible LLM-Based Agent System for Materials Science"
bib_key: DBLP:conf/emnlp/ZhangSHML24
year: 2024
domain: material
type: Method
venue: Findings of EMNLP 2024
paper_link: https://doi.org/10.18653/v1/2024.findings-emnlp.192
---
# HoneyComb: A Flexible LLM-Based Agent System for Materials Science

> Findings of EMNLP 2024 (pp. 3369–3382) | Method | material
> Zhang, Su, Huang, Ma, Li et al. · DBLP: `conf/emnlp/ZhangSHML24`

## TL;DR
A three-component LLM agent system for materials science combining **MatSciKB (38,469 entry KB)** + **ToolHub (general + specialized APIs based on Inductive Tool Construction)** + a **hybrid Retriever (BM25 + Contriever)**. GPT-4-based HoneyComb achieves **MaScQA 79.07% (vs GPT-4 alone 58.46%, +20.61pp)** and **SciQA 96.54% (vs 90.84%, +5.70pp)**. It lifts HoneyBee-7B from a 16.62% baseline to 79.69%, a dramatic +63pp increase.

## Background
- **Limitations of materials-science LLMs**: existing models rely on general-domain training data → they lack materials-science-specific knowledge (arXiv preprints, Wikipedia materials entries, textbook formulas, etc.).
- **The success of domain agents such as Coscientist (Boiko et al. 2023)** suggests the approach is applicable to materials science as well.
- Static LLMs cannot reflect data sources that are updated daily, such as PubMed / Materials Project → real-time tool augmentation is needed.
- The release of **MaScQA (Zaki et al. 2023)** provided a materials-science evaluation set → establishing a basis for quantitatively validating tool-augmented systems.

## Construction Methodology

```
HoneyComb overall architecture (Fig. 1, p.4)

Query → [Knowledge Retrieval Phase]
            │
            ├─ MatSciKB (semantic search)
            └─ ToolHub Tool Selection
                  ↓ Executor (iterative)
            ┌─ Tool Assessor: decides which tool to use
            └─ Tool Executor: execute + evaluate result → refine
                  ↓
            Retriever (BM25 + Contriever hybrid)
                  ↓
            LLM → Final Answer

────────────────────────────────────────
Component 1: MatSciKB (Table 1, p.6 verbatim figures)
  Total entries: 38,469
  ┌──────────────────────────────────┬────────┐
  │ Source                           │ Entries│
  ├──────────────────────────────────┼────────┤
  │ Materials Science Papers (arXiv) │ 20,384 │
  │ Wikipedia (Materials Science)    │  3,620 │
  │ Materials Science Textbook       │  1,930 │
  │ Materials Science Dataset        │ 10,473 │
  │ Materials Science Formula        │     57 │
  │ GPT-generated Examples           │  2,005 │
  └──────────────────────────────────┴────────┘
  · 16-category tree structure
  · CRUD operation support (real-time updates)

────────────────────────────────────────
Component 2: ToolHub (Inductive Tool Construction, Algorithm 1)
  General Tools (Table 2):
    Google Search, Arxiv Search, Wikipedia Search,
    YouTube Search, Python REPL
  Specialized Tools:
    domain functions such as the Materials Project API
    + a set of sub-tools auto-synthesized by ITC

  Inductive Tool Construction (ITC):
    1. Select a random subset D_train of computational questions
    2. LLM automatically parses tool descriptions and parameters
    3. Decompose into sub-tools per task
    4. Remove duplicate and unnecessary tools (refine)

────────────────────────────────────────
Component 3: Hybrid Retriever
  · BM25 (lexical) → fast keyword match
  · Contriever (dense) → semantic/contextual matching
  · Simple queries: BM25 / complex queries: Contriever (m < k+1 results)

────────────────────────────────────────
Agent-ToolHub 2-phase Protocol
  Phase 1 — Tool Assessor:
     "original query → select a candidate subset of tools"
  Phase 2 — Tool Executor (Fig. 2):
     perform the thought-process
     ├─ solvable with a single tool → execute
     └─ complex → multi-tool decompose
```

## Input
- **User natural-language query** (materials-science domain)
- **Task types**:
  - factoid (e.g., "The crystal structure of Fe₂O₃?")
  - computational (e.g., "The formation energy of BaTiO₃?")
  - reasoning (e.g., GATE exam NUM/MATCH/MCQ)

## Output (answer format)
- Natural-language answer (with citations + sources)
- MaScQA format: A/B/C/D or a numeric value
- SciQA format: 4-choice answer

## Real task examples

### MaScQA — GATE past exams (using Zaki et al. 2023, 650 questions)
> **Task distribution**:
> · MCQ 285 / MATCH 70 / MCQN 67 / NUM 228
> · 14 materials-science sub-domains (thermodynamics, atomic structure, mechanical behavior, …)
>
> HoneyComb processing flow:
> · MCQ conceptual → MatSciKB search → retrieve relevant textbook chunks + Wikipedia entries → LLM answer
> · NUM computational → ToolHub's Python REPL or specialized formula tool → compute numeric value

### SciQ — 11,679 multiple-choice science (using Welbl et al. 2017; denoted SciQA in this paper)
> **Task**: 4-choice biology/chemistry/physics questions at an early-undergraduate level
> On SciQ, HoneyComb improves by +5.5%p using ToolHub alone (Table 5)

### Real-world queries (system demo)
> **Q (factoid):** "What is the crystal structure of perovskite BaTiO₃?"
> → MatSciKB search → "BaTiO₃: perovskite structure, cubic system, a≈4.01Å" → answer
>
> **Q (computational):** "What is the formation energy of Fe₂O₃?"
> → ToolHub → Materials Project API → ΔH_f ≈ -2.03 eV/atom → answer + DOI

## Key evaluation results

### Table 3 — HoneyComb integration effect (Accuracy %)
| Backbone LLM | MaScQA baseline | + HoneyComb | Δ (pp) | SciQA baseline | + HoneyComb | Δ (pp) |
|---|---|---|---|---|---|---|
| **HoneyBee-7B** (materials-science SFT) | 16.62 | **33.38** | **+16.76** | 33.96 | **79.69** | **+45.73** |
| GPT-3.5 | 33.54 | 38.46 | +4.92 | 90.69 | 90.83 | +0.14 |
| **GPT-4** | 58.46 | **79.07** | **+20.61** | 90.84 | **96.54** | **+5.70** |
| LLaMA2 | 22.15 | 36.31 | +14.16 | 75.79 | 78.66 | +2.87 |
| LLaMA3 | 24.62 | 47.23 | +22.61 | 93.00 | 93.32 | +0.32 |

→ **HoneyBee+HoneyComb jumps +45.73pp on SciQA** (16.62 → 79.69) — the largest effect occurs when RAG is combined with a domain-specific SFT model.

### Table 5 — Ablation Study (GPT-4 basis)
| Setting | MatSciKB | ToolHub | Retriever | **MaScQA Acc.** | **SciQA Acc.** |
|---|---|---|---|---|---|
| Baseline GPT-4 | – | – | – | 61.38 | 90.84 |
| + MatSciKB only | ✓ | – | – | 78.31 (+16.93) | – |
| + ToolHub only | – | ✓ | – | 73.23 (+11.85) | 96.34 (+5.50) |
| **Full HoneyComb** | ✓ | ✓ | ✓ | **79.07** | **96.56** |

→ MaScQA: MatSciKB has the largest standalone effect (+16.93pp), reaching +17.69pp when combined with ToolHub.
→ SciQA: reaching the 96% range with ToolHub alone (general tools suffice for simple fact verification).

### Table 4 — Performance by material category (e.g., Atomic Structure)
| Model | Baseline | + HoneyComb |
|---|---|---|
| HoneyBee | 12.0 | 34.00 |
| GPT-3.5 | 35.00 | 32.00 (drop) |
| GPT-4 | 55.00 | (HoneyComb applied) |
| ... | ... | ... |

→ **LLaMA-3 improves +33.34pp on Material Testing.** GPT-3.5 shows performance drops in some categories — domain-mismatch scenarios exist.

## Limitations
- **Generalizability beyond MaScQA/SciQA is unverified** (acknowledged by the authors, Limitations section).
- **MatSciKB curation details are undisclosed**: the selection criteria and deduplication procedure for the 20,384 arXiv papers are not specified in the text.
- **ToolHub depends on Materials Project API availability** — vulnerable to service outages or rate limits.
- **Extensibility to domains beyond materials science is unverified** (authors' own assessment).
- **Performance drops in some categories with GPT-3.5** — a modality-mismatch case where RAG is not always helpful.
- **No evaluation of open-ended tasks such as research design and prediction** (focus is on MCQ/NUM).
- **MatSciKB may be a static snapshot**: a real-time update mechanism is mentioned, but evaluation is batch.

## Related links
- **Paper**: [EMNLP Findings 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.192)
- **DBLP**: [conf/emnlp/ZhangSHML24](https://dblp.org/rec/conf/emnlp/ZhangSHML24)
- **Benchmarks used**:
  - MaScQA — Zaki et al. 2023 (Digital Discovery), 650 GATE questions
  - SciQA → actually SciQ (Welbl et al. 2017), 11,679 MC science questions
- **Compared systems**: LLaMP (Chiang et al. 2025), Darwin, StructChem, HoneyBee-7B SFT
