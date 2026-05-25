---
title: "Europe PMC in 2023"
bib_key: "europepmc2024"
year: 2024
domain: medical, bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad1085
---
# Europe PMC in 2023

europepmc2024 | 2024 | Nucleic Acids Research | dataset | [medical, bio] | [paper](https://doi.org/10.1093/nar/gkad1085)

**DB**: Europe PMC open-access life science literature database
**DB size**: 42M+ abstracts, 9M+ full-text articles, 650K+ preprints (2023년 9월 15일 기준)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Europe PMC REST API / Bulk download

> Nucleic Acids Research | 2024 | dataset | medical, bio
#### 📌 한 줄 요약
EMBL-EBI가 운영하며 37개 국제 연구 펀딩 기관이 지원하는 생명과학 오픈 액세스 문헌 플랫폼. **4,200만 개 이상**의 초록과 **900만 개 이상**의 전문 기사를 제공하며, **31개 프리프린트 서버**에서 수집한 **65만 개 이상**의 프리프린트와 **20억 개 이상**의 텍스트 마이닝 주석을 RESTful API로 무료 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 생명과학 오픈 액세스 문헌을 통합하여 무료로 제공하는 인프라의 필요성
- 프리프린트 서버가 난립하여 동료심사 전 최신 연구를 통합 탐색하기 어려움
- 텍스트 마이닝을 위한 구조화된 주석 데이터의 공개 제공 부재

**이 시스템이 필요한 이유**
- ELIXIR Core Data Resource 및 Global Core Biodata Resource로 지정된 핵심 인프라
- 37개 국제 연구 펀딩 기관이 후원하는 연구 성과물을 오픈 액세스로 집적
- 2018년 9개 서버에서 시작하여 2023년 31개 서버로 프리프린트 통합 확장

#### 🔨 시스템 구성
EMBL-EBI가 호스팅하는 오픈 액세스 플랫폼. 콘텐츠는 매일 업데이트되며, 60개 이상의 생명과학 데이터베이스·인용·펀딩·프로토콜·동료심사 자료와 연계된 풍부한 메타데이터를 제공한다. Unpaywall을 통해 1,300만 개 이상의 출판물에 무료 전문 링크를 연결. 프리프린트 수록 기준(2023년 3월 신설): 무료 접근, 생명과학 주요 콘텐츠, 심사 절차 보유, 표절·위법 행위 정책, 최소 30건 이상, 기계가독성 메타데이터 제공 조건 모두 충족 필요. 텍스트 마이닝 API 등 신규 코드는 GitLab에 오픈 소스로 공개(2022년 POSI 채택).

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹사이트 | europepmc.org — 브라우저 기반 탐색 |
| REST API | RESTful API — 무료, 일일 업데이트 |
| 벌크 다운로드 | 5.7M 오픈 액세스 기사 (PDF·XML), 매주 업데이트, 분기별 아카이브 |

#### 📤 제공 데이터 형식
- 초록, 전문(오픈 액세스 기사), 메타데이터 (제목, 저자, 저널, PMID/PMCID/DOI)
- 텍스트 마이닝 주석 20B+: 유전자/단백질명, 유기체, 질환, 화학물질
- Preprint Evaluations API: DocMaps 프레임워크 기반 동료 리뷰 보고서 메타데이터
- Article Status Monitor: 출판 생애주기 추적 (CSV 내보내기, POST REST API)
- 기관 ROR ID 매핑 (41% 기관, 80%+ 그랜트 PI)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 전체 초록 | **42M+** (2023년 9월 15일 기준) |
| 전문(full text) 기사 | **9M+** (2023년 9월 15일 기준) |
| 프리프린트 (전체) | **650,000+** (2023년 9월 15일 기준) |
| 프리프린트 (전문 보유) | **53,624** (2023년 9월 15일 기준) |
| COVID-19 프리프린트 전문 | **65,000+** |
| 통합 프리프린트 서버 | **31개** (2023년 기준) |
| 텍스트 마이닝 주석 | **2B+** |
| 오픈 액세스 PDF 벌크 다운로드 | **5.7M** |
| 후원 펀딩 기관 | **37개** |
| Unpaywall 전문 링크 연결 | **13M+** |

#### ⚠️ 한계점
- **프리프린트 철회/삭제 추적**: 전문을 보유한 프리프린트에 대해서만 가능; 초록만 수록된 프리프린트의 철회 상태는 중앙 집중적 추적 불가
- **프리프린트 버전 링크 불가**: bioRxiv, medRxiv처럼 버전 간 DOI를 재사용하는 서버에서는 버전 간 링크 연결 불가
- **프리프린트-저널 논문 매칭 한계**: 저자나 제목이 크게 변경된 경우 프리프린트와 최종 출판 논문 간의 매핑 실패 가능

## 관련 정보
- **논문**: [https://doi.org/10.1093/nar/gkad1085](https://doi.org/10.1093/nar/gkad1085)
