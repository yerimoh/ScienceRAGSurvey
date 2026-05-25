---
title: "Quantum chemistry structures and properties of 134 kilo molecules"
bib_key: "ramakrishnan2014quantum"
year: 2014
domain: chem
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/sdata.2014.22
---
# Quantum chemistry structures and properties of 134 kilo molecules

ramakrishnan2014quantum | 2014 | Scientific Data | dataset | [chem] | [paper](https://doi.org/10.1038/sdata.2014.22)

**DB**: QM9
**DB size**: 133,885개 안정 소형 유기 분자 (GDB-17 9중원자 이하 서브셋)
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: QM9 (DFT/B3LYP/6-31G(2df,p) 계산 결과)

> Scientific Data | 2014 | dataset | chem
#### 📌 한 줄 요약
QM9는 GDB-17 화학 우주에서 중원자 9개 이하 유기 분자 133,885개에 대한 B3LYP/6-31G(2df,p) 수준의 기하 구조·에너지·전자·열역학 성질을 제공하는 표준 양자화학 벤치마크 데이터셋이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 분자 크기에 따라 조합적으로 증가하는 화학 공간을 체계적으로 탐색할 계산 데이터셋이 없었음
- 하이브리드 QM/ML 방법 개발 및 구조-성질 관계 분석을 위한 일관된 대규모 데이터셋 부재
**이 시스템이 필요한 이유**
- 기계학습 퍼텐셜 및 분자 성질 예측 모델의 훈련·검증용 표준 벤치마크 필요
- 신약 발견 및 재료 설계를 위한 화학 공간의 체계적 계산 탐색

#### 🔨 시스템 구성
GDB-17 화학 우주 데이터베이스에서 C, H, O, N, F 원소로 이루어진 중원자 9개 이하 분자 134k 서브셋을 추출한다. PM7 기하 최적화 후 B3LYP/6-31G(2df,p) 수준에서 재최적화. 에너지·엔탈피·자유에너지 원자화 에너지, 쌍극자 모멘트, 분극률, 프론티어 오비탈 고유값 등 계산. C7H10O2 화학식의 6,095개 이성질체에 대해 추가로 G4MP2 수준 계산.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 공개 저장소 | figshare/원저자 제공 데이터 다운로드 |
| QM9 형식 | xyz 형식 분자 구조 + 성질 파일 |

#### 📤 제공 데이터 형식
- xyz 형식 3D 기하 구조
- 스칼라 성질 (에너지, 엔탈피, 자유에너지, 쌍극자 모멘트, 분극률)
- 진동 주파수
- HOMO/LUMO 에너지 및 갭

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 분자 수 (총 추출) | 133,885 |
| 화학식 수 | 621 stoichiometries |
| 최다 이성질체 화학식 | C7H10O2 (6,095개) |
| 계산 수준 | DFT/B3LYP/6-31G(2df,p) |

#### ⚠️ 한계점
- C, H, O, N, F 원소만 포함 (S, Br, Cl, I, 금속 제외)
- 중원자 9개 이하 소분자만 포함하여 drug-like 분자 (MW>250) 커버 제한
- 134k 중 3,054개는 기하 일관성 검증 실패

## 관련 정보
- **논문**: [Quantum chemistry structures and properties of 134 kilo molecules](https://doi.org/10.1038/sdata.2014.22)
