---
notion_id: 355f2dcd-4912-81a6-96a1-fb28e9797ce2
title: "SQuAI: Scientific Question-Answering with Multi-Agent Retrieval-Augmented Generation"
bib_key: DBLP:conf/cikm/BesrourHS025
year: 2025
domain: bio, chem, physics
type: benchmark
venue: CIKM 2025
paper_link: https://doi.org/10.1145/3746252.3761471
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# SQuAI: 4-Agent Multi-Agent RAG + Q-A-E 1,000-question Benchmark over unarXive

> CIKM 2025 | Method + Benchmark | computer science · physics · biology · chemistry · mathematics
> Ines Besrour, Jingbo He, Tobias Schreieder, Michael Färber — TU Dresden (faerber-lab)
> DBLP: `conf/cikm/BesrourHS025` · DOI: 10.1145/3746252.3761471

## 한 줄 요약
unarXive 2024 arXiv 풀텍스트 코퍼스 위에서 작동하는 **4-agent multi-agent RAG 시스템** SQuAI와 함께 제안된 **Q-A-E (Question-Answer-Evidence) 트리플렛 1,000문항** 벤치마크. 복합 질문을 **sub-question decomposition** 으로 풀어 단계적 retrieval+합성을 수행하며, faithfulness가 standard RAG 대비 최대 **12%p** 향상.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 출처: unarXive 2024
  └─ arXiv 풀텍스트 (1991-2024, 약 230만 편)
  └─ 분야: CS, 수학, 물리, 생물, 화학 등 전 과학 분야

Step 2 — Q-A-E 트리플렛 합성 (DeepEval + LLaMA 3.3 70B Instruct)
  ┌──────────────────────────────────────────────────────────┐
  │ 각 question에 대해:                                       │
  │   Q (Question)     ← LLaMA 3.3 70B로 합성                 │
  │   A (Answer)       ← 인라인 인용 [1][2] 포함 long-form    │
  │   E (Evidence)     ← Q의 정답 근거가 되는 원논문 인용      │
  └──────────────────────────────────────────────────────────┘

Step 3 — 두 서브셋 구성
  ┌─────────────────────────┬────────┬──────────────────────┐
  │ Subset                  │ 문항수 │ 특성                  │
  ├─────────────────────────┼────────┼──────────────────────┤
  │ unarXive Simple         │   500  │ 비전문가용, 광범위    │
  │ unarXive Expert         │   500  │ 전문가용, 본문 증거   │
  ├─────────────────────────┼────────┼──────────────────────┤
  │ 합계                    │ 1,000  │                      │
  └─────────────────────────┴────────┴──────────────────────┘

Step 4 — 평가 protocol
  · 합성 reference answer와 직접 비교 지양
  · 대신 retrieved evidence ↔ generated answer 관계성 평가
  · 지표: Answer Relevance / Contextual Relevance / Faithfulness
    (DeepEval framework, 각 0–1)
```

---

## SQuAI System: 4-Agent Architecture (논문/GitHub 직접 인용)

```
[사용자 복합 질문]
       │
       ▼
┌──────────────────────────────────────┐
│ Agent 1 — Decomposer                 │ ← 핵심 차별점
│   "Decomposes complex user queries   │
│    into simpler, semantically        │
│    distinct sub-questions"           │
└──────────┬───────────────────────────┘
           │ sub-question 들
           ▼
┌──────────────────────────────────────┐
│ Agent 2 — Generator                  │
│   각 sub-question에 대해 retrieve →   │
│   Q–A–E 트리플렛 생성                 │
└──────────┬───────────────────────────┘
           │ 후보 Q-A-E 다수
           ▼
┌──────────────────────────────────────┐
│ Agent 3 — Judge                      │
│   "Evaluates the relevance and       │
│    quality of each Q-A-E triplet     │
│    using a learned scoring mechanism"│
└──────────┬───────────────────────────┘
           │ filtered Q-A-E
           ▼
