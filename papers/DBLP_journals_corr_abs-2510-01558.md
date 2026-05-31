---
title: "CardioRAG: A Retrieval-Augmented Generation Framework for Multimodal Chagas Disease Detection"
bib_key: "DBLP:journals/corr/abs-2510-01558"
year: 2025
domain: medical
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2510.01558
---
# CardioRAG: Retrieval-Augmented ECG Diagnosis
> arXiv 2025 | Method | medical

## 한 줄 요약
CardioRAG는 12-lead ECG 기반 샤가스병(Chagas disease) 검출을 위해, 과거 환자 ECG 사례 DB(VAE 잠재표현 + 추출 임상특징 + 진단라벨)에서 잠재공간 코사인 유사도로 가장 유사한 사례를 검색하고, 이를 구조화된 컨텍스트로 LLM에 grounding해 해석 가능한 진단을 생성하는 RAG 프레임워크다. (영상 외 생리신호로 K3 확장)

## 시스템 구조 (CardioRAG Architecture)
- **VAE ECG 잠재표현:** 4개 residual block 인코더로 ECG를 256차원 잠재로 인코딩(L = L_recon + β·L_KL, β=0.1).
- **과거 사례 DB:** 각 사례에 VAE 잠재 + 인구통계 + 임상특징(RBBB/LAFB 자동검출, V5 ventricular rate·RMSSD) + 진단 라벨 저장.
- **검색→LLM grounding:** 잠재공간 코사인 유사도로 후보 검색 후 복합점수(S_VAE + w_age·S_age)로 재정렬해 top-k 선택. 검색 사례는 **구조화된 텍스트**(인구통계·특징·HRV·라벨)로 변환되어 LLM에 입력(원 파형은 검색 단계에만 사용). LLM=DeepSeek-R1:1.5b.

## 동작 파이프라인 (inference)
1. ECG 전처리 → 임상특징 자동 추출 → VAE로 256차원 잠재 인코딩.
2. 잠재 유사도 검색 + 복합점수 재정렬 → top-k(최적 k=8) 사례.
3. 검색 사례를 구조화 컨텍스트로 프롬프트에 결합.
4. LLM이 이진 진단 + confidence + 임상 추론을 JSON으로 출력.

## 주요 결과
데이터: SaMi-Trop(양성)·PTB-XL(음성)·CODE-15%. 테스트 100명(양성50/음성50). RAG 미적용 recall 48.98% → **RAG(k=8) recall 85.7~89.8%**. 최적(P2 간결 프롬프트, k=8): accuracy 58.59% / recall 87.76% / F1 0.68. k=16은 과다검색으로 저하(역U자).

## 한계점
- accuracy 58~59% ceiling — 소형 LLM 한계, 대형 LLM 평가 필요.
- 소형 LLM의 confidence score 신뢰 어려움.
- 검색 DB 구성 데이터셋·분할이 본문에 명시 부족.

## 관련 정보
- arXiv: 2510.01558 (Shen, Zhai, Tu, Shi; Imperial College London / Oxford)
