---
title: "The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods"
bib_key: "zdrazil2024chembl"
year: 2024
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad1004
---
# The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods

zdrazil2024chembl | 2024 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkad1004)

**DB**: ChEMBL (2023 release)
**DB size**: 기탁 데이터가 문헌 추출 데이터 양 초과 (구체적 수치 abstract 미기재)
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ChEMBL web interface + REST API

> Nucleic Acids Research | 2024 | dataset | chem
#### 📌 한 줄 요약
ChEMBL의 2023년 상태를 기술한 논문으로, 기탁 데이터가 최초로 문헌 추출 데이터를 초과하고, 항-SARS-CoV-2 화합물 스크리닝 데이터, 특허 바이오활성 데이터, Chemical Probe 플래그 등이 추가되었다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- ChEMBL 2009년 출시 이후 문헌 추출 데이터가 주를 이루었으나, 비문헌 기탁 데이터 필요성 증가
- COVID-19 대응을 위한 항바이러스 화합물 데이터 신속 통합이 요구됨
**이 시스템이 필요한 이유**
- EUbOPEN 컨소시엄과 협력하여 Chemical Probe 데이터 정기 기탁 체계 수립
- Natural Product 특성 점수, Chemical Probe 플래그 등 새로운 주석 기능 추가

#### 🔨 시스템 구성
EUbOPEN Chemical Probe 데이터 정기 기탁. Release 27에서 항-SARS-CoV-2 활성 스크리닝 데이터 통합. 특허 바이오활성 데이터 추가. Natural Product 유사성 점수 및 Chemical Probe 플래그 신설. 약 270,000개 바이오활성 측정치에 action type 초기 주석 작업 수행.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | https://www.ebi.ac.uk/chembl/ |
| REST API | 구조·타겟·바이오활성 조회 |
| 데이터 다운로드 | SQL, SDF, FASTA 전체 덤프 |

#### 📤 제공 데이터 형식
- 화합물 구조 (SMILES, InChI)
- 바이오활성 측정치
- Chemical Probe / Natural Product 플래그
- Action type 주석

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| Action type 주석 바이오활성 | ~270,000개 |
| 데이터 구성 | 기탁 > 문헌 추출 (최초) |

#### ⚠️ 한계점
- 기탁 데이터 비중 증가로 품질 일관성 관리 복잡성 상승
- 상업적 특허 바이오활성 데이터는 완전한 재배포에 제한이 있을 수 있음

## 관련 정보
- **논문**: [The ChEMBL Database in 2023](https://doi.org/10.1093/nar/gkad1004)
