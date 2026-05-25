---
title: "PubChem 2023 update"
bib_key: "kim2023pubchem"
year: 2023
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkac956
---
# PubChem 2023 update

kim2023pubchem | 2023 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkac956)

**DB**: PubChem (2022 update)
**DB size**: 데이터 출처 120개 이상 신규 추가 (논문에 총 레코드 수 미기재)
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PUG-REST, PUG-View API

> Nucleic Acids Research | 2023 | dataset | chem
#### 📌 한 줄 요약
PubChem의 2022년 업데이트를 기술한 논문으로, Google Patents 통합, Cell Line·Taxonomy 컬렉션 추가, 바이오어세이 데이터 모델 개선 등 주요 확장 사항을 설명한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 특허 화학물질 데이터와 PubChem 간 연동이 불완전했음
- 세포주·분류군(taxon)별 화학 정보 접근이 체계적이지 않았음
**이 시스템이 필요한 이유**
- 특허 데이터(Google Patents)를 통합하여 화학 공간 커버리지 대폭 확대
- AI 모델 학습용 데이터 표준화 API 기능(standardize) 요구 증대

#### 🔨 시스템 구성
120개 이상 데이터 소스로부터 신규 데이터 통합. Google Patents 통합으로 특허 데이터 컬렉션 대폭 확장. Cell Line 및 Taxonomy 데이터 컬렉션 신설. 바이오어세이 데이터 모델 업데이트. PUG-REST와 PUG-View에 타겟 중심 다운로드(단백질·유전자·경로·세포주·분류군별) 기능 추가. PubChemRDF 대규모 업데이트 포함.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| PUG-REST | 화학 구조 표준화 옵션('standardize') 신규 지원 |
| PUG-View | 타겟 중심 데이터 다운로드 |
| Cell Line Collection | 특정 세포주의 화학 정보 빠른 접근 |
| Taxonomy Collection | 특정 분류군의 화학 정보 접근 |

#### 📤 제공 데이터 형식
- SMILES, InChI, SDF
- JSON, XML
- RDF (PubChemRDF)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 신규 데이터 소스 | 120개 이상 (2년간 추가) |
| 수록 바이오어세이 모델 | 업데이트됨 (구체적 수치 논문 미기재) |

#### ⚠️ 한계점
- 논문은 업데이트 기능 중심으로 기술되어 총 레코드 수 등 전체 규모 통계 미제공
- Google Patents 통합으로 인한 데이터 중복 및 품질 관리 과제 존재

## 관련 정보
- **논문**: [PubChem 2023 update](https://doi.org/10.1093/nar/gkac956)
