---
title: "NOAA National Centers for Environmental Information (NCEI)"
bib_key: "noaa_ncei"
year: 2015
domain: earth, climate
type: dataset
venue: National Oceanic and Atmospheric Administration (system reference)
paper_link: https://www.ncei.noaa.gov
---
# NOAA National Centers for Environmental Information (NCEI)

noaa_ncei | 2015 | National Oceanic and Atmospheric Administration (system reference) | dataset | [earth, climate] | [portal](https://www.ncei.noaa.gov)

**DB**: NOAA NCEI — world's largest archive for weather, climate, and geophysical data
**DB size**: ~60 PB (archive + backup copy, per ncei.noaa.gov/about); 매일 ~20 TB 신규 수집
**DB Open/Private**: Open (대부분 공개)
**Modality**: ['Time series', 'Satellite image', 'Gridded data', 'Station data']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NOAA NCEI 포털 / CDO (Climate Data Online) API

> National Oceanic and Atmospheric Administration (system reference) | 2015 | dataset | earth, climate
#### 한 줄 요약
2015년 NOAA의 세 개 데이터 센터(NCDC·NGDC·NODC) 통합으로 출범한 세계 최대 기상·기후 아카이브. 100 PB 이상의 기후 기록(지상 관측, 위성, 해양, 지구물리)을 보유하며 GHCN, GSOD, OISST 등 수십 개 핵심 기후 데이터셋을 공개 배포. **정식 학술 논문이 아닌 기관 시스템 참고 항목(`@misc`)임에 유의.**

#### 개발/구축 배경
**기존 인프라의 한계**
- NOAA 내 기상(NCDC)·지구물리(NGDC)·해양(NODC) 데이터가 분산 운영되어 통합 탐색 불가
- 1970년대 디지털화 이전 기상 관측 기록의 장기 보존 필요
- 기후 변화 모니터링을 위한 100년 이상 연속 균질 시계열 필요

**이 시스템이 필요한 이유**
- 기후 기준치(Climate Normals), 극단값 기록, 지구 온도 변화 추적의 단일 권위 출처
- IPCC, 미국 국가 기후 평가(NCA), 기상 예보 모델 검증의 기초 데이터
- 보험·농업·에너지·도시 계획 등 기후 관련 의사결정 지원

#### 시스템 구성
NCEI는 3개 전임 기관의 통합:
- **NCDC** (National Climatic Data Center, 1951~): 기상·기후 기록
- **NGDC** (National Geophysical Data Center, 1964~): 지자기·지진·해안 데이터
- **NODC** (National Oceanographic Data Center, 1961~): 해양 온도·염분·해류

주요 데이터셋: GHCN (Global Historical Climatology Network), GSOD (Global Surface Summary of Day), OISST (Optimum Interpolation SST), NSIDC 협력 빙하·적설, NEXRAD 레이더 아카이브.

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| CDO (Climate Data Online) | ncei.noaa.gov/cdo-web/ — 관측소별 데이터 다운로드 |
| NCEI API | api.ncei.noaa.gov — RESTful JSON API |
| THREDDS/OPeNDAP | 격자 데이터 원격 부분 다운로드 |
| S3 클라우드 | AWS Open Data — NOAA 위성·기상 데이터 |

#### 제공 데이터 형식
- 지상 관측: CSV/JSON (GHCN-D, GSOD, ISD)
- 격자 데이터: NetCDF (OISST, 재분석)
- 위성 이미지: GOES, AVHRR, VIIRS
- 지구물리: 지자기·지진·쓰나미 이벤트
- 해양: CTD(수온·염분), 파도, 해수면 변화

#### 주요 통계 (ncei.noaa.gov/about 기준)
| 항목 | 수치 |
|---|---|
| 총 보유 데이터 | **~60 PB** (archive + backup copy, ncei.noaa.gov/about 확인) |
| 일일 신규 수집 | **~20 TB** |
| GHCN-D 관측소 수 | **~100,000** 개+ |
| 기록 기간 | **140+ 년** (일부 1880년대 시작) |
| 설립 | 2015년 (NCDC+NGDC+NODC 통합) |
| 접근 | 공개 (무료) |

#### 한계점
- 데이터 형식과 API가 다양하여 일관된 RAG 파이프라인 구축 어려움
- 역사 관측소 데이터의 품질 관리 불균일 (균질화 필요)
- 일부 고해상도 실시간 데이터는 상업적 재배포 제한
- 아카이브 규모가 방대하여 특정 데이터셋 탐색에 도메인 지식 필요

## 관련 정보
- **포털**: [https://www.ncei.noaa.gov](https://www.ncei.noaa.gov)
- **CDO**: [https://www.ncei.noaa.gov/cdo-web/](https://www.ncei.noaa.gov/cdo-web/)
