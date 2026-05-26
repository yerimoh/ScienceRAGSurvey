---
notion_id: 355f2dcd-4912-8125-a0b1-edf649b6be58
title: Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation
bib_key: DBLP:journals/corr/abs-2603-07233
year: 2026
domain: bio
type: Method
venue: Gen2 @ ICLR
paper_link: https://arxiv.org/abs/2603.07233
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation

> Gen2 @ ICLR | 2026 | Method | bio

## 한 줄 요약
RAG를 유전자 perturbation 세포 반응 예측에 최초로 적용한 프레임워크 PT-RAG. Naive RAG가 오히려 성능을 저하시킨다는 핵심 발견과 함께, GenePT 임베딩 + Gumbel-Softmax 기반 2단계 미분 가능 검색으로 STATE 대비 분포 유사도 지표 개선을 달성.

<details>
<summary>사전 지식</summary>
**Perturbation**은 "교란" 또는 "섭동"이라는 뜻으로, 맥락에 따라 쓰임이 다릅니다.
**일반적인 의미**로는 어떤 시스템을 원래 상태에서 *의도적으로 건드려서 변화를 관찰하는 것*입니다.
---
**생물학에서 (방금 논문의 맥락)**
유전자를 꺼버리거나(knockdown/knockout) 과발현시키는 등 세포에 가하는 *유전적 조작*을 말합니다.
예를 들어, "BRCA1 유전자를 perturbation한다" → BRCA1을 억제해서 세포가 어떻게 반응하는지(유전자 발현이 어떻게 바뀌는지) 관찰하는 것.
방금 논문에서는 **Perturb-seq**이라는 기술을 사용하는데, 이건 CRISPR로 수천 개 유전자를 하나씩 꺼보면서 각 세포의 전체 유전자 발현 변화를 한꺼번에 측정하는 방법입니다. 그 결과 데이터를 보고 "이 유전자를 건드렸더니 저 유전자들이 이렇게 반응했네"를 학습하는 게 PT-RAG의 목적이고요.
---
**다른 분야에서는**
- 물리학: 시스템에 작은 외부 자극을 주는 것 (섭동 이론)
- 머신러닝: 입력 데이터를 약간 변형해서 모델 반응을 보는 것 (adversarial perturbation 등)
한마디로 **"건드려서 어떻게 반응하는지 본다"** 는 개념입니다.
</details>

## 연구 배경 및 동기
### 기존 방법의 한계점
- GEARS, scGPT, STATE 등 기존 perturbation 예측 모델들은 cell state와 perturbation identity만을 기반으로 발현 프로파일을 생성하며, **관련 perturbation 간 지식을 활용하지 않음**
- 언어 도메인의 RAG를 단순 적용(vanilla RAG)할 경우, perturbation 도메인에서는 **유사성 기준이 사전 정의되지 않아** 오히려 성능 저하가 발생함
- perturbation 검색에서 관련성은 **세포 유형(cell type)에 크게 의존**하나, 기존 방법은 이를 고려하지 않음

### 이 연구가 필요한 이유
- 유전자 perturbation 효과는 같은 유전자라도 세포 유형에 따라 크게 달라지므로, **cell-type-aware 맥락 검색**이 필수적
- 이미 관측된 수천 개의 perturbation 실험 데이터를 RAG 방식으로 활용하면 미지 perturbation 예측 일반화 성능 향상 가능
- **미분 가능한 검색 메커니즘**을 통해 생성 목표와 검색 목표를 end-to-end로 공동 최적화

## 시스템 아키텍처

```
입력: (perturbation gene g, cell state c)
       │
       ▼
[Stage 1: GenePT 임베딩 기반 후보 검색]
  - 입력 perturbation을 GenePT 임베딩으로 인코딩
  - 학습 DB 내 K개 유사 perturbation 후보 검색 (코사인 유사도)
       │
       ▼
[Stage 2: Gumbel-Softmax 기반 적응적 선택]
  - cell state + perturbation embedding 조건부
  - Straight-Through Gumbel-Softmax로 이산 선택 미분 가능화
  - 최적 subset 선택 (sparsity loss로 mode collapse 방지)
       │
       ▼
[Context Aggregation]
  - 선택된 perturbation의 관측 발현 프로파일 집계
       │
       ▼
[Generator (STATE 기반)]
  - Context + 입력 조건으로 perturbation 후 발현 분포 예측
       │
       ▼
출력: 예측 gene expression profile (2,000 HVGs)
```

