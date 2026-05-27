---
title: LLaMP - Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation
bib_key: DBLP:conf/emnlp/ChiangHCR25
year: 2025
domain: material
type: Method
venue: EMNLP 2025
paper_link: https://arxiv.org/abs/2401.17244
---
# LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation

> EMNLP 2025 | Method + Benchmark | material
> Chiang, Chou, Riebesell — UC Berkeley / Cambridge / LBNL · arXiv:2401.17244

## 한 줄 요약
Materials Project(MP) API를 ReAct 기반 hierarchical multi-agent로 래핑하여 LLM이 DFT 계산값을 직접 조회·검증하도록 하고, **자체 일관성(Self-Consistency of Response, SCoR)** 지표로 응답 변동성을 측정하는 RAG 에이전트 시스템. Bulk modulus MAE를 GPT-4의 41.225에서 **14.574로 65% 감소**시키고, 자기 순서(magnetic ordering) 분류 정확도를 GPT-4의 0.48에서 **0.98로 향상**.

## 제작 배경
- **LLM의 hallucination 문제**: GPT-3.5는 NaCl elastic tensor에서 C₁₁=289.2 GPa을 환각 (DFT 값 76 GPa의 ~4배 오차), C₂₂·C₃₃·C₅₅·C₆₆ 값 누락 (논문 p.7).
- **수치 데이터의 재현성**: high-stakes 자율 실험실(self-driving labs)에서는 동일 쿼리에 대한 응답이 일관되어야 하나, vanilla LLM은 매 호출마다 다른 수치를 생성.
- 기존 prompt-based 접근(StructChem, Darwin 등 fine-tuning 방식)은 (a) 특정 edge case에 과적합되어 재현성 부족, (b) 다양한 데이터 소스 결합 어려움.
- **Materials Project**가 DFT 기반 ~150,000개 무기 화합물 물성을 공개 API로 제공 → 정답을 실시간 fetch 가능.

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Materials Project (MP) API
  ┌─ DFT (PBE-GGA) 기반 ~150,000개 무기 화합물 DB
  ├─ Bulk/shear modulus, bandgap, formation energy, magnetic ordering,
  │  3D crystal structure, elastic tensor, synthesis recipes, ...
  └─ MAPI를 langchain Tool로 wrap (MPThermoExpert, MPElasticityExpert, …)

Step 2 — Hierarchical ReAct Agent (Fig. 1)
  ┌─────────── Supervisor ReAct Agent (GPT-4) ───────────┐
  │  · Action space Â = A ∪ L (action + language)        │
  │  · 사용자 쿼리 분해 → 적절한 Assistant에 delegate       │
  │  · 각 assistant 응답을 episodic memory로 통합 추론     │
  └───────────────────────────────────────────────────────┘
           ↓                       ↓
  ┌─ MPThermoExpert ──┐    ┌─ MPElasticityExpert ─┐
  │  Formation energy  │    │  Bulk/shear modulus  │
  │  Phase diagram     │    │  Young's modulus     │
  └────────────────────┘    └──────────────────────┘
           ↓                       ↓
  ┌─ MPStructureExpert ┐    ┌─ MPMagnetismExpert ──┐
  │  Crystal structure │    │  Magnetic ordering   │
  │  Lattice params    │    │  Magnetization       │
  └────────────────────┘    └──────────────────────┘
  └─ MPSynthesisExpert ── 실험 synthesis recipes + DOI

Step 3 — SCoR 지표 정의 (Sec 4.2)
  N회 반복 호출에서 n개 valid 응답, ˆσ = 표준편차
  ┌─ Precision = (1/n) · |median ± ˆσ|     [수치 불확도]
  ├─ Coefficient of Precision (CoP)
  │   = exp(-Precision)  ∈ [0,1]
  ├─ Confidence = n / N                     [응답 가용성]
  └─ SCoR = CoP × Confidence  ∈ [0, 1]
            ↑                         ↑
        SCoR=1: 항상 동일 응답   SCoR=0: 매우 불일관

