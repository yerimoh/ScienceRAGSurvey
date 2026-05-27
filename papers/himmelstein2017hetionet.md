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

## 한 줄 요약
29개 공개 자원을 통합한 **47,031 노드 (11 type) × 2,250,197 relationship (24 edge type)** 의 hetnet (heterogeneous network). 약물 재활용(drug repurposing) edge prediction 표준 GT로 자리잡았으며, **40명 community 멤버**의 실시간 피드백을 받은 **fully open** 연구.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 소스 통합 (29 public resources)
  └─ DrugBank, ChEMBL, SIDER, Bgee, GTEx, MSigDB, GO, DO, MeSH,
     GWAS Catalog, LINCS L1000, STRING, BioGRID, PathBank, etc.

Step 2 — Node typing (11 types)
  ┌──────────────────────┬─────────────────────────┐
  │ Node type            │ 예시                     │
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
  └─ ... 24 종류 총

Step 4 — Drug Repurposing 모델: Project Rephetio
  └─ Metapath-based feature engineering
  └─ Logistic regression on metapath similarities
  └─ DM (Compound-treats-Disease) edge prediction
  └─ 새 후보: nicardipine, fluoxetine for Multiple Sclerosis 등

Step 5 — Open community development
  └─ GitHub-first manuscript (dhimmel/rephetio-manuscript)
  └─ 40명 외부 community 멤버 실시간 피드백
  └─ "entirely open" 연구 모델
```

---

## 원문 직접 인용 (Himmelstein 2017 eLife §본문)

> "Hetionet v1.0 consists of **47,031 nodes of 11 types** and **2,250,197 relationships of 24 types**. Data was integrated from **29 public resources** to connect compounds, diseases, genes, anatomies, etc."

> "The hetnet contains 47,031 nodes of 11 types (Table 1) and 2,250,197 relationships of 24 types (Table 2). The nodes consist of **1,552 small molecule compounds** and **137 complex diseases**."

> "This study was **entirely open** and received realtime feedback from **40 community members**."

---

## Project Rephetio 평가 결과

| 항목 | 내용 |
|---|---|
| Task | Compound-treats-Disease edge prediction |
| Training | known 1,552 × 137 (compound × disease) treatments |
| Features | metapath count + diffusion-based scores |
| AUROC | ~0.97 (validation) |
| 신약 발견 사례 | nicardipine for MS, fluoxetine reuse 등 |

---

## 주요 활용

| 항목 | 내용 |
|---|---|
| Task 정의 | Drug repurposing edge prediction |
| Granularity | Compound-treats-Disease (DM) edge inference |
| 후속 작업 | EdgePrediction, NodeXL community detection |
| KG embedding 모델 | TransE, ComplEx, DistMult on Hetionet |
| 차별성 | DRKG/PrimeKG와 별도로 repurposing edge-prediction 표준 |

---

## 한계점
- **2017년 v1.0 cutoff**: 신약/신질환 미반영
- **Open Targets / DrugBank 의존성**: 원본 DB 라이선스 변경 시 일부 사용 제한
- **Predicted treatment 검증**: edge prediction은 hypothesis 생성, wet-lab 추가 필요
- **Heterogeneity bias**: 일부 edge type은 data sparse
- **단방향 relationship**: 모든 edge는 unweighted (strength 미반영)

---

## 관련 정보
- **논문 (eLife)**: [10.7554/eLife.26726](https://doi.org/10.7554/eLife.26726)
- **공식 사이트**: [het.io](https://het.io) — 인터랙티브 탐색
- **GitHub**: [hetio/hetionet](https://github.com/hetio/hetionet)
- **데이터 다운로드**: [github.com/hetio/hetionet/tree/master/hetnet](https://github.com/hetio/hetionet/tree/master/hetnet)
- **Project Rephetio 결과**: [het.io/repurpose](https://het.io/repurpose)
- **이 benchmark를 사용한 주요 작업**: DRKG, PrimeKG (구조적 영감), TxGNN, GraIL 등 biomedical KG embedding/inference 연구
