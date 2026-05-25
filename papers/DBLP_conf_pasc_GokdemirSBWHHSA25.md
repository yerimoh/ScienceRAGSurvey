---
title: "HiPerRAG: High-Performance Retrieval Augmented Generation for Scientific Insights"
bib_key: "DBLP:conf/pasc/GokdemirSBWHHSA25"
year: 2025
domain: general
type: Method
venue: PASC 2025
paper_link: https://doi.org/10.1145/3732775.3733586
---
# HiPerRAG: High-Performance Retrieval Augmented Generation for Scientific Insights

DBLP:conf/pasc/GokdemirSBWHHSA25 | 2025 | PASC 2025 | Method | [general] | [paper](https://doi.org/10.1145/3732775.3733586)

**Retriever**: ColTrast (query-aware encoder fine-tuning, contrastive + late-interaction)
**Eval Task**: SciQ, PubMedQA, ProteinInteractionQA, ProteinFunctionQA, BioSynthQP
**Eval Metric**: Accuracy (SciQ: 90%, PubMedQA: 76%)
**Method Name**: HiPerRAG
**Modality**: Text, Multimodal documents (Oreo: high-throughput multimodal parsing)

> PASC 2025 | 2025 | Method | general (cross-domain science)
#### 📌 한 줄 요약
HPC(고성능 컴퓨팅)를 활용하여 360만 편 이상의 과학 논문을 인덱싱하고, Oreo 멀티모달 문서 파싱 모델과 ColTrast 쿼리 인식 인코더 파인튜닝으로 SciQ 90%, PubMedQA 76% 정확도를 달성하며 GPT-4 및 도메인 특화 모델을 능가하는 대규모 과학 RAG 워크플로이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- RAG를 수백만 편 논문으로 확장하면 문서 파싱 및 임베딩 계산 비용이 급증
- 과학 콘텐츠의 미묘한 의미론(수식, 그림, 표)을 표현 정렬하는 알고리즘 복잡성 높음

**이 시스템이 필요한 이유**
- 과학 출판물이 지수적으로 증가하는 환경에서 유사 발견 방지 및 학제간 협력 촉진을 위한 대규모 RAG 필요
- PubMed에서 연간 169만 편, 분당 3편 이상 등록되는 의생명 논문 처리 인프라 필요

#### 🔨 시스템 구성
**Oreo**: 멀티모달 문서 파싱 고처리량 모델 (텍스트, 그림, 표, 수식 통합 처리). **ColTrast**: 대조 학습과 late-interaction 기법을 결합한 쿼리 인식 인코더 파인튜닝 알고리즘 (다양한 모델 크기, 손실 함수 비교). Polaris, Sunspot, Frontier 수천 대 GPU로 분산 확장. HPC 기반 warmstart 최적화로 효율적 인덱싱.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 인덱싱 규모 | 3.6M 이상 과학 논문 |
| SciQ 정확도 | 90% |
| PubMedQA 정확도 | 76% |
| 비교 대상 능가 | PubMedGPT (도메인 특화), GPT-4 (상용) |
| 신규 벤치마크 | ProteinInteractionQA, ProteinFunctionQA, BioSynthQP |
| HPC 플랫폼 | Polaris, Sunspot, Frontier (수천 GPU) |

#### ⚠️ 한계점
- 수천 대 GPU 인프라가 필요하여 일반 연구자의 접근성 제한
- Oreo 파싱 정확도는 문서 레이아웃 복잡도에 따라 달라짐
- 학제간 의미론 정렬(cross-domain semantic alignment)의 어려움 남아 있음

## 관련 정보
- **논문 (ACM DL)**: [https://doi.org/10.1145/3732775.3733586](https://doi.org/10.1145/3732775.3733586)
- **arXiv preprint**: [https://arxiv.org/abs/2505.04846](https://arxiv.org/abs/2505.04846)
