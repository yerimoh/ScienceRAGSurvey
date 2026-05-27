---
notion_id: 355f2dcd-4912-8153-8151-d3b4e52f86da
title: Rationale-Guided Retrieval Augmented Generation for Medical Question Answering
bib_key: DBLP:conf/naacl/SohnPYPHSKK25
year: 2025
domain: medical
type: Method
venue: NAACL 2025 (Long Paper)
paper_link: https://aclanthology.org/2025.naacl-long.635/
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Rationale-Guided Retrieval Augmented Generation for Medical Question Answering (RAG²)

> NAACL | 2025 | Method | medical

## 한 줄 요약
LLM이 먼저 chain-of-thought rationale을 생성해 이를 검색 쿼리로 활용하고, **PubMed/PMC/Textbooks/Clinical Guidelines** 4개 코퍼스에서 균등 검색하며, perplexity 변화량으로 자동 라벨링된 데이터로 Flan-T5-large 770M 필터링 모델을 학습해 정보성 스니펫만 LLM에 전달. 단일 단계 검색만 사용하면서도 MedQA·MedMCQA·MMLU-Med에서 Llama-3-8B 평균 **+6.1%**, GPT-4o **+0.9%** 향상.

## 제작 배경
**기존 의료 RAG의 한계**
- 의료 쿼리에 환자 정보 등 광범위한 맥락을 포함하면 검색기가 혼란, 너무 짧으면 암묵적 의료 지식 의존 필요
- MedCPT 같은 PubMed-편향 retriever는 임상 가이드라인/교과서 소외 → retriever bias
- Self-BioRAG는 LLM 전체 파인튜닝 필요 (Llama-2 7B/13B 학습) → 학습 비용 큼
- Adaptive-RAG는 정답/오답만 라벨로 사용 → 문서 유용성의 미세 신호 무시

**왜 필요한가**
- 단일 패스 + 770M 소형 필터링 모델만으로 SOTA에 근접하는 효율적 의료 RAG가 필요
- 의료 도메인은 어노테이션 비용이 매우 높으므로 perplexity 차이로 자동 라벨링하는 방법이 매력적
- 저자 인용: "These rationale-based queries help identify key... and they refine poorly targeted retrieval results" (§1)

## 시스템 아키텍처 (논문 Figure 1)
```
                       [Initial Query x]
                            │
                            ▼
        ┌──────────────────────────────────────┐
        │  ① Rationale-Based Query Formulation │
        │  ────────────────────────────────    │
        │  Base LLM (Llama-3-8B / Meerkat-7B / │
        │            GPT-4o) at temp=0         │
        │  Chain-of-Thought로 rationale 생성   │
        │  → rationale 텍스트 자체가 새 쿼리   │
        │    (초기 쿼리 미포함 — token 한계)   │
        └──────────────┬───────────────────────┘
                       │
        ┌──────────────▼───────────────────────┐
        │  ② Balanced Retrieval                │
        │  ────────────────────────────────    │
        │  4개 corpus 각각에서 동일 비율 검색  │
        │  - PubMed (대형, MedCPT 학습 소스)   │
        │  - PMC (대형, open access)           │
        │  - Medical Textbooks (소형, 전문)    │
        │  - Clinical Guidelines (소형, 최신)  │
        │  → MedCPT cross-encoder가 초기 쿼리  │
        │    기준 재순위                       │
        └──────────────┬───────────────────────┘
                       │
        ┌──────────────▼───────────────────────┐
        │  ③ Rationale-Guided Filtering        │
        │  ────────────────────────────────    │
        │  Flan-T5-large (770M, 단일 RTX 3090) │
        │  ΔPPL = PPL(x) − PPL(x, d) 기반 학습 │
        │  → 각 snippet의 Helpful / Not Helpful│
        │    판정 후 Helpful만 LLM에 투입      │
        └──────────────┬───────────────────────┘
                       │
                       ▼
                [Final LLM Answer]
```

