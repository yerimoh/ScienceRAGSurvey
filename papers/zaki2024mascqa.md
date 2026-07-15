---
title: MaScQA - Investigating Materials Science Knowledge of Large Language Models
bib_key: zaki2024mascqa
year: 2024
domain: material
type: benchmark
venue: Digital Discovery (RSC)
paper_link: https://pubs.rsc.org/en/content/articlelanding/2024/dd/d3dd00188a
---
# MaScQA: Investigating Materials Science Knowledge of Large Language Models

> Digital Discovery 2024 | Benchmark | material
> Zaki, Mausam, Krishnan — IIT Delhi (M3RG-IITD) · arXiv:2308.09115

## TL;DR
A benchmark for evaluating the undergraduate-graduate-level materials science knowledge of LLMs, built from **650 questions** drawn from past papers of India's GATE (Graduate Aptitude Test in Engineering) in Materials Science and Metallurgical Engineering, classified along 4 question structures (MCQ/MATCH/MCQN/NUM) × 14 materials science domains. GPT-4-CoT achieves the best performance at 62.0%, and GPT-4's conceptual errors (64%) far outweigh its computational errors (36%), quantifying that lack of domain knowledge is the main bottleneck. HoneyComb (GPT-4 + MatSciKB + ToolHub) reaches 79.07%, demonstrating the effect of RAG augmentation.

## Background
- Domain-specialized LLMs (ChemGPT, BioBERT, etc.) exist in abundance for chemistry and biology, but **materials science lacks a dedicated evaluation set**.
- Existing LLM benchmarks (MMLU, SciQ, etc.) focus on general scientific common sense and do not include undergraduate-graduate-level computational problems in thermodynamics, crystallography, or phase transition.
- The GATE exam is a **national-level graduate admissions test** taken by more than 800,000 candidates in India each year (an average of 100,000 for major departments); it is jointly set by 5 IIT institutions to verify the core competencies of materials science and metallurgy undergraduate graduates → it has a reliable answer key.

## Construction Methodology

```
Step 1 — Source selection
  └─ GATE (Graduate Aptitude Test in Engineering) administered by India's IITs
      Collection of past papers from the Materials Science and
      Metallurgical Engineering (MT) section
  └─ Official source: gate.iitkgp.ac.in/old_question_papers.html
      (IIT Kharagpur is one of the GATE-administering institutions)

Step 2 — Question structure classification (Axis A)
  ┌──────────┬────────────────────────────────────────┬─────┐
  │ Type     │ Description                             │ Num │
  ├──────────┼────────────────────────────────────────┼─────┤
  │ MCQ      │ 4-option multiple choice, concept-      │ 285 │
  │          │ focused (1 correct answer)              │     │
  │ MATCH    │ Matching two lists, 4-option            │  70 │
  │ MCQN     │ 4 options + numerical calculation req.  │  67 │
  │ NUM      │ Numerical entry (no options)            │ 228 │
  ├──────────┼────────────────────────────────────────┼─────┤
  │ Total    │                                        │ 650 │
  └──────────┴────────────────────────────────────────┴─────┘
  (13 of the MCQ questions have a multiple-correct-answer format)

Step 3 — Domain classification (Axis B, 14 categories)
  thermodynamics · atomic structure · mechanical behavior ·
  materials manufacturing · material applications · phase transition ·
  electrical properties · material processing · transport phenomenon ·
  magnetic properties · material characterization · fluid mechanics ·
  material testing · miscellaneous

Step 4 — Expert review
  └─ 2 materials science domain experts independently labeled domains
  └─ Label disagreement → consensus reached through discussion
  └─ Answer verification: based on the official IIT Kharagpur answer key

Step 5 — Evaluation protocol
  ┌─ Zero-shot: "Solve the following question. Write the
  │              correct answer inside a list at the end."
  └─ Chain-of-Thought(CoT): "Solve the following question with
                            highly detailed step-by-step
                            explanation. Write the correct
                            answer inside a list at the end."
  └─ Evaluated GPT-3.5 / GPT-4 via the OpenAI API
  └─ Model outputs were saved as text files and answers were
     manually extracted afterward
     (the model does not always follow the specified format)

Step 6 — Release
  └─ github.com/M3RG-IITD/MaScQA
  └─ All 650 questions (no Train/Val/Test split)
```

## Input
- **Question format**: text-based natural language questions (no images or graphs)
- **Number of questions**: 650 (MCQ 285 + MATCH 70 + MCQN 67 + NUM 228)
- **Domains**: 14 materials science sub-areas
- **Language**: English
- **Metadata**: question_id, structure_type, domain_label, correct_answer

## Output (Answer format)
- **MCQ / MATCH / MCQN**: one of the options A/B/C/D (or multiple options)
- **NUM**: a numerical value (integer or floating point with a specified number of digits)
- **Evaluation metric**: answer match rate (% accuracy)
- **Baseline**: with random selection, MCQ 25%, MATCH 25%, MCQN 25%, NUM 0%

## Example Questions (reconstructed from the paper body + Figure 1·4·5·8 captions)

