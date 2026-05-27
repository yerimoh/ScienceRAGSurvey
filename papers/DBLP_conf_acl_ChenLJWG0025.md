---
title: "Towards Omni-RAG: Comprehensive Retrieval-Augmented Generation for Large Language Models in Medical Applications"
bib_key: "DBLP:conf/acl/ChenLJWG0025"
year: 2025
domain: medical
type: Method
venue: ACL 2025 (Vienna, Austria), pp. 15285–15309
paper_link: https://aclanthology.org/2025.acl-long.742/
---
# Omni-RAG: Comprehensive Multi-Source RAG for Medical Applications via Source Planning Optimisation (SPO)

> ACL 2025 | 2025 | Method | medical

## 한 줄 요약
의료 QA의 8개 광범위 데이터셋(Reasoning/Research/Clinical/Open-ended)을 5개 이질적 지식 소스 — **Book, Guideline, Research(PubMed), Wiki, Graph(UMLS+DrugBank)** — 로 동시 커버하는 **MedOmniKB**를 구축하고, 전문가 LLM(Qwen2.5-72B-AWQ)이 SFT+DPO로 소형 planner(Qwen2.5-7B)에게 "어느 소스에 어떤 쿼리로 몇 번 묻는가"를 학습시키는 **Source Planning Optimisation (SPO)** 방식. 평균 정확도 **+4.6 ~ +7.0**% 향상으로 SOTA baselines (Reflexion, SeRTS, Trainable Planning, RaFe) 전반을 능가.

## 제작 배경
**기존 의료 RAG 한계 (논문 §1)**
- 기존 시스템은 PubMed 또는 Wikipedia 단일 소스 의존
- 질의 유형(진단, 약물 상호작용, 최신 연구, consumer health)마다 최적 소스가 다름에도 동일 검색 전략 사용
- 모델이 "각 소스에 무엇이 있는지"에 대한 기대치와 정렬되지 않음 → 부적절한 소스 호출
- 저자 인용: "Existing methods typically treat all sources uniformly, using the original question to retrieve without tailoring the search strategy to different sources" (§1)

**왜 필요한가**
- 의료 AI는 환자 안전과 직결 → "correctness and trustworthiness are paramount" (§1)
- 진단·임상 의사결정·연구지식·소비자 건강 등 의료 시나리오를 포괄해야 임상 적용 가능
- 단일 소스는 long-tail (드문 질환, 최신 약물, 임상 가이드라인 업데이트) 누락

## 어떻게 만들었나 (Construction Methodology)
### Step 1 — MedOmniKB 5-소스 구축 (논문 §3)
**Unstructured Sources**
| Source | #Docs | #Chunks | #Words/Chunk |
|---|---|---|---|
| **Book** (교과서) | 27.7k | 13.1M | 150.1 |
| **Guideline** (임상 가이드라인) | 45.7k | 647.7k | 106.7 |
| **Research** (PubMed 2024 baseline) | 25.3M | 48.0M | 128.7 |
| **Wiki** (English Wikipedia) | 6.4M | 29.7M | 112.1 |

**Structured Source**
| Source | #Concepts | #Definitions | #Relations |
|---|---|---|---|
| **Graph** (UMLS + DrugBank) | 1.7M | 317.9k | 2.9M |

- Book: 18,182 PDFs (의학·외과·영상의학) + StatPearls + MedRAG 교과서
- Guideline: 13개 가이드라인 소스에서 45,679 articles
- Research: 2024 PubMed 전체 스냅샷 (title+abstract)
- Wiki: HuggingFace English Wikipedia 처리
- Graph: UMLS Metathesaurus Full Subset + DrugBank의 description/indication/pharmacodynamics/absorption/drug interaction을 노드 정의에 통합. SQLite 저장 (online UMLS API latency 회피)

**검색 인프라**
- Unstructured: MedCPT-article-encoder → Qdrant vector DB
- Graph: SQLite에서 concept 정의 + 1-hop relations 추출 후 reranker로 필터링

