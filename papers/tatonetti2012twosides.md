---
title: "TWOSIDES & OFFSIDES: Data-driven Prediction of Drug Effects and Interactions"
bib_key: "tatonetti2012twosides"
year: 2012
domain: medical, bio
type: benchmark
venue: Science Translational Medicine
paper_link: https://doi.org/10.1126/scitranslmed.3003377
---
# TWOSIDES & OFFSIDES: Data-driven Prediction of Drug Effects and Interactions

> Science Translational Medicine 4(125):125ra31 | 2012 | Benchmark (DDI side-effect canonical GT) | medical · bio
> Nicholas P. Tatonetti, Patrick P. Ye, Roxana Daneshjou, Russ B. Altman — Stanford University
> DOI: [10.1126/scitranslmed.3003377](https://doi.org/10.1126/scitranslmed.3003377) · PMID 22422992

## TL;DR
A statistical approach that corrects for unmeasured confounding factors in the FDA's spontaneous adverse event reporting system (FAERS) is used to build two resources: **OFFSIDES** (a single-drug side-effect DB) and **TWOSIDES** (a drug-pair side-effect DB). It has become the canonical ground truth for evaluating DDI side-effect prediction models.

---

## How It Was Built (Construction Methodology)

```
Step 1 — Data source: FAERS (FDA Adverse Event Reporting System)
  └─ Raw data of adverse event reports spontaneously reported to the FDA (millions of records)

Step 2 — Correction for unmeasured confounding (authors' core contribution)
  └─ Developed an adaptive correction methodology
  └─ Corrects for patient demographics, comorbidities, and drug exposure patterns
  └─ Removes false-positive side-effect signals

Step 3 — Building two resources
  ┌──────────────┬─────────────────────────────────┐
  │ OFFSIDES     │ Single-drug side-effect database │
  │              │ Additional side effects beyond   │
  │              │ the FDA on-label ones            │
  ├──────────────┼─────────────────────────────────┤
  │ TWOSIDES     │ Drug pair × side-effect labels   │
  │              │ DDI side-effect type prediction  │
  │              │ canonical GT (whereas DrugBank   │
  │              │ has only "existence", this       │
  │              │ provides type labels too)        │
  └──────────────┴─────────────────────────────────┘

Step 4 — External validation
  └─ Corroborated 47 drug class interactions with independent EMR data
  └─ Key finding: SSRI + thiazide → significant increase in QT prolongation
```

---

## Direct Quotes from the Original (Tatonetti 2012 STM, PMC3382018 body verbatim)

> "We developed an adaptive approach to correct for unmeasured confounding factors in spontaneous reporting databases and created two resources: **Offsides (a database of drug effects) and Twosides (a database of drug-drug interaction side effects)**."

> Data source: "**1,851,171 adverse event reports** in the AERS from the FDA's Web site from the first quarter of **2004 to the first quarter of 2009**"

> Propensity score matching (PSM): "**Each exposed patient (that is, report) is matched to a nonexposed patient with a similar probability** according to the PSM model, thereby mitigating the effects of confounders" + "we used PSM to model the probability that a given report lists [that drug] as a concomitant medication" using "the top 200 covariates (sorted by their Spearman correlation coefficient, ρ)"

> **OFFSIDES dataset**: "**438,801 off-label side effects** for **1,332 drugs** and **10,097 adverse events**"

> **TWOSIDES dataset**: "**868,221 significant associations** between **59,220 pairs of drugs** and **1,301 adverse events**"

> EMR validation: "We found additional evidence of drug effects for **47 of 395 interactions** when looking for short-term (≤36 days) changes in laboratory markers after the start of treatment"

> SSRI + thiazide QT case: "patients receiving combined thiazides and SSRIs showed **1.5 (95% CI, 1.2 to 1.9) times as likely** to record a prolonged QT interval compared to thiazide-only users"

---

## Dataset Statistics (paper body verbatim)

| Item | Value |
|---|---|
| AERS raw reports | 1,851,171 (2004 Q1 ~ 2009 Q1) |
| **OFFSIDES side-effect label count** | **438,801** |
| OFFSIDES number of drugs | 1,332 |
| OFFSIDES adverse event types | 10,097 |
| **TWOSIDES number of drug pairs** | **59,220** |
| TWOSIDES significant associations | 868,221 |
| TWOSIDES adverse event types | 1,301 |
| EMR validation rate | 47/395 (≈12%) |

## Primary Uses

| Item | Description |
|---|---|
| Database-verified DDI prediction GT | Standard for DDI side-effect type labels |
| Label granularity | Finer than DrugBank ("DDI exists or not") (specific ADR type) |
| Citing follow-up work | Decagon (Zitnik 2018), MUFFIN, DDI-PULearn, and many other DDI model evaluations |
| Integration location | Core data of the TDC `multi_pred.DDI` task |

---

## Limitations
- Reliance on FAERS spontaneous reporting → sample bias (under-reporting / over-reporting)
- Temporal cutoff: data through 2012, new drugs not reflected
- Causation ≠ correlation: spurious signals possible even after confounding correction
- Side-effect type standardization: reliance on MedDRA terminology
- Applies only to drug pairs (3+ concurrent drugs not supported)

---

## Related Links
- **Paper (DOI)**: [10.1126/scitranslmed.3003377](https://doi.org/10.1126/scitranslmed.3003377)
- **PubMed**: [PMID 22422992](https://pubmed.ncbi.nlm.nih.gov/22422992/)
- **Data download**: [tatonettilab.org/offsides](https://tatonettilab.org/offsides) (current) · originally Stanford-hosted
- **Follow-up work using this data**: TDC `multi_pred.DDI`, Decagon (Zitnik et al. 2018 Bioinformatics), MR-GNN, and other standard GTs for DDI side-effect prediction
