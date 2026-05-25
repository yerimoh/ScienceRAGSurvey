---
title: "AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models"
bib_key: "DBLP:journals/nar/VaradiADNNYYSWL22"
year: 2022
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkab1061
---
# AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models

DBLP:journals/nar/VaradiADNNYYSWL22 | 2022 | Nucleic Acids Res. | dataset | [bio] | [paper](https://doi.org/10.1093/nar/gkab1061)

**DB**: AlphaFold DB (AlphaFold Protein Structure Database) — 초기 릴리스
**DB size**: 초기 릴리스: 21개 모델 생물체 프로테옴의 360,000개 이상 예측 구조; 향후 UniRef90 1억 개 이상 대표 서열로 확장 예정
**DB Open/Private**: Open (alphafold.ebi.ac.uk)
**Modality**: Structured Table (원자 좌표, 잔기별/쌍별 신뢰도)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: AlphaFold DB / EBI (alphafold.ebi.ac.uk)

> Nucleic Acids Res. | 2022 | dataset | bio

#### 📌 한 줄 요약
DeepMind의 AlphaFold v2.0으로 예측한 고정확도 단백질 구조를 개방 접근 방식으로 제공하는 대규모 데이터베이스로, 초기 릴리스에 21개 모델 생물체 프로테옴 360,000개 이상의 구조를 포함하며 단백질 서열 공간의 구조적 커버리지를 전례 없이 확장한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- PDB는 실험적으로 결정된 구조만 포함 — 전체 단백질 서열 공간의 극히 일부
- 수백만 개의 단백질 서열에 대한 구조 정보 부재
- 구조 예측은 있었으나 정확도가 실험 수준에 못 미침

**이 시스템이 필요한 이유**
- AlphaFold2의 혁신적 정확도를 활용한 대규모 구조 예측 데이터베이스 필요
- 구조 미결정 단백질의 기능 연구를 가속화할 개방형 자원 필요

#### 🔨 시스템 구성
EMBL-EBI와 DeepMind 공동 개발. AlphaFold v2.0으로 예측한 구조를 공개 접근 방식으로 제공. 초기 릴리스: 21개 모델 생물체 프로테옴의 360,000개 이상 예측 구조. 예측 원자 좌표(pLDDT), 잔기별 신뢰도(pLDDT), 쌍별 신뢰도(PAE; Predicted Aligned Error) 제공. 프로그래밍 접근(API) 및 인터랙티브 3D 시각화 지원. 향후 UniRef90의 1억 개 이상 대표 서열 전체 커버 예정.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| AlphaFold DB 포털 | https://alphafold.ebi.ac.uk — 무료 공개 접근 |
| API | REST API 프로그래밍 접근 |
| DOI | https://doi.org/10.1093/nar/gkab1061 |

#### 📤 제공 데이터 형식
- mmCIF/PDB 형식 (예측 원자 좌표)
- pLDDT 점수 (잔기별 신뢰도 0–100)
- PAE 행렬 (Predicted Aligned Error, 도메인 간 상대 위치 신뢰도)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 초기 릴리스 예측 구조 수 | **360,000개 이상** |
| 포함 모델 생물체 프로테옴 수 | **21개** |
| 향후 확장 목표 | **UniRef90 1억 개 이상 서열** |

#### ⚠️ 한계점
- 예측 구조로 실험 검증 미완
- 고신뢰도 구조는 pLDDT≥70 기준 (저신뢰도 영역 존재)
- 다량체 복합체·리간드 결합 구조 초기 릴리스에 미포함

## 관련 정보
- **논문**: [AlphaFold Protein Structure Database](https://doi.org/10.1093/nar/gkab1061)
