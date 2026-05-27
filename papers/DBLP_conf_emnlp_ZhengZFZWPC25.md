---
notion_id: 355f2dcd-4912-815c-b521-d607762bcce7
title: Benchmarking Foundation Models with Retrieval-Augmented Generation in Olympic-Level Physics Problem Solving
bib_key: DBLP:conf/emnlp/ZhengZFZWPC25
year: 2025
domain: physics
type: Method
venue: EMNLP (Findings) 2025
paper_link: https://aclanthology.org/2025.findings-emnlp.1196/
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Benchmarking Foundation Models with Retrieval-Augmented Generation in Olympic-Level Physics Problem Solving

> EMNLP Findings | 2025 | Method | physics

## 한 줄 요약
**PhoPile** — 7개 국제 Physics Olympiad(IPhO, APhO, EuPhO, NBPhO, RMPh, USAPhO, BPhO)에서 모은 3,052개 올림피아드 문제(2018년 이전 2,662개 retrieval corpus + 2019-2021년 390개 test) 기반 **최초의 멀티모달 RAG 물리 벤치마크**. 텍스트·이미지가 결합된 진정한 olympiad 난이도 문제에 대해 8개 LLM/LMM × 7개 retriever × 1-3 shot × reflection on/off를 종합 평가.

## 제작 배경
**기존 데이터셋의 한계**
- SciQ, ScienceQA, TheoremQA 등은 "small number of low-difficulty, text-only physics problems" (논문 §1)
- OlympiadBench는 난이도는 올렸지만 RAG 없이 isolation 평가 → retrieval 효용 미평가
- 물리 답안은 numerical, symbolic, diagrammatic 다양 → 수학과 달리 자동 채점 매우 어려움

**왜 필요한가**
- 수험생이 과거 유사 문제를 참고하여 새 문제를 푸는 학습 방식 = few-shot retrieval과 유사
- Olympiad는 연도 간 개념이 반복 → 과거 문제 retrieval이 효과적일 것이라는 가설 검증 필요
- 저자 인용: "competition problems share similar concepts across years, and past problems capture not only the necessary physics knowledge from basic principles, but also problem-solving strategies" (§1)

## 어떻게 만들었나 (Construction Methodology)
**Step 1: Data Collection**
- 7개 대회 공식 PDF에서 2009-2021 문제 수집
- IPhO (International), APhO (Asian), EuPhO (European), NBPhO (Nordic-Baltic), RMPh (Romanian Master), USAPhO (United States), BPhO (British)
- 2019-2021 → test set (390문제)
- 2009-2018 → retrieval corpus (2,662문제)

**Step 2: 표준화 (논문 §2)**
1. LaTeX 변환: 수식·도해를 표준 LaTeX로 변환
2. Image placeholder: `###img_1###` 형태로 이미지 위치 표시
3. Hierarchical Question Structure: main problem + sub-questions 계층 보존
4. Token statistics 정규화 (Table 2)

**Step 3: 시스템 아키텍처**
```
                  [New Olympiad Question + ###img###]
                                │
                                ▼
              ┌──────────────────────────────────┐
              │   Retrievers (7 종)              │
              │   ─────────────────────────      │
              │   Text-only:                     │
              │     - BM25 (sparse)              │
              │     - Emb-cos (all-MiniLM-L6-v2) │
              │     - Dragon+                    │
              │     - Contriever                 │
              │   Multimodal:                    │
              │     - CLIP                       │
              │     - VisualBERT                 │
              │     - ALIGN                      │
              └────────────┬─────────────────────┘
                           │ Top-k similar (q_i, a_i) pairs
                           ▼
              ┌──────────────────────────────────┐
              │   Generator (8 종)               │
              │   ─────────────────────────      │
              │   Closed: GPT-3.5, GPT-4,        │
              │           GPT-4V, Gemini-Pro,    │
              │           Gemini-Pro-V           │
              │   Open: Llama-3-70B,             │
              │         DeepSeek-Math,           │
              │         Mistral-7B, Phi-3.5,     │
              │         Mathstral-7B (FT 가능)   │
              │   - Few-shot prompt with         │
              │     retrieved Q-A pairs          │
              │   - Sub-question 자동 chain      │
              └────────────┬─────────────────────┘
                           │
                           ▼ Candidate answer
              ┌──────────────────────────────────┐
              │   (Optional) Reflection (GPT-4)  │
              │   ─────────────────────────      │
              │   Answer w/RAG vs Answer w/o RAG │
              │   → 더 정확한 답 선택            │
              └────────────┬─────────────────────┘
                           │
                           ▼
              ┌──────────────────────────────────┐
              │   GPT-4 Judge                    │
              │   ─────────────────────────      │
              │   Reference answer + Student     │
              │   answer → 0-10 점               │
              │   (full score 정답 / 부분점수    │
              │    중간단계 비율)                │
              └──────────────────────────────────┘
```

