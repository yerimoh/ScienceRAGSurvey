---
title: "CG-RAG: Research Question Answering by Citation Graph Retrieval-Augmented LLMs"
bib_key: "DBLP:conf/sigir/HuLD0A0025"
year: 2025
domain: general
type: Method
venue: SIGIR
paper_link: https://doi.org/10.1145/3726302.3729920
---
# CG-RAG: Citation-Graph Retrieval-Augmented LLMs for Research QA
> SIGIR 2025 | Method | general (scientific research)

## 한 줄 요약
연구 논문을 청크(chunk) 단위로 분해해 인용 관계로 연결한 계층적 인용 그래프(hierarchical citation graph)를 구축하고, sparse(어휘)·dense(의미) 신호를 그래프 위에서 얽힘 융합(entangled fusion)하는 검색기 **LeSeGR**를 제안하여, 검색된 근거 청크의 문맥 이웃까지 LLM에 제공해 grounded 답변을 생성하는 연구 QA 프레임워크.

## 시스템 구조 (CG-RAG Architecture)
CG-RAG는 (1) 계층적 인용 그래프 구성, (2) LeSeGR 검색기, (3) 문맥 인지 답변 생성기의 세 부분으로 이루어진다.

**계층적 인용 그래프 (논문 청크 노드 + 인용 엣지).** 논문 본문은 related work / method / experiment 등 섹션마다 역할이 다른 이질적 정보를 담으므로, 논문 단위가 아니라 고정 길이 청크 단위로 분해한다(최대 청크 길이 8,192 토큰). 엣지는 두 종류다.
- **문서 내(intra-document) 엣지:** 순차적 인접(adjacency)과 명시적 상호참조(cross-reference).
- **문서 간(inter-document) 엣지:** 두 논문에 인용 관계가 있을 때, 한 청크에 대해 상대 논문에서 가장 관련 높은 Top-n 청크를 연결한다(관련도는 sparse·dense 점수의 합).

**LeSeGR (Lexical-Semantic Graph Retrieval) — sparse+dense의 그래프 상 통합.** 기존 hybrid 검색이 두 신호를 검색 후 단순 결합(post-retrieval)하는 것과 달리, LeSeGR는 그래프 위상 안에서 두 신호를 얽어 융합한다.
- **Sparse 신호:** 질의–청크 어휘 관련도(코사인/내적).
- **Dense 신호:** 청크 간 의미 유사도(MLP로 청크 임베딩 차이를 변환).
- **GNN 메시지 패싱:** 각 층에서 "질의-청크 sparse 점수 × 청크 간 dense 점수" 곱이 메시지 흐름을 게이팅(gating)하여 관련 정보만 이웃으로 전파한다. K층을 거친 최종 얽힘 표현으로 모든 청크를 점수화한다.
- **이론적 일반성:** 이웃이 없고 집계가 mean/sum이면 LeSeGR 점수가 "log(sparse) + log(dense)"로 환원되어, 기존 post-retrieval hybrid 융합이 LeSeGR의 특수 경우임을 보인다(그래프 DB로 hybrid 검색을 일반화).

## 동작 파이프라인 (inference)
1. 계층적 인용 그래프 구성.
2. sparse·dense 인코더로 질의·청크 인코딩, 질의-청크 어휘 관련도와 청크 간 의미 유사도 계산.
3. K층 메시지 패싱으로 두 신호를 얽혀 전파, 최종 표현으로 청크 점수화.
4. **서브그래프 검색:** Top-N 청크와 그 문맥 이웃을 합쳐 유도 부분그래프를 추출.
5. **grounded 생성:** 각 문맥 서브그래프를 LLM이 요약한 뒤, 질의와 함께 최종 답변을 생성.

구현: 생성 LLM은 GPT-4o(2024-05-13), sparse 신호 BGE-M3, dense 신호 MiniLM, 그래프 인코더는 2층·4헤드·은닉차원 1024의 Graph Transformer.

## 주요 결과
**데이터셋:** PubMedQA-1k(QA 1,000쌍, 논문 7,849편), PapersWithCodeQA(질문 924개, 논문 12,171편).

PapersWithCodeQA

| Method | Acc | F1 | MRR | Hit@1 |
|---|---|---|---|---|
| BM25 | 0.689 | 0.617 | 0.765 | 0.736 |
| ColBERT (best hybrid) | 0.769 | 0.661 | 0.827 | 0.778 |
| **LeSeGR (ours)** | **0.835** | **0.703** | **0.884** | **0.827** |

PubMedQA — QA / 검색(Hit@1)

| Method | Acc | F1 | Hit@1 |
|---|---|---|---|
| BM25 | 0.662 | 0.604 | 0.835 |
| ColBERT | 0.724 | 0.642 | 0.913 |
| **LeSeGR** | **0.778** | **0.685** | **0.961** |

효율(PapersWithCodeQA): LeSeGR는 GPU 메모리 1,921MB / 질의 지연 403.94ms로 ColBERT(12,674MB / 561.91ms)보다 메모리·지연 모두 우수. Ablation: 문맥 이웃 수 n=4가 최적, 그래프 인코더는 Graph Transformer > GCN > GAT.

## 한계점
논문에 명시적 Limitations 절은 없다. (요약자 주: 검증 도메인이 PubMed·PapersWithCode 두 과학 코퍼스에 한정, 생성에 GPT-4o API 의존, Top-n 등 그래프 구성 하이퍼파라미터 민감성은 ablation에서만 다룸.)

## 관련 정보
- arXiv: 2501.15067 (https://arxiv.org/abs/2501.15067)
- DOI: https://doi.org/10.1145/3726302.3729920 (SIGIR 2025, pp. 678–687)
- 저자: Yuntong Hu, Zhihan Lei, Zhongjie Dai, Allen Zhang, Abhinav Angirekula, Zhengwu Zhang, Liang Zhao
