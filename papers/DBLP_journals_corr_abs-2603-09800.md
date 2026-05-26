---
title: "MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations"
bib_key: DBLP:journals/corr/abs-2603-09800
year: 2026
domain: physics
type: Method
venue: arXiv (NeurIPS 2025 ML4PS Workshop + Lepton Photon 2025)
paper_link: https://arxiv.org/abs/2603.09800
---
# MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations

> arXiv 2026 | Method | physics
> University of Wisconsin-Madison (CMS Collaboration)
> DBLP: `journals/corr/abs-2603-09800`

## 한 줄 요약
CERN CMS(Compact Muon Solenoid) 실험 협업의 방대한 내부 분석 노트·위키·가이드라인을 대상으로 on-premise 밀집 검색(DPR + cross-encoder 재랭킹 + 4-bit 양자화 Mistral-7B)을 구현한 RAG 시스템. 의미론적 질의(Set 2)에서 BM25 대비 **P@1 약 5.8× 향상**(0.75 vs. 0.13).

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문서 수집 (오프라인 파이프라인)
  Selenium 기반 자동화 스크레이퍼:
  CMS 내부 DB에서 분석 노트·위키·가이드라인 수집
  OCR + layout parsing으로 고충실도 텍스트 추출

Step 2 — 임베딩 및 벡터 DB 구축
  문단 단위 청킹 → DPR 인코더(multiset-base) → 768차원 벡터
  Chroma DB에 임베딩 저장
  2단계 벡터 DB 구조:
  ┌─ Abstract DB: 각 분석의 초록 수준 임베딩
  └─ Full-Doc DB: 전문 페이지 단위 임베딩

Step 3 — 온라인 추론 파이프라인
  사용자 질의
       ↓
  DPR 인코더(동일 모델)로 질의 벡터화
       ↓
  Abstract DB에서 관련 분석 후보 식별
       ↓
  Full-Doc DB에서 세부 구절 검색
       ↓
  Cross-encoder 재랭킹 (ms-marco-MiniLM-L-6-v2)
       ↓
  4-bit 양자화 Mistral-7B (Ollama/LangChain)으로 응답 생성

Step 4 — 평가 쿼리 설계
  전문가가 2가지 유형의 쿼리 세트 설계:
  Set 1: 정확한 키워드 매칭 질의 (ex. "VBF H→ττ analysis note")
  Set 2: 의미론적 질의 (ex. "transverse momentum requirement"
          → 문서에는 "pT cut"으로 기술)

Step 5 — 인프라
  모든 컴포넌트 on-premise (NVIDIA Tesla T4, 15GB VRAM)
  Streamlit 기반 웹 인터페이스
```

---

## 평가 쿼리 예시

**Set 2 (의미론적):**
> **Q.** "What is the transverse momentum requirement for the leading jet in the VBF analysis?"
>
> 문서에는 "pT cut on the leading jet" 또는 "leading jet pT threshold"로 기술 → 키워드 미스매치 발생
> MITRA: cross-encoder 재랭킹으로 의미론적으로 일치하는 문서 반환

**Set 1 (정확 키워드):**
> **Q.** "Find the CMS analysis note on the WH associated production measurement"
>
> BM25와 MITRA 모두 정확히 찾음 (P@1 = 1.00)

---

## 주요 평가 결과

| 지표 | Set 1 (정확 키워드) | Set 2 (의미론적) |
|---|---|---|
| P@1 — BM25 | 1.00 | 0.13 |
| P@1 — MITRA | 1.00 | **0.75** |
| 향상 비율 | — | **~5.8×** |
| MRR — BM25 | — | 0.35 |
| MRR — MITRA | — | **0.81** |
| NDCG@5 — BM25 | — | 0.59 |
| NDCG@5 — MITRA | — | **0.88** |

Set 1 (정확 키워드): BM25와 MITRA 동률 → 키워드 검색으로 충분한 경우
Set 2 (의미론적): MITRA가 압도적 우위 → 실제 사용자 질의에서 중요

---

## 한계점
- 프로토타입 단계 — CMS 협업 전체 배포 전
- 평가 쿼리 집합이 소규모 (전문가 설계 2세트)
- 검색 품질(P@k)은 측정되나 LLM 답변의 사실 정확도 평가 미수행
- 다른 물리 협업(ATLAS, ALICE 등) 외부로의 일반화 미검증
- 민감 문서 협업 정책에 따라 인덱싱 제외 → 지식 커버리지 불완전

---

## 관련 정보
- **논문**: [arXiv:2603.09800](https://arxiv.org/abs/2603.09800)
- **수락**: NeurIPS 2025 Machine Learning for Physical Sciences Workshop + Lepton Photon 2025
- **저자 소속**: University of Wisconsin-Madison (CMS Collaboration)
