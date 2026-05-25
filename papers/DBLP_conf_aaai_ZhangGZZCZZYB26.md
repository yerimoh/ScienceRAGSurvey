---
title: "Patho-AgenticRAG: Towards Multimodal Agentic Retrieval-Augmented Generation for Pathology VLMs via Reinforcement Learning"
bib_key: "DBLP:conf/aaai/ZhangGZZCZZYB26"
year: 2026
domain: medical
type: Method
venue: AAAI 2026
paper_link: https://arxiv.org/abs/2508.02258
---
# Patho-AgenticRAG: Towards Multimodal Agentic Retrieval-Augmented Generation for Pathology VLMs via Reinforcement Learning

DBLP:conf/aaai/ZhangGZZCZZYB26 | 2026 | AAAI 2026 | Method | [medical] | [paper](https://arxiv.org/abs/2508.02258)

**DB**: 병리학 교과서 기반 page-level 임베딩 데이터베이스 (authoritative pathology textbooks)
**DB Open/Private**: Open (GitHub 공개)
**Modality**: ['Text', 'Image']
**Retriever**: Joint text-image retrieval (page-level embedding from pathology textbooks)
**Eval Task**: Pathology multiple-choice diagnosis, pathology VQA
**Eval Metric**: Accuracy
**Method Name**: Patho-AgenticRAG

> AAAI 2026 | 2026 | Method | medical
#### 한 줄 요약
병리 VLM의 환각 문제를 해결하기 위해 권위 있는 병리학 교과서의 페이지 단위 임베딩 DB를 구축하고, 텍스트+이미지 공동 검색 및 강화학습 기반 에이전틱 추론을 결합한 멀티모달 RAG 시스템이다.

#### 개발/구축 배경
**기존 인프라의 한계**
- 병리 이미지는 초고해상도·복잡한 조직 구조·세밀한 임상 의미로 인해 기존 VLM에서 환각이 빈번히 발생
- 기존 RAG 방법은 텍스트 기반 지식 베이스에 의존, 병리 진단에 필수적인 시각 정보 활용 불가
- 단순 텍스트 검색은 병리 이미지의 시각적 맥락(tissue morphology 등)을 포착하지 못함

**이 시스템이 필요한 이유**
- 병리학 교과서 페이지 단위 검색으로 텍스트+이미지를 동시에 제공 → 시각 진단 단서 보존
- 강화학습으로 다단계 검색 및 추론(task decomposition, multi-turn search) 능력 강화

#### 시스템 구성
- **지식 소스**: 권위 있는 병리학 교과서에서 page-level 임베딩으로 DB 구축 (텍스트+이미지 공존 페이지)
- **검색 방식**: joint text-image search — 쿼리 텍스트+이미지 시각 단서를 동시에 검색
- **에이전틱 구성**: 추론·태스크 분해·multi-turn 검색 상호작용 지원 (강화학습 기반)
- **K×O 분류**: K2.O1 (병리학 교과서 = 큐레이션 지식 베이스 + 이미지 모달리티)

#### 주요 통계 (논문/abstract 기준)
| 항목 | 수치 |
|---|---|
| 지식 소스 | 병리학 교과서 page-level 임베딩 DB (규모 미기재) |
| 검색 모달리티 | Text + Image (joint) |
| 평가 태스크 | Pathology multiple-choice diagnosis, visual QA |
| 성능 | 기존 멀티모달 모델 대비 유의미하게 향상 (abstract: "significantly outperforms") |
| arXiv 제출 | 2025년 8월 (arXiv:2508.02258) |

#### 한계점
- 병리학 도메인에 특화 → 방사선·안과 등 타 의료 모달리티로의 일반화 미검증
- 교과서 기반 DB는 최신 임상 가이드라인이나 연구 문헌 미반영
- 강화학습 기반 에이전틱 추론의 훈련 비용 높음

## 관련 정보
- **논문 (arXiv)**: [arXiv:2508.02258](https://arxiv.org/abs/2508.02258)
- **GitHub**: [Patho-AgenticRAG](https://github.com/Wenchuan-Zhang/Patho-AgenticRAG)
- **주의**: main.tex Cross-Source 섹션에서 "texts derived from PubMed with medical images"라고 기술되어 있으나, 실제 지식 소스는 PubMed가 아닌 병리학 교과서 (abstract 확인, arXiv:2508.02258)
