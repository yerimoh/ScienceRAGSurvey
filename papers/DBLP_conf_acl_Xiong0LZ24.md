---
title: "Benchmarking Retrieval-Augmented Generation for Medicine"
bib_key: "DBLP:conf/acl/Xiong0LZ24"
year: 2024
domain: medical, bio
type: Method
venue: ACL (Findings)
paper_link: https://aclanthology.org/2024.findings-acl.372
---

# MEDRAG: Benchmarking Retrieval-Augmented Generation for Medicine
> ACL Findings 2024 | Method | medical · bio

## 한 줄 요약
**MEDRAG**는 의학 QA를 위한 first-stage RAG 툴킷/파이프라인으로, 4개 도메인 corpus를 묶은 **MedCorp**에서 4종 retriever(BM25/Contriever/SPECTER/MedCPT)와 RRF fusion으로 관련 snippet을 검색하고, 이를 6종 LLM의 chain-of-thought 프롬프트에 주입해 답을 생성한다. corpus·retriever·LLM을 자유롭게 조합·교체할 수 있는 모듈형 시스템으로, 각 구성요소가 의학 RAG 성능에 미치는 영향을 체계적으로 비교할 수 있게 설계되었다.

## 시스템 구조 (MEDRAG Architecture)
MEDRAG는 **corpus → retriever → LLM** 세 층으로 이루어진 모듈형 파이프라인이며, 각 층의 구성요소를 plug-and-play로 교체할 수 있다.

### (1) Corpora — MedCorp
네 개의 이질적 의학 문서 집합을 통합한 코퍼스. 각 document를 검색 단위인 **snippet**으로 분할해 사용한다.

| Corpus | Documents | Snippets | 평균 길이 | 성격 |
|---|---|---|---|---|
| PubMed | 23.9M | 23.9M | 296 tokens | 생의학 논문 abstract |
| StatPearls | 9.3k | 301.2k | 119 tokens | 임상 의사결정 지원 자료 (NCBI Bookshelf) |
| Textbooks | 18 | 125.8k | 182 tokens | 의학 교과서 |
| Wikipedia | 6.5M | 29.9M | 162 tokens | 일반 백과사전 |
| **MedCorp (합계)** | **30.4M** | **54.2M** | **221 tokens** | 통합 코퍼스 |

- StatPearls는 본 논문이 biomedical NLP 커뮤니티에서 **처음 평가**한 corpus다.
- 서로 다른 도메인(논문/임상/교과서/일반)을 섞어 질문 유형별로 어떤 출처가 유효한지 비교 가능하게 했다.

### (2) Retrievers (4종)
서로 다른 매칭 전략을 가진 retriever를 동일 인터페이스로 제공한다.

- **BM25** — lexical retriever (bag-of-words + TF-IDF, Pyserini). 정확한 용어 일치에 강함.
- **Contriever** — dense retriever. Wikipedia·CCNet에서 contrastive learning으로 사전학습된 범용 semantic 임베딩.
- **SPECTER** — 과학 문헌 도메인 dense retriever. 유사 문서를 임베딩 공간에서 가깝게 인코딩.
- **MedCPT** — 생의학 특화 dense retriever. 255M PubMed 사용자 click 데이터로 학습, biomedical IR에서 SOTA.

### (3) RRF — Reciprocal Rank Fusion
여러 retriever의 순위를 결합해 공통적으로 상위에 오는 snippet을 우대하는 fusion 기법.
- **RRF-2**: BM25 + MedCPT (lexical/dense 한 쌍의 최적 조합)
- **RRF-4**: 4개 retriever 전부 결합 (가장 넓은 커버리지)
- 단일 retriever 대비 MedCorp에서 평균 성능을 **+1.4% ~ +10.7%** 향상.

### (4) LLMs (6종)
검색된 context를 받아 답을 생성하는 reader. 범용/생의학, 상용/오픈소스를 망라.

| Model | 크기 | 유형 | 도메인 |
|---|---|---|---|
| GPT-4 | proprietary | 상용 | 범용 |
| GPT-3.5 | proprietary | 상용 | 범용 |
| Mixtral | 8×7B | 오픈소스 | 범용 |
| Llama2 | 70B | 오픈소스 | 범용 |
| MEDITRON | 70B | 오픈소스 | 생의학 |
| PMC-LLaMA | 13B | 오픈소스 | 생의학 |

