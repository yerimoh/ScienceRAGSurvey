---
title: "Architecture and Design of Storage and Data Management for the NASA Earth Observing System Data and Information System (EOSDIS)"
bib_key: "DBLP:conf/mss/KoblerBCH95"
year: 1995
domain: earth
type: dataset
venue: IEEE Symposium on Mass Storage Systems (MSS 1995)
paper_link: https://doi.org/10.1109/MASS.1995.528217
---
# Architecture and Design of Storage and Data Management for the NASA EOSDIS

DBLP:conf/mss/KoblerBCH95 | 1995 | MSS 1995 | dataset | [earth] | [paper](https://doi.org/10.1109/MASS.1995.528217)

**DB**: NASA Earth Observing System Data and Information System (EOSDIS) / NASA Earthdata
**DB size**: 수십 PB급 (지구관측 위성 데이터 통합 아카이브; 1994년 이후 지속 축적)
**DB Open/Private**: Open (NASA Earthdata 계정 필요, 무료)
**Modality**: ['Satellite image', 'Gridded data', 'Time series', 'Tabular']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NASA Earthdata / EOSDIS (earthdata.nasa.gov)

> MSS 1995 | 1995 | dataset | earth
#### 📌 한 줄 요약
NASA의 지구관측위성 데이터 통합 아카이브 EOSDIS의 스토리지·데이터 관리 아키텍처를 기술한 1995년 논문. 육지·대기·해양·빙권을 커버하는 EOS 위성 데이터의 분산 저장·배포 시스템 설계를 설명하며, 현재의 NASA Earthdata 포털로 이어지는 인프라의 초기 설계 문서.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 1990년대 이전 NASA 지구관측 데이터는 분산된 개별 미션 팀이 관리하여 통합 검색·접근 불가
- 테라바이트~페타바이트 규모 위성 데이터의 장기 보존 및 과학자 배포 인프라 부재
- Terra, Aqua 등 EOS 위성군 출범에 맞춰 표준화된 데이터 시스템 필요

**이 시스템이 필요한 이유**
- 지구 시스템(육지·대기·해양·빙권) 전체를 커버하는 통합 지구관측 데이터 아카이브 구축
- DAAC(Distributed Active Archive Centers) 분산 네트워크로 도메인별 전문 처리·배포
- 표준 데이터 형식(HDF-EOS)과 메타데이터 체계로 다중 미션 데이터 상호 운용

#### 🔨 시스템 구성
EOSDIS는 12개 DAAC(분산 활성 아카이브 센터)로 구성된 분산 네트워크. 각 DAAC는 도메인별 전문 처리 역할을 담당(예: NSIDC→빙권, SEDAC→사회-환경, ORNL DAAC→탄소·생태). 데이터 표준: HDF-EOS (계층적 데이터 형식). EOSDIS Data Pool: 공개 FTP/HTTP 다운로드. Earthdata Search(현재): 통합 메타데이터 카탈로그 검색.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| Earthdata Search | search.earthdata.nasa.gov — 통합 메타데이터 검색 및 데이터 주문 |
| DAAC 직접 접근 | 각 DAAC 포털 (NSIDC, LP DAAC, ORNL, GES DISC 등) |
| OPeNDAP | 격자 데이터 원격 부분 접근 |
| S3/클라우드 | NASA Earthdata Cloud (AWS) — 고성능 클라우드 분석 |

#### 📤 제공 데이터 형식
- 위성 영상: HDF-EOS, GeoTIFF, NetCDF
- 대기 데이터: AIRS, MODIS, MERRA-2 재분석
- 육지 데이터: MODIS 식생, 지표 반사율, 화재
- 해양 데이터: SST, 해수면, 클로로필
- 빙권: 해빙 면적, 빙하, 적설

#### 📊 주요 통계 (논문/공식 자료 기준)
| 항목 | 수치 |
|---|---|
| 아카이브 규모 | **수십 PB** (2020년대 기준) |
| DAAC 수 | **12개** 분산 아카이브 센터 |
| 논문 출판 | MSS 1995 (IEEE) — 시스템 초기 설계 문서 |
| 접근 | 공개 (NASA Earthdata 계정 무료 등록) |
| 데이터 범위 | 육지 · 대기 · 해양 · 빙권 전체 |

#### ⚠️ 한계점
- 1995년 논문이므로 현재 EOSDIS/Earthdata의 실제 운영 규모·기능과 크게 다름 (참고 문헌으로서의 한계)
- 도메인별 데이터 형식이 상이하여 다중 DAAC 데이터 통합에 전처리 부담
- 고해상도 원시 데이터는 파일 크기가 수 GB~수십 GB에 달해 RAG용 직접 활용 어려움
- 과학 분야 RAG 시스템 중 EOSDIS를 검색 코퍼스로 활용한 사례 없음

## 관련 정보
- **논문**: [doi:10.1109/MASS.1995.528217](https://doi.org/10.1109/MASS.1995.528217)
- **현재 포털**: [NASA Earthdata](https://www.earthdata.nasa.gov)
