---
title: "MMed-RAG: Versatile Multimodal RAG System for Medical VLMs"
bib_key: "DBLP:conf/iclr/0005ZLWSWZ0Y25"
year: 2025
domain: medical
type: Method
venue: ICLR 2025
paper_link: https://arxiv.org/abs/2410.13085
---
# MMed-RAG: Versatile Multimodal RAG System for Medical VLMs

> ICLR | 2025 | Method | medical
## 📌 한 줄 요약
의료 대형 시각-언어 모델(Med-LVLM)에 RAG를 결합할 때 발생하는 모달리티 간 오정렬 및 정보 과의존성(환각) 문제를 해결하기 위해 고안된 다목적 멀티모달 RAG 시스템.
## 🎯 연구 배경 및 동기
- **기존 방법의 한계점**: 기존 Med-LVLM 모델들은 시각 정보와 맞지 않는 사실적 환각(Factual Hallucination) 현상을 빈번히 겪음. RAG를 도입하여 이 문제를 해결하려 했으나, 기존의 RAG 기법은 특정 데이터셋에 국한되어 다양한 의료 도메인에 일반화되지 않으며, 검색된 텍스트 정보가 주어지면 시각(이미지) 정보를 무시해 버리는 '교차 모달리티 오정렬(Cross-Modality Misalignment)' 및 외부 노이즈 정보에 그대로 의존해 버리는 전체 정렬 오류가 발생함.
- **이 연구가 필요한 이유**: 다양한 영상 소스(방사선, 병리, 안과)를 포괄적으로 지원하면서도, RAG의 도입이 기존 모델의 시각 지능을 해치지 않도록 신뢰성과 사실성을 보장하는 고도화된 RAG 튜닝 기법이 필요함.
## 🏗️ 시스템 아키텍처
[image]
1. **Domain-Aware Retrieval**: 입력된 의료 이미지를 Domain Identification 모듈(BiomedCLIP)에 통과시켜 도메인을 예측한 뒤, 해당 도메인에 맞는 특화 검색기(Radiology, Pathology 등)를 선별적으로 호출.
2. **Adaptive Retrieved Context Selection**: 검색된 top-k 문서의 유사도 점수 하락률을 분석하여 쓸모없는 정보(Noise)가 포함되기 직전에 k값을 잘라내는 동적 필터링 수행.
3. **RAG-Based Preference Fine-Tuning (RAG-PT)**: DPO(Direct Preference Optimization) 기반의 선호도 파인튜닝을 진행. 시각 정보를 무시한 채 텍스트 검색 결과만 베끼는 습관을 교정하고, 내부 지식과 검색 지식의 균형을 맞춤.
## 🔑 핵심 모듈 상세 설명
- **Domain-Aware Mechanism**: 일반 범용 검색기를 훈련하는 대신, ResNet-50과 bio-BioClinicalBERT를 대조 학습(Contrastive Learning, InfoNCE Loss) 시킨 도메인별 검색기(전문가)를 모듈화하여 배치.
- **Adaptive Truncation (적응형 절삭)**: Gap Statistic 기법에서 영감을 받아, `log(S_i / S_{i+1})` (S는 유사도 점수)가 특정 임계치를 초과하면 그 이후의 검색 결과를 버림으로써 노이즈 삽입을 차단.
- **RAG-PT Preference Pairs 설계 원리**:
	- *교차 모달리티 정렬*: 고도로 왜곡된 가짜 이미지를 넣고 검색된 정답 텍스트를 함께 주었을 때 모델이 정답을 출력하는 것을 '비선호(Dispreferred)'로 지정. 원본 이미지로 제대로 답을 추론한 것을 '선호(Preferred)'로 설정해 시각 지표를 우선시하도록 훈련.
	- *전체 정렬*: 검색 정보의 방해를 피하기 위해, 잘못된 검색 결과가 있더라도 원본 이미지로 정확히 진단한 사례를 긍정 강화.
## 🧪 실험 및 평가
- **평가 태스크**: Medical VQA (MIMIC-CXR, IU-Xray, Harvard-FairVLMed, PMC-OA, Quilt-1M), Report Generation (병리 제외 3개 데이터셋)
- **주요 결과 (VQA Accuracy)**:
| 모델 | IU-Xray | MIMIC-CXR | Harvard-FairVLMed | PMC-OA | Quilt-1M |
| LLaVA-Med-1.5 | 75.47 | 75.79 | 63.03 | 59.28 | 62.80 |
| MedDr (Baseline) | 83.33 | 55.16 | 80.72 | 57.01 | 68.15 |
| RULE (Baseline) | 84.51 | 81.86 | 87.49 | 70.36 | 68.97 |
| **MMed-RAG (Ours)** | **89.54** | **88.49** | **87.94** | **64.54** | **72.95** |

## 💡 핵심 기여
- 검색을 위해 다양한 모달리티를 강제로 하나의 범용 검색기에 구겨 넣는 대신, 가벼운 도메인 식별기를 앞단에 배치하여 유연하고 확장 가능한 멀티모달 검색 구조 제시.
- RAG 도입으로 인해 오히려 발생할 수 있는 '검색 결과 맹신(Copy-Reference)'과 '오답 의존(Over-Reliance)' 부작용을 수학적으로 증명하고 DPO로 실질적 개선 달성.
## ⚠️ 한계점
- 여러 도메인이 혼합될수록 모든 것을 커버하는 '단일 범용 검색기' 훈련은 사실상 매우 어려움(MoE 방식 한계 확인).
- Base LLM(LLaVA-Med)이 Pre-training 단계에서 few-shot 학습 능력을 제대로 갖추지 못한 경우, RAG를 결합하더라도 Few-shot 환경에서 성능 하락이 두드러짐.
## 🔗 관련 연구 및 관련 정보
- GitHub: [https://github.com/richard-peng-xia/MMed-RAG](https://github.com/richard-peng-xia/MMed-RAG)
- arXiv: [arXiv:2410.13085](https://arxiv.org/abs/2410.13085)
- 평가 벤치마크: MIMIC-CXR, IU-Xray, Harvard-FairVLMed, PMC-OA, Quilt-1M (5개 데이터셋, radiology/ophthalmology/pathology)
- 핵심 결과: **의료 VLM의 사실적 정확도 평균 43.8% 향상** (abstract 확인, arXiv:2410.13085)
- 지식소스: PubMed 텍스트가 아닌 도메인별 의료 이미지 데이터셋(방사선/안과/병리)에서 직접 검색
