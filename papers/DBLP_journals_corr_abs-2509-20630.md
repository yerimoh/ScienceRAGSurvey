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

## 실제 데이터 형식 예시 (논문 §2 + Figure 1 + Table 1)

### 유형 A — Asymptotic Behaviors (EOS + diatomic PEC)

> **EOS benchmark**: 1,000 WBM crystal structures, V/V₀ scan
>
> ```
> Input:     periodic crystal at varied volumes
> Predict:   E(V/V₀) — should follow Birch–Murnaghan EOS
> Metrics (DFT-agnostic):
>   - Derivative flips ↓  (smooth PEC should have 1)
>   - Tortuosity ↓        (arc-chord ratio, ideal = 1)
>   - Spearman ρ at compression: → -1 (monotonic)
>   - Spearman ρ at tension: → +1
>   - Missing predictions (NaN/divergence) ↓
> ```
>
> **Diatomic PEC**: homonuclear pairs across periodic table
> - 0.9 × r_cov ~ 3.1 × r_vdw 거리 범위 스캔
> - Top Matbench Discovery 모델이 종종 실패 → "apparent benchmark success may result from plausible many-body error cancellation"

### 유형 B — Stability & Reactivity (MD on RM24)

> **NVT MD**: 120 random amorphous mixture structures (RM24)
> ```
> Thermostat: Nosé-Hoover NVT
> Temperature: linear 300 K → 3000 K
> Duration: 10 ps
> Metric: # valid trajectories, MD steps per second (SPS)
>         SPS = a·N^b  (asymptotic scaling)
> ```
>
> **NPT MD**: 80 RM24 structures
> ```
> Thermostat: Nosé-Hoover NPT
> Temperature: 300 K → 3000 K
> Pressure: 0 GPa → 500 GPa (linear ramp)
> Duration: 10 ps
> ```
>
> **Reactivity test** (hydrogen combustion):
> ```
> 1 ns annealing MD (2 × 10⁶ steps, 0.5 fs)
> H + O system: 300 K → 3000 K → 300 K
> Monitor: # H₂O formed, ΔH, bond breaking/formation
> ```

### 유형 C — EOS Benchmark Results (Table 1)

> 1,000 WBM structures, lower=better (deviation from ideal physics)
>
> | Model | Derivative flips ↓ | Tortuosity ↓ | E compression ρ ↓ | dE/dV compression ρ ↑ | Missing ↓ |
> |---|---|---|---|---|---|
> | **MACE-MPA** | **1.037** | **1.005** | **-0.999** | **0.996** | **2** |
> | eSEN | 1.042 | 1.008 | -0.999 | 0.997 | 5 |
> | MACE-MP(M) | 1.042 | 1.009 | -0.999 | 0.994 | 5 |
> | MatterSim | 1.045 | 1.006 | -0.997 | 0.993 | 3 |
> | CHGNet | 1.105 | 1.015 | -0.996 | 0.993 | 3 |
> | SevenNet | 1.109 | 1.019 | -0.998 | 0.989 | 3 |
> | M3GNet | 1.175 | 1.018 | -0.996 | 0.990 | 5 |
> | ORBv2 | 1.316 | 1.037 | -0.992 | 0.970 | 7 |
>
> → **Matbench Discovery 상위 모델** ≠ EOS 상위 모델 (force smoothness ≠ energy regression)

### 유형 D — 4-category benchmark structure

> ```
> ┌─────────────────────────────────────────────────┐
> │ A. Asymptotic Behaviors                          │
> │    · EOS (1,000 WBM crystals)                    │
> │    · Diatomic PEC (homonuclear, periodic table)  │
> │    Metrics: smoothness, repulsion, conservation  │
> │                                                  │
> │ B. Stability & Reactivity                        │
> │    · MD on RM24 (NVT 120 + NPT 80 structures)    │
> │    · H₂ combustion 1 ns annealing                 │
> │    Metrics: valid steps, SPS, ΔH                  │
> │                                                  │
> │ C. Distribution Shifts                           │
> │    · Energy conservation drift                   │
> │    · Force rotational equivariance               │
> │    Metrics: drift/error in differential-entropy bins │
> │                                                  │
> │ D. Thermodynamic Properties                      │
> │    · Phonon spectra                              │
> │    · Equation of state                           │
> │    · Free energy, elastic constants              │
> └─────────────────────────────────────────────────┘
> ```
>
> Models evaluated: **MACE-MP(M), CHGNet, M3GNet, MatterSim, ORBv2, SevenNet, MACE-MPA, eSEN** (Table S4)
> Workflow: Prefect orchestration · Parquet/JSON/ASE DB storage · GitHub submission

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
