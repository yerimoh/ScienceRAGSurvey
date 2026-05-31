---
title: "Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation"
bib_key: "DBLP:conf/naacl/SunZHX25"
year: 2025
domain: medical
type: Method
venue: NAACL
paper_link: https://arxiv.org/abs/2407.15268
---
# FactMM-RAG: Fact-Aware Multimodal RAG for Radiology Reports
> NAACL 2025 | Method | medical

## 한 줄 요약
RadGraph로 추출한 사실(entity-relation) 일치도를 기준으로 영상-리포트 쌍을 마이닝해 사실 인지형(fact-aware) 멀티모달 retriever를 학습하고, 검색된 참조 리포트를 LLaVA에 조건으로 주입해 사실적으로 정확한 흉부 방사선 리포트를 생성하는 RAG 시스템. 진단 라벨 감독이나 전문가 큐레이션 없이 사실 인지를 생성기까지 전파한다.

## 시스템 구조 (FactMM-RAG Architecture)
- **RadGraph 사실 일치 쌍 마이닝:** ① 같은 증상 라벨로 false negative 제거, ② 엔티티/릴레이션 기반 사실 유사도에 엄격 임계값 δ를 적용해 positive 쌍 선별.
- **사실 인지 멀티모달 retriever:** 백본 MARVEL(T5-ANCE 기반). 쿼리=영상, 문서=(리포트,영상) 쌍을 인코딩, 마이닝한 사실 positive로 InfoNCE 대조학습(τ=0.01).
- **생성기 조건화:** LLaVA-1.5가 쿼리 X-ray + 검색된 참조 리포트 + 지시 프롬프트로 findings 생성.

## 동작 파이프라인 (inference)
1. 학습된 MARVEL로 쿼리 영상 인코딩.
2. 학습 코퍼스에서 코사인 유사도 **top-1** 참조 리포트 검색(자기검색·비정상 리포트 제외).
3. 영상 + 참조 리포트 + 프롬프트를 LLaVA에 입력.
4. findings 자기회귀 생성.

## 주요 결과
데이터: MIMIC-CXR(train 125,417 / val 991 / test 1,624), zero-shot CheXpert(1,000). SOTA retriever 대비 **F1CheXbert 최대 +6.5%, F1RadGraph +2%**. MIMIC-CXR: F1CheXbert 0.602 / F1RadGraph 0.257 / ROUGE-L 0.307 / BERTScore 0.561 (Med-MARVEL·CLIP 등 baseline 상회). Oracle 상한 F1CheXbert 0.992.

## 한계점
- 흉부 방사선에 한정(뇌 스캔·조직병리 일반화 미검증).
- 평가 지표가 사실/텍스트 유사도 중심 — 간결성·인간 정합 평가 부재.

## 관련 정보
- arXiv: 2407.15268 · NAACL 2025 (Sun et al.)
- 코드: https://github.com/cxcscmu/FactMM-RAG
