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
1993년 출범한 NASA 천문학 문헌 정보 시스템(ADS). 2000년 당시 **약 150만 건**의 서지·초록 레코드를 보유하며, 천문학(~85%), 기기·계측, 물리학, 천문학 프리프린트 등 4개 서비스로 구성. bibcode 기반 식별 체계와 SIMBAD·NED 등 외부 데이터 아카이브 간 실시간 교차 탐색을 최초로 구현한 천문학 K1 핵심 인프라.

## 연구 배경 및 동기
**천문학 문헌 접근의 특수성**
- 종래 NASA STI(Scientific and Technical Information) 데이터베이스는 도서관 사서 중심 설계로 연구자 직접 활용에 부적합
- 학술지·프리프린트·관측 데이터 아카이브가 분산되어 통합 탐색 불가
- 1987년 Garching 회의에서 자연어 검색 기반 천문학 초록 서비스의 필요성이 처음 제기됨

**시스템 구축 경과**
- 1991년 워싱턴 D.C. 회의("On-Line Literature in Astronomy")에서 네트워크 기반 통합 정보 시스템 구상 확립
- 1993년 2월 WWW 기반 Abstract Service 공개, 이후 5주 내에 사용자 수 4배 증가 (월 400 → 1,600명)
- 1993년 여름 SIMBAD와 최초 대서양 간 실시간 데이터베이스 교차 쿼리 연결 구축
- 1994년 미국천문학회(AAS)가 ISI Science Citation Index 서브셋을 구입하여 ADS에 인용 데이터 제공

## 시스템 개요

### ADS 4개 서비스 (2000년 기준)
| 서비스 | 특징 |
|---|---|
| Astronomy (천문학) | 전체 ADS 이용의 ~85% 차지, 가장 완성된 서비스 |
| Instrumentation (기기) | 초록 수는 Astronomy보다 많음; SPIE 공식 출판 웹사이트 기반으로 활용 |
| Physics (물리학) | 물리학 관련 서지 정보 제공 |
| Astronomy Preprints (프리프린트) | 미출판 프리프린트 색인 |

### Bibcode 체계
- 국제 표준 서지 코드(Uniform Bibliographic Code, Schmitz et al. 1995)에 따라 고유 식별자 부여
- 형식: `YYYY저널약어VVVVVMPPPPAa` (연도·저널·권·페이지·저자 이니셜 인코딩)
- 예시: `2000A&AS..143...41K` (이 논문 자체의 bibcode)
- bibcode를 기반으로 ADS ↔ SIMBAD ↔ 전자 저널 간 하이퍼링크 연결 가능

### 데이터 구성 (Astronomy 서비스 기준)
- **초록**: ~500,000건 천문학 논문 색인; 1975년 이후 주요 저널 거의 완전 수록
- **Bitmaps (페이지 이미지)**: 주요 천문학 저널 구호(back issue) 스캔 이미지; 전자 저널 이전 시기 포함
- **인용/참고문헌**: AAS가 ISI로부터 구입한 인용 데이터(1982년 1월~1998년 9월 범위)
- **하이퍼링크**: ~173만 건 (그 중 ~31%가 ADS 외부 데이터 소스 연결)

### 외부 연계 아카이브 (2000년 기준)
- **SIMBAD** (Strasbourg Data Center, CDS): 천체 이름 → 논문 교차 탐색
- **NED** (NASA/IPAC Extragalactic Database): 외부 은하 데이터베이스
- **CDS-Vizier**: 저널 데이터 테이블
- **HEASARC**: 고에너지 천체물리학 아카이브
- **전자 저널**: ApJL, ApJ, ApJS, A&A, A&AS, AJ, PASP, MNRAS, New Astronomy, Nature, Science (당시 전자 저널 파트너)

### 검색 인터페이스
- 저자·제목·초록 필드 검색
- 자연어 주제 검색 (entropy matching 기반)
- SIMBAD/NED 천체 이름 조합 쿼리 (논리 OR/AND 연산)
- 「Find Similar Abstracts」: 기존 논문 초록을 쿼리로 사용하는 유사 논문 검색
- 참고문헌/피인용 논문 역추적 검색
- 미러 사이트를 통한 전 세계 분산 서비스

## 데이터 규모 (2000년 논문 보고 기준)
- **총 초록·서지 레코드**: 약 150만 건 (4개 서비스 합산; 천문학 단독 ~500,000건)
- **월간 쿼리 수**: 약 580,000건 (1999년 3월 기준)
- **월간 사용자**: 약 20,000명 이상 (1999년 3월 기준)
- **월간 초록 조회**: 약 400,000건; 논문 전문 조회: 약 110,000건
- **하이퍼링크**: 약 173만 건
- **쿼리 성장률**: 17개월마다 2배 증가 (1996~1999년 기준)
- **연간 쿼리**: 약 500만 건
- **ADS 임팩트 추정**: 연 333 FTE 연구 인력 절감 효과 (하버드-스미소니언 천체물리학 센터 전체 규모에 해당)

## 한계점
- **인용 데이터 불완전**: AAS-ISI 계약에 따라 ADS 내부 논문 간 인용만 포함; 천문학 외 문헌 인용 누락
- **키워드 검색 미지원 (당시)**: 구 STI 키워드 체계와 저널 키워드 체계 간 비호환으로 키워드 쿼리 제거됨 (변환 작업 진행 중)
- **역사 문헌 디지털화 미완**: 1975년 이전 문헌은 완전 수록되지 않음; AJ는 1849년부터 완전 수록된 최초 사례(1999년 1월)
- **Instrumentation/Physics 서비스**: 천문학 서비스 대비 기능 미성숙
- **미래 과제(논문 언급)**: 구 관측소 보고서·폐간 저널 스캔 확장(Harvard Preservation Project 협력), 키워드 체계 통합, 비영어권 초록 확대

## 관련 정보
- **논문**: Kurtz et al. 2000, A&AS 143, 41–59. [https://arxiv.org/abs/astro-ph/0002104](https://arxiv.org/abs/astro-ph/0002104)
- **동반 논문**: SEARCH (Eichhorn et al.), ARCHITECTURE (Accomazzi et al.), DATA (Grant et al.) — 모두 동일 호(A&AS) 수록
- **ADS URL (2000년 기준)**: http://adswww.harvard.edu/
- **현재 URL**: [https://ui.adsabs.harvard.edu](https://ui.adsabs.harvard.edu)
- **Urania**: ADS+CDS/SIMBAD+전자 저널을 묶는 천문학 통합 디지털 정보 환경 개념명 (당시 천문학에만 존재한 학제적 전자 정보 생태계)
