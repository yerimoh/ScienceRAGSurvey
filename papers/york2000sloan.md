---
title: "The Sloan Digital Sky Survey: Technical Summary"
bib_key: "york2000sloan"
year: 2000
domain: astronomy
type: dataset
venue: The Astronomical Journal
paper_link: https://arxiv.org/abs/astro-ph/0006396
---
# The Sloan Digital Sky Survey: Technical Summary

york2000sloan | 2000 | The Astronomical Journal | dataset | [astronomy] | [paper](https://arxiv.org/abs/astro-ph/0006396)

**DB**: Sloan Digital Sky Survey (SDSS) — imaging and spectroscopic sky survey
**DB size**: Survey goal: pi steradians (northern sky), ~1 million galaxy spectra, ~100,000 quasar spectra (York 2000 design spec; actual DR17 cumulative: hundreds of millions of objects)
**DB Open/Private**: Open
**Modality**: ['Image', 'Spectrum', 'Catalog']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: SDSS (2.5m telescope, Apache Point Observatory)

> The Astronomical Journal | 2000 | dataset | astronomy
#### 한 줄 요약
2000년 기준 설계 사양을 기술한 SDSS 기술 요약 논문. 5개 광학 필터(ugriz)로 북반구 약 pi 스테라디안을 촬영하고, 약 100만 개 은하와 10만 개 퀘이사의 분광 관측을 목표로 함. 수십 년에 걸친 SDSS 데이터 릴리스(DR1–DR17)를 통해 수억 개의 천체가 카탈로그화되었으며, 현대 천문학 K3 관측 데이터의 핵심 자원이다.

#### 개발/구축 배경
**기존 인프라의 한계**
- 기존 하늘 탐사는 필름 기반 사진 건판에 의존하여 균일한 측광 보정과 대규모 분광 관측이 불가
- 은하 적색편이 분포, 대규모 구조, 퀘이사 분포에 대한 체계적 데이터 부재

**이 시스템이 필요한 이유**
- 측광과 분광 데이터를 동일 망원경으로 통합하여 광도와 거리를 동시 측정
- 5-band CCD 이미저(2048×2048 배열)와 다중 광섬유 분광기(640개 동시)로 대규모 자동화 관측
- 보정된 디지털 카탈로그를 공개하여 은하 진화, 퀘이사 연구, 은하수 구조 연구에 활용

#### 시스템 구성
2.5m 전용 망원경(Apache Point Observatory, 뉴멕시코). 5개 필터(u, g, r, i, z): g' ~23등급 심도. 두 광섬유 분광기(각 320개 광섬유): 3800–9200Å, R~2000. 데이터 파이프라인: 실시간 천체 추출, 측광 보정, 분광 추출 자동화. Photo 파이프라인(이미지 처리·별–은하 분리)과 Spectro 파이프라인(적색편이 자동 측정) 포함.

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| SkyServer | skyserver.sdss.org — 웹 SQL 쿼리 인터페이스 |
| CasJobs | 대용량 배치 쿼리 |
| SciServer | 클라우드 분석 환경 |
| FITS 파일 | das.sdss.org — 원본 이미지·스펙트럼 직접 다운로드 |

#### 제공 데이터 형식
- 5-band 측광 카탈로그: 위치·등급·형태 파라미터
- 분광 카탈로그: 적색편이, 분류(별/은하/퀘이사), 스펙트럼
- 이미지 타일 (FITS 형식)
- CasJobs SQL 쿼리 가능 스키마

#### 주요 통계
| 항목 | 수치 |
|---|---|
| 측광 목표 면적 | ~10,000 deg² (pi sr) |
| 분광 목표 은하 | ~1,000,000 개 |
| 분광 목표 퀘이사 | ~100,000 개 |
| DR17 누적 분광 | ~4.9M 스펙트럼 |
| 측광 심도 | g' ~ 23 등급 |
| 파장 범위 (분광) | 3800–9200 Å |

#### 한계점
- 2000년 논문은 완성 이전 설계 사양이므로 실제 달성값은 후속 DR 논문 참조 필요
- 북반구 고위도 영역 중심이므로 은하면 및 남반구 미커버
- 5개 광학 밴드만 제공 (적외선·UV 제외); 후속 WISE·GALEX 데이터와 결합 필요

## 관련 정보
- **논문**: [https://arxiv.org/abs/astro-ph/0006396](https://arxiv.org/abs/astro-ph/0006396)
- **데이터 포털**: [https://www.sdss.org](https://www.sdss.org)