### Generator Prompt (논문 Figure 3, 그대로 인용)
> "Your task is to answer the physics questions. The mathematical formulas are provided in Latex code. There are some related questions and their answers you may find helpful.
> Here are the examples:
> Question: {Retrieved Question 1}
> Reference answer: {Reference Answer to Question 1}
> Question: {Retrieved Question 2}
> Reference answer: {Reference Answer to Question 2}
> The question that you need to solve is: {Question to be answered}
> Respond with the FINAL answer to the question to get a higher score as possible as you can, rather than only give directions or suggestions for solving the problem. Do NOT use the conditions in the example questions to solve the question."

### Reflection Prompt (Figure 4)
> "Your task is to choose the answer with a higher score of the given physics problem.
> Question: {Question to be answered}
> Answer 1: {Candidate answer without RAG}
> Answer 2: {Candidate answer with RAG}
> Please give a reason and output the final answer number in side '##', for example, ##1##."

### Judge Prompt (Figure 5)
> "You are a professional physicist and you will grade answers provided by physics students by reference to standard answers. The full score is 10 points, and the minimum score is 0 points. If the student gives the final answer, full marks will be awarded directly. If the student does not give the final answer or the final answer is incorrect, please score based on the proportion of correct calculation steps given by the student. You only need to output a score number."

## Input/Output
**Input**: Olympiad 물리 문제 (text + LaTeX + optional image) + (선택) k개 retrieved Q-A pair

**Output**: 단계별 풀이 + 최종 답안 (numerical / symbolic / diagrammatic)

**Evaluation**: GPT-4 grader가 reference answer 대비 0-10점 (Pass Rate = 정답 인정 비율, Average Score = 0-10 평균)

## 예시 사례
### 예시 ① — Charged Ring (논문 Figure 1, retrieval pipeline showcase)
> **New Question (test set)**:
> > "Consider a uniformly charged metallic ring of radius R and total charge q. The ring is a hollow toroid of thickness 2a≪R. This thickness can be neglected in parts A, B, C, and E. The xy plane coincides with the plane of the ring, while the z-axis is perpendicular to it, as shown in Figure 1. In parts A and B you might need to use the formula (Taylor expansion): (1 + xε) ≈ 1 + εx + 0.5ε(ε−1)x², when x≪1. Calculate the electrostatic potential Φ(z) along the axis of the ring at a z distance from its center (point A in ###img_1###)."
>
> **Retrievers tested**: BM25, MiniLM+cosine, Dragon+, Contriever (text-only) 또는 CLIP/VisualBERT/ALIGN (multimodal)
> **Generators tested**: GPT-4, Gemini-Pro, Llama-3, Mistral 등 8종

### 예시 ② — Error Analysis (저자가 직접 분류한 negative case, §3.3)
> 검색이 오히려 성능을 떨어뜨린 3가지 원인 (논문 §3.3):
> 1) "the general retriever was not effectively applied to physics problems, as retriever specific to physics may consider the questions that using the same theorem as the top-k relevant ones, instead of those with highest semantic similarity"
> 2) "The format in retrieved questions misleads the candidate models' answering. The retrieved questions and their reference answer may provide guidance answers instead of directly answering the question. Therefore, the foundation models may refuse to answer the final answer directly"
> 3) "some wrong answers arise from using conditions in the retrieved questions as if they were the known conditions in the current question"

