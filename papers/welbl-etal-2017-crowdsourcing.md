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

> WNUT @ EMNLP 2017 (pp. 94–106) | Benchmark | bio · chem · physics · earth science
> Welbl, Liu, Gardner — UCL / University of Washington / Allen Institute for AI

## 한 줄 요약
물리·화학·생물·지구과학 4분야의 초·중·고~대학 입문 수준 교과서에서 추출한 단락 기반으로, 크라우드워커가 **AI가 제안한 distractor를 검수·수정하는 방식**으로 생성한 **13,679개** 4지 선다형 과학 문제. 두 가지 버전(MC + direct-answer)을 제공하며, 인간이 SciQ 문항과 실제 시험 문항을 구별하지 못할 정도의 품질. RAG retriever baseline(Lucene)이 신경망 reader를 능가하는 retrieval-heavy 데이터셋. 전체 예산 **$10,415**으로 구축.

## 제작 배경
- **과학 시험 QA의 핵심 병목**: 대규모 in-domain 학습 셋의 부재.
- 2016 Kaggle 8th-grade 과학 시험 챌린지에서 최고 시스템도 단 **60% accuracy** 달성 (retrieval 기반이 신경망 reader를 능가).
- 크라우드소싱의 어려움: (1) 도메인 전문성 부족, (2) 질문의 다양성·관련성 확보 곤란, (3) **distractor 품질이 낮으면 문제가 trivial해짐**.
- 본 논문 핵심 아이디어: 사람의 task를 "처음부터 생성"이 아닌 "AI 제안에 대한 select / modify / validate"로 reframe → 빠르고 저렴하며 다양성 확보.

## 어떻게 만들었나 (Construction Methodology)

```
Step 0 — 도메인 코퍼스 수집
  └─ 28권 교과서 (CK-12, OpenStax 등 Creative Commons 학습 자료)
  └─ 영역: biology · chemistry · earth science · physics
  └─ 수준: elementary → college introductory

Step 1 — Noisy classifier로 relevant 문단 자동 선별
  └─ "in-domain" 단락만 워커에게 제시 → irrelevant 단락 제거

Step 2 — 크라우드워커 질문 생성 (AMT Master's status, $0.30/HIT)
  └─ 단락 3개씩 제시 → 그 중 1개를 골라 단답형 QA 작성
  └─ 12.1%의 경우 워커가 3개 단락 모두 사용 → 모두 거부도 허용
  └─ 총 175명 워커 참여

Step 3 — Distractor Generation 모델 학습
  └─ Random forest binary classifier:
      "이 candidate가 plausible distractor인가?"
  └─ 학습 데이터: 실제 시험 문항의 false answer (positive)
                  + 무작위 표현 (negative)
  └─ 입력 특징 φ(q, a*, a'):
      WordNet 유사도, 분포 의미, POS, phonetic 등 다수

Step 4 — Crowd 검수·수정 (AMT, $0.20/HIT)
  └─ 모델이 제안한 top distractor 후보들 제시
  └─ 워커가 선택 / 수정 / 새로 생성
  └─ 최종 distractor 중 36.1%가 모델 직접 생성, 약 50%는 워커 수용

Step 5 — Quality validation
  └─ Distinguishability test: 별도 워커에게 SciQ + 실제 시험 문제 혼합 제시
      → "구별 불가" → SciQ가 실제 시험 수준 품질
  └─ Support passage가 대부분 문항에 첨부

Step 6 — Split 및 공개
  ┌─────────────┬────────┬─────────────────────────┐
  │             │ MC ver │ Direct-answer ver       │
  ├─────────────┼────────┼─────────────────────────┤
  │ Train       │ 11,679 │ 10,481                  │
  │ Validation  │  1,000 │    887                  │
  │ Test        │  1,000 │    884                  │
  ├─────────────┼────────┼─────────────────────────┤
  │ Total       │ 13,679 │ 12,252                  │
  └─────────────┴────────┴─────────────────────────┘
  (direct-answer가 작은 이유: 일부 passage는 저작권상 비공개)
  공개처: AllenAI / huggingface.co/datasets/allenai/sciq
  Total budget: $10,415
```

## 제공 필드 구조

| Field | Description |
|---|---|
| `question` | 과학 문제 텍스트 |
| `correct_answer` | 정답 선택지 |
| `distractor1` / `distractor2` / `distractor3` | 오답 선택지 3개 |
| `support` | 정답 근거 단락 (대부분 문항 포함, MC 버전에서는 추론에 미사용) |

## 실제 문항 예시 (논문 Fig. 1, training set 첫 4개 verbatim)

### Example 1 — Biology (Mesophiles)
> **Q:** *"What type of organism is commonly used in preparation of foods such as cheese and yogurt?"*
>
> 1) **mesophilic organisms** ← 정답
> 2) protozoa
> 3) gymnosperms
> 4) viruses
>
> **Support:** *"Mesophiles grow best in moderate temperature, typically between 25°C and 40°C (77°F and 104°F). Mesophiles are often found living in or on the bodies of humans or other animals. The optimal growth temperature of many pathogenic mesophiles is 37°C (98°F), the normal human body temperature. Mesophilic organisms have important uses in food preparation, including cheese, yogurt, beer and wine."*

