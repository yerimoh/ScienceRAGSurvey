---
title: "The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar, and APOGEE-2 Data"
bib_key: "abdurro2022seventeenth"
year: 2022
domain: astronomy
type: dataset
venue: The Astrophysical Journal Supplement Series
paper_link: https://arxiv.org/abs/2112.02026
---
# The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar, and APOGEE-2 Data

abdurro2022seventeenth | 2022 | The Astrophysical Journal Supplement Series | dataset | [astronomy] | [paper](https://arxiv.org/abs/2112.02026)

**DB**: SDSS Data Release 17 (DR17) — final data release of SDSS-IV
**DB size**: ~4.9M spectra cumulative; MaNGA: over 10,000 galaxy IFU cubes; APOGEE-2: over 650,000 stars; MaStar: almost 30,000 unique stars (abstract verified, arXiv:2112.02026)
**DB Open/Private**: Open
**Modality**: ['Spectrum', 'Catalog', 'IFU cube']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: SDSS DR17 (SDSS-IV final release)

> The Astrophysical Journal Supplement Series | 2022 | dataset | astronomy
#### 한 줄 요약
SDSS-IV의 최종(완전) 공개 데이터 릴리스. MaNGA(적분시야분광), MaStar(항성 스펙트럼 라이브러리), APOGEE-2(근적외선 항성 분광)의 완전 공개와 함께 SDSS 역사상 가장 많은 누적 스펙트럼을 제공하며, 수억 개의 천체를 카탈로그화한 SDSS의 20년 성과를 총결산한다.

#### 개발/구축 배경
**기존 인프라의 한계**
- SDSS-I/II/III를 거치며 측광 및 단일 광섬유 분광이 주류였으나 은하 내 공간 분해 분광(IFU) 데이터 부재
- 근적외선 항성 분광 기반 은하수 화학 진화 연구 데이터 부재
- 항성 대기 파라미터 측정을 위한 균일한 스펙트럼 라이브러리 부재

**이 시스템이 필요한 이유**
- SDSS-IV (2014–2020)는 MaNGA, MaStar, APOGEE-2, eBOSS 4개 서브서베이로 구성
- DR17은 이 4개 서브서베이의 완전 최종 공개 — 추가 데이터 릴리스 없음
- SDSS-V (2020~)로 이어지는 레거시 데이터셋 확정판

#### 시스템 구성
- **MaNGA**: 2.5m SDSS 망원경 + IFU 광섬유 묶음으로 10,000개 이상 은하의 2D 분광 지도 생성
- **MaStar**: ~30,000개 고유 항성의 스펙트럼 라이브러리 (3622–10354Å, R~1800)
- **APOGEE-2**: H밴드 근적외선 분광 (1.51–1.70μm, R~22,500), 650,000개 이상 항성
- **eBOSS**: 퀘이사·LRG·ELG 우주론 분광 (DR16에서 완전 공개)

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| SkyServer / CasJobs | skyserver.sdss.org — SQL 쿼리 |
| Science Archive Server | data.sdss.org/sas/dr17/ — FITS 직접 다운로드 |
| Marvin | MaNGA 전용 분석 플랫폼 |

#### 제공 데이터 형식
- IFU 분광 데이터 큐브 (MaNGA, FITS)
- 항성 분광 카탈로그 (MaStar, APOGEE-2)
- 측광 카탈로그 (ugriz + 적외선)
- 값-추가 카탈로그 (VAC): 항성 파라미터, 화학 조성, 운동학

#### 주요 통계
| 항목 | 수치 |
|---|---|
| MaNGA 은하 | **10,000+** 개 IFU 스펙트럼 큐브 (abstract: "over 10,000") |
| MaStar 항성 | **~30,000** 개 고유 항성 (abstract: "almost 30,000") |
| APOGEE-2 항성 | **650,000+** 개 (abstract: "over 650,000") |
| 누적 SDSS 스펙트럼 | **~4.9M** 개 |
| DR17 카탈로그 공개 | 2022년 1월 |

#### 한계점
- DR17은 SDSS-IV의 최종 릴리스로 이후 업데이트 없음; 최신 데이터는 SDSS-V 참조
- MaNGA의 공간 분해능은 ~1–2 kpc (z~0.03) 수준으로 고적색편이 은하 미적용
- APOGEE-2는 근적외선 전용으로 먼지 소광이 적은 은하면 방향 관측에 최적화

## 관련 정보
- **논문**: [https://arxiv.org/abs/2112.02026](https://arxiv.org/abs/2112.02026)
- **데이터 포털**: [https://www.sdss.org/dr17](https://www.sdss.org/dr17)
