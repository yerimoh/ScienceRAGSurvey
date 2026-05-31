---
title: "HyKGE: A Hypothesis Knowledge Graph Enhanced RAG Framework for Accurate and Reliable Medical LLMs Responses"
bib_key: "DBLP:conf/acl/Jiang0XQFWTDC0W25"
year: 2025
domain: medical
type: Method
venue: ACL
paper_link: https://aclanthology.org/2025.acl-long.580/
---
# HyKGE: Hypothesis Knowledge Graph Enhanced RAG
> ACL 2025 | Method | medical

## 한 줄 요약
짧고 불완전한 의료 질의를 보완하기 위해 LLM이 먼저 생성한 가설 출력(Hypothesis Output, HO)을 검색 시드로 삼아, 융합된 큐레이티드 의료 지식그래프 위에서 멀티홉 추론 체인을 검색하고, HO fragment 단위 재랭킹으로 노이즈를 걸러 종합 답변을 합성하는 KG 기반 RAG. LLM 호출 2회만으로 외부 KG 지식을 주입한다.

## 시스템 구조 (HyKGE Architecture)
- **LLM Hypothesis Output(HO):** "의료 전문가" 프롬프트로 질의에 대한 단계별 가설을 생성해 질의에 없던 엔티티를 끌어내어 검색을 풍부하게 시드.
- **융합 큐레이티드 의료 KG:** CMeKG + CPubMed-KG + Disease-KG 융합(엔티티 약 128.9만, 관계 약 356.9만). 엔티티 설명은 Wikipedia/Baidu/Medical Baike에서 보강.
- **NER·링킹:** W2NER로 질의⊕HO에서 엔티티 추출, GTE 임베딩 유사도(δ=0.7)로 KG 노드에 링킹.
- **멀티홉 검색:** k=3 hop 이내 Path / Co-ancestor / Co-occurrence 추론 체인 + 엔티티 설명 수집.
- **HO Fragment Granularity-aware Reranking:** 질의⊕HO를 fragment(윈도 10/오버랩 4)로 청킹, BGE reranker로 체인을 점수화·가지치기(topK=10) — 검색 지식과 가설의 밀도 정렬.

## 동작 파이프라인 (inference)
1. 질의 → LLM 가설 출력 HO.
2. NER(질의⊕HO) → GTE 링킹으로 KG 엔티티 확정.
3. k=3 멀티홉 추론 체인 검색.
4. HO fragment 기준 BGE 재랭킹 → topK=10 체인.
5. 체인을 화살표로 직렬화 + 설명 결합 → LLM Reader가 종합 답변 생성.

## 주요 결과
중국어 의료 QA(MMCU-Medical, CMB-Exam, CMB-Clin)에서 8개 baseline 상회. 예: MMCU-Medical EM(GPT-3.5) Base 43.52 → **HyKGE 49.65**, PCR 50.55 → **57.82**. 해석가능성(ACJ/PPL/ROUGE-R)도 큰 폭 개선. LLM 호출 2회·평균 19.76초로 다단계 baseline보다 효율적. Ablation: HO 제거 시 가장 큰 하락(49.65→41.08).

## 한계점
- 노이즈 필터링으로 약간의 추가 시간.
- 중국어 의료 데이터셋에 한정(타 언어·도메인 미검증).
- 성능이 KG 완전성에 의존, 원 KG에 엔티티 설명이 없어 외부 보강 필요.

## 관련 정보
- arXiv: 2312.15883 · ACL 2025 (Jiang et al.)
- 코드: https://github.com/Artessay/HyKGE
