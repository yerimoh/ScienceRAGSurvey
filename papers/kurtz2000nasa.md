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

kurtz2000nasa | 2000 | Astronomy and Astrophysics Supplement Series | dataset | [astronomy, physics] | [paper](https://arxiv.org/abs/astro-ph/0002104)

**DB**: NASA Astrophysics Data System (ADS)
**DB size**: ~1.5M bibliographic/abstract records (2000년 논문 기준, 4개 서비스 합산)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NASA ADS (bibcode-based search system)

> Astronomy and Astrophysics Supplement Series | 2000 | dataset | astronomy, physics
#### 📌 한 줄 요약
1993년 출범한 NASA 천문학 문헌 정보 시스템(ADS). 2000년 당시 **약 150만 건**의 서지·초록 레코드를 보유하며, 천문학(~85%), 기기·계측, 물리학, 천문학 프리프린트 등 4개 서비스로 구성. bibcode 기반 식별 체계와 SIMBAD·NED 등 외부 데이터 아카이브 간 실시간 교차 탐색을 최초로 구현한 천문학 K1 핵심 인프라.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 종래 NASA STI(Scientific and Technical Information) 데이터베이스는 도서관 사서 중심 설계로 연구자 직접 활용에 부적합
- 학술지·프리프린트·관측 데이터 아카이브가 분산되어 통합 탐색 불가
- 1987년 Garching 회의에서 자연어 검색 기반 천문학 초록 서비스의 필요성이 처음 제기됨

**이 시스템이 필요한 이유**
- 1991년 워싱턴 D.C. 회의("On-Line Literature in Astronomy")에서 네트워크 기반 통합 정보 시스템 구상 확립
- 1993년 2월 WWW 기반 Abstract Service 공개, 이후 5주 내에 사용자 수 4배 증가 (월 400 → 1,600명)
- 1993년 여름 SIMBAD와 최초 대서양 간 실시간 데이터베이스 교차 쿼리 연결 구축

#### 🔨 시스템 구성
ADS는 4개 서비스(Astronomy·Instrumentation·Physics·Astronomy Preprints)로 구성. bibcode(Uniform Bibliographic Code, Schmitz et al. 1995) 기반 고유 식별자로 ADS ↔ SIMBAD ↔ 전자 저널 간 하이퍼링크 연결. 1994년 AAS가 ISI Science Citation Index 서브셋을 구입하여 인용 데이터 제공. ~173만 건 하이퍼링크 중 ~31%가 ADS 외부 데이터 소스(SIMBAD, NED, CDS-Vizier, HEASARC 등) 연결. 전자 저널 파트너: ApJL, ApJ, ApJS, A&A, A&AS, AJ, PASP, MNRAS, New Astronomy, Nature, Science (2000년 기준).

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | 저자·제목·초록 필드 검색, 자연어 주제 검색 (entropy matching) |
| SIMBAD/NED 연계 | 천체 이름 조합 쿼리 (논리 OR/AND) |
| 유사 논문 검색 | 「Find Similar Abstracts」: 기존 논문 초록을 쿼리로 사용 |
| 미러 사이트 | 전 세계 분산 서비스 |

#### 📤 제공 데이터 형식
- 서지 레코드: 제목, 저자, 저널, bibcode
- 초록 (1975년 이후 주요 저널 거의 완전 수록)
- Bitmaps (주요 천문학 저널 구호 스캔 이미지)
- 인용/참고문헌 데이터 (AAS-ISI 계약, 1982년 1월~1998년 9월 범위)
- 하이퍼링크 ~173만 건 (ADS 외부 데이터 소스 포함)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 서지·초록 레코드 | **~1.5M** (2000년 기준, 4개 서비스 합산) |
| 천문학 단독 초록 | **~500,000건** |
| 월간 쿼리 수 | **~580,000건** (1999년 3월 기준) |
| 월간 사용자 | **~20,000명+** (1999년 3월 기준) |
| 월간 초록 조회 | **~400,000건** |
| 논문 전문 조회 | **~110,000건** / 월 |
| 하이퍼링크 | **~1.73M건** |
| 연간 쿼리 | **~5M건** |
| 쿼리 성장률 | 17개월마다 2배 (1996~1999년) |
| ADS 임팩트 추정 | 연 333 FTE 연구 인력 절감 효과 |

#### ⚠️ 한계점
- **인용 데이터 불완전**: AAS-ISI 계약에 따라 ADS 내부 논문 간 인용만 포함; 천문학 외 문헌 인용 누락
- **키워드 검색 미지원 (당시)**: 구 STI 키워드 체계와 저널 키워드 체계 간 비호환으로 키워드 쿼리 제거됨 (변환 작업 진행 중)
- **역사 문헌 디지털화 미완**: 1975년 이전 문헌은 완전 수록되지 않음 (AJ는 1849년부터 완전 수록된 최초 사례, 1999년 1월)
- **Instrumentation/Physics 서비스**: 천문학 서비스 대비 기능 미성숙
- **미래 과제(논문 언급)**: 구 관측소 보고서·폐간 저널 스캔 확장(Harvard Preservation Project 협력), 키워드 체계 통합, 비영어권 초록 확대

## 관련 정보
- **논문**: [https://arxiv.org/abs/astro-ph/0002104](https://arxiv.org/abs/astro-ph/0002104)