## 핵심 모듈 상세 설명
### Rationale-Guided Filtering (핵심 혁신)
- 훈련 데이터 생성:
  - x: 질의, d: 검색된 문서, r: rationale
  - 라벨: `ΔPPL = PPL(x) − PPL(x, d)`
  - 상위 25% ΔPPL → "Helpful" (문서가 rationale의 perplexity를 크게 낮춤 = 유용)
  - 하위 25% → "Not Helpful"
- Flan-T5-large (770M)를 binary classifier로 SFT
- 추론 시 각 snippet에 대해 filter 적용 → Helpful만 유지

### Rationale-Based Query
- CoT prompt로 base LLM이 rationale 생성 (temperature=0)
- Rationale 자체가 검색 쿼리 (초기 쿼리는 reranker에서만 사용)
- 이유: "the initial query and the rationale exceeds the maximum length of MedCPT"
- 짧은 쿼리는 자동 확장, 긴 쿼리는 핵심 추론 단계만 추출

### Balanced Retrieval
| 코퍼스 | 규모 | 특징 |
|---|---|---|
| PubMed | 대형 (MedCorp) | 생의학 논문 abstract |
| PMC | 대형 | open access full text |
| Medical Textbooks | 소형 | StatPearls 등 표준 교과서 |
| Clinical Guidelines | 소형 | 최신 임상 진료 가이드라인 |

- 각 corpus에서 동일 개수 retrieval → MedCPT-편향 완화
- "balanced approach consistently outperforms others, highlighting the..." (Appendix Figure A3 캡션)

## Input/Output
**Input**
- USMLE/AIIMS/MMLU 스타일 multi-choice 의료 질의 (4-5 선택지)

**Output**
- 정답 선택지 + 추론 과정 (rationale)

## 예시 사례
### COPD Exacerbation Case (MedQA, 논문 Figure 4 — 전체 인용)
> **Initial Query (full case)**:
> > "A 62-year-old man presents to the emergency department with shortness of breath. … He feels as if he is unable to take a deep breath. The patient has a past medical history of COPD and a 44-pack-year smoking history. The patient has been admitted before for a similar presentation. Vitals: T 98.7°F, BP 177/118 mmHg, P 123/min, R 33/min, O2 sat 80% on room air. The patient is started on 100% oxygen, albuterol, ipratropium, magnesium, and prednisone. … He is still short of breath. Physical exam: bilateral wheezes, poor air movement.
> > Which of the following is the best next step in management? (A) BiPAP (B) Chest tube placement (C) Intubation (D) Needle Decompression"
>
> **Meerkat-7B without RAG (자체 추론)**:
> > "...The presence of bilateral wheezes and poor air movement on physical examination suggests exacerbation of COPD with significant airflow obstruction. … (C) Intubation may be necessary for patients who are in respiratory failure and not responding to medical therapy… Therefore, the answer is (C) Intubation." ❌
>
> **RAG with rationale query (no filtering — distractor 유입)**:
> > Top-1 snippet: "...respiratory and hemodynamic signs of tension pneumothorax should be considered a medical emergency and addressed immediately, as this requires urgent needle decompression."
> > Model output: "The presence of bilateral wheezes could also be consistent with a severe COPD exacerbation, but the clinical picture is more suggestive of a tension pneumothorax… Therefore, the answer is (D) Needle decompression." ❌
>
> **RAG² with rationale-guided filtering**:
> > 필터 모델이 tension pneumothorax snippet을 Not-Helpful로 제거 → Top-3 snippet 남음:
> > "...Non-invasive positive pressure ventilation is considered to be effective in reversing acute respiratory failure in selected patients with elevated carbon dioxide and no other life-threatening comorbidities…"
> > Model output: "These findings suggest an exacerbation of COPD with respiratory failure. … Non-invasive positive pressure ventilation can be used in COPD exacerbations to decrease the work of breathing and improve oxygenation. … Therefore, the answer is (A) BiPAP." ✓
>
> **저자 해석 (논문 §5)**: "the initial error stems from the model's distraction by irrelevant information, but proper filtering lead to the correct diagnosis and management plan."

