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
Microsoft Academic Graph(MAG) 종료 이후의 공백을 메우기 위해 출시된 **완전 오픈** 학술 지식 그래프로, **2억 900만 개 저작물**, **20억 1,300만 명** 저자식별 데이터, **12만 4천 개** 저널·리포지토리, **10만 9천 개** 기관, **6만 5천 개** 개념을 웹 GUI·전체 데이터 덤프·REST API로 무료 제공한다.

## 연구 배경 및 동기
**MAG 종료로 인한 공백**
- Microsoft Academic Graph(MAG)가 서비스 종료되면서 대규모 공개 학술 그래프 인프라가 사라짐
- Scopus, Web of Science 등 상용 DB는 비용·접근 제한이 존재하여 오픈 대안의 필요성 증대

**OpenAlex가 해결하는 문제**
- MAG를 대체하는 **완전 무료·완전 공개(fully-open)** 학술 지식 그래프 제공
- Works·Authors·Venues·Institutions·Concepts 5개 엔티티 유형을 상호 연결된 그래프로 구조화

## 핵심 기능
| 엔티티 유형 | 규모 (논문 발표 기준, 2022년) |
|---|---|
| Works (저널 논문·도서 등 학술 저작물) | 2억 900만 개 (209M) |
| Authors (중복 제거된 저자) | 20억 1,300만 명 (2,013M) |
| Venues (저널 및 온라인 리포지토리) | 12만 4,000개 (124K) |
| Institutions (연구 기관) | 10만 9,000개 (109K) |
| Concepts (Wikidata 기반 계층적 주제 분류) | 6만 5,000개 (65K) |

**데이터 접근 방법 (3가지)**
1. **웹 기반 GUI** — 브라우저에서 직접 탐색
2. **전체 데이터 덤프(full data dump)** — 전체 스냅샷 일괄 다운로드
3. **고용량 REST API** — 필터링·정렬·페이지네이션 지원

**API 기능**
- 여러 엔티티 유형에 걸친 필터링(filtering)
- 인덱싱된 필드에 대한 정렬(sorting)
- 커서 기반 및 오프셋 페이지네이션
- JSON 응답 형식

## 데이터 규모 (2022년 논문 기준)
- **총 저작물**: 2억 900만 개 (저널 논문·도서 등 포함)
- **저자**: 20억 1,300만 명 (중복 제거 처리)
- **저널·리포지토리**: 12만 4,000개
- **기관**: 10만 9,000개
- **개념**: 6만 5,000개 (Wikidata 연계, 자동 계층적 다중 태그 분류기 사용)
- **라이선스**: CC BY 4.0 (상업적 활용 포함 자유 재사용 가능)

## 데이터 출처 (논문에 명시된 소스)
- Crossref (서지 메타데이터)
- PubMed (생의학 문헌)
- ORCID (저자 식별자)
- ROR (연구기관 레지스트리, Research Organization Registry)
- Microsoft Academic Graph (MAG) 레거시 데이터
- Unpaywall (오픈 액세스 정보)
- OpenCitations (인용 데이터)

## 한계점
- 논문에서 "현재 활발히 개발 중(under active development)"임을 명시
- 인용 정보의 정확도 및 커버리지 개선이 향후 과제로 기술
- 저자 및 기관 파싱·중복 제거(parsing and deduplication)의 정확도 개선 필요
- 분야별 커버리지 불균일 (이공계 위주로 강함)

## 관련 정보
- **논문**: [https://arxiv.org/abs/2205.01833](https://arxiv.org/abs/2205.01833)
