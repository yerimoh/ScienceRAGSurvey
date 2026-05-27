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

## 한 줄 요약
**Biomedical knowledge graph (KG) link prediction**을 위한 **표준 benchmark framework**. **7 node types × 30 edge types**, 4-tier quality cutoff (high/medium/low/all), **leakage-controlled train-test split** (symmetric reverse edge / inverse relation / super-relation 제거), **typed negative sampling** 으로 task난이도 조절. PyKEEN 인터페이스로 다양한 embedding 모델 비교 가능. **Hits@K / MRR / ROC-AUC / PR-AUC** 표준 metric 제공.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문제 인식: 기존 link prediction benchmark의 약점
  ┌──────────────────────────────────────────────┐
  │ FB15K (Freebase), WN18 (WordNet), UMLS:      │
  │  · train-test leakage (역방향 edge 등)        │
  │  · 단일 도메인 / hierarchical taxonomy       │
  │  · 생의학 특유 heterogeneity 미반영          │
  │ → 생의학 graph는 7+ node × 30+ relation       │
  │   typed structure 필요                       │
  └──────────────────────────────────────────────┘

Step 2 — Graph creation module
  ┌──────────────────────────────────────────────┐
  │ Source databases (예시):                      │
  │  · UniProt, DrugBank, KEGG, Reactome,        │
  │    DisGeNET, OMIM, STITCH, GO 등              │
  │ Output: 7 node types × 30 edge types graph  │
  │   - Gene / Protein / Drug / Disease /        │
  │     Anatomy / Phenotype / GO term            │
  │   - drug-target, drug-disease, gene-disease, │
  │     gene-pathway, etc.                       │
  └──────────────────────────────────────────────┘

Step 3 — Quality cutoff (4-tier)
  · all      : 모든 confidence 포함 (noisy)
  · low      : low confidence filter
  · medium   : medium confidence filter
  · high     : high confidence only (smallest, cleanest)
  → 사용자가 task 난이도 선택

Step 4 — Train-test split module (핵심 contribution)
  ┌──────────────────────────────────────────────┐
  │ Robustness 보장:                              │
  │  · Test entities must appear in train        │
  │  · Reverse edges of symmetric relations     │
  │    제거 (e.g., gene-gene interaction)        │
  │  · Inverse relation 제거                     │
  │    (e.g., drug-target vs target-drug)        │
  │  · Super-relation 제거 (subsumption)         │
  │ Split type: random 또는 time-slice          │
  └──────────────────────────────────────────────┘

Step 5 — Negative sampling
  · True negatives from source DBs (e.g., over- vs
    under-expression in gene-anatomy)
  · Typed negative sampling for relations without
    explicit negatives

Step 6 — Training + Evaluation module
  · External libraries 지원 (PyKEEN 인터페이스)
  · Metrics: Hits@K, MRR, ROC-AUC, PR-AUC
  · Baseline 결과 제공 (TransE, ComplEx, RotatE 등)
```

---

## 실제 데이터 형식 예시 (논문 §2 + Figure 1)

### 유형 A — Triple format (head, relation, tail)

> ```
> (Drug:Aspirin, drug_treats_disease, Disease:Headache)
> (Gene:TP53, gene_associated_disease, Disease:LiFraumeni)
> (Protein:P53, protein_in_pathway, Pathway:Apoptosis)
> (Gene:BRCA1, gene_expressed_in_anatomy, Anatomy:Breast)
> ```
>
> **Node types** (7개): Gene, Protein, Drug, Disease, Anatomy, Phenotype, GO term

### 유형 B — Quality-filtered subset

> ```
> High-quality subset:
>   · 노이즈 최소화 (high-confidence edge만)
>   · Smaller graph, faster training
> All subset:
>   · 전체 (most challenging, noisiest)
>   · Larger graph, realistic
> 사용자 task: 'OpenBioLink_HQ' vs 'OpenBioLink_All'
> ```

### 유형 C — Leakage-controlled split protocol

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
> → "trivially inferred" edges 제거
> ```

### 유형 D — Evaluation metric protocol

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

## 평가 framework 요약

| Dimension | Options |
|---|---|
| **Quality cutoff** | high / medium / low / all |
| **Split type** | random / time-slice |
| **Direction** | directed / undirected |
| **Source filter** | exclude specific source DBs |
| **Edge type filter** | exclude specific relation types |
| **Negatives** | from-source / typed-random |
| **Metrics** | Hits@K / MRR / ROC-AUC / PR-AUC |
| **Models** | PyKEEN 라이브러리 호환 (TransE, ComplEx, RotatE, etc.) |

---

## 주요 활용 (논문 + 후속)

| 항목 | 내용 |
|---|---|
| 표준 biomedical KG benchmark | FB15K-237 / WN18RR의 생의학 대응품 |
| Leakage 통제 | KG embedding 평가의 fair comparison |
| PyKEEN 통합 | 다양한 embedding 모델 빠른 비교 |
| Bioinformatics application note | 짧은 (~2 페이지) 형식, 코드/데이터 강조 |
| 후속 작업 | OGB-biokg (Hu 2020 NeurIPS), CLADD/MedGraphRAG의 사용 substrate |

---

## 한계점
- **Static dataset**: 데이터 update 시 leaderboard 재계산 필요
- **Source DB 의존**: UniProt/DrugBank 등의 라이센스 / coverage 제약
- **Confidence cutoff 임의성**: 4-tier 분류 기준이 source-specific
- **2020 cutoff**: 최신 DrugBank / DisGeNET 업데이트 미반영
- **English-only / public DB만**: 폐쇄 (UpToDate 등) 미커버
- **Edge type sparsity**: 일부 type은 sample 수 적음
- **Limited expressiveness**: 단순 (h,r,t) 구조 → 시간/조건 정보 없음

---

## 관련 정보
- **논문 (Bioinformatics)**: [10.1093/bioinformatics/btaa274](https://doi.org/10.1093/bioinformatics/btaa274)
- **DBLP**: [journals/bioinformatics/BreitOAS20](https://dblp.org/rec/journals/bioinformatics/BreitOAS20.html)
- **GitHub**: [OpenBioLink/OpenBioLink](https://github.com/OpenBioLink/OpenBioLink)
- **저자 소속**: Medical University of Vienna — Section for AI and Decision Support
- **이 benchmark가 평가한 모델 family**: TransE, ComplEx, RotatE, DistMult, R-GCN 등 (PyKEEN-호환)
- **이 benchmark를 사용한 후속 작업**: OGB-biokg [[DBLP:conf/nips/HuFZDRLCL20]], 생의학 KG embedding 논문 다수
- **관련 benchmark**: FB15K-237, WN18RR (general), UMLS (KGE 표준), OGB-biokg (heterogeneous)
