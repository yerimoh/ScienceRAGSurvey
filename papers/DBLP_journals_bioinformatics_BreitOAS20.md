---
title: "OpenBioLink: a benchmarking framework for large-scale biomedical link prediction"
bib_key: "DBLP:journals/bioinformatics/BreitOAS20"
year: 2020
domain: bio, medical
type: benchmark
venue: Bioinformatics 36(13):4097-4098
paper_link: https://doi.org/10.1093/bioinformatics/btaa274
---
# OpenBioLink: 7-node × 30-edge biomedical KG benchmark with leakage-controlled splits

> Bioinformatics 36(13):4097-4098 | 2020 | Benchmark (biomedical knowledge graph link prediction) | bio · medical
> Anna Breit, Simon Ott, Asan Agibetov, Matthias Samwald — Medical University of Vienna
> DOI: [10.1093/bioinformatics/btaa274](https://doi.org/10.1093/bioinformatics/btaa274) · DBLP: `journals/bioinformatics/BreitOAS20`

## TL;DR
A **standard benchmark framework** for **biomedical knowledge graph (KG) link prediction**. **7 node types × 30 edge types**, a 4-tier quality cutoff (high/medium/low/all), a **leakage-controlled train-test split** (removing symmetric reverse edges / inverse relations / super-relations), and **typed negative sampling** to tune task difficulty. Allows comparison across various embedding models through the PyKEEN interface. Provides standard metrics: **Hits@K / MRR / ROC-AUC / PR-AUC**.

---

## Construction Methodology

```
Step 1 — Problem recognition: weaknesses of existing link prediction benchmarks
  ┌──────────────────────────────────────────────┐
  │ FB15K (Freebase), WN18 (WordNet), UMLS:      │
  │  · train-test leakage (reverse edges, etc.)   │
  │  · single domain / hierarchical taxonomy     │
  │  · biomedical-specific heterogeneity unmodeled│
  │ → biomedical graphs need a 7+ node × 30+      │
  │   relation typed structure                    │
  └──────────────────────────────────────────────┘

Step 2 — Graph creation module
  ┌──────────────────────────────────────────────┐
  │ Source databases (examples):                  │
  │  · UniProt, DrugBank, KEGG, Reactome,        │
  │    DisGeNET, OMIM, STITCH, GO, etc.           │
  │ Output: 7 node types × 30 edge types graph  │
  │   - Gene / Protein / Drug / Disease /        │
  │     Anatomy / Phenotype / GO term            │
  │   - drug-target, drug-disease, gene-disease, │
  │     gene-pathway, etc.                       │
  └──────────────────────────────────────────────┘

Step 3 — Quality cutoff (4-tier)
  · all      : includes all confidence levels (noisy)
  · low      : low confidence filter
  · medium   : medium confidence filter
  · high     : high confidence only (smallest, cleanest)
  → user selects task difficulty

Step 4 — Train-test split module (core contribution)
  ┌──────────────────────────────────────────────┐
  │ Robustness guarantees:                        │
  │  · Test entities must appear in train        │
  │  · Remove reverse edges of symmetric          │
  │    relations (e.g., gene-gene interaction)   │
  │  · Remove inverse relations                  │
  │    (e.g., drug-target vs target-drug)        │
  │  · Remove super-relations (subsumption)      │
  │ Split type: random or time-slice            │
  └──────────────────────────────────────────────┘

Step 5 — Negative sampling
  · True negatives from source DBs (e.g., over- vs
    under-expression in gene-anatomy)
  · Typed negative sampling for relations without
    explicit negatives

Step 6 — Training + Evaluation module
  · Supports external libraries (PyKEEN interface)
  · Metrics: Hits@K, MRR, ROC-AUC, PR-AUC
  · Provides baseline results (TransE, ComplEx, RotatE, etc.)
```

---

## Example of Actual Data Format (paper §2 + Figure 1)

### Type A — Triple format (head, relation, tail)

> ```
> (Drug:Aspirin, drug_treats_disease, Disease:Headache)
> (Gene:TP53, gene_associated_disease, Disease:LiFraumeni)
> (Protein:P53, protein_in_pathway, Pathway:Apoptosis)
> (Gene:BRCA1, gene_expressed_in_anatomy, Anatomy:Breast)
> ```
>
> **Node types** (7 total): Gene, Protein, Drug, Disease, Anatomy, Phenotype, GO term

### Type B — Quality-filtered subset

> ```
> High-quality subset:
>   · minimized noise (high-confidence edges only)
>   · Smaller graph, faster training
> All subset:
>   · full set (most challenging, noisiest)
>   · Larger graph, realistic
> User task: 'OpenBioLink_HQ' vs 'OpenBioLink_All'
> ```

### Type C — Leakage-controlled split protocol

> ```
> ┌──────────────────────────────────────────────┐
> │ For relation R between A and B:               │
> │                                              │
> │ If R is symmetric (e.g., gene-gene int):     │
> │   - Test triple (A, R, B) present →           │
> │     remove (B, R, A) from train               │
> │                                              │
> │ If R has inverse R⁻¹:                         │
> │   - Test (A, R, B) present →                  │
> │     remove (B, R⁻¹, A) from train            │
> │                                              │
> │ If R has super-relation R_super:              │
> │   - Test (A, R, B) present →                  │
> │     remove (A, R_super, B) from train         │
> └──────────────────────────────────────────────┘
> → remove "trivially inferred" edges
> ```

### Type D — Evaluation metric protocol

> ```
> For each test triple (h, r, t):
>   1. Generate corruptions: (h, r, ?) and (?, r, t)
>   2. Score all candidates with model
>   3. Filter known true edges from corruption set
>   4. Compute rank of true (t / h)
>
> Metrics:
>   Hits@K (K=1,3,10) — fraction with rank ≤ K
>   MRR — Mean Reciprocal Rank
>   ROC-AUC — overall edge ranking
>   PR-AUC — precision-recall area
> ```

---

## Evaluation Framework Summary

| Dimension | Options |
|---|---|
| **Quality cutoff** | high / medium / low / all |
| **Split type** | random / time-slice |
| **Direction** | directed / undirected |
| **Source filter** | exclude specific source DBs |
| **Edge type filter** | exclude specific relation types |
| **Negatives** | from-source / typed-random |
| **Metrics** | Hits@K / MRR / ROC-AUC / PR-AUC |
| **Models** | PyKEEN library compatible (TransE, ComplEx, RotatE, etc.) |

---

## Main Uses (paper + follow-up)

| Item | Content |
|---|---|
| Standard biomedical KG benchmark | Biomedical counterpart to FB15K-237 / WN18RR |
| Leakage control | fair comparison for KG embedding evaluation |
| PyKEEN integration | fast comparison across various embedding models |
| Bioinformatics application note | short (~2 page) format, emphasizes code/data |
| Follow-up work | substrate used by OGB-biokg (Hu 2020 NeurIPS), CLADD/MedGraphRAG |

---

## Limitations
- **Static dataset**: leaderboard must be recomputed when data is updated
- **Source DB dependence**: license / coverage constraints from UniProt/DrugBank, etc.
- **Arbitrariness of confidence cutoff**: 4-tier classification criteria are source-specific
- **2020 cutoff**: latest DrugBank / DisGeNET updates not reflected
- **English-only / public DBs only**: closed sources (UpToDate, etc.) not covered
- **Edge type sparsity**: some types have few samples
- **Limited expressiveness**: simple (h,r,t) structure → no temporal/conditional information

---

## Related links
- **Paper (Bioinformatics)**: [10.1093/bioinformatics/btaa274](https://doi.org/10.1093/bioinformatics/btaa274)
- **DBLP**: [journals/bioinformatics/BreitOAS20](https://dblp.org/rec/journals/bioinformatics/BreitOAS20.html)
- **GitHub**: [OpenBioLink/OpenBioLink](https://github.com/OpenBioLink/OpenBioLink)
- **Author affiliation**: Medical University of Vienna — Section for AI and Decision Support
- **Model family evaluated by this benchmark**: TransE, ComplEx, RotatE, DistMult, R-GCN, etc. (PyKEEN-compatible)
- **Follow-up work using this benchmark**: OGB-biokg [[DBLP:conf/nips/HuFZDRLCL20]], many biomedical KG embedding papers
- **Related benchmarks**: FB15K-237, WN18RR (general), UMLS (KGE standard), OGB-biokg (heterogeneous)
