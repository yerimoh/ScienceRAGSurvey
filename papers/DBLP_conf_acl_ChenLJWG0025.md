---
title: "Towards Omni-RAG: Comprehensive Retrieval-Augmented Generation for Large Language Models in Medical Applications"
bib_key: "DBLP:conf/acl/ChenLJWG0025"
year: 2025
domain: medical
type: Method
venue: ACL 2025 (Vienna, Austria), pp. 15285–15309
paper_link: https://aclanthology.org/2025.acl-long.742/
---
# Omni-RAG: Comprehensive Multi-Source RAG for Medical Applications

DBLP:conf/acl/ChenLJWG0025 | 2025 | ACL 2025 | Method | [medical] | [paper](https://aclanthology.org/2025.acl-long.742/)

**Retriever**: MedCPT-article-encoder (dense) + Qdrant 벡터 DB; BM25 (Research/Wiki); SQLite 그래프 DB (Graph 소스)
**Eval Task**: 다중소스 의료 QA (MedQA, MedMCQA, BioASQ, LiveQA, MedicationQA 등)
**Eval Metric**: 의료 QA 정확도 (Accuracy)
**Method Name**: Omni-RAG (Source Planning Optimisation, SPO)
**Modality**: Text, Graph

> ACL 2025 | 2025 | Method | medical
#### 📌 한 줄 요약
교과서·임상 가이드라인·PubMed 초록·Wikipedia·UMLS+DrugBank 그래프 등 5개 의료 지식 소스를 통합한 MedOmniKB를 구축하고, Source Planning Optimisation(SPO)으로 질의에 최적화된 소스 선택 계획을 학습시켜 소형 모델이 다중소스를 효과적으로 활용하도록 한 의료 RAG 시스템이다.

#### 🎯 개발/구축 배경
**기존 의료 RAG의 한계**
- 기존 시스템은 단일 소스(PubMed 또는 Wikipedia)에 의존하거나 여러 소스를 단순 병합하여 사용
- 질의 유형(진단, 약물 상호작용, 최신 연구 등)에 따라 최적 지식 소스가 다르지만 기존 방법은 소스 선택 전략이 없음
- 모델이 각 소스의 실제 내용에 대한 기대치와 정렬되지 않아 부적절한 소스를 선택하는 문제

**이 연구가 필요한 이유**
- 의료 AI 시스템이 신뢰할 수 있으려면 진단 추론, 임상 의사결정, 연구 지식 획득, 소비자 건강 질의 등 다양한 의료 시나리오를 포괄적으로 지원해야 함

#### 🔨 시스템 구성
**MedOmniKB — 5가지 지식 소스**
1. **Book (교과서)**: 18,182개 의료 PDF (의학, 외과, 영상의학 등) + StatPearls + MedRAG 교과서 → 27.7K 문서 / 13.1M 청크
2. **Guideline (임상 가이드라인)**: 13개 가이드라인 소스에서 45,679개 문서 (임상 진료 가이드라인)
3. **Research (PubMed)**: 2024 PubMed baseline 전체 스냅샷 → 25.3M 문서 / 48.0M 청크
4. **Wiki (Wikipedia)**: HuggingFace 영어 Wikipedia → 6.4M 문서 / 29.7M 청크
5. **Graph (UMLS + DrugBank)**: UMLS Metathesaurus 전체 서브셋 (1.7M 개념) + DrugBank 약물 정보 → 1.7M 개념 / 317.9K 정의 / 2.9M 관계 (SQLite 저장)

**Source Planning Optimisation (SPO)**
- 전문가 LLM이 각 소스에 대한 계획 탐색 (다중 쿼리 생성)
- 전문가 LLM이 각 쿼리의 검색 결과 평가 (Gold answer 지지 여부 판정)
- 소형 모델이 positive/negative 계획 쌍으로부터 SFT + DPO 학습

**검색 인프라**
- 비정형 소스 (Book, Guideline, Research, Wiki): MedCPT-article-encoder + Qdrant 벡터 DB
- 정형 소스 (Graph): SQLite 기반 직접 조회 (온라인 UMLS API 지연 회피)

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| MedOmniKB 전체 문서 수 | ~25.3M (Research 기준) |
| Graph 개념 수 | 1.7M |
| Graph 관계 수 | 2.9M |
| 평가 데이터셋 | MedQA, MedMCQA, BioASQ, LiveQA, MedicationQA 등 |
| 소형 모델의 SOTA 달성 | 다중소스 활용에서 state-of-the-art (논문 Table 기준) |

#### ⚠️ 한계점
- 5개 소스 모두 K1(문헌) 및 K2(큐레이션 DB) 소스로 구성되어 있으며, 실제 K4(개인/임상 경험) 지식은 포함하지 않음
- MedOmniKB 구축 비용이 높음 (25.3M PubMed 문서 처리)
- SPO 학습에 전문가 LLM 추론이 반복 필요하여 학습 비용 증가
- 소스 외 분포(out-of-distribution) 데이터에 대한 적응성은 추가 검증 필요

## 관련 정보
- **논문**: [ACL Anthology 2025.acl-long.742](https://aclanthology.org/2025.acl-long.742/)
- **arXiv 프리프린트**: [arXiv:2501.02460](https://arxiv.org/abs/2501.02460)
- **코드/프로젝트**: [GitHub: Jack-ZC8/Omni-RAG-Medical](https://github.com/Jack-ZC8/Omni-RAG-Medical)
- **저자 소속**: Shanghai Jiao Tong University / Fudan University / Shanghai AI Lab
- **K×O 분류**: K1.O1 (주요 문헌+가이드라인 통합) + K2.O1 (UMLS+DrugBank KG)
- **서베이 내 위치**: §Held by individuals and communities (다중소스 K1+K2 통합 패턴의 대표 사례)
