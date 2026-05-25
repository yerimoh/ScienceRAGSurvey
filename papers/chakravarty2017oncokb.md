---
title: "OncoKB: a precision oncology knowledge base"
bib_key: "chakravarty2017oncokb"
year: 2017
domain: medical
type: dataset
venue: JCO Precision Oncology
paper_link: https://doi.org/10.1200/PO.17.00011
---
# OncoKB: a precision oncology knowledge base

chakravarty2017oncokb | 2017 | JCO Precision Oncology | dataset | [medical] | [paper](https://doi.org/10.1200/PO.17.00011)

**DB**: OncoKB (Memorial Sloan Kettering Cancer Center 정밀 종양학 지식 베이스)
**DB size**: 출판 시점 수백 개 유전자·변이; 지속 업데이트
**DB Open/Private**: Open (학술 무료) / 상업적 사용 라이선스
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OncoKB REST API / oncokb.org 웹 인터페이스

> JCO Precision Oncology | 2017 | dataset | medical
#### 📌 한 줄 요약
Memorial Sloan Kettering Cancer Center가 구축한 암 정밀 의학 지식 베이스로, FDA 승인 및 임상시험 단계 치료제와의 연관성을 기반으로 체세포 변이의 임상적 실행 가능성(actionability)을 4단계 증거 수준으로 체계화한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 임상 종양 유전체 데이터(MSK-IMPACT 패널 등)에서 수천 개의 변이가 보고되지만 임상적 의미를 즉각 해석할 단일 참조 자원이 없었다
- 기존 암 변이 DB(COSMIC, ClinVar)는 임상 실행 가능성 정보가 부족했다
- FDA 승인 바이오마커와 임상시험 근거를 계층화된 수준으로 정리한 큐레이션 DB가 필요했다

**이 시스템이 필요한 이유**
- 종양내과 의사가 진료 현장에서 환자의 변이 프로파일을 즉시 해석하고 치료 선택에 활용할 수 있는 컴퓨터 보조 도구가 필요하다
- MSK-IMPACT 등 대규모 종양 시퀀싱 프로그램에서 생성되는 수만 건의 변이 보고서 자동화 주석을 지원해야 한다

#### 🔨 시스템 구성
OncoKB는 변이의 임상적 실행 가능성을 4단계 증거 수준으로 분류한다.
- **Level 1**: FDA 승인 치료제의 바이오마커 (해당 암종 내)
- **Level 2**: 표준 치료 가이드라인 권고 바이오마커 (NCCN 등)
- **Level 3**: 임상시험 증거 있는 바이오마커 (3A: 동일 암종, 3B: 다른 암종)
- **Level 4**: 생물학적 증거 기반 추론
- **Resistance**: 치료 내성 관련 변이

유전자·변이·암종의 3차원 구조로 정보 조직화; 전문 큐레이터 팀이 MSK 임상 경험과 문헌을 기반으로 수동 큐레이션.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| OncoKB REST API | api.oncokb.org — 변이 주석, 유전자 정보, 치료 연관 쿼리 |
| 웹 인터페이스 | oncokb.org — 변이 검색, 유전자 요약, 치료 가이드 |
| 학술 라이선스 | 비영리 학술 기관 무료 등록; 상업 사용 별도 계약 |

#### 📤 제공 데이터 형식
- 변이별 임상 실행 가능성 레이블 (Level 1~4, Resistance)
- 연관 FDA 승인 치료제 목록
- 임상시험 참조 정보
- 유전자-암종 요약 텍스트

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 임상 실행 가능성 레벨 | **4단계** (Level 1, 2, 3A/3B, 4) + Resistance |
| 운영 기관 | Memorial Sloan Kettering Cancer Center (MSK) |
| 초기 데이터 기반 | MSK-IMPACT 패널 (468개 유전자) |
| 참고 표준 | FDA 승인 바이오마커, NCCN 가이드라인, 주요 임상시험 |

#### ⚠️ 한계점
- 상업적 사용 시 라이선스 비용 — 제약사·바이오텍 RAG 시스템 적용 제약
- MSK 임상 경험 중심 큐레이션으로 특정 암종(유방, 폐, 대장) 편향 가능성
- Level 3·4 변이는 증거 강도가 낮아 임상 적용 시 주의 필요
- 희귀 변이·희귀 암종은 커버리지 제한

## 관련 정보
- **논문**: [Chakravarty et al., JCO Precision Oncology 2017](https://doi.org/10.1200/PO.17.00011)
