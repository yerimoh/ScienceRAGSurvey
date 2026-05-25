---
title: "INSPIRE-HEP: The information system for high-energy physics"
bib_key: "inspirehep"
year: 2012
domain: physics
type: dataset
venue: INSPIRE Collaboration (system reference)
paper_link: https://inspirehep.net
---
# INSPIRE-HEP: The information system for high-energy physics

> INSPIRE Collaboration | 2012 | dataset | physics

## 한 줄 요약
고에너지 물리학(HEP) 문헌 **약 185만 건 이상**을 보유하는 물리학 커뮤니티 전용 문헌 정보 시스템. 1974년 SPIRES에서 출발하여 CERN·DESY·Fermilab·IHEP·IN2P3가 공동 운영하며, 저자 중의성 해소와 arXiv 전문 검색을 통합 제공한다. 정식 학술 논문이 아닌 기관 시스템 참고 항목(misc)임에 유의.

## 시스템 개요
**성격**: INSPIRE-HEP는 단일 논문이 아닌 운영 중인 정보 시스템에 대한 참고 항목. bib 항목은 `@misc` 유형이며 2012년을 기준 연도로 사용.

**운영 기관**
- 공동 운영: CERN(스위스), DESY(독일), Fermilab(미국), IHEP(중국), IN2P3(프랑스)
- 협력 기관: arXiv.org, NASA-ADS, PDG(입자 데이터 그룹), HEPDATA, HEP 출판사
- 참고: SLAC은 2021년 운영 파트너에서 탈퇴

**역사적 배경**
- 1974년 SLAC/DESY에서 SPIRES(Stanford Physics Information REtrieval System) 시작 — 수십 년간 HEP 커뮤니티 표준 서지 시스템
- INSPIRE는 "SPIRES의 신뢰받는 큐레이션 콘텐츠"와 "CERN에서 개발된 Invenio 디지털 도서관 기술"을 결합하여 구축
- 새 시스템으로 전환하며 저자 중의성 해소, 전문(fulltext) 검색, 개인화 저자 페이지 등 기능 대폭 확장

## 핵심 기능
| 기능 | 설명 |
|---|---|
| 저자 중의성 해소 | 고품질 저자 프로필 생성 및 검색 정확도 향상을 위한 자동 저자 식별 |
| 전문(Fulltext) 검색 | 최근 arXiv 논문의 본문·그림 캡션 전문 검색 및 스니펫 표시 |
| LHC 실험 노트 | LHC 실험(ATLAS, CMS, LHCb 등) 내부 기술 노트 색인 |
| arXiv 통합 | arXiv hep-* 카테고리 자동 수집 및 즉시 색인 |
| 개인화 저자 페이지 | 논문 클레임, h-index 등 개인 연구자 프로필 |
| INSPIRE REST API | 논문·저자·기관·실험·학술행사·채용 공고 엔티티 조회 |

**콘텐츠 유형**
- 논문(Literature): arXiv 프리프린트, 저널 논문, 보고서
- 저자(Authors): 중의성 해소된 연구자 프로필
- 기관(Institutions): 소속 기관 레코드
- 실험(Experiments): 고에너지 물리학 실험 정보
- 학술행사(Conferences): HEP 분야 학술대회 목록
- 채용 공고(Jobs): HEP 분야 포지션 목록

## 데이터 규모
- **논문 레코드**: 약 1,858,514건 (2025년 5월 기준, INSPIRE API `/api/literature` 조회)
- **접근**: 무료 (공개 API, 속도 제한 있음)
- **갱신**: 실시간 (arXiv 자동 수집)
- **언어**: 주로 영어; HEP 분야 국제 논문 포함

## 한계점
- **HEP 특화 범위**: 고에너지 물리학 중심으로 천체물리학, 핵물리학 일부는 포함되나 물리학 전 분야 커버하지 않음
- **파트너 변동**: SLAC이 2021년 파트너 탈퇴 — 장기 운영 구조의 불안정성
- **출처 한계**: 공식 학술 논문이 아닌 `@misc` 시스템 참고 항목 — 시스템 설계·방법론에 대한 동료 심사 문헌 부재
- **과거 이력 한정**: SPIRES 시대 구형 레코드 중 일부는 메타데이터 품질이 불균일
- **미래 계획(공식 문서 언급)**: 제3자용 API 확장, 과거 콘텐츠 추가, 사용자 오류 수정 기능 확대

## 관련 정보
- **공식 사이트**: [https://inspirehep.net](https://inspirehep.net)
- **도움말**: [https://help.inspirehep.net/knowledge-base/inspire-project-overview/](https://help.inspirehep.net/knowledge-base/inspire-project-overview/)
- **REST API 문서**: [https://github.com/inspirehep/rest-api-doc](https://github.com/inspirehep/rest-api-doc)
- **전신 시스템**: SPIRES (1974년 SLAC/DESY 시작)
