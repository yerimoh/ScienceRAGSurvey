---
title: "Davis Kinase Inhibitor Selectivity Dataset: Comprehensive Kd Matrix"
bib_key: "davis2011kinase"
year: 2011
domain: chem, bio, medical
type: benchmark
venue: Nature Biotechnology
paper_link: https://doi.org/10.1038/nbt.1990
---
# Davis Dataset: 72 Kinase Inhibitors × 442 Kinases Comprehensive Kd Matrix

> Nature Biotechnology 29(11):1046–1051 | 2011 | Benchmark (DTI regression canonical) | chem · bio · medical
> Mindy I. Davis, Jeremy P. Hunt, Sanna Herrgard, Pietro Ciceri, Lisa M. Wodicka, Gabriel Pallares, Michael Hocker, Daniel K. Treiber, Patrick P. Zarrinkar — DiscoveRx Corporation
> DOI: [10.1038/nbt.1990](https://doi.org/10.1038/nbt.1990) · PMID 22037378

## 한 줄 요약
**72개 kinase inhibitor × 442개 kinase** (human catalytic protein kinome의 >80% 커버)의 결합 친화도(**Kd**)를 종합 측정한 대규모 DTI 매트릭스. drug-target interaction **regression** task의 표준 benchmark로 거의 모든 DTI 논문에 등장.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Kinase panel 구축
  └─ Human catalytic protein kinome >80% 커버
  └─ 442 kinases (type I + type II + atypical kinases)
  └─ DiscoveRx KINOMEscan platform 사용

Step 2 — Inhibitor 선정
  └─ 72 commercially available kinase inhibitors
  └─ Type I (ATP-competitive) + Type II (allosteric) 혼합
  └─ Pre-clinical → marketed drugs (예: imatinib, dasatinib, sunitinib)

Step 3 — Kd 측정
  └─ Competition binding assay (KINOMEscan)
  └─ Dissociation constant Kd (nM 단위)
  └─ 모든 (inhibitor, kinase) 쌍에 대해 측정
  └─ Sparsity 일부 있음 (결합 약한 쌍 제외)

Step 4 — Type I vs Type II 비교 분석
  └─ Type II 일반적으로 더 선택적
  └─ "Group-selective" inhibitor 패턴 발견
  └─ Understudied kinase의 도구 화합물 식별
```

---

## 원문 직접 인용 (Davis 2011 Nat Biotechnol §Abstract)

> "We evaluate the **interaction of 72 kinase inhibitors with 442 kinases**, covering **>80% of the human catalytic protein kinome**."

> "Type II inhibitors are more selective than type I inhibitors, but there are exceptions."

> "We identify **group-selective** inhibitors that target specific kinase subfamilies while remaining selective elsewhere, providing a resource for identifying appropriate tool compounds for understudied kinases."

---

## 데이터셋 통계 (DTI benchmark perspective)

| 항목 | 수치 |
|---|---|
| Inhibitor 수 | 72 |
| Kinase 수 | 442 (human catalytic kinome >80%) |
| Assay | KINOMEscan competition binding |
| Output unit | Kd (nM) |
| Sparsity | 측정된 쌍만 보고 (~약 30% 활성) |
| Subset 통상 사용 | DeepDTA 등 모델 평가 시 68 × 442 reduced |

---

## 주요 활용

| 항목 | 내용 |
|---|---|
| Task 정의 | Drug-Target Interaction (DTI) regression |
| Metric | RMSE, MSE, CI (Concordance Index), Spearman |
| Pairing | KIBA (Tang 2014)와 함께 보고되는 표준 짝꿍 |
| Pioneer 모델 | DeepDTA (Öztürk 2018), GraphDTA, MolTrans 등 |
| TDC 통합 | `multi_pred.DTI.DAVIS` |

---

## 한계점
- **단일 assay platform**: KINOMEscan 의존 → 다른 assay 결과와 차이 가능
- **Sparsity**: 측정되지 않은 쌍 다수 → matrix completion task로도 활용
- **In vitro only**: 세포 내 효과 미반영
- **Kinase family bias**: catalytic kinase 위주, pseudokinase 미포함
- **시간**: 2011년 데이터, 최신 inhibitor (kinase degrader 등) 미반영

---

## 관련 정보
- **논문 (DOI)**: [10.1038/nbt.1990](https://doi.org/10.1038/nbt.1990)
- **PubMed**: [PMID 22037378](https://pubmed.ncbi.nlm.nih.gov/22037378/)
- **DiscoveRx KINOMEscan**: [discoverx.com/kinomescan](https://www.discoverx.com)
- **공식 데이터**: published in paper supplementary; TDC `DAVIS` task에서 표준화
- **이 benchmark를 사용한 주요 작업**: DeepDTA (Öztürk 2018), GraphDTA (Nguyen 2021), MolTrans (Huang 2020), 거의 모든 DTI deep learning 논문
