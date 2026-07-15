---
title: "Open Graph Benchmark: Datasets for Machine Learning on Graphs"
bib_key: "DBLP:conf/nips/HuFZDRLCL20"
year: 2020
domain: bio, general
type: benchmark
venue: NeurIPS 2020
paper_link: https://proceedings.neurips.cc/paper/2020/hash/fb60d411a5c5b72b2e7d3527cfc84fd0-Abstract.html
---
# OGB / OGB-biokg: 15-dataset graph ML benchmark with realistic splits

> NeurIPS 2020 | Benchmark (graph machine learning, multi-domain) | bio · general
> Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, Jure Leskovec — Stanford / TU Dortmund / Harvard / Microsoft Research
> DBLP: [conf/nips/HuFZDRLCL20](https://dblp.org/rec/conf/nips/HuFZDRLCL20.html)

## TL;DR
**A standard benchmark of 15 large-scale graph datasets** (node/link/graph property prediction × Nature/Society/Information domains). Key contribution: **realistic application-specific data splits** (not random, but time / scaffold / species based) + **standard evaluator + public leaderboard**. The **ogbl-biokg** subset is a task related to §o3-weakverifier that evaluates MRR-based link prediction over a heterogeneous biomedical knowledge graph (93,773 nodes / 5,088,434 edges).

---

## How it was built (Construction Methodology)

```
Step 1 — Problem recognition: weaknesses of existing graph ML benchmarks
  ┌──────────────────────────────────────────────┐
  │ - CORA/CITESEER/PUBMED: 2,700~20K nodes      │
  │ - TU collection: 200~5K graphs               │
  │ - FB15K/WN18: 15K~40K entities               │
  │   → small vs. real graphs (1M+ nodes)         │
  │ - Random split is unrealistic (overly optimistic) │
  │ - Lack of a consistent protocol              │
  └──────────────────────────────────────────────┘

Step 2 — 15 dataset composition (3 task categories × 5 domains)
  ┌──────────────┬──────────────────────────────┐
  │ Node (ogbn-) │ products / proteins / arxiv  │
  │              │ papers100M / mag             │
  ├──────────────┼──────────────────────────────┤
  │ Link (ogbl-) │ ppa / collab / ddi / citation│
  │              │ wikikg / biokg               │
  ├──────────────┼──────────────────────────────┤
  │ Graph (ogbg-)│ molhiv / molpcba / ppa / code│
  └──────────────┴──────────────────────────────┘

Step 3 — Realistic splits (the paper's key contribution)
  · Time: academic graphs (arxiv, citation, wikikg) →
          past → future
  · Scaffold: molecular graphs (molhiv, molpcba) →
              structurally distinct test molecules
  · Species: protein graphs (proteins, ppa) →
             species-disjoint train/test
  · Random: biokg (heterogeneous KG)
  · Sales rank: ogbn-products (Amazon)

Step 4 — Dataset-specific evaluator
  · Provides a standard metric class for each dataset
  · Hits@K (ppa, collab, ddi), MRR (citation, biokg, wikikg)
  · ROC-AUC (proteins, molhiv), AP (molpcba)
  · Accuracy (products, arxiv, papers100M, mag, ppa graph)
  · F1 (code sub-token prediction)

Step 5 — End-to-end pipeline
  · PyTorch + PyG + DGL compatible data loader
  · OGB Evaluator class (dataset-specific)
  · Public leaderboard (ogb.stanford.edu)
  · Submission via GitHub (code required)
```

---

## Example of the actual data format (paper §3-5 + Table 1-2)

### Type A — OGB-biokg (heterogeneous biomedical KG)

> **Task**: KG completion (link prediction)
>
> ```
> Scale:         93,773 nodes / 5,088,434 edges
> Node types:    5 (disease, drug, protein, side_effect, function)
> Edge types:    51 relation types
> Hetero:        ✓ (typed nodes + typed edges)
> Split:         random 94/3/3
> Split rate:    train 94% / val 3% / test 3%
> Metric:        Mean Reciprocal Rank (MRR)
> Negative:      filtered evaluation
> ```
>
> Triple example: `(Drug:Aspirin, treats, Disease:Headache)`
> Evaluation: for each test (h,r,t), rank after corrupting head/tail

### Type B — OGB Link prediction 6 dataset summary

> | Dataset | Domain | Split | Metric | #Nodes | #Edges |
> |---|---|---|---|---|---|
> | ogbl-ppa | Nature | Throughput 70/20/10 | Hits@100 | 576K | 30M |
> | ogbl-collab | Society | Time 92/4/4 | Hits@50 | 236K | 1.3M |
> | ogbl-ddi | Nature | Protein target 80/10/10 | Hits@20 | 4.3K | 1.3M |
> | ogbl-citation | Society | Time 99/1/1 | MRR | 2.9M | 30.6M |
> | ogbl-wikikg | Information | Time 94/3/3 | MRR | 2.5M | 17M |
> | **ogbl-biokg** | **Information** | **Random 94/3/3** | **MRR** | **94K** | **5M** |

### Type C — End-to-end pipeline (paper Figure 2)

> ```
> (a) OGB datasets → (b) OGB data loader →
> (c) User ML model → (d) OGB Evaluator →
> (e) Public leaderboard
> ```
>
> Python API:
> ```python
> from ogb.linkproppred import LinkPropPredDataset, Evaluator
> dataset = LinkPropPredDataset(name='ogbl-biokg')
> split = dataset.get_edge_split()
> # split['train'], split['valid'], split['test']
> evaluator = Evaluator(name='ogbl-biokg')
> # result_dict = evaluator.eval(input_dict)  # MRR
> ```

### Type D — Evaluation protocol (Filtered MRR for KG completion)

> ```
> For each test triple (h, r, t):
>   1. Generate 500 corrupted heads + 500 corrupted tails
>   2. Score all (h, r, t') and (h', r, t) with model
>   3. Filter true edges from corruption set
>   4. Compute Mean Reciprocal Rank of true entity
>
> Public leaderboard tracks reproducible submissions
> (code mandatory for submission)
> ```

---

## Evaluation framework summary

| Category | Datasets | Primary metric | Eval protocol |
|---|---|---|---|
| **Node** (ogbn-) | products, proteins, arxiv, papers100M, mag | Accuracy / ROC-AUC | Application-specific split |
| **Link** (ogbl-) | ppa, collab, ddi, citation, wikikg, **biokg** | Hits@K / **MRR** | Filtered ranking |
| **Graph** (ogbg-) | molhiv, molpcba, ppa, code | ROC-AUC / AP / Accuracy / F1 | Scaffold / Species / Project |

→ ogbl-biokg is the KG embedding evaluation substrate for §o3-weakverifier; the other datasets are general graph ML.

---

## Key results (paper §3-5 + Table 3)

| Finding | Meaning |
|---|---|
| GNN performance on small datasets (e.g., CORA) is statistically insignificant | Large-scale benchmark needed |
| Random split is 8.46pp easier than application-specific split | Unrealistic |
| ogbg-molhiv with scaffold split is 5.66pp harder in ROC-AUC | OOD test |
| Mini-batch GNN matches or outperforms full-batch | Scalability feasible |
| GNNs lack generalization across OGB datasets | OOD generalization frontier |

→ **Conclusion**: essential infrastructure for advancing graph ML; every subsequent graph ML paper is compared on the OGB leaderboard.

---

## Limitations
- **Static benchmark**: after 5 years, some datasets are saturated
- **ogbl-biokg is relatively small**: compared to other KG benchmarks (Freebase, Wikidata)
- **Random split used only on biokg**: time/structure splits would also be interesting
- **Single task per dataset**: lacks multi-task / multi-objective evaluation
- **PyG/DGL dependency**: other frameworks require a separate wrapper
- **Public leaderboard dependency**: risk of dataset/leaderboard shutdown (Stanford hosting)

---

## Related links
- **Paper (NeurIPS 2020)**: [proceedings.neurips.cc](https://proceedings.neurips.cc/paper/2020/hash/fb60d411a5c5b72b2e7d3527cfc84fd0-Abstract.html)
- **DBLP**: [conf/nips/HuFZDRLCL20](https://dblp.org/rec/conf/nips/HuFZDRLCL20.html)
- **Official site**: [ogb.stanford.edu](https://ogb.stanford.edu/)
- **GitHub**: [snap-stanford/ogb](https://github.com/snap-stanford/ogb)
- **Author affiliations**: Stanford SNAP (Jure Leskovec) + TU Dortmund + Harvard + Microsoft Research
- **Follow-up work using this benchmark's ogbl-biokg subset**: numerous biomedical KG embedding studies
- **Related benchmarks**: [[DBLP:journals/bioinformatics/BreitOAS20]] (OpenBioLink — same domain, emphasizes leakage-control), FB15K-237 / WN18RR (general KG)
