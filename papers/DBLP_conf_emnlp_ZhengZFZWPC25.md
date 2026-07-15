---
notion_id: 355f2dcd-4912-815c-b521-d607762bcce7
title: Benchmarking Foundation Models with Retrieval-Augmented Generation in Olympic-Level Physics Problem Solving
bib_key: DBLP:conf/emnlp/ZhengZFZWPC25
year: 2025
domain: physics
type: Method
venue: EMNLP (Findings) 2025
paper_link: https://aclanthology.org/2025.findings-emnlp.1196/
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Benchmarking Foundation Models with Retrieval-Augmented Generation in Olympic-Level Physics Problem Solving

> EMNLP Findings | 2025 | Method | physics

## TL;DR
**PhoPile** — the **first multimodal RAG physics benchmark**, built on 3,052 olympiad problems collected from 7 international Physics Olympiads (IPhO, APhO, EuPhO, NBPhO, RMPh, USAPhO, BPhO) (2,662 problems from before 2018 as the retrieval corpus + 390 problems from 2019-2021 as the test set). It comprehensively evaluates 8 LLM/LMM × 7 retriever × 1-3 shot × reflection on/off on genuine olympiad-difficulty problems that combine text and images.

## Background
**Limitations of existing datasets**
- SciQ, ScienceQA, TheoremQA, and others consist of a "small number of low-difficulty, text-only physics problems" (paper §1)
- OlympiadBench raised the difficulty but evaluated in isolation without RAG → the utility of retrieval was not assessed
- Physics answers are diverse — numerical, symbolic, diagrammatic → unlike mathematics, automatic grading is very difficult

**Why it is needed**
- The learning approach where a student solves a new problem by referring to similar past problems = analogous to few-shot retrieval
- Concepts recur across years in the Olympiad → the hypothesis that retrieval of past problems is effective needs to be verified
- Author quote: "competition problems share similar concepts across years, and past problems capture not only the necessary physics knowledge from basic principles, but also problem-solving strategies" (§1)

## Construction Methodology
**Step 1: Data Collection**
- Collected 2009-2021 problems from the official PDFs of 7 competitions
- IPhO (International), APhO (Asian), EuPhO (European), NBPhO (Nordic-Baltic), RMPh (Romanian Master), USAPhO (United States), BPhO (British)
- 2019-2021 → test set (390 problems)
- 2009-2018 → retrieval corpus (2,662 problems)

**Step 2: Standardization (paper §2)**
1. LaTeX conversion: convert formulas and diagrams to standard LaTeX
2. Image placeholder: mark image positions in the form `###img_1###`
3. Hierarchical Question Structure: preserve the main problem + sub-questions hierarchy
4. Token statistics normalization (Table 2)

**Step 3: System Architecture**
```
                  [New Olympiad Question + ###img###]
                                │
                                ▼
              ┌──────────────────────────────────┐
              │   Retrievers (7 types)           │
              │   ─────────────────────────      │
              │   Text-only:                     │
              │     - BM25 (sparse)              │
              │     - Emb-cos (all-MiniLM-L6-v2) │
              │     - Dragon+                    │
              │     - Contriever                 │
              │   Multimodal:                    │
              │     - CLIP                       │
              │     - VisualBERT                 │
              │     - ALIGN                      │
              └────────────┬─────────────────────┘
                           │ Top-k similar (q_i, a_i) pairs
                           ▼
              ┌──────────────────────────────────┐
              │   Generator (8 types)            │
              │   ─────────────────────────      │
              │   Closed: GPT-3.5, GPT-4,        │
              │           GPT-4V, Gemini-Pro,    │
              │           Gemini-Pro-V           │
              │   Open: Llama-3-70B,             │
              │         DeepSeek-Math,           │
              │         Mistral-7B, Phi-3.5,     │
              │         Mathstral-7B (FT-able)   │
              │   - Few-shot prompt with         │
              │     retrieved Q-A pairs          │
              │   - Sub-question auto chain      │
              └────────────┬─────────────────────┘
                           │
                           ▼ Candidate answer
              ┌──────────────────────────────────┐
              │   (Optional) Reflection (GPT-4)  │
              │   ─────────────────────────      │
              │   Answer w/RAG vs Answer w/o RAG │
              │   → select the more accurate     │
              │     answer                       │
              └────────────┬─────────────────────┘
                           │
                           ▼
              ┌──────────────────────────────────┐
              │   GPT-4 Judge                    │
              │   ─────────────────────────      │
              │   Reference answer + Student     │
              │   answer → 0-10 score            │
              │   (full score for correct answer │
              │    / partial score by ratio of   │
              │    intermediate steps)           │
              └──────────────────────────────────┘
```

