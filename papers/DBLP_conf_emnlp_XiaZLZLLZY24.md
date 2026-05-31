---
title: "RULE: Reliable Multimodal RAG for Factuality in Medical Vision Language Models"
bib_key: "DBLP:conf/emnlp/XiaZLZLLZY24"
year: 2024
domain: medical
type: Method
venue: EMNLP
paper_link: https://arxiv.org/abs/2407.05131
---
# RULE: Reliable Multimodal RAG for Medical VLMs
> EMNLP 2024 | Method | medical

## 한 줄 요약
RULE은 의료 영상-리포트 검색 기반 멀티모달 RAG로, (1) 검색 컨텍스트 개수를 통계적 위험 제어(Factuality Risk Control)로 보정해 사실성 위험을 사용자 지정 상한 이하로 보장하고, (2) 검색 과의존을 줄이는 선호 튜닝(Knowledge-Balanced Preference Tuning)을 결합해 Med-LVLM의 사실 정확도를 평균 47.4% 개선한다.

## 시스템 구조 (RULE Architecture)
- **멀티모달 retriever:** CLIP 스타일 대조학습(ResNet-50 영상 + BioClinicalBERT 텍스트). 입력 영상으로 코사인 유사도 top-K 리포트 검색. 백본 Med-LVLM은 LLaVA-Med-1.5 7B.
- **Calibrated context selection (FRC):** 검색 개수 k를 Learn-then-Test 위험제어로 보정 — 사실성 위험 FR(k)이 상한 α를 넘지 않는 k만 채택(확률 1−δ 보장). 너무 많은 검색이 주는 노이즈를 통계적으로 차단.
- **RAG-based preference fine-tuning (KBPT):** 검색 없이는 맞히던 문제를 검색 후 틀리는 "과의존" 샘플을 dispreferred로 두는 DPO식 LoRA 선호 학습.

## 동작 파이프라인 (inference)
1. 입력 영상·질의 → retriever가 코사인 유사도 top-K 리포트 검색.
2. FRC로 보정된 k개 컨텍스트 선택.
3. (질의+선택 리포트+영상)을 KBPT로 튜닝된 LLaVA-Med에 입력.
4. 사실성 보정된 VQA 답 또는 리포트 생성.

## 주요 결과
Medical VQA 정확도(%): IU-Xray 75.47→**87.84**, MIMIC-CXR 75.79→**83.92**, Harvard-FairVLMed 63.03→**87.12**. 사실 정확도 평균 +47.4%, 기존 환각완화 대비 +14.46%, 과의존 error/ratio 각각 −42.9%/−47.3%.

## 한계점
- 사실성에 초점 — 안전성·공정성·강건성·프라이버시는 향후 과제.
- retriever 코퍼스(도메인 영상-리포트 쌍) 커버리지 밖 영상에서는 검색 품질 저하 가능.

## 관련 정보
- arXiv: 2407.05131 · EMNLP 2024 (Xia et al.)
- 코드: https://github.com/richard-peng-xia/RULE
