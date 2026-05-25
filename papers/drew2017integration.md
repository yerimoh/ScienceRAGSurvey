---
title: "Integration of over 9,000 mass spectrometry experiments builds a global map of human protein complexes"
bib_key: "drew2017integration"
year: 2017
domain: bio
type: dataset
venue: Molecular Systems Biology
paper_link: https://doi.org/10.15252/msb.20167490
---
# Integration of over 9,000 mass spectrometry experiments builds a global map of human protein complexes

drew2017integration | 2017 | Molecular Systems Biology | dataset | [bio] | [paper](https://doi.org/10.15252/msb.20167490)

**DB**: hu.MAP (Human Protein Complex Map)
**DB size**: 4,600개 이상의 복합체, 7,700개 이상의 단백질, 56,000개 이상의 고유 상호작용 (9,000개 이상의 질량분석 실험 통합)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: hu.MAP 웹 인터페이스 (http://proteincomplexes.org)

> Molecular Systems Biology | 2017 | dataset | bio
#### 📌 한 줄 요약
9,000개 이상의 발표된 질량분석 실험을 통합하여 4,600개 이상의 복합체, 7,700개 이상의 단백질, 56,000개 이상의 고유 상호작용을 포함하는 인간 단백질 복합체 지도(hu.MAP)를 구축했다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 기존에 발표된 인간 단백질 복합체 지도들은 포괄적인 커버리지가 부족했다
- 수천 개의 대규모 질량분석 실험 데이터가 분산되어 있어 통합 분석이 어려웠다
- 단백질 복합체 비교를 위한 정량적 평가 지표(k-cliques)가 없었다

**이 시스템이 필요한 이유**
- 인간 단백질 복합체의 완전한 집합을 정의하기 위해 기존 발표 데이터를 종합
- 많은 유전 질환이 단백질 복합체 기능 장애로 발생하여 복합체 지도의 임상적 중요성이 높음
- 신뢰도 높은 단백질 상호작용 예측 및 실험적 검증을 통한 새로운 질환 유전자 발견

#### 🔨 시스템 구성
9,000개 이상의 공개 질량분석 실험을 기계 학습 프레임워크로 통합하여 단백질 복합체를 예측했다. k-cliques라는 새로운 정량적 지표를 개발하여 복합체 집합 비교를 최적화했다. hu.MAP은 문헌 주석이 풍부하게 부여된 복합체들을 포함하며, 섬모병증(ciliopathy) 등 질환 관련 단백질의 커버리지가 향상되었다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | http://proteincomplexes.org — 복합체 검색 및 시각화 |
| 파일 다운로드 | 복합체 목록 및 단백질 상호작용 데이터 |

#### 📤 제공 데이터 형식
- 단백질 복합체 목록 (멤버 단백질, 신뢰 점수)
- 단백질-단백질 상호작용 네트워크
- 질환 관련 단백질 주석

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 통합 질량분석 실험 수 | **9,000개 이상** |
| 총 복합체 수 | **4,600개 이상** |
| 단백질 수 | **7,700개 이상** |
| 고유 상호작용 수 | **56,000개 이상** |

#### ⚠️ 한계점
- 질량분석 실험에서 검출되지 않는 복합체는 포함되지 않는다
- 기계 학습 기반 예측으로 일부 복합체는 실험적 검증이 필요하다
- 세포 유형, 조직, 조건에 따른 복합체 조성 변화를 포착하지 못한다

## 관련 정보
- **논문**: [Integration of over 9,000 mass spectrometry experiments builds a global map of human protein complexes](https://doi.org/10.15252/msb.20167490)
