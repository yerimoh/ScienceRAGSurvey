---
title: "Molecule Generation with Fragment Retrieval Augmentation"
bib_key: "DBLP:conf/nips/LeeKV0RPVN24"
year: 2024
domain: chem
type: Method
venue: NeurIPS 2024
paper_link: https://arxiv.org/abs/2411.12078
---
# Molecule Generation with Fragment Retrieval Augmentation

DBLP:conf/nips/LeeKV0RPVN24 | 2024 | NeurIPS 2024 | Method | [chem] | [paper](https://arxiv.org/abs/2411.12078)

**Retriever**: Fragment-based retrieval (hard/soft fragment vocabulary)
**Eval Task**: PMO benchmark (23 molecular optimization tasks), docking score optimization under QED/SA/novelty constraints
**Eval Metric**: AUC top-10 (property scores), diversity, novelty, synthesizability (SA score)
**Method Name**: f-RAG (Fragment Retrieval-Augmented Generation)
**Modality**: Molecular structures (SMILES/fragments)

> NeurIPS 2024 | 2024 | Method | chem
#### 📌 한 줄 요약
사전 학습된 분자 생성 모델에 단편(fragment) 검색 증강을 결합하여 PMO 벤치마크 23개 분자 최적화 태스크에서 탐색-활용 균형을 개선하고, 반복 정제(iterative refinement) 및 유전자 단편 변형(genetic fragment modification)으로 기존 단편 데이터베이스를 넘어선 신규 분자를 생성하는 프레임워크이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 기존 단편 기반 분자 생성 방법은 데이터베이스에 존재하는 단편만 재조합·소폭 변형하는 데 그쳐 탐색 범위가 제한됨
- 생성된 분자의 다양성(diversity), 신규성(novelty), 합성 가능성(synthesizability) 간의 균형 달성이 어려움

**이 시스템이 필요한 이유**
- 신약 발견에서 특정 생화학적 특성(합성 가능성, 비독성, 용해도, 결합 친화도)을 갖는 분자를 광범위한 화학 공간에서 발굴할 필요
- 기존 단편 이상으로 외삽(extrapolation)하는 생성 능력 필요

#### 🔨 시스템 구성
f-RAG는 사전 학습된 분자 생성 모델을 기반으로 두 가지 단편 유형을 검색한다: (1) **hard fragments**: 새로운 분자에 명시적으로 포함될 빌딩 블록, (2) **soft fragments**: 훈련 가능한 fragment injection module을 통해 새 단편 생성을 안내하는 참조 단편. 반복 정제 과정에서 생성된 단편으로 fragment vocabulary를 업데이트하고, post-hoc 유전자 단편 변형(genetic fragment modification)으로 추가 탐색을 강화한다. Therapeutics Data Commons (TDC) 라이브러리를 사용해 다양성을 계산하며, Tanimoto 유사도 기반 신규성과 SA 점수 기반 합성 가능성을 측정한다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 평가 벤치마크 | PMO benchmark, 23 tasks |
| 최대 oracle calls | 10,000 |
| 성능 지표 | AUC top-10 (avg property score vs. oracle calls) |
| 비교 기준선 | Graph GA, Mol GA, REINVENT, GP BO, STONED 등 9개 |
| 주요 결과 | f-RAG, PMO 벤치마크에서 AUC top-10 합계 기준 이전 방법 능가 |

#### ⚠️ 한계점
- Fragment vocabulary 크기에 의존적이며, 데이터베이스가 작을 경우 성능 저하 가능
- Docking score 최적화 시 실제 DFT/분자역학 검증 없이 프록시 점수에 의존
- 계산 비용이 반복 정제 단계 수에 따라 선형적으로 증가

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2411.12078](https://arxiv.org/abs/2411.12078)
- **NeurIPS 2024**: Advances in Neural Information Processing Systems 38
