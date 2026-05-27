---
title: "TDC: Therapeutics Data Commons — Machine Learning Datasets and Tasks for Drug Discovery and Development"
bib_key: "DBLP:conf/nips/HuangFG0RLCXSZ21"
year: 2021
domain: medical, bio, chem
type: benchmark
venue: NeurIPS Datasets and Benchmarks 2021
paper_link: https://arxiv.org/abs/2102.09548
---
# TDC (Therapeutics Data Commons): 66 AI-ready Datasets × 22 Learning Tasks Umbrella Benchmark

> NeurIPS 2021 Datasets and Benchmarks Track | Benchmark Suite | medical · bio · chem
> Kexin Huang, Tianfan Fu, Wenhao Gao, Yue Zhao, Yusuf H. Roohani, Jure Leskovec, Connor W. Coley, Cao Xiao, Jimeng Sun, Marinka Zitnik — Harvard / Stanford / MIT / Georgia Tech / IBM / UIUC
> DBLP: `conf/nips/HuangFG0RLCXSZ21` · arXiv: [2102.09548](https://arxiv.org/abs/2102.09548) · Web: [tdcommons.ai](https://tdcommons.ai)

## 한 줄 요약
약물 발견·개발 전 범위(small molecule → biologics → clinical trial)에 걸친 **66개 AI-ready 데이터셋 × 22개 learning task** 통합 평가 플랫폼. **29 public leaderboards**, **17 molecule generation oracles**, **23 evaluation 전략**, **33 data 분할/함수**, 오픈 Python 라이브러리 제공. Database-verified Prediction 시스템 (CLADD 등)의 사실상 표준 평가 hub.

---

## 어떻게 만들었나 (Construction Methodology)

```
3개 학습 패러다임 × 22 tasks × 66 datasets 구조

┌──────────────────────────────────────────────────────────────┐
│ 1. single_pred (단일 인스턴스 예측) — 9 tasks                │
│    └─ ADME (흡수·분포·대사·배설) Property Prediction         │
│    └─ Tox (독성) Prediction                                  │
│    └─ HTS (high-throughput screening) Prediction             │
│    └─ QM (양자역학 properties)                               │
│    └─ Yields (반응 수율) Prediction                          │
│    └─ Paratope / Epitope Prediction (항체 결합 부위)         │
│    └─ Antibody Developability Prediction                     │
│    └─ CRISPR Repair Outcome Prediction                       │
│                                                               │
│ 2. multi_pred (다중 인스턴스 예측) — 7 tasks                 │
│    └─ DTI (Drug-Target Interaction)                          │
│    └─ DDI (Drug-Drug Interaction)                            │
│    └─ PPI (Protein-Protein Interaction)                      │
│    └─ GDA (Gene-Disease Association)                         │
│    └─ DrugRes (Drug Response on cell lines, GDSC)            │
│    └─ DrugSyn (Drug Synergy)                                 │
│    └─ Peptide MHC binding / TCR-Epitope                      │
│                                                               │
│ 3. generation — 6 tasks                                       │
│    └─ Molecule Generation (de novo design)                   │
│    └─ Reaction / Retrosynthesis Prediction                   │
│    └─ Forward Synthesis Prediction                           │
│    └─ Paratope Antibody Sequence Generation                  │
│    └─ MolOpt (Molecule Optimization with 17 oracles)         │
└──────────────────────────────────────────────────────────────┘

Step 1 — 데이터셋 수집 + 정제
  공개 임상/생화학 DB 66종에서 raw data 다운로드
  → 통합 schema로 정규화 (SMILES, sequence, label 형식 표준화)
  → 결측치/중복 제거, train/val/test split 표준화

Step 2 — 평가 프로토콜 표준화
  · 33 data functions/splits: random/scaffold/cold-start/temporal/등
  · 23 evaluation strategies: AUROC/AUPRC/RMSE/MAE/Top-K/등
  · 17 molecule generation oracles: QED/SA/LogP/JNK3/GSK3β/DRD2/등
                                    (PMO benchmark 의 oracle 모음)

Step 3 — 29 Public Leaderboards
  · ADMET Group Leaderboard
  · Docking Group Leaderboard
  · 시간 추적 가능한 공개 비교 (reproducibility 보장)

Step 4 — Python Library + Documentation
  └─ pip install PyTDC
  └─ 통일된 `from tdc.single_pred import ADME` 식 API
  └─ tdcommons.ai 공식 문서 + Tutorial
```

---

## 원문 직접 인용 (arXiv:2102.09548 §Abstract 본문)

> *"Therapeutics machine learning is an emerging field with incredible opportunities for innovation and impact ... we introduce **Therapeutics Data Commons (TDC), the first unifying platform** to systematically access and evaluate machine learning across the entire range of therapeutics. To date, TDC includes **66 AI-ready datasets spread across 22 learning tasks** and spanning the discovery and development of safe and effective medicines."*

> *"TDC also provides an ecosystem of tools and community resources, including **33 data functions and types of meaningful data splits**, **23 strategies for systematic model evaluation**, **17 molecule generation oracles**, and **29 public leaderboards**. All resources are integrated and accessible via an open Python library."*

> *"We carry out extensive experiments on selected datasets, demonstrating that even the strongest algorithms **fall short of solving key therapeutics challenges**, including real dataset distributional shifts, multi-scale modeling of heterogeneous data, and robust generalization to novel data points."*

---

## Input / Output (학습 패러다임별)

| 패러다임 | Input | Output | 대표 task |
|---|---|---|---|
| **single_pred** | 단일 분자/단백질 (SMILES, sequence) | scalar/class label | ADMET, Toxicity (Tox21, SIDER, ClinTox 등 포함) |
| **multi_pred** | (drug, target) 또는 (drug, drug) pair | interaction score / class | DTI (BindingDB, DAVIS, KIBA 포함), DDI |
| **generation** | constraint / oracle 점수 | 신규 분자 SMILES | MolOpt, retrosynthesis |

**오라클 사용 시 예시**:
- QED / SA → 분자 약물성
- DRD2 / JNK3 / GSK3β → bioactivity prediction
- Docking 모듈 → Vina score (PMO subset)

---

## 주요 평가 결과 (논문 §본문 + Table)

### 평가 환경
- **29 public leaderboards** 운영 (ADMET Group, Docking Group 등)
- **23 evaluation strategies** (AUROC, AUPRC, RMSE, MAE, Top-K Recall, Spearman 등)
- **33 data splits** (random, scaffold, cold-start, temporal, lo-shot 등)

### 핵심 발견 (논문 §본문 인용)
- "even the **strongest algorithms fall short** of solving key therapeutics challenges"
- **Distribution shift** (시계열·실험실 간) 강건성 부족
- **Multi-scale modeling** (small molecule ↔ protein ↔ disease) 통합 미숙
- **Novel data points** 일반화 한계

---

## 데이터셋 통계 (대표 subset)

| Category | 대표 datasets |
|---|---|
| ADMET | Caco2, HIA, Pgp, Bioavailability, Lipophilicity, Solubility, BBBP, PAMPA, Half-Life, Clearance, hERG, AMES, DILI |
| Toxicity | ClinTox, Tox21, ToxCast, LD50 |
| HTS | SARS-CoV-2 in vitro, HIV |
| DTI | BindingDB (Kd/Ki/IC50/EC50), DAVIS, KIBA |
| DDI | DrugBank DDI, TWOSIDES |
| GDA | DisGeNET |
| DrugRes | GDSC cell-line response |
| Generation | MOSES, ZINC 250K, ChEMBL, USPTO retrosynthesis |

→ Database-verified Prediction RAG 시스템 (CLADD 등) 평가 시 자주 활용.

---

## 한계점 (논문 §Limitations + 후속 연구 지적)
- **데이터셋 품질 편차**: 일부 small-scale dataset은 충분한 변동 통계 부족
- **Distribution shift** 평가가 부족 (시간/실험실/도메인 간 동일성 가정)
- **시간 의존성 데이터**: 새로 발견된 drug-target은 leaderboard에 천천히 반영
- **Benchmark gaming**: leaderboard 최적화가 실제 의학적 가치와 분리 가능
- **타입별 dataset 균형**: small molecule 위주, biologics/macromolecule 비율 낮음
- **Closed-set evaluation**: 미발견 분자/단백질에 대한 generalization 측정 불가

---

## 관련 정보
- **논문 (arXiv)**: [2102.09548](https://arxiv.org/abs/2102.09548)
- **NeurIPS 2021 Datasets and Benchmarks Track**: [Round 1 paper](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/4c7a167bb329bd92580a99ce422d6fa6-Abstract-round1.html)
- **DBLP**: [conf/nips/HuangFG0RLCXSZ21](https://dblp.org/rec/conf/nips/HuangFG0RLCXSZ21.html)
- **공식 홈페이지**: [tdcommons.ai](https://tdcommons.ai)
- **PyPI**: `pip install PyTDC`
- **이 benchmark를 사용한 후속 RAG 작업**: CLADD (Database-verified Prediction), PMO (MolOpt subset reuse), Patho-AgenticRAG (Pathology subset), 등 의약 RAG 표준 평가 hub
