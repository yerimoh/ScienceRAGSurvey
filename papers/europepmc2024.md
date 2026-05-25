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

> Nucleic Acids Research | 2024 | dataset | medical · bio

## 한 줄 요약
**900만 개 이상**의 생의학 기사와 **65만 개 이상**의 프리프린트 오픈 전문을 제공하는 유럽 생의학 문헌 플랫폼. 31개 프리프린트 서버를 통합하고 RESTful API와 annotation API를 무료로 제공.

## 연구 배경 및 동기
**오픈 액세스 생의학 문헌의 필요성**
- PubMed는 초록 중심; 전문(full text) 오픈 액세스 접근 제한
- 프리프린트(bioRxiv, medRxiv 등)와 피어리뷰 논문의 통합 필요
- 유럽 연구 펀딩 기관(Wellcome, BBSRC 등)의 OA 의무화 지원

**이 플랫폼이 중요한 이유**
- **오픈 전문**을 RAG 파이프라인에 직접 활용 가능
- 프리프린트 31개 서버 통합으로 최신 연구 실시간 반영

## 핵심 기능
| 기능 | 설명 |
|---|---|
| 오픈 전문 | 9M+ 기사 전문 XML/PDF 제공 |
| 프리프린트 통합 | 31개 서버(bioRxiv, medRxiv, ChemRxiv 등) 650K+ |
| Annotation API | 유전자, 질환, 화합물 등 개체 주석 |
| RESTful API | 검색·조회·다운로드 무료 |
| 데이터 링크 | UniProt, PDB, ChEMBL 등 바이오 DB 연결 |

## 데이터 규모
- **피어리뷰 기사**: 9M+ (전문 오픈 액세스)
- **프리프린트**: 650K+ (31개 서버)
- **주석 데이터**: 수억 건 (유전자·질환·화합물·변이 등)
- **API**: `https://www.ebi.ac.uk/europepmc/webservices/rest/` — 무료

## 활용 방법
```
[전문 검색]
  → REST API: /search?query=COVID+vaccine&format=json
  → 초록·전문 XML 반환

[전문 다운로드]
  → /article/{SOURCE}/{ID}/fullTextXML

[Annotation API]
  → 문서 내 생체의학 개체(유전자·질환·화합물) 태깅 조회

[RAG 파이프라인]
  → 오픈 전문 XML → 섹션 분리 → 청킹 → 벡터 인덱싱
```

## 관련 정보
- **논문**: [https://doi.org/10.1093/nar/gkad1085](https://doi.org/10.1093/nar/gkad1085)
- **공식 사이트**: [https://europepmc.org](https://europepmc.org)
- **REST API 문서**: [https://europepmc.org/RestfulWebService](https://europepmc.org/RestfulWebService)
