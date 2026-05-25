---
title: "Climate Change 2023: Synthesis Report"
bib_key: "lee2023climate"
year: 2023
domain: earth
type: dataset
venue: IPCC
paper_link: https://www.ipcc.ch/report/ar6/syr/
---
# Climate Change 2023: Synthesis Report

lee2023climate | 2023 | IPCC | dataset | [earth] | [paper](https://www.ipcc.ch/report/ar6/syr/)

**DB**: IPCC Sixth Assessment Report (AR6) Synthesis
**DB size**: 3개 실무그룹 보고서 + 3개 특별보고서 통합 (6,841개 검토 의견 처리)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: IPCC AR6 Synthesis Report

> IPCC | 2023 | dataset | earth
#### 📌 한 줄 요약
기후과학 분야의 표준 참조 문헌인 IPCC 제6차 평가 보고서(AR6) 종합 보고서 — 실무그룹 I·II·III의 성과를 통합한 권위 있는 기후 과학 합성 문서.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 기후 과학 문헌이 수천 편의 개별 논문으로 분산되어 있어 종합적 합의 파악이 어려움
- 정책 결정자들이 접근 가능한 형식으로 기후 과학 컨센서스를 정리한 단일 권위 문서 부재

**이 시스템이 필요한 이유**
- 기후과학 RAG 시스템(예: ChatClimate)이 참조 소스로 활용하는 분야의 표준 신뢰 문서
- 일반적인 서지 색인이 아닌, 분야 자체가 표준으로 인정하는 합성 문서로 기능
- 2011–2020년 평균 지구 표면 온도 상승(1850–1900년 대비 +1.1°C) 등 기후 과학의 기준 수치 제공

#### 🔨 시스템 구성
IPCC(Intergovernmental Panel on Climate Change)가 발행. 핵심 집필팀(Core Writing Team) 49명, 검토 편집자(Review Editors) 9명, 확장 집필팀 7명, 기여 저자 28명 — 총 93명의 저자 참여. 3개 실무그룹의 평가 보고서와 3개 특별보고서(지구온난화 1.5°C, 기후변화와 토지, 해양과 빙권)를 통합:
- **WGI**: 기후 과학의 물리적 기초 (2021)
- **WGII**: 영향, 적응, 취약성 (2022)
- **WGIII**: 기후변화 완화 (2022)

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 무료 PDF | ipcc.ch에서 전문 무료 다운로드 (정책결정자 요약, 확장 보고서, 전체 권호 별도 제공) |
| 온라인 열람 | IPCC 공식 웹사이트 인터랙티브 열람 가능 |
| 다국어 | UN 공용 6개 언어로 요약본 제공 |

#### 📤 제공 데이터 형식
- 정책결정자 요약(SPM): 19개 헤드라인 성명 (A·B·C 세 파트)
- 확장 보고서(Longer Report)
- 전체 권호(Full Volume)
- 그림 및 도표 (인터랙티브 온라인 버전 포함)
- 프레젠테이션 슬라이드 덱

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 핵심 집필팀 | **49명** |
| 검토 편집자 | **9명** |
| 기여 저자 | **28명** |
| 총 저자 | **93명** |
| 검토 의견 수 | **6,841개** (정부 6,636 + 관찰자 205) |
| 검토 참여 정부 수 | **47개국** |
| 통합 실무그룹 수 | **3개** (WGI·WGII·WGIII) |
| 통합 특별보고서 수 | **3개** |
| 헤드라인 성명 수 | **19개** |
| 기준 온도 상승폭 | **+1.1°C** (2011–2020 vs 1850–1900) |

#### ⚠️ 한계점
- **서지 색인이 아님**: 논문을 직접 색인하지 않으며, 출간된 기후 과학 문헌의 합성 문서 — 새 논문은 약 7년 주기의 평가 사이클 후에만 반영
- **고정 스냅샷**: 2022년까지의 문헌을 기반으로 하며, 2023년 이후 발표된 연구 결과는 미반영
- **PDF 전용**: 구조화된 API나 기계 판독 가능한 데이터베이스 형태가 아니므로 RAG 시스템 통합 시 PDF 파싱 필요
- **동료 심사 논문 대체 불가**: 일차 연구 문헌의 서지 데이터베이스가 아닌 합성 문서이므로 일반적인 문헌 검색 용도로 사용 불가

## 관련 정보
- **논문**: [https://www.ipcc.ch/report/ar6/syr/](https://www.ipcc.ch/report/ar6/syr/)