## 주요 평가 결과
**Table 2 — Accuracy on 3 medical QA benchmarks**
| Model + RAG | MedQA | MedMCQA | MMLU-Med | Avg |
|---|---|---|---|---|
| **Llama-3-8B-Instruct (base, 0-shot)** | 57.7 | 53.5 | 69.5 | 60.2 |
|   + MedCPT (k=1) | 55.3 | 51.3 | 65.8 | 57.5 |
|   + MedRAG | 56.4 | 56.6 | 69.2 | 60.7 |
|   + query2doc | 54.3 | 50.0 | 58.5 | 54.3 |
|   + Adaptive-RAG | 57.3 | 53.1 | 70.3 | 60.2 |
|   + InstructRAG-ICL (2-shot) | 55.5 | 55.7 | 71.9 | 61.8 |
|   **+ RAG² (Ours)** | **64.6** | **59.4** | **74.8** | **66.3** |
| **Meerkat-7B (base)** | 71.2 | 60.8 | 73.8 | 68.6 |
|   + MedRAG | 67.9 | 60.6 | 76.1 | 68.2 |
|   + Adaptive-RAG | 71.4 | 60.5 | 74.0 | 68.6 |
|   **+ RAG² (Ours)** | **75.6** | **63.0** | **78.7** | **72.4** |
| **GPT-4o (0-shot, base)** | 88.5 | 76.7 | 92.8 | 86.0 |
|   + MedRAG | 88.3 | 75.9 | 92.4 | 85.5 |
|   + Adaptive-RAG | 88.5 | 76.7 | 92.5 | 85.9 |
|   **+ RAG² (Ours)** | **91.1** | **77.2** | **92.5** | **86.9** |

**핵심 관찰**
- 평균 향상: Llama-3-8B **+6.1**, Meerkat-7B **+3.8**, GPT-4o **+0.9** (소형 모델일수록 RAG² 효과 큼)
- MMLU-Med은 학습 데이터가 없으나 MedMCQA로 훈련한 필터 모델이 transfer (Llama +5.3, Meerkat +4.9)
- 일부 baseline RAG는 base보다 성능 저하 → "RAG frameworks do not always guarantee improved performance, especially in the medical domain" (§4.3)
- Filtering 모델 ensemble + GPT-4o on MedQA → 91.6 (단일 패스 원칙 위배라 main table 미포함)

## 핵심 기여
1. **Rationale-as-query**: 환자 정보가 검색에 노이즈가 되는 문제를 rationale로 대체 우회
2. **Perplexity-based 자동 라벨링**: 의료 어노테이션 희소성 문제 해결
3. **Balanced retrieval**: PubMed 일변도에서 벗어나 4 소스 동등 활용
4. **소형 필터링 모델**: 770M Flan-T5만으로 RTX 3090 단일 GPU에서 학습 가능

## 한계점
- Closed-book 설정에서만 평가 (오라클 문서 없는 환경)
- MMLU-Med 학습 데이터 부재 → MedMCQA로 transfer 학습 (도메인 mismatch 가능)
- Filter 모델은 base LLM에 의존적 → backbone 변경 시 재훈련 필요 (논문 §6 Limitations)
- Rationale가 잘못된 경우 잘못된 검색 → 다만 저자는 "incorrect rationale make up only a small portion" 주장

## 관련 정보
- **ACL Anthology**: [https://aclanthology.org/2025.naacl-long.635/](https://aclanthology.org/2025.naacl-long.635/)
- **arXiv**: [https://arxiv.org/abs/2411.00300](https://arxiv.org/abs/2411.00300)
- **GitHub**: [https://github.com/dmis-lab/RAG2](https://github.com/dmis-lab/RAG2)
- **저자 소속**: Korea University (DMIS Lab), Kyung Hee University, AIGEN Sciences
- **비교 baseline**: MedCPT, MedRAG, query2doc, Adaptive-RAG, InstructRAG, Self-BioRAG
- **K×O 분류**: K1.O1 (PubMed/PMC/교과서/가이드라인 4소스) — multi-source 균등 검색의 대표 사례
