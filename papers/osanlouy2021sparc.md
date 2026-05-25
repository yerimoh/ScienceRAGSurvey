---
title: "The SPARC DRC: building a resource for the autonomic nervous system community"
bib_key: "osanlouy2021sparc"
year: 2021
domain: medical, bio
type: dataset
venue: Frontiers in Physiology
paper_link: https://doi.org/10.3389/fphys.2021.693735
---
# The SPARC DRC: building a resource for the autonomic nervous system community

osanlouy2021sparc | 2021 | Frontiers in Physiology | dataset | [medical, bio] | [paper](https://doi.org/10.3389/fphys.2021.693735)

**DB**: SPARC (Stimulating Peripheral Activity to Relieve Conditions) Data and Resource Center
**DB size**: 논문에서 정확한 건수 명시 안 됨 — SPARC 컨소시엄 큐레이션 데이터셋 모음
**DB Open/Private**: Open (sparc.science)
**Modality**: Image (장기 스캐폴드, 2D 평면 지도), Structured Table (실험 데이터, 수학 모델)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: SPARC 데이터 포털 (sparc.science)

> Frontiers in Physiology | 2021 | dataset | medical, bio

#### 📌 한 줄 요약
NIH 지원 SPARC 프로그램의 데이터 및 자원 센터(DRC)로, 포유류 자율신경계의 실험 데이터·수학 모델·시뮬레이션 도구를 큐레이션·주석화하고 Google Maps 형식의 2D 평면 지도와 3D 장기 스캐폴드를 통해 신경조절 연구 커뮤니티에 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 자율신경계 데이터가 분산되어 통합 검색 및 교차 종 비교 불가
- 신경조절 장치 개발을 위한 계산 모델 접근 경로 부재
- 자율신경 해부학적 연결성 지도의 표준화 자원 없음

**이 시스템이 필요한 이유**
- NIH-SPARC 프로그램의 실험 데이터와 모델을 단일 지식베이스로 통합 필요
- 자율신경과학자 및 의료기기 제조업체를 위한 신경조절 가설 검증 플랫폼 필요

#### 🔨 시스템 구성
Auckland Bioengineering Institute 주도. SPARC 컨소시엄 제공 데이터·수학 모델을 큐레이션·주석화하여 단일 지식베이스로 통합. 의미론적 검색 인터페이스 + Google Maps 형식 2D 평면 지도(연결성 표시) + 3D 해부학 장기 스캐폴드(교차 종 비교 공통 좌표 프레임워크) 포함. 데이터 업로드, 큐레이션, 영상 세그멘테이션, 평면 지도 등록, 웹 포털 표시 파이프라인 구현. 온라인 계산 시설 연결로 신경조절 가설 검증 지원.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| SPARC 포털 | https://sparc.science — 무료 공개 접근 |
| DOI | https://doi.org/10.3389/fphys.2021.693735 |

#### 📤 제공 데이터 형식
- 2D 평면 연결성 지도 (신경 회로 다이어그램)
- 3D 해부학 장기 스캐폴드
- 실험 데이터 (전기생리학, 영상 등)
- 수학 모델 및 시뮬레이션 파일

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 지원 기관 | **NIH (SPARC 프로그램)** |
| 주요 초점 | **포유류 자율신경계** |
| 포털 기능 | **의미론적 검색, 2D 평면 지도, 3D 스캐폴드** |

#### ⚠️ 한계점
- 논문에서 정확한 데이터셋 건수·종 수 명시 안 됨
- 데이터 큐레이션·주석화 품질이 기여 기관별 상이
- 일부 장기·종의 스캐폴드 미완성

## 관련 정보
- **논문**: [The SPARC DRC: building a resource for the autonomic nervous system community](https://doi.org/10.3389/fphys.2021.693735)
