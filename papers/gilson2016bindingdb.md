---
title: "BindingDB in 2015: a public database for medicinal chemistry, computational chemistry and systems pharmacology"
bib_key: "gilson2016bindingdb"
year: 2016
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkv1072
---
# BindingDB in 2015: a public database for medicinal chemistry, computational chemistry and systems pharmacology

gilson2016bindingdb | 2016 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkv1072)

**DB**: BindingDB (2015 update)
**DB size**: 1M+ 데이터 항목 (주로 문헌 및 US 특허 기반)
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: BindingDB web interface + 고급 교차 검색

> Nucleic Acids Research | 2016 | dataset | chem
#### 📌 한 줄 요약
BindingDB의 2015년 업데이트로, 1백만 개 이상의 단백질-소분자 상호작용 데이터와 US 특허 바이오활성 데이터를 통합하고 타겟 예측·가상 스크리닝 도구를 강화하였다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 2007년 이후 데이터 규모가 크게 확장되었으나 특허 데이터 통합이 이루어지지 않았음
- 시스템 약리학 분석을 위한 도구가 부족했음
**이 시스템이 필요한 이유**
- US 특허에서 대량의 새로운 결합 데이터 추출 가능성
- 화합물의 잠재적 단백질 타겟 예측(폴리파마콜로지) 도구 수요

#### 🔨 시스템 구성
과학 논문 및 US 특허에서 단백질-소분자 결합 데이터를 추출한다. 고급 검색 도구(텍스트, 화학 구조, 단백질 서열, 수치 친화도 교차 검색)를 제공한다. PDB, PubMed, ZINC, 경로 정보와 연동. 타겟 예측 및 가상 스크리닝 도구 포함. 동족체(congeneric series) 데이터셋 제공.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | www.bindingdb.org 고급 교차 검색 |
| 다운로드 | SDF, TSV 형식 데이터셋 |
| 프로그래밍 방식 | 웹 서비스 API |
| 동족체 데이터셋 | 약물 설계 방법 검증용 특별 세트 |

#### 📤 제공 데이터 형식
- 단백질-리간드 결합 친화도 (Ki, IC50, Kd, EC50)
- 화합물 구조 (SMILES, SDF)
- 단백질 서열 정보
- 특허 및 문헌 출처 정보

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 데이터 항목 | 1M+ |

#### ⚠️ 한계점
- 특허 데이터 추출은 구조화되지 않은 텍스트 처리의 어려움으로 오류 가능성 존재
- 타겟 예측 도구는 훈련 데이터 편향에 영향을 받을 수 있음

## 관련 정보
- **논문**: [BindingDB in 2015](https://doi.org/10.1093/nar/gkv1072)
