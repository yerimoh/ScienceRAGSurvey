---
title: "BioRAG: A RAG-LLM Framework for Biological Question Reasoning"
bib_key: "DBLP:journals/corr/abs-2408-01107"
year: 2024
domain: bio, medical
type: Method
venue: arXiv 2024
paper_link: https://arxiv.org/abs/2408.01107
---
# BioRAG: A RAG-LLM Framework for Biological Question Reasoning

DBLP:journals/corr/abs-2408-01107 | 2024 | arXiv 2024 | Method | [bio, medical] | [paper](https://arxiv.org/abs/2408.01107)

**Retriever**: Specialized dense embedding model (domain fine-tuned), PubMed local + NCBI databases + web search engine
**Eval Task**: GeneTuring (7 tasks: gene alias, name conversion, location, SNP, gene-disease association, protein-coding), MedMCQA, Medical Genetics, College Biology, College Medicine
**Eval Metric**: Accuracy (exact match for nomenclature/genomics; recall for gene-disease; yes/no accuracy for others)
**Method Name**: BioRAG
**Modality**: Text (22 million scientific papers + NCBI databases)

> arXiv 2024 | 2024 | Method | bio · medical
#### 📌 한 줄 요약
2,200만 편의 생명과학 논문을 인덱싱하고 도메인 특화 임베딩 모델, 지식 계층 기반 벡터 검색, 반복적 검색(iterative retrieval)과 웹 검색 엔진을 결합하여 GeneTuring, MedMCQA 등 복수의 생명과학 QA 태스크에서 기존 RAG 프레임워크를 능가하는 생물학 질의응답 시스템이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 생명과학은 빠른 발견 속도와 복잡한 지식 엔티티 간 상호작용으로 포괄적 지식 창고 유지가 어려움
- 파인튜닝된 도메인 LLM(BioMistral, PMC-Llama)은 일반화 능력이 제한적
- 기존 과학 RAG 프레임워크(GeneGPT)는 특정 태스크에 과적합

**이 시스템이 필요한 이유**
- 학제간 융합 연구 지원을 위한 포괄적 생명과학 지식 창고 및 정확한 정보 검색 시스템 필요
- 최신 정보가 필요한 쿼리에서 단계적 추론(step-by-step reasoning)이 가능한 시스템 필요

#### 🔨 시스템 구성
2,200만 편 논문 파싱·인덱싱·분할 → 도메인 특화 임베딩 모델 훈련 (AdamW, 2 epochs) → 도메인 특화 지식 계층을 활용한 벡터 검색 강화 → 최신 정보 필요 쿼리는 질문 분해 + 반복 검색(최대 15회) + 웹 검색 엔진 통합. Llama3-70B를 기본 LLM으로 사용하며, 생물 DB 10개, 웹 10개, 로컬 PubMed 4개를 검색한다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 지식 베이스 규모 | 22백만 편 생명과학 논문 |
| 평가 데이터셋 | GeneTuring (7 tasks), MedMCQA, Medical Genetics, College Biology, College Medicine |
| Gene_alias 정확도 | 100% (BioRAG M2) |
| SNP_location 정확도 | 100% (BioRAG D2~M2) |
| Gene_disease_association | 86% (BioRAG M2) — 가장 어려운 태스크 |
| 기준선 대비 | BioLLM, GPT-3.5, SciRAG (NewBing) 모두 능가 |

#### ⚠️ 한계점
- 최대 15회 반복 내 답변 없으면 현재 오답 출력 (고정 종료 기준)
- 22M 논문 인덱싱 및 임베딩 모델 훈련에 상당한 계산 비용
- GeneGPT는 특정 태스크 특화로 BioRAG와 직접 비교 부적합

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2408.01107](https://arxiv.org/abs/2408.01107)
