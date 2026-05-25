---
title: "AlzheimerRAG: Multimodal Retrieval-Augmented Generation for Clinical Use Cases"
bib_key: "DBLP:journals/make/LahiriH25"
year: 2025
domain: medical
type: Method
venue: Mach. Learn. Knowl. Extr.
paper_link: https://doi.org/10.3390/make7030089
---
# AlzheimerRAG: Multimodal Retrieval-Augmented Generation for Clinical Use Cases

DBLP:journals/make/LahiriH25 | 2025 | Mach. Learn. Knowl. Extr. | Method | [medical] | [paper](https://doi.org/10.3390/make7030089)

**Retriever**: Dense (FAISS vector store, cross-modal attention fusion)
**Eval Task**: BioASQ, PubMedQA (clinical Alzheimer's case studies)
**Eval Metric**: Retrieval accuracy, hallucination rate, human comparison
**Method Name**: AlzheimerRAG
**Modality**: Text, Image (PubMed articles + extracted figures/ADNI)

> Mach. Learn. Knowl. Extr. | 2025 | Method | medical
#### 📌 한 줄 요약
PubMed 논문의 텍스트와 시각 자료를 cross-modal attention으로 융합하여 알츠하이머 임상 질문에 답하는 멀티모달 RAG 시스템으로, BioASQ 및 PubMedQA 벤치마크 대비 개선된 성능과 인간 수준의 정확도 및 낮은 환각률을 달성하였다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 텍스트 전용 RAG는 의학 문헌에 포함된 그림·표 등 시각 정보를 활용하지 못함
- Alzheimer's 도메인은 PubMed 내 그림, 스캔, ADNI 이미지와 같은 멀티모달 데이터가 풍부하지만 기존 시스템은 이를 통합하지 않음

**이 시스템이 필요한 이유**
- 알츠하이머 임상 활용 사례에서 텍스트+이미지 통합 검색 및 생성이 필요함
- 환각률 최소화 및 인간 비열등(non-inferior) 정확도 달성을 목표로 함

#### 🔨 시스템 구성
PubMed 논문에서 텍스트와 이미지를 인덱싱하여 FAISS 벡터 스토어에 저장하고, 쿼리 시 cross-modal attention fusion 기법으로 텍스트 및 시각 문서를 통합 검색한다. LLM을 통해 검색된 멀티모달 컨텍스트 기반으로 답변을 생성하며, 알츠하이머 임상 시나리오에 특화된 케이스 스터디를 제공한다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 평가 벤치마크 | BioASQ, PubMedQA |
| 정확도 | 인간 수준 비열등(non-inferior) |
| 환각률 | 낮음 (low hallucination rate) |
| 모달리티 | Text + Image (PubMed + ADNI) |

#### ⚠️ 한계점
- Alzheimer 단일 도메인에 특화되어 있어 일반화 범위 제한
- 대규모 이미지 인덱싱의 계산 비용 증가
- 정량적 성능 수치(F1, Accuracy)가 논문 초록 수준에서 구체적으로 공개되지 않음

## 관련 정보
- **논문**: [https://doi.org/10.3390/make7030089](https://doi.org/10.3390/make7030089)
- **arXiv preprint**: [arXiv:2412.16701](https://arxiv.org/abs/2412.16701)
