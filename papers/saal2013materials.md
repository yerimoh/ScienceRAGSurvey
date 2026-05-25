---
title: "Materials Design and Discovery with High-Throughput Density Functional Theory: The Open Quantum Materials Database (OQMD)"
bib_key: "saal2013materials"
year: 2013
domain: material
type: dataset
venue: JOM
paper_link: https://doi.org/10.1007/s11837-013-0755-4
---
# Materials Design and Discovery with High-Throughput Density Functional Theory: The Open Quantum Materials Database (OQMD)

saal2013materials | 2013 | JOM | dataset | [material] | [paper](https://doi.org/10.1007/s11837-013-0755-4)

**DB**: Open Quantum Materials Database (OQMD)
**DB size**: 200,000+ DFT 계산 결정 구조 (논문 기준)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OQMD REST API, www.oqmd.org

> JOM | 2013 | dataset | material
#### 📌 한 줄 요약
노스웨스턴대학교 Wolverton 그룹이 구축한 오픈 양자 재료 데이터베이스로, 20만 개 이상의 DFT 계산 결정 구조 및 형성 에너지를 무료 공개하여 재료 설계·발견에 활용한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 고처리량 DFT 계산으로 생성된 재료 특성 데이터가 공개되지 않아 재현 및 재활용 불가
- 배터리, 경량합금, 코팅 등 실용적 재료 문제에 대한 대규모 열역학 데이터 부족
- 실험 기반 탐색만으로는 광대한 조성 공간 커버 불가능

**이 시스템이 필요한 이유**
- ICSD(무기 결정 구조 데이터베이스) 수록 화합물 + 흔한 결정 구조의 데코레이션으로 방대한 DFT 계산 수행
- Li-공기 배터리, Li-이온 배터리 음극/양극, Mg 합금 등 5개 재료 문제에 직접 적용
- 열역학 안정성(GCLP) 계산으로 새로운 안정 화합물 예측 가능

#### 🔨 시스템 구성
OQMD는 VASP을 사용한 DFT 계산(GGA-PBE 범함수)으로 결정 구조의 총 에너지 및 형성 에너지를 계산한다. ICSD 수록 구조와 흔한 프로토타입 구조의 원소별 데코레이션으로 구성된다. 글로벌 구성 리니어 프로그래밍(GCLP)을 통해 임의 조성의 열역학적 안정성 예측이 가능하다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹사이트 | www.oqmd.org — 인터랙티브 쿼리 및 탐색 |
| API | REST API — 구조·에너지 데이터 접근 |
| 데이터 다운로드 | 전체 데이터베이스 무료 다운로드 지원 |

#### 📤 제공 데이터 형식
- DFT 계산 결정 구조 (총 에너지, 최적화된 격자 상수)
- 형성 에너지 (eV/atom)
- 열역학적 안정성 (볼록 헐 분석)
- 밴드갭 (일부 화합물)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 DFT 계산 결정 구조 | **200,000+** (2013년 논문 기준) |
| 비교 실험 형성 에너지 | **1,670** 개 결정에 대해 검증 (kirklin2015) |
| 데이터 공개 | 무료 공개 (http://oqmd.org) |
| 적용 재료 문제 | 5개 (배터리 음극·양극·코팅, Mg 합금, ML 예측) |

#### ⚠️ 한계점
- 논문 출판 당시(2013) 기준 20만 개 이상; 2015년 kirklin2015 논문에서 약 30만 개로 확장 보고
- GGA 범함수의 체계적 오차로 인한 형성 에너지 부정확성 (실험값과 평균 약 0.1 eV/atom 오차)
- 동역학적 안정성, 열적·엔트로피 효과는 미포함
- 특정 원소계(전이금속 산화물, f-전자계)에서 DFT+U 미적용 시 정확도 저하

## 관련 정보
- **논문**: [Materials Design and Discovery with HT-DFT: The OQMD (JOM, 2013)](https://doi.org/10.1007/s11837-013-0755-4)
