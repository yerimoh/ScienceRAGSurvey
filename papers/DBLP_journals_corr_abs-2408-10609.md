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

## TL;DR
A **6-dataset benchmark** (Srivatsan20 / Frangieh21 / Jiang24 / McFalineFigueroa23 / Norman19 / OP3) and **2 task families** (covariate transfer / combo prediction) for the standardized evaluation of **single-cell perturbation response prediction models**. Beyond fit metrics like RMSE + Pearson, it introduces a **rank-based metric** (ordering across perturbations) to expose mode-collapse models. It compares published models such as CPA / SAMS-VAE / BioLord / GEARS / scGPT with Latent Additive / Decoder-only baselines.

---

## Construction Methodology

```
Step 1 — Problem recognition: weaknesses of existing perturbation benchmarks
  ┌──────────────────────────────────────────────┐
  │ - Different split / metric per dataset        │
  │ - rank-blind metric (RMSE/Pearson) focused    │
  │   → Decoder-Only scores well with single mean │
  │ - Small-dataset focused → real-world not      │
  │   reflected                                   │
  │ - Lack of scFM (scGPT etc.) eval consistency  │
  └──────────────────────────────────────────────┘

Step 2 — 6 dataset selection (≥100 perturbations required)
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

Step 3 — Define 2 task families
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

## Example real data formats (paper §2 + Table 1 + Figure 2)

### Type A — Single-cell perturbation dataset record

> **Input**: control cell expression vector + perturbation metadata (covariate + pert ID)
>
> ```
> Cell shape:  (cells, genes) ~ (218,331 × ~33,000) for Frangieh21
> Pert metadata: (perturbation ID, target gene(s), covariate cell line)
> Covariate:   batch / cell type / dose
> ```
>
> **Output / Label**: post-perturbation cell expression vector (same gene shape)

### Type B — Covariate transfer task (5 datasets)

> ```
> Train: cells with covariate C1, C2 — all perturbations A,B,C
> Test:  cells with covariate C3 (unseen) — same perturbations A,B,C
> Model task: predict cell state under perturbation in unseen covariate
> Real-world analog: drug effect in unseen cell line / tissue
> ```

### Type C — Combinatorial prediction task (Norman19)

> ```
> Train: 155 single + 30% of 131 dual perturbations
> Test:  70% of dual perturbations (held out)
> Model task: predict A+B response from A and B single effects
> ```

### Type D — Rank metric calculation (paper Figure 2)

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

## Evaluation framework summary

| Category | Metric | Purpose |
|---|---|---|
| **Fit** | RMSE | accuracy of average response |
| Fit | cosine LogFC | LogFC direction agreement |
| **Rank** | rank RMSE | mode-collapse detection |
| Rank | rank cosine | specificity measurement |
| **Distributional** | MMD (gene) | full distribution agreement |
| Distributional | MMD PCA (top-256) | latent distribution agreement |
| Distributional | DEG recall (top-20 t-score) | DEG recovery rate |

→ Core contribution: the **rank metric** — looking only at RMSE, a Decoder-Only that predicts every perturbation as the single mean can look good, but it is immediately exposed with rank ≈ 0.5.

---

## Main results (paper §5)

| Finding | Meaning |
|---|---|
| CPA*(noAdv) with adversarial removed is always better than CPA* | adversarial component does not help |
| SAMS-VAE*(S) with sparsity removed is always better than SAMS-VAE* | the sparse-mask assumption is actually a loss |
| Latent Additive baseline is on par with or superior to published models | simple models are generally sufficient |
| Decoder-Only has good RMSE but rank ≈ 0.5 | mode-collapse, rank metric needed |
| Using scGPT embeddings gives only marginal improvement | scFM has no large effect on perturbation |
| Norman19 combo prediction: even a linear model is strong | dual effects are mostly linear |

→ **Conclusion**: "no single model architecture clearly outperforms others, simpler architectures are generally competitive and scale well with larger datasets" (paper §Abstract).

---

## Limitations
- **Single-cell transcriptomics only**: does not cover protein, phosphoproteomics
- **Fixed at 6 datasets**: larger atlases (CMap, LINCS, scPerturb 50-dataset) not included
- Focused on comparing model components like **adversarial / sparsity**; lacks evaluation of novel architectures
- **Static benchmark**: requires updates when new datasets appear
- **HPO compute**: 60+ trials × 6 models × 6 datasets → enormous compute
- **Time**: 2024 cutoff, does not reflect subsequent scFoundation/STATE

---

## Related links
- **arXiv**: [2408.10609](https://arxiv.org/abs/2408.10609)
- **DBLP**: [journals/corr/abs-2408-10609](https://dblp.org/rec/journals/corr/abs-2408-10609.html)
- **Author affiliations**: Altos Labs (Cambridge) + University College London
- **Datasets used by this benchmark**: Norman 2019 (canonical combo), Srivatsan 2020 (sci-Plex), Frangieh 2021 (immune + cancer), Jiang 2024, McFaline-Figueroa 2023, OP3 (NeurIPS 2023 challenge)
- **Models evaluated by this benchmark**: CPA, SAMS-VAE, BioLord, GEARS, scGPT, Latent Additive, Decoder-Only
- **Related benchmarks**: scPerturb (Peidli 2024 — data harmonization), NeurIPS 2023 perturbation prediction challenge
