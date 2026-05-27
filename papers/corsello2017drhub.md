---
title: "Drug Repurposing Hub: Hand-Curated Library of 4,707 Clinical Compounds"
bib_key: "corsello2017drhub"
year: 2017
domain: medical, chem
type: benchmark
venue: Nature Medicine
paper_link: https://doi.org/10.1038/nm.4306
---
# Drug Repurposing Hub: 4,707 Compounds + Targets Annotation

> Nature Medicine 23(4):405–408 (Correspondence) | 2017 | Benchmark / Resource | medical · chem
> Steven M. Corsello, Joshua A. Bittker, Zihan Liu, Joshua Gould, ..., Aravind Subramanian, Todd R. Golub — Broad Institute of MIT and Harvard
> DOI: [10.1038/nm.4306](https://doi.org/10.1038/nm.4306) · PMID 28388612

## 한 줄 요약
Broad Institute에서 **수작업으로 큐레이션한 4,707개 임상 화합물 라이브러리**. 그 중 **3,422개는 marketed / clinical trial 단계**, 나머지는 도구 화합물·withdrawn drugs. 50+ 화학 벤더에서 입수해 **identity verified + literature target annotated**. CLADD 등 RAG 시스템이 drug-target prediction의 GT로 사용.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Compound 큐레이션
  └─ Hand-curated 임상 화합물 list 구축
  └─ 50+ 화학 벤더에서 commercial 입수 (purity 검증)
  └─ Identity 확인 (mass spec, etc.)
  └─ 최종: 4,707 compounds

Step 2 — Clinical phase 분류
  ┌────────────────────────┬─────────┐
  │ Approved (marketed)    │ 다수     │
  │ Clinical trials        │         │
  │ ├─ Phase III           │         │
  │ ├─ Phase II            │         │
  │ └─ Phase I             │         │
  │ Tool compounds         │ 차이    │
  │ Withdrawn drugs        │         │
  ├────────────────────────┼─────────┤
  │ Total marketed/trialed │ 3,422   │
  │ Total                  │ 4,707   │
  │ QC-confirmed library   │ 1,988   │ (Figure 1)
  └────────────────────────┴─────────┘

Step 3 — Literature target annotation
  └─ 각 화합물에 대해 known protein targets 주석
  └─ Mechanism of Action (MOA) classification
  └─ Indication mapping (MeSH terms)

Step 4 — Online resource
  └─ broadinstitute.org/repurposing
  └─ Interactive search by compound / target / MOA / indication
```

---

## 원문 직접 인용 (Corsello 2017 Nat Med §본문)

> "we **hand-curated a collection of 4,707 compounds**, experimentally confirmed their identities, and annotated them with literature-reported targets"

> "The collection includes **3,422 drugs that are marketed around the world or that have been tested in human clinical trials**"

> "Compounds were obtained from more than 50 chemical vendors, and the **purity of each sample was established**"

> "we have created an online **Drug Repurposing Hub (http://www.broadinstitute.org/repurposing)** that contains detailed annotation for each of the compounds"

> "The final QC-confirmed library contains **1,988 drugs that are approved or marketed** for human use"

---

## 주요 활용

| 항목 | 내용 |
|---|---|
| Task 사용 사례 | Drug-target prediction GT (CLADD 등) |
| 검증 방식 | Zero-shot DTI prediction with held-out compounds |
| Annotation 수준 | Compound → Target (literature-derived) |
| 부가 정보 | MOA, indication, clinical phase, vendor |
| 후속 사용 | CLADD (AAAI 2026), 거의 모든 RAG drug-target 평가 |

---

## 데이터셋 통계

| 항목 | 수치 |
|---|---|
| Total compounds (큐레이션) | 4,707 |
| Marketed + clinical trial | 3,422 |
| QC-confirmed approved | 1,988 |
| Vendor sources | 50+ |
| Purity QC | All compounds verified |
| Target annotation | Literature-derived |
| Hosting | Broad Institute (broadinstitute.org/repurposing) |

---

## 한계점
- **2017년 cutoff**: 최신 신약 (예: GLP-1 agonists, ADC 등) 일부 미포함
- **Literature-derived targets**: 미확인 off-target 미반영
- **Hand-curated bias**: 큐레이터 우선순위에 따른 편향 가능
- **Withdrawn drugs 포함**: 안전성 문제 화합물도 library에 존재 (research용 용도)
- **Commercial availability 의존**: 일부 시판 중단 화합물 입수 제한
- **MOA granularity**: 일부 MOA는 broad/incomplete

---

## 관련 정보
- **논문 (DOI)**: [10.1038/nm.4306](https://doi.org/10.1038/nm.4306)
- **PubMed**: [PMID 28388612](https://pubmed.ncbi.nlm.nih.gov/28388612/)
- **공식 사이트**: [broadinstitute.org/repurposing](https://www.broadinstitute.org/repurposing)
- **데이터 다운로드**: clue.io/repurposing
- **이 자원을 사용한 주요 작업**: CLADD (DTI prediction, AAAI 2026), TDC subset, LINCS L1000 cross-reference
