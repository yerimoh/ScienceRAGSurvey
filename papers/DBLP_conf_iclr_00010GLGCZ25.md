---
title: "KGARevion: An AI Agent for Knowledge-Intensive Biomedical QA"
bib_key: "DBLP:conf/iclr/00010GLGCZ25"
year: 2025
domain: medical, bio
type: Method
venue: ICLR
paper_link: https://arxiv.org/abs/2410.04660
---
# KGARevion: KG-Grounded Agent for Biomedical QA
> ICLR 2025 | Method | medical · bio

## 한 줄 요약
KGARevion은 LLM의 잠재 지식으로 후보 triplet을 생성한 뒤, 이를 그라운디드 생의학 지식그래프(PrimeKG/OGB-biokg)에 검증·수정하고 답하는 Generate→Review→Revise→Answer 에이전트다. 사실 오류 triplet은 제거하고 불완전 지식은 유지해, KG에 검증된 지식으로 medical QA의 신뢰도를 높인다.

## 시스템 구조 (KGARevion Architecture)
- **Generate:** 질문에서 관련 후보 triplet을 LLM 잠재 지식으로 생성(객관식이면 choice-aware).
- **Review:** 각 triplet을 KG에 검증 — UMLS 코드로 엔티티 매핑, TransE 구조 임베딩을 관계 설명과 attention+FFN으로 정렬, LoRA 미세조정으로 True/False 출력. 두 soft-constraint: 사실 오류(Factually Wrong) 제거, 불완전 지식(Incomplete) 유지.
- **Revise:** False로 판정된 triplet을 재생성·재검증(최대 k 라운드).
- **Answer:** 검증된 True triplet 집합으로 최종 답 생성.
- **사용 KG:** PrimeKG / OGB-biokg(생의학 KG), UMLS 코드.

## 동작 파이프라인 (inference)
1. 질문 → 후보 triplet 생성(Generate).
2. KG 대조 검증(Review) → 사실 오류 제거, 불완전 보존.
3. False 집합 재생성·재검증(Revise, ≤k 라운드).
4. 검증된 triplet으로 답 생성(Answer).

## 주요 결과
medical QA 벤치마크(MMLU-Med, MedQA-US, PubMedQA*, BioASQ-Y/N, MedDDx Basic/Intermediate/Expert, AfriMed-QA)에서 평가. LLaMA3-8B·LLaMA3.1-8B(k=1) 및 open-ended(k=2)에서 baseline(직접 LLM, 일반 RAG, KG 방법) 대비 향상. (구체 수치는 원문 표 참조 — 단일 HTML 렌더 기준 검증.)

## 한계점
- 후보 triplet 생성 품질이 LLM 잠재 지식에 의존, KG에 없는 관계는 검증 한계.
- KG(PrimeKG/biokg) 커버리지·UMLS 매핑 정확도에 성능이 좌우.
- Review 모듈 LoRA 학습·다중 라운드로 추론 비용 증가.

## 관련 정보
- arXiv: 2410.04660 · ICLR 2025
- 코드: https://github.com/mims-harvard/KGARevion
