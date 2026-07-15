---
title: "KIBA: Integrated Kinase Inhibitor Bioactivity Score Dataset"
bib_key: "tang2014kiba"
year: 2014
domain: chem, bio, medical
type: benchmark
venue: Journal of Chemical Information and Modeling
paper_link: https://doi.org/10.1021/ci400709d
---
# KIBA: 52,498 compounds × 467 kinases — Integrated Bioactivity Score

> J. Chem. Inf. Model. 54(3):735–743 | 2014 | Benchmark (DTI regression at scale) | chem · bio · medical
> Jing Tang, Agnieszka Szwajda, Sushil Shakyawar, Tao Xu, Petteri Hintsanen, Krister Wennerberg, Tero Aittokallio — Institute for Molecular Medicine Finland (FIMM), University of Helsinki
> DOI: [10.1021/ci400709d](https://doi.org/10.1021/ci400709d) · PMID 24521231

## TL;DR
A large-scale DTI benchmark that merges data from **three large-scale biochemical kinase inhibitor assays** + **ChEMBL** + **STITCH** into a single integrated matrix of **52,498 compounds × 467 kinases**, converting IC50/Ki/Kd into **246,088 KIBA scores**. As the large-scale counterpart to Davis (2011), it is almost always reported together with it.

---

## Construction Methodology

```
Step 1 — Integrate 3 large-scale kinase assay sources
  ├─ Anastassiadis et al. 2011 (Nature Biotech) — ~30K activities
  ├─ Davis et al. 2011 (Nat Biotech) — Kd matrix
  ├─ Metz et al. 2011 (Nature Chem Biol) — pIC50 matrix
  └─ + ChEMBL bioactivities + STITCH chemical-protein

Step 2 — Integrate diverse measurement units (KIBA score computation)
  ┌─────────────────────────────────────────────┐
  │ Mixed bioactivity types:                    │
  │   - Kd (dissociation constant)              │
  │   - Ki (inhibition constant)                │
  │   - IC50 (50% inhibitory concentration)     │
  │                                              │
  │ KIBA score: model-based integration         │
  │   → collapse different assays/units into a single score │
  │   → bias correction + consistency filtering │
  └─────────────────────────────────────────────┘

Step 3 — Matrix result
  ┌─────────────────┬──────────────────────┐
  │ Item            │ Value                 │
  ├─────────────────┼──────────────────────┤
  │ Compounds       │ 52,498               │
  │ Kinase targets  │ 467                  │
  │ Integrated      │ 246,088 KIBA scores  │
  └─────────────────┴──────────────────────┘

Step 4 — Result analysis
  └─ Quantify activity concordance across assays
  └─ Cluster compound bioactivity profile patterns
  └─ Suggest drug repositioning candidates
```

---

## Direct Quotations (Tang 2014 JCIM §Abstract)

> "We integrated bioactivity measurements from **three recent large-scale biochemical assays** of kinase inhibitors alongside data from established databases (**ChEMBL** and **STITCH**)."

> "The study consolidated diverse bioactivity types including **IC50, Ki, and Kd** values across **52,498 compounds** and **467 kinase targets**, generating **246,088 integrated KIBA scores**."

---

## Primary Uses

| Item | Content |
|---|---|
| Task definition | Drug-Target Interaction (DTI) regression — large-scale |
| Output | KIBA score (lower means stronger binding) |
| Pairing | Standard counterpart reported together with the Davis dataset |
| Pioneer model | DeepDTA (Öztürk 2018) — baseline on both DAVIS + KIBA |
| Vs. Davis | About 700× larger scale, with higher sparsity |
| TDC integration | `multi_pred.DTI.KIBA` |

---

## Dataset Statistics

| Subset | Value |
|---|---|
| Compounds (drugs/inhibitors) | 52,498 |
| Kinase targets | 467 |
| Integrated KIBA scores | 246,088 |
| Sparsity | ~99% (most of the drug × target matrix is empty) |
| Original bioactivity units | Kd, Ki, IC50 all integrated |

---

## Limitations
- **Persistent sparsity**: 246K scores / (52K × 467) ≈ 1% — difficult as a matrix completion task
- **Unit-integration model assumption**: assumes accuracy in the KIBA score conversion (Kd/Ki/IC50 are not exactly comparable)
- **Kinase-only, nothing else**: kinase-specific, does not include other protein families
- **Time**: 2014 data, does not reflect the latest inhibitors (kinase degraders, allosteric)
- **Single integrated score**: loses type-specific binding mode information (e.g., type I vs II)

---

## Related links
- **Paper (DOI)**: [10.1021/ci400709d](https://doi.org/10.1021/ci400709d)
- **PubMed**: [PMID 24521231](https://pubmed.ncbi.nlm.nih.gov/24521231/)
- **Author affiliation**: FIMM, University of Helsinki (now Aittokallio Lab)
- **Major works using this benchmark**: DeepDTA, GraphDTA, AttentionDTA, MolTrans, KronRLS, SimBoost, and nearly every DTI deep learning paper
- **Counterpart reported together**: [Davis](davis2011kinase.html) (Davis et al. 2011 Nat Biotechnol)
