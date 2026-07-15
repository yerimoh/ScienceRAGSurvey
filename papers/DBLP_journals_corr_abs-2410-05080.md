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

## TL;DR
A benchmark of **102** tasks in which an LLM agent writes and executes scientific data-analysis code, extracted from **44 peer-reviewed publications** and validated by **9 domain experts**. Each task's output is a **self-contained Python file**, and evaluation is based on **per-step API-call accuracy + end-to-end executable code success**. Even the best-performing agent solves only **32.4% (independent), 34.3% (expert knowledge)** of the tasks.

---

## How It Was Built (Construction Methodology)

```
Step 1 — Task collection (based on peer-reviewed publications)
  ┌──────────────────────────────────────────────┐
  │ Extract tasks from 44 peer-reviewed publications │
  │ 4 disciplines: bioinformatics, computational │
  │   chemistry, geographical information science,│
  │   psychology & cognitive neuroscience        │
  │                                               │
  │ 102 tasks collected in total                 │
  └──────────────────────────────────────────────┘

Step 2 — Expert validation (9 subject matter experts)
  └─ Each task: multiple rounds manual validation
  └─ verify annotation quality + scientific plausibility
  └─ remove unrealistic tasks

Step 3 — Task unification — self-contained Python program
  ┌──────────────────────────────────────────────┐
  │ Input: task description + dataset path        │
  │ Required output: single .py file              │
  │ Execution: run the code written by the agent │
  │            and verify results                 │
  └──────────────────────────────────────────────┘

Step 4 — Evaluation metrics
  · Code execution success rate (binary)
  · Per-step API call accuracy (granular)
  · Cost (API tokens used)
  · Programs / execution results / costs evaluated jointly

Step 5 — Agent strategies tested
  · Direct prompting
  · OpenHands CodeAct
  · Self-debug
  · 3 attempts/task each
```

---

## Example of Actual Data Format (paper §2 + Figure 2 + Table 1)

### Type A — Task 4-component schema (paper Figure 2)

Each task consists of the following 4 components:

> **(a) Task Instruction**: natural-language task specification
> ```
> "Train a multitask model on the Clintox dataset to predict
>  a drug's toxicity and FDA approval status. Save the test
>  set predictions, including the SMILES representation of
>  drugs and the probability of positive labels, to
>  pred_results/clintox_test_pred.csv"
> ```
>
> **(b) Dataset Information** (directory + preview):
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

### Type B — Task-specific Success Criteria (Table 1 examples)

| Task instruction (summary) | Sub-tasks | Success Criteria |
|---|---|---|
| Train multitask model on ClinTox for tox+FDA approval | Feature Eng, Deep Learning | ROC-AUC ≥ 0.77 on test set |
| Build DTI model with DAVIS for COVID drug repurposing | Feature Eng, Deep Learning | Top-5 repurposed drugs match gold |
| Analyze IMU sleep data, compute sleep endpoints | Computational Analysis | `math.isclose` to gold answer |
| Visualize Toronto fire station coverage | Map Visualization | GPT-4o judge ≥ 60 score |

### Type C — 4 disciplines × 102 tasks distribution

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
> Sub-task frequency (each task combines several sub-tasks):
> - Information Visualization (65), Data Analysis (59), Data Visualization (45)
> - Computational Analysis (38), Data Processing (23), Model Development (23)
> - Feature Engineering (20), Map Visualization (18), Deep Learning (14)

### Type D — Evaluation metrics (paper §2.3)

> ```
> 4 program-level metrics:
>   1. VER (Valid Execution Rate)  — binary: program runs and output is saved
>   2. SR  (Success Rate)           — binary: success criteria met
>   3. CBS (CodeBERTScore)          — code similarity to the annotated program
>   4. Cost                          — API token cost
>
> + 5-stage Rubric (human eval):
>   Data Loading | Data Processing | Modeling/Viz | Output Formatting | Output Saving
> ```
>
> Best agent (OpenAI o1-preview + self-debug, 3 attempts):
> - **independent**: 32.4% → **42.2%** (with expert knowledge: 34.3%)
> - but a **10× cost** increase → clear cost-performance trade-off

### Type E — Comparison with existing benchmarks (Table 2)

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

## Evaluation Metric Details

| Metric | Meaning | Unit |
|---|---|---|
| **Execution success** | whether the code is executable | binary (per task) |
| **Per-step API accuracy** | correctness of function calls at each step | percentage |
| **End-to-end success** | whether the final result matches the expected output | binary |
| **Cost** | API token usage | $ |
| 3 attempts allowed | best-of-3 evaluation |

---

## Key Evaluation Results (paper body)

| Agent / Strategy | Independent (no expert knowledge) | Expert knowledge provided |
|---|---|---|
| Direct prompting (Claude/GPT-4) | (low) | (low+α) |
| OpenHands CodeAct | (medium) | (medium+α) |
| Self-debug | (improved) | (improved+α) |
| **Best agent (overall)** | **32.4%** | **34.3%** |
| OpenAI o1-preview + self-debug | (boost) | (highest) |

→ Conclusion: current LLM agents are **insufficient for end-to-end automation**. "even building a fully automatic AI Scientist is far from complete"

---

## Task Distribution Across the 4 Disciplines

| Discipline | Representative tasks |
|---|---|
| Bioinformatics | sequence analysis, RNA-seq pipeline |
| Computational Chemistry | molecular descriptors, DFT post-processing |
| Geographical Information Science | spatial data analysis, GIS workflow |
| Psychology & Cognitive Neuroscience | EEG/fMRI analysis, statistical modeling |

---

## Limitations
- **Only 102 tasks**: a larger-scale benchmark is needed
- **Limited to 4 disciplines**: physics, mathematics, etc. are not covered
- **Output as Python**: other languages / visualizations / mathematical proofs are not evaluated
- **Research-domain bias**: focused on data analysis, hypothesis generation is not evaluated
- **Lack of experimental validation**: code execution results are in silico, with no wet-lab validation
- **Timing**: 2024 cutoff, latest agents (Claude 3.7, etc.) not evaluated

---

## Related Links
- **arXiv**: [2410.05080](https://arxiv.org/abs/2410.05080)
- **DBLP**: [journals/corr/abs-2410-05080](https://dblp.org/rec/journals/corr/abs-2410-05080.html)
- **Official site**: [osu-nlp-group.github.io/ScienceAgentBench](https://osu-nlp-group.github.io/ScienceAgentBench/)
- **GitHub**: [OSU-NLP-Group/ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench)
- **Author affiliation**: Ohio State University
- **Venue**: ICLR 2025
- **Related work**: MLAgentBench (Huang et al.), SWE-Bench (Jimenez et al.), MatClaw (Zhang 2026, materials-specific code-as-action)
