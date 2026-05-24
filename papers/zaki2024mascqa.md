---
notion_id: 355f2dcd-4912-8138-b28d-c94f91168671
title: MaScQA - Investigating Materials Science Knowledge of Large Language Models
bib_key: zaki2024mascqa
year: 2024
domain: material
type: benchmark
venue: Digital Discovery (RSC)
paper_link: https://pubs.rsc.org/en/content/articlelanding/2024/dd/d3dd00188a
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# MaScQA: Investigating Materials Science Knowledge of Large Language Models

> Digital Discovery (RSC) | 2024 | Benchmark | Domain: material

---
## 한 줄 요약
인도 GATE 시험 기출문제를 기반으로 구축한 **재료과학 LLM 평가용 QA 벤치마크**. 650개의 문항으로 LLM의 학부 수준 재료과학 지식을 측정한다.

---
## 제작 배경
재료과학 분야에는 LLM을 도메인 특화 방식으로 평가할 수 있는 벤치마크가 존재하지 않았다. 일반 QA 벤치마크(MMLU 등)는 재료과학의 전문 개념(열역학, 결정 구조, 기계적 거동 등)을 충분히 커버하지 못하기 때문에, 실제 공학 시험 문제를 기반으로 한 도메인 특화 데이터셋이 필요했다.

---
## 어떻게 만들었나 (Construction Methodology)
### Step 1 — 문제 출처 선정
- 인도 IIT(Indian Institute of Technology)가 주관하는 **GATE(Graduate Aptitude Test in Engineering)** 시험의 재료과학(Materials Science & Metallurgy) 파트 기출문제를 수집
- GATE는 인도 공과대학원 입학 시험으로, 학부 수준의 광범위한 재료과학 지식을 검증하는 고난도 국가시험
- 공식 홈페이지(gate.iitkgp.ac.in)에서 이전 연도 문제지 수집

### Step 2 — 문항 분류 체계 설계
두 축으로 분류:

**① 문항 구조(Question Structure) 기준**
| 유형 | 설명 | 수 |
|---|---|---|
| MCQ | 4지 선다형, 개념 이해 중심 | 284 |
| NUM | 수치 계산 후 직접 입력 | 228 |
| MATCH | 항목 연결형 | 70 |
| MCQN | 수치 선택지가 있는 MCQ | 68 |

**② 재료과학 도메인(Domain) 기준**
| 도메인 | 예시 |
|---|---|
| Thermodynamics | 엔탈피, 깁스 에너지, 상평형 |
| Atomic Structure | 결정 구조, 격자 결함, 밀러 지수 |
| Mechanical Behavior | 응력-변형률, 피로, 파괴 역학 |
| Electrical Properties | 도체/반도체/절연체, 유전체 |
| Phase Transition | 상변태, TTT 다이어그램 |
| 외 9개 도메인 | — |

### Step 3 — 전문가 검수 및 정답 확인
- 2명의 재료과학 전문가가 **각 문항의 도메인 분류**를 독립적으로 수행
- 분류 불일치 항목은 토론을 통해 합의로 해결
- 정답은 IIT Kharagpur 공식 answer key에서 검증

### Step 4 — 데이터셋 공개
- GitHub(github.com/M3RG-IITD/MaScQA)에 오픈소스 공개
- 연구자들이 추가 문항을 기여할 수 있는 **오픈 확장형 구조**로 설계
- Train/Val/Test 분할 없이 전체 650개를 평가용으로 제공

---
## Input (입력)
| 항목 | 내용 |
|---|---|
| **출처** | 인도 IIT 주관 GATE(Graduate Aptitude Test in Engineering) 재료과학 기출문제 |
| **문항 형식** | 자연어 텍스트 질문 + 선택지(MCQ, MCQN) 또는 수치 입력(NUM, MATCH) |
| **도메인** | 열역학, 원자 구조, 기계적 거동, 재료 제조, 재료 응용, 상전이, 전기적 특성, 재료 공정, 수송 현상, 자기적 특성, 재료 특성화, 유체역학, 재료 시험, 기타 (총 14개) |

### 문항 유형별 분포
| 유형 | 수 | 설명 |
|---|---|---|
| MCQ | 284 | 4지 선다형 개념 문제 |
| NUM | 228 | 수치 계산 후 직접 입력 |
| MATCH | 70 | 항목 연결형 |
| MCQN | 68 | 수치 선택지가 있는 MCQ |
| **합계** | **650** | |

---
## Output (출력 / 정답 형식)
| 유형 | 출력 형태 |
|---|---|
| MCQ / MCQN | 선택지 중 정답 알파벳 (A / B / C / D) |
| NUM | 수치값 (단위 포함 가능) |
| MATCH | 매칭 쌍 목록 |

**평가 지표:** Accuracy (정답률)

---
## 예시 문항
### 예시 1 — MCQ (개념형)
> **Q.** Which of the following crystal structures has the highest packing efficiency?
> (A) Simple cubic  (B) BCC  (C) FCC  (D) Diamond cubic
>
> **A.** (C) FCC — 74% packing efficiency

### 예시 2 — NUM (계산형)
> **Q.** A steel rod of length 1 m is heated from 20°C to 120°C. If the coefficient of linear thermal expansion is 12 × 10⁻⁶ /°C, what is the increase in length (in mm)?
>
> **A.** 1.2 mm
> *(계산: ΔL = α × L × ΔT = 12×10⁻⁶ × 1 × 100 = 1.2×10⁻³ m)*

### 예시 3 — MATCH (연결형)
> **Q.** Match the following materials with their primary application:
> 1. Silicon  2. Kevlar  3. Alumina
> A. Bulletproof vest  B. Semiconductor  C. Refractory material
>
> **A.** 1-B, 2-A, 3-C

---
## 주요 평가 결과 (논문 기준)
| 모델 | 프롬프팅 | 전체 Accuracy |
|---|---|---|
| GPT-4 | Zero-shot | ~62% |
| GPT-4 | CoT | ~62.6% |
| GPT-3.5 | Zero-shot | ~40% |
| HoneyComb (GPT-4 기반) | — | **79.07%** |

> GPT-4도 약 62% 수준 → 재료과학 전문 지식의 복잡성을 반영한 난이도 높은 벤치마크

---
## 한계점
- 텍스트 기반 문제만 포함 (이미지/그래프 없음)
- 영어 문항만 존재
- GATE 시험 특성상 인도 커리큘럼 편향 가능성
- 최신 재료(배터리, 나노소재 등) 관련 문항 부족

---
## 관련 정보
- **논문:** [Digital Discovery, RSC, 2024](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d3dd00188a)
- **GitHub:** [https://github.com/M3RG-IITD/MaScQA](https://github.com/M3RG-IITD/MaScQA)
- **이 벤치마크를 사용한 논문:** HoneyComb (EMNLP Findings 2024)
