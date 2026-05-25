---
title: "USGS Earth Resources Observation and Science (EROS) Center"
bib_key: "usgs_eros"
year: 1973
domain: earth
type: dataset
venue: U.S. Geological Survey (system reference)
paper_link: https://www.usgs.gov/centers/eros
---
# USGS Earth Resources Observation and Science (EROS) Center

usgs_eros | 1973 | U.S. Geological Survey (system reference) | dataset | [earth] | [portal](https://www.usgs.gov/centers/eros)

**DB**: USGS EROS Center — Landsat and Earth observation archive
**DB size**: ~10 PB+ (Landsat 1–9 전체 기록 + 기타 위성 데이터); Landsat: 9백만+ 장면
**DB Open/Private**: Open (2008년 Landsat 완전 공개 정책 이후)
**Modality**: ['Satellite image', 'Multispectral', 'Thermal', 'Time series']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: EarthExplorer / USGS EROS Archive

> U.S. Geological Survey (system reference) | 1973 | dataset | earth
#### 한 줄 요약
1973년 설립된 USGS 지구 관측 데이터 아카이브. 1972년부터 현재까지 이어지는 **Landsat 1–9 전체 기록(50년 이상)**을 보유한 세계 최장 연속 지표면 위성 관측 아카이브. 2008년 무상 공개 정책 전환 이후 토지 이용 변화·삼림 감소·빙하 후퇴·도시 확장 연구의 핵심 K3 자원. **정식 학술 논문이 아닌 기관 시스템 참고 항목(`@misc`)임에 유의.**

#### 개발/구축 배경
**기존 인프라의 한계**
- 1960년대 이전 지구 표면 변화를 정기·균일하게 기록하는 디지털 수단 부재
- ERTS-1 (Earth Resources Technology Satellite, 후의 Landsat 1) 발사(1972)를 계기로 체계적 아카이브 필요

**이 시스템이 필요한 이유**
- Landsat은 16일 회귀 주기로 전 지구 지표를 반복 촬영 → 시계열 변화 감지 가능
- 2008년 Landsat 무상 공개(open archive)로 전 세계 연구자·정부·NGO의 활용 폭발적 증가
- NASA–USGS 공동 운영으로 Landsat 위성 연속성 보장

#### 시스템 구성
EROS 센터(사우스다코타주 수폴스): 주 데이터 처리·아카이브 시설. EarthExplorer(earthexplorer.usgs.gov): 웹 기반 탐색·주문·다운로드. ESPA(USGS EROS Science Processing Architecture): 온디맨드 데이터 처리.

Landsat 밴드 구성:
- Landsat 1–5 (MSS/TM): 4–7개 밴드, 30–80m 해상도
- Landsat 7 (ETM+): 8개 밴드, 15m 전색–30m 다중분광
- Landsat 8–9 (OLI/TIRS): 11개 밴드, 15–30m (열적외선 100m)

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| EarthExplorer | earthexplorer.usgs.gov — 장면 탐색·다운로드 |
| USGS M2M API | Machine-to-Machine API (JSON) |
| Google Earth Engine | GEE에 Landsat 컬렉션 통합 |
| AWS Open Data | s3://usgs-landsat/ — 클라우드 직접 접근 |

#### 제공 데이터 형식
- GeoTIFF (Landsat Collection 1/2 Surface Reflectance/Temperature)
- HDF (레거시)
- STACItem 메타데이터 (Collection 2 이후)
- 분석 준비 데이터(ARD): 타일 기반, 대기 보정 완료

#### 주요 통계 (model knowledge)
| 항목 | 수치 |
|---|---|
| Landsat 연속 관측 기간 | **50년+** (1972년~현재) |
| 총 Landsat 장면 수 | **~9,000,000** 장면+ |
| 위성 세대 | **Landsat 1–9** (9세대) |
| 공간 해상도 | 15–80 m (밴드·세대 별) |
| 반복 주기 | 16일 (단일 위성), 8일 (Landsat 8+9 조합) |
| 무상 공개 전환 | 2008년 |
| 설립 | 1973년 |

#### 한계점
- 16일 회귀 주기로 급격한 사건(홍수·화재) 일별 모니터링 불가 (Sentinel-2 8–10일 주기와 보완)
- 구름 피복에 의한 장면 사용 불가 비율 높음 (열대 지역 40%+ 영향)
- 초기 Landsat 1–4 데이터의 기하 보정 정확도 낮음
- 30m 해상도로 도심 세부 분석·개별 농지 모니터링 부족

## 관련 정보
- **포털**: [https://www.usgs.gov/centers/eros](https://www.usgs.gov/centers/eros)
- **EarthExplorer**: [https://earthexplorer.usgs.gov](https://earthexplorer.usgs.gov)
