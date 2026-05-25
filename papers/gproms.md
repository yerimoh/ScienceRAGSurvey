---
title: "gPROMS: Advanced process modeling software"
bib_key: "gproms"
year: 1990
domain: chem
type: dataset
venue: PSE (Process Systems Enterprise) / Siemens (Commercial Software)
paper_link: https://www.siemens.com/global/en/products/automation/industry-software/gproms.html
---
# gPROMS

gproms | 1990 | PSE/Siemens (Commercial Software) | dataset | [chem] | [website](https://www.siemens.com/global/en/products/automation/industry-software/gproms.html)

**DB**: gPROMS 내장 물성 데이터베이스 (INFOCHEM Multiflash 또는 CAPE-OPEN 기반 열역학 패키지 연동)
**DB size**: N/A (라이선스 소프트웨어, 공개 수치 없음)
**DB Open/Private**: Subscription (상용 라이선스)
**Modality**: Tabular
**Retriever**: N/A (K4 상업용 시뮬레이터 — 직접 queryable API 없음)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: gPROMS (PSE/Siemens)

> PSE/Siemens | ~1990 | dataset | chem
#### 📌 한 줄 요약
Process Systems Enterprise(PSE, 현 Siemens 자회사)가 개발한 고급 공정 모델링 플랫폼으로, 미분대수방정식(DAE) 기반 first-principles 모델링을 지원하며 정밀 열역학·전달현상 파라미터를 내장하여 배터리, 제약, 정제 공정 등의 고정밀 시뮬레이션에 활용된다.

#### 🎯 개발/구축 배경
**기존 공정 시뮬레이터의 한계**
- Aspen Plus, Pro/II 같은 steady-state 시뮬레이터는 단순화된 shortcut 모델 위주로 first-principles 동역학 모델 구현이 제한적
- 제약 결정화, 배터리 전극 반응, 막분리(membrane separation) 같은 복잡한 물리화학 현상을 정밀 모델링하려면 DAE 기반 플랫폼이 필요

**gPROMS의 위치**
- "Advanced Process Modeling" 영역: Aspen Plus/Pro/II보다 한 단계 높은 정밀도의 first-principles 모델링을 지원
- 배터리 셀 설계(gPROMS FormulatedProducts), 제약 공정(gPROMS Pharmaceutical), LNG 액화 공정에서 industry 표준

#### 🔨 시스템 구성
- **모델링 언어**: 독자적 DAE 기반 equation-oriented 모델링 언어 (gML)
- **열역학 패키지**: CAPE-OPEN 인터페이스를 통해 Multiflash, Aspen Properties 등 외부 물성 엔진 연동
- **최적화 엔진**: 모델 기반 최적화(MBO) 및 파라미터 추정 기능 내장
- **물성 데이터베이스**: INFOCHEM Multiflash 기반 상평형 및 전달 파라미터

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| gPROMS GUI | Process Builder 기반 모델 구성 및 실행 |
| Python API | gPROMS ModelBuilder Python Interface |
| CAPE-OPEN | 표준 CAPE-OPEN 인터페이스를 통한 타 플랫폼 연동 |

#### 📤 제공 데이터 형식
- 시뮬레이션 결과: 상태 변수 프로파일 (시간/공간 분포)
- 파라미터 추정 결과: 동역학 파라미터, 물성 파라미터
- 최적화 보고서: 설계 변수 및 목적함수 값

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 최초 상업 출시 | ~1990년대 초 (PSE 설립 1991년) |
| 현 소유사 | Siemens AG (2019년 PSE 인수) |
| 공개 데이터베이스 규모 | 비공개 (상용 라이선스) |

**NOTE**: `gproms` 항목은 references.bib에 bib 엔트리가 존재하지 않음 (누락된 인용).

#### ⚠️ 한계점
- first-principles 모델 구축에 전문적인 화학공학 지식이 필요하여 진입 장벽이 높음
- 내장 물성 데이터베이스는 CAPE-OPEN 표준을 통해 간접 접근만 가능하며 RAG 시스템과 직접 통합 불가
- 소규모 연구실 환경에서는 라이선스 비용이 부담

## 관련 정보
- **웹사이트**: [Siemens gPROMS](https://www.siemens.com/global/en/products/automation/industry-software/gproms.html)
- **PSE 원본**: [PSE gPROMS](https://www.psenterprise.com/products/gproms)
- **K4 분류**: Embedded in software — 고급 공정 모델링 tacit knowledge(DAE 파라미터, 물성 상관식)가 소프트웨어에 내장됨
- **BIB 상태**: references.bib에 bib 엔트리 없음 — 추가 필요
