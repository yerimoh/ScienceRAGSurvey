---
title: "BindingDB: a web-accessible database of experimentally determined protein-ligand binding affinities"
bib_key: "DBLP:journals/nar/LiuLWJG07"
year: 2007
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkl999
---
# BindingDB: a web-accessible database of experimentally determined protein-ligand binding affinities

DBLP:journals/nar/LiuLWJG07 | 2007 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkl999)

**DB**: BindingDB (초기 버전)
**DB size**: ~20,000 결합 친화도 측정치, 110 단백질 타겟, ~11,000 소분자 리간드
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: BindingDB web interface (bindingdb.org)

> Nucleic Acids Research | 2007 | dataset | chem
#### 📌 한 줄 요약
BindingDB는 실험적으로 결정된 단백질-리간드 결합 친화도를 수집한 공개 DB로, 약물 타겟 단백질을 중심으로 문헌에서 추출한 ~2만 개의 결합 데이터를 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 실험적 단백질-리간드 결합 친화도 데이터가 문헌에 분산되어 계산화학 및 약물 발견에 활용하기 어려웠음
- PDB 구조 데이터와 결합 친화도 정량 데이터의 통합 자원이 없었음
**이 시스템이 필요한 이유**
- 가상 스크리닝 방법 검증에 필요한 실험적 결합 데이터셋 필요
- 약물 타겟 단백질에 대한 SAR 분석 지원

#### 🔨 시스템 구성
과학 문헌에서 약물 타겟 또는 후보 약물 타겟 단백질에 대한 결합 친화도 데이터를 추출한다. PDB의 구조 데이터와 PubMed의 문헌과 연결. 구조, 부분구조, 유사도 검색; 단백질 서열 검색; 친화도 범위·분자량 검색 지원. 가상 스크리닝 도구도 포함.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | bindingdb.org 다양한 검색 유형 지원 |
| SDfile 다운로드 | 주석된 SDF 형식 데이터셋 다운로드 |
| 사용자 화합물 DB | 업로드한 화합물에 대한 가상 스크리닝 |

#### 📤 제공 데이터 형식
- 주석된 SDfile (화합물 구조 + 결합 친화도)
- 단백질 서열 정보
- PDB ID 링크
- PubMed ID 링크

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 결합 친화도 측정치 | ~20,000 |
| 단백질 타겟 (isoform·변이체 포함) | 110 |
| 소분자 리간드 | ~11,000 |

#### ⚠️ 한계점
- 초기 버전으로 데이터 범위가 제한적 (약물 타겟 중심)
- 수동 추출 방식으로 데이터 추가 속도 제한

## 관련 정보
- **논문**: [BindingDB: a web-accessible database of experimentally determined protein-ligand binding affinities](https://doi.org/10.1093/nar/gkl999)
