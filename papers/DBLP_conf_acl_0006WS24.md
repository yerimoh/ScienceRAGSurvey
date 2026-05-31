---
title: "MindMap: Knowledge Graph Prompting Sparks Graph of Thoughts in Large Language Models"
bib_key: "DBLP:conf/acl/0006WS24"
year: 2024
domain: medical
type: Method
venue: ACL
paper_link: https://arxiv.org/abs/2308.09729
---
# MindMap: Knowledge Graph Prompting for Medical QA
> ACL 2024 | Method | medical

## 한 줄 요약
MindMap는 큐레이티드 임상 지식그래프(질병-증상-약물-검사)에서 질의 관련 증거 서브그래프를 검색하고, 이를 자연어 추론 경로("graph of thoughts")로 통합하여 LLM이 명시적 KG 지식과 암묵 지식을 결합한 근거 답변 + 추론 경로(mind map)를 생성하도록 프롬프팅하는 KG-프롬프팅 프레임워크다.

## 시스템 구조 (MindMap Architecture)
- **큐레이티드 임상 KG:** EMCKG(영어, 1,122 노드 / 5,802 트리플 / 6 관계)와 CMCKG(중국어, 62,282 노드 / 506,490 트리플 / 12 관계). 증상→질병→검사/약물 임상 흐름.
- **증거 서브그래프 검색(상보적 2종):** LLM으로 질의 엔티티 추출 + BERT 유사도로 KG 노드 매칭 → ① path-based(질의 엔티티를 ≤k hop 경로로 연결), ② neighbor-based(경로 노드의 1-hop 이웃 확장). 클러스터링·샘플링으로 pruning.
- **Graph-of-thoughts:** 검색 서브그래프의 엔티티 체인을 LLM이 자연어로 변환·집계해 단일 추론 그래프로 통합.
- **프롬프트:** system instruction + question + 증거 그래프 + graph-of-thought instruction + exemplars.

## 동작 파이프라인 (inference)
1. **Evidence graph mining:** 엔티티 인식(LLM+BERT) → path/neighbor 서브그래프 검색.
2. **Aggregation:** 서브그래프들을 단일 추론 그래프로 통합·정제.
3. **Reasoning:** 프롬프트로 LLM이 그래프와 암묵 지식을 결합 → (a) 요약 답변, (b) 추론 과정, (c) mind map(구조화 텍스트) 출력.

## 주요 결과
backbone GPT-3.5로 일부 baseline에서 GPT-4 능가. 데이터셋: GenMedGPT-5k, CMCQA, ExplainCPE.
- GenMedGPT-5k BERTScore F1: MindMap **0.7954** > KG Retriever 0.7868 > GPT-4 0.7786. GPT-4 평가 ranking에서 MindMap 1.87 vs GPT-4 4.18.
- 쌍대 비교(MindMap vs GPT-4 승률): diversity/integrity 100%, 약물 추천 83%, 진단 73%.
- ExplainCPE 정확도 61.7%. Ablation: path+neighbor 결합이 단일 대비 우수.

## 한계점
- 성능이 큐레이티드 임상 KG의 완전성·정확성에 의존, KG 없는 영역 일반화 제한.
- 엔티티 인식·매칭 오류 시 서브그래프 오염 가능.
- 평가가 GPT-4 심판·BERTScore에 의존(편향 가능), 의료 3개 데이터셋에 국한.

## 관련 정보
- arXiv: 2308.09729 · ACL 2024 (Wen, Wang, Sun)
- 코드: https://github.com/wyl-willing/MindMap
