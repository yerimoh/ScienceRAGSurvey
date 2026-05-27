---
title: "MLIP Arena: Open Benchmark Platform for Machine Learning Interatomic Potentials"
bib_key: "DBLP:journals/corr/abs-2509-20630"
year: 2025
domain: material, chem, physics
type: benchmark
venue: NeurIPS 2025 Datasets & Benchmarks
paper_link: https://arxiv.org/abs/2509.20630
---
# MLIP Arena: Physics-aware MLIP Benchmark beyond DFT-error Metrics

> NeurIPS 2025 Datasets & Benchmarks Track | Benchmark (foundation MLIP physics-aware evaluation) | material · chem · physics
> Yuan Chiang, Tobias Kreiman, Christine Zhang, Matthew C. Kuner, Elizabeth Weaver, Ishan Amin, Hyunsoo Park, Yunsung Lim, Jihan Kim, Daryl Chrzan, Aron Walsh, Samuel M. Blau, Mark Asta, Aditi S. Krishnapriyan — UC Berkeley / LBNL / Imperial / KAIST
> DBLP: `journals/corr/abs-2509-20630` · arXiv: [2509.20630](https://arxiv.org/abs/2509.20630)

## 한 줄 요약
**Foundation MLIP (machine learning interatomic potential)** 을 **DFT-error metric 기반이 아닌 physics-aware 기반**으로 평가하는 open benchmark platform. **dynamical stability, gas adsorption, phase transition, vacancy migration** 등 downstream 물리 task 중심. Matbench Discovery의 약점 (error metric vulnerable to data leakage) 보완.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문제 인식: 기존 MLIP benchmark의 약점
  ┌──────────────────────────────────────────────┐
  │ 1. Data leakage (Matbench Discovery 등)       │
  │    → energy 과적합 → force/finite-T 부정확   │
  │ 2. Static dataset → 새 데이터셋 등장 시 무용 │
  │ 3. Error-based metric ≠ practical utility    │
  │    → 일부 MLIP는 ground-state error 낮으나   │
  │       phonon/transport에서 실패              │
  └──────────────────────────────────────────────┘

Step 2 — Physics-aware task 설계 (4 카테고리)
  ┌─────────────────────────────────────┐
  │ A. Asymptotic Behaviors             │
  │    - 비물리적 force divergence 검출  │
  │                                      │
  │ B. Stability & Reactivity           │
  │    - Dynamical stability             │
  │    - Phase transition                │
  │    - Vacancy migration               │
  │    - Gas adsorption                  │
  │                                      │
  │ C. Distribution Shifts              │
  │    - 학습 데이터 밖 chemistry        │
  │                                      │
  │ D. Thermodynamic Properties         │
  │    - phonon spectra                  │
  │    - elastic constants               │
  │    - free energy                     │
  └─────────────────────────────────────┘

Step 3 — Platform infrastructure
  ┌──────────────────────────────────────────────┐
  │ - Python package (open source)               │
  │   `pip install mlip-arena`                   │
  │ - Online leaderboard                         │
  │ - Workflow orchestration (Parquet, JSON,     │
  │   ASE DB)                                    │
  │ - Submission via GitHub                      │
  └──────────────────────────────────────────────┘

Step 4 — Evaluation philosophy
  · Physics priors 존중 (symmetry, conservation)
  · Failure-mode 노출 (실패 상황을 명시적 시각화)
  · Reproducibility (random seed, hyperparameter)
  · Multi-DFT reference (PBE/SCAN/HSE 등 비교)
```

---

## 원문 직접 인용 (arXiv:2509.20630 §Abstract + §1)

> "We introduce **MLIP Arena, a benchmark platform that evaluates force field performance based on physics awareness, chemical reactivity, stability under extreme conditions, and predictive capabilities for thermodynamic properties** and physical phenomena"

> "Existing benchmarks suffer from **data leakage, limited transferability, and an over-reliance on error-based metrics tied to specific density functional theory (DFT) references**"

> 4 카테고리: "**Asymptotic Behaviors / Stability and Reactivity / Distribution Shifts / Thermodynamic Properties**" + 구체적 phenomena "**Dynamical stability, Gas adsorption, Phase transition, Vacancy migration**"

> Matbench Discovery 비판: "non-compliant models rank highly for crystal stability metrics due to **energy overfitting at the expense of forces and finite-temperature capabilities**"

> Available: **https://github.com/atomind-ai/mlip-arena**

---

## 평가 framework

| Metric category | 내용 |
|---|---|
| **Physics awareness** | Symmetry preservation, energy conservation, force smoothness |
| **Chemical reactivity** | Bond breaking, transition state |
| **Stability under extreme conditions** | High T/P, defect, surface |
| **Thermodynamic predictions** | Phonons, elastic, gas adsorption, free energy |
| **Distribution shift** | OOD chemistry generalization |

→ DFT energy MAE/MAEF 같은 단순 error metric은 **secondary**.

---

## 주요 발견 (논문 본문)

| 관찰 | 의미 |
|---|---|
| Top Matbench Discovery model이 phonon에서 실패 | error metric의 한계 |
| Foundation MLIP들이 OOD chemistry에 transferability 부족 | 학습 데이터 dependence |
| Symmetry-breaking 발견 | physical prior 위반 |
| Force smoothness vs energy accuracy trade-off | PES landscape 품질 |

→ **결론**: MLIP foundation model 평가는 **physics-aware task** 기반이어야 함.

---

## 한계점
- **2025년 NeurIPS D&B submission**: 최종 leaderboard 진행 중
- **Foundation MLIP만 대상**: classical FF, specific-task MLIP 미커버
- **Task 수 제한**: ~수십 개 카테고리, 더 확장 필요
- **DFT reference 다양성**: PBE 위주, advanced functional 미충분
- **계산 비용**: physics-aware test가 단순 error metric보다 훨씬 무거움
- **CPU/GPU 다양성**: 다양한 hardware에서 정확도 일관성 검증 필요

---

## 관련 정보
- **arXiv**: [2509.20630](https://arxiv.org/abs/2509.20630)
- **DBLP**: [journals/corr/abs-2509-20630](https://dblp.org/rec/journals/corr/abs-2509-20630.html)
- **GitHub**: [atomind-ai/mlip-arena](https://github.com/atomind-ai/mlip-arena)
- **Python package**: `pip install mlip-arena`
- **공식 사이트**: [atomind.ai/mlip-arena](https://atomind.ai/mlip-arena/) (예정)
- **Venue**: NeurIPS 2025 Datasets & Benchmarks
- **저자 소속**: UC Berkeley / LBNL / Imperial College London / KAIST
- **관련 benchmarks**: Matbench Discovery (Riebesell 2025 NMI, beats), JARVIS-Leaderboard (Choudhary 2024 npj CompMat), AdsorbML (Lan 2023 npj CompMat)
