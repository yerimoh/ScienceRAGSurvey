---
title: "Crossref: The sustainable source of community-owned scholarly metadata"
bib_key: "DBLP:journals/qss/HendricksTLF20"
year: 2020
domain: general
type: dataset
venue: Quantitative Science Studies
paper_link: https://doi.org/10.1162/qss_a_00022
---
# Crossref: The sustainable source of community-owned scholarly metadata

> Quantitative Science Studies | 2020 | dataset | general

## 한 줄 요약
**1억 3천만 개 이상**의 DOI 기반 학술 메타데이터를 무료 REST API로 제공하는 커뮤니티 공유 인프라. reference linkage, funder 정보, ORCID 연계를 포함하는 K1 기반 핵심 식별 시스템.

## 연구 배경 및 동기
**기존 메타데이터 인프라의 한계**
- 학술 출판사별로 메타데이터 형식·접근 방식이 파편화
- 인용 연결(reference linkage)과 연구비 정보(funder data)의 공개 집계 부재
- 지속 가능한 오픈 인프라 필요성 대두

**이 연구가 필요한 이유**
- 학술 생태계 전반에 걸친 **DOI 등록 및 메타데이터 공유** 표준화
- 출판사·기관·연구자 모두가 기여하고 활용하는 공동체 소유 모델 구현

## 핵심 기능
| 기능 | 설명 |
|---|---|
| DOI 등록 및 조회 | 130M+ DOI 레코드, 무료 REST API |
| Reference Linkage | 인용 관계 연결 (CrossRef Cited-by) |
| Funder Data | 연구비 지원 기관 메타데이터 |
| ORCID 연계 | 저자 식별자 통합 |
| 오픈 액세스 상태 | Unpaywall 연계, OA 여부 표시 |

## 데이터 규모
- **총 레코드**: 130M+ (DOI 기반)
- **참여 출판사**: 수천 개 학술 출판사·기관
- **API**: `api.crossref.org` — 무료, 회원가입 불필요
- **갱신**: 실시간 (출판사가 직접 등록)

## 활용 방법
```
[DOI / 메타데이터 조회]
  → Crossref REST API (https://api.crossref.org/works/{DOI})
  → 제목, 저자, 출판일, 저널, 인용 수, reference list 반환

[Reference Linkage]
  → 인용 관계 그래프 구축 (논문 → 피인용 논문 연결)

[Funder 데이터]
  → Grant ID, Funder name 연계
```

## 관련 정보
- **논문**: [https://doi.org/10.1162/qss_a_00022](https://doi.org/10.1162/qss_a_00022)
- **API**: [https://api.crossref.org](https://api.crossref.org)
- **GitHub**: [https://github.com/CrossRef](https://github.com/CrossRef)
