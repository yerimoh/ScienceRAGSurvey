---
title: "KG-Rank: Enhancing Large Language Models for Medical QA with Knowledge Graphs and Ranking Techniques"
bib_key: "DBLP:conf/bionlp/YangLMZKLCCCML24"
year: 2024
domain: medical
type: Method
venue: BioNLP@ACL
paper_link: https://aclanthology.org/2024.bionlp-1.13/
---
# KG-Rank: Knowledge-Graph + Ranking for Long-form Medical QA
> BioNLP@ACL 2024 | Method | medical

## 한 줄 요약
KG-Rank는 의학 질문에서 의료 엔티티를 추출해 UMLS에서 one-hop 트리플(사실)을 가져온 뒤, IR의 ranking/re-ranking 기법(유사도·Answer Expansion·MMR·MedCPT 재랭킹)으로 가장 관련성 높은 사실만 추려 LLM에 주입함으로써, 파인튜닝 없이 장문(long-form) 의료 답변의 사실성·품질을 높이는 프레임워크다.

## 시스템 구조 (KG-Rank Architecture)
1. **의료 NER:** 프롬프트로 LLM이 질문에서 의료 엔티티를 추출, UMLS 엔티티로 매핑.
2. **UMLS one-hop 검색:** 엔티티별 one-hop 관계 트리플 (e_i', r, e_j') 수집(한 엔티티가 수천 관계 → ranking 필수).
3. **Ranking/Re-ranking(핵심):** UmlsBERT 임베딩으로 질문-트리플 정렬. 4가지 변형 — Similarity / Answer Expansion(가짜 답변 생성 후 [Q,A]로 검색) / MMR(관련성+다양성, 선택 수에 따라 다양성 페널티 증가) / Re-ranking(MedCPT cross-encoder).
4. **장문 합성:** 상위 트리플 + task 프롬프트를 LLM에 주입해 free-text 답변 생성.

## 동작 파이프라인 (inference)
1. 질문 → 의료 엔티티 추출 → UMLS 매핑.
2. one-hop 트리플 검색.
3. Similarity/AE/MMR/Re-ranking으로 트리플 정렬.
4. 상위 트리플 + 프롬프트 → LLM 장문 답변.

## 주요 결과
백본 GPT-4 등, 데이터셋 ExpertQA-Bio/Med, LiveQA, MedicationQA. GPT-4 기준 Zero-Shot→KG-Rank ROUGE-L: ExpertQA-Bio 23.00→**27.20**, ExpertQA-Med 25.45→**28.08**, MedicationQA 14.41→**16.19**; BERTScore도 일관 향상. 일반 도메인(Law/Business/Music/History)에서도 ROUGE-L 향상으로 확장성 시사.

## 한계점
- 사실성에 대한 physician 평가는 향후 과제(현재 미수행).
- 의료 특화 base model 평가 부족.
- ranking 단계가 추가 연산 시간 증가.

## 관련 정보
- arXiv: 2403.05881 · BioNLP@ACL 2024 (Yang et al.)
- 코드: https://github.com/YangRui525/KG-Rank · 소스 UMLS, 임베딩 UmlsBERT, 재랭커 MedCPT
