---
title: "BindingDB in 2024: a FAIR knowledgebase of protein-small molecule binding data"
bib_key: "liu2025bindingdb"
year: 2025
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkae1075
---
# BindingDB in 2024: a FAIR knowledgebase of protein-small molecule binding data

liu2025bindingdb | 2025 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkae1075)

**DB**: BindingDB (2024 update)
**DB size**: 2.9M 결합 측정치, 1.3M 화합물, 수천 단백질 타겟
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: BindingDB web interface + FAIR data services

> Nucleic Acids Research | 2025 | dataset | chem
#### 📌 한 줄 요약
BindingDB의 2024년 업데이트로, FAIR 원칙 준수 강화, 2.9M 결합 측정치 및 1.3M 화합물을 포함하며, 분산 사이트에 복제된 장기 데이터 아카이브를 구축하였다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 장기적 데이터 보존 및 재현성 보장 체계가 부족했음
- 2016년 이후 급격히 성장한 US 특허 바이오활성 데이터 통합 필요
**이 시스템이 필요한 이유**
- AI 모델 훈련, 계산화학 방법 개발, 의약화학 지원을 위한 대규모 FAIR 데이터 필요
- 분산 복제 아카이브로 데이터 지속가능성 확보

#### 🔨 시스템 구성
2016년 이후 주로 US 특허 데이터 큐레이션에 집중하여 대규모 성장을 이룬다. Responsive web design으로 웹사이트 전면 개편. 강화된 검색·필터링, 새 다운로드 옵션, 웹서비스 추가. 분산 사이트 복제 장기 데이터 아카이브 구축. FAIR 데이터 공유 정책 준수.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | bindingdb.org 개선된 반응형 검색 UI |
| 웹 서비스 | 데이터 조회 API |
| 다운로드 | 다양한 포맷 다운로드 옵션 |
| 분산 아카이브 | 장기 보존용 복제 사이트 |

#### 📤 제공 데이터 형식
- 결합 친화도 (Ki, IC50, Kd, EC50)
- 화합물 구조 (SMILES, SDF)
- 단백질 타겟 정보

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 결합 측정치 | 2.9M |
| 화합물 | 1.3M |
| 단백질 타겟 | 수천 (thousands) |

#### ⚠️ 한계점
- 특허 데이터 추출 기반 성장이 주를 이루어 특정 화합물 유형 편향 가능성
- 관련 자원(ChEMBL, PubChem) 대비 데이터 중복 관리 필요

## 관련 정보
- **논문**: [BindingDB in 2024: a FAIR knowledgebase](https://doi.org/10.1093/nar/gkae1075)
