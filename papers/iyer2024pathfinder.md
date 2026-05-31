---
title: "pathfinder: A Semantic Framework for Literature Review and Knowledge Discovery in Astronomy"
bib_key: "iyer2024pathfinder"
year: 2024
domain: astronomy
type: Method
venue: ApJS
paper_link: https://doi.org/10.3847/1538-4365/ad7c43
---
# Pathfinder: Semantic RAG Framework for Astronomy Literature
> ApJS 275:38, 2024 | Method | astronomy

## 한 줄 요약
Pathfinder는 약 35만 편의 천문학 논문(ADS+arXiv astro-ph) 초록을 임베딩 기반 의미 검색으로 색인하고, HyDE 질의 확장·reranking·RAG/ReAct 생성을 결합하여 인용을 단 장문 답변을 생성하는 천문학 문헌 리뷰·지식 발견용 시스템(프레임워크)이다. 키워드 일치에 의존하는 기존 검색을 의미 검색으로 대체한 grounded literature QA 도구이며, 벤치마크가 아니라 실제 배포된 시스템이다.

## 시스템 구조 (Pathfinder Architecture)
- **Corpus:** 총 352,194편의 peer-reviewed 천문학 논문(Kaggle arXiv astro-ph 약 27만 편을 ADS 메타데이터로 보강). 현재 버전은 초록(abstract)만 사용하며 향후 full-text 확장 가능.
- **Embedding / 벡터 검색:** OpenAI text-embedding-3-small(1536차원)로 임베딩, cosine similarity로 FAISS 인덱싱·검색. 시각화는 UMAP 2D 축소.
- **키워드 추출:** spaCy·pytextrank로 초록마다 20개 키워드 사전 추출(키워드 reranking에 사용).
- **Reranking (recency / citation / keyword):**
  - *Recency*: 약 5년 이상 오래된 논문에 시그모이드 페널티.
  - *Citation*: 피인용이 높은 문헌을 선호하는 시그모이드 가중.
  - *Keyword*: 천문 전문 용어·천체명·사용자 지정 문자열을 사전 키워드와 비교해 일치 문서를 가중.
- **2단계 검색 + 신경 reranker:** 초기 top-k=250을 HyDE 의미 검색으로 가져온 뒤, Cohere rerank-english-v3.0으로 재정렬해 최종 1~30편 선택.
- **생성기 (RAG + ReAct):** LangChain으로 RAG 구성. 검색된 초록 청크를 LLM에 전달해 답을 합성하며, 관련 출처가 없으면 "I don't know"로 응답하도록 제약. 복합·반사실 질의에는 ReAct 에이전트가 추론·검색을 반복. 생성·합의 평가에 GPT-4 / GPT-4o mini 사용.
- **프론트엔드:** Streamlit UI, HuggingFace Spaces 배포(pathfinder.app). 데이터셋·코드 공개.

## 동작 파이프라인 (inference)
1. 질의 입력 → 질의 유형 분류(단일/다중 논문 사실, 합의 평가, 복합, What-If·반사실 등) 및 NER·전문용어·시간민감 플래그 판별.
2. **HyDE 질의 확장:** LLM이 "전문 천문학자"로서 질의를 도메인 특화 가상 초록으로 재작성.
3. **의미 검색:** 확장 질의 임베딩으로 FAISS에서 top-k=250 후보 검색.
4. **Reranking:** recency·citation·keyword 가중 + Cohere reranker로 최종 1~30편 선정.
5. **답변 생성:** 질의 유형별 특화 프롬프트로 RAG 답변 생성(단일=간결, 다중=요약 합성, 넓은 질의=초기답변→자기비판→개선). 복합·반사실은 ReAct 단계로 처리.
6. **출력:** 답변 + top-k 논문 표 + 질의 유형 + 관련도(0~1) 추정. 합의 질의는 7단계(Strong Agreement … No Clear Consensus … Strong Disagreement)로 평가, 이상치(outlier) 논문도 플래그.

## 주요 기능/결과
- **활용:** 의미 기반 문헌 리뷰, 지식 발견, 합의 평가, 예상 밖 논문 탐지 등 grounded literature QA 워크플로우.
- **단일 논문 합성 벤치마크**(무작위 500편, top-k=10): Bag-of-Words s=0.46, r⁻¹=0.29 → HyDE+reranking s=0.84, r⁻¹=0.74.
- **다중 논문 합성 벤치마크**(리뷰 논문 200편, top-k=50): Bag-of-Words recall=0.15, nDCG=0.09 → HyDE+reranking recall=0.29, nDCG=0.19.
- **Gold QA 데이터셋:** Slack 봇으로 36명 천문학자가 370개 질문 제출, 전문가 답변 수집. 사용자 긍정 상호작용과 검색 점수가 양의 상관(Spearman ρ=+0.33).

## 한계점
- 초록만 색인 → 본문 깊은 데이터·방법 세부 질의는 자주 놓침.
- 매우 최신 논문·일부 niche 저널 미포함(불완전 코퍼스).
- 인용 그래프 미활용 → 상세 bibliometric 분석, 특정 저자·기관 검색, 계산 수행은 부적합.
- LLM 편향·환각 가능 → 답변을 top-k 논문과 교차 검증 필요.
- 복합·반사실 질의는 ReAct 없이는 직접 답변 불가하며, ReAct도 루프에 빠질 수 있음.

## 관련 정보
- Iyer, Yunus, O'Neill, Ye, et al., ApJS 275:38, 2024.
- arXiv: 2408.01556 (https://arxiv.org/abs/2408.01556)
- DOI: https://doi.org/10.3847/1538-4365/ad7c43
- 라이브 도구: pathfinder.app (HuggingFace Spaces 배포), 코드·데이터셋 공개.
