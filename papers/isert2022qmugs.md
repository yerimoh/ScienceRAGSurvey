---
title: "QMugs, quantum mechanical properties of drug-like molecules"
bib_key: "isert2022qmugs"
year: 2022
domain: chem
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/s41597-022-01390-7
---
# QMugs, quantum mechanical properties of drug-like molecules

isert2022qmugs | 2022 | Scientific Data | dataset | [chem] | [paper](https://doi.org/10.1038/s41597-022-01390-7)

**DB**: QMugs (Quantum-Mechanical Properties of Drug-like Molecules)
**DB size**: 665k+ 생물 활성 분자, ~2M 형태(conformers)
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: QMugs (GFN2-xTB + DFT/ωB97X-D/def2-SVP)

> Scientific Data | 2022 | dataset | chem
#### 📌 한 줄 요약
QMugs는 ChEMBL에서 추출한 665k개 이상의 drug-like 분자에 대한 반경험적(GFN2-xTB) 및 DFT(ωB97X-D/def2-SVP) 수준의 양자역학 성질을 제공하는 오픈 액세스 데이터셋이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- QM9 등 기존 QM 데이터셋은 소형 분자(9중원자 이하)에 한정되어 drug-like 분자 커버 미흡
- 생물 활성 관련 양자역학 성질 데이터를 포함한 대규모 컬렉션 부재
**이 시스템이 필요한 이유**
- Drug-like 분자 크기(MW 250-700)에서의 QM 성질 ML 모델 개발에 필요한 훈련 데이터
- 다중 수준 이론(반경험적+DFT)에서 학습하는 모델 지원

#### 🔨 시스템 구성
ChEMBL DB에서 생물학적·약리학적으로 관련된 분자를 추출한다. GFN2-xTB 반경험적 방법으로 기하 최적화 및 열역학 데이터 계산. DFT(ωB97X-D/def2-SVP) 수준에서 원자·분자 성질 추가 계산. DFT 밀도 행렬 및 오비탈 행렬도 포함.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| ETH Zurich 데이터 저장소 | DOI:10.3929/ethz-b-000482129 |

#### 📤 제공 데이터 형식
- 최적화된 분자 기하 구조 (xyz)
- 원자 성질 (GFN2-xTB 및 DFT 수준)
- 분자 성질 (쌍극자 모멘트, 분극률 등)
- DFT 밀도 및 오비탈 행렬

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 분자 수 | 665k+ |
| 형태 수 (conformers) | ~2M |
| 출처 DB | ChEMBL |

#### ⚠️ 한계점
- 계산 비용으로 인해 대형 분자(MW>700)는 포함되지 않음
- DFT 밀도 행렬 등 일부 데이터는 파일 크기가 매우 커 스토리지 요구사항 높음

## 관련 정보
- **논문**: [QMugs, quantum mechanical properties of drug-like molecules](https://doi.org/10.1038/s41597-022-01390-7)
