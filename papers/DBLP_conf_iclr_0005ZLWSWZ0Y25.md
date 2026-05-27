---
title: "MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models"
bib_key: "DBLP:conf/iclr/0005ZLWSWZ0Y25"
year: 2025
domain: medical
type: Method
venue: ICLR 2025
paper_link: https://arxiv.org/abs/2410.13085
---
# MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models

> ICLR | 2025 | Method | medical

## 한 줄 요약
의료 LVLM이 단일 검색기에 묶이지 않고 영상 도메인(방사선·안과·병리)을 자동 식별해 도메인별 검색기를 선택, 적응형 top-k 절삭으로 노이즈를 차단, RAG 기반 DPO 선호 학습으로 **cross-modality 오정렬**과 **ground truth 오정렬**을 동시 교정하는 다목적 RAG 시스템. 5개 데이터셋 × 3개 의료 영상 도메인에서 평균 **factual accuracy +43.8%**를 보고했다.

## 제작 배경
**기존 Med-LVLM 한계 (논문 §1, §3)**
- Med-LVLM은 텍스트 출력이 입력 이미지와 모순되는 **factual hallucination** 빈번
- 기존 의료 RAG (RULE, FactMM-RAG)는 단일 데이터셋(예: 흉부 X-ray)에만 특화 → 안과·병리로 일반화 실패
- RAG 도입 시 두 가지 새로운 오정렬 발생
  - **Cross-modality misalignment**: 모델이 이미지를 무시하고 검색 텍스트만 베끼는 "Copy-Reference" 현상
  - **Overall misalignment**: 검색 결과가 잘못된 경우에도 그대로 따르는 "Over-Reliance" 현상

**왜 필요한가**
- 진단 오류는 환자 안전과 직결 → 신뢰성이 핵심
- 다양한 영상 모달리티를 단일 시스템에서 운용해야 임상 적용 가능
- 저자 인용: "MMed-RAG can achieve an average improvement of **43.8%** in the factual accuracy of Med-LVLMs" (Abstract)
- "achieving improvements of **18.5%** and **69.1%** on Medical VQA and report generation tasks, respectively" (§1)

## 시스템 아키텍처
```
                    [Medical Image (xv) + Clinical Query (xt)]
                                    │
                                    ▼
                  ┌─────────────────────────────────┐
                  │   ① Domain-Aware Retrieval      │
                  │   ─────────────────────────     │
                  │   Domain Identification         │
                  │   (BiomedCLIP / ResNet-50 +     │
                  │    BioClinicalBERT, InfoNCE)    │
                  │       │                         │
                  │       ▼                         │
                  │   Domain label ∈ {Radiology,    │
                  │     Pathology, Ophthalmology}   │
                  │       │                         │
                  │       ▼                         │
                  │   Domain-specific Retriever     │
                  │   (각 도메인별 학습된 별도 모델)   │
                  └────────────┬────────────────────┘
                               │
                  ┌────────────▼────────────────────┐
                  │   ② Adaptive Retrieved Context  │
                  │      Selection                  │
                  │   ─────────────────────────     │
                  │   Top-k 결과의 유사도 점수 비율  │
                  │   log(S_i / S_{i+1}) 분석       │
                  │   → 점수 급락 직전에서 k 절삭   │
                  │     (Gap Statistic 기반)        │
                  └────────────┬────────────────────┘
                               │
                  ┌────────────▼────────────────────┐
                  │   ③ Med-LVLM + RAG-PT (DPO)     │
                  │   ─────────────────────────     │
                  │   3-stage preference data:      │
                  │   ①Direct-Copy-Homework→교정    │
                  │   ②Cannot-Solve-by-Self→교정    │
                  │   ③Wrong-Homework-Interference  │
                  │       →교정                     │
                  └────────────┬────────────────────┘
                               │
                               ▼
                        [Factual answer]
```

## 핵심 모듈 상세 설명
### Domain-Aware Retrieval
- 단일 범용 retriever 대신 도메인별 expert retriever 배치 (MoE 유사하지만 도메인 라우팅)
- 이미지를 먼저 도메인 식별 모듈에 통과 → 적절한 retriever만 호출
- 각 retriever는 ResNet-50 (vision) + BioClinicalBERT (text)을 **InfoNCE contrastive loss**로 학습
- Recall@1, R@5에서 단일 retriever 대비 큰 폭의 우위 (Table 20)

### Adaptive Truncation
- 검색 결과 순위가 깊어질수록 유사도 점수가 감소하는 추세를 활용
- `log(S_i / S_{i+1})`이 특정 임계치를 넘으면 그 이후 결과는 노이즈로 간주, 절삭
- 고정 k 대신 query별로 다른 k 선택 → 노이즈 삽입 차단

### RAG-Based Preference Tuning (RAG-PT)
3가지 preference pair 설계 (논문 Figure 1):
1. **"Think it by Self"** — 무관 이미지 + 정답 검색 텍스트로 정답 출력 = dispreferred (이미지를 보지 않고 베껴서 맞은 케이스 → 부정 강화)
2. **"Learn How to Copy"** — 자체 추론으론 못 풀고 검색 정보로 정답 출력 = preferred (검색을 잘 활용한 케이스 → 긍정 강화)
3. **"Avoid Wrong Homework"** — 잘못된 검색에도 원본 이미지로 정답 = preferred (검색 노이즈 방해를 이겨낸 케이스 → 긍정 강화)

DPO 손실:
> L_DPO(πθ; πref) = −E[log σ(α log(πθ(yw|x)/πref(yw|x)) − α log(πθ(yl|x)/πref(yl|x)))]  (Eq. 1)

