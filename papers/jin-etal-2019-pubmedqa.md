---
title: "PubMedQA: A Dataset for Biomedical Research Question Answering"
bib_key: "jin-etal-2019-pubmedqa"
year: 2019
domain: medical
type: benchmark
venue: EMNLP-IJCNLP 2019
paper_link: https://aclanthology.org/D19-1259/
---
# PubMedQA: A Dataset for Biomedical Research Question Answering

> EMNLP-IJCNLP 2019 | Benchmark | medical

## 한 줄 요약
PubMed 초록 중 **질문 제목 + 구조화된 초록**을 가진 논문에서 자동/수동으로 구성한 yes/no/maybe QA 벤치마크. **PQA-L (1k 전문가 주석) + PQA-U (61.2k 미주석) + PQA-A (211.3k 자동 생성)** 의 3분할로, 정량적 추론(quantitative reasoning)이 필수인 최초의 생의학 QA 데이터셋.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — PubMed 후보 추출 (25M references)
  └─ 필터 1: 제목에 물음표(?) 포함 → ~760k articles
  └─ 필터 2: 구조화 초록 보유 (Methods/Results/Conclusions) → ~120k
  └─ 결과: pre-PQA-U (yes/no/maybe로 답할 수 있을 후보)

Step 2 — 인스턴스 4-tuple 구성
  각 article에서:
  ┌────────────────┬───────────────────────────────────────┐
  │ Question       │ 원래 논문 제목 (e.g. "Do statins...?")│
  │ Context        │ 구조화 초록 − Conclusion section      │
  │ Long Answer    │ Conclusion section 자체               │
  │ Yes/No/Maybe   │ Long Answer를 요약한 단일 레이블      │
  └────────────────┴───────────────────────────────────────┘

Step 3 — PQA-L 1,000개 (전문가 주석, Algorithm 1)
  └─ 2,173 후보 중 1,091개 (50.2%) 는 yes/no/maybe 답변 불가로 제거
     (wh-question / multiple-choice 형식 등)
  └─ 두 명의 M.D. candidate 어노테이터:
     · Annotator 1: question + context + long answer → label (reasoning-free)
     · Annotator 2: question + context 만 → label (reasoning-required)
     · 두 레이블 동일 → 채택 / 불일치 → 합의 도출 (불가 시 인스턴스 제거)
  └─ 500개 = 10-fold cross-validation, 나머지 500개 = test set

Step 4 — PQA-U 61.2k (미주석, 반지도학습용)
  pre-PQA-U 중 PQA-L에 미포함된 yes/no/maybe-answerable 인스턴스.
  Rule-based 필터(wh-words / multi-entity selection 제거)로 식별
  → Annotator 1과 93% 일치율 검증

Step 5 — PQA-A 211.3k (자동 생성, 사전학습용)
  └─ Statement title (POS 태그 NP-(VBP/VBZ), Stanford CoreNLP)
  └─ Copula/auxiliary verb 추가로 question으로 변환
     · "Statins reduce AF." → "Do statins reduce AF?"
  └─ VB의 negation status로 Yes/No 자동 부여 (Maybe 없음)
  └─ 200k = 학습 / 11.3k = 검증
```

---

## 데이터셋 통계

| 항목 | PQA-L | PQA-U | PQA-A |
|---|---|---|---|
| QA pair 수 | 1.0k | 61.2k | 211.3k |
| Yes (%) | **55.2** | – | **92.8** |
| No (%) | **33.8** | – | **7.2** |
| Maybe (%) | **11.0** | – | 0.0 |
| 평균 질문 길이 (tok) | 14.4 | 15.0 | 16.3 |
| 평균 context 길이 (tok) | 238.9 | 237.3 | 238.0 |
| 평균 long answer 길이 (tok) | 43.2 | 45.9 | 41.0 |

---

## 실제 문항 형식 예시

> **Question.** Do preoperative statins reduce atrial fibrillation after coronary artery bypass grafting?
>
> **Context.**
> *(Objective)* Recent studies have demonstrated that statins have pleiotropic effects, including anti-inflammatory effects and AF preventive effects [...]
> *(Methods)* 221 patients underwent CABG in our hospital from 2004 to 2007. 14 patients with preoperative AF and 4 with valve surgery [...]
> *(Results)* The overall incidence of postoperative AF was 26%. Postoperative AF was significantly lower in the Statin group compared with the Non-statin group (**16% versus 33%, p=0.005**). [...]
>
> **Long Answer.** *(Conclusion)* Our study indicated that preoperative statin therapy seems to reduce AF development after CABG.
>
> **Answer:** **yes**

→ 핵심 supporting fact는 Results의 통계 비교(16% vs 33%, p=0.005). 추론 타입은 *Inter-group comparison* (57.5% of PQA-L에서 가장 흔함).

---

## 질문/추론 타입 분포 (PQA-L 200개 샘플 분석)

| 질문 타입 | % | 예시 |
|---|---|---|
| Does a factor influence the output? | 36.5 | "Does ibuprofen increase perioperative blood loss?" |
| Is a therapy good/necessary? | 26.0 | "Should circumcision be performed in childhood?" |
| Is a statement true? | 18.0 | "Sternal fracture in growing children: a rare and overlooked fracture?" |
| Is a factor related to the output? | 18.0 | "Can PRISM predict length of PICU stay?" |

| 추론 타입 | % |
|---|---|
| Inter-group comparison | **57.5** |
| Interpreting subgroup statistics | 16.5 |
| Interpreting (single) group statistics | 16.0 |
| **정량적 내용 추론이 필수인 비율** | **96.5%** |

---

## 주요 평가 결과 (PQA-L test 500개 기준)

| Model | Accuracy | Macro F1 |
|---|---|---|
| Majority baseline | 55.2% | – |
| BioBERT multi-phase fine-tuning + LongAnswer BoW supervision | **68.1%** | 52.8% |
| Human single performance | 78.0% | 72.2% |

**핵심 발견:** 최고 성능 모델도 인간보다 **9.9%p 낮음** → quantitative reasoning이 RAG / LLM에게 여전히 미해결 과제.

---

## 한계점
- **Clinical study 토픽 편중**: MeSH 분포에서 Pregnancy Outcome / Socioeconomic Factors / Risk Assessment / Survival Analysis 등이 일반 PubMed 대비 과대표상 (p < 0.05, two-proportion z-test).
- **PQA-A는 Maybe 없음**: 자동 생성 규칙(negation status 기반)이 binary만 지원 → 불확실성 학습 신호 부족.
- ~50%의 question-titled PubMed 논문은 yes/no/maybe로 답할 수 없음 (wh-question / multi-choice) → 후보군 좁음.
- 어노테이션 오류율 ~1% (두 어노테이터가 같은 실수를 한 경우, 인간 단일 성능 22% 오류율의 제곱).

---

## 관련 정보
- **논문**: [aclanthology.org/D19-1259](https://aclanthology.org/D19-1259/) (Jin et al., EMNLP-IJCNLP 2019, pp.2567–2577)
- **arXiv**: [1909.06146](https://arxiv.org/abs/1909.06146)
- **데이터셋**: [pubmedqa.github.io](https://pubmedqa.github.io)
- **이 벤치마크를 사용한 주요 후속 작업**: MIRAGE/MEDRAG (Xiong et al., ACL 2024) — PQA-L에서 context를 제거하여 RAG 평가용으로 재구성
