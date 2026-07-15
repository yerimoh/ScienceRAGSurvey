---
notion_id: 355f2dcd-4912-81a6-96a1-fb28e9797ce2
title: "SQuAI: Scientific Question-Answering with Multi-Agent Retrieval-Augmented Generation"
bib_key: DBLP:conf/cikm/BesrourHS025
year: 2025
domain: bio, chem, physics
type: benchmark
venue: CIKM 2025
paper_link: https://doi.org/10.1145/3746252.3761471
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# SQuAI: 4-Agent Multi-Agent RAG + Q-A-E 1,000-question Benchmark over unarXive

> CIKM 2025 | Method + Benchmark | computer science · physics · biology · chemistry · mathematics
> Ines Besrour, Jingbo He, Tobias Schreieder, Michael Färber — TU Dresden (faerber-lab)
> DBLP: `conf/cikm/BesrourHS025` · DOI: 10.1145/3746252.3761471

## TL;DR
A **Q-A-E (Question-Answer-Evidence) triplet 1,000-question** benchmark proposed together with SQuAI, a **4-agent multi-agent RAG system** operating over the unarXive 2024 arXiv full-text corpus. It solves complex questions via **sub-question decomposition**, performing staged retrieval + synthesis, and improves faithfulness by up to **12%p** compared to standard RAG.

---

## Construction Methodology

```
Step 1 — Data source: unarXive 2024
  └─ arXiv full text (1991-2024, about 2.3 million papers)
  └─ Fields: CS, mathematics, physics, biology, chemistry, and all scientific fields

Step 2 — Q-A-E triplet synthesis (DeepEval + LLaMA 3.3 70B Instruct)
  ┌──────────────────────────────────────────────────────────┐
  │ For each question:                                        │
  │   Q (Question)     ← synthesized with LLaMA 3.3 70B       │
  │   A (Answer)       ← long-form with inline citations [1][2]│
  │   E (Evidence)     ← original-paper citations grounding Q  │
  └──────────────────────────────────────────────────────────┘

Step 3 — Two subsets
  ┌─────────────────────────┬────────┬──────────────────────┐
  │ Subset                  │ #Qs    │ Characteristics       │
  ├─────────────────────────┼────────┼──────────────────────┤
  │ unarXive Simple         │   500  │ non-expert, broad     │
  │ unarXive Expert         │   500  │ expert, body evidence │
  ├─────────────────────────┼────────┼──────────────────────┤
  │ Total                   │ 1,000  │                      │
  └─────────────────────────┴────────┴──────────────────────┘

Step 4 — Evaluation protocol
  · Avoids direct comparison against the synthetic reference answer
  · Instead evaluates the retrieved evidence ↔ generated answer relationship
  · Metrics: Answer Relevance / Contextual Relevance / Faithfulness
    (DeepEval framework, each 0–1)
```

---

## SQuAI System: 4-Agent Architecture (direct quotes from paper/GitHub)

```
[User complex question]
       │
       ▼
┌──────────────────────────────────────┐
│ Agent 1 — Decomposer                 │ ← key differentiator
│   "Decomposes complex user queries   │
│    into simpler, semantically        │
│    distinct sub-questions"           │
└──────────┬───────────────────────────┘
           │ sub-questions
           ▼
┌──────────────────────────────────────┐
│ Agent 2 — Generator                  │
│   retrieve for each sub-question →    │
│   generate Q–A–E triplets            │
└──────────┬───────────────────────────┘
           │ many candidate Q-A-E
           ▼
┌──────────────────────────────────────┐
│ Agent 3 — Judge                      │
│   "Evaluates the relevance and       │
│    quality of each Q-A-E triplet     │
│    using a learned scoring mechanism"│
└──────────┬───────────────────────────┘
           │ filtered Q-A-E
           ▼
┌──────────────────────────────────────┐
│ Agent 4 — Answer Generator           │
│   "Synthesizes a final, coherent     │
│    answer from filtered Q-A-E        │
│    triplets" with in-line citations  │
└──────────┬───────────────────────────┘
           ▼
   [Final long-form answer + [1][2]... citations]
```

→ A representative case of Aggregative Synthesis's **"sub-question decomposition"** mechanism.

---

## Example Q-A-E triplet (excerpt from paper/GitHub)

> **Q**: "What is quantum computing and how is it used in cryptography?"
>
> **A**: "Quantum computing uses qubits to perform computations based on quantum mechanics [1]. It has potential applications in cryptography, particularly for breaking classical encryption schemes [2]."
>
> **E**:
> - `[1]` → specific citation context of the original paper (a quantum-computing introductory paper within unarXive)
> - `[2]` → original-paper context related to Shor's algorithm / post-quantum cryptography

→ Each citation `[i]` maps 1:1 to the original `cited paragraph`, enabling faithfulness evaluation.

---

## Key evaluation results (quoted from paper body)

### unarXive Simple/Expert (combined score, 0–1)
| Approach | unarXive Simple | unarXive Expert |
|---|---|---|
| Standard RAG (baseline) | 0.759 | 0.796 |
| SQuAI (Abstract retrieval) | 0.828 | 0.812 |
| **SQuAI (Full-Text retrieval)** | **0.847** | **0.864** |

### Faithfulness improvement (quoted from GitHub README)
> "SQuAI improves combined scores by up to **12%** in faithfulness compared to a standard RAG baseline."

Key findings:
- **Full-text retrieval > Abstract retrieval** (larger gap on the Expert subset: +5.2%p)
- **Sub-question decomposition** consistently improves over the single-query baseline on complex questions
- The Judge agent's quality filtering contributes to suppressing hallucination

---

## Evaluation metrics detail (DeepEval)

| Metric | Definition | Measured on |
|---|---|---|
| **Answer Relevance** | Semantic match between question ↔ generated answer | Q → A |
| **Contextual Relevance** | Degree to which the provided evidence is effectively integrated into the answer | E → A |
| **Faithfulness** | Whether the answer is supported by the evidence (no unsupported claims) | A ↔ E |

All three metrics range 0–1, using an LLM-as-judge approach.

---

## Limitations
- **Synthetic questions**: generated with LLaMA 3.3 70B → does not fully reflect the complex intent/expression diversity of real human researchers
- **Synthetic reference answer**: since the gold answer is LLM-generated, direct comparison is avoided → evaluation is limited to the evidence-answer relationship
- **Additional evaluation sets such as LitSearch are also used**: employed in evaluation beyond this 1,000 Q-A-E benchmark
- **CIKM 2025 short/full paper**: no arXiv preprint confirmed; only the ACM DL published version is an official source

---

## Related links
- **Paper (ACM DL)**: [doi.org/10.1145/3746252.3761471](https://doi.org/10.1145/3746252.3761471)
- **GitHub**: [github.com/faerber-lab/SQuAI](https://github.com/faerber-lab/SQuAI)
- **Dataset (HuggingFace)**: [ines-besrour/unarxive_2024](https://huggingface.co/datasets/ines-besrour/unarxive_2024)
- **DBLP**: [conf/cikm/BesrourHS025](https://dblp.org/rec/conf/cikm/BesrourHS025.html)
- **Author affiliation**: TU Dresden (faerber-lab)
- **Follow-up work using this benchmark**: SQuAI itself (CIKM 2025)
