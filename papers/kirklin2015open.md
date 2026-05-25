---
title: "The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies"
bib_key: "kirklin2015open"
year: 2015
domain: material
type: dataset
venue: npj Computational Materials
paper_link: https://doi.org/10.1038/npjcompumats.2015.10
---
# The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies

kirklin2015open | 2015 | npj Computational Materials | dataset | [material] | [paper](https://doi.org/10.1038/npjcompumats.2015.10)

**DB**: Open Quantum Materials Database (OQMD)
**DB size**: nearly 300,000 DFT total energy calculations (논문 기준)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OQMD REST API, www.oqmd.org/download

> npj Computational Materials | 2015 | dataset | material
#### 📌 한 줄 요약
OQMD의 2015년 확장 보고서로, 약 30만 건의 DFT 총에너지 계산을 담고 있으며 1,670개 실험 형성 에너지와의 최대 규모 비교를 통해 DFT 정확도를 체계적으로 평가하고 ~3,200개의 새로운 안정 화합물을 예측한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 2013년 OQMD 최초 보고(saal2013) 이후 규모가 20만 개에서 30만 개 수준으로 확장
- DFT 계산의 오차 특성에 대한 체계적 검증이 부족했으며, 실험값과의 최대 규모 비교가 필요
- 새로운 안정 화합물의 대규모 예측을 위한 데이터 기반 필요

**이 시스템이 필요한 이유**
- 전체 데이터베이스를 무제한 공개(www.oqmd.org/download)하여 재료과학 커뮤니티의 활용 극대화
- 실험 측정값 간의 편차까지 함께 분석함으로써 DFT 오차의 실질적 기여도 평가

#### 🔨 시스템 구성
ICSD(무기 결정 구조 데이터베이스) 수록 화합물과 흔한 결정 구조 프로토타입의 원소별 데코레이션으로 구성된 대규모 DFT(VASP, GGA-PBE) 계산 데이터베이스. 볼록 헐(convex hull) 분석으로 열역학적 안정성을 평가하며, 미실현 화합물의 존재 예측에도 활용된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 전체 다운로드 | www.oqmd.org/download — 무제한 무료 |
| 웹 인터페이스 | www.oqmd.org — 구조·에너지 쿼리 |
| REST API | 프로그래밍 방식 접근 |

#### 📤 제공 데이터 형식
- DFT 총에너지 및 형성 에너지 (eV/atom)
- 최적화 결정 구조 (격자 상수, 원자 위치)
- 열역학적 안정성 (볼록 헐 분석)
- 예측 화합물 안정성 데이터

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 DFT 계산 건수 | **~300,000** (nearly 300,000, 논문 기준) |
| 비교 실험 형성 에너지 | **1,670** 개 (가장 큰 DFT vs 실험 비교) |
| 평균 절대 오차 (DFT vs 실험) | **0.096 eV/atom** |
| 실험값 간 편차 (MAE) | **0.082 eV/atom** |
| 예측 신규 안정 화합물 | **~3,200** 개 (미실현 화합물) |

#### ⚠️ 한계점
- GGA-PBE 범함수의 체계적 오차로 실험 형성 에너지 대비 평균 약 0.1 eV/atom 오차
- 실험 측정값 자체의 불확실성(0.082 eV/atom)으로 인해 DFT 오차와의 분리가 어려움
- 동역학적 안정성, 유한 온도 효과 미포함
- f-전자 계열 및 강상관 전이금속 산화물에서의 정확도 한계

## 관련 정보
- **논문**: [The OQMD: assessing the accuracy of DFT formation energies (npj Comput. Mater., 2015)](https://doi.org/10.1038/npjcompumats.2015.10)
