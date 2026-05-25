---
title: "Pro/II: Process engineering simulation software"
bib_key: "proii"
year: 1967
domain: chem
type: dataset
venue: AVEVA (formerly SimSci) (Commercial Software)
paper_link: https://www.aveva.com
---
# Pro/II

proii | 1967 | AVEVA (formerly SimSci) (Commercial Software) | dataset | [chem] | [website](https://www.aveva.com)

**DB**: Pro/II 내장 열역학·물성 데이터베이스 (SimSci 독자 물성 패키지 및 DIPPR 기반)
**DB size**: N/A (라이선스 소프트웨어, 공개 수치 없음)
**DB Open/Private**: Subscription (상용 라이선스)
**Modality**: Tabular
**Retriever**: N/A (K4 상업용 시뮬레이터 — 직접 queryable API 없음)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Pro/II (AVEVA, formerly SimSci)

> AVEVA (formerly SimSci) | 1967 | dataset | chem
#### 📌 한 줄 요약
SimSci(현 AVEVA)가 1967년 출시한 화학·석유화학 공정 시뮬레이터로, 정제(Refining)·가스처리 공정에 특화된 열역학 및 단위조작 지식을 내장 데이터베이스에 캡슐화하여 제공한다.

#### 🎯 개발/구축 배경
**기존 공정 설계의 한계**
- 1960년대 석유화학·정제 산업의 대형화에 따라 복잡한 multi-unit 공정 시뮬레이션 수요가 급증
- 정류탑(distillation), 흡수탑, 열교환기 네트워크를 연립방정식으로 동시에 풀 수 있는 steady-state 시뮬레이터가 필요

**Pro/II의 위치**
- 정유소(Refinery), LNG 처리 시설, 석유화학 플랜트 설계에서 Aspen Plus와 함께 가장 널리 사용되는 공정 시뮬레이터
- 특히 정제 공정(crude oil distillation, FCC, hydrocracking)에 특화된 경험적 파라미터 내장

#### 🔨 시스템 구성
- **열역학 패키지**: 다수의 상태방정식(SRK, PR, CPA 등) 및 활동도 계수 모델
- **단위조작**: 증류, 흡수, 추출, 반응, 압축, 열교환 등 포괄적 unit operation library
- **정제 전용 모델**: Crude assay 처리, petroleum fractions 물성 예측
- **물성 데이터베이스**: SimSci 독자 DB + DIPPR 기반 순수 성분 파라미터

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| AVEVA E3D/Pro/II GUI | 인터랙티브 공정 설계 환경 |
| COM/OLE Automation | 외부 스크립트에서 시뮬레이션 제어 (제한적) |
| 배치 실행 | .prz 파일 기반 커맨드라인 실행 |

#### 📤 제공 데이터 형식
- 스트림 조성 및 열역학 상태 (온도, 압력, 기액 분율)
- 단위조작 성능 (분리 효율, 에너지 소비)
- 공정 경제성 평가 (CAPEX/OPEX 추정)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 최초 출시 | 1967 (SimSci) |
| 현 소유사 | AVEVA (2017년 Schneider Electric 인수 후 2023년 독립) |
| 공개 데이터베이스 규모 | 비공개 (상용 라이선스) |

#### ⚠️ 한계점
- Aspen Plus와 마찬가지로 내장 지식이 소프트웨어 내에 캡슐화되어 외부 RAG 시스템에서 직접 접근 불가
- 정제 특화 경험적 파라미터(crude assay correlation 등)는 공개 문서화가 매우 제한적
- 새로운 바이오연료나 신소재 공정에 대한 파라미터 부족

## 관련 정보
- **웹사이트**: [AVEVA Pro/II](https://www.aveva.com/en/products/pro-ii/)
- **K4 분류**: Embedded in software — 정제·가스처리 tacit knowledge가 소프트웨어 파라미터베이스에 내장됨
