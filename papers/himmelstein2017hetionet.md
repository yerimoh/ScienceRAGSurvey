---
title: "Hetionet: Systematic Integration of Biomedical Knowledge for Drug Repurposing"
bib_key: "himmelstein2017hetionet"
year: 2017
domain: medical, bio
type: benchmark
venue: eLife
paper_link: https://doi.org/10.7554/eLife.26726
---
# Hetionet v1.0: 47,031 nodes (11 types) × 2,250,197 relationships (24 types)

> eLife 6:e26726 | 2017 | Benchmark (drug-disease repurposing edge prediction GT) | medical · bio
> Daniel S. Himmelstein, Antoine Lizee, Christine Hessler, Leo Brueggeman, Sabrina L. Chen, Dexter Hadley, Ari Green, Pouya Khankhanian, Sergio E. Baranzini — UCSF / UPenn
> DOI: [10.7554/eLife.26726](https://doi.org/10.7554/eLife.26726)

## TL;DR
A hetnet (heterogeneous network) of **47,031 nodes (11 types) × 2,250,197 relationships (24 edge types)** integrated from 29 public resources. It has become the standard GT for drug repurposing edge prediction, and is a **fully open** study that received realtime feedback from **40 community members**.

---

## Construction Methodology

```
Step 1 — Integrating data sources (29 public resources)
  └─ DrugBank, ChEMBL, SIDER, Bgee, GTEx, MSigDB, GO, DO, MeSH,
     GWAS Catalog, LINCS L1000, STRING, BioGRID, PathBank, etc.

Step 2 — Node typing (11 types)
  ┌──────────────────────┬─────────────────────────┐
  │ Node type            │ Example                  │
  ├──────────────────────┼─────────────────────────┤
  │ Compound             │ 1,552 small molecules    │
  │ Disease              │ 137 complex diseases     │
  │ Gene                 │ proteins/genes           │
  │ Anatomy              │ tissues/organs           │
  │ Pathway              │ biological pathways      │
  │ Biological Process   │ GO BP                    │
  │ Cellular Component   │ GO CC                    │
  │ Molecular Function   │ GO MF                    │
  │ Symptom              │ disease symptoms         │
  │ Pharmacologic Class  │ MeSH                     │
  │ Side Effect          │ ADRs                     │
  └──────────────────────┴─────────────────────────┘

Step 3 — Edge typing (24 metaedges)
  └─ Compound-Disease (treats / palliates)
  └─ Compound-Gene (binds / upregulates / downregulates)
  └─ Disease-Gene (associates / upregulates / downregulates / locates)
  └─ Gene-Gene (interacts / covaries / regulates)
  └─ Anatomy-Gene (expresses / upregulates / downregulates)
  └─ ... 24 types in total

Step 4 — Drug Repurposing model: Project Rephetio
  └─ Metapath-based feature engineering
  └─ Logistic regression on metapath similarities
  └─ DM (Compound-treats-Disease) edge prediction
  └─ New candidates: nicardipine, fluoxetine for Multiple Sclerosis, etc.

Step 5 — Open community development
  └─ GitHub-first manuscript (dhimmel/rephetio-manuscript)
  └─ Realtime feedback from 40 external community members
  └─ "entirely open" research model
```

---

## Direct Quotes from the Original (Himmelstein 2017 eLife §body)

> "Hetionet v1.0 consists of **47,031 nodes of 11 types** and **2,250,197 relationships of 24 types**. Data was integrated from **29 public resources** to connect compounds, diseases, genes, anatomies, etc."

> "The hetnet contains 47,031 nodes of 11 types (Table 1) and 2,250,197 relationships of 24 types (Table 2). The nodes consist of **1,552 small molecule compounds** and **137 complex diseases**."

> "This study was **entirely open** and received realtime feedback from **40 community members**."

---

## Project Rephetio Evaluation Results

| Item | Description |
|---|---|
| Task | Compound-treats-Disease edge prediction |
| Training | known 1,552 × 137 (compound × disease) treatments |
| Features | metapath count + diffusion-based scores |
| AUROC | ~0.97 (validation) |
| Drug discovery cases | nicardipine for MS, fluoxetine reuse, etc. |

---

## Main Uses

| Item | Description |
|---|---|
| Task definition | Drug repurposing edge prediction |
| Granularity | Compound-treats-Disease (DM) edge inference |
| Follow-up work | EdgePrediction, NodeXL community detection |
| KG embedding models | TransE, ComplEx, DistMult on Hetionet |
| Distinctiveness | The repurposing edge-prediction standard, separate from DRKG/PrimeKG |

---

## Limitations
- **2017 v1.0 cutoff**: new drugs/diseases not reflected
- **Open Targets / DrugBank dependency**: some use may be restricted if the original DB licenses change
- **Predicted treatment validation**: edge prediction generates hypotheses; additional wet-lab work is needed
- **Heterogeneity bias**: some edge types have sparse data
- **Unidirectional relationships**: all edges are unweighted (strength not reflected)

---

## Related links
- **Paper (eLife)**: [10.7554/eLife.26726](https://doi.org/10.7554/eLife.26726)
- **Official site**: [het.io](https://het.io) — interactive exploration
- **GitHub**: [hetio/hetionet](https://github.com/hetio/hetionet)
- **Data download**: [github.com/hetio/hetionet/tree/master/hetnet](https://github.com/hetio/hetionet/tree/master/hetnet)
- **Project Rephetio results**: [het.io/repurpose](https://het.io/repurpose)
- **Major work using this benchmark**: DRKG, PrimeKG (structural inspiration), TxGNN, GraIL, and other biomedical KG embedding/inference research