Step 4 — 평가 대상
  ┌──────────────────────┬────────────────────────────┐
  │ Task                │ Sampling                    │
  ├──────────────────────┼────────────────────────────┤
  │ Bulk Modulus (GPa)  │ 3d 전이금속 10개 (Sc-Zn)     │
  │ Formation Energy    │ Common compounds (Si, Ge,  │
  │  (eV/atom)         │  InSe, MoS₂, BaTiO₃, CsPbI₃)│
  │ Electronic Bandgap  │ Common semiconductors +     │
  │  (eV)              │  Multi-element (Ba(PdS₂)₂,  │
  │                    │  FePO₄, DyBi₂IO₄, ...)      │
  │ Magnetic Ordering   │ 800 무작위 unary/binary/    │
  │  (FM/AFM/FiM/NM)   │  ternary 화합물             │
  └──────────────────────┴────────────────────────────┘
  각 task당 N=5 반복 → SCoR + MAE 산출

Step 5 — Baseline 비교
  · StructChem (chemistry prompting)
  · Darwin (Materials fine-tuned)
  · GPT-4+Serp (web search augmented)
  · Vanilla GPT-4, Gemini-Pro, Llama 3-8B, GPT-3.5
```

## Input (입력)
- **사용자 쿼리**: 자연어 (예: "What's the stiffest material with the lowest formation energy in Si-O system?")
- **사용 가능 모달리티**: 단일 화합물, 화학 시스템(예: Si-O), 다중 물성 동시 조회

## Output (출력 / 정답 형식)
- **수치 응답**: 단일 값 또는 dict (예: `{"Sc": {"Voigt": 45.715, "Reuss": 45.34, "VRH": 45.528}}`)
- **분류 응답**: FM / AFM / FiM / NM (magnetic ordering)
- **고차 데이터**: 3D 결정 구조, 6×6 elastic tensor matrix
- **참조 정보**: MP material ID (mp-XXXXX), 실험 합성 논문 DOI

## 실제 평가 문항 예시 (논문 본문 + Fig. A.1 / Table B5)

### 멀티 도메인 ReAct 쿼리 (Fig. A.1, p.13)
> **Q:** *"What's the stiffest material with the lowest formation energy in Si-O system?"*
>
> **LLaMP supervisor trace (논문 p.13 verbatim):**
> > "To answer this question, I need to find materials in the Si-O system with the lowest formation energy and the highest stiffness. I will use the MPThermoExpert tool to search for materials in the Si-O system and sort them by formation energy. After finding candidates, I will need to use the MPElasticityExpert tool to determine the stiffness of these materials."
>
> ```json
> { "action": "MPThermoExpert",
>   "action_input": { "input": "What are the materials with the lowest formation energy in the Si-O system?" } }
> ```
> ↓ (Si₂O₅, SiO₂의 여러 polymorph 후보 회수)
> ```json
> { "action": "MPElasticityExpert",
>   "action_input": { "input": "What are the bulk and Young's moduli for Si2O5 (mp-862998), SiO2 (mp-733790), SiO2 (mp-6922), SiO2 (mp-556985), and SiO2 (mp-556994)?" } }
> ```
> ↓ 최종: "The material with the highest bulk modulus would be considered the stiffest."

### Bulk Modulus 쿼리 (Table 1, 3d 전이금속)
> **Q:** *"What are the bulk moduli of Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn?"*
>
> LLaMP는 각 원소에 대해 Voigt / Reuss / VRH 세 값을 모두 반환 (MP DFT 기반).
> Vanilla GPT-4는 단일 추정값을 환각으로 생성.

### Higher-order data — Elastic Tensor (논문 p.7)
> **Q:** *"What is the full elastic tensor of NaCl?"*
>
> - **DFT 정답**: C₁₁ ≈ 76 GPa, 6×6 full tensor matrix
> - **GPT-3.5 (vanilla) 응답**: "C₁₁ = 289.2 GPa" (~4× 오차), C₂₂·C₃₃·C₅₅·C₆₆ 값 누락, matrix 형식 무시
> - **LLaMP**: MP API에서 정확한 6×6 tensor 회수

### 자기 순서 분류 (800 무작위 화합물, Fig. 3)
> **Q:** *"What is the magnetic ordering of [compound]?"* → FM / AFM / FiM / NM
>
> Confusion matrix (LLaMP w/ GPT-4): FM 클래스 136개 중 거의 모두 정답 → accuracy 0.98.

## 주요 평가 결과

### Table 1 — Bulk Modulus & Formation Energy (5회 평균)
| Model | **Bulk K (GPa) MAE↓** | SCoR↑ | **ΔH_f (eV) MAE↓** | SCoR↑ |
|---|---|---|---|---|
| **LLaMP** | **14.574** | **0.900** | **0.009** | **0.953** |
| StructChem | 41.017 | 0.200 | 3.146 | 0.200 |
| Darwin | 156.266 | 0.499 | 2.245 | 0.997 |
| GPT-4 + Serp | 41.742 | 0.352 | 8.214 | 0.745 |
| GPT-4 | 41.225 | 0.910 | 1.680 | 0.180 |
| Gemini-Pro | 43.429 | 0.169 | 1.630 | 0.737 |
| Llama 3 | 41.874 | 0.010 | 4.501 | 0.153 |

→ **LLaMP는 K MAE를 GPT-4 대비 65% 감소(41→15), ΔH_f MAE를 99% 감소(1.68→0.009)** 시키며 SCoR도 가장 높음.

### Table 2 — Magnetic Ordering & Magnetization (800 화합물)
| Model | Mag. Ordering Acc. | F1 | Magnetization MAE | R² |
|---|---|---|---|---|
| **LLaMP (GPT-4)** | **0.98** | **0.89** | **0.045** | **0.992** |
| GPT-4 | 0.48 | 0.26 | 1.611 | -0.201 |
| LLaMP (GPT-3.5) | 0.96 | 0.88 | 1.896 | 0.407 |
| GPT-3.5 | 0.23 | 0.18 | 1.988 | -0.024 |

→ **분류 정확도 0.23 → 0.96 (GPT-3.5) / 0.48 → 0.98 (GPT-4)** — RAG가 파라메트릭 환각을 사실상 제거.

### 핵심 발견
- **LLaMP는 magnetic ordering에서 vanilla GPT-4 대비 +50pp 정확도 향상** (도메인 지식 부족이 LLM의 주된 병목임을 확증).
- SCoR=1에 근접한 응답은 **재현 가능한 과학 워크플로우**에 통합 가능 (autonomous lab integration의 전제조건).
- Hierarchical multi-agent (supervisor + assistants)가 **flat planning보다 우수** — 단일 agent는 한꺼번에 너무 많은 정보를 보면 API schema 위반 빈번.

## 한계점
- **MP DFT의 체계적 오차**: PBE-GGA는 bandgap을 30~50% 과소평가 → 정답 자체가 실험값과 다를 수 있음.
- **MP 커버리지 한정**: 실험 합성된 화합물 중 일부만 MP에 등재 → MOF, COF, polymer 등 일부 클래스 부재.
- **Function-calling 의존**: backend LLM의 tool-use 능력에 직접 영향 (GPT-3.5는 일부 schema 위반).
- **ReAct 루프 실패 시 fallback 없음**: API 응답 파싱 실패하면 환각으로 퇴화.
- **인터랙티브 latency**: 5회 반복 + multi-agent 호출로 단일 쿼리당 수십 초 소요.

## 관련 정보
- **논문**: [arXiv:2401.17244](https://arxiv.org/abs/2401.17244)
- **EMNLP 2025 Anthology**: [ACL Anthology](https://aclanthology.org/2025.emnlp-main)
- **Materials Project**: [materialsproject.org](https://materialsproject.org)
- **DBLP**: [conf/emnlp/ChiangHCR25](https://dblp.org/rec/conf/emnlp/ChiangHCR25)
- **이 시스템을 비교 대상으로 사용한 논문**: HoneyComb (EMNLP Findings 2024) — MaScQA + LLaMP MP 물성 task에서 동일 프로토콜로 비교
