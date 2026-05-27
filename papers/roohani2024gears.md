---
title: "Predicting transcriptional outcomes of novel multigene perturbations with GEARS"
bib_key: "roohani2024gears"
year: 2024
domain: bio
type: Method
venue: Nature Biotechnology 42:927-935
paper_link: https://doi.org/10.1038/s41587-023-01905-6
---
# GEARS: GNN over gene-gene KG predicts unseen single- and multi-gene perturbations

> Nature Biotechnology 42(6):927-935 | 2024 | Method (cellular perturbation prediction with held-out eval protocol) | bio
> Yusuf Roohani, Kexin Huang, Jure Leskovec — Stanford SNAP / Genentech
> DOI: [10.1038/s41587-023-01905-6](https://doi.org/10.1038/s41587-023-01905-6) · GitHub: [snap-stanford/GEARS](https://github.com/snap-stanford/GEARS)

## 한 줄 요약
**Single-cell perturbation 효과 예측을 위한 GNN 모델** — Gene Ontology / co-expression 기반 **gene-gene knowledge graph**를 perturbation 임베딩과 결합하여 **학습 중 본 적 없는 single-gene 또는 multi-gene perturbation의 전사체 반응**을 예측. 평가는 Norman 2019 (102 single + 131 two-gene) / Adamson 2016 / Dixit 2016 위에서 **MSE on top-20 DEG / Pearson / Precision@10 for GI prediction**.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문제 인식
  ┌──────────────────────────────────────────────┐
  │ - Perturb-seq 실험 가능한 조합 < 10⁻⁶          │
  │   (20K 유전자 × 20K = 4억 dual pair)          │
  │ - 기존 모델은 학습에서 본 perturbation만 예측 │
  │   → unseen perturbation으로의 일반화 부족    │
  │ - 특히 dual-gene 효과는 단순 가산이 아님       │
  │   (GI: synergy, suppression, redirection 등)  │
  └──────────────────────────────────────────────┘

Step 2 — GEARS 모델 구조
  ┌──────────────────────────────────────────────┐
  │ (1) Gene-gene knowledge graph 입력            │
  │     - Gene Ontology (functional similarity)   │
  │     - Co-expression network                   │
  │  → GNN으로 gene-level embedding 학습          │
  │                                              │
  │ (2) Perturbation embedding                    │
  │     - 각 perturbed gene의 GNN embedding 사용 │
  │     - Multi-gene: 임베딩 합산                 │
  │                                              │
  │ (3) Cell-state decoder                        │
  │     - control cell expression + pert embed   │
  │     → predicted post-perturbation expression  │
  └──────────────────────────────────────────────┘

Step 3 — Held-out evaluation protocol (논문 contribution)
  ┌──────────────────────────────────────────────┐
  │ Single-gene splits:                           │
  │  · Seen: same perturbation, different cells   │
  │  · Unseen: perturbation never in training    │
  │                                              │
  │ Two-gene splits:                              │
  │  · Seen-Seen: both A and B individually seen │
  │  · Seen-Unseen: A seen, B unseen             │
  │  · Unseen-Unseen: neither in training        │
  └──────────────────────────────────────────────┘

Step 4 — Dataset 평가 (3개 핵심 dataset)
  ┌──────────────┬──────────┬──────────────────┐
  │ Dataset       │ Perts     │ 활용              │
  ├──────────────┼──────────┼──────────────────┤
  │ Norman 2019   │ 102 sg + 131 dg │ canonical dual-gene  │
  │ Adamson 2016  │ ~87 single  │ UPR pathway          │
  │ Dixit 2016    │ ~24 single  │ early Perturb-seq    │
  │ Replogle 2022 │ essential gene-scale │ added later (preprocessor) │
  └──────────────┴──────────┴──────────────────┘

Step 5 — 평가 metric (논문 §Methods)
  · MSE on top-20 DEG (differentially expressed genes)
  · Pearson correlation (predicted vs observed Δ expression)
  · Precision@10 for GI subtype classification
    (synergy / suppression / redirection / etc.)
  · Jaccard similarity of DEG sets
```

---

## 실제 데이터 형식 예시 (논문 §Methods + GitHub README)

### 유형 A — Single-gene perturbation training example

> **Input**:
> ```
> Control cell expression: (n_genes,) vector
> Perturbed gene: 'CEBPA' (Hugo symbol)
> Cell-line / batch covariate
> ```
>
> **Label**:
> ```
> Post-perturbation expression: (n_genes,) vector
> (averaged or per-cell distribution)
> ```

### 유형 B — Two-gene combinatorial perturbation

> **Input**:
> ```
> Perturbed genes: ('CEBPA', 'CEBPB')
> Cell-line / batch
> ```
>
> **Splits** (test setting):
> ```
> Seen-Seen:    train has CEBPA single + CEBPB single
> Seen-Unseen:  train has CEBPA single but CEBPB never seen
> Unseen-Unseen: train has neither
> → harder splits = more realistic generalization test
> ```

### 유형 C — GI (Genetic Interaction) subtype classification

> Predicted dual-gene response vs additive single effects:
> ```
> Predicted GI types (논문 Fig. 4):
>   · NEOMORPHIC: novel program (A+B ≠ A union B)
>   · REDUNDANT: same program (A+B ≈ A ≈ B)
>   · SUPPRESSOR: B suppresses A (A+B → control)
>   · EPISTASIS_A: A dominates (A+B ≈ A)
>   · POTENTIATION: B amplifies A
>   · ADDITIVE: A+B = A + B (linear baseline)
> ```
>
> Metric: Precision@10 — top-10 predicted GIs match ground-truth class

### 유형 D — Python API (GitHub README)

```python
from gears import PertData, GEARS
pert_data = PertData('./data')
pert_data.load(data_name='norman')                # 102 single + 131 dual
pert_data.prepare_split(split='simulation', seed=1)
gears_model = GEARS(pert_data, device='cuda:0')
gears_model.model_initialize(hidden_size=64)
gears_model.train(epochs=20)
# Metric: MSE top-20 DEG, Pearson, Precision@10
```

---

## 평가 framework 요약

| Metric | 의미 | 우선순위 |
|---|---|---|
| **MSE on top-20 DEG** | 가장 변화 큰 20개 유전자에서의 예측 정확도 | Primary |
| **Pearson correlation** | Δexpression 예측 vs 실측 상관 | Primary |
| **Precision@10 (GI)** | Top-10 예측 GI subtype 정확도 | Primary |
| **Jaccard similarity** | 예측 DEG set ∩ 실측 DEG set | Secondary |

→ **단순 MSE만 보면 부족** — Norman 2019의 control 평균이 baseline으로 강하기 때문. Top-20 DEG로 perturbation-specific signal 측정.

---

## 주요 결과 (논문 본문)

| 비교 | 결과 |
|---|---|
| Single-gene unseen | GEARS > scGen, CPA baselines |
| Two-gene seen-seen | GEARS ≈ linear baseline (대부분 가산) |
| Two-gene seen-unseen | GEARS > all baselines (gene-gene KG 효과) |
| Two-gene unseen-unseen | 가장 어려움, 모든 모델 낮은 성능 |
| GI subtype prediction | NEOMORPHIC/REDUNDANT 예측 가능 |

→ "When trained on single-gene perturbation data alone, GEARS cannot reliably predict outcomes for combinatorial perturbations" (GitHub README, 한계 명시).

---

## 한계점
- **Single-only training으로는 dual 예측 한계** (저자 GitHub README 명시)
- **Knowledge graph 의존**: GO/co-expression KG 품질이 결정적
- **Cell-line dependency**: K562 (Norman) 학습 → 다른 cell type 일반화 제한
- **Single-cell transcriptomics만**: protein, phenotype, organelle 미커버
- **Computational cost**: 큰 GNN, MPS hardware 필수
- **PerturBench (Wu 2024)에서 ablation 시**: GEARS가 단순 Latent Additive baseline과 거의 동등

---

## 관련 정보
- **논문 (Nat. Biotechnol.)**: [10.1038/s41587-023-01905-6](https://doi.org/10.1038/s41587-023-01905-6)
- **GitHub**: [snap-stanford/GEARS](https://github.com/snap-stanford/GEARS) (`pip install cell-gears`)
- **저자 소속**: Stanford SNAP (Jure Leskovec lab) + Genentech
- **이 모델이 사용한 dataset**: [[norman2019exploring]] (102 sg + 131 dg), Adamson 2016 (UPR), Dixit 2016 (TF), Replogle 2022 (essential)
- **이 모델을 평가한 benchmark**: [[DBLP:journals/corr/abs-2408-10609]] (PerturBench — GEARS와 baseline 비교)
- **후속 작업**: scFoundation, scGPT, STATE — 모두 GEARS와 baseline 비교
