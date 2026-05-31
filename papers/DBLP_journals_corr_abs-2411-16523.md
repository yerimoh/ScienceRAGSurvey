---
title: "LaB-RAG: Label Boosted Retrieval Augmented Generation for Radiology Report Generation"
bib_key: "DBLP:journals/corr/abs-2411-16523"
year: 2024
domain: medical
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2411.16523
---
# LaB-RAG: Label-Boosted RAG for Radiology Report Generation
> arXiv 2024 | Method | medical

## 한 줄 요약
LaB-RAG는 거대 모델을 task에 fine-tuning하지 않고도 방사선 리포트를 생성하는 학습-프리(training-free) RAG + in-context learning 파이프라인이다. 흉부 X-ray에서 범주형 라벨을 예측해 검색 후보를 필터링하고, 영상 임베딩 유사도로 MIMIC-CXR의 〈영상-라벨-텍스트〉 튜플을 검색한 뒤, frozen 범용 LLM에 검색된 리포트를 예시로 제시해 리포트를 생성한다.

## 시스템 구조 (LaB-RAG Architecture)
- **라벨 예측:** frozen 영상 임베딩(MIMIC-CXR는 BioViL-T) 위에 가벼운 로지스틱 회귀로 CheXpert 14 + Other = 15개 범주형 라벨 예측(라벨러는 CheXbert가 우수).
- **라벨 필터 + 영상유사도 검색:** 코퍼스(학습 split의 영상-라벨-텍스트 튜플)와 코사인 유사도로 순위화 후, 예측 라벨로 Exact(정확 일치) 또는 Partial(겹치는 positive 라벨로 재정렬) 필터.
- **범용 LLM 프롬프팅:** frozen Mistral-7B-Instruct에 검색 예시 리포트 + 예측 라벨(Naive/Simple/Verbose/Instruct 프롬프트). 학습되는 건 라벨 분류기뿐.

## 동작 파이프라인 (inference)
1. 영상 인코딩 → 15개 라벨 예측.
2. 코퍼스와 영상 유사도 순위화 → Exact/Partial 라벨 필터.
3. 상위 k=5 튜플의 리포트를 in-context 예시로 선택.
4. 라벨 + 예시 리포트를 frozen Mistral-7B에 입력(greedy, temp 0) → 리포트 생성.

## 주요 결과
MIMIC-CXR Findings: **F1-CheXbert 0.466**(CXRMate 0.456·RGRG 0.447·검색 baseline CXR-RePaiR 0.353 상회), BLEU-4 0.265 / ROUGE-L 0.446 / BERTScore 0.815. Impression F1-CheXbert 0.484. 단 **F1-RadGraph는 fine-tuning baseline(CXRMate)에 뒤짐**. CheXpert Plus Findings F1-CheXbert 0.507.

## 한계점
- 임상 라벨 정확도(F1-CheXbert)는 강하나 F1-RadGraph 등 일부 NLG 지표는 fine-tuning baseline에 열세.
- 라벨 분류기·labeler 품질, 검색 코퍼스 규모에 성능 의존.
- 평가가 흉부 X-ray 리포트 생성에 한정.

## 관련 정보
- arXiv: 2411.16523 (Song, Subramanyam, Madejski, Grossman)
- 코드: https://github.com/uc-cdis/label-boosted-RAG-for-RRG
