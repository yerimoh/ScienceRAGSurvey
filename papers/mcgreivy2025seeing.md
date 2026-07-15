---
title: "Seeing the Forest Through the Trees: Knowledge Retrieval for Streamlining Particle Physics Analysis"
bib_key: "mcgreivy2025seeing"
year: 2025
domain: physics
type: method
venue: arXiv preprint (arXiv:2509.06855)
paper_link: https://arxiv.org/abs/2509.06855
---
# Seeing the Forest Through the Trees: Knowledge Retrieval for Streamlining Particle Physics Analysis

> arXiv:2509.06855 | 2025 | method | physics
> McGreivy, Delaney, Beck, Williams — MIT (NSF AI Institute for AI and Fundamental Interactions, LHCb)

## TL;DR
Targeting the LHCb corpus, this work proposes two structured retrieval systems that overcome the chunk fragmentation limitation of standard RAG: **SCITREERAG** (paper LaTeX section tree + recursive attention-weighted embeddings) + **SCIGRAPHRAG** (LLM-constructed Neo4j Knowledge Graph + NL→CYPHER). Validated with **56 evaluation queries** automatically generated from HFLAV, SCITREERAG reduces "poor" ratings from 25% → 10% compared to baseRAG.

## Background
**Three limitations of standard RAG (author classification, Sec. 1)**
1. **Accidental Semantic Similarity** — retrieval of irrelevant chunks that only share keywords
2. **Fragmented Context** — chunk-wise concatenation damages logical relationships
3. **Lack of Global Knowledge** — inability to retrieve relationships and patterns across the corpus

**Why this system was needed**
- LHCb collaboration: thousands of papers, 1,600+ collaborators — need to support non-expert analysis using CERN open data
- LHC publications are scattered across INSPIRE-HEP and others → lack of comprehensive cross-document synthesis
- Lowering the entry barrier for new PhD students

## Construction Methodology

```
═══════════════════════════════════════════
[A] SCITREERAG — Local Knowledge Retrieval
═══════════════════════════════════════════
Step A1 — Tree construction (per article)
  parse sanitized LaTeX source
  abstract = root
  section/subsection = intermediate nodes
  paragraph / figure caption / table / equation = leaf nodes

Step A2 — Recursive LLM summary
  leaf summary = atomic content
  intermediate summary = recursive concat + summarize(children)
  root summary = abstract

Step A3 — Refined dense embedding
  each node summary → paragraph embedding
  recursive attention-weighted refinement:
    multi-level representation of the same information → amplify robust signal
    attenuate word-choice / hallucination artifacts

Step A4 — Retrieval (Greedy tree traversal)
  abstract → section → subsection → leaf
  prioritize topically relevant sections
  group leaf nodes from the same paper and add to context

═══════════════════════════════════════════
[B] SCIGRAPHRAG — Global Knowledge Retrieval
═══════════════════════════════════════════
Step B1 — Per-article KG
  GPT-5 mini builds abstract → high-level KG (observable, decay, period)
  domain normalization: e.g., "Bs → µ+µ−" → "B(s)0 -> mu+ mu-"
  body text → extract systematic uncertainty + analysis methods
  Entity types: yellow (decays) / purple (observables) /
                light blue (uncertainty) / orange (methods)

Step B2 — Canonicalization (cross-document merge)
  TF-IDF(name) + semantic emb(description) → hybrid sim
  agglomerative clustering by type
  LLM-as-judge decides entity merging within clusters
  ex) "tracking efficiency in vertex" vs "in muon" → kept separate

Step B3 — NL → CYPHER conversion
  LLM sees schema + 3 few-shot examples
  generates CYPHER expression (Neo4j)
  semantic similarity search (no exact string)

Step B4 — Query execution + LLM synthesis → NL answer

═══════════════════════════════════════════
[C] Evaluation — HFLAV Eval Q&A (Sec. A.2)
═══════════════════════════════════════════
HFLAV report "Averages of b-hadron, c-hadron,
  τ-lepton properties as of 2023"
  ↳ not included in LHCb corpus → genuine retrieval evaluation
  ↳ 7 chapters × 8 query = 56 queries
GPT-5 mini generates a rubric for each query:
  Essential / Expert-level / Factual benchmarks 3-tier
grade {poor / satisfactory / good} via LLM-as-judge
Human expert validates a sub-sample
```

## Input
- LHCb corpus (using sanitized LaTeX source)
- User natural-language queries (b-hadron lifetime, Vcb, CP violation phase, etc.)
- HFLAV reference values (quantitative benchmark)

## Output
- SCITREERAG: chunks from tree traversal + LLM response
- SCIGRAPHRAG: KG subgraph + CYPHER result + NL synthesis

