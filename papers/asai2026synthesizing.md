---
title: "Synthesizing Scientific Literature with Retrieval-Augmented Language Models"
bib_key: "asai2026synthesizing"
year: 2026
domain: bio, medical, physics
type: Method
venue: Nature
paper_link: https://doi.org/10.1038/s41586-025-10072-4
---

# OpenScholar: Synthesizing Scientific Literature with Retrieval-Augmented LMs
> Nature 2026 | Method | bio · medical · physics

## 한 줄 요약

OpenScholar는 4,500만 편의 공개 논문으로 구성된 대규모 datastore에서 관련 문헌을 검색하고, 학습된 retriever·reranker와 8B 규모의 전용 생성 LM을 결합하여, 과학적 질문에 대해 **인용이 부착된 장문 답변(synthesis)** 을 생성하는 retrieval-augmented LM 시스템이다. 핵심 특징은 생성 결과를 모델 스스로 평가해 추가 검색·보강을 반복하는 **iterative self-feedback generation** 루프이며, 이를 통해 비교적 작은 OpenScholar-8B가 GPT-4o를 인용 정확도·전문가 선호도에서 능가한다.

## 시스템 구조 (OpenScholar Architecture)

OpenScholar는 세 가지 핵심 구성요소로 이루어진다.

**1. OpenScholar-DataStore (OSDS) — 검색 대상 코퍼스**
- 출처: peS2o v3 (S2ORC / Semantic Scholar Open Research Corpus), 2024년 10월까지의 **4,500만 편(45 million papers)** 공개 논문.
- 논문을 250-word 단위 텍스트 블록으로 분할하여 총 **2억 3,400만 개의 passage(234 million passages)** 로 구성.

**2. Bi-encoder Retriever (θ_bi) — 1차 dense 검색**
- Contriever를 peS2o datastore 위에서 **unsupervised 방식으로 continual pre-training** 하여 과학 도메인에 적응시킨 dense retriever.
- 쿼리/passage를 밀집 벡터로 인코딩하고 nearest neighbor search로 **top 100 passages** 를 검색.

**3. Cross-encoder Reranker (θ_cross) — 정밀 재정렬**
- BGE-reranker를 합성 데이터로 fine-tuning한 **3억 4천만 파라미터(340M)** 모델로, (쿼리, passage) 쌍의 관련성을 1–5 척도로 직접 채점.
- bi-encoder가 뽑은 top 100을 재정렬해 최종 **top N(멀티 논문 과제에서 통상 ~10)** passage를 선정.
- **Meta-filtering**: (1) 논문당 최대 **3개 passage** 로 제한, (2) 정규화된 인용 수(citation count)를 관련성 점수에 반영.

**4. Generator LM (OpenScholar-8B)**
- 베이스 모델: **Llama 3.1 8B Instruct**.
- 검색된 passage를 컨텍스트로 받아 inline 인용 마커가 달린 답변과 자체 피드백을 생성하는 핵심 합성 엔진.
- OpenScholar는 생성 LM을 교체할 수 있는 일반 프레임워크로, 동일 파이프라인에 GPT-4o를 꽂은 **OpenScholar-GPT4o** 구성도 평가된다.

추론 시 검색 소스는 datastore에 한정되지 않고 세 가지를 병합한다: (1) 학습된 retriever로 peS2o datastore 검색, (2) 생성한 키워드로 **Semantic Scholar API** 의 abstract 검색, (3) **web search engine** 으로 얻은 공개 텍스트.

## 동작 파이프라인 (Inference: iterative self-feedback generation)

추론은 세 단계로 구성된다: **(1) 초기 응답·피드백 생성, (2) 피드백 기반 반복 보강(추가 검색 포함), (3) citation 검증.**

1. **초기 검색**: 세 소스(peS2o datastore, Semantic Scholar API abstract, web search)에서 passage를 모은 뒤, cross-encoder reranker가 meta-filtering과 함께 최종 top N(통상 10) passage로 좁힌다.
2. **초안 생성 (y₀)**: generator LM이 검색된 passage를 근거로 inline 인용 마커가 달린 초기 답변 y₀을 생성한다.
3. **자체 피드백 (self-feedback)**: 같은 LM이 y₀을 점검해 개선점을 기술하는 자연어 피드백 문장 f_t를 생성한다(효율을 위해 **최대 3개**).
4. **반복 보강 (iterative refinement)**: 각 피드백 항목에 대해 추가 검색이 필요하면 LM이 검색 쿼리를 생성하고, 새로 얻은 passage를 컨텍스트에 추가한 뒤 이전 답변·전체 passage를 반영하여 y₁, y₂, … 로 답변을 갱신한다(**최대 3회 피드백 반복**).
5. **Citation 검증 (citation verification)**: 마지막으로 인용이 필요한 모든 과학적 주장(citation-worthy statement)이 검색된 passage로 충분히 뒷받침되는지 확인하고, 근거가 없는 주장에는 LM이 **post-hoc로 인용을 삽입**하여 최종 답변을 완성한다.

추론 파라미터: temperature 0.7, 응답 최대 3,000 토큰 / 피드백 최대 1,000 토큰.

