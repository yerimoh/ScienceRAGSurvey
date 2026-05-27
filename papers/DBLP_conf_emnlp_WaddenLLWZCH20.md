---
notion_id: 355f2dcd-4912-812a-bbf9-cf63ebea591e
title: "SciFact: Fact or Fiction — Verifying Scientific Claims"
bib_key: DBLP:conf/emnlp/WaddenLLWZCH20
year: 2020
domain: bio, medical
type: benchmark
venue: EMNLP 2020
paper_link: https://aclanthology.org/2020.emnlp-main.609/
---
# SciFact: 1,409 Expert-Written Scientific Claims with Rationale Annotation

> EMNLP 2020 (Long Paper, pp. 7534–7550) | Benchmark + Baseline (VERISCI) | bio · medical
> David Wadden, Shanchuan Lin, Kyle Lo, Lucy Lu Wang, Madeleine van Zuylen, Arman Cohan, Hannaneh Hajishirzi — AI2 / Univ. of Washington
> DBLP: `conf/emnlp/WaddenLLWZCH20` · arXiv: [2004.14974](https://arxiv.org/abs/2004.14974)

## 한 줄 요약
과학 문헌에서 단일 atomic claim에 대해 **SUPPORTS / REFUTES / NOINFO** verdict를 부여하고 그 verdict를 정당화하는 **rationale 문장**까지 식별하는 task와, **1,409개 전문가 작성 claim** 으로 구성된 데이터셋. **abstract-level F1 + sentence-level (rationale) F1** 두 단위로 평가하는 verification benchmark의 표준.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Citation sentence 수집 (자연 발생 claim 출처)
  └─ S2-ORC corpus의 인용 문장(citation sentence) 추출
  └─ 인용 문장 ≈ 다른 논문의 결과를 진술하는 "natural claim"
  └─ 합성(synthetic) FEVER claim 대신 실제 과학 문헌에서 사용된 주장 채택

Step 2 — Claim 재작성 (전문가 annotators)
  └─ Annotators: biomedical research 학위/배경자
  └─ citation 문장을 atomic claim으로 변환
  └─ 예: "X reduces Y by Z% (p<0.001)" → "X reduces Y"

Step 3 — 증거 abstract 식별 + rationale 주석
  ┌───────────────────────────────────────────────┐
  │ 각 claim에 대해:                              │
  │   1. SUPPORTS / REFUTES / NOINFO abstract 식별│
  │   2. rationale 문장 표시 (Lei et al. 2016식)  │
  │      = verdict 근거 문장 (claim당 평균 1-3개)  │
  └───────────────────────────────────────────────┘
  Sentence-level rationale 주석 신뢰도:
    Cohen's κ = 0.71 (저자 보고)

Step 4 — 최종 데이터셋 구성
  ┌────────────────────┬──────────────────┐
  │ 항목               │ 규모              │
  ├────────────────────┼──────────────────┤
  │ Claim 수            │ 1,409            │
  │ Evidence-bearing   │ ~5,183 abstracts  │
  │ 평균 rationale     │ 1.7 문장/abstract │
  │ Split              │ train/dev/test    │
  │ Label 분포         │ SUPP/REFUTE/NEI   │
  └────────────────────┴──────────────────┘
```

---

## 원문 직접 인용 (arXiv:2004.14974 §본문)

> **Task 정의**: *"search literature containing evidence that **SUPPORTS or REFUTES** a given scientific claim, and to identify **rationales** justifying each decision"*

> **데이터셋 규모**: *"we construct SCIFACT, an expert-annotated dataset of **1,409 scientific claims** accompanied by abstracts that support or refute each claim, and annotated with **rationales** (Lei et al., 2016) justifying each SUPPORTS / REFUTES decision"*

> **레이블 체계**: *"labels each abstract as **SUPPORTS, REFUTES, or NOINFO** with respect to the claim"*

> **Annotation 출처 (자연 claim)**: *"we develop a novel annotation protocol in which annotators **re-formulate naturally occurring claims** in the scientific literature – citation sentences – into atomic scientific claims"*

> **Sentence-level 신뢰도**: *"sentence-level agreement. The resulting **Cohen's κ is 0.71**"*

> **FEVER와의 차이**: *"claims in the popular FEVER dataset (Thorne et al., 2018) are **synthetic**, since they are created by annotators by mutating sentences from Wikipedia"* → SciFact는 자연 발생 citation 활용

---

## Input / Output

### Input
| 항목 | 설명 |
|---|---|
| Claim | 자연어 atomic 과학 진술 (citation sentence 재작성) |
| Corpus | ~5,183 biomedical research abstracts |
| Task setting | (1) **Oracle abstract** (gold abstract 주어짐) / (2) **Open** (TF-IDF로 코퍼스 전체 검색) |

### Output + Evaluation Metrics
| 단위 | Metric | 의미 |
|---|---|---|
| **Abstract-level** | F1 (label) | claim ↔ abstract verdict (SUPP/REFUTE/NOINFO) 정확도 |
| **Sentence-level** | F1 (rationale) | 어떤 문장이 verdict의 근거인지 정확도 |

→ **두 단위 F1을 동시 평가**하는 것이 SciFact의 정체성. 단순 accuracy benchmark와 구분되는 핵심.

---

## 실제 Claim 예시 (논문 Table 1 + Fig 1 verbatim, COVID-19 데모)

### 예시 1 — 동일 claim에 대한 SUPPORTS / REFUTES evidence 양립
> **Claim**: *"Lopinavir / ritonavir have exhibited favorable clinical responses when used as a treatment for coronavirus."*
>
> **Supports (verbatim)**: *"...after lopinavir/ritonavir (Kaletra, AbbVie) was administered, β-coronavirus viral loads significantly decreased and no or little coronavirus titers were observed..."*
>
> **Refutes (verbatim)**: *"The focused drug repurposing of known approved drugs (such as lopinavir/ritonavir) has been reported failed for curing SARS-CoV-2 infected patients..."*

### 예시 2 — 기후 의존성 (단방향 어휘 검증 필요)
> **Claim**: *"The coronavirus cannot thrive in warmer climates."*
>
> **Supports**: *"...most outbreaks display a pattern of clustering in relatively cool and dry areas...unsuitable climates can cause the virus to destabilize quickly..."*
>
> **Refutes**: *"...significant cases in the coming months are likely to occur in more humid (warmer) climates, irrespective of the climate-dependence of transmission..."*

### 예시 3 — Statistical reasoning + 단방향 검증
> **Claim**: *"Cardiac injury is common in critical cases of COVID-19."*
>
> **Rationale 검증 포인트** (논문 §본문 인용):
> - 단방향 관계: *"replacing higher with lower would cause the rationale to REFUTE the claim rather than SUPPORT it"*
> - 통계적 유의성: *"the system should interpret **p < 0.001** as an indication that the reported finding is statistically significant"*

---

## VERISCI 베이스라인 (저자가 함께 제안한 3-stage pipeline)

```
[Claim 입력]
     │
     ▼
┌──────────────────────────────────┐
│ Step 1 — ABSTRACTRETRIEVAL        │
│   TF-IDF (unigram + bigram)       │
│   top-k = 3 abstracts             │
└──────────┬────────────────────────┘
           ▼
┌──────────────────────────────────┐
│ Step 2 — RATIONALESELECTION       │
│   RoBERTa-large sentence selector │
│   rationale 문장 이진 분류        │
└──────────┬────────────────────────┘
           ▼
┌──────────────────────────────────┐
│ Step 3 — LABELPREDICTION          │
│   RoBERTa-large classifier        │
│   SUPPORTS / REFUTES / NOINFO     │
└──────────┬────────────────────────┘
           ▼
   [Verdict + rationale 문장들]
```

**도메인 적응 실험 결과 (논문 §6)**: FEVER (Wikipedia) + Wikipedia 일반 claim 등 추가 학습 시 SciFact 성능 향상 → "simple domain adaptation techniques substantially improve performance" (§Abstract).

---

## 주요 평가 결과 (논문 본문 Table 3·4)

| Setting | Abstract Label-Only F1 | Abstract Label+Rationale F1 |
|---|---|---|
| Oracle Abstract (gold 주어짐) | ~89.7% | ~72.6% |
| Oracle Rationale (rationale 주어짐) | – | ~72.0% |
| **Open (TF-IDF 검색)** | ~64.1% | **~46.4%** |

→ Open setting에서 큰 폭의 성능 저하 → retrieval이 verification 성공의 큰 bottleneck.
→ Label+Rationale F1이 Label-Only F1보다 ~17%p 낮음 → rationale 식별이 label 추론보다 어려운 task.

---

## COVID-19 zero-shot 검증 케이스 (논문 §본문 인용)

> *"We showcase the ability of our model to verify expert-written claims concerning the novel coronavirus COVID-19 against the newly-released **CORD-19 corpus** (Wang et al., 2020). Expert annotators judge retrieved evidence to be plausible for **23 of 36 claims**."*

→ 실제 의료 위기 상황에서 zero-shot 일반화 가능성 시연. SciFact 학습 모델이 새 도메인(COVID-19)에 즉시 적용 가능.

---

## 핵심 기여
1. **Scientific Claim Verification** task 공식화 (claim → abstract → label + rationale)
2. **1,409개 전문가 주석 claim 데이터셋** (citation sentence 기반의 자연 claim)
3. **VERISCI 베이스라인** 및 도메인 적응 학습 효과 입증 (FEVER 사전학습 → SciFact 향상)
4. **Sentence-level + Abstract-level F1 동시 평가** 프로토콜 정립

---

## 한계점
- **소규모**: 1,409 claim, ~5,183 abstract corpus → SciFact-Open (500K)으로 확장됨
- **단방향 평가**: 단일 (claim, abstract) 쌍 단위; 다중 abstract 간 모순/통합 미평가
- **Citation sentence 출처 편향**: 인용 문장 기반이라 review-style claim에 편향 가능
- **인과관계·통계 해석 한계**: VERISCI는 p-value, 신뢰구간, coreference 해결에서 오류
- **Sentence-level 어려움**: rationale 식별이 abstract-level label 추론보다 더 어려움

---

## 관련 정보
- **논문 (ACL Anthology)**: [2020.emnlp-main.609](https://aclanthology.org/2020.emnlp-main.609/)
- **arXiv**: [2004.14974](https://arxiv.org/abs/2004.14974)
- **DOI**: [10.18653/v1/2020.emnlp-main.609](https://doi.org/10.18653/v1/2020.emnlp-main.609)
- **DBLP**: [conf/emnlp/WaddenLLWZCH20](https://dblp.org/rec/conf/emnlp/WaddenLLWZCH20.html)
- **GitHub**: [allenai/scifact](https://github.com/allenai/scifact)
- **확장**: **SciFact-Open** (Wadden et al., EMNLP Findings 2022) — 500K abstract pool로 open-domain 평가
- **이 benchmark를 사용한 후속 작업**: VerT5erini, ParagraphJoint, MultiVerS, OpenScholar (citation F1 평가에도 활용)
