---
notion_id: 355f2dcd-4912-8187-976c-c5f6caf063a5
title: PaperQA - Retrieval-Augmented Generative Agent for Scientific Research
bib_key: DBLP:journals/corr/abs-2312-07559
year: 2023
domain: bio, medical
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2312.07559v2
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# PaperQA: Retrieval-Augmented Generative Agent for Scientific Research

> arXiv 2023 | Method + Benchmark | bio · medical
> Jakub Lála, Odhran O'Donoghue, Aleksandar Shtedritski, Sam Cox, Samuel G Rodriques, Andrew D White (Future House / Francis Crick Institute / University of Rochester)

## 한 줄 요약
과학 문헌을 동적으로 검색·추출·요약하여 인용 hallucination 0%로 전문가 수준의 답변을 생성하는 에이전트 기반 RAG 시스템 **PaperQA**와, 이를 평가하기 위한 **LitQA** 벤치마크(50개 MC 생의학 질문)를 함께 제안.

---

## LitQA 벤치마크 — 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 소스 논문 선정
  LLM 학습 데이터 컷오프(2021년 9월) 이후 출판된 생의학 논문만 선택
  → 모델 파라메트릭 메모리에 없는 지식만 질문화

Step 2 — 질문 생성 원칙
  "Select a paper and devise a question that:
   (1) refers to a novel finding in the paper body
   (2) is NOT present in the abstract"
  → 전문 생의학 연구자가 질문 작성

Step 3 — 오답 선택지(Distractor) 생성
  질문 작성자가 직접 생성 OR
  LLM으로 그럴듯한 오답 후보 생성 후 검토

Step 4 — 동료 검토
  공동저자들의 독립 교차 검토 후 확정

Step 5 — 최종 구성
  ┌──────────────────┬──────┐
  │ 선택지 수         │ 문항수 │
  ├──────────────────┼──────┤
  │ Yes/No (2지)     │    5 │
  │ 3지 선다          │    6 │
  │ 4지 선다          │   23 │
  │ 5지 선다          │   10 │
  │ 6지 선다          │    4 │
  │ 7지 선다          │    2 │
  ├──────────────────┼──────┤
  │ 합계              │   50 │
  └──────────────────┴──────┘
  도메인: 생의학 (biomedical)
  평가 메트릭: Accuracy (Correct/All), Precision (Correct-Sure/Answered-Sure)
```

---

## 실제 문항 예시 (논문 본문 직접 인용)

### 쉬운 문항 (Yes/No)
> **Q.** Has anyone performed a base editing screen against splice sites in CD33 before?
>
> **(A) Yes  (B) No**
>
> → 2021년 9월 이후 출판 논문 본문에서만 답을 찾을 수 있는 사실형 질문

### 중간 난이도 (3지 선다)
> **Q.** How diffuse are the laminar patterns of the axonal terminations of lower Layer 5/Layer 6 intratelencephalic neurons compared to Layer 2-4 intratelencephalic neurons in mouse cortex?
>
> **(A) More diffuse  (B) About the same  (C) Less diffuse**

### 어려운 문항 (4지 선다, 부정형)
> **Q.** Which of these glycoRNAs does NOT show an increase in M0 macrophages upon stimulation with LPS: U1, U35a, Y5 or U8?
>
> **(A) U8  (B) U1  (C) U35a  (D) Y5**

---

## PaperQA 시스템 아키텍처

```
[사용자 질문]
      │
      ▼
┌─────────────────────────────────────────┐
│  Agent LLM (GPT-4, τ=0.5)              │
│  "충분한 증거(5건+)가 모일 때까지 반복" │
└──────┬──────────────────────────────────┘
       │ 도구 선택·호출
  ┌────┴─────┬──────────────────┐
  ▼          ▼                  ▼
[Search]  [Gather Evidence]  [Answer Question]
  │          │                  │
  │  키워드로  │  MMR 벡터 검색    │  Ask LLM
  │  ArXiv/  │  → Summary LLM   │  (파라메트릭 지식)
  │  PubMed  │    (GPT-3.5)     │  + 수집된 증거 8건
  │  검색     │    관련도 1-10점  │  → Answer LLM (GPT-4)
  │          │    상위 필터링    │  → 인용 포함 최종 답변
  ▼          ▼                  ▼
4,000자 청크  20개 소스/라운드    "(Author2023)" 형식 인용
text-embedding-ada-002 벡터화
```

4개 독립 LLM 인스턴스 운영:
| 역할 | 모델 | 역할 설명 |
|---|---|---|
| Agent LLM | GPT-4 (τ=0.5) | 도구 선택, 반복 여부 결정 |
| Summary LLM | GPT-3.5-turbo (τ=0.2) | 청크 요약 + 관련도 채점 |
| Answer LLM | GPT-4 (τ=0.5) | 최종 인용 포함 답변 생성 |
| Ask LLM | GPT-4 (τ=0.5) | 파라메트릭 지식 추출 |

---

## 주요 평가 결과

### LitQA 정확도 비교
| 시스템 | 정답수 | 오답수 | 모름 | **Accuracy** |
|---|---|---|---|---|
| **PaperQA** | **34.8** | **4.8** | **10.5** | **69.5%** |
| 인간 전문가 | 33.4 | 4.6 | 12.0 | 66.8% |
| Claude-2 | 20.3 | 26.3 | — | 43.6% |
| GPT-4 | 16.7 | 16.3 | 17.0 | 33.4% |
| Perplexity | 9.0 | 10.0 | 31.0 | 18.0% |

→ PaperQA ≈ 인간 전문가 (Cramér's V: human-human 0.66±0.03 vs human-PaperQA 0.67±0.02)

### 인용 Hallucination 비율
| 모델 | 유효 인용 | **Hallucination** | 샘플 |
|---|---|---|---|
| **PaperQA** | **100%** | **0%** | 237 |
| GPT-4 | 60.78% | 39.22% | 51 |
| GPT-3.5 | 52.50% | 47.5% | 80 |
| Claude-2 | 39.71% | 60.29% | 68 |

### 표준 벤치마크 (Ablation 포함)
| 구성 | MedQA-USMLE | BioASQ | PubMedQA |
|---|---|---|---|
| **PaperQA** | **68.0%** | **89.0%** | **86.3%** |
| GPT-4 단독 | 67.0% | 84.0% | 57.9% |
| AutoGPT | 54.0% | 73.0% | 56.8% |

---

## 한계점
- 인용된 원본 논문의 정보 자체가 틀린 경우 대처 불가
- 최신 사실 업데이트에 따른 답변 유효기간 문제
- 질문당 평균 비용 $0.18 (2023년 기준)

---

## 관련 정보
- **논문**: [arXiv:2312.07559](https://arxiv.org/abs/2312.07559v2)
- **GitHub**: [Future-House/paper-qa](https://github.com/Future-House/paper-qa)
- **이 벤치마크(LitQA)를 사용한 논문**: PaperQA2 (arXiv 2409.13740)