## Input/Output
**Input**
- xv: 의료 영상 (chest X-ray / retinal photo / pathology slide / OCT)
- xt: 임상 질의 (예: "Is there any focal airspace opacity present?")

**Output**
- Yes/No 진단, 자유 텍스트 보고서 (report generation), 또는 multi-choice 답변

## 예시 사례
### 예시 ① — Chest X-ray VQA (논문 Figure 4, 좌)
> **Question**: "Can focal airspace consolidation be seen on the image?"
>
> **Reference (Ground Truth)**:
> > "No, focal airspace consolidation cannot be seen on the image."
>
> **LLaVA-Med-1.5 (baseline) output**:
> > "Yes, there seems to be a focal airspace consolidation. The heart is normal in size… There appears to be a focal airspace consolidation on the right side of the lung…"
>
> **MMed-RAG (Ours) output**:
> > "No, focal airspace consolidation cannot be seen on the image."
>
> **해석**: LLaVA-Med가 무관한 "right side of the lung" 정보를 환각으로 추가 생성 → MMed-RAG는 이미지에 충실하게 No 답변. Attention map 분석 결과 MMed-RAG가 폐 영역(빨간 박스)에 강화된 attention을 부여함.

### 예시 ② — 동작 흐름 (Figure 1)
> **Question**: "Is there any focal airspace opacity present?"
>
> 1) 입력 흉부 X-ray → Domain Identification → "Radiology"
> 2) Radiology Retriever → IU-Xray report corpus에서 Top-k reports
> 3) Adaptive-k: 유사도 그래프 분석 후 k=3개만 유지
> 4) Med-LVLM이 reports + image 결합 → final answer

## 주요 평가 결과
**Table 1 — Medical VQA Accuracy (LLaVA-Med-1.5 backbone, %)**
| Method | IU-Xray | MIMIC-CXR | Harvard-FairVLMed | Quilt-1M | PMC-OA |
|---|---|---|---|---|---|
| LLaVA-Med-1.5 (base) | 75.47 | 75.79 | 63.03 | 62.80 | 59.28 |
| + Greedy decoding | 76.88 | 78.32 | 82.54 | 64.72 | 58.61 |
| + DoLa | 78.00 | 81.35 | 76.87 | 63.47 | 57.71 |
| + OPERA | 70.59 | 69.34 | 71.41 | 60.51 | 55.32 |
| + VCD | 68.99 | 70.89 | 65.88 | 61.43 | 55.10 |
| + MedDr | 83.33 | 55.16 | 70.17 | 68.15 | 59.97 |
| + FactMM-RAG | 84.51 | 77.58 | 83.67 | 69.25 | 60.49 |
| + RULE | 87.84 | 83.92 | 87.12 | 68.97 | 61.41 |
| **+ MMed-RAG (Ours)** | **89.54** | 83.57 | **87.94** | **72.95** | **64.54** |

**Table 1 — F1 (선택)**
| Method | IU-Xray | MIMIC-CXR | PMC-OA |
|---|---|---|---|
| LLaVA-Med-1.5 | 64.04 | 80.49 | 71.98 |
| RULE | 78.00 | 87.49 | 70.36 |
| **MMed-RAG** | **80.72** | **88.49** | **73.09** |

**기여 요약 (Abstract + §1)**
- 평균 factual accuracy 향상: **+43.8%**
- Medical VQA에서 base Med-LVLM 대비 **+18.5%**
- Report generation에서 base 대비 **+69.1%**
- Table 14: Copy-Reference Rate와 Over-Reliance Rate 모두 유의미 감소 (정량 측정 첫 시도)

## 핵심 기여
1. **Versatile multimodal RAG** — 단일 시스템으로 radiology/pathology/ophthalmology 전 도메인 커버
2. **이론적 보장** — Cross-modality와 overall misalignment 완화에 대한 mild assumption 기반 증명 (§4)
3. **Copy-Reference / Over-Reliance 진단 지표 도입** — RAG가 가져오는 부작용을 수치화

## 한계점
- 도메인이 늘어날수록 도메인별 retriever 학습 비용 선형 증가, "단일 범용 retriever"는 여전히 실현 어려움 (논문 §6 결론)
- Base Med-LVLM이 few-shot 학습 능력이 약하면 RAG-PT 효과 제한
- Domain Identification 단계 오분류 시 잘못된 retriever 선택 → cascade error
- DPO 학습용 preference pair 구성에 GPT-4 등 외부 LLM 필요 (Table 9에 prompt)

## 관련 정보
- **논문**: [ICLR 2025](https://openreview.net/forum?id=...)
- **arXiv**: [arXiv:2410.13085](https://arxiv.org/abs/2410.13085)
- **GitHub**: [https://github.com/richard-peng-xia/MMed-RAG](https://github.com/richard-peng-xia/MMed-RAG)
- **저자**: UNC-Chapel Hill, Brown, CMU, Rutgers, Washington, Stanford (Peng Xia, Kangyu Zhu, Haoran Li, Tianze Wang, Weijia Shi, Sheng Wang, Linjun Zhang, James Zou, Huaxiu Yao)
- **평가 데이터셋**: IU-Xray, MIMIC-CXR (radiology), Harvard-FairVLMed (ophthalmology, OCT), Quilt-1M (pathology), PMC-OA (pathology)
- **K×O 분류**: K1.O1 (의료 영상 corpus 검색) — 검색 대상이 텍스트가 아닌 image-report pair
