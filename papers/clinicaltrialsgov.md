---
title: "ClinicalTrials.gov"
bib_key: "clinicaltrialsgov"
year: 2000
domain: medical
type: dataset
venue: U.S. National Library of Medicine
paper_link: https://clinicaltrials.gov
---
# ClinicalTrials.gov

clinicaltrialsgov | 2000 | U.S. National Library of Medicine | dataset | [medical] | [paper](https://clinicaltrials.gov)

**DB**: ClinicalTrials.gov (미국 임상시험 등록 데이터베이스)
**DB size**: 400,000개 이상 등록 임상시험 (2023년 기준); 221개 국가
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ClinicalTrials.gov 웹사이트 / AACT (Aggregate Analysis of ClinicalTrials.gov) / REST API

> U.S. National Library of Medicine | 2000 | dataset | medical
#### 📌 한 줄 요약
미국국립의학도서관(NLM)이 운영하는 세계 최대 임상시험 등록 데이터베이스로, 2000년 출범 이후 221개국 400,000개 이상의 임상시험 정보를 무료로 제공하며 미국 FDA Modernization Act 1997에 의해 설립됐다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 임상시험 결과가 선택적으로 출판되어 부정적 결과가 문헌에서 사라지는 '출판 편향(publication bias)' 문제가 심각했다
- 어떤 임상시험이 진행 중인지 환자·의사·연구자가 접근할 수 있는 단일 저장소가 없었다
- 1997년 FDA Modernization Act가 특정 임상시험의 공개 등록을 처음으로 의무화했다

**이 시스템이 필요한 이유**
- 환자가 자신이 참여 가능한 임상시험을 직접 검색할 수 있는 공공 플랫폼이 필요하다
- 연구자와 제약사가 중복 연구를 피하고 임상 인프라를 효율적으로 활용할 수 있도록 등록 정보가 필요하다
- 2007년 FDA Amendments Act(FDAAA)로 결과 보고 의무화가 강화되면서 결과 데이터도 수집한다

#### 🔨 시스템 구성
ClinicalTrials.gov는 각 임상시험을 NCT 번호(NCT + 8자리)로 식별하며 다음 정보를 구조화하여 보관한다.
- **Protocol 정보**: 연구 제목, 조건/질환, 개입(의약품·시술), 연구 설계, 적격 기준, 1차/2차 평가변수
- **결과 보고**: Phase 2·3 이상 완료 시험의 1차 평가변수 결과 (FDAAA 2007 이후 의무)
- **장소 정보**: 참여 기관·국가, 연락처
- **상태 트래킹**: Recruiting / Active not recruiting / Completed / Terminated 등 상태 코드

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | clinicaltrials.gov — 무료 검색 |
| 공개 API | api.clinicaltrials.gov (v2) — JSON/CSV 반환 |
| AACT DB | aact.ctti-clinicaltrials.org — PostgreSQL 형식 전체 덤프; 연구용 무료 |
| XML 다운로드 | 전체 레코드 XML 또는 JSON 일괄 다운로드 |

#### 📤 제공 데이터 형식
- NCT 레코드 JSON/XML (프로토콜 전체)
- 결과 테이블 (1차·2차 평가변수 결과)
- 이상반응(Adverse Events) 테이블
- MeSH 질환 분류 + 개입(intervention) 표준화 용어

#### 📊 주요 통계 (공식 사이트 기준)
| 항목 | 수치 |
|---|---|
| 등록 임상시험 수 | **400,000개 이상** (2023년 기준) |
| 참여 국가 수 | **221개국** |
| 서비스 개시 | **2000년** |
| 의무화 근거 | FDA Modernization Act 1997 / FDAAA 2007 |
| 운영 기관 | U.S. National Library of Medicine (NLM) |

#### ⚠️ 한계점
- 등록 정보의 완성도 편차: 일부 시험은 1차 평가변수·결과 보고 미완성
- 미국 중심 등록 의무로 비미국 시험의 등록 비율 낮음 (WHO ICTRP 병행 참조 필요)
- 자유 텍스트 필드(적격 기준, 개입 설명)의 비정형성으로 자동 파싱 어려움
- 완료 후 결과 데이터 미제출 시험이 상당수 존재

## 관련 정보
- **공식 사이트**: [ClinicalTrials.gov](https://clinicaltrials.gov)
- **API 문서**: [api.clinicaltrials.gov](https://api.clinicaltrials.gov)