## 동작 파이프라인 (inference)
질문 한 건이 들어오면 다음 단계를 거친다.

1. **질문 입력** — 객관식 의학 질문을 query로 받는다.
2. **검색 (Question-Only Retrieval)** — 질문 텍스트만 retriever에 전달한다(아래 설정 참고).
3. **랭킹 / RRF fusion** — 선택된 retriever가 snippet을 순위화하고, 복수 retriever면 RRF로 순위를 병합한다.
4. **Context 구성** — 상위 **k개 snippet(default k=32)**을 프롬프트 앞에 prepend.
5. **생성** — LLM이 검색 context를 바탕으로 **chain-of-thought**로 추론.
6. **출력** — step-by-step 사고 과정과 선택 답안을 담은 JSON 산출.

### 핵심 평가 설정 두 가지
- **Zero-shot (ZSL)**: few-shot 예시 없이 동작. 예시를 구하기 어려운 실제 의료 상황을 반영.
- **Question-Only Retrieval (QOR)**: 검색 시 **정답 선택지(options)를 입력으로 주지 않고 질문만** 사용. 선택지를 retriever에 노출해 정답이 새어 나가던 기존 RAG 평가의 누수를 차단하는 설정으로, 의학 QA 평가에서 본 논문이 처음 제안·채택했다.

## 핵심 방법적 발견

| 발견 | 내용 (검증된 수치) |
|---|---|
| **MEDRAG 전반적 향상** | 6개 LLM에서 CoT 대비 최대 **+18%** 향상. GPT-3.5는 **+17.9%**로 최대, PMC-LLaMA는 약 **+0.52%**로 최소. |
| **좋은 retriever가 LLM 크기를 대체** | GPT-3.5 + MEDRAG(MedCorp + RRF-4) = **71.57%**, GPT-4 + CoT = **73.44%** (격차 1.87pp). GPT-3.5/Mixtral을 GPT-4-level로 끌어올림. |
| **RRF-4가 최적 fusion** | 전체 4 retriever 결합(RRF-4)이 MIRAGE 평균 최고(GPT-3.5 기준 71.57%). 단일 retriever 대비 **+1.4~10.7%**. BioASQ-Y/N처럼 개별 retriever가 약한 과제는 RRF-2(BM25+MedCPT)가 유리. |
| **log-linear scaling** | MMLU-Med·MedQA-US·MedMCQA에서 snippet 수 k≤32 구간 동안 성능이 대략 log-linear로 증가, 이후 noise 증가로 하락. |
| **"lost-in-the-middle"** | ground-truth snippet이 context의 앞·뒤에 있을 때 정확도 최고, **중간**에 위치하면 크게 하락하는 U자형 패턴. snippet 배치 순서가 성능에 영향. |

## 함께 제안한 벤치마크: MIRAGE
MEDRAG 평가를 위해 함께 공개한 의학 QA 벤치마크.
- **5개 데이터셋, 총 7,663개 객관식 문항**: MMLU-Med(1,089), MedQA-US(1,273), MedMCQA(4,183), PubMedQA(500), BioASQ-Y/N(618).
- 모두 zero-shot · question-only retrieval 설정에서 평가.
- (자세한 구축 과정은 본 요약에서 생략 — 본 요약은 MEDRAG 시스템 중심.)

## 한계점
저자들이 Limitations에서 명시한 내용.
1. 최신 RAG 변형이 아닌 **vanilla RAG** 구조에 집중.
2. corpus 커버리지가 불완전 (예: PubMed full-text, FAQ 등 미포함).
3. ground-truth snippet 평가가 **두 개 데이터셋에만** 가능.
4. **객관식(multiple-choice)** 포맷의 제약 — 생성된 rationale(근거 서술)에 대한 평가 부재.

## 관련 정보
- 논문: <https://aclanthology.org/2024.findings-acl.372> · arXiv: <https://arxiv.org/abs/2402.13178> (HTML: <https://arxiv.org/html/2402.13178>)
- MedRAG 툴킷: <https://github.com/Teddy-XiongGZ/MedRAG>
- MIRAGE 벤치마크: <https://github.com/Teddy-XiongGZ/MIRAGE>
