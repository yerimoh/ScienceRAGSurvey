---
title: "Medical Graph RAG: Evidence-based Medical Large Language Model via Graph Retrieval-Augmented Generation"
bib_key: "DBLP:conf/acl/WuZQCXMJG25"
year: 2025
domain: medical
type: method
venue: ACL 2025
paper_link: https://aclanthology.org/2025.acl-long.1381/
---
# MedGraphRAG: Evidence-based Medical RAG via Triple Graph Construction + U-Retrieval

> ACL 2025 (Long Paper, pp. 28443–28467) | Method | medical
> Junde Wu, Jiayuan Zhu, Yunli Qi, Jingkun Chen, Min Xu, Filippo Menolascina, Yueming Jin, Vicente Grau — Univ. of Oxford / CMU / MBZUAI / Univ. of Edinburgh / NUS
> DBLP: `conf/acl/WuZQCXMJG25`

## TL;DR
An evidence-based medical RAG framework that combines a **3-tier hierarchical graph** structure (user medical documents → medical literature → medical dictionary) with **U-Retrieval** (top-down tag matching + bottom-up graph traversal). It consistently outperforms baselines such as GraphRAG, MedRAG, and NaiveRAG on the **9 MultiMedQA MCQ + 2 fact-verification + DiverseHealth (12 total)** benchmarks.

---

## How It Was Built (Construction Methodology)

```
Step 1 — Triple Graph Construction (3-tier hierarchy)
  ┌───────────────────────────────┐
  │ Tier 1: User documents        │  ← patient records, clinical notes, etc.
  │ Tier 2: Medical literature    │  ← papers, textbooks (MedC-K corpus)
  │ Tier 3: Medical dictionary    │  ← UMLS / Medical Dictionary
  └──────────────┬────────────────┘
                 │  hierarchical link
                 ▼
  Entities are connected into the 3-tier graph as semantic units

Step 2 — Tag-based clustering
  Iteratively cluster similar graphs
  → forms a broad-to-detail multi-layer hierarchical tag structure

Step 3 — U-Retrieval (named after the 'U' shape)
  ▼ Top-down phase: LLM generates query tags → index graphs by tag similarity
  ▲ Bottom-up phase: traverse from the most relevant detailed graph, entity by
                   entity, up to the higher-level broader graphs
  → simultaneously secures retrieval efficiency and breadth of response context

Step 4 — Evidence-based response generation
  Prompt with the retrieved medical terms together with their official definitions
  → "evidence-based responses and official medical term explanation"
```

---

## Evaluation Setup (directly quoted from the paper's §Test Data)

> "Our test set are the test split of **9 multiple-choice biomedical datasets from the MultiMedQA suite**, 2 fact verification datasets about public health, i.e., FakeHealth and PubHealth, and 1 test set we collected, called DiverseHealth."

| Category | Dataset | Notes |
|---|---|---|
| MultiMedQA MCQ (9) | MedQA, MedMCQA, PubMedQA, MMLU-Med (clinical knowledge / medical genetics / anatomy / college medicine / professional medicine / college biology), LiveQA, MedicationQA | Answer-selection accuracy |
| Fact verification (2) | FakeHealth, PubHealth | Fact verification |
| In-house (1) | DiverseHealth | Broad coverage of general medicine |

---

## Key Evaluation Results (excerpted from the paper's Table 2)

| System | Avg. MultiMedQA Acc. (representative 9 datasets) | DiverseHealth Acc. |
|---|---|---|
| GPT-3.5 + NaiveRAG | 53.4 | – |
| GPT-3.5 + GraphRAG | 64.8 | – |
| GPT-3.5 + MedRAG | 68.4 | – |
| **GPT-3.5 + MedGraphRAG** | **74.6** | **+6%p vs MedRAG** |
| GPT-4 + MedGraphRAG | **80.1** | SOTA |

→ Combining the Triple Graph + U-Retrieval yields an average +10%p improvement over plain GraphRAG.

---

## Ablation (incremental impact of the 3 tiers, paper Fig.3)

| Tier added | MCQ Acc. increment |
|---|---|
| User docs only | baseline |
| + Medical literature (Tier 2) | +2% (alone) |
| + Medical dictionary (Tier 3) | +1% (alone) |
| Three tiers accumulated + U-Retrieval | +6~10%p |

Key finding: data accumulation + an appropriate retrieval method must work together to reach full potential.

---

## Limitations
- Limited handling of rare and emerging medical terms outside the vocabulary coverage of UMLS / Medical Dictionary
- High 3-tier graph traversal cost, which may introduce latency in real-time clinical applications
- The scale and composition details of the MedC-K corpus are not sufficiently described in the paper
- Some MultiMedQA datasets may overlap with the LLM's training data

---

## Related Links
- **Paper**: [ACL Anthology 2025.acl-long.1381](https://aclanthology.org/2025.acl-long.1381/)
- **DOI**: [10.18653/v1/2025.acl-long.1381](https://doi.org/10.18653/v1/2025.acl-long.1381)
- **DBLP**: [conf/acl/WuZQCXMJG25](https://dblp.org/rec/conf/acl/WuZQCXMJG25.html)
- **GitHub (presumed author implementation)**: https://github.com/MedicineToken/Medical-Graph-RAG
