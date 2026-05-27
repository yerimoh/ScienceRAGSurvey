---
title: "f-RAG: Molecule Generation with Fragment Retrieval Augmentation"
bib_key: "DBLP:conf/nips/LeeKV0RPVN24"
year: 2024
domain: chem
type: Method
venue: NeurIPS 2024
paper_link: https://arxiv.org/abs/2411.12078
---
# f-RAG: Molecule Generation with Fragment Retrieval Augmentation

> NeurIPS 2024 | Method (docking-verified hypothesis) | chem
> Seul Lee, Karsten Kreis, Srimukh Prasad Veccham, Meng Liu, Danny Reidenbach, Saee Paliwal, Arash Vahdat, Weili Nie — KAIST / NVIDIA / AstraZeneca
> DBLP: `conf/nips/LeeKV0RPVN24` · arXiv: [2411.12078](https://arxiv.org/abs/2411.12078)

## 한 줄 요약
사전학습된 분자 생성 모델에 **fragment retrieval augmentation** (hard fragments + soft fragments)을 결합하고 **iterative refinement + genetic fragment modification** 으로 fragment vocabulary를 외삽(extrapolation)하여, **PMO benchmark의 23 tasks** 중 12개에서 top-10 AUC를 기록하고 19개 task에서 최고 synthesizability를 달성한 fragment-RAG 방법.

---

## 어떻게 만들었나 (System Architecture)

```
[사전학습된 분자 생성 모델 (LSTM 등)]
              │
              ▼
┌──────────────────────────────────────┐
│ Fragment Vocabulary V                 │ ← ZINC 250K 등에서 추출
│  - hard fragments: 직접 분자에 포함   │
│  - soft fragments: injection module로 │
│    참조해 새 fragment 생성 안내       │
└──────────┬───────────────────────────┘
           │ retrieve top-k fragments
           ▼
┌──────────────────────────────────────┐
│ Hard Fragment Retrieval               │
│   property score 높은 단편 우선       │
│   → 생성 분자에 직접 포함             │
│                                       │
│ Soft Fragment Retrieval               │
│   훈련 가능한 fragment injection mod  │
│   → 신규 fragment 생성 안내           │
└──────────┬───────────────────────────┘
           ▼
[분자 생성 (SMILES) + property prediction]
           │
           ▼
┌──────────────────────────────────────┐
│ Iterative Refinement (closed loop):    │
│   1. property score 계산              │
│   2. 우수 분자에서 새 fragment 추출    │
│   3. V 업데이트 (vocabulary expansion)│
│   4. 다음 라운드 검색에 사용          │
└──────────┬───────────────────────────┘
           ▼
[Post-hoc Genetic Fragment Modification]
   crossover/mutation으로 추가 화학 공간 탐색
```

---

## 원문 직접 인용 (arXiv:2411.12078 §본문)

> **PMO 벤치마크 사용** (§4.1): *"We demonstrate the efficacy of f-RAG on the **23 tasks** from the **PMO benchmark**. Following the standard setting of the benchmark, we set the maximum number of oracle calls to 10,000 and evaluate optimization performance with the area under the curve (AUC) of the average property score versus oracle calls."*

> **결과** (§4.1): *"f-RAG ... achieves the highest **AUC top-10 values in 12 out of 23 tasks**, demonstrating that the proposed combination of hard fragment retrieval, soft fragment retrieval, and genetic fragment modification is highly effective"*

> **Diversity / Synthesizability**: *"f-RAG shows the highest **diversity in 12 out of 23 tasks**, and the highest **synthesizability in 19 out of 23 tasks**"*

> **Docking score 평가 (§4.2)**: *"we use docking score calculated by **QuickVina 2** with five protein targets, **parp1, fa7, 5ht1b, braf, and jak2**, to measure binding affinity. We use quantitative estimates of drug-likeness (**QED**) and **SA** to measure drug-likeness and synthesizability"*

---

## 평가 셋업

### Setup 1 — PMO Benchmark (Gao et al. 2022, NeurIPS)
- **Tasks**: 23 molecular optimization tasks (TDC oracle 기반)
- **Oracle budget**: 10,000 calls 제한
- **Primary metric**: AUC top-10 (average property score 누적 vs oracle calls)
- **Auxiliary metric**: Diversity, Novelty, Synthesizability (SA score)

### Setup 2 — Docking Score Optimization under QED/SA/Novelty constraints (§4.2)
- **Docking program**: QuickVina 2
- **Protein targets**: parp1, fa7, 5ht1b, braf, jak2 (5 종)
- **Constraint**: target property y = c_DS × c_QED × c_SA × c_Novelty (normalized product)
- **Baseline 비교**: Lee et al. (DECOMPDIFF), DST 등 SBDD 방법

---

## 주요 평가 결과 (논문 본문 Table 1)

| 비교 시스템 | Top-7 PMO baselines + 2 SOTA | AUC top-10 합계 |
|---|---|---|
| Graph GA | classical GA fragment crossover | – |
| Mol GA | hyperparameter-tuned Graph GA | (baseline) |
| Genetic GFN | recent SOTA | (baseline) |
| **f-RAG** | hard + soft + genetic | **highest sum across all PMO baselines** |

핵심 성능 numbers (논문 본문):
- AUC top-10 highest in **12/23 tasks**
- Synthesizability highest in **19/23 tasks**
- Diversity highest in **12/23 tasks**

---

## 핵심 기여
1. **Fragment retrieval as RAG for molecules** — 텍스트 RAG 패러다임을 분자 생성으로 확장
2. **Hard + Soft 이중 검색** — 명시적 포함(hard) + injection module(soft) 결합
3. **Iterative refinement로 vocabulary 외삽** — 데이터베이스 밖 fragment 탐색
4. **Post-hoc genetic modification** — crossover/mutation으로 추가 다양성 확보
5. **PMO benchmark에서 SOTA 갱신** — 12/23 task에서 AUC top-10 1위

---

## 한계점
- **Fragment vocabulary 크기 의존성**: 작은 DB → 성능 저하
- **Docking score는 proxy**: 실제 binding affinity의 근사값
- **계산 비용 선형 증가**: refinement 반복 수에 비례
- **5 protein targets만 평가**: 다양한 단백질 가족 일반화 미검증
- **합성 합리성**: SA score는 reaction template 기반 추정으로 실제 합성 실현성과 차이

---

## 관련 정보
- **논문 (arXiv)**: [2411.12078](https://arxiv.org/abs/2411.12078)
- **NeurIPS 2024 OpenReview**: search "Molecule Generation with Fragment Retrieval Augmentation"
- **DBLP**: [conf/nips/LeeKV0RPVN24](https://dblp.org/rec/conf/nips/LeeKV0RPVN24.html)
- **저자 소속**: KAIST, NVIDIA, AstraZeneca
- **사용 벤치마크**: **PMO** (Wenhao Gao et al., NeurIPS 2022, [arXiv:2206.12411](https://arxiv.org/abs/2206.12411))
- **사용 docking tool**: [QuickVina 2](https://qvina.github.io/) (Alhossary et al. 2015, Bioinformatics)
