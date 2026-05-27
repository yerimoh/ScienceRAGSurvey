---
title: "MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations"
bib_key: DBLP:journals/corr/abs-2603-09800
year: 2026
domain: physics
type: Method
venue: arXiv (NeurIPS 2025 ML4PS Workshop)
paper_link: https://arxiv.org/abs/2603.09800
---
# MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations

> arXiv 2603.09800 | 2026 | Method | physics
> University of Wisconsin-Madison (CMS Collaboration) — NeurIPS 2025 ML4PS Workshop
> "MITRA" = Sanskrit "friend"

## 한 줄 요약
CERN CMS 협업의 방대한 내부 분석 노트·위키·가이드라인을 **on-premise**(NVIDIA Tesla T4, 15GB)에서 검색하는 RAG 시스템. DPR + cross-encoder 재랭킹 + 4-bit Mistral-7B를 결합하고 **2-tier DB**(abstracts → full-text)로 cross-analysis 혼동 방지. **의미론적 질의(Set 2)에서 BM25 대비 P@1 5.8배(0.13 → 0.75)** 향상.

## 제작 배경
**기존 방법의 한계**
- CMS 협업: 수천 명 멤버, 수 TB 분석 노트·내부 위키·가이드라인 → 수동 키워드 검색 비효율
- BM25 등 정확 키워드 매칭은 "transverse momentum" ↔ "pT cut" 같은 도메인 동의어 처리 불가
- 미공개 분석 데이터는 외부 LLM API(예: chATLAS의 GPT-4o-mini) 사용 시 프라이버시 우려
- 대규모 협업의 누적 API 비용은 자체 호스팅 대비 비합리적
- 단일 DB에서 다중 분석(Higgs vs Dark Matter)을 다루면 cross-analysis confusion 발생

**왜 MITRA가 필요했는지**
- "Higgs→di-muon 분석"의 "the most important background"와 "dark matter search"의 그것은 답이 다름 → context-aware DB 분리 필요
- 인스턴스별 키워드보다 **semantic equivalence**가 실사용에서 더 중요

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문서 수집 (Offline)
  Selenium 자동화 스크립트 → CMS 내부 DB 로그인 + PDF 다운로드
  OCR + layout parsing (Surya, Tesseract)
  단순 PyPDF/PDFPlumber 미사용 (복잡 레이아웃에서 손실)
  paragraph 단위 chunking

Step 2 — 임베딩 (DPR)
  facebook/dpr-question_encoder-multiset-base
  → 768-차원 벡터
  Chroma DB 저장

Step 3 — 2-Tier 벡터 DB 구조
  ┌─ Abstracts DB    : 모든 분석의 초록만
  └─ Full-Text DB    : 분석별 chunked 전문

  쿼리 처리:
    1) 첫 질문 → Abstracts DB에서 가장 가까운 분석 선택
    2) 사용자가 분석 선택 확인 (human-in-the-loop)
    3) 이후 모든 질문 → 해당 분석의 Full-Text DB만 검색
       → cross-analysis confusion 방지

Step 4 — Reranking (Cross-Encoder)
  cross-encoder/ms-marco-MiniLM-L-6-v2
  Top-k (tunable) → rerank → 정렬

Step 5 — Generation (On-Premise)
  Mistral-7B 4-bit quantized (Ollama, LangChain)
  명시적 prompt: "ground answers strictly within retrieved context"
  HW: NVIDIA Tesla T4 (15GB VRAM)
  UI: Streamlit

Step 6 — 평가 (전문가 설계 2 쿼리 세트)
  Set 1: 정확 키워드 phrasing
  Set 2: paraphrase / synonym (예: "transverse momentum requirement"
                                ↔ 문서의 "pT cut")
  Baselines: BM25 (Okapi)
  Metrics: P@1/3/5, R@1/3/5, MRR, NDCG@3/5
