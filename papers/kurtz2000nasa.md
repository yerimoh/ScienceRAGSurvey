---
title: "The NASA Astrophysics Data System: Overview"
bib_key: "kurtz2000nasa"
year: 2000
domain: astronomy, physics
type: dataset
venue: Astronomy and Astrophysics Supplement Series
paper_link: https://arxiv.org/abs/astro-ph/0002104
---
# The NASA Astrophysics Data System: Overview

> Astronomy and Astrophysics Supplement Series | 2000 | dataset | astronomy · physics

## 한 줄 요약
천문학, 행성과학, 물리학 문헌 **1,600만 개 이상**의 레코드를 보유하는 NASA 학술 문헌 시스템. 독자적인 bibcode 식별 체계와 SIMBAD·관측 데이터 아카이브 직접 링크를 제공하는 천문학 K1 핵심 인프라.

## 연구 배경 및 동기
**천문학 문헌 접근의 특수성**
- 천문학은 관측 데이터와 논문이 긴밀히 연결 — 논문만으로는 불충분
- 전통적 도서관 시스템은 망원경 데이터·측광 카탈로그와 연계 불가
- 1993년 NASA 지원으로 출범, 무료 디지털 천문학 문헌 아카이브 구축

**이 시스템이 중요한 이유**
- 천문학 커뮤니티 **사실상 표준** 문헌 검색 시스템
- 논문 ↔ 관측 데이터 ↔ 천체 카탈로그 간 직접 탐색 가능

## 핵심 기능
| 기능 | 설명 |
|---|---|
| Bibcode | 고유 식별자 (예: 2000A&AS..143...41K) |
| SIMBAD 연결 | 논문에서 언급된 천체 직접 링크 |
| 데이터 아카이브 링크 | HST, Chandra, VLA 등 관측 데이터 연결 |
| ADS Search API | 풀텍스트·메타데이터 무료 검색 |
| 인용 네트워크 | 천문학 커뮤니티 특화 인용 분석 |

## 데이터 규모
- **총 레코드**: 16M+ (천문학·행성과학·지구물리학·물리학)
- **전문 접근**: 수백만 건 디지털화 과거 논문 포함
- **API**: `api.adsabs.harvard.edu` — 무료 (API 키 필요)
- **갱신**: 실시간 (주요 저널 즉시 반영)

## 활용 방법
```
[문헌 검색]
  → ADS Search API: /v1/search/query?q=black+hole+merger&fl=bibcode,title
  → bibcode, 제목, 저자, 초록, 인용 수 반환

[Bibcode 조회]
  → 특정 논문의 bibcode로 전문·참고문헌·인용 논문 일괄 조회

[천체 연계 탐색]
  → 논문 → SIMBAD 객체 링크 → 관측 데이터 아카이브

[RAG 활용]
  → 천문학 도메인 RAG 시스템의 K1 코퍼스 (예: AstroLLaMA, UniAstro)
```

## 관련 정보
- **논문**: [https://arxiv.org/abs/astro-ph/0002104](https://arxiv.org/abs/astro-ph/0002104)
- **공식 사이트**: [https://ui.adsabs.harvard.edu](https://ui.adsabs.harvard.edu)
- **API 문서**: [https://api.adsabs.harvard.edu/v1/](https://api.adsabs.harvard.edu/v1/)