## Example queries (direct quotes from paper body + Appendix A.2·B.2)

### 📘 HFLAV Eval Example Query ① — b-hadron lifetime
> "What are the most precise measurements of b-hadron lifetimes performed by LHCb, and how do the systematic uncertainties in these measurements compare across different decay channels and methodologies?"

### 📘 HFLAV Eval Example Query ② — |Vcb|
> "What is LHCb's most precise measurement of |Vcb| from exclusive semileptonic B decays, and how does it compare to the inclusive determination? What are the dominant sources of theoretical and experimental uncertainty in the exclusive approach?"

### 📘 HFLAV Eval Example Query ③ — Polarization fractions
> "Which B0 decay mode has been most useful for studying polarization fractions in vector-vector final states, and what are the LHCb results?"

### 📘 SCIGRAPHRAG Example — Query γ (Sec. 4)
> **Q**: "What decay channel should I use to measure the CP violating phase γ? What sources of systematic uncertainty will dominate my analysis?"
>
> **SCIGRAPHRAG Response (verbatim)**:
> > "Use a combination of tree-level B → D(∗)h modes plus the time-dependent Bs → D∓s K± channel. Practically this means including B± → DK± and B± → Dπ± (with D → KSππ, KSKK, K±π∓, K±π∓π±π∓, 3- and 4-body final states), B± → D∗K±, B0 → DK∗0/± and B0 → DK+π− (GLW/ADS/GGSZ-type approaches) ... combining these channels is the route taken in recent LHCb determinations and gives the best precision on γ [2010.08483, 2410.21115, 2209.03692, 2412.14074]. The dominant systematic uncertainties will be external hadronic inputs and model/theory assumptions: uncertainties on D-decay hadronic parameters (rXD, δXD, κXD, CP-even fractions F+ for multi-body modes) ..."
>
> **LLM-as-judge result**: SCIGRAPHRAG = "good", SCITREERAG/RAG = "satisfactory" (authors agree)

### 📘 SCIGRAPHRAG Example — Query ∆ms (Sec. B.2)
> **Q**: "Which decay provides the most precise measurement of the B0s eigenstate oscillation frequency, ∆ms? What are the dominant systematic uncertainties for that measurement?"
>
> **Response excerpt**: *"the recent LHCb result quoted in the context gives ∆ms = 17.7683 ± 0.0051 (stat) ± 0.0032 (syst) ps−1 from B0s → D−s π+ [2104.04421]; earlier LHCb measurements on the same channels report compatible values with larger uncertainties (e.g. 17.768 ± 0.023 ± 0.006 [1304.4741])"*

## Key evaluation results (Sec. 4, Sec. B.1)

**LLM-as-judge Quality Grades (HFLAV 56-Q, averaged over context 8k/16k/32k)**

| System | "poor" ratio | "satisfactory + good" ratio |
|---|---|---|
| BaseRAG (standard) | 25% | ~42% |
| SCITREERAG (no diffusion) | 20% | >50% |
| **SCITREERAG + diffusion** | **10%** | **>50%** |

> Author conclusion: "SCITREERAG demonstrates modest but consistent improvements over BaseRAG ... receiving 'poor' ratings only 10% of the time compared to 25% for RAG."

**KG Canonicalization validation (Fig. 1)**
- Query γ: 17 "CKM Angle gamma" entities correctly merged into a single entity
- Query ∆ms: 4 duplicate "Delta m_s" entities found → case of **incomplete entity resolution** (noted by authors)

## Limitations
- **Absence of numerical standard benchmarks**: IR metrics such as P@k, MRR are not used (only LLM-as-judge)
- SCIGRAPHRAG is **work in progress** — KG construction and NL→Cypher reliability are insufficient
- Schema is narrowly defined (particle physics analysis) → generalization not validated
- Human expert validation covers only a sub-sample, full evaluation not performed
- Limited to the LHCb corpus — transferability to ATLAS/CMS/ALICE not validated
- KG construction is a one-time upfront cost per article, but GPT-5 mini API costs accumulate

## Related links
- **Paper**: [arXiv:2509.06855](https://arxiv.org/abs/2509.06855)
- **Author affiliation**: MIT (NSF AI Institute for AI and Fundamental Interactions)
- **LLM used**: GPT-5 mini (KG construction), embedding model (DPR / SciBERT family, not specified in the text)
- **Evaluation reference**: HFLAV 2023 report (Banerjee et al. 2024) — not included in the LHCb corpus
- **KG tools**: Neo4j (CYPHER query language)
- **Code release**: to be released in the workshop camera-ready version