## 핵심 모듈 상세 설명
### 1단계: GenePT 임베딩 후보 검색
- **GenePT**: ChatGPT 기반 유전자 기능 설명 텍스트로 학습된 유전자 임베딩 모델
- 입력 perturbation gene을 GenePT 공간에서 인코딩 후 학습 데이터 내 상위 K개 후보 perturbation 검색
- 의미 유사도(functional similarity) 기반 — 학습 파라미터 없음

### 2단계: Gumbel-Softmax 적응적 선택
- **Straight-Through Gumbel-Softmax estimator** (Jang et al. 2017) 적용
- 입력: [cell state embedding; perturbation embedding]
- 출력: K개 후보 중 이산적으로 최적 subset 선택
- **Sparsity loss** 추가: 모든 후보 선택하는 mode collapse 방지, 진짜 관련 context만 선택 유도
- 세포 유형별 선택된 perturbation 중복률 **19%** → cell-type-aware 특성 정량 검증

### Context Aggregation
- 선택된 perturbation들의 관측 scRNA-seq 발현 벡터를 집계
- Generator(STATE)의 입력 context로 제공

### Generator (STATE backbone)
- Arc Institute의 STATE: Transformer 기반 다중 세포 유형 perturbation 예측 모델
- Energy distance(MMD 기반 분포 손실)로 학습
- PT-RAG context가 추가된 상태에서 end-to-end 공동 최적화

## 실험 및 평가
### 평가 데이터셋
| 항목 | 내용 |
|---|---|
| **데이터셋** | Replogle-Nadig Perturb-seq (Replogle et al. 2022; Nadig et al. 2024) |
| **세포주** | K562, RPE1, Jurkat, HepG2 (4개 인간 세포주) |
| **총 세포 수** | ~0.6M |
| **perturbation 수** | 2,023개 (테스트: 1,635개) |
| **특징 수** | 2,000 HVGs |
| **실험 방법** | CRISPRi (CRISPR interference) 단일 유전자 knockdown |

### 주요 결과
| 방법 | W2 (↓) | 비고 |
|---|---|---|
| **PT-RAG (제안)** | STATE 대비 개선 | 최우수 |
| STATE (baseline) | 646.1 | 기존 SOTA |
| Vanilla RAG | **1189.5** | 오히려 최악 |
| GEARS | — | baseline |

- **핵심 발견**: Vanilla RAG는 STATE baseline 대비 W2에서 약 2배 성능 저하 → 도메인 특화 미분 가능 검색의 절대적 필요성 실증
- PT-RAG는 W1, W2 distributional similarity metrics에서 STATE 대비 유의미한 개선 달성

## 핵심 기여
1. **최초의 생물학적 perturbation 예측 RAG 프레임워크**: 언어 RAG를 단일 세포 생물학으로 확장
2. **Naive RAG의 실패 자체가 핵심 발견**: perturbation 도메인에서는 사전 정의된 유사도 기준이 없어 naive retrieval이 성능을 심각하게 저하시킴을 정량적으로 실증
3. **Cell-type-aware 미분 가능 검색**: Gumbel-Softmax 기반 2단계 파이프라인으로 세포 유형별로 다른 최적 context를 학습 가능하게 설계
4. **분포 수준 성능 향상**: W1, W2 등 distributional metrics에서 기존 SOTA 개선

## 한계점
- **단일 데이터셋 평가**: Replogle-Nadig 데이터셋 하나에만 실험 — 다른 Perturb-seq 데이터셋으로의 일반화 불확실
- **단일 유전자 perturbation만 지원**: 조합(combination) perturbation 미검증
- **End-to-end 학습 비용**: 미분 가능 검색의 공동 최적화는 상당한 컴퓨팅 자원 필요
- **텍스트 기반 GenePT 의존성**: 기능 설명이 없는 유전자는 Stage 1 검색 품질 저하 가능

## 관련 연구 및 관련 정보
- **논문 링크**: [https://arxiv.org/abs/2603.07233](https://arxiv.org/abs/2603.07233)
- **코드**: [https://github.com/difra100/PT-RAG_ICLR](https://github.com/difra100/PT-RAG_ICLR)
- **Venue**: ICLR 2026 Workshop — Generative AI in Genomics (Gen2)
- **베이스라인 모델**: STATE (Adduri et al. 2025), GEARS (Roohani et al. 2024), scGPT
- **사용 데이터셋**: Replogle et al. 2022 (Cell), Nadig et al. 2024
