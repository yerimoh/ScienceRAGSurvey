---
title: "The Cambridge Structural Database"
bib_key: "groom2016csd"
year: 2016
domain: chem
type: dataset
venue: Acta Crystallographica Section B
paper_link: https://doi.org/10.1107/S2052520616003954
---
# The Cambridge Structural Database

groom2016csd | 2016 | Acta Crystallographica Section B | dataset | [chem] | [paper](https://doi.org/10.1107/S2052520616003954)

**DB**: CSD (Cambridge Structural Database)
**DB size**: 800,000 엔트리 (2016년 기준 CSD 커뮤니티 서비스)
**DB Open/Private**: Open (커뮤니티 서비스) / Subscription (전체 기능)
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CSD (CCDC 운영, CSD 커뮤니티 웹 서비스)

> Acta Crystallographica Section B | 2016 | dataset | chem
#### 📌 한 줄 요약
CSD는 CCDC(Cambridge Crystallographic Data Centre)가 50년 이상 운영해온 소형 유기·금속유기 분자의 결정 구조 전체 기록으로, 2016년 기준 80만 개 엔트리를 포함하는 구조 화학의 근본 자원이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 발표된 결정 구조 데이터가 각 저널 부록에 분산되어 통합 접근과 재사용이 어려웠음
**이 시스템이 필요한 이유**
- 구조 화학 데이터의 단일 권위 저장소로 발표 결정 구조 공유 표준화 필요
- 데이터 재사용성·발견가능성 향상을 위한 표준 식별자 및 연결 서비스 필요

#### 🔨 시스템 구성
발표된 유기·금속유기 소분자 결정 구조를 계산(자동) 및 전문 편집자(수동) 처리를 거쳐 입력한다. 화학 정체성과 실험 데이터의 신뢰성 있는 연결이 핵심 품질 관리 단계. CSD Communications로 저널 논문 없이도 구조 직접 기탁 가능. 표준 식별자 사용으로 다른 자원과의 링크 서비스 제공.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| CSD 커뮤니티 웹 서비스 | 무료, 전 세계 교육 기관 접근 가능 |
| CCDC 소프트웨어 | Mercury, ConQuest 등 (기관 라이선스) |
| API | CCDC API (프로그래밍 접근) |
| 제3자 소프트웨어 | 다양한 분자 모델링 소프트웨어 통합 |

#### 📤 제공 데이터 형식
- CIF (Crystallographic Information File) - 구조 데이터 표준
- 3D 좌표 및 결정 대칭 정보
- 화학 구조 (SMILES, InChI 연동)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| CSD 커뮤니티 서비스 엔트리 | 800,000 |
| 총 엔트리 (논문 기재 테이블) | 363,372 → 731,675 (2014→2015 누적) |
| 관련 논문 수 | 232,858 → 408,899 |
| 연간 신규 엔트리 | 34,030 → 60,122 |
| R-factor < 10% 비율 | 92~94% |

#### ⚠️ 한계점
- 전체 기능 및 데이터 이용은 기관 라이선스 필요
- 폴리머, 단백질 구조는 PDB로 별도 분리되어 있음
- 80만 엔트리의 방대한 규모로 체계적 데이터 마이닝에 전문 도구 필요

## 관련 정보
- **논문**: [The Cambridge Structural Database](https://doi.org/10.1107/S2052520616003954)
