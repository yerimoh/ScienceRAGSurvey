---
title: "KIBA: Integrated Kinase Inhibitor Bioactivity Score Dataset"
bib_key: "tang2014kiba"
year: 2014
domain: chem, bio, medical
type: benchmark
venue: Journal of Chemical Information and Modeling
paper_link: https://doi.org/10.1021/ci400709d
---
# KIBA: 52,498 compounds × 467 kinases — Integrated Bioactivity Score

> J. Chem. Inf. Model. 54(3):735–743 | 2014 | Benchmark (DTI regression at scale) | chem · bio · medical
> Jing Tang, Agnieszka Szwajda, Sushil Shakyawar, Tao Xu, Petteri Hintsanen, Krister Wennerberg, Tero Aittokallio — Institute for Molecular Medicine Finland (FIMM), University of Helsinki
> DOI: [10.1021/ci400709d](https://doi.org/10.1021/ci400709d) · PMID 24521231

## 한 줄 요약
**3종의 large-scale 생화학 kinase inhibitor assay** + **ChEMBL** + **STITCH** 데이터를 **52,498 compounds × 467 kinases**의 단일 통합 매트릭스로 합쳐, IC50/Ki/Kd를 **246,088개 KIBA score**로 변환한 대규모 DTI benchmark. Davis (2011)의 대형 짝꿍으로 거의 항상 함께 보고됨.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 3개 large-scale kinase assay 소스 통합
  ├─ Anastassiadis et al. 2011 (Nature Biotech) — ~30K activities
  ├─ Davis et al. 2011 (Nat Biotech) — Kd 매트릭스
  ├─ Metz et al. 2011 (Nature Chem Biol) — pIC50 매트릭스
  └─ + ChEMBL bioactivities + STITCH chemical-protein

Step 2 — 다양한 측정 단위 통합 (KIBA score 계산)
  ┌─────────────────────────────────────────────┐
  │ Mixed bioactivity types:                    │
  │   - Kd (dissociation constant)              │
  │   - Ki (inhibition constant)                │
  │   - IC50 (50% inhibitory concentration)     │
  │                                              │
  │ KIBA score: 모델-기반 통합                  │
  │   → 서로 다른 assay/단위를 단일 score로     │
  │   → bias correction + consistency filtering │
  └─────────────────────────────────────────────┘

Step 3 — 매트릭스 결과
  ┌─────────────────┬──────────────────────┐
  │ 항목            │ 수치                  │
  ├─────────────────┼──────────────────────┤
  │ Compounds       │ 52,498               │
  │ Kinase targets  │ 467                  │
  │ Integrated      │ 246,088 KIBA scores  │
  └─────────────────┴──────────────────────┘

Step 4 — 결과 분석
  └─ 각 assay 간 활성 일치율 quantify
  └─ Compound bioactivity profile 패턴 군집
  └─ Drug repositioning 후보 시사
```

---

## 원문 직접 인용 (Tang 2014 JCIM §Abstract)

> "We integrated bioactivity measurements from **three recent large-scale biochemical assays** of kinase inhibitors alongside data from established databases (**ChEMBL** and **STITCH**)."

> "The study consolidated diverse bioactivity types including **IC50, Ki, and Kd** values across **52,498 compounds** and **467 kinase targets**, generating **246,088 integrated KIBA scores**."

---

## 주요 활용

| 항목 | 내용 |
|---|---|
| Task 정의 | Drug-Target Interaction (DTI) regression — 대규모 |
| Output | KIBA score (낮을수록 강한 결합) |
| Pairing | Davis dataset과 함께 보고되는 표준 짝꿍 |
| Pioneer 모델 | DeepDTA (Öztürk 2018) — DAVIS + KIBA 둘 다 baseline |
| 대비 Davis | 약 700× 큰 규모, sparsity 더 높음 |
| TDC 통합 | `multi_pred.DTI.KIBA` |

---

## 데이터셋 통계

| Subset | 수치 |
|---|---|
| Compounds (drugs/inhibitors) | 52,498 |
| Kinase targets | 467 |
| 통합 KIBA scores | 246,088 |
| Sparsity | ~99% (drug × target 매트릭스 대부분 비어 있음) |
| Bioactivity 원본 단위 | Kd, Ki, IC50 모두 통합 |

---

## 한계점
- **여전한 sparsity**: 246K scores / (52K × 467) ≈ 1% — matrix completion task로 어려움
- **단위 통합 model assumption**: KIBA score 변환 시 정확도 가정 (Kd/Ki/IC50 ≠ 정확히 비교 가능)
- **Kinase 외 무관**: kinase-specific, 다른 단백질 family 미포함
- **시간**: 2014년 데이터, 최신 inhibitor (kinase degrader, allosteric) 미반영
- **단일 통합 score**: type-specific binding mode 정보 손실 (예: type I vs II)

---

## 관련 정보
- **논문 (DOI)**: [10.1021/ci400709d](https://doi.org/10.1021/ci400709d)
- **PubMed**: [PMID 24521231](https://pubmed.ncbi.nlm.nih.gov/24521231/)
- **저자 소속**: FIMM, University of Helsinki (now Aittokallio Lab)
- **이 benchmark를 사용한 주요 작업**: DeepDTA, GraphDTA, AttentionDTA, MolTrans, KronRLS, SimBoost 등 거의 모든 DTI deep learning 논문
- **함께 보고되는 짝꿍**: [Davis](davis2011kinase.html) (Davis et al. 2011 Nat Biotechnol)
