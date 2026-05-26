---
title: "AlzheimerRAG: Multimodal Retrieval-Augmented Generation for Clinical Use Cases"
bib_key: "DBLP:journals/make/LahiriH25"
year: 2025
domain: medical
type: Method
venue: Mach. Learn. Knowl. Extr.
paper_link: https://doi.org/10.3390/make7030089
---
# AlzheimerRAG: Cross-modal Attention Fusion for Alzheimer Clinical RAG

> Mach. Learn. Knowl. Extr. (MDPI) | 2025 | Method | medical
> Aritra Kumar Lahiri, Qinmin Vivian Hu — Toronto Metropolitan University (Canada)
> DBLP: `journals/make/LahiriH25` · arXiv: [2412.16701](https://arxiv.org/abs/2412.16701)

## 한 줄 요약
PubMed 논문의 텍스트와 추출된 시각 자료(그림·도표)를 **cross-modal attention fusion** 으로 통합하여 알츠하이머 임상 질의응답을 수행하는 멀티모달 RAG 시스템. QLoRA 기반 PEFT로 Llama-2-7b-pubmed를 미세조정하고, **BioASQ + PubMedQA** 벤치마크에서 텍스트 전용 RAG 대비 검색·합성 품질이 개선됨.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 소스 (멀티모달 PubMed)
  PubMed Alzheimer's 관련 논문에서 추출:
    • 텍스트 청크 (introduction, methods, results, discussion)
    • 시각 요소: figure 이미지, table 이미지
  시각 요소는 Vision Language Model로 자동 captioning

Step 2 — Cross-modal Embedding 생성
  ┌────────────┐                ┌──────────────┐
  │ Text chunks │ ─ tokenize ─►  │ Text encoder │ ─► text emb
  └────────────┘                └──────────────┘
  ┌────────────┐                ┌──────────────┐
  │ Figure imgs │ ─ caption  ─►  │ VLM encoder  │ ─► visual emb
  └────────────┘                └──────────────┘
                       │
                       ▼
          Cross-modal embedding fusion (어텐션)
                       │
                       ▼
                FAISS Vector Store + Object Store

Step 3 — PEFT 기반 미세조정
  Base model: Llama-2-7b-pubmed
  Training: QLoRA + PubMedQA dataset
  목적: 의학 도메인 특화 + 멀티모달 입력 처리

Step 4 — 추론 파이프라인 (Cross-modal Attention Fusion)
  사용자 쿼리 → similarity 검색 (text + visual 동시) →
    Cross-modal attention으로 retrieved context 정렬 →
    Fine-tuned LLM이 답변 생성

Step 5 — 평가
  Benchmarks: BioASQ, PubMedQA
  Comparison: text-only RAG baseline + non-RAG LLM
  Metric: retrieval accuracy, hallucination rate, human comparison
```

---

## 원문 직접 인용 (arXiv:2412.16701)

> "incorporates **cross-modal attention fusion techniques** to integrate textual and visual data processing by efficiently indexing and accessing vast amounts of biomedical literature"

> "Our experimental results, compared to benchmarks such as **BioASQ and PubMedQA**, yield improved performance in the retrieval and synthesis of domain-specific information"

> "These processed elements are then converted into embeddings through a **cross-modal embedding fusion method** and stored in an object store and a vector database"

> "fine-tuned the **'Llama-2-7b-pubmed'** model by training it with the PubMedQA dataset from HuggingFace. The fine-tuning used parameter-efficient fine-tuning (PEFT) techniques like **QLoRA**"

---

## 주요 평가 결과

| 항목 | 수치 |
|---|---|
| 도메인 | Alzheimer's disease (clinical use cases) |
| Backbone LLM | Llama-2-7b-pubmed (PEFT/QLoRA fine-tuned) |
| 평가 벤치마크 | BioASQ, PubMedQA |
| 모달리티 | Text + Image (PubMed articles + extracted figures) |
| 정확도 | Human-level non-inferior |
| 환각률 | Low (텍스트 전용 baseline 대비 감소) |

→ 텍스트 전용 RAG, 비-RAG LLM 모두 대비 일관되게 우위.

---

## Case Study (논문 §Discussion)
- 알츠하이머 진단 보조 시나리오
- 임상 의사결정 지원
- 약물 상호작용 + 부작용 정보 통합
- 환자 교육 자료 생성

---

## 한계점
- Alzheimer 단일 도메인 특화 → 일반화 범위 제한
- 대규모 이미지 인덱싱 계산 비용 증가
- 정량 성능 수치(F1, exact accuracy)가 논문에 명시적 표 형태로 제공되지 않음 (정성 비교 위주)
- Llama-2-7b 기반이라 최신 frontier LLM 대비 제한 존재
- 이미지 captioning 품질이 fusion 결과에 큰 영향을 미침

---

## 관련 정보
- **논문 (MDPI)**: [doi.org/10.3390/make7030089](https://doi.org/10.3390/make7030089)
- **arXiv preprint**: [arXiv:2412.16701](https://arxiv.org/abs/2412.16701)
- **DBLP**: [journals/make/LahiriH25](https://dblp.org/rec/journals/make/LahiriH25.html)
- **GitHub**: 공개 코드 미확인