### MCQ — Conceptual (quoted from the paper body)
> One of the cases where GPT-4-CoT exhibits a conceptual error in the paper body:
>
> **Q (Fig. 4(b)).** Relating lattice parameter (a) and atomic diameter (D) in a given crystal structure.
>
> GPT-4-CoT applied the incorrect relation `a = √(8/3) · D` → inconsistent with the correct answer `a = (4/√6) · D`.
>
> *A representative case showing LLM formula-retrieval errors in the Atomic structure area*

### MATCH — Application-domain matching (quoted from the paper body)
> **Q (Fig. 6).** Match materials to their primary application (missile cone heads, semiconductors, refractory uses, etc.).
>
> *Analysis in the paper body (p.18)*: "GPT-3.5-CoT was only able to determine the material properties required for the missile cone heads ... [it] tries to arrive at the correct answer by eliminating the options." → GPT-3.5 relies on an elimination strategy, while GPT-4 reaches the correct answer through conceptual inter-relating.

### MCQN — Numerical + multiple choice (quoted from the paper body)
> **Q (Fig. 7).** A numerical question with four numeric options.
>
> *Paper body*: "The GPT-3.5-CoT solution used the correct concept but made calculation errors leading to a final incorrect answer. However, GPT-4-CoT used the correct concept and did not make calculation mistakes."

### NUM — Direct numerical entry (quoted from the paper body)
> **Q (Fig. 8).** Sample numerical question related to **platinum's crystal structure** (FCC, calculating interplanar distance d).
>
> *Paper body*: "Both models applied the correct concept. However, GPT-3.5-CoT made a calculation mistake in obtaining the interplanar distance 'd'..." → the concept is correct but an arithmetic error makes NUM accuracy the lowest of all categories.

> ※ The original GATE question text can be checked in the official IIT Kharagpur question paper PDFs (each figure caption is in image format, so text cannot be extracted directly from the PDF).

## Key Evaluation Results (Table 1)

| Evaluation Method | MCQ (285) | MATCH (70) | MCQN (67) | NUM (228) | **Overall** |
|---|---|---|---|---|---|
| Baseline (random) | 25 | 25 | 25 | 0 | – |
| GPT-3.5 (zero-shot) | 56.49 | 40.00 | 35.82 | 15.79 | 38.31 |
| GPT-3.5-CoT | 56.84 | 38.57 | 34.33 | 14.04 | 37.38 |
| GPT-4 (zero-shot) | 74.74 | 88.57 | 59.70 | 33.77 | 60.15 |
| **GPT-4-CoT** | **76.84** | **92.86** | 52.24 | **37.28** | **62.00** |
| HoneyComb (GPT-4+MatSciKB+ToolHub, EMNLP 2024) | — | — | — | — | **79.07** |

**Key findings**
- The improvement from GPT-4 → GPT-4-CoT is marginal (+1.85pp) — suggesting that CoT does not always help.
- All models perform worst on the NUM category → numerical calculation is the main bottleneck.
- On MATCH, GPT-4 is **more than 2×** as accurate as GPT-3.5 (88.57% vs 40.00%) → a difference in conceptual inter-relating ability.
- Of the 13 multi-correct MCQ questions, GPT-4 gets only 6 correct and GPT-4-CoT only 7.

**Error analysis (sample of 100 GPT-4-CoT incorrect answers, Table 3)**
| Error Type | Proportion |
|---|---|
| Conceptual error (lack of knowledge) | ~64% |
| Computational error (calculation mistake) | ~36% |
| Grounding error (error in applying concepts) | ~0% (CoT almost eliminates it) |

→ Reinforcing domain knowledge (RAG/SFT) takes priority over improving calculation ability.

**Domain analysis (GPT-4-CoT, Table 2)**
- **Lowest-accuracy areas**: Electrical properties · Mechanical behavior (~60% incorrect)
- Thermodynamics · Atomic structure · Phase transition · Transport phenomena · Magnetic properties: 40%+ incorrect
- **Highest-accuracy areas**: Material testing (0 incorrect) · Material characterization

## Limitations
- **No images or graphs**: only text-based questions are included → multimodal evaluation is not possible (the actual GATE includes some figure-based questions).
- **Indian curriculum bias**: given the nature of GATE questions, they are based on Indian undergraduate textbooks → subtle differences in emphasis relative to US/European curricula are possible.
- **Latest materials not covered**: a shortage of questions on hot topics since the 2010s such as batteries, 2D materials, nanomaterials, MOF, and perovskite solar cells.
- **Language**: English only (multilingual evaluation not possible).
- **No Train/Val/Test split**: all 650 questions are used only as an evaluation set → if a separate training split is needed, users must construct it themselves.
- **Ambiguity in grading numerical calculations**: the floating-point rounding digits differ per question → a tolerance setting is needed for automatic grading.

## Related links
- **Paper**: [Digital Discovery, RSC, 2024 (DOI: 10.1039/D3DD00188A)](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d3dd00188a)
- **arXiv**: [2308.09115](https://arxiv.org/abs/2308.09115)
- **GitHub**: [M3RG-IITD/MaScQA](https://github.com/M3RG-IITD/MaScQA)
- **Official GATE question source**: [gate.iitkgp.ac.in](https://gate.iitkgp.ac.in/old_question_papers.html)
- **Follow-up work using this benchmark**:
  - HoneyComb (EMNLP Findings 2024) — achieves 79.07% (RAG agent)
  - Adopted as a standard benchmark by subsequent materials science RAG papers
