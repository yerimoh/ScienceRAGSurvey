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

DBLP:journals/corr/abs-2205-01833 | 2022 | arXiv (CoRR) | dataset | [general] | [paper](https://arxiv.org/abs/2205.01833)

**DB**: OpenAlex scholarly knowledge graph
**DB size**: 209M works, 2,013M authors, 124K venues, 109K institutions, 65K concepts (2022년 논문 기준)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OpenAlex REST API / Full data dump

> arXiv (CoRR) | 2022 | dataset | general
#### 📌 한 줄 요약
Microsoft Academic Graph(MAG) 종료 이후의 공백을 메우기 위해 출시된 **완전 오픈** 학술 지식 그래프로, **2억 900만 개 저작물**, **20억 1,300만 명** 저자식별 데이터, **12만 4천 개** 저널·리포지토리, **10만 9천 개** 기관, **6만 5천 개** 개념을 웹 GUI·전체 데이터 덤프·REST API로 무료 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- Microsoft Academic Graph(MAG)가 서비스 종료되면서 대규모 공개 학술 그래프 인프라가 사라짐
- Scopus, Web of Science 등 상용 DB는 비용·접근 제한이 존재하여 오픈 대안의 필요성 증대

**이 시스템이 필요한 이유**
- MAG를 대체하는 **완전 무료·완전 공개(fully-open)** 학술 지식 그래프 제공
- Works·Authors·Venues·Institutions·Concepts 5개 엔티티 유형을 상호 연결된 그래프로 구조화

#### 🔨 시스템 구성
Crossref(서지 메타데이터), PubMed(생의학 문헌), ORCID(저자 식별자), ROR(연구기관 레지스트리), MAG 레거시 데이터, Unpaywall(오픈 액세스 정보), OpenCitations(인용 데이터) 등 다수 소스를 통합하여 5개 엔티티(Works·Authors·Venues·Institutions·Concepts)를 구성. Wikidata 기반 계층적 다중 태그 분류기로 개념 태깅 자동화. CC BY 4.0 라이선스 적용.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 기반 GUI | 브라우저에서 직접 탐색 |
| 전체 데이터 덤프 | 전체 스냅샷 일괄 다운로드 |
| REST API | 필터링·정렬·페이지네이션 지원 (JSON 응답) |

#### 📤 제공 데이터 형식
- **Works**: 저널 논문, 도서 등 학술 저작물 메타데이터 (제목, 저자, 인용 등)
- **Authors**: 중복 제거된 저자 식별자 및 프로필
- **Venues**: 저널 및 온라인 리포지토리 정보
- **Institutions**: ROR 연계 연구기관 레코드
- **Concepts**: Wikidata 기반 계층적 주제 분류 (다중 태그)
- 라이선스: CC BY 4.0 (상업적 활용 포함 자유 재사용)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| Works (학술 저작물) | **209M** (2022년 기준) |
| Authors (중복 제거) | **2,013M** (2022년 기준) |
| Venues (저널·리포지토리) | **124K** (2022년 기준) |
| Institutions (기관) | **109K** (2022년 기준) |
| Concepts (주제 분류) | **65K** (2022년 기준) |
| 라이선스 | CC BY 4.0 |

#### ⚠️ 한계점
- 논문에서 "현재 활발히 개발 중(under active development)"임을 명시
- 인용 정보의 정확도 및 커버리지 개선이 향후 과제로 기술
- 저자 및 기관 파싱·중복 제거(parsing and deduplication)의 정확도 개선 필요
- 분야별 커버리지 불균일 (이공계 위주로 강함)

## 관련 정보
- **논문**: [https://arxiv.org/abs/2205.01833](https://arxiv.org/abs/2205.01833)
