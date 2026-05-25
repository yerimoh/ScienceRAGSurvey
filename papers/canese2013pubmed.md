---
title: "PubMed: the bibliographic database"
bib_key: "canese2013pubmed"
year: 2013
domain: medical, bio
type: dataset
venue: NCBI Handbook
paper_link: https://www.ncbi.nlm.nih.gov/books/NBK153387/
---
# PubMed: the bibliographic database

> NCBI Handbook | 2013 | dataset | medical · bio

## 한 줄 요약
NCBI가 운영하는 **2,200만 개 이상**의 생의학 인용 레코드 데이터베이스. MeSH(Medical Subject Headings) 통제 어휘와 NCBI E-utilities API를 통해 무료로 접근할 수 있는 생의학 K1 핵심 인프라.

## 연구 배경 및 동기
**생의학 문헌 접근의 필요성**
- MEDLINE 수록 저널 중심의 체계적 의학 문헌 색인 필요
- 임상·연구 커뮤니티의 신속한 문헌 탐색 지원
- 생의학 NLP·RAG 시스템의 핵심 코퍼스 역할

**이 데이터베이스가 중요한 이유**
- 1996년 인터넷 공개 이후 생의학 문헌의 **글로벌 표준 검색 인프라**
- MeSH 어휘를 통한 정밀 주제 검색 가능

## 핵심 기능
| 기능 | 설명 |
|---|---|
| MeSH 어휘 | 29,000개 이상 통제 주제어로 정밀 색인 |
| NCBI E-utilities | esearch, efetch, elink API 무료 제공 |
| MEDLINE 수록 | 약 5,200개 학술지 색인 |
| 링크아웃 | PMC 전문, 저자 기관 링크 연결 |
| 임상 쿼리 필터 | RCT, 메타분석 등 근거 등급별 필터 |

## 데이터 규모
- **총 인용 레코드**: 22M+ (매년 약 80만 건 추가)
- **전문 연계(PMC)**: 7M+ 오픈액세스 전문
- **API**: NCBI E-utilities — 무료, 등록 시 속도 향상
- **갱신**: 일 단위 업데이트

## 활용 방법
```
[문헌 검색 (esearch)]
  → https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi
    ?db=pubmed&term=COVID+treatment&retmax=100

[레코드 조회 (efetch)]
  → PMID 리스트 → 초록·메타데이터 반환

[MeSH 기반 정밀 탐색]
  → MeSH term[MH] 필터로 주제 계층 탐색

[RAG 코퍼스 활용]
  → MedRAG, MedCorp, BioASQ 등 생의학 RAG 벤치마크의 기본 코퍼스
```

## 관련 정보
- **참조**: [https://www.ncbi.nlm.nih.gov/books/NBK153387/](https://www.ncbi.nlm.nih.gov/books/NBK153387/)
- **공식 사이트**: [https://pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov)
- **E-utilities**: [https://www.ncbi.nlm.nih.gov/books/NBK25499/](https://www.ncbi.nlm.nih.gov/books/NBK25499/)
