---
title: "hu.MAP 2.0: integration of over 15,000 proteomic experiments builds a global compendium of human multiprotein assemblies"
bib_key: "drew2021hu"
year: 2021
domain: bio
type: dataset
venue: Molecular Systems Biology
paper_link: https://doi.org/10.15252/msb.202010016
---
# hu.MAP 2.0: integration of over 15,000 proteomic experiments builds a global compendium of human multiprotein assemblies

drew2021hu | 2021 | Molecular Systems Biology | dataset | [bio] | [paper](https://doi.org/10.15252/msb.202010016)

**DB**: hu.MAP 2.0 (Human Protein Complex Map 2.0)
**DB size**: 7,000개 가까운 물리적 어셈블리 (15,000개 이상의 프로테오믹스 실험 통합)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: hu.MAP 2.0 웹 인터페이스 (http://humap2.proteincomplexes.org/)

> Molecular Systems Biology | 2021 | dataset | bio
#### 📌 한 줄 요약
15,000개 이상의 프로테오믹스 실험을 통합하여 7,000개 가까운 인간 단백질 어셈블리를 식별하고, 274개의 전혀 특성화되지 않은 단백질과 253개의 다중 복합체 참여 단백질(moonlighting)을 발굴한 hu.MAP 초판의 후속 자원이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- hu.MAP 1.0(2017)은 9,000개 질량분석 실험 기반이었으나, 인간 세포 내 단백질 복합체의 포괄적 집합에 대한 지식이 여전히 불완전했다
- 전혀 특성화되지 않은 단백질들의 복합체 참여 여부 예측이 어려웠다

**이 시스템이 필요한 이유**
- 실험 데이터 추가로 보다 정확하고 포괄적인 인간 단백질 복합체 지도 구축
- 274개의 완전 비특성화 단백질에 대한 새로운 가설 제공
- 복수 복합체에 참여하는 promiscuous 단백질(달빛 활동 가능성) 식별

#### 🔨 시스템 구성
기계 학습 프레임워크를 사용하여 15,000개 이상의 질량분석 실험에서 단백질 복합체를 식별했다. hu.MAP 2.0은 기존 최신 고처리량 단백질 복합체 자원보다 더 정확하고 포괄적이다. 사용자 친화적인 웹 인터페이스(http://humap2.proteincomplexes.org/)를 통해 검색 가능하다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | http://humap2.proteincomplexes.org/ — 복합체 검색 및 시각화 |
| 파일 다운로드 | 복합체 목록 및 단백질 상호작용 데이터 |

#### 📤 제공 데이터 형식
- 단백질 복합체 목록 (멤버 단백질, 신뢰 점수)
- 단백질-단백질 상호작용 데이터
- 비특성화 단백질 가설 목록

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 통합 프로테오믹스 실험 수 | **15,000개 이상** |
| 식별된 물리적 어셈블리 수 | **약 7,000개** |
| 완전 비특성화 단백질 | **274개** (새 가설 제공) |
| 다중 복합체 참여 단백질 | **253개** (promiscuous) |

#### ⚠️ 한계점
- 질량분석 기반으로 검출 편향이 있어 특정 단백질 복합체가 누락될 수 있다
- 기계 학습 예측의 신뢰도가 복합체마다 다르며 추가 실험 검증이 필요하다
- 세포 유형·조직·환경 조건에 따른 복합체 동적 변화를 포착하지 못한다

## 관련 정보
- **논문**: [hu.MAP 2.0: integration of over 15,000 proteomic experiments builds a global compendium of human multiprotein assemblies](https://doi.org/10.15252/msb.202010016)
