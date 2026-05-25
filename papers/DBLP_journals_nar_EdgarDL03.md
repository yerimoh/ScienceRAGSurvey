---
title: "Gene Expression Omnibus: NCBI gene expression and hybridization array data repository"
bib_key: "DBLP:journals/nar/EdgarDL03"
year: 2002
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/30.1.207
---
# Gene Expression Omnibus: NCBI gene expression and hybridization array data repository

DBLP:journals/nar/EdgarDL03 | 2002 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/30.1.207)

**DB**: GEO (Gene Expression Omnibus)
**DB size**: 고처리량 유전자 발현 및 게놈 혼성화 실험 데이터의 공개 저장소 (3개 핵심 엔티티: 플랫폼, 샘플, 시리즈)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NCBI GEO 웹 (http://www.ncbi.nlm.nih.gov/geo)

> Nucleic Acids Research | 2002 | dataset | bio
#### 📌 한 줄 요약
고처리량 유전자 발현 데이터의 증가하는 수요에 대응하여 NCBI가 구축한 공개 저장소로, 플랫폼(프로브 목록), 샘플(측정 데이터), 시리즈(실험 묶음) 세 가지 핵심 데이터 엔티티로 구성된다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 고처리량 유전자 발현 데이터에 대한 공개 저장소의 수요가 급증하였으나 중앙 집중식 공개 데이터 허브가 부재했다
- 개별 연구실의 데이터베이스는 특정 분석 방법에 특화되어 있어 데이터 공유와 재활용에 한계가 있었다

**이 시스템이 필요한 이유**
- GEO는 개별 유전자 발현 데이터베이스를 대체하지 않고 보완하는 3차 중앙 데이터 배포 허브로 설계
- 유전자 발현 및 게놈 혼성화 실험의 이종 데이터셋을 제출·저장·검색할 수 있는 유연하고 개방된 설계
- 국제 공개 데이터 공유 요건을 충족하는 표준화된 제출 플랫폼 제공

#### 🔨 시스템 구성
GEO의 세 가지 핵심 데이터 엔티티: (1) **플랫폼(Platform)** — 어떤 분자 집합을 검출할 수 있는지 정의하는 프로브 목록, (2) **샘플(Sample)** — 측정 대상 분자 집합을 기술하고 단일 플랫폼을 참조하는 분자 풍도 데이터, (3) **시리즈(Series)** — 실험을 구성하는 의미 있는 데이터셋으로 샘플들을 조직화. GEO는 http://www.ncbi.nlm.nih.gov/geo를 통해 공개 접근 가능하다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | http://www.ncbi.nlm.nih.gov/geo — 무료 브라우저 검색 |
| SOFT 형식 다운로드 | 플랫폼·샘플·시리즈 데이터 다운로드 |

#### 📤 제공 데이터 형식
- SOFT (Simple Omnibus Format in Text) 형식
- 플랫폼 정의 파일
- 샘플 분자 풍도 데이터
- 시리즈 메타데이터

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 핵심 데이터 엔티티 | **3개** (Platform, Sample, Series) |
| 설립 기관 | NCBI, NLM, NIH |
| 접근 방식 | 공개 웹 (무료) |

#### ⚠️ 한계점
- GEO는 분석 특화 인하우스 데이터베이스를 대체하지 않고 보완하는 중앙 허브로 설계되어 직접 분석 기능이 제한적이다
- 이종 데이터셋 간 표준화(정규화)가 제출자에 따라 달라 직접 비교에 주의가 필요하다
- 2002년 창립 논문으로 초기 수록 데이터셋 수가 현재에 비해 매우 적었다

## 관련 정보
- **논문**: [Gene Expression Omnibus: NCBI gene expression and hybridization array data repository](https://doi.org/10.1093/nar/30.1.207)
