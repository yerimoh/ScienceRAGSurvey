---
notion_id: 355f2dcd-4912-8173-be88-d85ffb1b9127
title: GeoGPT-RAG Technical Report
bib_key: DBLP:journals/corr/abs-2509-09686
year: 2025
domain: earth
type: benchmark
venue: arXiv
paper_link: https://arxiv.org/abs/2509.09686v2
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# GeoGPT-RAG Technical Report

> arXiv | 2025 | Benchmark · Method | earth

## 한 줄 요약
지구과학 분야 전용 RAG 스택(GeoEmbedding, GeoReranker, RAFT)을 개발하고, GPT-4o + RAGAS 프레임워크로 1,000편 오픈 액세스 지구과학 논문에서 자동 생성한 938개 QA 벤치마크 **GeoRAG-QA**를 공개. Top-1 retrieval recall **0.908**, 전문가 평가 시 **85.7%** 정답 정확도 달성.

## 제작 배경
**기존 벤치마크의 한계**
- MTEB·BEIR 등 범용 IR 벤치마크는 지질학·석유 탐사·지구물리학 같이 고도로 특화된 어휘·구조를 가진 지구과학 자료에 부적합
- 지구과학 RAG 평가에는 검색기 성능을 객관적으로 비교할 수 있는 표준 벤치마크가 부재했음
- 고품질 라벨이 부족한 지구과학 도메인에서는 합성 데이터 생성·품질 통제 파이프라인 자체가 연구 과제

**왜 이 시스템·벤치마크가 필요했는지**
- GeoGPT는 38개국 1M+ 논문 규모의 지구과학 도메인을 지원해야 하므로, 도메인 적응 embedding/reranker가 핵심
- 비전문가·신입 연구자도 RAG로 지구과학 정보를 정확히 검색·합성할 수 있어야 함

## 어떻게 만들었나 (Construction Methodology)
**전체 구성**: GeoGPT 라이브러리 → RAGAS 기반 자동 QA 생성 → 수동 검수 → GeoRAG-QA 938 공개

```
Step 1 — 소스 코퍼스 구성
  GeoGPT 라이브러리(공공 라이브러리 1,500만 벡터,
  사용자 라이브러리 300만 벡터)에서
  오픈 액세스 지구과학 논문 1,000편 무작위 샘플링

Step 2 — 자동 QA 쌍 생성 (RAGAS Test Set Generation)
  ┌─ LLM: GPT-4o (질문·정답 생성)
  └─ Embedding: text-embedding-3-small (유사성 검증)

  4종 질문 유형으로 1,000개 생성
  ┌────────────────────────────────┬──────┐
  │ Single-document fact-based     │  250 │
  │ Single-document inference      │  250 │
  │ Multi-document                 │  188 │
  │ Conditional                    │  250 │
  └────────────────────────────────┴──────┘

Step 3 — 수동 품질 검증
  결함 있는 62개 제거
  "The answer is not present in the context" 항목 → GPT-4o로 재생성
  → 최종 938 QA 공개

Step 4 — 검색 시스템 학습
  ┌─ GeoEmbedding: Mistral-7B 기반 decoder-only encoder
  │  - 360k 학습 샘플 + Qwen 합성 지구과학 데이터
  │  - LoRA r=8, α=16, in-batch negatives, InfoNCE loss
  └─ GeoReranker: BGE-M3 기반 cross-encoder
     - 30k 지구과학 + 360k 일반 페어
     - LLaMA3로 0~3 품질 라벨링, label 0 제외
     - SimANS hard-negative mining

Step 5 — 평가 (GeoRAG-QA 938 / 70 전문가)
  Top-K Recall (자동 938) + Answer Recall (RAGAS)
  + Expert accuracy on 70 petroleum exploration Qs
```

> **주의**: GeoRAG-QA는 **open-ended free-text** 벤치마크입니다. 정답은 MC 선택지가 아니라 자유 문장이고, 평가 메트릭은 RAGAS의 Answer Recall과 Top-K Recall입니다.

## Input (입력)
| 항목 | 내용 |
|---|---|
| 소스 코퍼스 | GeoGPT 라이브러리에서 1,000편 무작위 샘플 |
| 청크 분할 | NLTK + BERT-NSP 기반 512-token semantic segmentation |
| 임베딩 | GeoEmbedding (Mistral-7B 인코더 변환, 4,096 token context) |
| 벡터 DB | Zilliz Cloud (Milvus) — 1,500만 공공 + 300만 사용자 벡터 |

