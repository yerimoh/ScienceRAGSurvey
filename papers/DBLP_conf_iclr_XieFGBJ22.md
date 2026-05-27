---
title: "Crystal Diffusion Variational Autoencoder for Periodic Material Generation"
bib_key: "DBLP:conf/iclr/XieFGBJ22"
year: 2022
domain: material, chem, physics
type: benchmark
venue: ICLR 2022
paper_link: https://arxiv.org/abs/2110.06197
---
# CDVAE: 3-Dataset Crystal Generation Benchmark (Perov-5 / Carbon-24 / MP-20)

> ICLR 2022 | Benchmark (periodic material generation) + Method | material · chem · physics
> Tian Xie, Xiang Fu, Octavian-Eugen Ganea, Regina Barzilay, Tommi Jaakkola — MIT CSAIL
> arXiv: [2110.06197](https://arxiv.org/abs/2110.06197) · OpenReview: [03RLpj-tc_](https://openreview.net/forum?id=03RLpj-tc_)

## 한 줄 요약
주기 결정 구조 생성(periodic material generation)을 위한 **3-dataset standard benchmark** (Perov-5 18,928[^perov] / Carbon-24 10,153[^carbon] / MP-20)와 **3-task evaluation suite** (Reconstruction, Generation, Property Optimization)를 제안. 평가 지표로 **Validity, Coverage (COV-R / COV-P), Property statistics (EMD)**[^metrics]를 도입해 이전 method들의 비교 불가능 문제를 해결.

[^perov]: arXiv:2110.06197 §5: "**Perov-5** (Castelli et al., 2012) includes **18928 perovskite materials** that share the same structure but differ in composition. There are **56 elements** and all materials have **5 atoms in the unit cell**."
[^carbon]: arXiv:2110.06197 §5: "**Carbon-24** (Pickard, 2020) includes **10153 materials** that are all made up of carbon atoms but differ in structures. There is **1 element** and the materials have **6 - 24 atoms** in the unit cells."
[^metrics]: arXiv:2110.06197 §5.2: "1) **Validity**. ... shortest distance between any pair of atoms is larger than 0.5 Å ... 2) **Coverage (COV)**. ... **COV-R (Recall) and COV-P (Precision)** ... 3) **Property statistics**. We compute the **earth mover's distance (EMD)** ... density (ρ), energy (E), and number of unique elements (# elem.)"

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문제 인식: material generation 평가의 비표준
  ┌──────────────────────────────────────────────┐
  │ "Past studies in this field used very       │
  │  different tasks and metrics, making it     │
  │  difficult to compare different methods"     │
  │  → standard tasks / datasets / metrics 필요 │
  └──────────────────────────────────────────────┘

Step 2 — 3 standard datasets curation (QM simulations 기반)
  ┌──────────────┬─────────┬──────────────────────────┐
  │ Dataset      │ # mater │ 특성                     │
  ├──────────────┼─────────┼──────────────────────────┤
  │ Perov-5      │ 18,928  │ 56 elements / 5 atoms/cell │
  │              │         │ same structure (perovskite)│
  │ Carbon-24    │ 10,153  │ 1 element (C) / 6–24 atoms│
  │              │         │ different structures       │
  │ MP-20        │ ~45,000 │ Materials Project ≤ 20 atoms│
  │              │         │ diverse compositions       │
  └──────────────┴─────────┴──────────────────────────┘

Step 3 — 3 standard tasks
  ┌─────────────────────────┬───────────────────────────────┐
  │ Task                    │ 평가 대상                       │
  ├─────────────────────────┼───────────────────────────────┤
  │ 1. Reconstruction       │ latent z → original 구조 복원 │
  │ 2. Generation           │ novel valid 구조 생성          │
  │ 3. Property Optimization│ target 속성 최적화 구조 생성  │
  └─────────────────────────┴───────────────────────────────┘

Step 4 — 평가 지표 (실제 QM 계산 비용 회피)
  · Validity:
    - structure: min pairwise distance > 0.5 Å
    - composition: SMACT charge neutrality
  · Coverage (COV-R / COV-P): generated vs test set 분포 일치
  · Property statistics (EMD):
    - density (g/cm³), GNN-predicted energy (eV/atom), # elements
  · Property optimization: top-5/10/15 percentile success rate
  · Sample size: 10,000 random generations for validity/coverage
                 1,000 valid for property statistics

Step 5 — Baselines 비교
  · Cond-DFC-VAE (Court 2020): cubic perovskite 만 가능
  · FTCP (Ren 2020): 절대 좌표 직접 encoding
  · G-SchNet (Gebauer 2019): 분자용 autoregressive
  · P-G-SchNet: G-SchNet에 periodicity 추가
```

---

## 실제 데이터 형식 예시 (논문 §5 + Figure 3)

### 유형 A — Perov-5 (페로브스카이트 5-atom unit cell)

> **Composition**: ABX₃ 페로브스카이트 구조 (모두 동일한 cubic perovskite 구조, 조성만 다름)
>
> **예시 entry** (논문 Figure 3 Ground Truth):
> ```
> Formula:    F-N-V-Rh-O-O      (5 atoms)
> Structure:  cubic perovskite (5-atom unit cell)
> # elements: 4  (F, N, V, Rh, O 중 4종)
> ```
>
> 총 **18,928 materials × 56 elements** — 모두 동일 구조, 조성 다양성만 평가.

### 유형 B — Carbon-24 (탄소-only allotrope)

> **Composition**: 순수 탄소 (1 element)만 사용
>
> **예시 entry** (논문 Figure 3 Ground Truth):
> ```
> Formula:    C₂₄        (또는 6 ≤ N ≤ 24 atoms)
> Structure:  diamond, graphite, lonsdaleite, 등 다양한 allotrope
> Constraint: 모두 carbon, 다양한 3D bonding network
> ```
>
> 총 **10,153 materials × 1 element** — 동일 조성, 구조 다양성만 평가.

### 유형 C — MP-20 (Materials Project ≤ 20 atoms)

> **Composition**: Materials Project 전체에서 unit cell ≤ 20 atoms인 entry
>
> **예시 entries** (논문 Figure 3 Ground Truth):
> ```
> Sn-Zr-O-F-O              (5 atoms, mixed cation+anion)
> Ba-Ru-O                  (3 atoms, perovskite-like)
> Ti-V-S × N (TiTiS + Na-S) (다중 cation sulfide)
> Eu-O-Sb-O × N            (rare-earth oxide)
> Mg-Al-Si-Si-Al-Al        (intermetallic)
> ```
>
> 총 **~45,000 materials** — 조성·구조·element 다양성 모두 평가 (가장 도전적인 dataset).

### 평가 sample 규모 (validity / coverage / property statistics)

> **Validity & Coverage 측정**:
> ```
> Sample: 10,000 materials randomly sampled from N(0, I) latent
> Validity 기준:
>   - Structure: min pairwise atom distance > 0.5 Å
>   - Composition: SMACT charge neutrality
> ```
>
> **Property statistics 측정**:
> ```
> Sample: 1,000 valid materials (validity test pass한 것 중 random)
> EMD over: density ρ (g/cm³), GNN-predicted E (eV/atom), # elements
> ```
>
> Ground truth validity baseline:
> - structure: 100.0% (모든 dataset)
> - composition: Perov-5 98.60%, Carbon-24 100.0%, MP-20 91.13%

---

## 평가 framework 요약

| Metric | 의미 | 단위 |
|---|---|---|
| **Validity (structure)** | min pairwise distance > 0.5 Å | binary (%) |
| **Validity (composition)** | SMACT charge neutrality | binary (%) |
| **COV-R (Recall)** | test set이 generated에 의해 cover되는 비율 | % |
| **COV-P (Precision)** | generated 중 quality 높은 비율 | % |
| **EMD (density)** | g/cm³ 분포 차이 | Earth Mover's Distance |
| **EMD (energy)** | independent GNN E (eV/atom) 분포 차이 | EMD |
| **EMD (# elements)** | 원소 수 분포 차이 | EMD |
| **Property optimization SR** | top-5/10/15 percentile 도달율 | % (over 100 generations) |
| **Reconstruction match rate** | pymatgen StructureMatcher pass | % (stol=0.5, angle_tol=10, ltol=0.3) |
| **Reconstruction RMSE** | matched 구조 RMSE, ∛(V/N) 정규화 | normalized |

→ ground truth 100% validity vs Perov-5 98.60% / Carbon-24 100.0% / MP-20 91.13% composition validity (training 분포).

---

## 주요 결과 (논문 §5)

| Task | CDVAE 결과 | 의미 |
|---|---|---|
| Reconstruction | lowest RMSE among all models | latent → 구조 복원 가장 정확 |
| Generation (Validity) | significantly higher than baselines | NCSN diffusion이 안정 구조 학습 |
| Generation (Coverage) | better COV-R + COV-P | test 분포에 잘 매칭 |
| Property optimization | FTCP 능가, Perov-5에서 Cond-DFC-VAE와 비슷 | Carbon-24가 가장 어려움 |

→ "Both G-SchNet and P-G-SchNet are incapable of property optimization" — molecular adapation 한계 노출.

---

## 한계점
- **Validity의 약한 기준**: "0.5 Å" pairwise distance는 "relative weak criterion" (논문 자체 표현)
- **EMD-based property statistics**: GNN proxy energy, 실제 DFT 검증 미포함
- **3개 dataset 한정**: oxide, alloy, surface 등 미커버
- **VAE-based**: 후속 diffusion-based 모델 (DiffCSP, MatterGen 등) 출현
- **시간**: 2022 cutoff, 최신 foundation MLIP 평가 미포함

---

## 관련 정보
- **OpenReview**: [03RLpj-tc_](https://openreview.net/forum?id=03RLpj-tc_)
- **arXiv**: [2110.06197](https://arxiv.org/abs/2110.06197)
- **GitHub**: [txie-93/cdvae](https://github.com/txie-93/cdvae)
- **저자 소속**: MIT CSAIL
- **Venue**: ICLR 2022
- **이 benchmark를 사용한 후속 작업**: DiffCSP (Jiao 2023 NeurIPS), MatterGen (Zeni 2025 Nature), FlowMM (Miller 2024 ICML), SyMat — Perov-5/Carbon-24/MP-20 standard split 채택
