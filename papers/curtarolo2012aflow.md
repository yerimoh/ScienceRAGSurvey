---
title: "AFLOW: An automatic framework for high-throughput materials discovery"
bib_key: "curtarolo2012aflow"
year: 2012
domain: material
type: dataset
venue: Computational Materials Science
paper_link: https://doi.org/10.1016/j.commatsci.2012.02.005
---
# AFLOW: An automatic framework for high-throughput materials discovery

curtarolo2012aflow | 2012 | Computational Materials Science | dataset | [material] | [paper](https://doi.org/10.1016/j.commatsci.2012.02.005)

**DB**: AFLOW (Automatic Flow) / AFLOWLIB
**DB size**: 논문 기준 합금·금속간화합물·무기화합물 대규모 고처리량 계산 (구체적 수치는 지속 확장)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: AFLOW REST API / AFLOWLIB (aflowlib.duke.edu)

> Computational Materials Science | 2012 | dataset | material
#### 📌 한 줄 요약
Duke대학교 Curtarolo 그룹이 개발한 고처리량 재료 계산 자동화 프레임워크로, 합금·금속간화합물·무기화합물의 결정 구조 특성을 자동 계산하여 AFLOWLIB 데이터베이스에 공개한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 계산 재료과학의 가능성에도 불구하고 체계적·자동화된 대규모 데이터 생성 인프라 부재
- 개별 연구자의 수동 계산으로는 광대한 합금·화합물 공간 탐색 불가
- 기하학 구조 분석, 전자 구조 계산, 결과 후처리를 통합하는 워크플로 도구 필요

**이 시스템이 필요한 이유**
- 합금 설계, 초경질 재료, 형상기억합금 등 다양한 응용에서 대규모 데이터 필요
- 고처리량 계산으로 미실현 화합물의 존재 및 특성 예측 가능
- 재료 연구 컨소시엄을 통한 오픈 데이터 공유로 커뮤니티 활용 극대화

#### 🔨 시스템 구성
AFLOW는 VASP 기반 DFT 계산의 자동화 파이프라인 소프트웨어 프레임워크이다. 결정 구조 생성, k-포인트 선택, 계산 설정, 자동 수렴 확인, 결과 파싱 등 전체 워크플로를 자동화한다. 기하학 구조 분석(대칭군, 위그너-자이츠 셀)과 전자 구조 계산(밴드 구조, 상태밀도)이 통합되며, AFLOWLIB.org 웹사이트에서 계산 결과를 오픈 데이터로 제공한다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 포털 | aflowlib.duke.edu — 인터랙티브 탐색 및 온라인 도구 |
| REST API | AFLOWLIB REST API — 구조·특성 데이터 접근 |
| 소프트웨어 | AFLOW 소프트웨어 패키지 — 로컬 실행 |

#### 📤 제공 데이터 형식
- 결정 구조 (CIF, POSCAR)
- 전자 밴드 구조, 상태밀도 (DOS)
- 형성 에너지, 안정성 데이터
- 탄성 상수, 디바이 온도
- 열전 특성 (일부)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 계산 대상 | 합금, 금속간화합물, 무기화합물 |
| 계산 엔진 | VASP (GGA-PBE) |
| 소프트웨어 공개 | 오픈소스 (재료 연구 컨소시엄 웹사이트) |
| 논문 출판 연도 | 2012 (Comput. Mater. Sci. vol.58) |

#### ⚠️ 한계점
- 2012년 원본 논문에 구체적 데이터베이스 레코드 수치 미기재 (이후 AFLOWLIB 확장)
- Materials Project, OQMD와 DFT 설정(에너지 컷오프, 슈도포텐셜 등)이 상이하여 교차 비교 시 주의 필요
- RAG 시스템에서는 AFLOW/OQMD 모두 현재까지 실질적 활용 사례 거의 없음 (survey 기준)
- 구조 최적화 자동화 중 특정 복잡계에서 수렴 실패 가능성

## 관련 정보
- **논문**: [AFLOW: An automatic framework for high-throughput materials discovery (Comput. Mater. Sci., 2012)](https://doi.org/10.1016/j.commatsci.2012.02.005)
