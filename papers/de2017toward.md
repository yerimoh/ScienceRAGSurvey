---
title: "Toward a new data standard for combined marine biological and environmental datasets—expanding OBIS beyond species occurrences"
bib_key: "de2017toward"
year: 2017
domain: bio
type: dataset
venue: Biodiversity Data Journal
paper_link: https://doi.org/10.3897/BDJ.5.e10989
---
# Toward a new data standard for combined marine biological and environmental datasets—expanding OBIS beyond species occurrences

de2017toward | 2017 | Biodiversity Data Journal | dataset | [bio] | [paper](https://doi.org/10.3897/BDJ.5.e10989)

**DB**: OBIS (Ocean Biodiversity Information System)
**DB size**: 전 세계 해양 생물다양성 출현 기록의 통합 저장소 (논문은 새로운 데이터 표준 확장을 논의하며 구체적 수치는 제공하지 않음)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OBIS API / OBIS-ENV-DATA 표준 (UNESCO-IOC)

> Biodiversity Data Journal | 2017 | dataset | bio
#### 📌 한 줄 요약
해양 생물다양성 정보 시스템(OBIS)을 종 출현 기록 중심에서 생물·환경 결합 데이터셋으로 확장하는 새로운 데이터 표준(OBIS-ENV-DATA)을 제안하여 해양 생물 및 환경 데이터를 통합 표현하는 방안을 논의한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 기존 OBIS는 Darwin Core 기반 종 출현 기록에 특화되어 있어 환경 측정 데이터(온도, 염도, 영양염 등)와 생물 샘플 데이터를 통합하는 데 한계가 있었다
- 해양 생물학과 환경 데이터를 연결하는 공통 데이터 표준이 없어 연구자들이 별도 분석 시스템을 구축해야 했다

**이 시스템이 필요한 이유**
- 해양 생태계 연구에서 종 출현과 환경 조건을 함께 분석하기 위한 통합 데이터 표준 필요
- UNESCO-IOC OBIS 사무국과 국제 OBIS 노드들(EurOBIS, OBIS-USA, MedOBIS, 남극 OBIS 등)의 협력으로 글로벌 표준 개발
- 생물다양성 데이터와 환경 데이터의 연계를 통한 기후변화 영향 연구 지원

#### 🔨 시스템 구성
OBIS-ENV-DATA는 Darwin Core Event core와 Occurrence 및 Extended Measurement or Fact (EMoF) 확장을 결합하여 생물 샘플 계층 구조, 종 출현, 관련 환경 측정값을 통합 표현한다. UNESCO-IOC OBIS 사무국이 조정하며 전 세계 수십 개의 지역 OBIS 노드가 데이터를 제공한다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 포털 | https://obis.org — 해양 생물다양성 데이터 검색 |
| OBIS API | 프로그래밍 방식 데이터 접근 |
| 파일 다운로드 | Darwin Core Archive 형식 |

#### 📤 제공 데이터 형식
- 종 출현 기록 (Darwin Core 형식)
- 환경 측정 데이터 (Extended Measurement or Fact)
- 생물 샘플 계층 구조 (이벤트 기반)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 제안 표준 | OBIS-ENV-DATA (Darwin Core Event core + Occurrence + EMoF) |
| 운영 기관 | UNESCO-IOC OBIS 사무국 |
| 참여 국제 노드 | 전 세계 수십 개 (EurOBIS, OBIS-USA, MedOBIS, 남극 OBIS 등) |

#### ⚠️ 한계점
- 2017년 논문은 새로운 데이터 표준 제안에 초점을 맞추어 당시 데이터 규모에 대한 정량적 수치를 제공하지 않는다
- 데이터 품질과 지리적 커버리지가 OBIS 노드마다 불균등하다
- 환경 측정 데이터 통합은 표준화 수준이 낮아 데이터 비교 가능성에 제한이 있다

## 관련 정보
- **논문**: [Toward a new data standard for combined marine biological and environmental datasets](https://doi.org/10.3897/BDJ.5.e10989)
