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

## 실제 데이터 형식 예시 (논문 §2 + Figure 2 + Table 1)

### 유형 A — Task 4-component schema (논문 Figure 2)

각 task는 다음 4개 component로 구성:

> **(a) Task Instruction**: 자연어 task 명세
> ```
> "Train a multitask model on the Clintox dataset to predict
>  a drug's toxicity and FDA approval status. Save the test
>  set predictions, including the SMILES representation of
>  drugs and the probability of positive labels, to
>  pred_results/clintox_test_pred.csv"
> ```
>
> **(b) Dataset Information** (디렉토리 + preview):
> ```
> Dataset Directory:
> |-- clintox/
> |---- clintox_test.csv
> |---- clintox_train.csv
>
> Dataset Preview:
> [START Preview of clintox/clintox_train.csv]
> smiles,FDA_APPROVED,CT_TOX
> CCC(/C=C/Cl)(C#C)O,1,0
> C[C@H]1C[C@H]2[C@@H]3CC[C@@H](...),1,0
> [END Preview ...]
> ```
>
> **(c) Expert-Provided Knowledge** (optional):
> ```
> 1. On the task: The ClinTox dataset contains drugs approved by ...
> 2. On featurization: To represent the molecular structure,
>    use Extended-Connectivity Fingerprints (ECFPs) ...
> ```
>
> **(d) Annotated Program** (ground truth, hidden):
> ```python
> import deepchem as dc
> from deepchem.molnet.load_function.molnet_loader import _MolnetLoader
> class MyClintoxLoader(_MolnetLoader):
>     def create_dataset(self): ...
> CLINTOX_TASKS = ['FDA_APPROVED', 'CT_TOX']
> ...
> test_scores_df.to_csv('pred_results/clintox_test_pred.csv')
> ```

### 유형 B — Task-specific Success Criteria (Table 1 예시)

| Task instruction (요약) | Sub-tasks | Success Criteria |
|---|---|---|
| Train multitask model on ClinTox for tox+FDA approval | Feature Eng, Deep Learning | ROC-AUC ≥ 0.77 on test set |
| Build DTI model with DAVIS for COVID drug repurposing | Feature Eng, Deep Learning | Top-5 repurposed drugs match gold |
| Analyze IMU sleep data, compute sleep endpoints | Computational Analysis | `math.isclose` to gold answer |
| Visualize Toronto fire station coverage | Map Visualization | GPT-4o judge ≥ 60 score |

### 유형 C — 4 disciplines × 102 tasks 분포

> ```
> ┌──────────────────────────────────────────────┬─────┐
> │ Bioinformatics                                │     │
> │ Computational Chemistry                       │     │
> │ Geographical Information Science (GIS)        │  102│
> │ Psychology & Cognitive Neuroscience           │     │
> ├──────────────────────────────────────────────┼─────┤
> │ Source: 44 peer-reviewed publications         │     │
> │ Validated by: 9 subject matter experts        │     │
> │ (senior PhD students + professors)            │     │
> └──────────────────────────────────────────────┴─────┘
> ```
>
> Sub-task 빈도 (각 task는 여러 sub-task 조합):
> - Information Visualization (65), Data Analysis (59), Data Visualization (45)
> - Computational Analysis (38), Data Processing (23), Model Development (23)
> - Feature Engineering (20), Map Visualization (18), Deep Learning (14)

### 유형 D — Evaluation metrics (논문 §2.3)

> ```
> 4 program-level metrics:
>   1. VER (Valid Execution Rate)  — binary: program 실행되고 output 저장됨
>   2. SR  (Success Rate)           — binary: success criteria 충족
>   3. CBS (CodeBERTScore)          — annotated program과 코드 유사도
>   4. Cost                          — API token 비용
>
> + 5-stage Rubric (human eval):
>   Data Loading | Data Processing | Modeling/Viz | Output Formatting | Output Saving
> ```
>
> Best agent (OpenAI o1-preview + self-debug, 3 attempts):
> - **independent**: 32.4% → **42.2%** (with expert knowledge: 34.3%)
> - 그러나 **10× cost** 증가 → 비용-성능 trade-off 명확

### 유형 E — 기존 benchmark 비교 (Table 2)

| Benchmark | Code Gen | # Test Tasks | Heterogeneous Data | Shortcut Prevent |
|---|---|---|---|---|
| SWE-Bench | File-Level Edit | 2,294 | ✗ | ✗ |
| BioCoder-Py | Function-Level | 1,126 | ✗ | ✗ |
| ML-Bench | Line-Level | 260 | ✓ | ✗ |
| MLAgentBench | File-Level Edit | 13 | ✗ | ✗ |
| DiscoveryBench-Real | Indirect (NL hypothesis) | 239 | ✓ | ✗ |
| SciCode | Function-Level | 80 | ✗ | ✓ |
| BLADE | Function-Level | 12 | ✗ | ✗ |
| **ScienceAgentBench** | **File-Level Gen** | **102** | ✓ | ✓ |

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
