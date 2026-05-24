---
notion_id: 355f2dcd-4912-8153-8151-d3b4e52f86da
title: Rationale-Guided Retrieval Augmented Generation for Medical Question Answering
bib_key: DBLP:conf/naacl/SohnPYPHSKK25
year: 2025
domain: medical
type: Method
venue: NAACL
paper_link: https://aclanthology.org/2025.naacl-long.635/
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Rationale-Guided Retrieval Augmented Generation for Medical Question Answering

> NAACL | 2025 | Method | medical

## 한 줄 요약
LLM이 생성한 근거(rationale)를 쿼리로 활용하고, perplexity 차이 기반 소형 필터링 모델을 훈련하며, 4개 바이오메디컬 코퍼스에서 균등 검색하는 세 가지 혁신으로 의료 QA RAG의 신뢰성을 높인 RAG² 프레임워크.

## 연구 배경 및 동기
**기존 방법의 한계점**
- LLM은 관련 없거나 유해한 컨텍스트에 취약: 의학 텍스트의 전문 용어가 비관련 문서 검색 위험 증가
- 의료 쿼리의 검색 타겟팅 어려움: 광범위한 환자 정보를 포함하면 검색 시스템 혼란, 너무 짧으면 암묵적 의료 지식 의존
- 검색기 편향(retriever bias): MedCPT 같은 대형 코퍼스 훈련 검색기는 PubMed 편향, 소규모 임상 가이드라인·교과서 과소 표현

**이 연구가 필요한 이유**
- Self-BioRAG 등 기존 방법은 LLM 파인튜닝 또는 반복적 RAG 실행 필요 → 높은 계산 비용
- Adaptive-RAG는 정답/오답만 라벨로 사용해 문서 유용성의 세밀한 영향 파악 못함
- 단일 단계 검색 + 소형 필터링 모델만으로 효율적 성능 개선 필요

## 시스템 아키텍처
```
[초기 쿼리 x]
    ↓
[Rationale-Based Query Formulation]
  - LLM이 Chain-of-Thought로 rationale 생성
  - rationale만을 검색 쿼리로 사용 (초기 쿼리 미포함)
    ↓
[Balanced Retrieval]
  - 4개 코퍼스 균등 검색: PubMed, PMC, Textbooks, Clinical Guidelines
  - MedCPT reranker로 초기 쿼리 기준 재순위
    ↓
[Rationale-Guided Filtering]
  - Flan-T5-large 필터링 모델이 유용 스니펫 선별
  - perplexity 차이(ΔPPL)로 라벨링된 데이터로 훈련
    ↓
[LLM Generator]
  - 유용 스니펫만 컨텍스트로 최종 답변 생성
```

## 핵심 모듈 상세 설명
**1. Rationale-Guided Filtering (핵심 혁신)**
- 훈련 데이터 생성: LLM이 RAG 없을 때 vs. 있을 때 rationale의 perplexity 차이 ΔPPL = PPL(x) - PPL(x, d) 계산
- 상위 25% ΔPPL 기준으로 문서를 Helpful/Not Helpful 라벨링
- Flan-T5-large(770M)를 필터링 모델로 훈련 (RTX 3090 24G 단일 GPU)
- 추론 시 필터링 모델이 각 스니펫의 유용성 판단 → 정보성 스니펫만 LLM에 전달

**2. Rationale-Based Query Formulation**
- CoT 프롬프트로 LLM이 초기 쿼리에 대한 rationale 생성
- rationale만 검색 쿼리로 사용 (초기 쿼리 + rationale 합치면 검색기 최대 길이 초과)
- 단계적 문제 풀이로 핵심 구성요소 식별 + 짧은 쿼리의 경우 자동 확장

**3. Balanced Retrieval**
- 4개 바이오메디컬 코퍼스에서 균등 검색: PubMed, PMC (대형), Textbooks, Clinical Guidelines (소형)
- MedCPT cross-encoder reranker로 원래 쿼리 기준 재순위
- retriever bias 완화: 훈련 데이터와 무관하게 모든 코퍼스 동등 표현

**데이터베이스 구성**
| 코퍼스 | 유형 | 특징 |
|---|---|---|
| PubMed | 대형 | 생물의학 논문, MedCPT 훈련 소스 |
| PMC | 대형 | 오픈 액세스 생물의학 논문 |
| Medical Textbooks | 소형·전문 | 표준 의학 교과서 |
| Clinical Guidelines | 소형·전문 | 최신 임상 가이드라인 |

## 실험 및 평가
**평가 데이터셋**
| 데이터셋 | 출처 | 문항 수 |
|---|---|---|
| MedQA | USMLE 시험 문제 (Jin et al., 2021) | 1,273 (test) |
| MedMCQA | AIIMS/NEET PG 시험 (Pal et al., 2022) | 6,150 (test) |
| MMLU-Med | MMLU 6개 의학 과목 (Hendrycks et al., 2021) | 1,089 (test) |

**주요 결과 (정확도)**
| 모델 + 방법 | MedQA | MedMCQA | MMLU-Med | 평균 |
|---|---|---|---|---|
| Llama-3-8B (baseline) | 57.7 | 53.5 | 69.5 | 60.2 |
|   • MedRAG | 56.4 | 56.6 | 69.2 | 60.7 |
|   • **RAG² (Ours)** | **64.6** | **59.4** | **74.8** | **66.3** |
| Meerkat-7B (baseline) | 71.2 | 60.8 | 73.8 | 68.6 |
|   • **RAG² (Ours)** | **75.6** | **63.0** | **78.7** | **72.4** |
| GPT-4o (baseline) | 88.5 | 76.7 | 92.8 | 86.0 |
|   • **RAG² (Ours)** | **91.1** | **77.2** | **92.5** | **86.9** |

- Llama-3-8B에서 평균 +6.1%, MedRAG 대비 +5.6% 개선
- Meerkat-7B에서 평균 +3.8% 개선
- GPT-4o에서 평균 +0.9% 개선

## 핵심 기여
- RAG²: 단일 단계 검색 + 소형 필터링 모델만으로 의료 RAG 효율·성능 동시 향상
- Perplexity 차이 기반 자동 라벨링 → 의료 도메인 희소 어노테이션 문제 해결
- 균등 검색 전략으로 retriever bias 완화
- 3개 의료 QA 벤치마크에서 SOTA 달성 (기존 최고 대비 최대 +5.6%)

## 한계점
- Closed-book QA 설정만 평가 (오라클 문서 없는 환경)
- MMLU-Med 훈련 데이터 없어 MedMCQA 훈련 데이터로 필터링 모델 훈련
- 일부 설정에서 GPT-4o 단독 대비 소폭 성능 저하 가능성
- 필터링 모델이 베이스 LLM 의존적 (모델 변경 시 재훈련 필요)

## 관련 연구 및 관련 정보
- **ACL Anthology**: [https://aclanthology.org/2025.naacl-long.635/](https://aclanthology.org/2025.naacl-long.635/)
- **GitHub**: [https://github.com/dmis-lab/RAG2](https://github.com/dmis-lab/RAG2)
- **arXiv**: [https://arxiv.org/abs/2411.00300](https://arxiv.org/abs/2411.00300)
- **비교 기준 방법**: MedRAG, MedCPT, Adaptive-RAG, InstructRAG, query2doc
- **소속**: Korea University (DMIS Lab), Kyung Hee University, AIGEN Sciences
