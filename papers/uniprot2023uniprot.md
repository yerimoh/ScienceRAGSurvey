---
title: "UniProt: the Universal Protein Knowledgebase in 2023"
bib_key: "uniprot2023uniprot"
year: 2023
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkac1052
---
# UniProt: the Universal Protein Knowledgebase in 2023

uniprot2023uniprot | 2023 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/gkac1052)

**DB**: UniProt Knowledgebase (UniProtKB = Swiss-Prot + TrEMBL)
**DB size**: 227M+ sequences (2023년 논문 기준)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: UniProt REST API / FTP

> Nucleic Acids Research | 2023 | dataset | bio
#### 📌 한 줄 요약
전 세계 단백질 서열과 기능 주석의 표준 인프라로, 2억 2,700만 개 이상의 단백질 서열을 무료로 제공하며 150개 이상의 외부 데이터베이스와 교차 참조를 지원한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 기존 단백질 데이터베이스들은 수작업 검토 데이터(Swiss-Prot)와 자동 주석 데이터(TrEMBL)가 분리되어 있어 통합 접근이 불편했다
- 시퀀싱 기술의 발전으로 단백질 서열 수가 폭발적으로 증가하면서 자동화된 품질 관리 필요성이 대두되었다

**이 시스템이 필요한 이유**
- 고품질 수작업 검토 항목(Swiss-Prot)과 자동 주석 항목(TrEMBL)을 단일 데이터베이스로 통합 제공
- 기계 학습 기법을 활용한 자동 주석 시스템으로 미검토 항목의 품질을 보완
- 모든 분류 그룹에 대한 참조 프로테옴 구축을 목표로 진행 중

#### 🔨 시스템 구성
UniProtKB는 수작업 검토된 Swiss-Prot 항목과 자동 주석의 TrEMBL 항목으로 구성된다. 서열, 기능 주석, 분류 정보, 도메인 정보, 변이체, 하위 세포 위치, 150개 이상의 다른 데이터베이스 교차 참조를 포함한다. 2023년 업데이트에서는 새 웹사이트(https://www.uniprot.org/)가 공개되었고, 전체 항목의 85% 이상에 AlphaFold 구조를 연결했다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | https://www.uniprot.org/ — 무료 브라우저 검색 |
| REST API | UniProt REST API — 프로그래밍 방식 쿼리 |
| FTP | 전체 데이터셋 bulk 다운로드 |

#### 📤 제공 데이터 형식
- 단백질 서열 (FASTA)
- 기능 주석 (UniProtKB 형식)
- XML, TSV, JSON 형식 지원
- 150개 이상의 외부 데이터베이스 교차 참조

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 전체 서열 수 | **227M+** (2023년 기준) |
| AlphaFold 구조 연결 비율 | **85%+** |
| 교차 참조 데이터베이스 수 | **150개 이상** |

#### ⚠️ 한계점
- 수작업 검토 항목(Swiss-Prot)은 전체 대비 극히 일부로, 대부분의 항목은 자동 주석에 의존한다
- 서열 수의 급격한 증가로 수작업 검토의 포괄적 확장이 어렵다
- 신규 서열과 기능 사이의 정보 격차(annotation gap)가 지속적으로 존재한다

## 관련 정보
- **논문**: [UniProt: the Universal Protein Knowledgebase in 2023](https://doi.org/10.1093/nar/gkac1052)
