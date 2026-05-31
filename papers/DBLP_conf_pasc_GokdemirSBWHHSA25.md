---
title: "HiPerRAG: High-Performance Retrieval Augmented Generation for Scientific Insights"
bib_key: "DBLP:conf/pasc/GokdemirSBWHHSA25"
year: 2025
domain: bio, medical, chem, physics
type: Method
venue: PASC
paper_link: https://arxiv.org/abs/2505.04846
---
# HiPerRAG: HPC-Scale RAG for Scientific QA
> PASC 2025 | Method | bio · medical · chem · physics

## 한 줄 요약
HiPerRAG는 고성능 컴퓨팅(HPC)으로 360만 편 이상의 과학 논문을 색인·검색해 객관식 과학 QA에 답하는 RAG 인프라다. 멀티모달 문서 파서 Oreo와 질의 인지 인코더 미세조정 ColTrast를 핵심으로, Polaris·Sunspot·Frontier 슈퍼컴퓨터의 수천 GPU로 백만 문서 규모 RAG를 가능하게 한다. (출력은 합성이 아니라 검색-답변형 closed-form QA이므로 K1.O1로 분류.)

## 시스템 구조 (HiPerRAG Architecture)
- **코퍼스:** 360만 편 이상의 과학 논문을 색인·검색.
- **Oreo (멀티모달 문서 파싱):** 대규모 과학 문헌을 고처리량으로 파싱하는 모델. 기존 파서 대비 약 4.5배 빠름.
- **ColTrast (검색기 미세조정):** 질의 인지(query-aware) 인코더를 contrastive + late-interaction 방식으로 미세조정해 검색 정확도를 높이는 알고리즘.
- **생성기:** 검색된 패시지를 LLM에 전달해 객관식 답을 생성.
- **HPC 스택:** Polaris·Sunspot·Frontier에서 수천 GPU로 확장하는 인프라(독립 모델이 아니라 백만 문서 규모 RAG를 떠받치는 소프트웨어 스택).

## 동작 파이프라인 (inference)
1. 질문 입력 → ColTrast로 미세조정된 인코더로 360만+ 논문 색인에서 관련 패시지 검색.
2. 검색된 패시지를 LLM 생성기에 전달.
3. 객관식/단답 형태의 답을 생성하고 정확도로 평가.

## 주요 결과
- 기존 과학 QA 벤치마크에서 **SciQ 90%, PubMedQA 76% 정확도**.
- 자체 제작 단백질 QA 벤치마크(ProteinInteractionQA, ProteinFunctionQA) 도입.
- 핵심 기여: 백만 문서 규모로의 RAG 확장(파싱·임베딩 비용 문제 해결)과 검색 정확도 향상.

## 한계점
- 출력이 객관식 QA에 한정되어 다중 출처 통합(synthesis)이나 장문 합성은 다루지 않음.
- 슈퍼컴퓨터급 자원을 전제로 한 인프라라 재현·접근성이 제한적.
- 단백질 QA 벤치마크가 LLM 생성으로 만들어져 품질 편향 가능.

## 관련 정보
- arXiv: 2505.04846 (https://arxiv.org/abs/2505.04846)
- DOI: https://doi.org/10.1145/3732775.3733586 (PASC 2025)
- Argonne National Laboratory · University of Chicago 외
