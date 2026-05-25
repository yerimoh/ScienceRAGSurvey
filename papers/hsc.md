---
title: "HSC Chemistry: thermodynamic and metallurgical calculation software"
bib_key: "hsc"
year: 1974
domain: material
type: dataset
venue: Metso Outotec (Outotec) (Commercial Software)
paper_link: https://www.mogroup.com/portfolio/hsc-chemistry/
---
# HSC Chemistry

hsc | ~1974 | Metso Outotec (Commercial Software) | dataset | [material] | [website](https://www.mogroup.com/portfolio/hsc-chemistry/)

**DB**: HSC Chemistry 내장 열역학 데이터베이스 (약 30,000개 화학종의 엔탈피·엔트로피·열용량 등 표준 열역학 데이터)
**DB size**: ~30,000 화학종 (버전에 따라 상이, 비공개 정밀 수치)
**DB Open/Private**: Subscription (상용 라이선스)
**Modality**: Tabular
**Retriever**: N/A (K4 상업용 시뮬레이터 — 직접 queryable API 없음)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: HSC Chemistry (Metso Outotec)

> Metso Outotec | ~1974 | dataset | material
#### 📌 한 줄 요약
Outotec(현 Metso Outotec)이 개발한 야금학 특화 열역학 계산 소프트웨어로, 약 30,000개 화학종의 열역학 데이터(H, S, Cp)를 내장하여 고온 야금 공정(제련, 소성, 침출)의 물질·에너지 수지, 상평형, 깁스 에너지 최소화를 계산한다.

#### 🎯 개발/구축 배경
**기존 야금 계산의 한계**
- 제련소, 광산 처리 공정에서 다성분 고온 반응의 평형 산출물 예측은 수작업으로 불가능
- JANAF, NIST-JANAF 등 개별 데이터 테이블에서 수동으로 추출하는 방법은 시간 소모적이고 오류 발생 가능성이 높음

**HSC Chemistry의 위치**
- 비철 금속 제련(구리, 니켈, 납, 아연), 철강, 시멘트, 무기화학 공정 분야의 야금 열역학 표준 도구
- 고온(수백~수천 도) 반응 평형 및 ellingham diagram 계산에 특화

#### 🔨 시스템 구성
- **열역학 데이터베이스**: ~30,000개 화학종의 H°, S°, Cp(T) 다항식 계수 내장
- **깁스 에너지 최소화**: 다성분 고온 반응 평형 산출물 자동 계산
- **물질·에너지 수지**: 유닛 공정의 mass/energy balance 계산
- **Eh-pH 다이어그램**: Pourbaix diagram 생성
- **HSC Sim**: 공정 시뮬레이션 모듈

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| HSC Chemistry GUI | 윈도우 기반 인터페이스에서 반응 입력 및 결과 확인 |
| 데이터베이스 검색 | 내장 DB에서 화학종 검색 및 물성값 조회 |
| 스프레드시트 연동 | Excel 연동을 통한 결과 내보내기 |

#### 📤 제공 데이터 형식
- 반응 평형 산출물 조성 (mol%)
- 열역학 함수 값 (ΔG, ΔH, ΔS, Keq)
- Ellingham diagram, Pourbaix diagram
- 물질·에너지 수지 표

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 내장 화학종 수 | ~30,000 (버전별 상이) |
| 적용 온도 범위 | 25°C ~ 수천°C |
| 개발사 | Metso Outotec (핀란드) |
| 공개 데이터베이스 규모 | 비공개 (상용 라이선스) |

**NOTE**: `hsc` 항목은 references.bib에 bib 엔트리가 존재하지 않음 (누락된 인용).

#### ⚠️ 한계점
- 내장 열역학 데이터베이스는 소프트웨어 내에 캡슐화되어 외부 RAG 시스템에서 직접 접근·질의 불가
- 데이터베이스 출처(원본 실험 측정값 vs. 추정값)에 대한 메타데이터가 제한적으로 제공됨
- 용융 합금 시스템의 CALPHAD 수준 계산에는 FactSage 같은 다성분 용융 데이터베이스가 더 적합

## 관련 정보
- **웹사이트**: [Metso Outotec HSC Chemistry](https://www.mogroup.com/portfolio/hsc-chemistry/)
- **K4 분류**: Embedded in software — 야금학·고온 열역학 tacit knowledge(화학종 열역학 데이터)가 소프트웨어 데이터베이스에 내장됨
- **BIB 상태**: references.bib에 bib 엔트리 없음 — 추가 필요
