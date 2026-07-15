---
title: "Exploring genetic interaction manifolds constructed from rich single-cell phenotypes"
bib_key: "norman2019exploring"
year: 2019
domain: bio
type: dataset
venue: Science 365(6455):786-793
paper_link: https://doi.org/10.1126/science.aax4438
---
# Norman 2019: 287 dual-CRISPRi pair × K562 — canonical GI manifold substrate

> Science 365(6455):786-793 | 2019 | Dataset (dual-CRISPRi Perturb-seq for genetic interaction analysis) | bio
> Thomas M. Norman, Max A. Horlbeck, Joseph M. Replogle, Alex Y. Ge, Albert Xu, Marco Jost, Luke A. Gilbert, Jonathan S. Weissman — UCSF / Whitehead Institute
> DOI: [10.1126/science.aax4438](https://doi.org/10.1126/science.aax4438)

## TL;DR
A **Perturb-seq atlas** measured across **287 dual-CRISPRi (CRISPR interference) gene pairs × K562 erythroleukemia cells**. Each dual perturbation expresses two sgRNAs in the same cell to simultaneously knock down two genes. Based on **rich single-cell transcriptomic phenotypes**, it constructs a **genetic interaction manifold** and directly classifies GI subtypes of gene pairs such as **synergy / suppression / redirection / neomorphism** in phenotype space. It has since become the **standard substrate for all dual-gene perturbation prediction models**, including GEARS / PerturBench / scGPT.

---

## Construction Methodology

```
Step 1 — Motivation: limits of GI measurement
  ┌──────────────────────────────────────────────┐
  │ Traditional GI measurement (epistasis):       │
  │   · single readout (growth rate, death, etc.) │
  │   · only a scalar GI score is produced        │
  │   · same score can hide distinct molecular    │
  │     mechanisms                                │
  │ → need GI based on rich phenotype             │
  │   (transcriptome)                             │
  └──────────────────────────────────────────────┘

Step 2 — Building cell line + perturbation library
  ┌──────────────────────────────────────────────┐
  │ Cell line: K562 (erythroleukemia)            │
  │ CRISPRi machinery: dCas9-KRAB stable line   │
  │ sgRNA library:                                │
  │   · single-gene sgRNA pool                    │
  │   · all pair combinations → dual sgRNA        │
  │     constructs                                │
  │ Pair selection: TF + cell-fate regulator     │
  │   focus (myeloid/erythroid lineage related)  │
  └──────────────────────────────────────────────┘

Step 3 — Perturb-seq experiment scale
  ┌──────────────────────────────────────────────┐
  │ Single-gene perturbations:     ~107–155 genes │
  │ Dual-gene combinations:        ~131–287 pairs │
  │ (reported values vary by analysis stage /     │
  │  filtering)                                    │
  │ Per-perturbation cell count:   ~hundreds       │
  │ Total cells profiled:          ~hundreds of    │
  │                                thousands        │
  │ Readout: 10x Chromium single-cell RNA-seq    │
  └──────────────────────────────────────────────┘

Step 4 — GI manifold analysis
  · compute the mean transcriptomic delta of each
    perturbation
  · visualize perturbation embeddings with UMAP/PCA
  · place single + dual perturbations in the same space
  · compare the position of the dual against the
    linear/nonlinear combination of the two single
    points → classify GI subtypes

Step 5 — GI subtype classification scheme
  ┌──────────────────────────────────────────────┐
  │ NEOMORPHIC: dual differs from either single │
  │ REDUNDANT:  dual ≈ single A ≈ single B      │
  │ SUPPRESSOR: dual ≈ control (B suppresses A) │
  │ EPISTASIS_A: dual ≈ single A (A dominant)   │
  │ POTENTIATION: dual >> single A + single B   │
  │ ADDITIVE: dual ≈ single A + single B (linear)│
  └──────────────────────────────────────────────┘
```

---

## Example of actual data formats (paper §Methods + Supplementary)

### Type A — Single-gene CRISPRi perturbation record

> ```
> Cell:        K562 (CRISPRi-ready, dCas9-KRAB stable)
> sgRNA:       targeting CEBPA promoter (TSS-proximal)
> Knockdown:   transcriptional repression (~80-95% of WT)
> Readout:     scRNA-seq (10x Chromium)
> Cell count:  ~500-2000 cells per perturbation
> Gene exp:    raw UMI count matrix (cells × genes)
> ```

### Type B — Dual-gene combinatorial perturbation

> ```
> Dual sgRNA construct: sgRNA-A (targets CEBPA)
>                     + sgRNA-B (targets CEBPB)
> Co-infection:        single cell gets both sgRNAs
> Verification:        sgRNA capture or barcoding
> Phenotype:           cell expression vector under
>                     simultaneous CEBPA + CEBPB KD
> ```

### Type C — GI manifold input/output

> **Input**:
> ```
> Single A perturbation embedding (e.g., CEBPA)
> Single B perturbation embedding (e.g., CEBPB)
> Dual (A+B) perturbation embedding (observed)
> ```
>
> **Analysis**:
> ```
> Predicted additive: linear sum of single deltas
> Compute: |dual - predicted_additive|
>         → magnitude of nonlinear GI effect
> Direction: projection of dual onto control axis,
>           single A axis, single B axis
>         → classify into 6 GI subtypes
> ```

### Type D — Example downstream ML usage (GEARS convention)

> ```
> Standard split (GEARS, PerturBench):
>   Train:  all 155 single + 30% of 131 dual
>   Test:   remaining 70% of dual perturbations
>   Goal:   predict dual response from singles + KG context
>
> Standard evaluation splits introduced by GEARS:
>   Seen-Seen:    both A and B singles in train
>   Seen-Unseen:  only A single in train
>   Unseen-Unseen: neither in train
> ```

---

## Evaluation framework (used by downstream models)

| Metric | Meaning | Used by |
|---|---|---|
| **MSE on top-20 DEG** | Prediction accuracy on DEGs | GEARS, PerturBench |
| **Pearson correlation** | Correlation of the overall Δexpression | General |
| **Precision@10 (GI subtype)** | Accuracy of the top 10 predicted GI classifications | GEARS GI head |
| **MMD (PCA top-256)** | Distribution match | PerturBench |
| **rank metric** | Ordering across all perturbations | PerturBench (mode-collapse detection) |

→ Norman 2019 by itself has no metric; downstream models evaluate using the metrics above.

---

## Key findings (paper §Results)

| Finding | Meaning |
|---|---|
| GI manifold aligns with cell-fate programs | erythroid / myeloid lineage axes |
| Many suppressor pairs detected | ones that a scalar GI score could not capture |
| Neomorphic pairs (e.g., CEBPA+CEBPB) discovered | emergence of new programs |
| ~70% of dual phenotypes are additive (linear) | non-additive GI is around 30% |
| Rich phenotype enables epistasis classification | overcomes the limits of scalar fitness |

→ **Conclusion**: scRNA-seq-based rich phenotypes triggered a paradigm shift in GI analysis, becoming the standard substrate for subsequent perturbation prediction models.

---

## Limitations
- **K562 cell line only**: does not cover other cell types / primary cells
- **CRISPRi (knockdown) only**: knockout, overexpression, and drug perturbation are separate
- **Pair selection focused on TF + cell-fate regulators**: other pathways not included
- **Single time point**: no time-course information
- **287 pairs << ~400 million possible combinations**: an extremely small fraction of the combinatorial space
- **scRNA-seq dropout**: limited accuracy for low-expression genes

---

## Related links
- **Paper (Science)**: [10.1126/science.aax4438](https://doi.org/10.1126/science.aax4438)
- **Data access**: GEO + GEARS preprocessed version (`gears.PertData.load('norman')`)
- **Author affiliation**: UCSF (Weissman lab) / Whitehead Institute
- **Subsequent work using this dataset**:
  - GEARS [[roohani2024gears]] (102 sg + 131 dg standard split)
  - PerturBench [[DBLP:journals/corr/abs-2408-10609]] (155 sg + 131 dg, combo prediction task)
  - scGPT, scFoundation — use Norman19 as a fine-tuning benchmark
- **Prior work**: Adamson 2016 (UPR), Dixit 2016 (Perturb-seq prototype), Replogle 2022 (genome-scale Perturb-seq)
