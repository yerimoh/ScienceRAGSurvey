---
title: "FactSage: thermochemical software suite"
bib_key: "factsage"
year: 1976
domain: material
type: dataset
venue: GTT-Technologies / CRCT (Commercial Software)
paper_link: https://www.factsage.com
---
# FactSage

factsage | 1976 | GTT-Technologies/CRCT (Commercial Software) | dataset | [material] | [website](https://www.factsage.com)

**DB**: FactSage 내장 열화학 데이터베이스 (순수 물질 FACT-Pure-Substances DB + 다성분 용융 상 FToxid, FTstel, FTsalt 등 솔루션 데이터베이스)
**DB size**: ~60,000개 화합물 및 다수의 다성분 용융 상 파라미터 세트 (공개 수치 제한적)
**DB Open/Private**: Subscription (상용 라이선스; 학술 및 무료 기본 버전 존재)
**Modality**: Tabular
**Retriever**: N/A (K4 상업용 시뮬레이터 — 직접 queryable API 없음)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: FactSage (GTT-Technologies / CRCT)

> GTT-Technologies/CRCT | 1976 | dataset | material
#### 📌 한 줄 요약
GTT-Technologies(독일)와 캐나다 CRCT(Polytechnique Montréal)가 공동 개발·유지하는 열화학 소프트웨어로, 야금·유리·세라믹·핵연료 공정에서 다성분 고온 반응의 CALPHAD 기반 상평형과 깁스 에너지 최소화를 계산하며, 철강·비철 야금 산업이 의존하는 가장 포괄적인 열역학 데이터베이스를 내장하고 있다.

#### 🎯 개발/구축 배경
**기존 열역학 계산 도구의 한계**
- 단순 이성분·삼성분 합금 시스템은 수동으로 계산 가능하나 다성분 슬래그·합금 시스템(Fe-Cr-Ni-O-S-...)은 전용 CALPHAD 데이터베이스 없이 계산 불가
- JANAF 같은 순수 성분 데이터는 다성분 혼합물의 용융 상거동을 기술하지 못함

**FactSage의 위치**
- CALPHAD 방법론의 산업 표준: 용융 합금, 슬래그, 용융 염의 비이상 용액 거동을 Modified Quasichemical Model(MQM) 등으로 기술
- 철강(FTstel), 산화물 슬래그(FToxid), 핵연료(FTnucl), 용융 염(FTsalt) 등 20개 이상의 전용 솔루션 데이터베이스
- 철강·알루미늄·구리 제련, 유리 제조, 원자로 핵연료 거동 예측에 산업 표준

#### 🔨 시스템 구성
- **FACT-Pure-Substances Database**: ~60,000 화합물의 열역학 데이터 (H, S, Cp, 상전이 엔탈피)
- **Solution Databases**: FToxid (산화물), FTstel (강철), FTsalt (용융 염), FTnucl (핵연료) 등
- **CALPHAD 엔진**: Gibbs energy minimization 기반 상평형 계산 (EquiliB, Phase Diagram 모듈)
- **공정 시뮬레이션**: 반응로 시뮬레이션(Reaction Web), 혼합 계산

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| FactSage GUI | 윈도우 기반 모듈 인터페이스 |
| FactSage Web (제한적) | 기본 계산 접근 (일부 기능 무료 제공) |
| ChemSheet/Matlab 연동 | Excel ChemSheet 또는 MATLAB 통한 배치 계산 |

#### 📤 제공 데이터 형식
- 상평형 결과: 안정 상 목록, 조성 (mol%)
- 깁스 에너지 함수 값, 화학 포텐셜
- 상다이어그램 (binary/ternary/pseudo-binary)
- 물성값: 밀도, 점도 (일부 데이터베이스)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| FACT 프로젝트 시작 | ~1976 (F*A*C*T 프로젝트) |
| 내장 화합물 수 (Pure-Substances) | ~60,000 |
| 솔루션 데이터베이스 수 | 20개 이상 (FToxid, FTstel, FTsalt 등) |
| 개발 기관 | GTT-Technologies(독일) + CRCT, Polytechnique Montréal(캐나다) |
| 공개 데이터베이스 규모 | 비공개 (상용 라이선스) |

**NOTE**: `factsage` 항목은 references.bib에 bib 엔트리가 존재하지 않음 (누락된 인용).

#### ⚠️ 한계점
- CALPHAD 솔루션 데이터베이스는 수십 년간 축적된 실험 데이터를 기반으로 하지만 파라미터 출처가 완전히 공개되지 않음
- 내장 데이터베이스는 소프트웨어 외부에서 직접 접근·질의 불가 (RAG 통합 불가)
- 특정 합금계나 신소재의 경우 검증된 CALPHAD 파라미터가 없어 외삽 오류 발생 가능

## 관련 정보
- **웹사이트**: [FactSage](https://www.factsage.com)
- **K4 분류**: Embedded in software — 야금·고온화학 tacit knowledge(CALPHAD 솔루션 파라미터)가 소프트웨어 데이터베이스에 내장됨
- **BIB 상태**: references.bib에 bib 엔트리 없음 — 추가 필요
