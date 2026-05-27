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

## 한 줄 요약
단백질의 기능(Gene Ontology term)을 시퀀스/구조로부터 예측하는 task의 **국제 challenge benchmark**. CAFA1(2010) → CAFA2(2013) → CAFA3(2017–2019) 3회 cycle 운영. **time-delayed evaluation** 프로토콜로 challenge 시작 시점에 GO annotation이 없는 단백질이 챌린지 기간 동안 실험으로 검증된 결과를 hidden test set으로 사용.

---

## 어떻게 만들었나 (CAFA Challenge Methodology)

```
Step 1 — Challenge timeline (3년 주기)
  ┌──────────────────────────────────────────────┐
  │ T0: Challenge 개시 — UniProt-GO annotation   │
  │     snapshot 공개                            │
  │                                               │
  │ T0 ~ T0+9개월: 참가자 예측 제출 마감          │
  │     (각 미주석 단백질에 대해 GO term 후보들  │
  │      을 확률 점수와 함께 ranked list 제출)   │
  │                                               │
  │ T0+9 ~ T0+30개월: 자연 실험적 검증 누적       │
  │     UniProt이 새 GO annotation 등록          │
  │                                               │
  │ T0+30개월: Held-out test set 확정             │
  │     T0 시점 unannotated였으나 챌린지 기간    │
  │     실험으로 새 annotation을 받은 단백질들    │
  └──────────────────────────────────────────────┘

Step 2 — Evaluation: time-delayed held-out
  └─ 챌린지 시작 후 새로 annotated된 단백질만 test
  └─ data leakage 원천 차단 (전체 시간축으로)
  └─ "retrieve-then-rank GO term" task 형식

Step 3 — Target 종 + 분야
  └─ 18+ target species (human, mouse, yeast, A. thaliana 등)
  └─ 3 GO sub-ontologies: BP (Biological Process),
                          MF (Molecular Function),
                          CC (Cellular Component)
  └─ NK (No Knowledge) + LK (Limited Knowledge) categories

Step 4 — Evaluation metric
  └─ Fmax (precision-recall curve의 max F1)
  └─ Smin (semantic distance, GO 계층 고려)
  └─ ROC-AUC (per-term basis)
  └─ Coverage (얼마나 많은 단백질에 예측 제공)
```

---

## 원문 직접 인용 (Zhou 2019 Genome Biol §Title)

> Title: *"The **CAFA challenge reports improved protein function prediction** and new functional annotations for hundreds of genes through experimental screens"*

> "the third Critical Assessment of Function Annotation (CAFA3) ... evaluation of method performance using time-delayed propagation"

> CAFA series: CAFA1 (2010–2011, 18 species), CAFA2 (2013–2014, ~100,000 proteins), CAFA3 (2016–2018, ~92,000 proteins)

---

## 평가 셋업

| 항목 | CAFA3 (2017–2019) |
|---|---|
| Challenge cycle | 3rd edition |
| Target proteins | ~92,000 (challenge 시작 시 unannotated) |
| Held-out test size | 챌린지 기간 동안 새로 annotated된 ~3,000–10,000 단백질 |
| GO sub-ontologies | MF (Molecular Function), BP (Biological Process), CC (Cellular Component) |
| Categories | No-Knowledge (NK), Limited-Knowledge (LK) |
| Submission format | Per-protein, per-GO-term confidence score (0–1) |
| Primary metric | Fmax (precision-recall 기반) |
| Secondary metrics | Smin (semantic distance), ROC-AUC, coverage |

---

## 주요 평가 결과 (논문 본문)

| 항목 | 내용 |
|---|---|
| 참가 팀 | 50+ 국제 그룹 |
| 최고 성능 모델 | DeepGOPlus, NetGO, GOLabeler, ... (CAFA3) |
| 인간 단백질 GO MF Fmax | ~0.6 (top systems) |
| 종 횡단 generalization | 인간 외 종에서 성능 저하 |
| "Improved" 키워드 | CAFA1 → CAFA3로 일관된 성능 향상 입증 |

---

## 주요 활용

| 항목 | 내용 |
|---|---|
| Task | Protein → GO term ranking |
| Retrieval-then-rank | retrieve homologs → rank candidate GO terms canonical 패턴 |
| Database verifier | UniProt-GO held-out experimental annotations |
| RAG application | sequence embedding retrieval → GO term proposal |
| 후속 작업 | CAFA4 (2020–), CAFA5 (Kaggle 2023) |

---

## 한계점
- **Sparse annotation**: GO term은 인간조차 부분 annotated, full ground truth 없음
- **Bias toward studied proteins**: 잘 연구된 단백질이 over-represented
- **GO ontology drift**: 챌린지 도중 ontology 자체 업데이트 가능
- **Long-tail GO terms**: 희귀 function은 examples 부족
- **3년 cycle**: 평가 결과 발표가 모델 개발 후 한참 뒤
- **Domain bias**: human/model organism 비율 높음, microbial protein 적음

---

## 관련 정보
- **논문 (Genome Biol)**: [10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)
- **PubMed**: [PMID 31744546](https://pubmed.ncbi.nlm.nih.gov/31744546/)
- **공식 사이트**: [biofunctionprediction.org](https://www.biofunctionprediction.org/cafa) (CAFA consortium)
- **CAFA3 데이터**: synapse.org/cafa3
- **Kaggle CAFA5 (2023)**: [kaggle.com/competitions/cafa-5-protein-function-prediction](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction)
- **이 challenge를 사용한 주요 모델**: DeepGOPlus, NetGO, GOLabeler, Funfams, Argot, INGA, TALE, ProteInfer 등
