---
title: "OpenFold: retraining AlphaFold2 yields new insights into its learning mechanisms and capacity for generalization"
bib_key: "ahdritz2024openfold"
year: 2024
domain: bio
type: dataset
venue: Nature Methods
paper_link: https://doi.org/10.1038/s41592-024-02272-z
---
# OpenFold: retraining AlphaFold2 yields new insights into its learning mechanisms and capacity for generalization

ahdritz2024openfold | 2024 | Nature Methods | dataset | [bio] | [paper](https://doi.org/10.1038/s41592-024-02272-z)

**DB**: OpenProteinSet (OpenFold 학습 데이터셋, MSA 기반)
**DB size**: 논문에서 정확한 MSA 건수 미명시 — AlphaFold2와 동등 수준의 학습 데이터
**DB Open/Private**: Open (GitHub: aqlaboratory/openfold)
**Modality**: Structured Table (다중 서열 정렬[MSA], 단백질 서열, 3차원 구조)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OpenFold (openfold.gurikilab.org)

> Nature Methods | 2024 | dataset | bio

#### 📌 한 줄 요약
AlphaFold2를 처음부터 재학습하여 AlphaFold2와 동등한 정확도를 달성한 빠르고 메모리 효율적인 오픈소스 구현체로, AlphaFold2의 학습 메커니즘과 일반화 능력에 대한 새로운 통찰(계층적 학습, 훈련 데이터 규모 강건성)을 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- AlphaFold2 구현은 새로운 모델 학습에 필요한 코드 및 데이터 미포함
- 단백질-리간드 복합체 예측 등 새로운 태스크로 확장 불가
- AlphaFold2 학습 과정과 일반화 능력 분석 도구 부재

**이 시스템이 필요한 이유**
- AlphaFold2를 새로운 태스크(단백질-리간드 복합체 등)에 적용하기 위한 학습 가능 구현체 필요
- 단백질 모델링 커뮤니티를 위한 오픈소스 재현 가능 플랫폼 필요

#### 🔨 시스템 구성
Columbia University 주도 다기관 협업. AlphaFold2의 빠르고 메모리 효율적인 학습 가능 구현체 OpenFold를 처음부터 학습하여 AlphaFold2와 동등 정확도 달성. 학습 세트 크기·다양성을 의도적으로 제한해도 놀라운 강건성 확인 (이차 구조 요소 대부분 제거해도 일반화 유지). 학습 중 중간 구조 분석으로 단백질 폴딩 계층적 학습 메커니즘 규명. 학습 데이터·코드·가중치 전체 공개.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| GitHub | https://github.com/aqlaboratory/openfold — 코드 및 모델 가중치 공개 |
| DOI | https://doi.org/10.1038/s41592-024-02272-z |

#### 📤 제공 데이터 형식
- 오픈소스 학습 코드 (PyTorch 기반)
- 사전 학습 모델 가중치
- OpenProteinSet: AlphaFold2 스타일 예측을 위한 MSA 데이터셋

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| AlphaFold2 대비 정확도 | **동등 수준 (처음부터 학습)** |
| 강건성 테스트 | **이차 구조 요소 대부분 제거 시에도 일반화 유지** |

#### ⚠️ 한계점
- 단백질 단량체 구조 예측 중심 (다량체·복합체 확장은 추후)
- 대규모 GPU 자원 필요 (처음부터 학습 시)
- 학습 데이터의 PDB 기반 편향 내재

## 관련 정보
- **논문**: [OpenFold: retraining AlphaFold2 yields new insights](https://doi.org/10.1038/s41592-024-02272-z)