## 주요 평가 결과
**Table 4 — PhoPile-Test (text-only, Pass Rate% / Avg Score)**
| Model | Input | w/o RAG | Emb-cos | BM25 | Dragon+ | Contriever |
|---|---|---|---|---|---|---|
| Llama-3-70B | T | 10.51 (1.34) | 5.4 (1.84) | **19.07** (4.86) | 13.62 (4.83) | 10.28 (4.65) |
| Llama-3-70B + Reflection | T | 10.51 | **19.38** (4.35) | **19.38** (4.35) | 14.51 | 10.80 |
| GPT-3.5 | T | 7.95 (4.12) | 8.72 | 8.23 | 10.00 | 7.69 |
| Gemini-Pro | T | 17.18 (5.30) | 16.15 | 15.90 | 16.41 | **30.51** (5.19) |
| Gemini-Pro + Reflection | T | 17.18 | **21.54** (5.72) | 20.51 | 18.72 | 19.74 |
| GPT-4 | T | 26.41 (6.27) | 24.10 | 25.19 | 25.71 | 25.19 |
| GPT-4 + Reflection | T | 26.41 | 27.92 | 27.69 | **28.46** (6.34) | 26.99 |
| Mathstral-7B-v0.1-FT | T | 6.62 | 27.17 | **29.02** (9.28) | 28.90 | 27.66 |
| Llama-3-8B-FT | T | 5.86 | **28.31** (5.90) | 26.44 | 27.46 | 25.39 |

**Table 5 — PhoPile(V)-Test (multimodal, image+text)**
| Model | w/o RAG | CLIP | VisualBERT | ALIGN |
|---|---|---|---|---|
| Gemini-Pro-V | 12.82 (5.09) | **17.48** | 13.59 | 14.56 |
| Gemini-Pro-V + Reflection | 12.82 | 14.56 | **17.48** (5.28) | 15.53 |
| GPT-4V | 21.79 (6.26) | **30.10** (6.20) | 24.27 | 15.53 |
| GPT-4V + Reflection | 21.79 | 26.41 | 22.33 | 23.30 |

**Table 6 — k-shot 효과 (Avg Score in parens)**
| Model | k | Emb-cos | BM25 | Dragon+ | Contriever |
|---|---|---|---|---|---|
| GPT-3.5 | 1 | 8.97 | 6.92 | 9.74 | 0.77 |
| GPT-3.5 | 2 | 8.72 | 8.23 | 10.00 | 7.69 |
| GPT-3.5 | 3 | 9.74 | 6.41 | 7.44 | 7.71 |
| GPT-4 | 1 | 26.74 | 22.82 | 26.41 | **28.97** |
| GPT-4 | 2 | 24.10 | 25.19 | 25.71 | 25.19 |
| GPT-4 | 3 | 25.90 | 22.56 | 22.37 | 24.62 |

**Table 3 — GPT-4 Grader 신뢰성 (tolerance k)**
| Tolerance k | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Accuracy (%) vs human | 37 | 49 | 73 | 87 |

**핵심 관찰**
- 최고 성능: GPT-4V + CLIP(multimodal) = **30.10%** ; Gemini-Pro + Contriever(text) = **30.51%**
- RAG 효과는 model마다 다름 — 일부 (GPT-3.5 + Contriever) 는 base보다 하락
- Reflection은 약한 모델(Gemini-Pro, Llama-3-70B)에서 큰 향상
- k=1이 종종 k=2,3보다 우수 → "Shot 수 증가가 항상 좋은 것은 아님"
- Open-source FT 모델(Mathstral 29.02)이 GPT-4와 거의 동급

## 핵심 기여
1. **PhoPile** — 7개 대회 기반 최초의 multimodal physics olympiad RAG benchmark
2. **8 LLM/LMM × 7 retriever × 3 shot × reflection 종합 ablation** — 가장 광범위한 physics RAG 평가
3. **Step-wise + solution-level GPT-4 judge** — 추론 단계 채점 프레임워크 (tolerance k=3에서 인간 일치율 87%)
4. **Error taxonomy** — RAG 실패 3가지 원인 분류 (semantic mismatch / format misleading / condition leakage)

## 한계점
- 일반 retriever만 사용 → physics-specific retriever 부재 ("highlights the significance of establishing domain-specific retrievers", §3.3)
- GPT-4 judge 의존 → judge가 물리 전문성을 보장하지 않음
- 영어 문제 중심 (다국어 대회는 영어 번역본)
- 검색 노이즈 robustness 미흡 → conditions leakage 빈발

## 관련 정보
- **논문 링크**: [https://aclanthology.org/2025.findings-emnlp.1196/](https://aclanthology.org/2025.findings-emnlp.1196/)
- **arXiv**: [https://arxiv.org/abs/2510.00919](https://arxiv.org/abs/2510.00919)
- **관련 벤치마크**: SciQ (Welbl et al., 2017), ScienceQA (Lu et al., 2022), TheoremQA (Chen et al., 2023), OlympiadBench (He et al., 2024)
- **K×O 분류**: K3 (체계적 지식/educational artifacts) × O1 (closed-form QA) — 과거 olympiad Q-A pair를 demonstration으로 활용
