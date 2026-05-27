---
title: "PerturBench: Benchmarking Machine Learning Models for Cellular Perturbation Analysis"
bib_key: "DBLP:journals/corr/abs-2408-10609"
year: 2024
domain: bio
type: benchmark
venue: arXiv 2024 (Altos Labs / UCL)
paper_link: https://arxiv.org/abs/2408.10609
---
# PerturBench: 6-dataset standardized benchmark for single-cell perturbation models

> arXiv 2024 (Altos Labs technical report) | Benchmark (cellular perturbation prediction) | bio
> Yan Wu, Esther Wershof, Sebastian M. Schmon, Marcel Nassar, Błażej Osiński, Ridvan Eksi, Zichao Yan, Rory Stark, Kun Zhang, Thore Graepel — Altos Labs / University College London
> arXiv: [2408.10609](https://arxiv.org/abs/2408.10609) · DBLP: `journals/corr/abs-2408-10609`

## 한 줄 요약
**단일세포 perturbation response 예측 모델**의 표준 평가를 위한 **6-dataset benchmark** (Srivatsan20 / Frangieh21 / Jiang24 / McFalineFigueroa23 / Norman19 / OP3) 와 **2 task family** (covariate transfer / combo prediction). RMSE + Pearson 같은 fit metric 외에 **rank-based metric** (perturbation 간 순서)을 도입해 mode-collapse 모델을 노출. CPA / SAMS-VAE / BioLord / GEARS / scGPT 등 published model + Latent Additive / Decoder-only baseline 비교.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 문제 인식: 기존 perturbation benchmark의 약점
  ┌──────────────────────────────────────────────┐
  │ - 데이터셋마다 다른 split / metric           │
  │ - rank-blind metric (RMSE/Pearson) 위주      │
  │   → Decoder-Only가 single mean으로 좋은 점수 │
  │ - 작은 dataset 위주 → real-world 미반영      │
  │ - scFM (scGPT 등) 평가 일관성 부재          │
  └──────────────────────────────────────────────┘

Step 2 — 6 dataset 선정 (≥100 perturbations 필수)
  ┌──────────────────┬──────┬──────┬─────────┬───────────┐
  │ Dataset           │ Sing │ Dual │ Modality│ Cells     │
  ├──────────────────┼──────┼──────┼─────────┼───────────┤
  │ Srivatsan20       │  188 │   0  │ chem    │ 178,213   │
  │ Frangieh21        │  248 │   0  │ genetic │ 218,331   │
  │ Jiang24            │  219 │   0  │ genetic │ 1,628,476 │
  │ McFalineFigueroa23│  525 │   0  │ genetic │ 892,800   │
  │ Norman19           │  155 │ 131  │ genetic │ 91,168    │
  │ OP3 (Szałata)      │  144 │   0  │ chem    │ 296,147   │
  └──────────────────┴──────┴──────┴─────────┴───────────┘

Step 3 — 2 task family 정의
  · Covariate transfer:
      train: pert A,B,C in cells X,Y
      test:  pert A,B,C in cells Z (unseen covariate)
  · Combo prediction (Norman19 only):
      train: all single + 30% of duals
      test:  remaining 70% of dual perturbations

Step 4 — Metric suite (fit + rank + distributional)
  · Fit metrics:
      - RMSE on aggregated response
      - cosine similarity of LogFC
  · Rank metrics (new contribution):
      - rank(X) = fraction of perturbations closer to
        prediction than the ground truth target
      - 0=perfect, 0.5=random, 1=worst
  · Distributional:
      - MMD (gene space + PCA top-256)
      - DEG recall (top-20 t-score)

Step 5 — Model zoo + baselines
  Published: CPA*, SAMS-VAE*, BioLord*, GEARS, scGPT
  Baselines: Latent Additive, Decoder-Only, Decoder(Cov), Linear
  Ablations: CPA*(noAdv), SAMS-VAE*(S)

Step 6 — Benchmarking rules
  · Optuna HPO 60+ trials × 6 parallel
  · Best HP selected on RMSE + 0.1*rankRMSE
  · 4 seeds × best HP for stability
```

---

## 실제 데이터 형식 예시 (논문 §2 + Table 1 + Figure 2)

### 유형 A — Single-cell perturbation dataset record

> **Input**: control cell expression vector + perturbation metadata (covariate + pert ID)
>
> ```
> Cell shape:  (cells, genes) ~ (218,331 × ~33,000) for Frangieh21
> Pert metadata: (perturbation ID, target gene(s), covariate cell line)
> Covariate:   batch / cell type / dose
> ```
>
> **Output / Label**: post-perturbation cell expression vector (same gene shape)

### 유형 B — Covariate transfer task (5 datasets)

> ```
> Train: cells with covariate C1, C2 — all perturbations A,B,C
> Test:  cells with covariate C3 (unseen) — same perturbations A,B,C
> Model task: predict cell state under perturbation in unseen covariate
> Real-world analog: drug effect in unseen cell line / tissue
> ```

### 유형 C — Combinatorial prediction task (Norman19)

> ```
> Train: 155 single + 30% of 131 dual perturbations
> Test:  70% of dual perturbations (held out)
> Model task: predict A+B response from A and B single effects
> ```

### 유형 D — Rank metric calculation (논문 Figure 2)

> ```
> Predicted pert X embedding ≈ control population mean
> Compute cosine similarity to all known perturbations
> rank(X) = position of X in sorted list / total perts
>        0 = perfect (X closest to itself)
>        0.5 = random ordering
>        1 = X furthest from its true target
> → catches mode-collapse: Decoder-only has good RMSE but rank≈0.5
> ```

---

## 평가 framework 요약

| Category | Metric | 목적 |
|---|---|---|
| **Fit** | RMSE | average response 정확도 |
| Fit | cosine LogFC | LogFC 방향 일치 |
| **Rank** | rank RMSE | mode-collapse 탐지 |
| Rank | rank cosine | specificity 측정 |
| **Distributional** | MMD (gene) | full distribution 일치 |
| Distributional | MMD PCA (top-256) | latent 분포 일치 |
| Distributional | DEG recall (top-20 t-score) | DEG 회수율 |

→ 핵심 contribution: **rank metric** — RMSE만 보면 Decoder-Only가 모든 perturbation을 single mean으로 예측해도 좋게 보이지만, rank ≈ 0.5로 즉시 노출.

---

## 주요 결과 (논문 §5)

| 발견 | 의미 |
|---|---|
| Adversarial 제거한 CPA*(noAdv)가 CPA*보다 항상 좋음 | adversarial component가 도움 안 됨 |
| Sparsity 제거한 SAMS-VAE*(S)가 SAMS-VAE*보다 항상 좋음 | sparse mask 가정이 오히려 손실 |
| Latent Additive baseline이 published 모델과 동등 또는 우위 | 단순 모델이 일반적으로 충분 |
| Decoder-Only는 RMSE 양호하나 rank ≈ 0.5 | mode-collapse, rank metric 필요 |
| scGPT 임베딩 사용 시 marginal 개선만 | scFM가 perturbation에 큰 효과 없음 |
| Norman19 combo prediction: linear model도 강함 | dual 효과가 대부분 linear |

→ **결론**: "no single model architecture clearly outperforms others, simpler architectures are generally competitive and scale well with larger datasets" (논문 §Abstract).

---

## 한계점
- **단일세포 transcriptomics만**: protein, phosphoproteomics 미커버
- **6 dataset 고정**: 더 큰 atlas (CMap, LINCS, scPerturb 50-dataset) 미포함
- **Adversarial / sparsity** 같은 모델 구성 비교 위주, novel architecture 평가 부족
- **Static benchmark**: 새 dataset 등장 시 update 필요
- **HPO compute**: 60+ trials × 6 model × 6 dataset → 막대한 compute
- **시간**: 2024 cutoff, 후속 scFoundation/STATE 미반영

---

## 관련 정보
- **arXiv**: [2408.10609](https://arxiv.org/abs/2408.10609)
- **DBLP**: [journals/corr/abs-2408-10609](https://dblp.org/rec/journals/corr/abs-2408-10609.html)
- **저자 소속**: Altos Labs (Cambridge) + University College London
- **이 benchmark가 사용한 dataset**: Norman 2019 (canonical combo), Srivatsan 2020 (sci-Plex), Frangieh 2021 (immune + cancer), Jiang 2024, McFaline-Figueroa 2023, OP3 (NeurIPS 2023 challenge)
- **이 benchmark가 평가한 모델**: CPA, SAMS-VAE, BioLord, GEARS, scGPT, Latent Additive, Decoder-Only
- **관련 benchmark**: scPerturb (Peidli 2024 — data harmonization), NeurIPS 2023 perturbation prediction challenge
