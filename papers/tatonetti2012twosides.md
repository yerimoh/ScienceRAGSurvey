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

## 한 줄 요약
FDA의 자발적 부작용 보고 시스템(FAERS)에서 측정되지 않은 교란 요인을 보정하는 통계적 접근으로 두 가지 자원을 구축: **OFFSIDES** (단일 약물 부작용 DB)와 **TWOSIDES** (약물 쌍 간 부작용 DB). DDI side-effect 예측 모델 평가의 canonical ground truth로 자리잡음.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 출처: FAERS (FDA Adverse Event Reporting System)
  └─ FDA에 자발 보고된 부작용 신고 raw data (수백만 건)

Step 2 — 측정되지 않은 교란 보정 (저자 핵심 기여)
  └─ Adaptive correction methodology 개발
  └─ 환자 인구통계·동반질환·약물 노출 패턴 보정
  └─ 거짓 양성 부작용 신호 제거

Step 3 — 자원 두 개 구축
  ┌──────────────┬─────────────────────────────────┐
  │ OFFSIDES     │ 단일 약물 부작용 데이터베이스    │
  │              │ FDA on-label 외 추가 부작용     │
  ├──────────────┼─────────────────────────────────┤
  │ TWOSIDES     │ 약물 쌍 × 부작용 라벨           │
  │              │ DDI side-effect type prediction │
  │              │ canonical GT (DrugBank는        │
  │              │ "존재 여부"만 있는 반면, type   │
  │              │ 라벨까지 제공)                  │
  └──────────────┴─────────────────────────────────┘

Step 4 — 외부 검증
  └─ 47 drug class interactions를 독립적인 EMR 데이터로 corroborate
  └─ 핵심 발견: SSRI + thiazide → QT prolongation 유의 증가
```

---

## 원문 직접 인용 (Tatonetti 2012 STM, PMC3382018 body verbatim)

> "We developed an adaptive approach to correct for unmeasured confounding factors in spontaneous reporting databases and created two resources: **Offsides (a database of drug effects) and Twosides (a database of drug-drug interaction side effects)**."

> Data source: "**1,851,171 adverse event reports** in the AERS from the FDA's Web site from the first quarter of **2004 to the first quarter of 2009**"

> Propensity score matching (PSM): "**Each exposed patient (that is, report) is matched to a nonexposed patient with a similar probability** according to the PSM model, thereby mitigating the effects of confounders" + "we used PSM to model the probability that a given report lists [that drug] as a concomitant medication" using "the top 200 covariates (sorted by their Spearman correlation coefficient, ρ)"

> **OFFSIDES dataset**: "**438,801 off-label side effects** for **1,332 drugs** and **10,097 adverse events**"

> **TWOSIDES dataset**: "**868,221 significant associations** between **59,220 pairs of drugs** and **1,301 adverse events**"

> EMR validation: "We found additional evidence of drug effects for **47 of 395 interactions** when looking for short-term (≤36 days) changes in laboratory markers after the start of treatment"

> SSRI + thiazide QT case: "patients receiving combined thiazides and SSRIs showed **1.5 (95% CI, 1.2 to 1.9) times as likely** to record a prolonged QT interval compared to thiazide-only users"

---

## 데이터셋 통계 (논문 본문 verbatim)

| 항목 | 수치 |
|---|---|
| AERS raw reports | 1,851,171 (2004 Q1 ~ 2009 Q1) |
| **OFFSIDES 부작용 라벨 수** | **438,801** |
| OFFSIDES 약물 수 | 1,332 |
| OFFSIDES adverse event 종류 | 10,097 |
| **TWOSIDES 약물 쌍 수** | **59,220** |
| TWOSIDES significant associations | 868,221 |
| TWOSIDES adverse event 종류 | 1,301 |
| EMR validation 비율 | 47/395 (≈12%) |

## 주요 활용

| 항목 | 내용 |
|---|---|
| Database-verified DDI prediction GT | DDI side-effect type 라벨 표준 |
| 라벨 granularity | DrugBank("DDI exists or not")보다 세밀 (specific ADR type) |
| 인용 후속 작업 | Decagon (Zitnik 2018), MUFFIN, DDI-PULearn, 등 다수 DDI 모델 평가 |
| 통합 위치 | TDC `multi_pred.DDI` task의 핵심 데이터 |

---

## 한계점
- FAERS 자발 보고 의존 → 표본 편향 (under-reporting / over-reporting)
- 시간적 cutoff: 2012년까지 데이터, 신약 미반영
- 인과관계 ≠ 상관관계: confounding 보정해도 spurious signal 가능
- 부작용 유형 표준화: MedDRA terminology 의존
- 약물 쌍에만 적용 (3+ 약물 동시 복용 미지원)

---

## 관련 정보
- **논문 (DOI)**: [10.1126/scitranslmed.3003377](https://doi.org/10.1126/scitranslmed.3003377)
- **PubMed**: [PMID 22422992](https://pubmed.ncbi.nlm.nih.gov/22422992/)
- **Data download**: [tatonettilab.org/offsides](https://tatonettilab.org/offsides) (현재) · 원본은 Stanford 호스팅
- **이 데이터를 사용한 후속 작업**: TDC `multi_pred.DDI`, Decagon (Zitnik et al. 2018 Bioinformatics), MR-GNN 등 DDI side-effect 예측 표준 GT
