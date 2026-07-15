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

## TL;DR
**A GNN model for predicting single-cell perturbation effects** — it combines a **gene-gene knowledge graph** based on Gene Ontology / co-expression with perturbation embeddings to predict the **transcriptomic response of single-gene or multi-gene perturbations never seen during training**. Evaluation is done on Norman 2019 (102 single + 131 two-gene) / Adamson 2016 / Dixit 2016 using **MSE on top-20 DEG / Pearson / Precision@10 for GI prediction**.

---

## Construction Methodology

```
Step 1 — Problem framing
  ┌──────────────────────────────────────────────┐
  │ - Experimentally feasible Perturb-seq combos < 10⁻⁶ │
  │   (20K genes × 20K = 400M dual pairs)         │
  │ - Existing models predict only perturbations seen │
  │   in training                                 │
  │   → poor generalization to unseen perturbations │
  │ - Dual-gene effects in particular are not simple additions │
  │   (GI: synergy, suppression, redirection, etc.) │
  └──────────────────────────────────────────────┘

Step 2 — GEARS model architecture
  ┌──────────────────────────────────────────────┐
  │ (1) Gene-gene knowledge graph input           │
  │     - Gene Ontology (functional similarity)   │
  │     - Co-expression network                   │
  │  → learn gene-level embedding via GNN         │
  │                                              │
  │ (2) Perturbation embedding                    │
  │     - use each perturbed gene's GNN embedding │
  │     - Multi-gene: sum the embeddings          │
  │                                              │
  │ (3) Cell-state decoder                        │
  │     - control cell expression + pert embed   │
  │     → predicted post-perturbation expression  │
  └──────────────────────────────────────────────┘

Step 3 — Held-out evaluation protocol (paper contribution)
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

Step 4 — Dataset evaluation (3 core datasets)
  ┌──────────────┬──────────┬──────────────────┐
  │ Dataset       │ Perts     │ Usage             │
  ├──────────────┼──────────┼──────────────────┤
  │ Norman 2019   │ 102 sg + 131 dg │ canonical dual-gene  │
  │ Adamson 2016  │ ~87 single  │ UPR pathway          │
  │ Dixit 2016    │ ~24 single  │ early Perturb-seq    │
  │ Replogle 2022 │ essential gene-scale │ added later (preprocessor) │
  └──────────────┴──────────┴──────────────────┘

Step 5 — Evaluation metrics (paper §Methods)
  · MSE on top-20 DEG (differentially expressed genes)
  · Pearson correlation (predicted vs observed Δ expression)
  · Precision@10 for GI subtype classification
    (synergy / suppression / redirection / etc.)
  · Jaccard similarity of DEG sets
```

---

## Example of actual data format (paper §Methods + GitHub README)

### Type A — Single-gene perturbation training example

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

### Type B — Two-gene combinatorial perturbation

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

### Type C — GI (Genetic Interaction) subtype classification

> Predicted dual-gene response vs additive single effects:
> ```
> Predicted GI types (paper Fig. 4):
>   · NEOMORPHIC: novel program (A+B ≠ A union B)
>   · REDUNDANT: same program (A+B ≈ A ≈ B)
>   · SUPPRESSOR: B suppresses A (A+B → control)
>   · EPISTASIS_A: A dominates (A+B ≈ A)
>   · POTENTIATION: B amplifies A
>   · ADDITIVE: A+B = A + B (linear baseline)
> ```
>
> Metric: Precision@10 — top-10 predicted GIs match ground-truth class

### Type D — Python API (GitHub README)

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

## Evaluation framework summary

| Metric | Meaning | Priority |
|---|---|---|
| **MSE on top-20 DEG** | Prediction accuracy on the 20 genes with the largest changes | Primary |
| **Pearson correlation** | Predicted vs observed Δexpression correlation | Primary |
| **Precision@10 (GI)** | Accuracy of the top-10 predicted GI subtypes | Primary |
| **Jaccard similarity** | Predicted DEG set ∩ observed DEG set | Secondary |

→ **Looking at MSE alone is insufficient** — because the control mean of Norman 2019 is a strong baseline. Top-20 DEG is used to measure the perturbation-specific signal.

---

## Main results (paper body)

| Comparison | Result |
|---|---|
| Single-gene unseen | GEARS > scGen, CPA baselines |
| Two-gene seen-seen | GEARS ≈ linear baseline (mostly additive) |
| Two-gene seen-unseen | GEARS > all baselines (gene-gene KG effect) |
| Two-gene unseen-unseen | hardest, all models low performance |
| GI subtype prediction | NEOMORPHIC/REDUNDANT predictable |

→ "When trained on single-gene perturbation data alone, GEARS cannot reliably predict outcomes for combinatorial perturbations" (GitHub README, limitation stated explicitly).

---

## Limitations
- **Single-only training is limited for dual prediction** (stated explicitly in the authors' GitHub README)
- **Knowledge graph dependency**: the quality of the GO/co-expression KG is decisive
- **Cell-line dependency**: trained on K562 (Norman) → limited generalization to other cell types
- **Single-cell transcriptomics only**: does not cover protein, phenotype, organelle
- **Computational cost**: large GNN, MPS hardware required
- **Under ablation in PerturBench (Wu 2024)**: GEARS is nearly on par with a simple Latent Additive baseline

---

## Related links
- **Paper (Nat. Biotechnol.)**: [10.1038/s41587-023-01905-6](https://doi.org/10.1038/s41587-023-01905-6)
- **GitHub**: [snap-stanford/GEARS](https://github.com/snap-stanford/GEARS) (`pip install cell-gears`)
- **Author affiliation**: Stanford SNAP (Jure Leskovec lab) + Genentech
- **Datasets used by this model**: [[norman2019exploring]] (102 sg + 131 dg), Adamson 2016 (UPR), Dixit 2016 (TF), Replogle 2022 (essential)
- **Benchmark that evaluated this model**: [[DBLP:journals/corr/abs-2408-10609]] (PerturBench — comparing GEARS with baselines)
- **Follow-up work**: scFoundation, scGPT, STATE — all compare GEARS with baselines
