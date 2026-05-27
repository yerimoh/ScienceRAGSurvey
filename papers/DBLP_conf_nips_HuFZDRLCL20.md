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

## 한 줄 요약
**15개 large-scale graph dataset의 표준 benchmark** (node/link/graph property prediction × Nature/Society/Information 도메인). 핵심 contribution: **realistic application-specific data splits** (random이 아닌 time / scaffold / species 기반) + **표준 evaluator + public leaderboard**. **ogbl-biokg** subset은 heterogeneous biomedical knowledge graph (93,773 nodes / 5,088,434 edges) 위에서 MRR 기반 link prediction을 평가하는 §o3-weakverifier 관련 task.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문제 인식: 기존 graph ML benchmark의 약점
  ┌──────────────────────────────────────────────┐
  │ - CORA/CITESEER/PUBMED: 2,700~20K nodes      │
  │ - TU collection: 200~5K graphs               │
  │ - FB15K/WN18: 15K~40K entities               │
  │   → real graph (1M+ nodes)에 비해 작음        │
  │ - Random split은 비현실적 (overly optimistic) │
  │ - 일관된 protocol 부재                       │
  └──────────────────────────────────────────────┘

Step 2 — 15 dataset 구성 (3 task category × 5 domain)
  ┌──────────────┬──────────────────────────────┐
  │ Node (ogbn-) │ products / proteins / arxiv  │
  │              │ papers100M / mag             │
  ├──────────────┼──────────────────────────────┤
  │ Link (ogbl-) │ ppa / collab / ddi / citation│
  │              │ wikikg / biokg               │
  ├──────────────┼──────────────────────────────┤
  │ Graph (ogbg-)│ molhiv / molpcba / ppa / code│
  └──────────────┴──────────────────────────────┘

Step 3 — Realistic splits (논문 핵심 contribution)
  · Time: 학술 그래프 (arxiv, citation, wikikg) →
          past → future
  · Scaffold: 분자 그래프 (molhiv, molpcba) →
              structurally distinct test molecules
  · Species: protein graph (proteins, ppa) →
             species-disjoint train/test
  · Random: biokg (heterogeneous KG)
  · Sales rank: ogbn-products (Amazon)

Step 4 — Dataset-specific evaluator
  · 각 dataset마다 표준 metric class 제공
  · Hits@K (ppa, collab, ddi), MRR (citation, biokg, wikikg)
  · ROC-AUC (proteins, molhiv), AP (molpcba)
  · Accuracy (products, arxiv, papers100M, mag, ppa graph)
  · F1 (code sub-token prediction)

Step 5 — End-to-end pipeline
  · PyTorch + PyG + DGL 호환 data loader
  · OGB Evaluator class (dataset-specific)
  · Public leaderboard (ogb.stanford.edu)
  · Submission via GitHub (코드 필수)
```

---

## 실제 데이터 형식 예시 (논문 §3-5 + Table 1-2)

### 유형 A — OGB-biokg (heterogeneous biomedical KG)

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
> 평가: 각 test (h,r,t)에 대해 head/tail 손상 후 ranking

### 유형 B — OGB Link prediction 6 dataset summary

> | Dataset | Domain | Split | Metric | #Nodes | #Edges |
> |---|---|---|---|---|---|
> | ogbl-ppa | Nature | Throughput 70/20/10 | Hits@100 | 576K | 30M |
> | ogbl-collab | Society | Time 92/4/4 | Hits@50 | 236K | 1.3M |
> | ogbl-ddi | Nature | Protein target 80/10/10 | Hits@20 | 4.3K | 1.3M |
> | ogbl-citation | Society | Time 99/1/1 | MRR | 2.9M | 30.6M |
> | ogbl-wikikg | Information | Time 94/3/3 | MRR | 2.5M | 17M |
> | **ogbl-biokg** | **Information** | **Random 94/3/3** | **MRR** | **94K** | **5M** |

### 유형 C — End-to-end pipeline (논문 Figure 2)

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

### 유형 D — 평가 protocol (Filtered MRR for KG completion)

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

## 평가 framework 요약

| Category | Datasets | Primary metric | Eval protocol |
|---|---|---|---|
| **Node** (ogbn-) | products, proteins, arxiv, papers100M, mag | Accuracy / ROC-AUC | Application-specific split |
| **Link** (ogbl-) | ppa, collab, ddi, citation, wikikg, **biokg** | Hits@K / **MRR** | Filtered ranking |
| **Graph** (ogbg-) | molhiv, molpcba, ppa, code | ROC-AUC / AP / Accuracy / F1 | Scaffold / Species / Project |

→ ogbl-biokg는 §o3-weakverifier의 KG embedding 평가 substrate; 다른 dataset은 graph ML 일반.

---

## 주요 결과 (논문 §3-5 + Table 3)

| 발견 | 의미 |
|---|---|
| 작은 데이터셋 (CORA 등) 위 GNN 성능이 통계적으로 무의미 | 대규모 benchmark 필요 |
| Random split이 application-specific split보다 8.46pp 쉬움 | 비현실적 |
| Scaffold split의 ogbg-molhiv는 ROC-AUC 5.66pp 어려움 | OOD test |
| Mini-batch GNN이 full-batch과 동등 또는 우위 | scalable 가능 |
| OGB datasets 전반에 GNN 일반화 능력 부족 | OOD 일반화 frontier |

→ **결론**: graph ML 발전에 필수 인프라; 모든 후속 graph ML 논문이 OGB leaderboard에서 비교됨.

---

## 한계점
- **Static benchmark**: 5년 경과로 일부 dataset 포화
- **ogbl-biokg는 작은 편**: 다른 KG benchmark (Freebase, Wikidata) 대비
- **Random split이 biokg에서만 사용**: time/structure split도 흥미로움
- **단일 task per dataset**: multi-task / multi-objective 평가 부족
- **PyG/DGL 의존**: 다른 framework는 별도 wrapper 필요
- **Public leaderboard 의존**: dataset/leaderboard 종료 위험 (Stanford 호스팅)

---

## 관련 정보
- **논문 (NeurIPS 2020)**: [proceedings.neurips.cc](https://proceedings.neurips.cc/paper/2020/hash/fb60d411a5c5b72b2e7d3527cfc84fd0-Abstract.html)
- **DBLP**: [conf/nips/HuFZDRLCL20](https://dblp.org/rec/conf/nips/HuFZDRLCL20.html)
- **공식 사이트**: [ogb.stanford.edu](https://ogb.stanford.edu/)
- **GitHub**: [snap-stanford/ogb](https://github.com/snap-stanford/ogb)
- **저자 소속**: Stanford SNAP (Jure Leskovec) + TU Dortmund + Harvard + Microsoft Research
- **이 benchmark의 ogbl-biokg subset 사용 후속 작업**: 생의학 KG embedding 연구 다수
- **관련 benchmark**: [[DBLP:journals/bioinformatics/BreitOAS20]] (OpenBioLink — 같은 도메인, leakage-control 강조), FB15K-237 / WN18RR (general KG)
