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

inspirehep | 2012 | INSPIRE Collaboration (system reference) | dataset | [physics] | [paper](https://inspirehep.net)

**DB**: INSPIRE-HEP high-energy physics literature database
**DB size**: ~1,858,514 records (2025년 5월 기준, INSPIRE API `/api/literature` 조회)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: INSPIRE REST API

> INSPIRE Collaboration (system reference) | 2012 | dataset | physics
#### 📌 한 줄 요약
고에너지 물리학(HEP) 문헌 **약 185만 건 이상**을 보유하는 물리학 커뮤니티 전용 문헌 정보 시스템. 1974년 SPIRES에서 출발하여 CERN·DESY·Fermilab·IHEP·IN2P3가 공동 운영하며, 저자 중의성 해소와 arXiv 전문 검색을 통합 제공한다. **정식 학술 논문이 아닌 기관 시스템 참고 항목(`@misc`)임에 유의.**

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 1974년 SLAC/DESY에서 SPIRES(Stanford Physics Information REtrieval System) 시작 — 수십 년간 HEP 커뮤니티 표준 서지 시스템이었으나 현대적 기능 부재
- 저자 중의성 해소, 전문(fulltext) 검색, 개인화 저자 페이지 등 기능이 구형 시스템에서 지원되지 않음

**이 시스템이 필요한 이유**
- INSPIRE는 "SPIRES의 신뢰받는 큐레이션 콘텐츠"와 "CERN에서 개발된 Invenio 디지털 도서관 기술"을 결합하여 구축
- 운영 기관: CERN(스위스), DESY(독일), Fermilab(미국), IHEP(중국), IN2P3(프랑스)
- 협력 기관: arXiv.org, NASA-ADS, PDG(입자 데이터 그룹), HEPDATA, HEP 출판사

#### 🔨 시스템 구성
INSPIRE REST API를 통해 논문(Literature)·저자(Authors)·기관(Institutions)·실험(Experiments)·학술행사(Conferences)·채용 공고(Jobs) 6개 엔티티 유형 조회 제공. arXiv hep-* 카테고리 자동 수집 및 즉시 색인. LHC 실험(ATLAS, CMS, LHCb 등) 내부 기술 노트 색인 포함. 저자 중의성 해소: 고품질 저자 프로필 생성 및 자동 저자 식별. 최근 arXiv 논문의 본문·그림 캡션 전문 검색 및 스니펫 표시.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | inspirehep.net — 무료 브라우저 검색 |
| REST API | `/api/literature` 등 엔티티별 엔드포인트 — 무료, 속도 제한 있음 |

#### 📤 제공 데이터 형식
- 논문(Literature): arXiv 프리프린트, 저널 논문, 보고서 메타데이터
- 저자(Authors): 중의성 해소된 연구자 프로필, h-index
- 기관(Institutions): 소속 기관 레코드
- 실험(Experiments): 고에너지 물리학 실험 정보
- 학술행사(Conferences): HEP 분야 학술대회 목록
- 채용 공고(Jobs): HEP 분야 포지션 목록

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 논문 레코드 | **~1,858,514건** (2025년 5월 기준) |
| 접근 | 무료 (공개 API, 속도 제한 있음) |
| 갱신 | 실시간 (arXiv 자동 수집) |
| 전신 시스템 | SPIRES (1974년 SLAC/DESY 시작) |

#### ⚠️ 한계점
- **HEP 특화 범위**: 고에너지 물리학 중심으로 천체물리학·핵물리학 일부는 포함되나 물리학 전 분야 미커버
- **파트너 변동**: SLAC이 2021년 파트너 탈퇴 — 장기 운영 구조의 불안정성
- **출처 한계**: 공식 학술 논문이 아닌 `@misc` 시스템 참고 항목 — 시스템 설계·방법론에 대한 동료 심사 문헌 부재
- **과거 이력 한정**: SPIRES 시대 구형 레코드 중 일부는 메타데이터 품질이 불균일
- **미래 계획(공식 문서 언급)**: 제3자용 API 확장, 과거 콘텐츠 추가, 사용자 오류 수정 기능 확대

## 관련 정보
- **논문**: [https://inspirehep.net](https://inspirehep.net)
