---
title: "Building a knowledge graph to enable precision medicine"
bib_key: "chandak2023building"
year: 2023
domain: chem
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/s41597-023-01960-3
---
# Building a knowledge graph to enable precision medicine

chandak2023building | 2023 | Scientific Data | dataset | [chem] | [paper](https://doi.org/10.1038/s41597-023-01960-3)

**DB**: PrimeKG (Precision Medicine Knowledge Graph)
**DB size**: 17,080 질환, 4,050,249 관계, 10개 생물학적 스케일
**DB Open/Private**: Open
**Modality**: ['Structured', 'Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PrimeKG (그래프 구조 + 임상 가이드라인 텍스트)

> Scientific Data | 2023 | dataset | chem
#### 📌 한 줄 요약
PrimeKG는 20개 고품질 자원을 통합하여 17,080개 질환과 405만 개 관계를 포함하는 정밀의학 분석용 멀티모달 지식 그래프이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 질환 생물학 지식이 논문, 비표준화 저장소, 진화하는 온톨로지에 분산되어 있음
- 유전형에서 임상 표현형까지 다양한 생물학적 스케일을 통합한 지식 그래프가 없었음
**이 시스템이 필요한 이유**
- 분자·유전자 요인과 표현형 결과 간 관계를 AI로 분석하기 위한 통합 자원 필요
- 약물 재목적화(drug repurposing)를 위한 '적응증', '금기', '적응증 외 사용' 약물-질환 엣지 필요

#### 🔨 시스템 구성
20개 고품질 자원(DrugBank, UMLS, MONDO, NCBI Gene, UniProt 등)을 통합한다. 질환 관련 단백질 교란, 생물학적 과정·경로, 해부학적·표현형 스케일, 승인 약물 치료 작용 등 10개 생물학적 스케일을 포함. 임상 가이드라인의 언어 설명을 멀티모달 분석 지원을 위해 그래프와 결합.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 직접 다운로드 | 그래프 구조 파일 (노드·엣지 CSV) |
| 지속 업데이트 | 신규 데이터 통합 지침 제공 |
| Harvard Dataverse | 공식 데이터 저장소 |

#### 📤 제공 데이터 형식
- 그래프 노드·엣지 CSV
- 임상 가이드라인 텍스트
- 엔티티-관계 매핑

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 질환 | 17,080 |
| 관계 수 | 4,050,249 |
| 통합 생물학적 스케일 | 10 |
| 통합 자원 수 | 20 |

#### ⚠️ 한계점
- 특정 질환 영역(희귀 질환)은 데이터가 부족할 수 있음
- 온톨로지 업데이트에 따른 지속적 유지보수 필요
- 텍스트 기반 임상 가이드라인은 언어·버전 편차 존재

## 관련 정보
- **논문**: [Building a knowledge graph to enable precision medicine](https://doi.org/10.1038/s41597-023-01960-3)
