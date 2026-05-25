---
title: "An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics"
bib_key: "liu2018integrated"
year: 2018
domain: medical, bio
type: dataset
venue: Cell
paper_link: https://doi.org/10.1016/j.cell.2018.02.052
---
# An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics

liu2018integrated | 2018 | Cell | dataset | [medical, bio] | [paper](https://doi.org/10.1016/j.cell.2018.02.052)

**DB**: TCGA-CDR (The Cancer Genome Atlas Pan-Cancer Clinical Data Resource)
**DB size**: 11,000명 이상의 인간 종양, 33개 암종
**DB Open/Private**: Open (NCI GDC portal)
**Modality**: Genomic, Structured Table (임상·생존 데이터, 다중 플랫폼 분자 프로파일)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: TCGA-CDR / NCI GDC 포털

> Cell | 2018 | dataset | medical, bio

#### 📌 한 줄 요약
약 10년에 걸쳐 33개 암종 11,000명 이상 환자의 임상병리 주석 및 다중 플랫폼 분자 프로파일을 수집한 TCGA 팬캔서 임상 데이터 자원(TCGA-CDR)을 구축하고, 표준화된 생존 결과 분석 엔드포인트(OS, PFI, DFI, DSS)를 정의한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- TCGA 임상 데이터가 암종별로 분리되어 표준화 부재
- 생존 분석 엔드포인트 정의가 암종마다 불일치하여 비교 연구 어려움
- 다중 오믹스 데이터와 임상 결과를 통합한 표준화 자원 없음

**이 시스템이 필요한 이유**
- 게놈 특성과 임상 결과의 대규모 상관관계 분석을 위한 표준화 자원 필요
- 4가지 표준 생존 엔드포인트(OS/PFI/DFI/DSS) 기반 일관된 분석 필요

#### 🔨 시스템 구성
약 10년간 TCGA 프로그램이 수집한 33개 암종 11,000명 이상 환자의 임상병리 주석 및 다중 플랫폼 분자 프로파일 통합. TCGA-CDR은 4가지 주요 임상 결과 엔드포인트(전체 생존[OS], 무진행 생존 구간[PFI], 무병 생존 구간[DFI], 질환 특이 생존[DSS]) 포함. Cox 비례위험 회귀모형 및 Kaplan-Meier 생존 곡선 활용. 독립적 암 유전체 연구와의 검증.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| NCI GDC 포털 | https://portal.gdc.cancer.gov — 무료 공개 접근 |
| Cell 논문 보충 | https://doi.org/10.1016/j.cell.2018.02.052 (Table S1) |

#### 📤 제공 데이터 형식
- 표준화 임상 데이터 테이블 (CSV/Excel)
- 생존 결과 엔드포인트 (OS, PFI, DFI, DSS)
- 다중 플랫폼 분자 프로파일 (mRNA, miRNA, CNV, methylation, protein)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 환자/종양 수 | **11,000명 이상** |
| 암종 수 | **33개** |
| 데이터 수집 기간 | **약 10년** |
| 생존 엔드포인트 수 | **4개 (OS, PFI, DFI, DSS)** |

#### ⚠️ 한계점
- 일부 암종에서 특정 엔드포인트(DFI 등) 데이터 불완전
- 오랜 수집 기간으로 치료 프로토콜 이질성
- 특정 암종(소아암 등) 과소 대표

## 관련 정보
- **논문**: [An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics](https://doi.org/10.1016/j.cell.2018.02.052)
