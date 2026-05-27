---
title: "Matbench Discovery: A Framework to Evaluate ML Crystal Stability Predictions"
bib_key: "riebesell2025matbench"
year: 2025
domain: material, chem, physics
type: benchmark
venue: Nature Machine Intelligence
paper_link: https://doi.org/10.1038/s42256-025-01055-1
---
# Matbench Discovery: ML Crystal Stability Benchmark on 257K WBM Structures

> Nature Machine Intelligence 7:836–847 | 2025 | Benchmark (convex-hull stability prediction) | material · chem · physics
> Janosh Riebesell, Rhys E. A. Goodall, Philipp Benner, Yuan Chiang, Bowen Deng, Gerbrand Ceder, Mark Asta, Alpha A. Lee, Anubhav Jain, Kristin A. Persson — Cambridge / LBNL / BAM / UC Berkeley
> arXiv: [2308.14920](https://arxiv.org/abs/2308.14920) · DOI: [10.1038/s42256-025-01055-1](https://doi.org/10.1038/s42256-025-01055-1)

## 한 줄 요약
ML energy 모델을 **고처리량 안정 무기 결정 탐색의 pre-filter**로 평가하는 task-based benchmark. **WBM 데이터셋의 257K+ 구조**에 대해 **convex hull distance**의 F$_1$, DAF, precision/recall을 측정하며, **UIP(Universal Interatomic Potential)** 들이 F$_1$ 0.57–0.82, **discovery acceleration factor up to 6×**로 최고 성능.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Test corpus: WBM dataset
  └─ Wang et al. 2021 npj CompMat
  └─ 257,487 구조 (relaxed + unrelaxed)
  └─ Materials Project을 합성한 chemistry 확장

Step 2 — Task 정의
  ┌──────────────────────────────────────────┐
  │ Input: 미relaxed candidate crystal       │
  │ Predict: distance from convex hull       │
  │   (relaxed → E_hull < 0 → stable)        │
  │ Threshold: 0 eV/atom above convex hull   │
  │   → binary classification: stable/unstable│
  └──────────────────────────────────────────┘

Step 3 — Primary metrics (classification-focused)
  · F$_1$ score (binary stable/unstable)
  · DAF (Discovery Acceleration Factor):
    "found N stable from K predictions" vs random
  · Precision (P): TP / (TP + FP)
  · Recall (R): TP / (TP + FN)

Step 4 — Secondary: regression metrics
  · MAE on E_hull (eV/atom)
  · Disagreement with classification metric:
    "high false-positive rate near 0 eV/atom decision boundary"

Step 5 — Public leaderboard + Python package
  └─ Submission via Python package
  └─ Online leaderboard maintained
```

---

## 실제 데이터 형식 예시 (논문 §2 + Table 1)

### 유형 A — Test input/output schema (IS2RE-style)

> **Input**: WBM 데이터셋의 **unrelaxed** prototype structure (5 batches of elemental substitution, 1–5회 치환)
>
> ```
> Structure:   periodic unit cell (initial, not DFT-relaxed)
> Prototype:   ICSD-based with elemental substitution
> Batch ID:    1 ~ 5 (substitution depth, OOD progressing)
> ```
>
> **Predict**:
> ```
> E_above_hull (eV/atom) — distance from MP convex hull
> → Classify: stable (E ≤ 0) / unstable (E > 0)
> ```
>
> **Training corpus (compliant)**:
> - Materials Project v2022.10.28 release (~154K crystals)
> - All relaxation frames, energies/forces/stresses allowed
> - Auxiliary tasks (charge, magmom) allowed

### 유형 B — Test set scale & cleaning

> ```
> ┌────────────────────────────────────────────────┬──────────┐
> │ Source: WBM (Wang et al. 2021 npj CompMat)     │  257,487 │
> │   - Removed pathological (|E| > 5 eV/atom)     │     -524 │
> │   - Removed MP-overlapping protostructures     │  -11,175 │
> │   - Removed duplicated protostructures         │   ...    │
> │ Final unique prototype test set                │  215,488 │
> │   of which thermodynamically stable (E ≤ 0)    │   32,942 │
> └────────────────────────────────────────────────┴──────────┘
> ```

### 유형 C — Leaderboard model 정렬 (Table 1)

> | Rank | Model | F$_1$ ↑ | DAF ↑ | Prec ↑ | MAE ↓ | Training | Targets |
> |---|---|---|---|---|---|---|---|
> | 1 | **eqV2 S DeNS** | **0.815** | **5.042** | 0.771 | 0.036 | MPtrj 1.6M | EFSD |
> | 2 | ORB MPtrj | 0.765 | 4.702 | 0.719 | 0.045 | MPtrj 1.6M | EFSD |
> | 3 | SevenNet | 0.724 | 4.252 | 0.650 | 0.048 | MPtrj 1.6M | EFSG |
> | 4 | MACE | 0.669 | 3.777 | 0.577 | 0.057 | MPtrj 1.6M | EFSG |
> | 5 | CHGNet | 0.613 | 3.361 | 0.514 | 0.063 | MPtrj 1.6M | EFSGM |
> | 6 | M3GNet | 0.569 | 2.882 | 0.441 | 0.075 | MPF 188K | EFSG |
> | 7 | ALIGNN | 0.567 | 3.206 | 0.490 | 0.093 | MP 2022 155K | E only |
> | 8 | MEGNet | 0.510 | 2.959 | 0.452 | 0.130 | MP Graphs 133K | E only |
> | 9 | CGCNN | 0.507 | 2.855 | 0.436 | 0.138 | MP 2022 155K | E only |
> | … | Wrenformer, BOWSR, Voronoi RF | 0.466 → 0.333 | … | | | | |
> | — | Dummy (random) | 0.185 | 1.000 | 0.154 | 0.124 | — | — |
>
> → UIPs (energy+force+stress) > energy-only one-shot 모델: 명확한 격차

### 유형 D — Regression vs Classification 불일치 예시

> "Accurate regressors can yield **high false-positive rates near the decision boundary at 0 eV/atom**" — 작은 MAE라도 hull 근처에서는 stable/unstable 오분류 다수 발생.
>
> 예시: CGCNN+P, Wrenformer, BOWSR — regression MAE는 양호하나 F$_1$이 낮음 (task-based 평가 필요성 증명)

---

## 원문 직접 인용 (arXiv:2308.14920 §Abstract)

> "We present **Matbench Discovery**, an evaluation framework for ML energy models, applied as **pre-filters for high-throughput searches of stable inorganic crystals**."

> Ranking (best→worst): "**EquiformerV2 + DeNS > Orb > SevenNet > MACE > CHGNet > M3GNet > ALIGNN > MEGNet > CGCNN > CGCNN+P > Wrenformer > BOWSR > Voronoi fingerprint random forest**"

> "UIPs emerge as the top performers, achieving **F$_1$ scores of 0.57–0.82** and **discovery acceleration factors (DAF) of up to 6× on the first 10k stable predictions**"

> "**Accurate regressors can yield high false-positive rates near the decision boundary at 0 eV/atom above the convex hull**" — regression metric ≠ task metric

> "the WBM dataset consists of **257,487 structures**"

---

## 평가 metric 상세

| Metric | 의미 | 우선순위 |
|---|---|---|
| **F$_1$** | binary stable/unstable | Primary |
| **DAF** | discovery acceleration vs random | Primary |
| **Precision** | TP / (TP+FP), reduce wasted DFT calls | Primary |
| **Recall** | TP / (TP+FN), avoid missing stable materials | Primary |
| MAE (E_hull) | regression error | Secondary (misleading) |

→ **task-based 평가**를 강조 (regression metric은 부수적). 작은 MAE라도 decision boundary 근처에서 false positive 많을 수 있음.

---

## 주요 평가 결과 (논문 본문)

| Model | F$_1$ | DAF |
|---|---|---|
| Voronoi RF | (낮음) | – |
| MEGNet / CGCNN | (중간) | – |
| M3GNet | 0.57+ | ~3× |
| CHGNet, MACE, SevenNet, Orb | (높음) | – |
| **EquiformerV2 + DeNS** | **0.82** (top) | **6×** (top, first 10k) |

→ Universal Interatomic Potentials (UIP) > task-specific models > one-shot predictors

---

## 한계점
- **WBM 데이터셋 한계**: 합성된 구조 → 실험 검증 미반영
- **Regression vs classification 갈등**: 작은 MAE도 boundary near false positive
- **DFT functional 의존**: PBE 기반 ground truth, 다른 functional과 격차
- **Stable ≠ synthesizable**: 열역학적 stability만 평가, 합성 경로/속도론 미반영
- **Open Catalyst 등 다른 도메인 미포함**: 표면, 분자 미커버
- **데이터 leakage 위험**: 일부 모델이 WBM 인접 구조로 학습되었을 가능성

---

## 관련 정보
- **논문 (Nature MI)**: [10.1038/s42256-025-01055-1](https://doi.org/10.1038/s42256-025-01055-1)
- **arXiv**: [2308.14920](https://arxiv.org/abs/2308.14920)
- **공식 사이트**: [matbench-discovery.materialsproject.org](https://matbench-discovery.materialsproject.org/)
- **Python package**: `pip install matbench-discovery`
- **GitHub**: [janosh/matbench-discovery](https://github.com/janosh/matbench-discovery)
- **WBM 데이터셋**: Wang et al. 2021 npj CompMat (Matbench Discovery의 test corpus)
- **이 benchmark를 사용한 후속 작업**: MLIP Arena (NeurIPS 2025 D&B), foundation MLIP papers
