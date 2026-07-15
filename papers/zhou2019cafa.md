---
title: "CAFA3: Critical Assessment of Function Annotation Challenge"
bib_key: "zhou2019cafa"
year: 2019
domain: bio, medical
type: benchmark
venue: Genome Biology
paper_link: https://doi.org/10.1186/s13059-019-1835-8
---
# CAFA3: Time-delayed Protein-GO Function Prediction Benchmark

> Genome Biology 20:244 | 2019 | Benchmark (protein function annotation canonical) | bio · medical
> Naihui Zhou, Yuxiang Jiang, ... Iddo Friedberg (and ~100 co-authors) — international CAFA consortium
> DOI: [10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8) · PMID 31744546

## TL;DR
An **international challenge benchmark** for the task of predicting protein function (Gene Ontology terms) from sequence/structure. Run over three cycles: CAFA1 (2010) → CAFA2 (2013) → CAFA3 (2017–2019). Using a **time-delayed evaluation** protocol, proteins that had no GO annotation at the challenge start but were experimentally verified during the challenge period are used as the hidden test set.

---

## How it was built (CAFA Challenge Methodology)

```
Step 1 — Challenge timeline (3-year cycle)
  ┌──────────────────────────────────────────────┐
  │ T0: Challenge opens — UniProt-GO annotation  │
  │     snapshot released                        │
  │                                               │
  │ T0 ~ T0+9 months: participant prediction     │
  │     submission deadline                       │
  │     (for each unannotated protein, submit a  │
  │      ranked list of candidate GO terms with  │
  │      probability scores)                     │
  │                                               │
  │ T0+9 ~ T0+30 months: natural experimental    │
  │     validation accumulates                    │
  │     UniProt registers new GO annotations     │
  │                                               │
  │ T0+30 months: Held-out test set finalized    │
  │     proteins that were unannotated at T0 but │
  │     received new experimental annotations    │
  │     during the challenge period               │
  └──────────────────────────────────────────────┘

Step 2 — Evaluation: time-delayed held-out
  └─ only proteins newly annotated after the challenge start are tested
  └─ blocks data leakage at its source (across the full time axis)
  └─ "retrieve-then-rank GO term" task format

Step 3 — Target species + fields
  └─ 18+ target species (human, mouse, yeast, A. thaliana, etc.)
  └─ 3 GO sub-ontologies: BP (Biological Process),
                          MF (Molecular Function),
                          CC (Cellular Component)
  └─ NK (No Knowledge) + LK (Limited Knowledge) categories

Step 4 — Evaluation metric
  └─ Fmax (max F1 on the precision-recall curve)
  └─ Smin (semantic distance, accounts for GO hierarchy)
  └─ ROC-AUC (per-term basis)
  └─ Coverage (how many proteins predictions are provided for)
```

---

## Direct quotes from the source (Zhou 2019 Genome Biol §Title)

> Title: *"The **CAFA challenge reports improved protein function prediction** and new functional annotations for hundreds of genes through experimental screens"*

> "the third Critical Assessment of Function Annotation (CAFA3) ... evaluation of method performance using time-delayed propagation"

> CAFA series: CAFA1 (2010–2011, 18 species), CAFA2 (2013–2014, ~100,000 proteins), CAFA3 (2016–2018, ~92,000 proteins)

---

## Evaluation setup

| Item | CAFA3 (2017–2019) |
|---|---|
| Challenge cycle | 3rd edition |
| Target proteins | ~92,000 (unannotated at challenge start) |
| Held-out test size | ~3,000–10,000 proteins newly annotated during the challenge period |
| GO sub-ontologies | MF (Molecular Function), BP (Biological Process), CC (Cellular Component) |
| Categories | No-Knowledge (NK), Limited-Knowledge (LK) |
| Submission format | Per-protein, per-GO-term confidence score (0–1) |
| Primary metric | Fmax (precision-recall based) |
| Secondary metrics | Smin (semantic distance), ROC-AUC, coverage |

---

## Key evaluation results (paper body)

| Item | Content |
|---|---|
| Participating teams | 50+ international groups |
| Top-performing models | DeepGOPlus, NetGO, GOLabeler, ... (CAFA3) |
| Human protein GO MF Fmax | ~0.6 (top systems) |
| Cross-species generalization | performance drops on species other than human |
| "Improved" keyword | demonstrates consistent performance gains from CAFA1 → CAFA3 |

---

## Main uses

| Item | Content |
|---|---|
| Task | Protein → GO term ranking |
| Retrieval-then-rank | canonical pattern of retrieve homologs → rank candidate GO terms |
| Database verifier | UniProt-GO held-out experimental annotations |
| RAG application | sequence embedding retrieval → GO term proposal |
| Follow-up work | CAFA4 (2020–), CAFA5 (Kaggle 2023) |

---

## Limitations
- **Sparse annotation**: GO terms are only partially annotated even for humans; no full ground truth
- **Bias toward studied proteins**: well-studied proteins are over-represented
- **GO ontology drift**: the ontology itself may be updated during the challenge
- **Long-tail GO terms**: rare functions lack examples
- **3-year cycle**: evaluation results are published long after model development
- **Domain bias**: high proportion of human/model organism, few microbial proteins

---

## Related links
- **Paper (Genome Biol)**: [10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)
- **PubMed**: [PMID 31744546](https://pubmed.ncbi.nlm.nih.gov/31744546/)
- **Official site**: [biofunctionprediction.org](https://www.biofunctionprediction.org/cafa) (CAFA consortium)
- **CAFA3 data**: synapse.org/cafa3
- **Kaggle CAFA5 (2023)**: [kaggle.com/competitions/cafa-5-protein-function-prediction](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction)
- **Major models using this challenge**: DeepGOPlus, NetGO, GOLabeler, Funfams, Argot, INGA, TALE, ProteInfer, etc.
