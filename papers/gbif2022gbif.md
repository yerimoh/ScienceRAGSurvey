---
title: "GBIF: the global biodiversity information facility"
bib_key: "gbif2022gbif"
year: 2022
domain: bio
type: dataset
venue: GBIF Secretariat
paper_link: https://www.gbif.org/
---
# GBIF: the global biodiversity information facility

gbif2022gbif | 2022 | GBIF Secretariat | dataset | [bio] | [paper](https://www.gbif.org/)

**DB**: GBIF (Global Biodiversity Information Facility)
**DB size**: 전 세계 생물다양성 출현 기록 집계 (논문/데이터 인용 기준 수치 제공 없음 — GBIF Secretariat 2022 데이터 인용)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: GBIF API / GBIF.org 웹 포털

> GBIF Secretariat | 2022 | dataset | bio
#### 📌 한 줄 요약
국제 협력으로 운영되는 전 세계 생물다양성 정보 시설(GBIF)로, 전 세계 다양한 기관에서 수집된 생물 출현 기록(species occurrence records)을 통합하여 공개 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 전 세계 생물다양성 데이터가 수많은 기관(자연사 박물관, 대학, 정부 기관)에 분산되어 있어 글로벌 규모의 연구가 어려웠다
- 생물다양성 보전, 기후변화 대응, 생태학 연구를 위한 글로벌 데이터 접근 인프라가 필요했다

**이 시스템이 필요한 이유**
- 생물다양성 연구, 보전, 지속가능한 개발 목표(SDGs) 지원을 위한 공개 인프라
- 전 세계 연구자, 정책 입안자, 일반 대중이 생물다양성 데이터에 자유롭게 접근할 수 있도록 지원
- 다양한 데이터 제공자(자연사 박물관, 시민과학, 원격탐사 등)의 데이터를 표준화하여 통합

#### 🔨 시스템 구성
GBIF는 국제 협력 기반의 개방형 데이터 인프라로, 전 세계 수천 개 기관에서 제출한 생물 출현 기록을 Darwin Core 표준으로 통합한다. GBIF.org 포털과 REST API를 통해 데이터 접근을 제공한다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 포털 | https://www.gbif.org — 생물다양성 데이터 검색 및 탐색 |
| REST API | GBIF API — 프로그래밍 방식 데이터 접근 |
| 데이터 다운로드 | Darwin Core Archive 형식 bulk 다운로드 |

#### 📤 제공 데이터 형식
- 생물 출현 기록 (Darwin Core 형식)
- 분류학적 체크리스트
- 데이터셋 메타데이터

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 데이터 인용 형식 | GBIF Secretariat (2022) 형식으로 인용 |
| 접근 방식 | 공개 (무료) |
| 표준 | Darwin Core |

#### ⚠️ 한계점
- gbif2022gbif 인용은 GBIF Secretariat 데이터 인용으로 전통적인 저널 논문이 아니다
- 데이터 품질이 제공 기관마다 다르며 오분류, 위치 오류가 존재할 수 있다
- 전 세계 생물다양성의 지리적·분류학적 편향이 있다 (유럽·북미 데이터 과잉 대표)

## 관련 정보
- **논문**: [GBIF: the global biodiversity information facility](https://www.gbif.org/)
