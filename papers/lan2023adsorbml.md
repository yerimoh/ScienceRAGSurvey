---
title: "AdsorbML: A Leap in Efficiency for Adsorption Energy Calculations using Generalizable ML Potentials"
bib_key: "lan2023adsorbml"
year: 2023
domain: material, chem
type: benchmark
venue: npj Computational Materials
paper_link: https://doi.org/10.1038/s41524-023-01121-5
---
# AdsorbML: 1,000 Adsorbate-Surface Pairs DFT-Success Benchmark

> npj Computational Materials 9:172 | 2023 | Benchmark (adsorption-energy workflow + Open Catalyst Dense dataset) | material · chem
> Janice Lan, Aini Palizhati, Muhammed Shuaibi, Brandon M. Wood, Brook Wander, Abhishek Das, Matt Uyttendaele, C. Lawrence Zitnick, Zachary W. Ulissi — Meta AI (FAIR) / CMU
> arXiv: [2211.16486](https://arxiv.org/abs/2211.16486) · DOI: [10.1038/s41524-023-01121-5](https://doi.org/10.1038/s41524-023-01121-5)

## 한 줄 요약
ML interatomic potential을 사용해 **adsorbate-surface 결합 에너지 계산**을 가속하는 알고리즘 + benchmark. **Open Catalyst Dense** 데이터셋 (~1,000 surfaces × ~100,000 configurations) 위에서 **87.36% 최저-에너지 configuration 식별률**과 **~2000× DFT 대비 속도 향상** 달성.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Task 정의
  ┌────────────────────────────────────────────────┐
  │ Input: adsorbate molecule + catalyst surface   │
  │ Output: lowest-energy adsorbate-surface        │
  │         configuration (3D pose) + binding E    │
  │ Verifier: DFT (ground truth)                   │
  └────────────────────────────────────────────────┘

Step 2 — Open Catalyst Dense dataset 구축
  └─ ~1,000 catalyst surfaces (binary alloys, oxides, intermetallics 등)
  └─ ~100,000 unique adsorbate-surface configurations
  └─ DFT (PBE) ground truth labels
  └─ 표준화된 benchmark 형식

Step 3 — AdsorbML 알고리즘
  ┌──────────────────────────────────────────────┐
  │ 1. Heuristic + random initial configurations │
  │ 2. ML potential (GemNet-OC 등) energy 예측    │
  │ 3. Low-energy candidates → ML relaxation     │
  │ 4. Top-k candidates → DFT 정밀 검증           │
  │ 5. 최저 에너지 configuration 선택             │
  └──────────────────────────────────────────────┘

Step 4 — Evaluation metrics
  · Success rate: lowest-energy config 찾기 비율 (target)
  · Speedup: DFT-only baseline 대비
  · Energy error: vs DFT ground truth
  · Trade-off curve: accuracy × efficiency
```

---

## 실제 데이터 형식 예시 (논문 §Methods + Table I + Table II)

### 유형 A — Input/Output schema

> **Input**: catalyst surface + adsorbate (반응 중간체, *CHO / *CO / *OH 등)
>
> ```
> Surface:    slab with 3D periodic boundary
> Adsorbate:  reaction intermediate (e.g., *CHO for CO2 reduction)
> Initial config: heuristic (symmetry-based) + random sampling
> ```
>
> **Output**: lowest adsorption energy + valid relaxed structure
>
> ```
> E_ads ≡ min over all valid relaxed configs (eV)
> Valid 기준:
>   - 흡착물이 표면에서 desorption 안 됨
>   - dissociation 안 됨
>   - surface mismatch 없음
> Success: predicted E_ads가 DFT 최솟값과 0.1 eV 이내
> ```

### 유형 B — OC20-Dense dataset 구조

> | Split | Unique systems | Unique configs | Adsorbates | Bulks |
> |---|---|---|---|---|
> | **Validation** | 973 | 85,658 | 74 | 833 |
> | **Test** | 989 | 105,714 | 74 | 837 |
>
> 각 split은 ~250 systems × 4 subsplits = **ID, OOD-Adsorbate, OOD-Catalyst, OOD-Both**

### 유형 C — Algorithm (ML+SP / ML+RX, top-k)

> ```
> 1. Generate initial configs (heuristic + random sampling)
> 2. ML potential relaxation → rank by energy (lowest first)
> 3. Take best-k candidates:
>    Option A (ML+SP): single-point DFT on each → take min
>    Option B (ML+RX): full DFT relaxation from ML state → take min
> 4. Return: min(DFT outputs)
> ```
>
> Trade-off knob: **k = 1, 2, 3, 4, 5** (k↑ → 정확도↑, speedup↓)

### 유형 D — Model 비교 (Table I, OC20-Dense Test)

> | Model | Success Rate ↑ | Energy MAE [eV] ↓ | OC20 S2EF Force MAE [eV/Å] |
> |---|---|---|---|
> | SchNet | 1.01% | 0.5150 | 0.0496 |
> | DimeNet++ | 1.72% | 0.4329 | 0.0446 |
> | PaiNN | 10.92% | 0.2994 | 0.0294 |
> | GemNet-OC | 46.51% | 0.1849 | 0.0179 |
> | GemNet-OC-MD | 50.05% | 0.1966 | 0.0173 |
> | GemNet-OC-MD-Large | 48.03% | 0.1935 | 0.0164 |
> | SCN-MD-Large | 51.87% | 0.1758 | 0.0160 |
> | **eSCN-MD-Large** | **56.52%** | **0.1739** | **0.0139** |
>
> → AdsorbML (eSCN-MD-Large, k=3, ML+SP): **89.28% success × ~2000× speedup** (논문 Figure 3 balanced point: 87.36% × 2290×)

---

## 원문 직접 인용 (arXiv:2211.16486 §Abstract)

> "we demonstrate **machine learning potentials can be leveraged to identify low energy adsorbate-surface configurations** more accurately and efficiently"

> "one balanced option finding the lowest energy configuration **87.36% of the time**, while achieving a **~2000× speedup** in computation"

> "we introduce the **Open Catalyst Dense dataset** containing nearly **1,000 diverse surfaces and ~100,000 unique configurations**"

---

## 주요 평가 결과

| Configuration | Success Rate | Speedup vs DFT |
|---|---|---|
| Fast (ML only, top-1) | 낮음 | ~10,000× |
| **Balanced (ML+DFT top-k)** | **87.36%** | **~2000×** |
| Conservative (ML+DFT top-N) | 더 높음 | ~500× |

→ Accuracy-efficiency trade-off spectrum 제공.

---

## 평가 단위

| 항목 | 내용 |
|---|---|
| Test set | Open Catalyst Dense (~1,000 surfaces) |
| Metric | Success rate + Speedup |
| Baseline | DFT-only structure relaxation |
| ML potential | GemNet-OC, SchNet, eSCN 등 OC family |
| Adsorbates | OC20 reaction intermediates (CO, CHO, OH, NO 등) |

---

## 한계점
- **PBE functional 의존**: 다른 functional과 격차
- **OC20-trained models 한정**: 다른 chemistry 적용 시 transfer 한계
- **Initial configuration 의존**: heuristic 시작점 품질이 결과에 영향
- **메모리·계산비 (대형 unit cell)**: 큰 셀에서 ML 정확도 저하
- **Catalyst 외 도메인 미커버**: bulk/molecular system 미평가
- **시간**: 2023년 cutoff, 최신 foundation MLIP 미반영

---

## 관련 정보
- **논문 (npj CompMat)**: [10.1038/s41524-023-01121-5](https://doi.org/10.1038/s41524-023-01121-5)
- **arXiv**: [2211.16486](https://arxiv.org/abs/2211.16486)
- **데이터**: Open Catalyst Project Dense subset
- **공식 사이트**: [opencatalystproject.org](https://opencatalystproject.org/)
- **GitHub**: [Open-Catalyst-Project/ocp](https://github.com/Open-Catalyst-Project/ocp)
- **이 benchmark를 사용한 후속 작업**: Open Catalyst 2022/2024 (OC22, OC24), MLIP Arena (NeurIPS 2025 D&B), foundation MLIP 평가
