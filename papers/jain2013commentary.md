---
title: "Commentary: The Materials Project: A materials genome approach to accelerating materials innovation"
bib_key: "jain2013commentary"
year: 2013
domain: material
type: dataset
venue: APL Materials
paper_link: https://doi.org/10.1063/1.4812323
---
# Commentary: The Materials Project: A materials genome approach to accelerating materials innovation

jain2013commentary | 2013 | APL Materials | dataset | [material] | [paper](https://doi.org/10.1063/1.4812323)

**DB**: Materials Project
**DB size**: 논문 기준 "all known inorganic materials"의 DFT 특성 계산 (2013년 기준 수만 개, 현재 ~15만 개 이상으로 성장)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Materials Project REST API (MPRester), www.materialsproject.org

> APL Materials | 2013 | dataset | material
#### 📌 한 줄 요약
미국 재료게놈이니셔티브(Materials Genome Initiative)의 핵심 프로그램으로, 모든 알려진 무기 재료의 DFT 계산 특성(전자 구조, 안정성, 탄성, 자성 등)을 무료로 제공하는 고처리량 재료 데이터베이스.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 새로운 재료 발견·최적화는 수년의 실험 시간과 높은 비용을 요구
- 계산 재료과학 데이터가 개별 연구 그룹에 분산되어 재현·공유가 어려움
- 새로운 기능성 재료 탐색(배터리, 태양전지, 촉매 등)에 체계적 데이터 인프라 부재

**이 시스템이 필요한 이유**
- 고처리량 DFT 계산으로 재료 특성 데이터를 대규모로 자동 생성·축적
- 인실리코(in silico) 재료 설계 및 데이터 기반 발견을 위한 오픈 플랫폼 필요
- 인터랙티브 탐색과 데이터 마이닝을 모두 지원하는 다채널 접근 환경 요구

#### 🔨 시스템 구성
Materials Project는 VASP 기반 DFT 계산 엔진으로 무기 결정 구조의 전자 구조, 형성 에너지, 밴드갭, 탄성 상수, 자성 특성, Li 이온 배터리 삽입 전압 등 다수의 특성을 자동 계산한다. 계산 결과는 MongoDB 기반 데이터베이스에 저장되며 Materials Project API(MPRester)를 통해 프로그래밍 방식으로 접근 가능하다. FireWorks 워크플로 엔진과 pymatgen 오픈소스 라이브러리 생태계와 연계된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 포털 | www.materialsproject.org — 인터랙티브 구조 탐색, 대시보드 |
| REST API | MPRester (Python) — 구조·특성 쿼리, 재료 ID(mp-xxx) 기반 조회 |
| 데이터 마이닝 | 오픈 데이터셋 다운로드 지원 |

#### 📤 제공 데이터 형식
- 결정 구조 (CIF, POSCAR 형식)
- DFT 계산 특성: 형성 에너지, 밴드갭, 전자 상태밀도, 탄성 상수
- Li/Na/K 이온 배터리 삽입 전압, 용량, 확산 계수
- 표면 에너지, 작업 함수
- 자기 모멘트, 자성 배열

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 데이터베이스 목표 | 모든 알려진 무기 재료의 DFT 특성 계산 |
| 계산 엔진 | VASP (GGA + U, HSE06 선택적) |
| API 방식 | REST API (MPRester), 무료·오픈 |
| 논문 출판 연도 | 2013 (APL Materials vol.1, no.1) |

#### ⚠️ 한계점
- 논문 출판 시점(2013)에는 데이터베이스 규모가 상대적으로 작았으며, 이후 지속적으로 확장됨 (논문에 구체적 레코드 수 미기재)
- DFT 계산값이므로 실험값과 체계적 오차 존재 (예: GGA 밴드갭 과소평가)
- 주로 정적(0 K) 특성에 집중하며, 유한 온도·압력 조건 특성은 별도 처리 필요
- 구조 안정성 예측이 핵심이나 합성 가능성까지 보장하지는 않음

## 관련 정보
- **논문**: [Commentary: The Materials Project (APL Materials, 2013)](https://doi.org/10.1063/1.4812323)