**GeoRAG-QA 자체 구성**

| 질문 유형 | 문항 수 | 평균 검색 점수 | 검색 성공률 |
|---|---|---|---|
| Single-document, fact-based | 250 | 0.873 | 246/250 |
| Single-document inference   | 250 | 0.805 | 246/250 |
| Multi-document              | 188 | 0.874 | 188/188 |
| Conditional                 | 250 | 0.820 | 247/250 |
| **합계**                     | **938** | **0.842** | **927/938 (98.8%)** |

## Output (출력 / 정답 형식)
모델이 생성한 텍스트 형태의 정답. 평가 지표는 **Answer Recall (RAGAS)** + **Top-K Recall** + **전문가 정답 정확도(70Q)**.

## 예시 문항 (논문 본문 명시 내용)
> 본 논문은 구체적인 QA 인스턴스를 본문에 인용하지 않습니다. 대신 질문 생성에 사용된 **프롬프트 템플릿**과 **유형 카테고리**(Table 6)를 직접 인용합니다. 구체적 Q/A 예시는 HuggingFace 공개 데이터셋([GeoRAG-QA](https://huggingface.co/datasets/GeoGPT-Research-Project/GeoRAG-QA))에서 확인 가능.

### 📘 Query-Generation Prompt (본문 그대로)
> "Instruction: Given the next [document], create a [question] and [answer] pair that are grounded in the main point of the document, don't add any additional information that is not in the document and [use prompt by different query type of Table 6]. The [question] is by an information-seeking user and the [answer] is provided by a helping AI Agent."

### 📘 Query Type Categories (Table 6)
> "What / Which / Who·Whose / When / Where / How / Why / General question / Imperative question — The question should use [q_word]... to ask. Please ask in general form. Use imperative sentences to prompt the text."

### 📘 Answer-Rewriting Prompt
> "Your generated answer should contain 6 to 8 sentences. Your generated answer should have exactly the same meaning as the [Short Answer] and must perfectly address the [Query] without deviating. The content of your generated answer should fully utilize the content from the [References], and you must not fabricate any facts."

### 📘 전문가 평가 도메인
> "We further conducted manual evaluation on 70 domain-specific questions related to petroleum exploration. These questions were reviewed by subject matter experts to assess the factual accuracy of the generated answers."
> → 전문가 평가 정확도: **85.7%** (Table 4)

## 주요 평가 결과
**GeoGPT-RAG Top-K Recall on GeoRAG-QA (Table 2)**

| 시스템 | Top-1 | Top-3 | Top-5 | Top-8 | Top-32 | Top-64 |
|---|---|---|---|---|---|---|
| GeoGPT-RAG | **0.908** | 0.945 | 0.950 | 0.959 | 0.966 | 0.969 |

**End-to-End Answer Recall (Table 3)**

| Model | Answer Recall |
|---|---|
| GeoGPT-0630 (no RAG) | 0.529 |
| GeoGPT-0630 + RAG | **0.666** (+13.7pp) |

**RAFT (Retrieval-Augmented Fine-Tuning) (Table 5)**

| Model | In-Domain Recall | Out-Domain Recall |
|---|---|---|
| GeoGPT (no RAG-training) | 69.72 | 42.04 |
| GeoGPT + RAFT | **78.12** | **46.49** |
| 향상폭 | +12.05% | +10.59% |

**전문가 평가 (Petroleum 70Q, Table 4)**: **0.857** accuracy

## 한계점
- GeoRAG-QA는 GPT-4o가 역산 생성한 합성 QA — 실제 도메인 전문가가 즉흥적으로 물어보는 자연 분포와 차이
- 오픈 액세스 1,000편만 샘플링 → 접근 제한 학술지 미커버
- Conditional QA 250개의 구체 정의·생성 프로토콜 불명확
- 검색 latency·운영 비용에 대한 직접 벤치마크는 미수록

## 관련 정보
- **논문**: [arXiv:2509.09686v2](https://arxiv.org/abs/2509.09686v2)
- **GeoRAG-QA 데이터셋**: [HuggingFace](https://huggingface.co/datasets/GeoGPT-Research-Project/GeoRAG-QA)
- **GeoEmbedding 모델**: [HuggingFace](https://huggingface.co/GeoGPT-Research-Project/GeoEmbedding)
- **이 벤치마크를 사용한 RAG 시스템**: GeoGPT-RAG 본 논문
