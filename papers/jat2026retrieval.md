---
title: "Retrieval-Augmented Question Answering over Scientific Literature for the Electron-Ion Collider"
bib_key: "jat2026retrieval"
year: 2026
domain: physics
type: Method
venue: arXiv 2026 (submitted to JINST)
paper_link: https://arxiv.org/abs/2604.02259
---
# Retrieval-Augmented Question Answering over Scientific Literature for the Electron-Ion Collider

> arXiv:2604.02259 | 2026 | Method | physics
> Ramaiah University of Applied Sciences (India) + College of William & Mary (USA)
> 후속 작업: AI4EIC의 RAGS4EIC (arXiv:2403.15729)을 로컬 LLaMA로 확장

## 한 줄 요약
EIC 관련 **arXiv 178편 논문**을 인덱싱한 자체(in-house) 벡터 데이터베이스를 구축하고, **LLaMA 3.2**(오픈소스, 로컬 배포)로 답변을 생성하는 RAG Q&A 시스템. **AI4EIC2023_DATASETS 51Q**로 평가, **Context Recall ~1.0, chunk 180·MMR 조합 최고 성능**. 독점 모델 의존성·클라우드 KB 전송 위험 제거.

## 제작 배경
**기존 접근법(RAGS4EIC, arXiv:2403.15729)의 한계**
- GPT-4 등 **독점 모델** 의존 + **클라우드 호스팅** 외부 KB → 미출판 EIC 데이터의 외부 전송 위험
- 비용·인터넷 의존도가 높아 자원 제약 환경에서 사용 불가
- proprietary tokenizer 의존 → 도메인 특화 fine-tuning 한계

**왜 이 시스템이 필요했는지**
- "EIC는 multi-continental, multi-institutional 프로젝트"(190+ institutes) → privacy-first가 필수
- 미출판 사전 공개 자료의 외부 노출 방지
- 비용 효율 솔루션으로 자원 제약 기관도 deploy 가능

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Knowledge Base 구축
  arXiv preprint repository에서 EIC 관련 178편 수집
  도메인: phenomenology, software, detector, accelerator physics
  메타데이터(arXiv ID, authors, year) 를 chunk에 concatenate
  → semantic chunk-source disambiguation

Step 2 — Chunking & Embedding
  LangChain RecursiveCharacterTextSplitter:
    chunk size 120 또는 180 chars, overlap = 20 chars
  Embedding: mxbai-embed-large (Mixedbread AI, 1024-dim, MTEB 강함)
  로컬 배포, no API dependency

Step 3 — Vector Database
  ChromaDB 선택 (FAISS·Pinecone·LanceDB 비교 후)
    - 로컬 deploy 가능
    - LangChain orchestration과 매끄럽게 통합

Step 4 — Retrieval
  Query → 1024-dim vector (동일 mxbai-embed-large)
  Top-20 chunks 검색
  Similarity:
    ┌─ Cosine similarity (각도 기반)
    └─ MMR (Maximum Marginal Relevance) — relevance × diversity

Step 5 — Generation
  Top-20 chunks → prompt template → LLaMA 3.2 or 3.3 (on-premise)
  guardrail: "answer only from provided context"
  citation tracing: LangSmith로 arXiv ID 추적

Step 6 — Evaluation (RAGAS framework, 6 metrics)
  Benchmark: AI4EIC2023_DATASETS (51Q × N claims)
  4-way 조합 평가: chunk{120,180} × sim{cosine,MMR}
