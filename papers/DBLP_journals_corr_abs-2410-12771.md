---
title: "Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models"
bib_key: "DBLP:journals/corr/abs-2410-12771"
year: 2024
domain: material, chem, physics
type: benchmark
venue: arXiv (Meta FAIR Tech Report)
paper_link: https://arxiv.org/abs/2410.12771
---
# OMat24: 110M-DFT MLIP Training & Evaluation Suite (Matbench Discovery F1 > 0.9)

> arXiv 2024 (Meta FAIR Technical Report) | Benchmark + Dataset + Models (foundation MLIP) | material · chem · physics
> Luis Barroso-Luque, Muhammed Shuaibi, Xiang Fu, Brandon M. Wood, Misko Dzamba, Meng Gao, Ammar Rizvi, Matt Uyttendaele, C. Lawrence Zitnick, Zachary W. Ulissi — Fundamental AI Research (FAIR) at Meta
> arXiv: [2410.12771](https://arxiv.org/abs/2410.12771) · CoRR: `journals/corr/abs-2410-12771`

## 한 줄 요약
무기 재료(inorganic material)용 **110M+ DFT calculation 공개 데이터셋** + **EquiformerV2/eSEN MLIP 모델 체크포인트** + **Matbench Discovery 평가 프로토콜**을 묶은 large-scale training+benchmark suite. 기존 데이터의 약 100배 규모이며, **F1 > 0.9 (stability)**, **MAE 20 meV/atom (formation energy)** 달성. **공개된 모든 leaderboard top model이 OMat24 채택**.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문제 인식: open MLIP training data 부족
  ┌──────────────────────────────────────────────┐
  │ "the state-of-the-art in openly available    │
  │  and reproducible datasets and models        │
  │  lagged behind proprietary models"           │
  │ + MPTrj/MPF 같은 기존 dataset은 equilibrium  │
  │   위주, far-from-equilibrium 부족             │
  └──────────────────────────────────────────────┘

Step 2 — OMat24 dataset 구성
  ┌──────────────────────────────────────────────┐
  │ - 110M+ single-point DFT calculations         │
  │ - 118M structures total (energy, forces,      │
  │   cell stress labels)                          │
  │ - 1–100 atoms per structure                    │
  │   (majority < 20 atoms from Alexandria)        │
  │ - Source: Alexandria base + AIMD sampling +   │
  │   non-equilibrium perturbations                │
  │ - DFT settings designed for compatibility     │
  │   with MPtrj/Materials Project                 │
  └──────────────────────────────────────────────┘

Step 3 — Three core design principles
  · Scale: ~2 orders of magnitude > 기존 open dataset
  · Diversity: periodic table 전반 + far-from-equilibrium
  · Open-science: CC-by license, full reproducibility

Step 4 — Pretrained MLIP 모델
  · EquiformerV2 variants (Liao 2023, 2024)
  · eSEN variants (Fu 2024)
  · Pretrained on OMat24, fine-tuned for MPtrj
    DFT-settings compatibility

Step 5 — Evaluation protocol
  ┌──────────────────────────────────────────────┐
  │ 1. Matbench Discovery (WBM 257K structures)   │
  │    → F1, DAF, precision, recall, MAE          │
  │ 2. Thermal conductivity / phonon benchmarks   │
  │    (newly introduced)                          │
  │ 3. Softening bias quantification              │
  │    (energy/force/derivative systematic        │
  │     underestimation correction)                │
  └──────────────────────────────────────────────┘

Step 6 — 공개 자원
  · Dataset: HuggingFace fairchem/OMAT24 (CC-by-4.0)
  · Models: HuggingFace fairchem/OMAT24
  · Code: github.com/FAIR-Chem/fairchem (MIT)
```

---

## 원문 직접 인용 (arXiv:2410.12771 §Abstract + §1 + §2)

> "we present the **Open Materials 2024 (OMat24) dataset, comprising over 110M DFT calculations** across diverse chemistries, materials, and configurations."

> "MLIP models trained on OMat24 achieve leading performance on the **Matbench Discovery leaderboard, surpassing previous models with F1 scores above 0.9 for stability and 20 meV/atom accuracy for formation energy**."

> "Models trained on OMat24 also exhibit the highest accuracy in newly developed **thermal conductivity and phonon prediction task benchmarks**."

> "OMat24's diversity **corrects the consistent softening bias of prior models trained on less diverse datasets**, which systematically underpredicted energy, forces, and derivative properties like phonons."

> "The OMat24 dataset includes a total of **118 million structures labeled with energy, forces and cell stress**. The number of atoms per structure ranges from **1 to 100 atoms per structure**." (§2.1)

> Three design principles: "**Scale**: OMat24 is a large-scale public ab-initio training dataset for inorganic materials **up to 2 orders of magnitude larger than other openly available datasets** in terms of number of single-point calculations. **Diversity**: OMat24 has compositional diversity across the periodic table thanks to community efforts to prototype and catalog hypothetical materials, and contains a large fraction of far-from-equilibrium structures. **Open-science**: OMat24 is released under a permissive CC-by license." (§2.1)

> "**Since its release, all top models on the leaderboard have adopted the dataset.**" (§1)

---

## 평가 framework

| Benchmark | Metric | 의미 |
|---|---|---|
| **Matbench Discovery** | F$_1$ (stability) | binary stable/unstable WBM 257K |
| **Matbench Discovery** | MAE (formation E) | regression eV/atom |
| **Matbench Discovery** | DAF | discovery acceleration |
| **Phonon prediction** | newly added | force-derivative property |
| **Thermal conductivity** | newly added | transport property |
| **Softening bias** | systematic error magnitude | energy/force/phonon underestimation |

→ OMat24 train 모델: F$_1$ > 0.9, MAE = 20 meV/atom (Matbench Discovery top)

---

## 주요 결과 (논문 §2 + Tables)

| Metric | OMat24-trained 모델 | 의미 |
|---|---|---|
| Matbench F$_1$ (stability) | **> 0.9** | 이전 best 대비 향상 |
| Formation E MAE | **20 meV/atom** | DFT-level 정확도 |
| Softening bias | 사라지거나 reduce됨 | non-equilibrium 학습 효과 |
| Phonon prediction | highest accuracy | force-derivative 정확 |
| Architecture | EquiformerV2, eSEN | 동일 데이터로 다른 아키텍처도 향상 |

→ **결론**: dataset diversity (특히 far-from-equilibrium)가 MLIP 정확도 결정적, 모든 leaderboard top model이 OMat24를 채택.

---

## 한계점
- **DFT settings compatibility**: MPtrj와 다른 functional/parameter → fine-tuning 필요
- **Inorganic bulk material 한정**: 분자, 표면, 인터페이스 미커버
- **License**: dataset CC-by, model checkpoint custom license
- **Compute requirement**: 110M DFT 계산은 reproducibility를 제한
- **Static dataset**: 후속 OMat25/26 등장 시 비교 필요
- **시간**: 2024 cutoff (논문 명시 2026-05-21 revision)

---

## 관련 정보
- **arXiv**: [2410.12771](https://arxiv.org/abs/2410.12771)
- **DBLP**: [journals/corr/abs-2410-12771](https://dblp.org/rec/journals/corr/abs-2410-12771.html)
- **Dataset**: [huggingface.co/datasets/fairchem/OMAT24](https://huggingface.co/datasets/fairchem/OMAT24) (CC-by-4.0)
- **Models**: [huggingface.co/fairchem/OMAT24](https://huggingface.co/fairchem/OMAT24)
- **GitHub**: [FAIR-Chem/fairchem](https://github.com/FAIR-Chem/fairchem) (MIT)
- **저자 소속**: Meta FAIR
- **이 dataset을 사용한 후속 작업**: Matbench Discovery top models (모두 OMat24 채택), MLIP Arena (NeurIPS 2025 D&B)
- **관련 데이터셋**: MPtrj (Deng 2023), Alexandria (Schmidt 2024), Materials Project, OC20 (Chanussot 2021), OC22, ODAC23
