---
title: "ZINC: a free tool to discover chemistry for biology"
bib_key: "irwin2012zinc"
year: 2012
domain: chem
type: dataset
venue: Journal of Chemical Information and Modeling
paper_link: https://doi.org/10.1021/ci3001277
---
# ZINC: a free tool to discover chemistry for biology

irwin2012zinc | 2012 | Journal of Chemical Information and Modeling | dataset | [chem] | [paper](https://doi.org/10.1021/ci3001277)

**DB**: ZINC (2012 version)
**DB size**: 20M+ 상업적 구매 가능 분자
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ZINC web interface (zinc.docking.org)

> Journal of Chemical Information and Modeling | 2012 | dataset | chem
#### 📌 한 줄 요약
ZINC은 생물학적으로 관련된 형태로 제공되는 2천만 개 이상의 상업적 구매 가능 분자를 모은 공개 리간드 발견 자원으로, ready-to-dock 포맷으로 다운로드 가능하다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 구매 가능한 화합물 목록이 분산되어 있고, 도킹에 필요한 3D 형태로 준비되지 않은 경우가 많았음
- 생물학 연구자들이 계산화학 전문 지식 없이 화합물 검색을 수행하기 어려웠음
**이 시스템이 필요한 이유**
- 가상 스크리닝(virtual screening)을 위해 즉시 사용 가능한 3D 도킹 포맷 화합물 라이브러리 필요
- 구매 가능성 정보와 생물학적 활성 주석을 통합한 단일 자원 부재

#### 🔨 시스템 구성
상업적 화합물 목록을 수집하여 3D 생물학적 관련 형태(protonation state, tautomer 포함)로 변환한다. 구조, 생물 활성, 물리적 성질, 판매처, 카탈로그 번호, 이름, CAS 번호로 검색 가능하다. 소규모 커스텀 서브셋 생성·편집·공유·다운로드 기능 제공.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | zinc.docking.org 구조/성질 검색 |
| 서브셋 다운로드 | ready-to-dock 포맷(MOL2, SDF 등) |
| 커스텀 서브셋 | 필터링 후 직접 다운로드 |

#### 📤 제공 데이터 형식
- 3D 도킹 포맷 (MOL2, SDF)
- SMILES
- 물리화학적 성질 (MW, LogP, HBA/HBD 등)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 구매 가능 분자 | 20M+ |

#### ⚠️ 한계점
- 상업 카탈로그 기반이므로 실제 구매 가능 여부는 갱신 주기에 따라 변동
- 구매처별 가격·리드타임 정보는 외부 링크에 의존

## 관련 정보
- **논문**: [ZINC: a free tool to discover chemistry for biology](https://doi.org/10.1021/ci3001277)
