---
title: "MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations"
bib_key: "DBLP:journals/corr/abs-2603-09800"
year: 2026
domain: physics
type: Method
venue: arXiv (NeurIPS 2025 ML4PS Workshop / Lepton Photon 2025)
paper_link: https://arxiv.org/abs/2603.09800
---
# MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations

DBLP:journals/corr/abs-2603-09800 | 2026 | arXiv | Method | [physics] | [paper](https://arxiv.org/abs/2603.09800)

**Retriever**: Dense Passage Retrieval (facebook/dpr-question_encoder-multiset-base) + Cross-encoder Reranker (cross-encoder/ms-marco-MiniLM-L-6-v2)
**Eval Task**: CMS internal document retrieval (physics analysis QA)
**Eval Metric**: Precision@k, Recall@k, MRR, NDCG@5
**Method Name**: MITRA
**Modality**: Text

> arXiv | 2026 | Method | physics
#### 📌 한 줄 요약
CERN Compact Muon Solenoid(CMS) 실험 협업의 방대한 내부 문서(분석 노트, 위키, 가이드라인)를 대상으로 개인 정보 보호 on-premise RAG를 구현한 시스템으로, 의미론적 검색(DPR)과 재랭킹(cross-encoder)을 결합하여 BM25 대비 P@1 기준 약 5.8× 향상을 달성했다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- CMS 협업은 수천 명의 연구자가 생성하는 방대한 내부 문서를 보유하지만, 전통적 키워드 검색(BM25)은 사용자 질의와 문서 표현 간의 의미론적 불일치에 취약
- 상업적 LLM API 사용은 비공개 연구 데이터를 외부 서버로 전송하는 문제 발생

**MITRA가 필요한 이유**
- 새로운 PhD 학생이나 다른 분석 그룹의 전문가가 특정 측정의 세부 내용을 파악하는 데 많은 시간 소모
- "transverse momentum requirement" 같은 일상적 표현으로 질의했을 때 "pT cut"이라고 명시된 문서를 정확히 찾아야 함

#### 🔨 시스템 구성
**오프라인 파이프라인 (데이터베이스 구축)**
1. Selenium 기반 자동화 스크레이퍼: CMS 내부 DB에서 문서 수집
2. OCR + layout parsing: 고충실도 텍스트 추출
3. 문단 단위 청킹 후 DPR 인코더로 768차원 벡터 생성
4. Chroma DB에 임베딩 저장

**온라인 파이프라인 (추론)**
1. 사용자 질의 → 동일 DPR 인코더로 인코딩
2. 2단계 벡터 DB: 추상(Abstract) DB에서 관련 분석 식별 후 전문(Full-Doc) DB에서 세부 검색
3. Cross-encoder 재랭킹 (ms-marco-MiniLM-L-6-v2)
4. 4-bit 양자화 Mistral-7B LLM (Ollama/LangChain)으로 응답 생성

**인프라**
- 모든 컴포넌트 on-premise (NVIDIA Tesla T4, 15GB 메모리)
- Streamlit 기반 웹 인터페이스

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| Set 1 P@1 (정확 키워드 매칭) — MITRA | 1.00 |
| Set 1 P@1 — BM25 | 1.00 |
| Set 2 P@1 (의미론적 질의) — MITRA | 0.75 |
| Set 2 P@1 — BM25 | 0.13 |
| P@1 향상 비율 (Set 2) | ~5.8× |
| Set 2 MRR — MITRA | 0.81 |
| Set 2 MRR — BM25 | 0.35 |
| Set 2 NDCG@5 — MITRA | 0.88 |
| Set 2 NDCG@5 — BM25 | 0.59 |

> **주의**: main.tex에서 "6× improvement over BM25"로 서술되어 있으나, 논문의 Table 1/2 원본 수치로부터 계산된 P@1 향상은 약 5.8×(=0.75/0.13)이다. "6×"는 반올림된 서술로 추정되며, main.tex의 서술이 사실과 크게 다르지 않으나 정밀 수치는 원 논문 Table 확인 필요.

#### ⚠️ 한계점
- 프로토타입 단계 (현재 전체 협업 배포 전)
- 평가 쿼리 집합이 소규모 (전문가 설계 쿼리 2세트)
- P@k/R@k 메트릭은 검색 품질을 평가하나 하위 언어 모델의 답변 정확도(QA hallucination)는 별도 평가 미수행
- 다른 physics collaboration 외부로의 일반화 가능성 미검증

## 관련 정보
- **논문**: [arXiv:2603.09800](https://arxiv.org/abs/2603.09800)
- **수락**: NeurIPS 2025 Machine Learning for Physical Sciences Workshop + Lepton Photon 2025
- **저자 소속**: University of Wisconsin-Madison
- **K4 분류**: K4.O1 — 기관 내부 문서(CMS 내부 코퍼스)에 대한 RAG 시스템