```

## Input (입력)
- 사용자 자연어 질문 (Streamlit UI)
- 첫 질의로 분석 선택 후 conversation 락온 (session-bound context)

## Output (출력)
- 검색된 passages + Mistral-7B가 생성한 cited 답변
- Out-of-context 질문에 대한 **거절 능력** (저자가 별도 정성 테스트)

## 예시 문항 (논문 본문 verbatim 인용)

### 📘 Cross-Analysis Confusion 예시 (Sec. 3 본문)
> **Q**: "What is the most important background?"
>
> 저자 분석: *"will have a different, and potentially conflicting, answer for a Higgs to di-muon analysis versus a search for dark matter"*
> → 2-tier DB로 분석 컨텍스트를 락온함으로써 해결

### 📘 Set 2 Semantic Query (Sec. 4 본문)
> **Q (사용자 phrasing)**: "transverse momentum requirement"
>
> **문서 내 표현**: `"pT cut"`
>
> **결과**: BM25 P@1 = 0.13, MITRA P@1 = **0.75** (5.8× 향상)

### 📘 Out-of-Context 거절 (Sec. 4 정성 테스트 본문)
> **세션 컨텍스트**: dark matter search 분석에 락온됨
> **Q**: "How many Higgs bosons were discovered in this search?"
> **MITRA 응답 (저자 인용)**: *"it did not hallucinate an answer. Instead, it correctly inferred from the retrieved passages that the document was unrelated to Higgs bosons and informed the user that the analysis in question is a dark matter search."*

## 주요 평가 결과 (Tables 1, 2)

**Table 1 — Precision / Recall @k**

| Query Set | System | P@1 | R@1 | P@3 | R@3 | P@5 | R@5 |
|---|---|---|---|---|---|---|---|
| Set 1 (exact KW) | BM25 | 1.00 | 0.85 | 0.40 | 0.90 | **0.32** | **1.00** |
| Set 1 (exact KW) | MITRA | 1.00 | 0.85 | 0.40 | 0.90 | 0.24 | 0.90 |
| **Set 2 (semantic)** | BM25 | 0.13 | 0.03 | 0.25 | 0.56 | 0.18 | 0.59 |
| **Set 2 (semantic)** | MITRA | **0.75** | **0.66** | **0.33** | **0.81** | 0.20 | **0.81** |

**Table 2 — MRR / NDCG**

| Query Set | System | MRR | NDCG@3 | NDCG@5 |
|---|---|---|---|---|
| Set 1 | BM25 | 1.00 | 1.00 | 0.98 |
| Set 1 | MITRA | 1.00 | 1.00 | 1.00 |
| **Set 2** | BM25 | 0.35 | 0.67 | 0.59 |
| **Set 2** | MITRA | **0.81** | **0.91** | **0.88** |

> **핵심 인사이트**: Set 1(정확 키워드)에서는 BM25 = MITRA. Set 2(현실적 paraphrase)에서 MITRA가 압도. "실사용자가 source document 정확 용어를 알고 검색하는 경우는 거의 없다"는 저자 주장.

## 한계점 (저자 명시)
- **프로토타입 단계** — CMS 협업 전체 배포 전, multiple document types로 확장 예정
- 평가 쿼리 집합이 소규모 (전문가 설계 2세트)
- **검색 품질만 측정**, LLM 답변의 faithfulness/relevancy LLM-as-judge 평가 미수행
- 쿼리 latency·throughput 정량 벤치마크는 future work
- 멀티턴 conversation, vLLM/llama.cpp 등 고성능 inference engine으로의 production 이전 예정
- 다른 물리 협업(ATLAS의 chATLAS, ALICE 등) 외부 일반화 미검증

## 관련 정보
- **논문**: [arXiv:2603.09800](https://arxiv.org/abs/2603.09800)
- **수락**: NeurIPS 2025 Machine Learning for Physical Sciences Workshop
- **저자 소속**: University of Wisconsin-Madison (CMS Collaboration)
- **그랜트**: U.S. DOE, Office of Science, DE-SC0017647
- **비교 시스템**: chATLAS (ATLAS, GPT-4o-mini 기반 API 의존) ↔ MITRA (on-premise 4-bit Mistral-7B)
