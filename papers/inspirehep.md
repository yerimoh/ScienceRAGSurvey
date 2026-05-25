---
title: "INSPIRE-HEP: The information system for high-energy physics"
bib_key: "inspirehep"
year: 2012
domain: physics
type: dataset
venue: INSPIRE Collaboration
paper_link: https://inspirehep.net
---
# INSPIRE-HEP: The information system for high-energy physics

> INSPIRE Collaboration | 2012 | dataset | physics

## 한 줄 요약
고에너지 물리학(HEP) 문헌 **150만 개 이상**을 집약하는 물리학 커뮤니티 전용 문헌 정보 시스템. SPIRES(1974~)의 후계자로 CERN·DESY·Fermilab·IHEP·IN2P3가 공동 운영하며, 저자 중의성 해소와 정밀 인용 네트워크 분석을 제공.

## 연구 배경 및 동기
**고에너지 물리학 문헌의 특수성**
- HEP 연구는 수천 명의 저자가 참여하는 대형 실험 결과물이 다수
- 동명이인·다국적 저자 식별 문제 심각 — 정밀 저자 중의성 해소 필수
- 1974년 SPIRES 이후 50년간 물리학 커뮤니티의 표준 문헌 시스템

**이 시스템이 중요한 이유**
- 고에너지 물리학 분야 **사실상 유일한** 커뮤니티 관리 문헌 DB
- arXiv 프리프린트와 저널 논문을 통합하여 최신 연구 즉시 반영

## 핵심 기능
| 기능 | 설명 |
|---|---|
| 저자 중의성 해소 | HEPNames — 연구자 프로필·소속 이력 추적 |
| 인용 네트워크 | h-index, i10-index 등 HEP 특화 지표 |
| arXiv 통합 | 프리프린트 즉시 색인 |
| 실험 DB 연계 | ATLAS, CMS, LHCb 등 실험 정보 연결 |
| INSPIRE REST API | 논문·저자·기관·실험 엔티티 조회 |

## 데이터 규모
- **총 레코드**: 1.5M+ (HEP 논문·프리프린트·보고서)
- **저자 프로필**: 150K+ (HEPNames)
- **인용 링크**: 수천만 건
- **API**: `inspirehep.net/api/` — 무료, 속도 제한 있음
- **갱신**: 실시간 (arXiv hep-* 자동 수집)

## 활용 방법
```
[문헌 검색]
  → REST API: https://inspirehep.net/api/literature?q=Higgs+boson
  → 제목, 저자, 인용 수, arXiv ID, DOI 반환

[저자 조회]
  → /api/authors?q=name:Weinberg+Steven
  → HEPNames 프로필, 소속 이력, 논문 목록

[인용 분석]
  → /api/literature/{recid}/citations
  → 피인용 논문 전체 목록

[실험 필터]
  → collaboration:CMS 등 실험별 논문 필터링
```

## 관련 정보
- **공식 사이트**: [https://inspirehep.net](https://inspirehep.net)
- **API 문서**: [https://github.com/inspirehep/rest-api-doc](https://github.com/inspirehep/rest-api-doc)
- **HEPNames**: [https://inspirehep.net/authors](https://inspirehep.net/authors)
