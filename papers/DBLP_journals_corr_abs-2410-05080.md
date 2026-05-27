---
title: "ScienceAgentBench: Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery"
bib_key: "DBLP:journals/corr/abs-2410-05080"
year: 2024
domain: bio, chem, material, physics, general
type: benchmark
venue: ICLR 2025 / arXiv:2410.05080
paper_link: https://arxiv.org/abs/2410.05080
---
# ScienceAgentBench: 102 Tasks × 44 Peer-Reviewed Publications, Per-step API + E2E Code Success

> ICLR 2025 | Benchmark (data-driven scientific discovery agents) | bio · chem · material · physics · general
> Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Liang, Zixuan Tian, Junlin Wang, Xuechen Li, Hua Xu, Zhen Wang, Yu Su, Huan Sun — Ohio State University
> DBLP: `journals/corr/abs-2410-05080` · arXiv: [2410.05080](https://arxiv.org/abs/2410.05080)

## 한 줄 요약
LLM agent가 과학 데이터 분석 코드를 작성·실행하는 task **102개**를 **44 peer-reviewed publications**에서 추출하고 **9 domain experts**가 검증한 benchmark. 각 task의 출력은 **self-contained Python file**, 평가는 **per-step API-call accuracy + end-to-end executable code success**. 최고 성능 agent도 task의 **32.4% (independent), 34.3% (expert knowledge)** 만 해결.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Task 수집 (peer-reviewed publication 기반)
  ┌──────────────────────────────────────────────┐
  │ 44 peer-reviewed publications에서 task 추출  │
  │ 4 disciplines: bioinformatics, computational │
  │   chemistry, geographical information science,│
  │   psychology & cognitive neuroscience        │
  │                                               │
  │ 102 tasks 총 수집                            │
  └──────────────────────────────────────────────┘

Step 2 — 전문가 검증 (9 subject matter experts)
  └─ Each task: multiple rounds manual validation
  └─ annotation 품질 + scientific plausibility 확인
  └─ 비현실 task 제거

Step 3 — Task 통일 — self-contained Python program
  ┌──────────────────────────────────────────────┐
  │ Input: task description + dataset path        │
  │ Required output: single .py file              │
  │ Execution: agent 작성 코드 실행해서          │
  │            결과 검증                          │
  └──────────────────────────────────────────────┘

Step 4 — Evaluation metrics
  · Code execution success rate (binary)
  · Per-step API call accuracy (granular)
  · Cost (API tokens used)
  · Programs / execution results / costs 동시 평가

Step 5 — Agent strategies tested
  · Direct prompting
  · OpenHands CodeAct
  · Self-debug
  · 각 3 attempts/task
```

---

## 원문 직접 인용 (arXiv:2410.05080 §Abstract + §1)

> "we present **ScienceAgentBench, a new benchmark** for evaluating language agents for data-driven scientific discovery"

> "we extract **102 tasks from 44 peer-reviewed publications in four disciplines** and engage **nine subject matter experts** to validate them"

> "We unify the target output for every task to a **self-contained Python program file** and employ an array of evaluation metrics to examine the generated programs, execution results, and costs"

> Strategies: "**direct prompting, OpenHands CodeAct, and self-debug**"

> Results: "the best-performing agent can only solve **32.4% of the tasks independently and 34.3% with expert-provided knowledge**"

> "OpenAI o1-preview with direct prompting and self-debug, which can boost the performance"

---

## 평가 metric 상세

| Metric | 의미 | 단위 |
|---|---|---|
| **Execution success** | 코드가 실행 가능한가 | binary (per task) |
| **Per-step API accuracy** | 각 단계 함수 호출 정확성 | percentage |
| **End-to-end success** | 최종 결과가 expected output과 일치 | binary |
| **Cost** | API 토큰 사용량 | $ |
| 3 attempts allowed | best-of-3 평가 |

---

## 주요 평가 결과 (논문 본문)

| Agent / Strategy | 독립 (no expert knowledge) | 전문가 지식 제공 |
|---|---|---|
| Direct prompting (Claude/GPT-4) | (낮음) | (낮음+α) |
| OpenHands CodeAct | (중간) | (중간+α) |
| Self-debug | (개선) | (개선+α) |
| **Best agent (overall)** | **32.4%** | **34.3%** |
| OpenAI o1-preview + self-debug | (boost) | (highest) |

→ 결론: 현재 LLM agent는 **end-to-end automation 불충분**. "even building a fully automatic AI Scientist is far from complete"

---

## 4개 분야 task 분포

| Discipline | 대표 task |
|---|---|
| Bioinformatics | sequence analysis, RNA-seq pipeline |
| Computational Chemistry | molecular descriptors, DFT post-processing |
| Geographical Information Science | spatial data analysis, GIS workflow |
| Psychology & Cognitive Neuroscience | EEG/fMRI analysis, statistical modeling |

---

## 한계점
- **102 tasks 만**: 더 큰 scale benchmark 필요
- **4 disciplines 한정**: physics, mathematics 등 미커버
- **Output as Python**: 다른 언어 / 시각화 / 수학 증명 미평가
- **연구 도메인 편향**: data analysis 위주, 가설 생성 미평가
- **실험 검증 부재**: 코드 실행 결과는 in silico, wet-lab 검증 없음
- **시간**: 2024 cutoff, 최신 agent (Claude 3.7 등) 미평가

---

## 관련 정보
- **arXiv**: [2410.05080](https://arxiv.org/abs/2410.05080)
- **DBLP**: [journals/corr/abs-2410-05080](https://dblp.org/rec/journals/corr/abs-2410-05080.html)
- **공식 사이트**: [osu-nlp-group.github.io/ScienceAgentBench](https://osu-nlp-group.github.io/ScienceAgentBench/)
- **GitHub**: [OSU-NLP-Group/ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench)
- **저자 소속**: Ohio State University
- **Venue**: ICLR 2025
- **관련 작업**: MLAgentBench (Huang et al.), SWE-Bench (Jimenez et al.), MatClaw (Zhang 2026, materials-specific code-as-action)