### Generator Prompt (paper Figure 3, quoted verbatim)
> "Your task is to answer the physics questions. The mathematical formulas are provided in Latex code. There are some related questions and their answers you may find helpful.
> Here are the examples:
> Question: {Retrieved Question 1}
> Reference answer: {Reference Answer to Question 1}
> Question: {Retrieved Question 2}
> Reference answer: {Reference Answer to Question 2}
> The question that you need to solve is: {Question to be answered}
> Respond with the FINAL answer to the question to get a higher score as possible as you can, rather than only give directions or suggestions for solving the problem. Do NOT use the conditions in the example questions to solve the question."

### Reflection Prompt (Figure 4)
> "Your task is to choose the answer with a higher score of the given physics problem.
> Question: {Question to be answered}
> Answer 1: {Candidate answer without RAG}
> Answer 2: {Candidate answer with RAG}
> Please give a reason and output the final answer number in side '##', for example, ##1##."

### Judge Prompt (Figure 5)
> "You are a professional physicist and you will grade answers provided by physics students by reference to standard answers. The full score is 10 points, and the minimum score is 0 points. If the student gives the final answer, full marks will be awarded directly. If the student does not give the final answer or the final answer is incorrect, please score based on the proportion of correct calculation steps given by the student. You only need to output a score number."

## Input/Output
**Input**: Olympiad physics problem (text + LaTeX + optional image) + (optional) k retrieved Q-A pairs

**Output**: step-by-step solution + final answer (numerical / symbolic / diagrammatic)

**Evaluation**: a GPT-4 grader scores 0-10 against the reference answer (Pass Rate = proportion of answers accepted as correct, Average Score = 0-10 average)

## Examples
### Example ① — Charged Ring (paper Figure 1, retrieval pipeline showcase)
> **New Question (test set)**:
> > "Consider a uniformly charged metallic ring of radius R and total charge q. The ring is a hollow toroid of thickness 2a≪R. This thickness can be neglected in parts A, B, C, and E. The xy plane coincides with the plane of the ring, while the z-axis is perpendicular to it, as shown in Figure 1. In parts A and B you might need to use the formula (Taylor expansion): (1 + xε) ≈ 1 + εx + 0.5ε(ε−1)x², when x≪1. Calculate the electrostatic potential Φ(z) along the axis of the ring at a z distance from its center (point A in ###img_1###)."
>
> **Retrievers tested**: BM25, MiniLM+cosine, Dragon+, Contriever (text-only) or CLIP/VisualBERT/ALIGN (multimodal)
> **Generators tested**: 8 models including GPT-4, Gemini-Pro, Llama-3, Mistral

### Example ② — Error Analysis (negative cases classified directly by the authors, §3.3)
> The 3 causes by which retrieval instead degraded performance (paper §3.3):
> 1) "the general retriever was not effectively applied to physics problems, as retriever specific to physics may consider the questions that using the same theorem as the top-k relevant ones, instead of those with highest semantic similarity"
> 2) "The format in retrieved questions misleads the candidate models' answering. The retrieved questions and their reference answer may provide guidance answers instead of directly answering the question. Therefore, the foundation models may refuse to answer the final answer directly"
> 3) "some wrong answers arise from using conditions in the retrieved questions as if they were the known conditions in the current question"

