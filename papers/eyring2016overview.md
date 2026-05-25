---
title: "Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6) Experimental Design and Organization"
bib_key: "eyring2016overview"
year: 2016
domain: earth, climate
type: dataset
venue: Geoscientific Model Development
paper_link: https://doi.org/10.5194/gmd-9-1937-2016
---
# Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6) Experimental Design and Organization

eyring2016overview | 2016 | Geoscientific Model Development | dataset | [earth, climate] | [paper](https://doi.org/10.5194/gmd-9-1937-2016)

**DB**: CMIP6 — Coupled Model Intercomparison Project Phase 6
**DB size**: Petabyte-scale; ~20 PB 이상 (전 세계 49개 모델링 그룹, 100여 개 기후 모델; 볼륨은 실제 생산 후 추정치)
**DB Open/Private**: Open (ESGF 통해 공개 배포)
**Modality**: ['NetCDF', 'Simulation output', 'Time series']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CMIP6 / ESGF (Earth System Grid Federation)

> Geoscientific Model Development | 2016 | dataset | earth, climate
#### 한 줄 요약
전 세계 기후 모델링 그룹의 지구 시스템 모델(ESM) 시뮬레이션을 조율·통합하는 CMIP6 설계 및 조직 논문. IPCC 제6차 평가 보고서(AR6)의 과학적 기반이 되는 **페타바이트 규모** 기후 시뮬레이션 데이터를 ESGF를 통해 공개 배포. 과거·현재·미래 기후 시나리오 시뮬레이션의 표준 프로토콜을 정의.

#### 개발/구축 배경
**기존 인프라의 한계**
- CMIP1–5는 개별 실험 설계로 모델 간 비교가 어렵고 커버리지 불균일
- CMIP5 이후 지구 시스템 모델 복잡성 증가 (탄소 순환, 에어로졸, 해양 생지화학 결합)
- 단일 모델 앙상블로는 내부 변동성과 모델 불확도 구분 불가

**이 시스템이 필요한 이유**
- IPCC AR6 과학적 근거 확보를 위한 다중 모델 앙상블 표준 필요
- 기후 변화 원인 규명(Detection & Attribution), 지역 영향 평가, 탄소 예산 추정 등 정책 관련 질문에 답하기 위한 체계적 실험 설계
- ScenarioMIP(SSP 경로), HighResMIP, AerChemMIP 등 18개 상호 비교 프로젝트(MIP) 통합 조율

#### 시스템 구성
CMIP6는 WCRP(세계기후연구프로그램)가 주관하며 3단계로 구성:
1. **DECK(Diagnostic, Evaluation and Characterization of Klima)**: 4가지 표준 실험 (piControl, historical, AMIP, abrupt4×CO₂) — 모든 참여 모델 의무
2. **Historical 시뮬레이션**: 1850–2014 관측 기반 강제력
3. **선택적 MIPs**: 21개 CMIP6-Endorsed MIP (ScenarioMIP, HighResMIP, PMIP, AerChemMIP 등)

데이터 배포: ESGF (Earth System Grid Federation) — 분산 페더레이션 아카이브, 전 세계 노드 운영.

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| ESGF 포털 | esgf-node.llnl.gov 등 — 웹 탐색·다운로드 |
| ESMValTool | Python 기반 진단·분석 도구 |
| Pangeo | 클라우드 기반 Zarr 포맷 접근 (Google Cloud, AWS) |
| intake-esm | Python 카탈로그 기반 검색 |

#### 제공 데이터 형식
- NetCDF-4 (CF Conventions)
- 변수: 대기(300+), 해양, 해빙, 육지, 에어로졸, 탄소 순환
- 시간 해상도: 서브일~월~연 평균
- 공간 해상도: 25km~200km (모델별 상이)

#### 주요 통계
| 항목 | 수치 |
|---|---|
| 참여 모델링 그룹 | **~49** 개 (전 세계) |
| 모델 수 | **100+** 개 ESM/GCM |
| 총 데이터 볼륨 | **~20 PB** 이상 (추산) |
| MIP 수 | **21** 개 (CMIP6-Endorsed MIPs, 논문 확인) |
| DECK 실험 | **4** 개 (의무) |
| 지원 IPCC 보고서 | AR6 (2021) |

#### 한계점
- 모델 해상도 한계: 대부분 100km 수준으로 극단 기상 사건·지역 기후 시뮬레이션 부족 (HighResMIP에서 일부 해결)
- 데이터 볼륨이 매우 커 일반 연구자의 로컬 다운로드 비현실적 → 클라우드 분석 필요
- NetCDF/CF 규약에 대한 도메인 지식 없이 RAG 파이프라인에서 직접 활용 어려움
- 모델 간 변수명·그리드 불균일 → 표준화 처리 필요

## 관련 정보
- **논문**: [https://doi.org/10.5194/gmd-9-1937-2016](https://doi.org/10.5194/gmd-9-1937-2016)
- **ESGF 포털**: [https://esgf-node.llnl.gov/projects/cmip6/](https://esgf-node.llnl.gov/projects/cmip6/)