```

## Input (입력)
- arXiv 178편 (chunked, embedded into ChromaDB)
- 사용자 자연어 질의
- Retrieval 전략: cosine sim 또는 MMR, top-20

## Output (출력)
- LLaMA 3.2가 생성한 답변 + LangSmith 추적 arXiv citation
- RAGAS 6-metric (Faithfulness, Answer Relevancy, Answer Correctness, Context Entity Recall, Context Recall, Context Precision)

## 예시 문항 (논문 4.1절 벤치마크 본문 인용)

### 📘 평가 데이터셋 구조 (본문 그대로)
> "The AI4EIC2023_DATASETS is the high quality benchmark dataset that contains the ground truth answers of a set of **51 questions** ... Each question in this dataset is mapped to a pre-defined number of sub-parts called 'claims', individual answer against each claim and a comprehensive answer of the entire question. The AI-generated QA-pairs are meticulously vetted by human experts to create a gold-truth."

### 📘 도메인 범위
> "These ground truth question-answers are generated using GPT-4.0 model, contextualized from the EIC-related publications from the arXiv pre-print repository across domains e.g., high energy phenomenology (hep.ph), nuclear experiments (nucl.ex) etc."

### 📘 Knowledge Base 구성 (Sec. 3)
> "The knowledge base of this RAG-inspired Q&A application is constructed with **178 EIC-related research articles** from the arXiv preprint repository. These scholarly articles span research domains across phenomenology, software development, detector design, accelerator physics etc."

### 📘 Chunking 철학 (저자 인용)
> "smaller chunks may increase precision but risk missing essential information, while larger chunks capture more content but may compromise relevance"

> 본 논문은 51개 Q 중 구체적 question 문장을 verbatim 인용하지 않습니다. AI4EIC2023_DATASETS GitHub 저장소에서 전체 51Q 확인 가능. (선행 논문 arXiv:2403.15729 참조)

## 주요 평가 결과 (Sec. 4.2)

**Retrieval Latency (Fig. 2, 중앙값)**

| 설정 | Latency |
|---|---|
| chunk 120 | 0.11 s |
| chunk 180 | 0.11–0.12 s |
| Cosine vs MMR | 비유의미 (차이 없음) |

**Inference Latency (Fig. 3) — LLM 선택이 결정적**

| LLM | Latency (median) | 비고 |
|---|---|---|
| **LLaMA 3.2** | **10–20 s** | 안정적, narrow IQR, outlier 50–60s |
| LLaMA 3.3 | 훨씬 큼 | 더 많은 compute, 극단 outlier 다수 |

> 저자 결론: **"LLaMA 3.3 model utilizes more compute and exhibits substantially higher and more varying latency ... we incorporated the LLaMA 3.2 model for further study."**

**RAGAS Metrics (Fig. 4·5, 4-way 조합 분포)**

| Metric | 관찰 |
|---|---|
| **Context Recall** | 클러스터링 ≈ 1.0 (특히 chunk 180에서 향상) |
| Faithfulness | chunk 180에서 high-skewed (좋음) |
| Context Precision | bimodal: [0.1, 0.3] vs [0.8+] |
| **Context Entity Recall** | low–moderate, **취약점** ← 도메인 entity 추출 한계 |
| Answer Relevancy / Correctness | chunk 180 + MMR 조합에서 가장 안정 |

> 저자 분석: **"the dense embedding models are optimized for general semantic not for any specific scientific terminology"** → 과학 named entity recall이 약점

## 한계점 (저자 명시)
- arXiv 178편으로 한정 — 기관 내부 문서·보고서·detector 명세는 미포함
- **Context Entity Recall 낮음**: 일반 임베딩 모델이 EIC 도메인 named entity(detector 코드, 입자 기호 등) 처리 부족
- LLaMA 3.3은 latency 폭증으로 사용 불가 → LLaMA 3.2로 회귀
- 평가가 GPT-4 생성 51Q에 한정, human-curated diverse 벤치마크 부재
- LangGraph 파이프라인 업그레이드 예정 (현재는 LangChain)

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2604.02259](https://arxiv.org/abs/2604.02259)
- **선행 연구 (RAGS4EIC)**: [https://arxiv.org/abs/2403.15729](https://arxiv.org/abs/2403.15729) (AI4EIC, GPT-3.5 + Pinecone)
- **평가 데이터셋**: AI4EIC2023_DATASETS (51Q × N claim, GitHub 공개)
- **저자 소속**: Ramaiah University (India) + College of William & Mary (USA)
- **차별점**: 로컬 LLaMA, ChromaDB, mxbai-embed-large → 완전 on-premise · cost-effective alternative