### Step 2 — Source Planning Optimisation (SPO, 논문 §4, Figure 2)
```
       ┌─────────────────────────────────────────────────┐
       │  Training Q (with gold answer)                  │
       └────────────────────┬────────────────────────────┘
                            │
                            ▼
       ┌─────────────────────────────────────────────────┐
       │  ① Planning Exploration                         │
       │  ───────────────────────────────                │
       │  Expert LLM (Qwen2.5-72B-Instruct-AWQ)          │
       │  → 각 소스마다 multiple queries 생성            │
       │     Plan P = {(i, j, q_ij)} where i=source,     │
       │              j=query index                      │
       │     Per-source 쿼리 ≤ 4 (context 한계)          │
       └────────────────────┬────────────────────────────┘
                            │
                            ▼
       ┌─────────────────────────────────────────────────┐
       │  ② Planning Judging                             │
       │  ───────────────────────────────                │
       │  각 query로 retrieve → 문서 d_ij                │
       │  Expert LLM이 "이 문서가 gold answer를          │
       │  support하는가?" 판정                           │
       │  → positive plan (support) / negative plan      │
       └────────────────────┬────────────────────────────┘
                            │
                            ▼
       ┌─────────────────────────────────────────────────┐
       │  ③ Planning Learning                            │
       │  ───────────────────────────────                │
       │  소형 planner (Qwen2.5-7B) on positive plans:   │
       │   (1) SFT (supervised fine-tuning)              │
       │   (2) DPO with (positive, negative) pairs       │
       └────────────────────┬────────────────────────────┘
                            │
                            ▼
                  [Trained Planner Mθ]
                            │
       (Inference) ─────────┼─────────
                            ▼
       For new question x → 5 sources × ≤4 queries each
                            ▼
              MedOmniKB → Top-k documents D
                            ▼
                  Reader (frozen Qwen/Llama/Mistral)
                            ▼
                       Answer y
```

## Input/Output
**Input**: 의료 질의 x (MCQ 또는 open-ended)

**Output**: Source plan P + 최종 답변 y. P는 다음 형태:
> `<book>seborrheic dermatitis symptoms and signs; greasy yellow scales skin condition; ...</book>`
> `<guideline>clinical approach to infantile skin conditions; pediatric dermatology best practices; ...</guideline>`
> `<research>recent studies on seborrheic vs atopic dermatitis; pathophysiology of greasy scale formation; ...</research>`
> `<wiki>atopic dermatitis; infant skin rashes; allergic contact dermatitis triggers; ...</wiki>`
> `<graph>Psoriasis, genetic transmission and skin manifestations; Skin scaling, underlying dermatological conditions; ...</graph>`

## 예시 사례
### 예시 ① — Seborrheic Dermatitis (논문 Figure 2 — 핵심 case study)
> **Original Question (MedQA-style MCQ)**:
> > "A 3-month-old boy is brought to the physician by his parents for the evaluation of a rash on his scalp and forehead. The parents report that the rash has been present for several weeks. They state that the rash is sometimes red and scaly... Some patches are covered by greasy yellow scales. Which of the following is the most likely diagnosis?
> > A. Atopic dermatitis  B. Seborrheic keratosis  C. Allergic contact dermatitis  D. Seborrheic dermatitis"
>
> **Gold Answer**: D. Seborrheic dermatitis
>
> **SPO Planner 출력 (5-source plan)**:
> > `<book>seborrheic dermatitis symptoms and signs; greasy yellow scales skin condition; ...</book>`
> > `<guideline>clinical approach to infantile skin conditions; pediatric dermatology best practices; ...</guideline>`
> > `<research>recent studies on seborrheic vs atopic dermatitis; pathophysiology of greasy scale formation; ...</research>`
> > `<wiki>atopic dermatitis; infant skin rashes; allergic contact dermatitis triggers; ...</wiki>`
> > `<graph>Psoriasis, genetic transmission and skin manifestations; Skin scaling, underlying dermatological conditions; ...</graph>`
>
> **Planning Judging 단계 비교**:
> - "Support Gold Answer" plan → DPO에서 positive 강화
> - "Not Support Gold Answer" plan → negative 억제
>
> **결과**: 5개 소스에서 각각 다른 시맨틱 layer의 정보를 끌어와 D 정답 도출. 단일 PubMed RAG는 "infant skin rash" 일반 정보만 끌어와 D vs A 혼동 가능

## 주요 평가 결과
**Table 4 — 8개 데이터셋 정확도, Reader = Frozen Qwen2.5-7B-Instruct**
| Method | MedQA | MedMCQA | MMLU-Med | PubMedQA | BioASQ | SEER | DDXPlus | MIMIC-IV | **Avg** |
|---|---|---|---|---|---|---|---|---|---|
| No Retrieval | 60.80 | 56.17 | 76.95 | 34.60 | 74.81 | 51.00 | 42.80 | 58.50 | 56.95 |
| Original Question | 62.45 | 63.25 | 80.90 | 47.00 | 89.00 | 58.40 | 42.80 | 57.90 | 62.71 |
| Query2Doc | 62.92 | 66.42 | 80.26 | 46.40 | 88.24 | 58.80 | 42.40 | 56.90 | 62.79 |
| Frozen 72B Prompting | 72.11 | 65.33 | 81.73 | 53.80 | 89.64 | 57.10 | 48.70 | 62.00 | 66.30 |
| Reflexion (72B) | 73.13 | 66.00 | 79.06 | 52.60 | 89.64 | 57.90 | 49.40 | 62.60 | 66.29 |
| SeRTS (72B) | 70.70 | 66.83 | 82.55 | 55.60 | 90.03 | 57.10 | 51.20 | 62.50 | 67.06 |
| Trainable Planning (7B) | 72.03 | 66.42 | 82.19 | 54.80 | 89.90 | 57.20 | 46.40 | 60.30 | 66.16 |
| RaFe Planning (7B) | 70.86 | 66.50 | 78.70 | 53.40 | 89.77 | 55.20 | 50.30 | 63.70 | 66.05 |
| **SPO Planning (7B, Ours)** | **76.98** | **71.08** | **85.49** | **60.20** | 89.77 | **61.90** | **52.40** | **69.60** | **70.93** |

