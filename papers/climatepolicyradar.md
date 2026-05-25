---
title: "Climate Policy Radar: A database of climate change laws and policies"
bib_key: "climatepolicyradar"
year: 2024
domain: earth
type: dataset
venue: Climate Policy Radar (misc)
paper_link: https://www.climatepolicyradar.org/
---
# Climate Policy Radar

climatepolicyradar | 2024 | Climate Policy Radar | dataset | [earth] | [portal](https://www.climatepolicyradar.org/)

**DB**: Climate Policy Radar — climate change laws, policies, and UNFCCC submissions
**DB size**: 수만 건의 기후 정책 문서 (국가 법률, NDC, LTS, UNFCCC 제출서 포함; 200개+ 국가)
**DB Open/Private**: Open (공개 검색, 일부 API 접근)
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Climate Policy Radar 포털 / API (app.climatepolicyradar.org)

> Climate Policy Radar | 2024 | dataset | earth
#### 📌 한 줄 요약
190개 이상 국가의 기후변화 관련 법률, 정책, UNFCCC 제출문서(NDC, LTS 등)를 수집·구조화한 공개 텍스트 데이터베이스. 과학적 기후 아카이브(CMIP6, NOAA NCEI)를 보완하는 정책 문서 코퍼스로, RAG 시스템의 기후 정책 질의응답을 위한 텍스트 기반 K3 자원.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 국가별 기후 정책 문서가 분산·비표준화되어 비교 분석 불가
- UNFCCC, IPCC 등 공식 기구 문서가 체계적으로 색인화되지 않아 검색 어려움
- 기후 과학 RAG 시스템이 정책 문서를 검색 코퍼스로 활용하는 사례 부재

**이 시스템이 필요한 이유**
- 기후 과학 데이터(관측·시뮬레이션)와 기후 정책 텍스트를 연결하는 K3 자원 필요
- 연구자·정책 입안자·시민사회가 국가별 기후 공약 이행 현황 검색 가능
- NLP 기반 기후 정책 분석(Climate R2AG 등)의 텍스트 기반 검색 코퍼스 제공

#### 🔨 시스템 구성
Climate Policy Radar는 자동화 크롤링+수작업 큐레이션으로 기후 관련 법률·정책 문서를 수집. 각 문서는 국가, 문서 유형(법률/NDC/LTS 등), 연도, 섹터(에너지/교통/농업 등) 메타데이터와 함께 색인화. 전문 텍스트 검색(벡터+키워드)과 API를 통해 접근 가능.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 포털 | app.climatepolicyradar.org — 키워드/필터 검색 |
| 공개 API | api.climatepolicyradar.org — 문서 메타데이터·텍스트 접근 |
| 데이터 다운로드 | 일부 데이터셋 공개 다운로드 지원 |

#### 📤 제공 데이터 형식
- 기후 법률 및 정책 문서 (PDF 원문 + 추출 텍스트)
- UNFCCC NDC (Nationally Determined Contributions) 전문
- LTS (Long-term Strategies), NZT (Net Zero Targets) 문서
- 문서 메타데이터: 국가, 연도, 유형, 섹터 분류

#### 📊 주요 통계 (공식 자료 기준)
| 항목 | 수치 |
|---|---|
| 커버 국가 수 | **200개+** |
| 문서 유형 | 국가 기후법 · NDC · LTS · UNFCCC 제출 |
| 접근 방식 | 공개 (무료) |
| 설립 | 2020 (Climate Policy Radar Ltd., 영국 비영리) |

#### ⚠️ 한계점
- 정책 문서 텍스트 중심으로, 과학적 수치·데이터(관측값, 시뮬레이션)는 포함 안 함
- 일부 국가 문서는 번역 없이 원문 언어로만 제공
- 논문(학술지 게재) 형태가 아닌 @misc 참고 항목이므로 학술적 인용 시 주의
- survey에서는 "none of them appears as a retrieval corpus in any catalogued scientific RAG system" 분류

## 관련 정보
- **포털**: [https://www.climatepolicyradar.org/](https://www.climatepolicyradar.org/)
- **앱**: [https://app.climatepolicyradar.org/](https://app.climatepolicyradar.org/)
