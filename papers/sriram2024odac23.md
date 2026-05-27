---
title: "The Open DAC 2023 Dataset and Challenges for Sorbent Discovery in Direct Air Capture"
bib_key: "sriram2024odac23"
year: 2024
domain: material, chem
type: benchmark
venue: ACS Central Science
paper_link: https://doi.org/10.1021/acscentsci.3c01629
---
# ODAC23: 8,400 MOFs × 38M DFT for Direct-Air-Capture Sorbent Discovery

> ACS Central Science 10:923–941 | 2024 | Benchmark + Dataset (DFT-verified MOF sorbent screening) | material · chem
> Anuroop Sriram, Sihoon Choi, Xiaohan Yu, Logan M. Brabson, Abhishek Das, Zachary Ulissi, Matt Uyttendaele, Andrew J. Medford, David S. Sholl — Meta FAIR / Georgia Tech / ORNL
> arXiv: [2311.00341](https://arxiv.org/abs/2311.00341) · DOI: [10.1021/acscentsci.3c01629](https://doi.org/10.1021/acscentsci.3c01629)

## 한 줄 요약
**직접 공기 포집(Direct Air Capture, DAC)**용 **금속-유기 골격체(MOF)** 후보 탐색을 위한 **38M+ DFT calculation × 8,400+ MOF benchmark**. 입력은 MOF + adsorbate(CO₂, H₂O) 구조이며, **OC20과 동일한 3-task 정의 (S2EF / IS2RE / IS2RS)**로 ML 모델을 평가. MOF adsorption DFT 데이터로는 현재 **가장 큰 공개 데이터셋**.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 과학적 동기
  ┌──────────────────────────────────────────────┐
  │ - Annual CO₂ emission ~36B tonnes (2020)     │
  │ - Atmospheric CO₂ +50% since preindustrial   │
  │   → ~420 ppm                                 │
  │ - DAC: ambient-condition negative emissions  │
  │ - MOFs: modular, tunable, high porosity      │
  │   → ideal customizable sorbents              │
  │ - 문제: vast chemical space + humidity/temp  │
  │   dependence → 효율적 screening 필요          │
  └──────────────────────────────────────────────┘

Step 2 — MOF corpus 구성 (8,400+ frameworks)
  ┌──────────────┬────────┬───────────────────────┐
  │ Set          │ Count  │ Source                │
  ├──────────────┼────────┼───────────────────────┤
  │ Pristine MOFs│ 4,942  │ CoRE MOF + curated    │
  │ Defective MOFs│ 3,470  │ defect 1–16% 농도     │
  │ Ultrastable   │   114  │ Nandy fragmented +   │
  │              │        │ recombined            │
  └──────────────┴────────┴───────────────────────┘
  · 57 metals (Zn / Cu / Cd 최다)
  · monometallic 89% / bimetallic 10.7% / 
    trimetallic <1%

Step 3 — Adsorbate placement
  · Classical FF + Monte Carlo sampling
  · ~2–6 placements per framework
  · CO₂ only / H₂O only / CO₂ + H₂O / CO₂ + 2H₂O

Step 4 — DFT 계산 규모
  ┌──────────────────────────────────────────────┐
  │ - 38M+ single-point DFT calculations         │
  │ - 170K converged adsorption energies          │
  │ - ~400M core-hours compute                    │
  │ - largest MOF-adsorption DFT dataset to date │
  └──────────────────────────────────────────────┘

Step 5 — Benchmark task 정의 (OC20-style)
  ┌─────────────────────────────────────────────┐
  │ S2EF (Structure → Energy + Forces)           │
  │  · 입력: MOF+adsorbate single structure      │
  │  · 출력: Ẽ_ads + per-atom forces             │
  │                                              │
  │ IS2RE (Initial Structure → Relaxed Energy)  │
  │  · 입력: 초기 placement (non-relaxed)        │
  │  · 출력: 최종 relaxed adsorption energy      │
  │                                              │
  │ IS2RS (Initial Structure → Relaxed Struct)  │
  │  · 입력: 초기 placement                       │
  │  · 출력: 최종 relaxed 3D coordinates         │
  └─────────────────────────────────────────────┘

Step 6 — Adsorption energy 정의
  Ẽ_ads = E_system − E_MOF − n_CO2·E_CO2 − n_H2O·E_H2O
  (tilde = not necessarily relaxed)

Step 7 — Promising MOF 식별 (downstream verification)
  · ODAC23 안에서 직접 promising MOF 발굴
  · Single + co-adsorption energy 분석
  · Adsorbate-adsorbate interaction energy 계산
```

---

## 실제 데이터 형식 예시 (논문 §Tasks + §Results + Table S3)

### 유형 A — S2EF input/output (Structure → Energy + Forces)

> **Input** (periodic unit cell):
> ```
> MOF (e.g., CoRE-MOF 코드 ZIDBEV, IMAGAG, IPIDUH)
>   + adsorbate placement: 1 × CO2 또는 1 × H2O 또는 1 × CO2 + 1 × H2O
>   + initial positions from classical FF + Monte Carlo
> ```
>
> **Output** (DFT ground truth, PBE-D3 functional):
> ```
> Ẽ_ads (non-relaxed adsorption energy, eV)
> Forces per atom (eV/Å, 3D vector)
> ```
>
> **Adsorption energy 정의**:
> ```
> Ẽ_ads = E_system − E_MOF − n_CO2·E_CO2 − n_H2O·E_H2O
> ```

### 유형 B — IS2RE / IS2RS (Initial → Relaxed)

> **IS2RE**: initial placement → final relaxed adsorption energy E_ads
> **IS2RS**: initial placement → final relaxed 3D coordinates of all atoms
>
> 표준 OC20-style train/test split, MOF framework로 stratified
> (pristine 구조와 그 defective version이 같은 split에 배치)

### 유형 C — Promising DAC MOF 예시 (논문 Table S3 / Fig. 3)

> Top promising MOFs identified directly in ODAC23 by DFT:

| CSD code | E_ads(CO₂) − E_ads(H₂O) | Adsorbate-adsorbate E |
|---|---|---|
| **ZIDBEV** | 강한 CO₂ binding | E_inter_mol ≈ 0 eV (separate adsorption OK) |
| **IMAGAG** | favors CO₂+H₂O 공존 | E_inter_mol = −0.64 eV |
| **IPIDUH** | CO₂+H₂O 비호환 | E_inter_mol = +1.04 eV |
| **TUGTAR** | CO₂+H₂O 비호환 | E_inter_mol = +0.51 eV |
| **KOQLUZ** | 강한 MOF 재배열 | E_inter_mol = −2.31 eV |
| **LEWZET** | 두 번째 H₂O 흡착 시 distortion | 2nd E_inter_mol = −5.48 eV |

>
> **선별 기준** (Findley & Sholl):
> - E_ads(CO₂) < −0.5 eV (sufficient binding at dilute DAC conditions)
> - E_ads(CO₂) 가 E_ads(H₂O) 보다 favorable (CO₂ over water)
>
> → 5,079 pristine MOF 중 **135개**가 두 기준 모두 충족 (classical FF로는 0개)

### 유형 D — Dataset 규모 분포 (논문 §Methods)

> ```
> ┌──────────────────────────┬───────────┐
> │ Pristine MOFs            │   4,942   │
> │ Defective MOFs (1–16%)   │   3,470   │
> │ Ultrastable (Nandy frag) │     114   │
> ├──────────────────────────┼───────────┤
> │ Total MOFs               │   8,400+  │
> │ Adsorbate placements/MOF │   2–6     │
> │ Converged adsorption E   │ 170,000+  │
> │ Single-point DFT calc    │  38M+     │
> │ Compute (core-hours)     │ 400M+     │
> └──────────────────────────┴───────────┘
> ```
>
> Metals: 57 species · monometallic 89% / bimetallic 10.7% / trimetallic <1%
> Most common: Zn, Cu, Cd

---

## 평가 framework

| Task | Input | Output | Primary Metric |
|---|---|---|---|
| **S2EF** | MOF+adsorbate single config | Ẽ_ads + forces | Energy MAE + Force MAE |
| **IS2RE** | initial (non-relaxed) | relaxed E_ads | Energy MAE within 20 meV/atom |
| **IS2RS** | initial (non-relaxed) | relaxed 3D structure | RMSD vs DFT-relaxed |
| **Adsorbate-adsorbate interaction** | CO₂+H₂O combined | E_inter_mol | qualitative ranking |
| **Co-adsorption energy** | CO₂+H₂O joint vs separate | favorability ranking | DFT ground truth |

→ OC20/OC22 with the **same evaluation protocol** → MOF/DAC domain으로 확장

---

## 주요 결과 (논문 §Results)

| 발견 | 의미 |
|---|---|
| MOFs with various adsorbate-adsorbate interactions identified | ZIDBEV (E=0), IMAGAG (-0.64 eV), IPIDUH (1.04 eV) 등 |
| Co-adsorption distortion 효과 | LEWZET 2nd H₂O 시 -5.48 eV (MOF distortion) |
| Direct identification of promising DAC MOFs | downstream FF screening 불필요 |
| FF-based screening 한계 노출 | open-metal site / defect에서 FF 부정확 |
| ML models trained on ODAC23 | DFT-level 근사로 high-throughput screening 가능 |

→ **결론**: ML + ODAC23 = DAC sorbent discovery의 **scalable in-silico verification platform**

---

## 한계점
- **DFT functional dependence**: PBE-based, 다른 functional과 격차
- **OC20-style framework**: liquid/gas phase 외 confined geometry 한정
- **Adsorbate 한정**: CO₂, H₂O만 (다른 기체 미커버)
- **Compute cost**: 400M core-hours 재현 불가
- **Class imbalance**: monometallic 89% → bimetallic/trimetallic 데이터 sparse
- **Defect concentration 1–16%**: amorphous / heavily-defective MOF 미커버
- **시간**: 2023 cutoff, 후속 ODAC24/25 등장 시 비교 필요

---

## 관련 정보
- **논문 (ACS Central Sci.)**: [10.1021/acscentsci.3c01629](https://doi.org/10.1021/acscentsci.3c01629)
- **arXiv**: [2311.00341](https://arxiv.org/abs/2311.00341)
- **공식 사이트**: [opencatalystproject.org](https://opencatalystproject.org/) (Open DAC subset)
- **GitHub**: [Open-Catalyst-Project/ocp](https://github.com/Open-Catalyst-Project/ocp)
- **저자 소속**: Meta FAIR / Georgia Tech / ORNL
- **이 dataset을 사용한 후속 작업**: OMat24 (Meta 2024, OpenDAC를 design 참조), MLIP Arena gas-adsorption task
- **관련 데이터셋**: OC20 (Chanussot 2021), OC22 (Tran 2023), OMat24 (Barroso-Luque 2024), CoRE MOF database (Chung 2014)
