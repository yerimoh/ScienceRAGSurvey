---
title: "GraPPI: A Retrieve-Divide-Solve GraphRAG Framework for Large-scale Protein-protein Interaction Exploration"
bib_key: "DBLP:conf/naacl/LiCJ25"
year: 2025
domain: bio
type: Method
venue: NAACL
paper_link: https://aclanthology.org/2025.findings-naacl.201/
---
# GraPPI: Retrieve-Divide-Solve GraphRAG over STRING PPI
> NAACL 2025 (Findings) | Method | bio

## 한 줄 요약
GraPPI는 STRING 단백질-단백질 상호작용(PPI) 지식그래프 위에서 동작하는 GraphRAG로, 대규모 신호전달 경로를 Retrieve-Divide-Solve 전략으로 처리한다. 거대한 경로를 개별 PPI 엣지로 분할해 병렬 설명한 뒤 경로 수준으로 합성·재정렬해, 치료 타깃 발굴을 위한 설명 가능·확장 가능한 경로 분석을 생성한다.

## 시스템 구조 (GraPPI Architecture)
- **STRING PPI KG:** 노드 18,767(인간 단백질) / 엣지 2,955,220. 엣지에 combined_score(신뢰도)·상호작용 유형, 노드에 단백질 주석.
- **Retrieve:** 이동식 kNN 그래프 윈도로 연결 단백질 노드를 추출해 상호작용 서브그래프 구성(FAISS).
- **Divide:** 엣지 설명 에이전트가 전체 경로를 개별 엣지로 분해, 각 엣지를 양 끝 단백질 컨텍스트와 함께 병렬 분석.
- **Solve:** 경로 설명 에이전트가 PPI 경로 설명을 합성하고 LLM zero-shot 랭킹으로 치료 관련성 평가.
- **생성기:** 임베딩 text-embedding-3-small, LLM GPT-4o/4o-mini/4-Turbo + 전문가 공동설계 CoT.

## 동작 파이프라인 (inference)
1. 초기 단백질 입력 → 연결 노드 추출 + kNN 윈도로 상호작용 서브그래프 형성.
2. Edge Explanation: 각 PPI 엣지를 양 끝 단백질 주석과 함께 병렬 설명(분할).
3. Path Exploration: 엣지 설명을 집계해 다중 PPI 경로 설명 합성.
4. Re-rank: LLM 관련성 점수로 경로 정렬 → 상위 n개 경로 제시.

## 주요 결과
평가: 정확도(의미·어휘 정렬, BERTScore·ROUGE), 확장성(경로 40~160 그래프), 전문가 케이스 스터디. 4개 설정(Baseline / Zero-shot+CoT / RAG w/o CoT / GraPPI)에서 **GraPPI가 모든 LLM·지표 최고**. 예: GPT-4-Turbo ROUGE-1 F1 RAG 38.70 → **GraPPI 42.19**, ROUGE-L 31.93 → **37.47**.

## 한계점
- STRING이 알려진 모든 PPI를 포괄하지 못함.
- 케이스 스터디가 초기 단백질 2개 기반(대표성 제한).
- 그래프가 커질수록 이점 감소, 엣지 설명이 LLM 컨텍스트 한계 근접.
- 연구용 프로토타입(배포 시스템 아님).

## 관련 정보
- arXiv: 2501.16382 · NAACL 2025 Findings (Li, Chen, Jeon)
- 코드: https://github.com/AaronLi43/GraPPI
