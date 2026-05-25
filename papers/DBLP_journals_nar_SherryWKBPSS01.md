---
title: "dbSNP: the NCBI database of genetic variation"
bib_key: "DBLP:journals/nar/SherryWKBPSS01"
year: 2001
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/29.1.308
---
# dbSNP: the NCBI database of genetic variation

DBLP:journals/nar/SherryWKBPSS01 | 2001 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/29.1.308)

**DB**: dbSNP (NCBI Database of Single Nucleotide Polymorphisms)
**DB size**: 유전체 변이의 일반 카탈로그 — 대규모 연관 연구·유전자 지도 작성·진화생물학 설계를 위한 공개 데이터베이스
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NCBI 웹/FTP (http://www.ncbi.nlm.nih.gov/SNP)

> Nucleic Acids Research | 2001 | dataset | bio
#### 📌 한 줄 요약
NCBI가 구축한 유전체 변이의 일반 카탈로그로, GenBank, PubMed, LocusLink, 인간 게놈 프로젝트 데이터와 통합되며 연관 연구·유전자 지도·진화생물학 연구에 필요한 대규모 표본 설계를 지원한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 연관 연구, 유전자 지도 작성, 진화생물학에 요구되는 대규모 표본 설계를 위해 게놈 변이의 일반 카탈로그가 필요했다 (1999년 Genome Research 논문으로 처음 제안)
- 개별 연구실에서 발견된 SNP 데이터가 분산되어 있어 통합 접근이 어려웠다

**이 시스템이 필요한 이유**
- 단일 염기 다형성(SNP), 소규모 삽입/결실, 미소위성 등 다양한 유형의 유전체 변이를 단일 카탈로그로 통합
- NCBI의 GenBank, PubMed, LocusLink, 인간 게놈 프로젝트 데이터와 통합하여 컨텍스트 제공
- 공개 웹 및 익명 FTP를 통해 연구 커뮤니티에 무료 제공

#### 🔨 시스템 구성
dbSNP은 NCBI에서 운영하며 다양한 유형의 유전체 변이를 수집·통합한다. 제출된 데이터는 GenBank, PubMed(문헌), LocusLink(유전자 위치), 인간 게놈 프로젝트 데이터와 연결된다. 웹 인터페이스(http://www.ncbi.nlm.nih.gov/SNP)와 익명 FTP(ftp://ncbi.nlm.nih.gov/snp/)를 통해 전체 콘텐츠에 접근 가능하다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | http://www.ncbi.nlm.nih.gov/SNP — 무료 브라우저 검색 |
| 익명 FTP | ftp://ncbi.nlm.nih.gov/snp/ — 다양한 형식의 전체 다운로드 |

#### 📤 제공 데이터 형식
- SNP 제출 데이터 (다양한 형식)
- GenBank/PubMed/LocusLink/인간 게놈 프로젝트와의 교차 참조
- 염색체 위치 정보

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 설립 기관 | NCBI (National Center for Biotechnology Information), NLM, NIH |
| 통합 데이터 | GenBank, PubMed, LocusLink, Human Genome Project |
| 접근 방식 | 공개 웹 + 익명 FTP (무료) |

#### ⚠️ 한계점
- 2001년 창립 논문으로, 초기에는 수록 변이의 수가 현재에 비해 매우 적었다
- 제출 기반 데이터베이스로 제출 품질이 일정하지 않아 중복 또는 오류 항목이 존재할 수 있다
- 초기에는 SNP 위주였으나 다른 변이 유형으로의 확장이 이루어졌다

## 관련 정보
- **논문**: [dbSNP: the NCBI database of genetic variation](https://doi.org/10.1093/nar/29.1.308)
