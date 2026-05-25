---
title: "Gene ontology: tool for the unification of biology"
bib_key: "ashburner2000gene"
year: 2000
domain: bio
type: dataset
venue: Nature Genetics
paper_link: https://doi.org/10.1038/75556
---
# Gene ontology: tool for the unification of biology

ashburner2000gene | 2000 | Nature Genetics | dataset | [bio] | [paper](https://doi.org/10.1038/75556)

**DB**: Gene Ontology (GO)
**DB size**: 3개 독립 온톨로지 (biological process, molecular function, cellular component) — 세계 와이드 웹에서 공개 접근
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: GO Consortium 공개 온톨로지 (http://www.geneontology.org)

> Nature Genetics | 2000 | dataset | bio
#### 📌 한 줄 요약
모든 진핵생물에 적용 가능한 동적 통제 어휘(온톨로지)를 제공하여 유전자와 단백질의 생물학적 역할을 통합적으로 기술하는 Gene Ontology Consortium의 창립 논문이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 게놈 프로젝트의 완료로 핵심 생물학적 기능을 공유하는 유전자들이 모든 진핵생물에 걸쳐 존재함이 명확해졌지만, 종 간 기능 지식 이전을 위한 공통 어휘가 없었다
- 각 모델 생물체 데이터베이스(SGD, FlyBase, MGI)가 서로 다른 용어를 사용하여 종 간 비교가 어려웠다

**이 시스템이 필요한 이유**
- 한 생물체에서의 유전자 기능 지식을 다른 생물체로 이전하기 위한 공통 통제 어휘 필요
- 지식이 축적되고 변화함에 따라 갱신 가능한 동적 온톨로지 구조 요구
- 모델 생물체 데이터베이스 컨소시엄(SGD, FlyBase, MGI) 협력으로 공동 구축

#### 🔨 시스템 구성
Gene Ontology는 세 가지 독립 온톨로지로 구성된다: (1) **Biological Process** — 생물학적 목표 또는 기능에 기여하는 사건이나 분자 기능의 넓은 집합, (2) **Molecular Function** — 유전자 산물의 분자 수준 활동, (3) **Cellular Component** — 세포 내 위치 또는 세포 외 환경. 각 온톨로지는 월드 와이드 웹(http://www.geneontology.org)을 통해 접근 가능하다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | http://www.geneontology.org — 온톨로지 탐색 |
| 파일 다운로드 | OBO/OWL 형식의 온톨로지 파일 |

#### 📤 제공 데이터 형식
- GO 용어 및 정의 (OBO/OWL 형식)
- GO 주석 파일 (GAF 형식)
- 종별 유전자-GO 용어 매핑

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 온톨로지 수 | **3개** (Biological Process, Molecular Function, Cellular Component) |
| 적용 대상 | 모든 진핵생물 |
| 창립 컨소시엄 | SGD, FlyBase, MGI (효모, 파리, 마우스) |

#### ⚠️ 한계점
- 2000년 창립 논문으로, 초기에는 효모·파리·마우스 세 모델 생물체를 중심으로 구성되었다
- 온톨로지 용어의 지속적 갱신이 필요하여 레거시 주석과의 일관성 유지가 과제이다
- 모든 생물학적 과정에 대한 완전한 기술은 불가능하며 동적으로 확장되는 구조이다

## 관련 정보
- **논문**: [Gene ontology: tool for the unification of biology](https://doi.org/10.1038/75556)
