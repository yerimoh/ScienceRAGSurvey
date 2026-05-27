---
title: "HoneyComb: A Flexible LLM-Based Agent System for Materials Science"
bib_key: DBLP:conf/emnlp/ZhangSHML24
year: 2024
domain: material
type: Method
venue: Findings of EMNLP 2024
paper_link: https://doi.org/10.18653/v1/2024.findings-emnlp.192
---
# HoneyComb: A Flexible LLM-Based Agent System for Materials Science

> Findings of EMNLP 2024 (pp. 3369–3382) | Method | material
> Zhang, Su, Huang, Ma, Li 외 · DBLP: `conf/emnlp/ZhangSHML24`

## 한 줄 요약
재료과학에 특화된 **MatSciKB (38,469 entry KB)** + **ToolHub (general + Inductive Tool Construction 기반 specialized API)** + **하이브리드 Retriever (BM25 + Contriever)**의 3-컴포넌트 LLM 에이전트 시스템. GPT-4 기반 HoneyComb이 **MaScQA 79.07% (vs GPT-4 단독 58.46%, +20.61pp)**, **SciQA 96.54% (vs 90.84%, +5.70pp)** 달성. 16.62% baseline의 HoneyBee-7B를 79.69%로 끌어올려 +63pp 증가의 극적 효과.

## 제작 배경
- **재료과학 LLM의 한계**: 기존 모델들은 일반 도메인 학습 데이터에 의존 → 재료과학 특화 (arXiv preprint, Wikipedia 재료 항목, textbook formula 등) 지식 부재.
- **Coscientist (Boiko et al. 2023) 등 도메인 agent의 성공**이 재료과학에도 적용 가능함을 시사.
- 정적(static) LLM은 PubMed/Materials Project 같이 매일 업데이트되는 데이터 소스를 반영 못함 → real-time tool augmentation 필요.
- **MaScQA (Zaki et al. 2023)** 발표로 재료과학 평가 셋이 마련됨 → tool-augmented system을 정량적으로 검증할 기반 마련.

## 어떻게 만들었나 (Construction Methodology)

```
HoneyComb 전체 아키텍처 (Fig. 1, p.4)

Query → [Knowledge Retrieval Phase]
            │
            ├─ MatSciKB (시맨틱 검색)
            └─ ToolHub Tool Selection
                  ↓ Executor (iterative)
            ┌─ Tool Assessor: 어떤 도구 쓸지 결정
            └─ Tool Executor: 실행 + 결과 평가 → refine
                  ↓
            Retriever (BM25 + Contriever 하이브리드)
                  ↓
            LLM → Final Answer

────────────────────────────────────────
Component 1: MatSciKB (Table 1, p.6 verbatim 수치)
  Total entries: 38,469
  ┌──────────────────────────────────┬────────┐
  │ Source                           │ Entries│
  ├──────────────────────────────────┼────────┤
  │ Materials Science Papers (arXiv) │ 20,384 │
  │ Wikipedia (Materials Science)    │  3,620 │
  │ Materials Science Textbook       │  1,930 │
  │ Materials Science Dataset        │ 10,473 │
  │ Materials Science Formula        │     57 │
  │ GPT-generated Examples           │  2,005 │
  └──────────────────────────────────┴────────┘
  · 16개 카테고리 트리 구조
  · CRUD operation 지원 (실시간 갱신)

────────────────────────────────────────
Component 2: ToolHub (Inductive Tool Construction, Algorithm 1)
  General Tools (Table 2):
    Google Search, Arxiv Search, Wikipedia Search,
    YouTube Search, Python REPL
  Specialized Tools:
    Materials Project API 등 도메인 함수
    + ITC로 자동 합성된 sub-tool 세트

  Inductive Tool Construction (ITC):
    1. 무작위 computational 질문 subset D_train 선정
    2. LLM이 도구 description·파라미터 자동 파싱
    3. 태스크별로 sub-tool로 decompose
    4. 중복·불필요 tool 제거 (refine)

────────────────────────────────────────
Component 3: Hybrid Retriever
  · BM25 (lexical) → 빠른 keyword match
  · Contriever (dense) → 의미적/문맥적 매칭
  · 단순 쿼리: BM25 / 복잡 쿼리: Contriever (m < k+1 결과)

────────────────────────────────────────
Agent-ToolHub 2-phase Protocol
  Phase 1 — Tool Assessor:
     "원본 쿼리 → 후보 도구 subset 선택"
  Phase 2 — Tool Executor (Fig. 2):
     thought-process 수행
     ├─ 단일 tool로 해결 가능 → 실행
     └─ 복잡 → multi-tool decompose
```

## Input (입력)
- **사용자 자연어 쿼리** (재료과학 도메인)
- **태스크 유형**:
  - factoid (예: "Fe₂O₃의 결정 구조?")
  - computational (예: "BaTiO₃의 formation energy?")
  - reasoning (예: GATE 시험 NUM/MATCH/MCQ)

## Output (출력 / 정답 형식)
- 자연어 답변 (인용 + 출처)
- MaScQA 형식: A/B/C/D 또는 수치
- SciQA 형식: 4지 선다 정답

## 실제 태스크 예시

