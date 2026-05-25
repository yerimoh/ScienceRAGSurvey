---
title: "Gaia Data Release 3: Summary of the Content and Survey Properties"
bib_key: "vallenari2023gaia"
year: 2023
domain: astronomy
type: dataset
venue: Astronomy & Astrophysics
paper_link: https://arxiv.org/abs/2208.00211
---
# Gaia Data Release 3: Summary of the Content and Survey Properties

vallenari2023gaia | 2023 | Astronomy & Astrophysics | dataset | [astronomy] | [paper](https://arxiv.org/abs/2208.00211)

**DB**: Gaia Data Release 3 (GDR3) — ESA Gaia astrometric/photometric/spectroscopic all-sky survey
**DB size**: ~1,500 million (1.5 billion) sources with positions, parallaxes, proper motions; ~470 million with astrophysical parameters; ~220 million BP/RP spectra
**DB Open/Private**: Open
**Modality**: ['Astrometry', 'Photometry', 'Spectrum', 'Catalog']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Gaia DR3 (ESA Gaia satellite, L2 orbit, launched 2013)

> Astronomy & Astrophysics | 2023 | dataset | astronomy
#### 한 줄 요약
유럽우주국(ESA) Gaia 위성의 세 번째 데이터 공개로, 임무 초기 34개월 관측 데이터를 처리한 카탈로그. **약 15억 개 광원**에 대한 천체위치, 시차, 고유운동 및 광도 데이터 제공. 3,300만 개 광원의 시선속도, 2.2억 개 BP/RP 저해상도 스펙트럼, 4.7억 개 광원의 천체물리 파라미터를 포함하는 천문학 역사상 최대 규모 전천 목록 중 하나.

#### 개발/구축 배경
**기존 인프라의 한계**
- Hipparcos(1997) 카탈로그: 118,218개 항성의 시차 측정으로 당시 혁신적이었으나 규모와 정밀도 한계
- 지상 측성 카탈로그: 대기 굴절·온도 변화로 정밀도 제한, 전천 균일 관측 불가

**이 시스템이 필요한 이유**
- 마이크로초각(μas) 정밀도 시차로 은하계 3D 구조 지도 작성
- 단일 위성으로 전천을 반복 스캔하여 균일한 천체측성 기준 틀(ICRF 연결) 제공
- 시선속도·스펙트럼 포함으로 6D 위상공간(위치+속도) 완성

#### 시스템 구성
Gaia 위성: L2 리사쥬 궤도, 두 망원경(각도 106.5° 고정), SiC 경면. 주 카메라: 106 CCD (0.7 Giga-pixel). 스캐닝 법칙: 5~6시간마다 자전, 63.3일마다 세차. 데이터 처리: Gaia Data Processing and Analysis Consortium (DPAC, 유럽 9개국 450명+).

- **천체측성**: 위치·시차·고유운동 (G < 21 등급)
- **측광**: G, G_BP, G_RP 3-밴드
- **분광**: RVS (시선속도), BP/RP (저해상도 광학 스펙트럼)

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| Gaia Archive | gea.esac.esa.int — ADQL 쿼리 |
| CDS VizieR | vizier.cds.unistra.fr — 카탈로그 조회 |
| Gaia DR3 직접 다운로드 | ESA Science Data Centre |
| TAP 서비스 | 표준 IVOA TAP 프로토콜 |

#### 제공 데이터 형식
- 주 소스 카탈로그 (위치, 시차, 고유운동, G/GBP/GRP 측광)
- 시선속도 카탈로그 (RVS, ~33M 광원)
- BP/RP 평균 스펙트럼 (~220M 광원)
- RVS 평균 스펙트럼 (~1M 광원)
- 천체물리 파라미터 (Teff, logg, [Fe/H] 등, ~470M 광원)
- 변광성 카탈로그 (~10M, 24가지 유형)
- 태양계 천체 (~150,000개)
- 쌍성 궤도 요소 (~800,000쌍)

#### 주요 통계
| 항목 | 수치 |
|---|---|
| 전체 광원 수 | **~1,500,000,000** (15억) |
| 시선속도 광원 | **~33,000,000** |
| BP/RP 스펙트럼 | **~220,000,000** |
| 천체물리 파라미터 | **~470,000,000** 광원 |
| 변광성 | **~10,000,000** 개, 24유형 |
| 태양계 천체 | **~150,000** 개 |
| 소행성 반사 스펙트럼 | **~60,000** 개 |
| 쌍성 | **~800,000** 쌍 |
| 관측 기간 (GDR3) | 34개월 (임무 초기) |

#### 한계점
- GDR3는 임무 초기 34개월 데이터로 최종 Gaia DR4/DR5 대비 정밀도와 완전성 낮음
- 밝은 별(G < 6) 및 빽빽한 성단 영역에서 포화·혼잡도 문제로 정밀도 저하
- BP/RP 스펙트럼의 해상도 매우 낮음(R~50–100): 세부 원소 풍요도 측정 불가
- 시선속도 완전성은 G_RVS < 14 등급에 한정

## 관련 정보
- **논문**: [https://arxiv.org/abs/2208.00211](https://arxiv.org/abs/2208.00211)
- **Gaia Archive**: [https://gea.esac.esa.int/archive/](https://gea.esac.esa.int/archive/)
