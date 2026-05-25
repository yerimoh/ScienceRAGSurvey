---
title: "OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts"
bib_key: "DBLP:journals/corr/abs-2205-01833"
year: 2022
domain: general
type: dataset
venue: arXiv (CoRR)
paper_link: https://arxiv.org/abs/2205.01833
---
# OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts

> arXiv (CoRR) | 2022 | dataset | general

## 한 줄 요약
**2억 개 이상**의 학술 저작물을 완전 무료·무제한으로 제공하는 개방형 학술 지식 그래프. Crossref, PubMed, arXiv, 기관 리포지토리를 통합하여 works·authors·venues·institutions·concepts 5개 엔티티를 구조화.

## 연구 배경 및 동기
**기존 학술 인덱스의 한계**
- Microsoft Academic Graph(MAG) 서비스 종료(2021)로 대규모 공개 학술 그래프 공백 발생
- Scopus, Web of Science 등 상용 DB는 비용과 접근 제한 존재
- 완전 오픈 학술 인프라 필요성 증대

**이 연구가 필요한 이유**
- MAG의 후계 시스템으로 **완전 무료·무제한** 학술 데이터 제공
- 5개 핵심 엔티티(작품·저자·기관·저널·개념)를 관계 그래프로 통합

## 핵심 기능
| 엔티티 | 규모 |
|---|---|
| Works (논문·프리프린트) | 200M+ |
| Authors | 400M+ |
| Venues (저널·컨퍼런스) | 200K+ |
| Institutions | 100K+ |
| Concepts (AI 기반 주제 분류) | 65K+ |

## 데이터 규모
- **총 저작물**: 200M+ (전 학문 분야)
- **API**: `api.openalex.org` — 무료, 속도 제한 없음, 등록 불필요
- **데이터 소스**: Crossref, PubMed, arXiv, ORCID, ROR, 기관 리포지토리 통합
- **갱신**: 주기적 배치 업데이트

## 활용 방법
```
[학술 저작물 검색]
  → OpenAlex REST API: https://api.openalex.org/works?filter=...
  → 제목, 저자, 기관, 인용 관계, OA 상태 반환

[인용 네트워크 분석]
  → referenced_works / citing_works 필드로 그래프 탐색

[개념 기반 탐색]
  → AI 분류된 concepts(65K+)로 주제별 논문 집계

[데이터 덤프]
  → 전체 스냅샷 S3 다운로드 가능
```

## 관련 정보
- **논문**: [https://arxiv.org/abs/2205.01833](https://arxiv.org/abs/2205.01833)
- **API**: [https://api.openalex.org](https://api.openalex.org)
- **공식 사이트**: [https://openalex.org](https://openalex.org)
