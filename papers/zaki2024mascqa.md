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
> Zaki, Elton, Badireddy, Krishnamurthy — IIT Delhi (M3RG-IITD)
> DBLP: `journals/dd/ZakiEBK24`

## 한 줄 요약
인도 GATE(Graduate Aptitude Test in Engineering) 재료과학 기출문제 **650문항**을 4가지 문항 구조 × 14개 도메인으로 분류해 구축한 LLM 재료과학 지식 평가 벤치마크. GPT-4도 ~62%에 그쳐 전문 지식의 난이도를 반영하며, HoneyComb(RAG 강화)은 79.07%를 달성.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 소스 선정
  인도 IIT 주관 GATE(Graduate Aptitude Test in Engineering)
  재료과학·야금공학 파트 기출문제 수집
  공식 홈페이지(gate.iitkgp.ac.in) 이전 연도 문제지

Step 2 — 문항 분류 체계 설계
  축 A: 문항 구조(Question Structure)
  ┌──────────┬─────────────────────────────────────────┬─────┐
  │ 유형     │ 설명                                     │ 수  │
  ├──────────┼─────────────────────────────────────────┼─────┤
  │ MCQ      │ 4지 선다형, 개념 이해 중심               │ 284 │
  │ NUM      │ 수치 계산 후 직접 입력                   │ 228 │
  │ MATCH    │ 항목 연결형                               │  70 │
  │ MCQN     │ 수치 선택지가 있는 MCQ                   │  68 │
  ├──────────┼─────────────────────────────────────────┼─────┤
  │ 합계     │                                         │ 650 │
  └──────────┴─────────────────────────────────────────┴─────┘

  축 B: 재료과학 도메인(14개)
  Thermodynamics, Atomic Structure, Mechanical Behavior,
  Electrical Properties, Phase Transition, Transport Phenomena,
  Magnetic Properties, Material Processing, Material Characterization,
  Material Testing, Fluid Mechanics, Other + 2개 소분류

Step 3 — 전문가 검수 및 정답 확인
  2명의 재료과학 전문가가 독립적으로 도메인 분류
  분류 불일치 → 토론 합의
  정답: IIT Kharagpur 공식 answer key 기준 검증

Step 4 — 공개
  GitHub: github.com/M3RG-IITD/MaScQA
  Train/Val/Test 분할 없이 전체 650개를 평가셋으로 제공
  오픈 확장형 구조로 연구자 기여 가능
```

---

## 실제 문항 예시

### MCQ — 개념형
> **Q.** Which of the following crystal structures has the highest packing efficiency?
>
> (A) Simple cubic  (B) Body-centred cubic  (C) **Face-centred cubic** ← 정답  (D) Diamond cubic
>
> *FCC: 74% packing factor (vs. BCC 68%, SC 52%)*

### NUM — 수치 계산형
> **Q.** A steel rod of length 1 m is heated from 20°C to 120°C. Coefficient of linear thermal expansion = 12 × 10⁻⁶ /°C. Increase in length (mm)?
>
> **A.** 1.2 mm
> *(ΔL = α × L × ΔT = 12×10⁻⁶ × 1 × 100 = 1.2×10⁻³ m)*

### MATCH — 항목 연결형
> **Q.** Match the following with their primary application:
> 1. Silicon  2. Kevlar  3. Alumina
> A. Bulletproof vest  B. Semiconductor  C. Refractory material
>
> **A.** 1–B, 2–A, 3–C

---

## 주요 평가 결과

| 모델 | 프롬프팅 방식 | Accuracy |
|---|---|---|
| GPT-3.5 | Zero-shot | ~40% |
| GPT-4 | Zero-shot | ~62% |
| GPT-4 | Chain-of-Thought | ~62.6% |
| **HoneyComb** (GPT-4 + MatSciKB + ToolHub) | — | **79.07%** |

GPT-4도 62% 수준 → 재료과학 전문 계산 문제(NUM, MATCH)가 난이도를 견인.

---

## 한계점
- 텍스트 기반 문제만 포함 (이미지·그래프 없음)
- GATE 시험 특성상 인도 커리큘럼 편향 가능성
- 최신 재료(배터리, 나노소재, 2D 소재) 관련 문항 부족
- 영어 문항만 존재

---

## 관련 정보
- **논문**: [Digital Discovery, RSC, 2024](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d3dd00188a)
- **GitHub**: [M3RG-IITD/MaScQA](https://github.com/M3RG-IITD/MaScQA)
- **이 벤치마크를 사용한 논문**: HoneyComb (EMNLP Findings 2024), MIRAGE의 재료과학 확장 비교
