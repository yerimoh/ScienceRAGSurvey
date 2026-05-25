---
title: "Mikulski Archive for Space Telescopes (MAST)"
bib_key: "mast"
year: 1997
domain: astronomy
type: dataset
venue: Space Telescope Science Institute (system reference)
paper_link: https://archive.stsci.edu
---
# Mikulski Archive for Space Telescopes (MAST)

mast | 1997 | Space Telescope Science Institute (system reference) | dataset | [astronomy] | [portal](https://archive.stsci.edu)

**DB**: MAST — unified NASA archive for UV/optical/NIR space telescope data
**DB size**: Petabyte-scale; hosts Hubble (~200 TB+), JWST (growing rapidly), Kepler/K2, TESS, Pan-STARRS (~1 PB DR2), GALEX, IUE, and others
**DB Open/Private**: Open (most missions; some proprietary periods)
**Modality**: ['Image', 'Spectrum', 'Light curve', 'Catalog']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: MAST Portal / MAST API (astroquery.mast)

> Space Telescope Science Institute (system reference) | 1997 | dataset | astronomy
#### 한 줄 요약
미국 우주망원경과학연구소(STScI)가 운영하는 NASA 우주 망원경 통합 아카이브. Hubble, JWST, TESS, Kepler, Pan-STARRS 데이터를 단일 포털에서 제공하는 천문학 K3 관측 데이터의 핵심 인프라. **정식 학술 논문이 아닌 기관 시스템 참고 항목(`@misc`)임에 유의.**

#### 개발/구축 배경
**기존 인프라의 한계**
- 1980년대~1990년대 NASA 우주 망원경들이 각각 별도 아카이브 운영 → 미션 간 데이터 통합 불가
- IUE(1978), HST(1990) 등 초기 미션 데이터의 장기 보존과 접근성 확보 필요

**이 시스템이 필요한 이유**
- STScI는 HST 과학 운영 기관으로 자연스럽게 UV/광학 아카이브 중심 역할
- 단일 포털에서 미션 간 교차 탐색 및 동일 천체의 다파장 데이터 결합 가능
- JWST(2021~) 데이터의 공식 아카이브로 지정되어 현재 천문학의 최첨단 데이터 관리

#### 시스템 구성
MAST Portal (mast.stsci.edu): 웹 기반 검색·시각화·다운로드. astroquery.mast: Python API. CAOM (Common Archive Observation Model): 미션 간 균일 메타데이터 스키마. DOI 기반 데이터셋 인용 지원. AWS S3 클라우드 사본(MAST in the Cloud) 제공.

#### 호스팅 미션 목록
| 미션 | 파장 범위 | 주요 데이터 유형 |
|---|---|---|
| Hubble Space Telescope (HST) | UV–광학–근적외선 | 이미지, 스펙트럼, 시계열 |
| James Webb Space Telescope (JWST) | 근적외선–중적외선 | 이미지, 스펙트럼 |
| TESS | 광학 | 광도 곡선, 전광 이미지 |
| Kepler / K2 | 광학 | 광도 곡선 (외계행성) |
| Pan-STARRS (PS1) | 광학 | 이미지, 카탈로그 |
| GALEX | UV | 이미지, 스펙트럼 |
| IUE (1978–1996) | UV | 스펙트럼 (레거시) |
| FUSE | 원자외선 | 스펙트럼 |

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| MAST Portal | mast.stsci.edu — 웹 GUI 탐색·다운로드 |
| astroquery.mast | Python 라이브러리, 배치 쿼리 |
| MAST API (REST) | JSON/VO Table 반환 |
| AWS S3 | s3://stpubdata/ — 클라우드 직접 접근 |

#### 주요 통계 (model knowledge)
| 항목 | 수치 |
|---|---|
| 운영 시작 | 1997년 (IUE 아카이브 기반) |
| 호스팅 미션 | 20개 이상 |
| HST 축적 데이터 | ~200 TB+ |
| Pan-STARRS DR2 | ~1 PB |
| JWST 연간 데이터 생산 | ~50–100 TB/yr |
| 접근 | 공개 (독점 기간 경과 후) |

#### 한계점
- 전파·X선·감마선 미션은 MAST 미호스팅 (별도 NRAO, Chandra, Fermi 아카이브)
- 일부 미션 데이터는 독점 기간(12~18개월) 존재
- 대용량 데이터셋 (TESS 전광 이미지, Pan-STARRS)은 로컬 다운로드 비현실적 — 클라우드 분석 필요
- 미션 간 데이터 포맷 불균일 (FITS 기반이나 확장 구조 상이)

## 관련 정보
- **포털**: [https://archive.stsci.edu](https://archive.stsci.edu)
- **MAST Portal**: [https://mast.stsci.edu](https://mast.stsci.edu)