### MaScQA — GATE 기출 (Zaki et al. 2023 활용, 650문항)
> **태스크 분포**:
> · MCQ 285 / MATCH 70 / MCQN 67 / NUM 228
> · 14개 재료과학 sub-domain (thermodynamics, atomic structure, mechanical behavior, …)
>
> HoneyComb 처리 흐름:
> · MCQ 개념형 → MatSciKB 검색 → 관련 textbook chunk + Wikipedia 항목 회수 → LLM 답변
> · NUM 계산형 → ToolHub의 Python REPL 또는 specialized formula tool → 수치 산출

### SciQ — 11,679 multiple-choice 과학 (Welbl et al. 2017 활용; 본 논문에서는 SciQA로 표기)
> **태스크**: 4지 선다 생물·화학·물리 학부 초반 수준 문제
> HoneyComb는 SciQ에 대해 ToolHub만 사용해도 +5.5%p 향상 (Table 5)

### Real-world 쿼리 (시스템 데모)
> **Q (factoid):** "What is the crystal structure of perovskite BaTiO₃?"
> → MatSciKB 검색 → "BaTiO₃: 페로브스카이트 구조, 입방정계, a≈4.01Å" → 답변
>
> **Q (computational):** "What is the formation energy of Fe₂O₃?"
> → ToolHub → Materials Project API → ΔH_f ≈ -2.03 eV/atom → 답변 + DOI

## 주요 평가 결과

### Table 3 — HoneyComb 통합 효과 (Accuracy %)
| Backbone LLM | MaScQA baseline | + HoneyComb | Δ (pp) | SciQA baseline | + HoneyComb | Δ (pp) |
|---|---|---|---|---|---|---|
| **HoneyBee-7B** (재료과학 SFT) | 16.62 | **33.38** | **+16.76** | 33.96 | **79.69** | **+45.73** |
| GPT-3.5 | 33.54 | 38.46 | +4.92 | 90.69 | 90.83 | +0.14 |
| **GPT-4** | 58.46 | **79.07** | **+20.61** | 90.84 | **96.54** | **+5.70** |
| LLaMA2 | 22.15 | 36.31 | +14.16 | 75.79 | 78.66 | +2.87 |
| LLaMA3 | 24.62 | 47.23 | +22.61 | 93.00 | 93.32 | +0.32 |

→ **HoneyBee+HoneyComb이 SciQA에서 +45.73pp 점프** (16.62 → 79.69) — domain-specific SFT 모델에 RAG가 결합되었을 때 가장 큰 효과.

### Table 5 — Ablation Study (GPT-4 기준)
| Setting | MatSciKB | ToolHub | Retriever | **MaScQA Acc.** | **SciQA Acc.** |
|---|---|---|---|---|---|
| Baseline GPT-4 | – | – | – | 61.38 | 90.84 |
| + MatSciKB only | ✓ | – | – | 78.31 (+16.93) | – |
| + ToolHub only | – | ✓ | – | 73.23 (+11.85) | 96.34 (+5.50) |
| **Full HoneyComb** | ✓ | ✓ | ✓ | **79.07** | **96.56** |

→ MaScQA: MatSciKB가 단독 효과 최대 (+16.93pp), ToolHub와 조합 시 +17.69pp 도달.
→ SciQA: ToolHub만으로 96%대 달성 (단순 사실 검증에 일반 도구가 충분).

### Table 4 — Material Category별 성능 (예: Atomic Structure)
| Model | Baseline | + HoneyComb |
|---|---|---|
| HoneyBee | 12.0 | 34.00 |
| GPT-3.5 | 35.00 | 32.00 (drop) |
| GPT-4 | 55.00 | (HoneyComb 적용) |
| ... | ... | ... |

→ **LLaMA-3는 Material Testing에서 +33.34pp** 향상. GPT-3.5는 일부 카테고리에서 성능 하락 — domain mismatch 시나리오 존재.

## 한계점
- **MaScQA·SciQA 외 generalizability 미검증** (저자 인정, Limitations section).
- **MatSciKB curation 비공개 세부**: arXiv 20,384 papers의 선정 기준·중복 처리 절차가 본문에 명시되지 않음.
- **ToolHub는 Materials Project API 가용성에 의존** — 서비스 중단·rate limit 시 취약.
- **재료과학 외 도메인 확장성 미검증** (저자 자체 평가).
- **GPT-3.5에서 일부 카테고리 성능 하락** — RAG가 항상 도움되지 않는 modality mismatch 사례 존재.
- **연구 design·예측 같은 open-ended 태스크 평가 부재** (MCQ/NUM 중심).
- **MatSciKB가 정적 스냅샷일 가능성**: 실시간 갱신 메커니즘은 언급되나 평가는 batch.

## 관련 정보
- **논문**: [EMNLP Findings 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.192)
- **DBLP**: [conf/emnlp/ZhangSHML24](https://dblp.org/rec/conf/emnlp/ZhangSHML24)
- **사용 벤치마크**:
  - MaScQA — Zaki et al. 2023 (Digital Discovery), 650 GATE 문제
  - SciQA → 실제로는 SciQ (Welbl et al. 2017), 11,679 MC 과학 문제
- **비교 대상 시스템**: LLaMP (Chiang et al. 2025), Darwin, StructChem, HoneyBee-7B SFT
