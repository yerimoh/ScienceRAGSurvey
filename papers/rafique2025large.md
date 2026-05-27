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

> arXiv 2601.05278 | 2025 | Method | physics
> Rafique, Singh, Srinivas — Argonne National Laboratory (DUNE Collaboration)
> Presented at Lepton Photon 2025, Madison WI

## 한 줄 요약
**Deep Underground Neutrino Experiment (DUNE)** 의 DocDB·Indico·내부 위키 문서를 Fermilab/ALCF 인프라(Aurora 슈퍼컴퓨터 + Argo + Ollama)에서 검색하는 RAG 프로토타입 시스템. `multi-qa-mpnet-base-dot-v1` + FAISS로 인덱싱, 다양한 질의 유형에서 **예비 검색 정확도 ~70%** 보고. on-premise · 인증된 DUNE 공동연구자만 접근.

## 제작 배경
**기존 방법의 한계**
- DUNE 협업은 DocDB(기술 설계 보고서/TDR, 분석 노트), Indico(미팅·발표), 내부 위키 등 **다수 분산 플랫폼**에 문서 보관
- 신규 협력자가 reconstruction, simulation, data analysis, detector operations 정보를 찾는 데 시간 집약적
- 상용 LLM 직접 사용 시 **data privacy, reproducibility, network accessibility** 모두 우려
- ATLAS/CMS의 chATLAS/MITRA와 유사한 needs

**왜 DUNE-GPT가 필요했는지**
- "next-generation neutrino experiment"로서 미공개 데이터 외부 전송 금지
- Fermilab compliance 내에서 동작해야 함
- 인증된 DUNE 협력자만 접근 가능한 secure interface 필요

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 소스 수집
  ┌─ DocDB : TDR, 분석 노트, 기술 노트
  ├─ Indico : 회의 발표 자료, 미팅 노트
  └─ 내부 wiki : DUNE 운영 문서
  포맷: PDF, DOCX, TXT, PNG 등 다종
  Sensitive/restricted 콘텐츠는 협업 정책에 따라 **제외**
  → 협업 전체 접근 가능 문서만 처리

Step 2 — 전처리
  메타데이터 추출 (날짜, 저자, 문서 타입)
  token-level segmentation → embedding 준비

Step 3 — Embedding & Retrieval
  Embedding model: multi-qa-mpnet-base-dot-v1
                    (transformer encoder, scientific-text optimized)
  Vector DB: FAISS (Facebook AI Similarity Search)
  Similarity: cosine similarity

Step 4 — Response Generation (on-premise)
  LLM hosting:
  ┌─ Argonne (Argo)    : prototype 개발
  └─ Fermilab (Ollama) : 최종 배포 인프라
  RAG: retrieved snippets로 LLM 조건화
       → hallucination 위험 최소화 + grounded answer
  반환: 답변 + DUNE 내부 출처 인용

Step 5 — Deployment
  Aurora supercomputer (ALCF) → Fermilab 이전 진행
  Python backend, 경량 web interface
  인증된 DUNE 협력자만 접근 (Fermilab SSO 통합 예정)

Step 6 — 예비 평가 (Sec. 4)
  Detector specifics + reconstruction algorithms
    + physics analysis workflows
  검색 정확도 ~70% (preliminary, 정량 IR 메트릭 미시행)
```

## Input (입력)
- 자연어 질의 (web interface)
- 인증된 DUNE 협력자 자격증명

## Output (출력)
- 검색 컨텍스트 기반 답변 + DUNE 내부 출처 인용
- top-3 retrieved references (Fig. 3 frontend 표시)

## 예시 문항 (논문 본문 명시 내용)

> 본 논문은 4쪽 짧은 proceedings로, **구체적인 verbatim Q/A 예시는 본문에 포함되어 있지 않음**. 다만 시스템의 평가 범위와 인터페이스를 다음과 같이 명시:

### 📘 평가 질의 카테고리 (Sec. 4 본문 그대로)
> "Initial benchmarks demonstrate that the RAG-based system retrieves relevant documentation with high accuracy (∼70%) across **diverse query types, including detector specifics, reconstruction algorithms, and physics analysis workflows**."

### 📘 Frontend 예시 (Fig. 3 caption)
> "Frontend web interface showing a sample question, response, and the **top three retrieved references** used in response generation."
> *(구체 question 텍스트는 figure에만 표시되고 본문에 inline 인용 없음)*

### 📘 데이터 소스 범위
> "We extracted publicly accessible and internal DUNE documentation, including DUNE documents, presentations, meeting notes, technical design reports, and working group materials from DocDB and Indico."

### 📘 보안 정책 (Sec. 3 본문)
> "all operations—including embedding generation and LLM inference—are performed within the DUNE internal computing environment. **Only authenticated DUNE collaborators will be able to use this tool.**"

> 본 paper는 system overview proceedings이며, 정량 평가 + 구체 Q/A 케이스 스터디는 follow-up paper에 예정.

## 주요 결과 (Sec. 4 Preliminary)

| 항목 | 값 |
|---|---|
| **검색 정확도 (preliminary)** | ~70% (across diverse query types) |
| 임베딩 모델 | `multi-qa-mpnet-base-dot-v1` |
| 벡터 DB | FAISS |
| Generation LLM | Argo (Argonne) + Ollama (Fermilab) |
| HW (prototype) | Aurora supercomputer (ALCF, Intel Gaudi) |
| HW (deploy) | Fermilab Ollama 인프라 |
| 처리 포맷 | PDF, DOCX, TXT, PNG 등 |

> **비교 기준 없음**: MITRA(CMS, P@1=0.75 on semantic queries) · chATLAS(ATLAS, GPT-4o-mini API) 같은 BM25 baseline 정량 비교 미수행. 저자가 "preliminary" 명시.

## 한계점 (저자 명시)
- **프로토타입 단계** — 협업 전체 배포 전, 체계적 벤치마크 부재
- **민감 문서 제외**: 협업 정책으로 controlled 자료 인덱싱 불가 → 지식 커버리지 불완전
- **정량 메트릭 부재**: P@k, MRR, recall@k 등 IR metric으로 평가 미시행
- BM25 등 베이스라인 대비 정량 비교 없음
- Multi-modal content (plots, figures) 미통합 — future work
- 검색 모델과 LLM 조합의 최적화 실험 미수행
- DUNE 외 LBL/SBN/실험 외부 transferability 미검증

## 관련 정보
- **논문**: [arXiv:2601.05278](https://arxiv.org/abs/2601.05278) (v2, 13 Jan 2026)
- **발표**: 32nd International Symposium on Lepton Photon Interactions at High Energies, Madison WI, Aug 25–29, 2025
- **저자 소속**: Argonne National Laboratory (DUNE Collaboration)
- **인프라**: Aurora (ALCF) + Argo + Fermilab Ollama
- **유사 시스템**: chATLAS (ATLAS), MITRA (CMS), AI4EIC RAGS4EIC (EIC)
- **그랜트**: U.S. DOE Office of HEP + 다국 funding agencies