## 학습 (Training)

**Generator LM (OpenScholar-8B) distillation**
- 더 큰 teacher 모델 **Llama 3.1 70B** 로 합성 학습 데이터를 생성(약 10,000편 논문을 샘플링해 쿼리·응답 생성).
- 세 종류의 데이터 포맷을 합성: (a) **answer generation** (쿼리 → 응답), (b) **feedback generation** (초기 응답 → 피드백), (c) **feedback incorporation** (이전 응답 + 피드백 → 보강 응답). 최종/중간 출력을 모두 학습에 넣으면 작은 LM이 더 효과적인 피드백을 학습한다고 보고.
- 데이터 균형: 과학 도메인 50% + 일반 도메인 50%. 상위 100,000편 피인용 논문에서 fact verification·boolean QA 데이터를 추가 합성.
- **2단계 데이터 필터링**: (1) **Pairwise** — 최종 반복 y_T와 초안 y₀을 비교해 더 나은 쪽을 채택(over-editing·중복 증가로 y₀이 선호되는 경우가 약 20%), (2) **Rubric 기반** — 구성(organization)과 사실 정확성/인용 정확성 두 항목 모두 5점 만점에 4.5점 이상이어야 유효.
- 최종 **130k 학습 인스턴스** 를 torchtune으로 **2 epoch** 학습.

**Retriever (θ_bi)**: Contriever를 peS2o datastore에서 unsupervised로 continual pre-training.

**Reranker (θ_cross)**: peS2o abstract로부터 쿼리를 무작위 생성하고 top 10 passage를 검색한 뒤, **Llama 3 70B Instruct** 가 1–5 관련성 점수를 부여(4–5=positive, 1–2=negative, 3 폐기)하여 합성 학습 데이터를 만들고 BGE-reranker(340M)를 fine-tuning.

## 주요 결과 (시스템 성능)

검색이 없는 LLM은 인용을 **78–90%** 빈도로 날조(fabricate)했다. 도메인별로는 CS에서 GPT-4o 78.7% / Llama 3.1 8B 92.1%, biomedicine에서 GPT-4o 94.8% / Llama 3.1 8B 97.6%의 인용 환각률을 보였다.

**Citation F1 (멀티 논문 과제)**

| 모델 | ScholarQA-CS | ScholarQA-Bio | ScholarQA-Neuro |
|---|---|---|---|
| OpenScholar-8B | 47.9 | 50.8 | 56.8 |
| OpenScholar-GPT4o | 39.5 | 51.5 | 43.5 |
| GPT-4o (no retrieval) | 0.1 | 0.2 | 0.1 |

**Correctness (ScholarQA-CS, 멀티 논문)**

| 모델 | Correctness |
|---|---|
| OpenScholar-GPT4o | 57.7 |
| OpenScholar-8B | 51.1 |
| PaperQA2 | 45.6 |
| GPT-4o | 45.0 |

**전문가 선호도 (전문가 작성 답변 대비 win-rate)**

| 모델 | 전문가 답변 대비 선호율 |
|---|---|
| OpenScholar-GPT4o | 70% |
| OpenScholar-8B | 51% |
| GPT-4o (단독) | 32% |

또한 인간 평가에서 OpenScholar-GPT4o는 Overall Usefulness 80%로 GPT-4o(69.7%)를 상회했다. 즉, 작은 8B 모델이라도 OpenScholar 파이프라인을 통하면 인용 정확도와 전문가 선호도에서 GPT-4o를 능가한다.

## 함께 제안한 벤치마크: ScholarQABench (간단히)

ScholarQABench는 OpenScholar 평가를 위해 함께 제안된 벤치마크로, **2,967개 전문가 작성 질의** 와 그중 **208개의 박사급 전문가 장문 답변**(답변당 약 1시간 소요)을 포함하며, computer science·physics·biomedicine·neuroscience 4개 도메인을 다룬다. 평가 지표는 **Citation F1(Precision/Recall 포함)**, correctness(accuracy/ROUGE-L/rubric), 그리고 Coverage·Organization·Relevance·Overall Usefulness 등의 품질 차원이다. (벤치마크 구축 세부는 본 요약에서 생략.)

## 한계점

저자들이 명시한 한계는 크게 세 가지다.
- **ScholarQABench**: 박사급 주석의 높은 비용(자원 집약성), 전문가 도메인 장문 응답을 신뢰성 있게 평가하기 어려움.
- **OpenScholar 시스템**: 반복적 self-feedback 추론 파이프라인의 효율(비용) 문제, 합성 학습 데이터 품질에 따른 잠재적 한계.
- **인간 평가**: 비교적 소규모 전문가 패널, 편향 최소화 노력에도 남는 평가 편향 가능성.

## 관련 정보

- Nature DOI: https://doi.org/10.1038/s41586-025-10072-4
- arXiv: 2411.14199 (https://arxiv.org/abs/2411.14199, full text: https://arxiv.org/html/2411.14199)
- GitHub: https://github.com/AkariAsai/OpenScholar (코드·모델·datastore·벤치마크·공개 데모 제공)
