---
title: "Large Language Model Integration for Knowledge Retrieval and Interaction for the DUNE Experiment"
bib_key: rafique2025large
year: 2025
domain: physics
type: Method
venue: arXiv (Lepton Photon 2025)
paper_link: https://arxiv.org/abs/2601.05278
---
# DUNE-GPT: LLM Integration for Knowledge Retrieval in the DUNE Experiment

> arXiv 2025 | Method | physics
> Rafique et al. — Argonne National Laboratory (DUNE Collaboration)
> DBLP: `journals/corr/abs-2601-05278`

## 한 줄 요약
Deep Underground Neutrino Experiment(DUNE) 협업의 DocDB·Indico·내부 위키에 산재된 방대한 실험 문서를 Fermilab 인프라(Aurora/Argo 슈퍼컴퓨터 + Ollama)에서 on-premise 밀집 검색으로 통합한 RAG 프로토타입 시스템. 다양한 질의 유형에서 예비 검색 정확도 ~70%를 보고.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 소스 식별 및 수집
  DUNE 내부 문서 생태계:
  ┌─ DocDB: 기술 설계 보고서(TDR), 분석 노트, 기술 노트
  ├─ Indico: 회의 발표 자료, 미팅 노트
  └─ 내부 위키 문서
  협업 정책에 따라 민감/제한 문서 제외 (공개 접근 가능 문서만)

Step 2 — 전처리 및 청킹
  다양한 형식 처리: PDF, DOCX, TXT, PNG 등
  메타데이터 추출 (날짜, 저자, 문서 타입)
  토큰 기반 분할 (청크 크기 미기재)

Step 3 — 임베딩 및 벡터 DB 구축
  임베딩 모델: multi-qa-mpnet-base-dot-v1 (과학 텍스트 최적화)
  벡터 DB: FAISS (Facebook AI Similarity Search)
  검색 방식: cosine similarity

Step 4 — LLM 통합 (on-premise)
  Argonne 슈퍼컴퓨터(Aurora/Argo):
    Aurora: 초기 개발 및 대규모 실험 (Intel Gaudi 가속기)
  Fermilab:
    Ollama로 LLM 내부 호스팅 (구체적 모델명 미기재)
  RAG 방식: 검색 컨텍스트를 LLM에 조건화하여 응답 생성

Step 5 — 접근 제어 및 인터페이스
  인증된 DUNE 공동연구자만 접근
  경량 웹 인터페이스:
    자연어 질의 → 포맷된 응답 + 출처 문서 인용 표시

Step 6 — 예비 평가
  다양한 질의 유형을 아우르는 쿼리 세트로 예비 평가
  결과: 검색 정확도 ~70% (preliminary)
  (P@k / MRR 등 정밀 메트릭 기반 체계 평가는 향후 과제)
```

---

## 실제 질의 예시 (논문 기술 기반)

**검출기 운영 질의:**
> **Q.** "What is the drift velocity of electrons in the liquid argon TPC at nominal electric field?"
>
> DUNE-GPT: DocDB TDR에서 관련 구절 검색 → 문서 인용 포함 답변 생성

**재구성 알고리즘 질의:**
> **Q.** "How does Pandora reconstruct neutrino interaction vertices in the far detector?"
>
> DUNE-GPT: Indico 발표 자료 + DocDB 분석 노트 통합 검색 → 답변

---

## 주요 결과

| 항목 | 수치 |
|---|---|
| 예비 검색 정확도 | ~70% (다양한 질의 유형) |
| 임베딩 모델 | multi-qa-mpnet-base-dot-v1 |
| 벡터 DB | FAISS |
| 처리 형식 | PDF, DOCX, TXT, PNG 등 |

MITRA(CMS, P@1=0.75)·chATLAS(ATLAS) 등 유사 물리 협업 RAG 시스템과 달리 BM25 대비 정량 비교 실험은 아직 미수행. "Preliminary" 단계임을 논문이 명시.

---

## 한계점
- 프로토타입 단계 — 협업 전체 배포 전, 체계적 벤치마크 미수행
- 민감 문서 제외로 지식 커버리지 불완전
- 검색 모델과 LLM의 조합 최적화 실험 미수행
- BM25 등 베이스라인 대비 정량 비교 없음

---

## 관련 정보
- **논문**: [arXiv:2601.05278](https://arxiv.org/abs/2601.05278)
- **수락**: 32nd International Symposium on Lepton Photon Interactions at High Energies, Madison WI, Aug 2025
- **저자 소속**: Argonne National Laboratory (DUNE Collaboration)
