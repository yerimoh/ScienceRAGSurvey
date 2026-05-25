---
title: "Large Language Model Integration for Knowledge Retrieval and Interaction for the DUNE Experiment"
bib_key: "rafique2025large"
year: 2025
domain: physics
type: Method
venue: arXiv (Lepton Photon 2025, Argonne/Fermilab)
paper_link: https://arxiv.org/abs/2601.05278
---
# DUNE-GPT: LLM Integration for Knowledge Retrieval in the DUNE Experiment

rafique2025large | 2025 | arXiv | Method | [physics] | [paper](https://arxiv.org/abs/2601.05278)

**Retriever**: Dense embedding (multi-qa-mpnet-base-dot-v1) + FAISS 벡터 DB, cosine similarity
**Eval Task**: DUNE 내부 문서 질의응답 (detector, reconstruction, physics analysis)
**Eval Metric**: Retrieval accuracy (~70% across diverse query types, preliminary)
**Method Name**: DUNE-GPT
**Modality**: Text

> arXiv | 2025 | Method | physics
#### 📌 한 줄 요약
Deep Underground Neutrino Experiment(DUNE) 협업의 DocDB, Indico, 내부 위키에 산재된 방대한 실험 문서를 대상으로 Fermilab 인프라에서 on-premise RAG를 구현한 프로토타입 시스템으로, 협업 구성원이 자연어로 실험 특화 지식을 조회할 수 있게 한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- DUNE 협업은 기술 설계 보고서(TDR), 분석 노트, 발표 자료, 회의록을 DocDB, Indico, 내부 위키에 분산 보관
- 신입 공동연구자나 다른 워킹 그룹 전문가가 재구성 알고리즘이나 검출기 운영 세부사항을 검색하는 데 많은 시간 소모
- 상업 LLM API 사용은 Fermilab의 데이터 보안 및 재현성 요구를 충족하지 못함

**DUNE-GPT가 필요한 이유**
- 협업 전체 생산성 및 신규 참여자 온보딩 효율화
- 분산된 DUNE 문서 생태계를 단일 자연어 인터페이스로 통합

#### 🔨 시스템 구성
**데이터 소스**
- DocDB: DUNE 내부 문서, 기술 노트, TDR
- Indico: 회의 발표 자료, 미팅 노트
- 내부 위키 문서
- 공개 접근 가능한 DUNE 문서 (협업 정책에 따라 민감 문서 제외)

**임베딩 및 검색 레이어**
- 다양한 형식(PDF, DOCX, TXT, PNG 등) 처리 + 메타데이터 추출 + 토큰 분할
- 임베딩 모델: multi-qa-mpnet-base-dot-v1 (과학 텍스트 최적화)
- 벡터 DB: FAISS (Facebook AI Similarity Search)
- 검색: cosine similarity 기반

**LLM 통합**
- Argonne 슈퍼컴퓨터(Aurora/Argo) 및 Fermilab(Ollama) 내부 호스팅 LLM
- RAG 방식으로 검색된 컨텍스트를 LLM에 조건화하여 응답 생성
- 인증된 DUNE 공동연구자만 접근 가능

**인터페이스**
- 경량 웹 인터페이스: 자연어 질의 → 포맷된 응답 + 문서 출처 인용
- Aurora (Argonne Leadership Computing Facility)에서 초기 개발 후 Fermilab 인프라로 이전 예정

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 예비 검색 정확도 | ~70% (다양한 질의 유형에서) |
| 처리 문서 형식 | PDF, DOCX, TXT, PNG 등 |
| 임베딩 모델 | multi-qa-mpnet-base-dot-v1 |
| 벡터 DB | FAISS |

> **주의**: "preliminary results" 단계이며, P@k/MRR 등 정밀 메트릭 기반 체계적 평가는 향후 과제로 명시됨.

#### ⚠️ 한계점
- 프로토타입 단계: 협업 전체 배포 전 단계이며 체계적 벤치마크 미수행
- 민감/제한 문서는 협업 정책에 따라 인덱싱 제외 (지식 커버리지 불완전)
- ATLAS chATLAS 등 유사 시스템과 달리 BM25 대비 정량 비교 실험이 아직 미수행
- 검출기 운영 로그, 코드 문서 등 다양한 형식 확장 계획 중

## 관련 정보
- **논문**: [arXiv:2601.05278](https://arxiv.org/abs/2601.05278)
- **수락**: 32nd International Symposium on Lepton Photon Interactions at High Energies, Madison WI, Aug 2025
- **저자 소속**: Argonne National Laboratory (DUNE Collaboration)
- **K4 분류**: K4.O1 — 기관 내부 문서(DUNE DocDB + Indico)에 대한 RAG 시스템
