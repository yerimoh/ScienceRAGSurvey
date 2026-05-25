---
title: "AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences"
bib_key: "varadi2024alphafold"
year: 2024
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad1011
---
# AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences

varadi2024alphafold | 2024 | Nucleic Acids Res. | dataset | [bio] | [paper](https://doi.org/10.1093/nar/gkad1011)

**DB**: AlphaFold DB (AlphaFold Protein Structure Database) — 2024 업데이트
**DB size**: 2억 1,400만 개 이상 단백질 서열에 대한 예측 구조 (2021년 초기 30만 건 대비 500배 확장)
**DB Open/Private**: Open (alphafold.ebi.ac.uk)
**Modality**: Structured Table (원자 좌표, 잔기별/쌍별 신뢰도)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: AlphaFold DB / EBI (alphafold.ebi.ac.uk)

> Nucleic Acids Res. | 2024 | dataset | bio

#### 📌 한 줄 요약
2021년 초기 30만 건에서 2024년 2억 1,400만 개 이상으로 약 500배 확장된 AlphaFold DB의 최신 현황을 보고하며, 모델 생물체·글로벌 보건 프로테옴·Swiss-Prot 통합 및 Google Cloud 기반 고급 데이터 접근 방법을 소개한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 2022년 AlphaFold DB 초기 릴리스는 21개 모델 생물체에 한정
- 글로벌 보건 관련 병원체 프로테옴 및 Swiss-Prot 전체 커버리지 미달
- FTP 직접 다운로드 외 대규모 고급 쿼리 방법 미비

**이 시스템이 필요한 이유**
- UniProt 데이터베이스 전체 수준의 구조 커버리지 확장 필요
- 연구자의 다양한 데이터 접근 수요(클라우드, API, 뷰어)에 대응

#### 🔨 시스템 구성
EMBL-EBI, Google DeepMind, Seoul National University 공동 업데이트. 2021년 초기 300,000건에서 2억 1,400만 개 이상으로 약 500배 확장. PDB, UniProt, Ensembl, InterPro, MobiDB 등 주요 데이터 자원과 통합. 모델 생물체 프로테옴, 글로벌 보건 프로테옴, Swiss-Prot 통합, 큐레이션 단백질 데이터셋 포함. FTP 직접 파일 접근 + Google Cloud Public Datasets 고급 쿼리 + REST API 엔드포인트. PAE 뷰어, 3D 뷰어 커스터마이징, 검색 엔진 개선.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| AlphaFold DB 포털 | https://alphafold.ebi.ac.uk — 무료 공개 접근 |
| FTP | 직접 파일 다운로드 |
| Google Cloud | Google Cloud Public Datasets 고급 쿼리 |
| REST API | 프로그래밍 접근 엔드포인트 |

#### 📤 제공 데이터 형식
- mmCIF/PDB 형식 (예측 원자 좌표)
- pLDDT 점수 (잔기별 신뢰도)
- PAE 행렬 (Predicted Aligned Error)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 예측 구조 수 | **214,000,000개 이상** |
| 2021년 초기 대비 확장 배수 | **약 500배** |
| 통합 데이터 자원 | **PDB, UniProt, Ensembl, InterPro, MobiDB** |

#### ⚠️ 한계점
- 예측 구조로 실험 검증 미완 (특히 저 pLDDT 영역)
- 서열 기반 예측으로 결합 파트너·리간드 컨텍스트 미반영
- 단백질 동역학 및 다형성 표현 한계

## 관련 정보
- **논문**: [AlphaFold Protein Structure Database in 2024](https://doi.org/10.1093/nar/gkad1011)