┌──────────────────────────────────────┐
│ Agent 4 — Answer Generator           │
│   "Synthesizes a final, coherent     │
│    answer from filtered Q-A-E        │
│    triplets" with in-line citations  │
└──────────┬───────────────────────────┘
           ▼
   [최종 long-form 답변 + [1][2]... 인용]
```

→ Aggregative Synthesis의 **"sub-question decomposition"** 메커니즘의 대표 사례.

---

## 예시 Q-A-E 트리플렛 (논문/GitHub 발췌)

> **Q**: "What is quantum computing and how is it used in cryptography?"
>
> **A**: "Quantum computing uses qubits to perform computations based on quantum mechanics [1]. It has potential applications in cryptography, particularly for breaking classical encryption schemes [2]."
>
> **E**:
> - `[1]` → 원논문(unarXive 내 quantum computing 도입 paper)의 specific citation context
> - `[2]` → Shor's algorithm / post-quantum cryptography 관련 원논문 context

→ 각 인용 `[i]`이 원문 `cited paragraph` 와 1:1 매핑되어, faithfulness 평가 가능.

---

## 주요 평가 결과 (논문 본문 인용)

### unarXive Simple/Expert (combined score, 0–1)
| Approach | unarXive Simple | unarXive Expert |
|---|---|---|
| Standard RAG (baseline) | 0.759 | 0.796 |
| SQuAI (Abstract retrieval) | 0.828 | 0.812 |
| **SQuAI (Full-Text retrieval)** | **0.847** | **0.864** |

### Faithfulness 개선 (GitHub README 인용)
> "SQuAI improves combined scores by up to **12%** in faithfulness compared to a standard RAG baseline."

핵심 발견:
- **Full-text retrieval > Abstract retrieval** (Expert subset에서 차이 더 큼: +5.2%p)
- **Sub-question decomposition** 이 복합 질문에서 단일 query baseline 대비 일관 향상
- Judge agent의 quality filtering이 hallucination 억제에 기여

---

## 평가 지표 상세 (DeepEval)

| 지표 | 정의 | 측정 대상 |
|---|---|---|
| **Answer Relevance** | 질문 ↔ 생성 답변의 의미적 일치도 | Q → A |
| **Contextual Relevance** | 제공 증거가 답변에 효과적으로 통합된 정도 | E → A |
| **Faithfulness** | 답변이 증거에 의해 지지되는지 (unsupported claim 없음) | A ↔ E |

3개 지표 모두 0–1 범위, LLM-as-judge 방식.

---

## 한계점
- **합성 질문**: LLaMA 3.3 70B 로 생성 → 실제 인간 연구자의 복잡한 의도/표현 다양성 부분 미반영
- **합성 reference answer**: gold answer가 LLM 생성이라 직접 비교 회피 → 평가가 evidence-answer 관계성에 한정
- **LitSearch 등 추가 평가 셋도 사용**: 본 1,000 Q-A-E benchmark 외에도 평가에 활용
- **CIKM 2025 short/full paper**: arXiv preprint 미확인, ACM DL 게재본만 정식 출처

---

## 관련 정보
- **논문 (ACM DL)**: [doi.org/10.1145/3746252.3761471](https://doi.org/10.1145/3746252.3761471)
- **GitHub**: [github.com/faerber-lab/SQuAI](https://github.com/faerber-lab/SQuAI)
- **데이터셋 (HuggingFace)**: [ines-besrour/unarxive_2024](https://huggingface.co/datasets/ines-besrour/unarxive_2024)
- **DBLP**: [conf/cikm/BesrourHS025](https://dblp.org/rec/conf/cikm/BesrourHS025.html)
- **저자 소속**: TU Dresden (faerber-lab)
- **이 벤치마크를 사용한 후속 작업**: SQuAI 자체 (CIKM 2025)
