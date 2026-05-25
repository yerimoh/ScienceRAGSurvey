---
title: "Polymer expert — A software tool for de novo polymer design"
bib_key: "bicerano2024polymer"
year: 2024
domain: material
type: Method
venue: Computational Materials Science
paper_link: https://doi.org/10.1016/j.commatsci.2024.112810
---
# Polymer expert — A software tool for de novo polymer design

bicerano2024polymer | 2024 | Computational Materials Science | Method | [material] | [paper](https://doi.org/10.1016/j.commatsci.2024.112810)

**Retriever**: QSPR-based retrieval over polymer analog library (PEARL)
**Eval Task**: De novo polymer design targeting desired properties (biobased PET alternatives, polycarbonate alternatives, high dielectric constant polymers)
**Eval Metric**: Property prediction accuracy (QSPR), candidate generation quality
**Method Name**: Polymer Expert
**Modality**: Structured data (repeat unit structures, QSPR properties)

> Computational Materials Science | 2024 | Method | material
#### 📌 한 줄 요약
광범위한 고분자 유사체 라이브러리(PEARL)와 QSPR(정량적 구조-성질 관계) 기반 검색 증강 추론을 활용하여 목표 성능 사양에 맞는 신규 고분자 반복 단위를 신속하게 생성하는 de novo 고분자 설계 전문가 시스템이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 기존 고분자 설계는 전문가 직관에 의존하여 새로운 후보 탐색이 느리고 편향적
- 구조-성질 관계를 체계적으로 활용하는 자동화 설계 도구 부재

**이 시스템이 필요한 이유**
- 고분자 산업에서 목표 성능(유전상수, 기계적 특성, 생분해성)을 맞추는 신규 반복 단위 신속 발굴 필요
- 초기 데이터베이스를 대규모 유사체 라이브러리로 자동 확장하고 QSPR 예측을 통합하는 시스템 필요

#### 🔨 시스템 구성
Polymer Expert는 4단계로 구현된다: (1) 초기 반복 단위 데이터베이스 생성, (2) 대규모 유사체 반복 단위 데이터베이스(PEARL) 확장, (3) 광범위 적용 QSPR로 모든 반복 단위 특성 계산, (4) 재료 모델링 소프트웨어 스위트 내 검색 가능 라이브러리로 통합. 쿼리 시 목표 성능 사양에 대해 PEARL을 검색하여 최적 후보를 반환한다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 적용 사례 1 | PET 생분해성 대안 식별 |
| 적용 사례 2 | 비스페놀-A 폴리카보네이트 대안 발굴 |
| 적용 사례 3 | 폴리프로필렌 동등 성능 소재 탐색 |
| 적용 사례 4 | 높은 유전상수 고분자 발굴 |
| 주요 발견 | 대부분의 유망 후보가 직관적으로 식별하기 어렵고 비자명(non-obvious) |

#### ⚠️ 한계점
- QSPR 예측의 정확도는 훈련 데이터 범위에 한정
- 생성된 후보의 실제 합성 가능성 및 실험적 검증이 별도로 필요
- 강한 외부 검증자 없이 QSPR 예측값만으로 평가 — 약한 검증(weak verification) 범주

## 관련 정보
- **논문**: [https://doi.org/10.1016/j.commatsci.2024.112810](https://doi.org/10.1016/j.commatsci.2024.112810)
