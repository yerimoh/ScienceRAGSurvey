---
title: "The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts"
bib_key: "DBLP:journals/corr/abs-2206-08917"
year: 2022
domain: material
type: dataset
venue: Journal of Chemical Theory and Computation (arXiv preprint 2022)
paper_link: https://arxiv.org/abs/2206.08917
---
# The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts

DBLP:journals/corr/abs-2206-08917 | 2022 | Journal of Chemical Theory and Computation | dataset | [material] | [paper](https://arxiv.org/abs/2206.08917)

**DB**: Open Catalyst 2022 (OC22)
**DB size**: 62,331 DFT relaxations (~9,854,504 single point calculations, 논문 기준)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: Total energy prediction (S2EF-Total), IS2RE-Total
**Eval Metric**: Energy MAE, Force MAE
**Method Name**: OC22 Dataset, Open Catalyst Project (opencatalystproject.org)

> Journal of Chemical Theory and Computation | 2022 | dataset | material
#### 📌 한 줄 요약
OC20에서 다루지 못한 산화물 전기촉매(OER 촉매) 재료를 위한 62,331건의 DFT 이완 데이터셋으로, 흡착 에너지를 넘어 일반화된 총 에너지 예측 태스크를 정의하고 OC20과의 결합 훈련으로 성능 향상을 입증한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- OC20은 질소·탄소·산소 화학계 위주로, 산화물 전기촉매 재료 학습 데이터 부족
- 산소 발생 반응(OER) 촉매는 재생에너지 저장·전환에 핵심이나 ML 훈련 데이터 미비
- 장거리 정전기 및 자기 상호작용이 중요한 산화물에 대한 별도 벤치마크 필요

**이 시스템이 필요한 이유**
- 산화물 재료의 다양한 표면 커버리지, 흡착 분자 조합을 체계적으로 포함
- 흡착 에너지 너머의 일반화된 총 에너지 예측 태스크로 ML 모델 적용 범위 확장
- OC20과의 결합 훈련(joint training)으로 두 데이터셋 모두에서 성능 향상 가능성 입증

#### 🔨 시스템 구성
VASP 기반 DFT 계산(RPBE 범함수)으로 산화물 슬랩 구조의 구조 이완을 수행한다. 다양한 산화물 재료, 표면 커버리지, 흡착 분자를 포함하며, 일반화된 총 에너지 태스크(S2EF-Total, IS2RE-Total)를 통해 흡착 에너지만이 아닌 시스템 전체 에너지 예측에 초점을 맞춘다. GemNet-OC 등 GNN 베이스라인과 함께 제공된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 공식 웹사이트 | opencatalystproject.org — 데이터 다운로드 |
| GitHub | github.com/Open-Catalyst-Project/ocp — 코드 및 베이스라인 |
| 리더보드 | 총 에너지 태스크 공개 벤치마크 |

#### 📤 제공 데이터 형식
- DFT 이완 궤적 (초기~최종 구조, 각 단계 에너지·힘)
- 총 에너지 (eV)
- 원자 힘 (eV/Å)
- 산화물 슬랩 구조 (ASE Atoms 형식)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 DFT 이완 계산 | **62,331** |
| 단일점 에너지 계산 | **~9,854,504** |
| 에너지 예측 개선 (결합 훈련, OC20) | **~19%** (총 에너지 기준) |
| 힘 예측 개선 (결합 훈련, OC22) | **~9%** |
| 최고 모델 성능 (에너지 예측, OC20+OC22) | GemNet-OC ~36% 향상 |

#### ⚠️ 한계점
- OC20 대비 데이터 규모 소규모 (6만 건 vs 128만 건)
- 산화물 특성상 장거리 정전기·자기 상호작용이 중요하나 현재 GNN은 이를 완전히 포착하지 못함
- 용매·전해질 효과 미포함
- RPBE 범함수 사용으로 실험값과 체계적 오차 존재

## 관련 정보
- **논문**: [The Open Catalyst 2022 (OC22) Dataset (arXiv:2206.08917)](https://arxiv.org/abs/2206.08917)