**Table 4 (cont.) — Reader = Frozen Llama3.1-8B**
| Method | MedQA | MedMCQA | MMLU-Med | PubMedQA | BioASQ | SEER | DDXPlus | MIMIC-IV | **Avg** |
|---|---|---|---|---|---|---|---|---|---|
| No Retrieval | 65.99 | 59.50 | 76.58 | 56.20 | 81.97 | 57.00 | 38.80 | 58.60 | 61.83 |
| Original Question | 60.57 | 57.50 | 72.18 | 74.20 | 87.47 | 57.60 | 39.00 | 58.10 | 63.33 |
| Frozen 72B Prompting | 71.17 | 62.08 | 75.94 | 71.40 | 89.00 | 57.50 | 41.10 | 58.60 | 65.85 |
| SeRTS | 71.88 | 63.25 | 77.13 | 71.60 | 89.51 | 57.00 | 42.90 | 60.10 | 66.67 |
| **SPO Planning (Ours)** | **77.45** | **69.25** | **78.97** | **75.60** | 89.64 | **60.70** | **45.70** | **64.10** | **70.18** |

**핵심 관찰**
- SPO 7B planner가 frozen 72B prompting과 SeRTS·Reflexion(둘 다 72B) 능가
- Qwen2.5-7B reader: 평균 56.95 (No-RAG) → 70.93 (SPO) = **+13.98** vs baseline
- SOTA baseline 대비 **+4.6 ~ +7.0%** 평균 향상
- 가장 큰 향상: PubMedQA(+5.6 over SeRTS, 60.20 vs 55.60), MIMIC-IV(+7.1, 69.60 vs 62.50)

## 핵심 기여
1. **MedOmniKB** — 5-소스(Book/Guideline/Research/Wiki/Graph) 통합 의료 지식 베이스, 기존 단일소스 KB 대비 규모 차원이 다름 (Table 1)
2. **Source Planning Optimisation (SPO)** — Plan Exploration → Plan Judging → Plan Learning 3-단계로 planner를 학습; LLM-as-judge 패러다임으로 gold annotation 없이 학습 데이터 확보
3. **소형 planner의 SOTA** — 7B planner가 72B baseline을 11개 데이터셋에서 능가 (효율성)
4. **5-소스 구조화 plan output** — `<book>...</book><guideline>...</guideline>...` 형식의 명시적 source-aware 쿼리

## 한계점
- 5개 소스 모두 K1(문헌)·K2(큐레이션 DB) 계열 — K4(개인/임상 경험) 미포함
- MedOmniKB 구축 비용 큼 (25.3M PubMed 처리)
- SPO 학습 시 전문가 LLM(72B) 추론 반복 필요 → 학습 비용 상승
- 소스 분포 외(out-of-distribution) 데이터에 대한 적응성은 추가 검증 필요 (논문 §6)
- Per-source query 수 4개로 제한 → 복잡 multi-hop 질의에서 부족할 가능성

## 관련 정보
- **논문**: [ACL Anthology 2025.acl-long.742](https://aclanthology.org/2025.acl-long.742/)
- **arXiv 프리프린트**: [arXiv:2501.02460](https://arxiv.org/abs/2501.02460)
- **코드/프로젝트**: [GitHub: Jack-ZC8/Omni-RAG-Medical](https://github.com/Jack-ZC8/Omni-RAG-Medical)
- **저자 소속**: Shanghai Jiao Tong University / Fudan University / Shanghai AI Lab
- **평가 데이터셋 (11종)**: MedQA, MedMCQA, MMLU-Med, PubMedQA, BioASQ, SEER, DDXPlus, MIMIC-IV-ED, LiveQA, MedicationQA, ExpertQA-Biomed (총 24,199 train / 4,837 dev / 8,248 test)
- **비교 baseline**: No Retrieval, Original Question, Query2Doc, Reflexion, SeRTS, Trainable Planning, RaFe Planning
- **K×O 분류**: K1.O1 (문헌+가이드라인) + K2.O1 (UMLS+DrugBank KG) — 다중소스 K1+K2 통합 패턴의 대표 사례