## Key Evaluation Results
**Table 4 — PhoPile-Test (text-only, Pass Rate% / Avg Score)**
| Model | Input | w/o RAG | Emb-cos | BM25 | Dragon+ | Contriever |
|---|---|---|---|---|---|---|
| Llama-3-70B | T | 10.51 (1.34) | 5.4 (1.84) | **19.07** (4.86) | 13.62 (4.83) | 10.28 (4.65) |
| Llama-3-70B + Reflection | T | 10.51 | **19.38** (4.35) | **19.38** (4.35) | 14.51 | 10.80 |
| GPT-3.5 | T | 7.95 (4.12) | 8.72 | 8.23 | 10.00 | 7.69 |
| Gemini-Pro | T | 17.18 (5.30) | 16.15 | 15.90 | 16.41 | **30.51** (5.19) |
| Gemini-Pro + Reflection | T | 17.18 | **21.54** (5.72) | 20.51 | 18.72 | 19.74 |
| GPT-4 | T | 26.41 (6.27) | 24.10 | 25.19 | 25.71 | 25.19 |
| GPT-4 + Reflection | T | 26.41 | 27.92 | 27.69 | **28.46** (6.34) | 26.99 |
| Mathstral-7B-v0.1-FT | T | 6.62 | 27.17 | **29.02** (9.28) | 28.90 | 27.66 |
| Llama-3-8B-FT | T | 5.86 | **28.31** (5.90) | 26.44 | 27.46 | 25.39 |

**Table 5 — PhoPile(V)-Test (multimodal, image+text)**
| Model | w/o RAG | CLIP | VisualBERT | ALIGN |
|---|---|---|---|---|
| Gemini-Pro-V | 12.82 (5.09) | **17.48** | 13.59 | 14.56 |
| Gemini-Pro-V + Reflection | 12.82 | 14.56 | **17.48** (5.28) | 15.53 |
| GPT-4V | 21.79 (6.26) | **30.10** (6.20) | 24.27 | 15.53 |
| GPT-4V + Reflection | 21.79 | 26.41 | 22.33 | 23.30 |

**Table 6 — k-shot effect (Avg Score in parens)**
| Model | k | Emb-cos | BM25 | Dragon+ | Contriever |
|---|---|---|---|---|---|
| GPT-3.5 | 1 | 8.97 | 6.92 | 9.74 | 0.77 |
| GPT-3.5 | 2 | 8.72 | 8.23 | 10.00 | 7.69 |
| GPT-3.5 | 3 | 9.74 | 6.41 | 7.44 | 7.71 |
| GPT-4 | 1 | 26.74 | 22.82 | 26.41 | **28.97** |
| GPT-4 | 2 | 24.10 | 25.19 | 25.71 | 25.19 |
| GPT-4 | 3 | 25.90 | 22.56 | 22.37 | 24.62 |

**Table 3 — GPT-4 Grader reliability (tolerance k)**
| Tolerance k | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Accuracy (%) vs human | 37 | 49 | 73 | 87 |

**Key observations**
- Best performance: GPT-4V + CLIP (multimodal) = **30.10%** ; Gemini-Pro + Contriever (text) = **30.51%**
- The RAG effect varies by model — some (GPT-3.5 + Contriever) drop below the base
- Reflection yields large gains on weaker models (Gemini-Pro, Llama-3-70B)
- k=1 is often better than k=2,3 → "increasing the number of shots is not always beneficial"
- The open-source FT model (Mathstral 29.02) is nearly on par with GPT-4

## Key Contributions
1. **PhoPile** — the first multimodal physics olympiad RAG benchmark, built on 7 competitions
2. **Comprehensive ablation of 8 LLM/LMM × 7 retriever × 3 shot × reflection** — the most extensive physics RAG evaluation
3. **Step-wise + solution-level GPT-4 judge** — a reasoning-step grading framework (87% agreement with humans at tolerance k=3)
4. **Error taxonomy** — classification of 3 causes of RAG failure (semantic mismatch / format misleading / condition leakage)

## Limitations
- Only general retrievers are used → absence of a physics-specific retriever ("highlights the significance of establishing domain-specific retrievers", §3.3)
- Dependence on the GPT-4 judge → the judge does not guarantee physics expertise
- English-problem-centric (multilingual competitions use English translations)
- Insufficient robustness to retrieval noise → conditions leakage occurs frequently

## Related Links
- **Paper link**: [https://aclanthology.org/2025.findings-emnlp.1196/](https://aclanthology.org/2025.findings-emnlp.1196/)
- **arXiv**: [https://arxiv.org/abs/2510.00919](https://arxiv.org/abs/2510.00919)
- **Related benchmarks**: SciQ (Welbl et al., 2017), ScienceQA (Lu et al., 2022), TheoremQA (Chen et al., 2023), OlympiadBench (He et al., 2024)
- **K×O classification**: K3 (systematic knowledge / educational artifacts) × O1 (closed-form QA) — uses past olympiad Q-A pairs as demonstrations
