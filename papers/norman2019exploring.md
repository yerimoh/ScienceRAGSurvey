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

## 한 줄 요약
**287 dual-CRISPRi (CRISPR interference) gene-pair × K562 erythroleukemia cells**에서 측정한 **Perturb-seq atlas**. 각 dual perturbation은 두 sgRNA를 동일 세포에 발현시켜 두 유전자를 동시 knockdown. **rich single-cell transcriptomic phenotype** 기반으로 **genetic interaction manifold**를 구성, 유전자 쌍의 **synergy / suppression / redirection / neomorphism** 등 GI subtype을 phenotype 공간에서 직접 분류. 이후 GEARS / PerturBench / scGPT 등 **모든 dual-gene perturbation prediction 모델의 표준 substrate**.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 동기: GI 측정의 한계
  ┌──────────────────────────────────────────────┐
  │ 전통 GI 측정 (epistasis):                    │
  │   · single readout (성장률, 사멸 등)         │
  │   · scalar GI score만 산출                   │
  │   · 같은 score여도 분자적 기전 다름           │
  │ → rich phenotype (전사체) 기반 GI 필요       │
  └──────────────────────────────────────────────┘

Step 2 — Cell line + perturbation library 구축
  ┌──────────────────────────────────────────────┐
  │ Cell line: K562 (erythroleukemia)            │
  │ CRISPRi machinery: dCas9-KRAB stable line   │
  │ sgRNA library:                                │
  │   · 단일 유전자 sgRNA pool                    │
  │   · 모든 페어 조합 → dual sgRNA constructs   │
  │ Pair selection: TF + cell-fate regulator     │
  │   focus (myeloid/erythroid lineage 관련)    │
  └──────────────────────────────────────────────┘

Step 3 — Perturb-seq 실험 규모
  ┌──────────────────────────────────────────────┐
  │ Single-gene perturbations:     ~107–155 게놈  │
  │ Dual-gene combinations:        ~131–287 쌍   │
  │ (보고된 값은 분석 단계 / 필터링에 따라 변동)  │
  │ Per-perturbation cell count:   ~수백          │
  │ Total cells profiled:          ~수십만        │
  │ Readout: 10x Chromium single-cell RNA-seq    │
  └──────────────────────────────────────────────┘

Step 4 — GI manifold 분석
  · 각 perturbation의 mean transcriptomic delta 계산
  · UMAP/PCA로 perturbation 임베딩 시각화
  · single + dual perturbation을 동일 공간에 배치
  · dual의 위치를 single 두 점의 선형/비선형 조합과
    비교 → GI subtype 분류

Step 5 — GI subtype 분류 체계
  ┌──────────────────────────────────────────────┐
  │ NEOMORPHIC: dual이 single 어느 것과도 다름  │
  │ REDUNDANT:  dual ≈ single A ≈ single B      │
  │ SUPPRESSOR: dual ≈ control (B가 A 억제)     │
  │ EPISTASIS_A: dual ≈ single A (A 우세)       │
  │ POTENTIATION: dual >> single A + single B   │
  │ ADDITIVE: dual ≈ single A + single B (선형) │
  └──────────────────────────────────────────────┘
```

---

## 실제 데이터 형식 예시 (논문 §Methods + Supplementary)

### 유형 A — Single-gene CRISPRi perturbation record

> ```
> Cell:        K562 (CRISPRi-ready, dCas9-KRAB stable)
> sgRNA:       targeting CEBPA promoter (TSS-proximal)
> Knockdown:   transcriptional repression (~80-95% of WT)
> Readout:     scRNA-seq (10x Chromium)
> Cell count:  ~500-2000 cells per perturbation
> Gene exp:    raw UMI count matrix (cells × genes)
> ```

### 유형 B — Dual-gene combinatorial perturbation

> ```
> Dual sgRNA construct: sgRNA-A (targets CEBPA)
>                     + sgRNA-B (targets CEBPB)
> Co-infection:        single cell gets both sgRNAs
> Verification:        sgRNA capture or barcoding
> Phenotype:           cell expression vector under
>                     simultaneous CEBPA + CEBPB KD
> ```

### 유형 C — GI manifold input/output

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

### 유형 D — Downstream ML 사용 예시 (GEARS 기준)

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

## 평가 framework (downstream model이 사용)

| Metric | 의미 | 사용처 |
|---|---|---|
| **MSE on top-20 DEG** | DEG에서의 예측 정확도 | GEARS, PerturBench |
| **Pearson correlation** | 전체 Δexpression 상관 | 일반적 |
| **Precision@10 (GI subtype)** | 상위 10개 예측 GI 분류 정확도 | GEARS GI head |
| **MMD (PCA top-256)** | 분포 일치 | PerturBench |
| **rank metric** | 모든 perturbation 간 순서 | PerturBench (mode-collapse 탐지) |

→ Norman 2019는 데이터 그 자체로는 metric 없음; downstream model이 위 metric으로 평가.

---

## 주요 발견 (논문 §Results)

| 발견 | 의미 |
|---|---|
| GI manifold가 cell-fate program으로 정렬 | erythroid / myeloid lineage 축 |
| Suppressor pair 다수 검출 | scalar GI score로 못 잡던 |
| Neomorphic pair (CEBPA+CEBPB 등) 발견 | 새 program 출현 |
| Dual phenotype의 ~70%는 가산 (linear) | 비가산 GI는 30% 정도 |
| rich phenotype이 epistasis 분류 가능 | scalar fitness 한계 극복 |

→ **결론**: scRNA-seq 기반 rich phenotype으로 GI analysis 패러다임 전환, 후속 perturbation prediction 모델의 표준 substrate가 됨.

---

## 한계점
- **K562 cell line만**: 다른 cell type / 1차 세포 미커버
- **CRISPRi (knockdown)만**: knockout, overexpression, drug perturbation 별도
- **TF + cell-fate regulator 위주 pair 선택**: 다른 pathway 미포함
- **단일 시점**: time-course 정보 없음
- **287 pair << 4억 가능 조합**: combinatorial space 극히 일부
- **scRNA-seq dropout**: 저발현 유전자 정확도 제한

---

## 관련 정보
- **논문 (Science)**: [10.1126/science.aax4438](https://doi.org/10.1126/science.aax4438)
- **데이터 접근**: GEO + GEARS 전처리 버전 (`gears.PertData.load('norman')`)
- **저자 소속**: UCSF (Weissman lab) / Whitehead Institute
- **이 dataset을 사용한 후속 작업**:
  - GEARS [[roohani2024gears]] (102 sg + 131 dg 표준 split)
  - PerturBench [[DBLP:journals/corr/abs-2408-10609]] (155 sg + 131 dg, combo prediction task)
  - scGPT, scFoundation — Norman19를 fine-tuning benchmark로 사용
- **선행 연구**: Adamson 2016 (UPR), Dixit 2016 (Perturb-seq 원형), Replogle 2022 (genome-scale Perturb-seq)
