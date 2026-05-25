---
title: "DrugBank 6.0: the DrugBank Knowledgebase for 2024"
bib_key: "knox2024drugbank"
year: 2024
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad976
---
# DrugBank 6.0: the DrugBank Knowledgebase for 2024

knox2024drugbank | 2024 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkad976)

**DB**: DrugBank 6.0
**DB size**: FDA 승인 약물 4,563개, 임상시험 약물 6,231개, 약물-약물 상호작용 1,413,413개
**DB Open/Private**: Open (기본) / Subscription (확장 기능)
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: DrugBank web interface (go.drugbank.com)

> Nucleic Acids Research | 2024 | dataset | chem
#### 📌 한 줄 요약
DrugBank 6.0은 약물·약물 타겟·약동학 정보의 '골드 스탠다드' 지식 자원으로, 4,563개 FDA 승인 약물, 140만 개 이상의 약물-약물 상호작용 데이터를 포함한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 2018년 마지막 업데이트 이후 FDA 승인 약물 목록 및 상호작용 데이터의 대폭 확장 필요
- 약물 기전 및 대사 경로의 시각적 표현이 부족했음
**이 시스템이 필요한 이유**
- 연간 3천만 뷰 이상의 주요 약물 정보 자원으로서의 지속적 업데이트 요구
- AI 기반 약물 재목적화, 부작용 예측, 타겟 발견을 위한 통합 지식 그래프 필요

#### 🔨 시스템 구성
2006년 출시 이후 지속 확장되어 온 약물 정보 지식 베이스이다. 약물 화학 구조, 약동학, 약력학, 작용 기전, 대사 경로, 타겟 단백질, 약물-약물/약물-식품 상호작용 등을 통합한다. 색상 풍부한 주석이 있는 약물 기전·대사 경로 신규 추가.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | go.drugbank.com 검색 |
| 데이터 다운로드 | XML, CSV 형식 (등록 후 무료) |
| API | DrugBank API (상업 라이선스 옵션) |

#### 📤 제공 데이터 형식
- 약물 화학 구조 (SMILES, InChI, SDF)
- 약동학·약력학 데이터
- 단백질 타겟 서열
- 약물-약물 상호작용 목록
- 경로 정보 (시각화 포함)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| FDA 승인 약물 | 4,563 (2018 대비 72% 증가) |
| 임상시험 약물 | 6,231 (38% 증가) |
| 약물-약물 상호작용 | 1,413,413 (300% 증가) |
| 약물-식품 상호작용 | 2,475 (200% 증가) |
| 연간 조회 수 | 30M+ |

#### ⚠️ 한계점
- 고급 API 기능은 상업 라이선스 필요
- 약물 기전 일부는 전문가 큐레이션이 아닌 예측 기반
- 시판 철수 약물 정보 업데이트가 지연될 수 있음

## 관련 정보
- **논문**: [DrugBank 6.0: the DrugBank Knowledgebase for 2024](https://doi.org/10.1093/nar/gkad976)
