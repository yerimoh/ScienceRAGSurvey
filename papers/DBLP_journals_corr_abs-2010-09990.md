---
title: "The Open Catalyst 2020 (OC20) Dataset and Community Challenges"
bib_key: "DBLP:journals/corr/abs-2010-09990"
year: 2020
domain: material
type: dataset
venue: ACS Catalysis (arXiv preprint 2020; published 2021)
paper_link: https://arxiv.org/abs/2010.09990
---
# The Open Catalyst 2020 (OC20) Dataset and Community Challenges

DBLP:journals/corr/abs-2010-09990 | 2020 | ACS Catalysis | dataset | [material] | [paper](https://arxiv.org/abs/2010.09990)

**DB**: Open Catalyst 2020 (OC20)
**DB size**: 1,281,040 DFT relaxations (~264,890,000 single point evaluations, 논문 기준)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: IS2RE (초기 → 이완 에너지), S2EF (구조 → 에너지·힘), IS2RS (초기 → 이완 구조)
**Eval Metric**: MAE, EwT (Energy within Threshold), Force MAE
**Method Name**: OC20 Dataset, Open Catalyst Project (opencatalystproject.org)

> ACS Catalysis | 2020/2021 | dataset | material
#### 📌 한 줄 요약
Facebook AI Research(현 Meta)와 Carnegie Mellon University가 공개한 태양연료·장기에너지저장·재생비료 합성 등에 쓰이는 촉매 발견을 위한 128만 건의 DFT 이완 계산 데이터셋으로, 머신러닝 잠재력 함수 개발을 위한 커뮤니티 벤치마크를 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 전산 촉매 분야에서 ML 모델 훈련에 필요한 데이터셋 규모가 관련 분야보다 현저히 작음
- 태양 연료, 재생 암모니아 합성, 장기 에너지 저장용 촉매 발견을 가속화할 체계적 데이터 필요
- 표면 조성·흡착 분자 다양성 모두를 커버하는 범용 ML 모델 개발을 위한 대규모 벤치마크 부재

**이 시스템이 필요한 이유**
- 질소·탄소·산소 화학계에서의 광범위한 재료 표면과 흡착 분자를 체계적으로 포함
- 훈련/검증/테스트 분할 사전 정의로 재현 가능한 ML 모델 개발 기반 마련
- 공개 리더보드를 통한 커뮤니티 기여 촉진

#### 🔨 시스템 구성
DFT 기반 구조 이완(VASP, RPBE 범함수) 계산으로 촉매 표면의 흡착 에너지 및 원자 힘을 생성한다. 다양한 bulk 재료, 표면 밀러 지수, 흡착 분자(N, C, O 화학계)를 체계적으로 결합하여 광범위한 화학 공간을 커버한다. GNN 기반 베이스라인(CGCNN, SchNet, DimeNet++)과 함께 제공된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 공식 웹사이트 | opencatalystproject.org — 데이터 다운로드 |
| GitHub | github.com/Open-Catalyst-Project/ocp — 코드 및 베이스라인 |
| 리더보드 | 공개 벤치마크 리더보드 |

#### 📤 제공 데이터 형식
- DFT 이완 궤적 (초기~최종 구조, 각 단계 에너지·힘)
- 흡착 에너지 (eV)
- 원자 힘 (eV/Å)
- 표면 슬랩 구조 (ASE Atoms 형식)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 DFT 이완 계산 | **1,281,040** |
| 단일점 에너지 계산 | **~264,890,000** |
| 화학계 | 질소(N), 탄소(C), 산소(O) 화학 |
| 중심 태스크 | 3개 (IS2RE, S2EF, IS2RS) |
| 베이스라인 GNN | CGCNN, SchNet, DimeNet++ |

#### ⚠️ 한계점
- 질소·탄소·산소 화학계로 범위 한정 (산화물 촉매는 OC22에서 확장)
- RPBE 범함수 사용으로 실험값과 체계적 오차 존재
- 용매·전해질 효과 미포함 (기상 흡착 조건만 고려)
- ML 모델 크기에 대한 상한이 확인되지 않아 더 큰 모델이 더 좋은 성능 달성 가능성

## 관련 정보
- **논문**: [The Open Catalyst 2020 (OC20) Dataset (arXiv:2010.09990)](https://arxiv.org/abs/2010.09990)
- **출판 버전**: [ACS Catalysis, 2021, DOI:10.1021/acscatal.0c04525](https://doi.org/10.1021/acscatal.0c04525)