### Example 2 — Earth Science (Coriolis)
> **Q:** *"What phenomenon makes global winds blow northeast to southwest or the reverse in the northern hemisphere and northwest to southeast or the reverse in the southern hemisphere?"*
>
> 1) **coriolis effect** ← 정답
> 2) muon effect
> 3) centrifugal effect
> 4) tropical effect
>
> **Support:** *"Without Coriolis Effect the global winds would blow north to south or south to north. But Coriolis makes them blow northeast to southwest or the reverse in the Northern Hemisphere. The winds blow northwest to southeast or the reverse in the southern hemisphere."*

### Example 3 — Chemistry/Physics (Phase Change)
> **Q:** *"Changes from a less-ordered state to a more-ordered state (such as a liquid to a solid) are always what?"*
>
> 1) **exothermic** ← 정답
> 2) unbalanced
> 3) reactive
> 4) endothermic
>
> **Support:** *"Summary: Changes of state are examples of phase changes, or phase transitions. All phase changes are accompanied by changes in the energy of a system. Changes from a more-ordered state to a less-ordered state (such as a liquid to a gas) are endothermic. Changes from a less-ordered state to a more-ordered state (such as a liquid to a solid) are always exothermic."*

### Example 4 — Physics (Radioactive Decay)
> **Q:** *"What is the least dangerous radioactive decay?"*
>
> 1) **alpha decay** ← 정답
> 2) beta decay
> 3) gamma decay
> 4) zeta decay
>
> **Support:** *"All radioactive decay is dangerous to living things, but alpha decay is the least dangerous."*

### Example 5 (논문 p.2 본문 인용) — Force Reasoning
> *"With which force does the moon affect tidal movements of the oceans?"*
> → 자연 현상에 대한 추상적 이해 + 새로운 시나리오 적용을 요구 → 논문이 강조하는 "transfer of domain-specific background knowledge"의 대표 사례.

## 주요 평가 결과 (Table 2, MC version test set)

| Model | Accuracy |
|---|---|
| **Lucene** (IR retrieval, AllenAI textbooks) | **80.0** |
| Aristo (AllenAI과학시험 시스템) | 77.4 |
| AS Reader (neural) | 74.1 |
| GA Reader (neural) | 73.8 |
| TableILP (table-based) | 31.8 |
| **Humans** | **87.8 ± 0.045** |

**핵심 발견 #1**: Lucene IR baseline이 신경망 reader(AS/GA)을 **5–6pp 능가** — SciQ는 retrieval-heavy 데이터셋임을 입증. 실제 시험 환경에서도 retrieval-based가 우위.

**핵심 발견 #2**: TableILP는 hand-collected 백그라운드 표에 의존 → SciQ의 분야 다양성을 커버 못해 31.8%로 추락.

**핵심 발견 #3**: SciQ를 추가 학습 데이터로 활용 시 **실제 4th/8th-grade 과학 시험에서 +3.3% 정확도 향상** (AS/GA Reader) — 도메인 외 평가에서도 transfer 효과 입증.

### Direct-answer 버전 (BiDAF on passage + question)
- BiDAF: **EM 66.7% / F1 75.7%** — SQuAD 대비 EM 1.3% / F1 1.6% 낮음.
- 그러나 작은 학습 셋(10k)으로 SQuAD(87.5k)에 근접한 성능 도달.

## 한계점
- **난이도가 낮음**: 고등학교 ~ 학부 초반 수준 → 전문 연구 수준 QA 평가에는 부적합.
- **크라우드소싱 특성상 문항 품질 불균일**: 일부 단순 사실 회상, 일부 추론 필요.
- **재료과학·천문학·고급 수학 문항 거의 없음** — 28권 교과서가 covered 도메인 한정.
- **텍스트 기반만**: 이미지·수식·표 활용 문항 없음.
- **Distractor 품질의 휴리스틱 한계**: 36.1%가 모델 생성 → 일부 워커 수용 distractor의 plausibility는 random forest classifier의 feature에 좌우.
- **MC 버전에서 support passage 제외**: 시스템이 own background knowledge 사용해야 함 → 정통한 RAG 시스템과 fit하나 closed-book QA로는 어려움.

## 관련 정보
- **논문**: [ACL Anthology W17-4413](https://aclanthology.org/W17-4413/)
- **HuggingFace**: [allenai/sciq](https://huggingface.co/datasets/allenai/sciq)
- **AllenAI 공식**: [allenai.org/data/sciq](https://allenai.org/data/sciq)
- **예산**: $10,415 (논문 Section 3.2)
- **이 벤치마크를 사용한 논문**:
  - HoneyComb (EMNLP Findings 2024) — GPT-4 단독 90.84% → +HoneyComb 96.54% 달성
  - HiPerRAG (PASC 2025)
  - 다수 LLM-only QA 평가의 표준 sanity-check 셋
