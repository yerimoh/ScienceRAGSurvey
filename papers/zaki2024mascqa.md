---
title: MaScQA - Investigating Materials Science Knowledge of Large Language Models
bib_key: zaki2024mascqa
year: 2024
domain: material
type: benchmark
venue: Digital Discovery (RSC)
paper_link: https://pubs.rsc.org/en/content/articlelanding/2024/dd/d3dd00188a
---
# MaScQA: Investigating Materials Science Knowledge of Large Language Models

> Digital Discovery 2024 | Benchmark | material
> Zaki, Mausam, Krishnan — IIT Delhi (M3RG-IITD) · arXiv:2308.09115

## 한 줄 요약
인도 GATE(Graduate Aptitude Test in Engineering) 재료과학·야금공학 기출문제 **650 문항**을 4가지 문항 구조(MCQ/MATCH/MCQN/NUM) × 14개 재료과학 도메인으로 분류하여 구축한 LLM의 학부 졸업 수준 재료과학 지식 평가 벤치마크. GPT-4-CoT가 62.0%로 최고 성능이며, GPT-4의 conceptual error(64%)가 computational error(36%)를 압도해 도메인 지식 부족이 주요 병목임을 정량화. HoneyComb(GPT-4 + MatSciKB + ToolHub)가 79.07%로 RAG 강화 효과 입증.

## 제작 배경
- 화학·생물 분야에는 도메인 특화 LLM(ChemGPT, BioBERT 등)이 다수 존재하나, **재료과학에는 전문 평가 셋이 부재**.
- 기존 LLM 벤치마크(MMLU, SciQ 등)는 일반 과학 상식 위주로, 학부 졸업 수준의 thermodynamics·crystallography·phase transition 계산 문제를 포함하지 않음.
- GATE 시험은 인도에서 매년 80만 명 이상이 응시(주요 학과 평균 10만 명)하는 **국가 수준 대학원 입시**로, 재료과학·야금 학부 졸업자의 핵심 역량을 검증하기 위해 IIT 5개 기관이 공동 출제 → 신뢰성 있는 정답 키 보유.

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 소스 선정
  └─ 인도 IIT 주관 GATE (Graduate Aptitude Test in Engineering)
      재료과학·야금공학(MT) 파트 기출문제 수집
  └─ 공식 출처: gate.iitkgp.ac.in/old_question_papers.html
      (IIT Kharagpur가 GATE 주관 기관 중 하나)

Step 2 — 문항 구조 분류 (Axis A)
  ┌──────────┬────────────────────────────────────────┬─────┐
  │ 유형     │ 설명                                    │ 수  │
  ├──────────┼────────────────────────────────────────┼─────┤
  │ MCQ      │ 4지 선다, 개념 이해 중심 (1개 정답)     │ 285 │
  │ MATCH    │ 두 리스트 매칭, 4지 옵션                │  70 │
  │ MCQN     │ 4지 옵션 + 수치 계산 필요               │  67 │
  │ NUM      │ 수치 입력 (선택지 없음)                 │ 228 │
  ├──────────┼────────────────────────────────────────┼─────┤
  │ 합계     │                                        │ 650 │
  └──────────┴────────────────────────────────────────┴─────┘
  (MCQ 중 13문제는 복수 정답 형식)

Step 3 — 도메인 분류 (Axis B, 14 카테고리)
  thermodynamics · atomic structure · mechanical behavior ·
  materials manufacturing · material applications · phase transition ·
  electrical properties · material processing · transport phenomenon ·
  magnetic properties · material characterization · fluid mechanics ·
  material testing · miscellaneous

Step 4 — 전문가 검수
  └─ 2명의 재료과학 도메인 전문가가 독립적으로 도메인 라벨링
  └─ 라벨 불일치 → 토론을 통한 합의 도출
  └─ 정답 검증: IIT Kharagpur 공식 answer key 기준

Step 5 — 평가 프로토콜
  ┌─ Zero-shot: "Solve the following question. Write the
  │              correct answer inside a list at the end."
  └─ Chain-of-Thought(CoT): "Solve the following question with
                            highly detailed step-by-step
                            explanation. Write the correct
                            answer inside a list at the end."
  └─ OpenAI API로 GPT-3.5 / GPT-4 평가
  └─ 모델 출력은 텍스트 파일로 저장 후 수동으로 답안 추출
     (모델이 항상 지정 포맷을 따르진 않음)

Step 6 — 공개
  └─ github.com/M3RG-IITD/MaScQA
  └─ 전체 650 문항 (Train/Val/Test 분할 없음)
