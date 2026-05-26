---
title: Crowdsourcing Multiple Choice Science Questions
bib_key: welbl-etal-2017-crowdsourcing
year: 2017
domain: bio, chem, physics
type: benchmark
venue: WNUT @ EMNLP 2017
paper_link: https://aclanthology.org/W17-4413/
---
# SciQ: Crowdsourcing Multiple Choice Science Questions

> WNUT @ EMNLP 2017 | Benchmark | bio · chem · physics
> Welbl, Liu, Gardner — University of Washington / Allen Institute for AI
> ACL Anthology: `W17-4413`

## 한 줄 요약
물리·화학·생물 분야 교과서·학습 자료에서 크라우드워커가 생성한 **13,679개** 4지 선다형 과학 문제로 구성된 벤치마크. 대부분 문항에 정답 근거 단락(supporting evidence)을 함께 제공하여 RAG 검색 기반 평가에 적합하며, HoneyComb RAG 에이전트가 96.54%를 달성.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 도메인 코퍼스 수집
  물리·화학·생물 교과서 및 온라인 학습 자료 텍스트 수집
  각 문서에서 문제를 만들 수 있는 핵심 문장 자동 추출

Step 2 — 크라우드워커 문제 생성 파이프라인
  AI가 도메인 코퍼스에서 관련 단락을 워커에게 자동 추천
       ↓
  크라우드워커(Amazon MTurk) → 질문 + 정답 작성
       ↓
  AI: 정답과 의미적으로 유사하지만 틀린 distractor 3개 자동 생성
       ↓
  크라우드워커 → distractor 검수 및 수정

Step 3 — 품질 검증
  Distinguishability test: 별도 워커가 크라우드소싱 문항과
  원본 시험 문항을 구별하지 못함 → 실제 시험 수준 품질 확인
  Supporting evidence 단락을 각 문항과 연결

Step 4 — 데이터셋 분할 및 공개
  ┌───────────┬────────┐
  │ 분할      │ 문항수  │
  ├───────────┼────────┤
  │ Train     │ 11,679 │
  │ Validation│  1,000 │
  │ Test      │  1,000 │
  ├───────────┼────────┤
  │ 합계      │ 13,679 │
  └───────────┴────────┘
  AllenAI 공개 / HuggingFace: allenai/sciq
```

---

## 제공 필드 구조

| 필드 | 설명 |
|---|---|
| `question` | 과학 문제 텍스트 |
| `correct_answer` | 정답 선택지 텍스트 |
| `distractor1~3` | 오답 선택지 3개 |
| `support` | 정답 근거 단락 (대부분 문항에 포함) |

---

## 실제 문항 예시

### 생물 (Biology)
> **Q.** What is the powerhouse of the cell?
>
> (A) Nucleus  (B) Ribosome  **(C) Mitochondria** ← 정답  (D) Golgi apparatus
>
> **Support:** *"The mitochondria are often referred to as the powerhouses of the cell because they generate most of the cell's supply of ATP, used as a source of chemical energy."*

### 화학 (Chemistry)
> **Q.** What type of bond holds the two strands of DNA together?
>
> (A) Ionic  (B) Covalent  **(C) Hydrogen** ← 정답  (D) Metallic

### 물리 (Physics)
> **Q.** Which law states that the pressure of a gas is inversely proportional to its volume at constant temperature?
>
> (A) Charles's Law  **(B) Boyle's Law** ← 정답  (C) Avogadro's Law  (D) Gay-Lussac's Law

---

## 주요 평가 결과 (HoneyComb 논문 기준, Test set)

| 모델 | Accuracy |
|---|---|
| HoneyBee-7B (재료과학 특화 SFT) | 33.96% |
| GPT-3.5 | 90.69% |
| GPT-4 (바닐라) | 90.84% |
| **HoneyComb (GPT-4 + MatSciKB + ToolHub)** | **96.54%** |

SciQ는 MaScQA 대비 난이도가 낮아(고등학교~학부 초반 수준) GPT-4 단독도 90%+를 달성. HoneyComb의 +5.7pp 추가 향상은 RAG가 기본 지식 확인에도 유효함을 시사.

---

## 한계점
- 고등학교~학부 초반 수준의 난이도 (전문 연구 수준 아님)
- 크라우드소싱 특성상 문항 품질 불균일
- 재료과학 문항 거의 없음 → 재료 분야 단독 평가에 부적합
- 텍스트 기반만 (이미지·수식 없음)

---

## 관련 정보
- **논문**: [ACL Anthology, WNUT@EMNLP 2017](https://aclanthology.org/W17-4413/)
- **HuggingFace**: [allenai/sciq](https://huggingface.co/datasets/allenai/sciq)
- **이 벤치마크를 사용한 논문**: HoneyComb (EMNLP Findings 2024), HiPerRAG (PASC 2025)
