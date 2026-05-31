---
title: "Biomedical knowledge graph-optimized prompt generation for large language models"
bib_key: "DBLP:journals/bioinformatics/SomanRMASPVCSRI24"
year: 2024
domain: bio, medical
type: Method
venue: Bioinformatics
paper_link: https://arxiv.org/abs/2311.17330
---
# KG-RAG: Biomedical Knowledge-Graph-Optimized Prompting (SPOKE)
> Bioinformatics 2024 | Method | bio · medical

## 한 줄 요약
SPOKE 생의학 지식그래프에서 질병 중심 서브그래프를 minimal graph schema로 추출하고, 임베딩 기반 context pruning으로 프롬프트와 의미적으로 가장 관련 있는 트리플만 골라 LLM 프롬프트에 주입하는 토큰 최적화 KG-RAG 프레임워크. 전체 스키마를 넣는 Cypher-RAG 대비 토큰을 평균 54% 줄이면서 검색 정확도·강건성을 높인다.

## 시스템 구조 (KG-RAG Architecture)
- **SPOKE KG:** 41개 큐레이티드 생의학 DB를 통합한 property graph(28종 노드 타입 ~4,200만 노드, 91종 엣지 타입 ~1.6억 엣지). 대부분 체계적 실험 측정 기반 큐레이션.
- **Minimal-schema 서브그래프:** 질병 노드의 이웃 트리플 (S,P,O)만 가져오고, SPOKE의 predicate 네이밍 규칙으로 스키마 없이 트리플을 영어 문장으로 변환(예: "Disease hypertension associates Gene VHL").
- **임베딩 기반 pruning:** 추출 트리플과 프롬프트를 같은 벡터공간에 임베딩, 코사인 유사도 75퍼센타일 초과 & ≥0.5인 것만 선택. context embedding은 PubMedBert.
- **프롬프트 생성:** 정제 컨텍스트를 자연어로 변환 + provenance(옵션: p-value 등 evidence) 첨부해 enriched prompt 구성.
- 하이퍼파라미터: context volume(100–200), context embedding model. 개체 인식은 GPT-3.5 추출 + MiniLM으로 SPOKE 질병 노드 매칭(99.7% 정확).

## 동작 파이프라인 (inference)
1. 질병 개체 인식(GPT-3.5 추출 → MiniLM 임베딩으로 SPOKE 노드 매칭).
2. 매칭 노드의 이웃 트리플 fetch.
3. 트리플·프롬프트 임베딩 → 코사인 pruning으로 prompt-aware context 선택.
4. 자연어 변환 + provenance 첨부 → enriched prompt 조립.
5. LLM(Llama-2-13b/GPT-3.5/GPT-4, temp 0)으로 답 생성.

## 주요 결과
**RAG 비교(KG-RAG vs Cypher-RAG, 100문항):** 검색 정확도 75%→**97%**; 개체명 소문자 perturbation 시 Cypher-RAG 0%로 붕괴, KG-RAG 97% 유지; 토큰 8006→**3693(−54%)**.
**True/False·MCQ(정확도):** MCQ에서 Llama-2 0.31→**0.53**, GPT-3.5 0.63→**0.79**, GPT-4 0.68→0.74. 세 LLM 모두 일관 향상.

## 한계점
- 현재 질병 중심 개체만 임베딩 → 질병 중심 질문에 한정(전체 노드로 확장은 future work).
- 성능이 SPOKE 정보 품질에 의존(KG 자체의 엄밀 평가는 범위 밖).
- SPOKE에 구현됨 — 타 KG/도메인 일반화는 향후 과제.

## 관련 정보
- arXiv: 2311.17330 · Bioinformatics 2024 (Soman et al., UCSF)
- 코드: https://github.com/BaranziniLab/KG_RAG