```

## Input (입력)
- **문항 형식**: 텍스트 기반 자연어 질문 (이미지·그래프 없음)
- **문항 수**: 650 (MCQ 285 + MATCH 70 + MCQN 67 + NUM 228)
- **도메인**: 14개 재료과학 sub-area
- **언어**: 영어
- **메타데이터**: question_id, structure_type, domain_label, correct_answer

## Output (출력 / 정답 형식)
- **MCQ / MATCH / MCQN**: A/B/C/D 중 한 옵션 (또는 복수 옵션)
- **NUM**: 수치 (정수 또는 지정 자릿수의 부동소수점)
- **평가 지표**: 정답 일치율 (% accuracy)
- **베이스라인**: 무작위 선택 시 MCQ 25%, MATCH 25%, MCQN 25%, NUM 0%

## 실제 문항 예시 (논문 본문 + Figure 1·4·5·8 캡션 기반 재구성)

### MCQ — 개념형 (논문 본문 인용)
> 논문 본문에서 GPT-4-CoT가 conceptual error를 보인 사례 중 하나:
>
> **Q (Fig. 4(b)).** Relating lattice parameter (a) and atomic diameter (D) in a given crystal structure.
>
> GPT-4-CoT는 잘못된 관계식 `a = √(8/3) · D`를 적용 → 정답인 `a = (4/√6) · D`와 어긋남.
>
> *Atomic structure 영역에서 LLM의 공식 retrieval 오류를 보여주는 대표 사례*

### MATCH — 응용 분야 매칭 (논문 본문 인용)
> **Q (Fig. 6).** Match materials to their primary application (missile cone heads, semiconductors, refractory uses 등).
>
> *논문 본문(p.18) 분석*: "GPT-3.5-CoT was only able to determine the material properties required for the missile cone heads ... [it] tries to arrive at the correct answer by eliminating the options." → GPT-3.5는 elimination 전략에 의존, GPT-4는 개념적 inter-relating으로 정답 도달.

### MCQN — 수치 + 다중 선택 (논문 본문 인용)
> **Q (Fig. 7).** A numerical question with four numeric options.
>
> *논문 본문*: "The GPT-3.5-CoT solution used the correct concept but made calculation errors leading to a final incorrect answer. However, GPT-4-CoT used the correct concept and did not make calculation mistakes."

### NUM — 수치 직접 입력 (논문 본문 인용)
> **Q (Fig. 8).** Sample numerical question related to **platinum's crystal structure** (FCC, calculating interplanar distance d).
>
> *논문 본문*: "Both models applied the correct concept. However, GPT-3.5-CoT made a calculation mistake in obtaining the interplanar distance 'd'..." → 개념은 맞지만 산술 오류로 NUM 정확도가 모든 카테고리 중 가장 낮음.

> ※ 원문 GATE 문제 텍스트는 IIT Kharagpur 공식 question paper PDF에서 확인 가능 (각 fig 캡션은 이미지 형식이라 PDF에서 직접 텍스트 추출 불가).

## 주요 평가 결과 (Table 1)

| Evaluation Method | MCQ (285) | MATCH (70) | MCQN (67) | NUM (228) | **Overall** |
|---|---|---|---|---|---|
| Baseline (random) | 25 | 25 | 25 | 0 | – |
| GPT-3.5 (zero-shot) | 56.49 | 40.00 | 35.82 | 15.79 | 38.31 |
| GPT-3.5-CoT | 56.84 | 38.57 | 34.33 | 14.04 | 37.38 |
| GPT-4 (zero-shot) | 74.74 | 88.57 | 59.70 | 33.77 | 60.15 |
| **GPT-4-CoT** | **76.84** | **92.86** | 52.24 | **37.28** | **62.00** |
| HoneyComb (GPT-4+MatSciKB+ToolHub, EMNLP 2024) | — | — | — | — | **79.07** |

**핵심 발견**
- GPT-4 → GPT-4-CoT 향상은 미미(+1.85pp) — CoT가 항상 도움되지 않음을 시사.
- NUM 카테고리에서 모든 모델이 최저 성능 → 수치 계산이 주요 병목.
- MATCH에서 GPT-4가 GPT-3.5의 **2배 이상** 정확도 (88.57% vs 40.00%) → 개념 inter-relating 능력 차이.
- 13개 multi-correct MCQ 중 GPT-4는 6개, GPT-4-CoT는 7개만 정답.

**Error 분석 (GPT-4-CoT 오답 100 문항 샘플, Table 3)**
| Error Type | 비율 |
|---|---|
| Conceptual error (지식 부족) | ~64% |
| Computational error (계산 실수) | ~36% |
| Grounding error (개념 적용 오류) | ~0% (CoT가 거의 제거) |

→ 도메인 지식 보강(RAG/SFT)이 계산 능력 향상보다 우선순위.

**Domain 분석 (GPT-4-CoT, Table 2)**
- **최저 정확도 영역**: Electrical properties · Mechanical behavior (~60% 오답)
- Thermodynamics · Atomic structure · Phase transition · Transport phenomena · Magnetic properties: 40%+ 오답
- **최고 정확도 영역**: Material testing (오답 0건) · Material characterization

## 한계점
- **이미지·그래프 없음**: 텍스트 기반 문제만 포함 → multimodal 평가 불가 (실제 GATE는 일부 그림 문제 포함).
- **인도 커리큘럼 편향**: GATE 문제 특성상 인도 학부 교과서 기반 → 미국·유럽 커리큘럼과 미세한 강조점 차이 가능.
- **최신 재료 미커버**: 배터리·2D 소재·나노소재·MOF·perovskite solar cell 등 2010년대 이후 hot topic 문제 부족.
- **언어**: 영어 단일 (다국어 평가 불가).
- **Train/Val/Test 분할 부재**: 전체 650 문항이 평가 셋으로만 사용 → 학습용 split 따로 필요시 사용자가 직접 구성.
- **수치 계산 채점의 모호성**: 부동소수점 반올림 자릿수가 문제별로 다름 → automatic grading 시 tolerance 설정 필요.

## 관련 정보
- **논문**: [Digital Discovery, RSC, 2024 (DOI: 10.1039/D3DD00188A)](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d3dd00188a)
- **arXiv**: [2308.09115](https://arxiv.org/abs/2308.09115)
- **GitHub**: [M3RG-IITD/MaScQA](https://github.com/M3RG-IITD/MaScQA)
- **공식 GATE 문제 출처**: [gate.iitkgp.ac.in](https://gate.iitkgp.ac.in/old_question_papers.html)
- **이 벤치마크를 사용한 후속 작업**:
  - HoneyComb (EMNLP Findings 2024) — 79.07% 달성 (RAG agent)
  - 후속 재료과학 RAG 논문들의 표준 벤치마크로 채택
