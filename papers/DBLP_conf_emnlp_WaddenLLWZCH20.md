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

## TL;DR
A task that, for a single atomic claim from the scientific literature, assigns a **SUPPORTS / REFUTES / NOINFO** verdict and further identifies the **rationale sentences** that justify that verdict, together with a dataset of **1,409 expert-written claims**. It is the standard verification benchmark that evaluates at two granularities: **abstract-level F1 + sentence-level (rationale) F1**.

---

## How It Was Built (Construction Methodology)

```
Step 1 — Collect citation sentences (source of naturally occurring claims)
  └─ Extract citation sentences from the S2-ORC corpus
  └─ A citation sentence ≈ a "natural claim" stating the results of another paper
  └─ Adopt claims actually used in real scientific literature instead of synthetic FEVER claims

Step 2 — Rewrite claims (expert annotators)
  └─ Annotators: people with degrees/backgrounds in biomedical research
  └─ Convert citation sentences into atomic claims
  └─ e.g.: "X reduces Y by Z% (p<0.001)" → "X reduces Y"

Step 3 — Identify evidence abstracts + rationale annotation
  ┌───────────────────────────────────────────────┐
  │ For each claim:                               │
  │   1. Identify SUPPORTS / REFUTES / NOINFO abstract│
  │   2. Mark rationale sentences (Lei et al. 2016 style)│
  │      = sentences justifying the verdict (avg 1-3 per claim)│
  └───────────────────────────────────────────────┘
  Sentence-level rationale annotation reliability:
    Cohen's κ = 0.71 (reported by authors)

Step 4 — Final dataset composition
  ┌────────────────────┬──────────────────┐
  │ Item               │ Scale             │
  ├────────────────────┼──────────────────┤
  │ Number of claims    │ 1,409            │
  │ Evidence-bearing   │ ~5,183 abstracts  │
  │ Avg rationale      │ 1.7 sentences/abstract │
  │ Split              │ train/dev/test    │
  │ Label distribution │ SUPP/REFUTE/NEI   │
  └────────────────────┴──────────────────┘
```

---

## Direct Quotes from the Paper (arXiv:2004.14974 §body)

> **Task definition**: *"search literature containing evidence that **SUPPORTS or REFUTES** a given scientific claim, and to identify **rationales** justifying each decision"*

> **Dataset scale**: *"we construct SCIFACT, an expert-annotated dataset of **1,409 scientific claims** accompanied by abstracts that support or refute each claim, and annotated with **rationales** (Lei et al., 2016) justifying each SUPPORTS / REFUTES decision"*

> **Label scheme**: *"labels each abstract as **SUPPORTS, REFUTES, or NOINFO** with respect to the claim"*

> **Annotation source (natural claims)**: *"we develop a novel annotation protocol in which annotators **re-formulate naturally occurring claims** in the scientific literature – citation sentences – into atomic scientific claims"*

> **Sentence-level reliability**: *"sentence-level agreement. The resulting **Cohen's κ is 0.71**"*

> **Difference from FEVER**: *"claims in the popular FEVER dataset (Thorne et al., 2018) are **synthetic**, since they are created by annotators by mutating sentences from Wikipedia"* → SciFact instead leverages naturally occurring citations

---

## Input / Output

### Input
| Item | Description |
|---|---|
| Claim | Natural-language atomic scientific statement (rewritten citation sentence) |
| Corpus | ~5,183 biomedical research abstracts |
| Task setting | (1) **Oracle abstract** (gold abstract given) / (2) **Open** (search the whole corpus via TF-IDF) |

### Output + Evaluation Metrics
| Granularity | Metric | Meaning |
|---|---|---|
| **Abstract-level** | F1 (label) | Accuracy of the claim ↔ abstract verdict (SUPP/REFUTE/NOINFO) |
| **Sentence-level** | F1 (rationale) | Accuracy of which sentence is the basis for the verdict |

→ Evaluating **both granularities of F1 simultaneously** is SciFact's identity. This is the key distinction from a simple accuracy benchmark.

---

## Real Claim Examples (paper Table 1 + Fig 1 verbatim, COVID-19 demo)

### Example 1 — Coexisting SUPPORTS / REFUTES evidence for the same claim
> **Claim**: *"Lopinavir / ritonavir have exhibited favorable clinical responses when used as a treatment for coronavirus."*
>
> **Supports (verbatim)**: *"...after lopinavir/ritonavir (Kaletra, AbbVie) was administered, β-coronavirus viral loads significantly decreased and no or little coronavirus titers were observed..."*
>
> **Refutes (verbatim)**: *"The focused drug repurposing of known approved drugs (such as lopinavir/ritonavir) has been reported failed for curing SARS-CoV-2 infected patients..."*

### Example 2 — Climate dependence (requires directional lexical verification)
> **Claim**: *"The coronavirus cannot thrive in warmer climates."*
>
> **Supports**: *"...most outbreaks display a pattern of clustering in relatively cool and dry areas...unsuitable climates can cause the virus to destabilize quickly..."*
>
> **Refutes**: *"...significant cases in the coming months are likely to occur in more humid (warmer) climates, irrespective of the climate-dependence of transmission..."*

### Example 3 — Statistical reasoning + directional verification
> **Claim**: *"Cardiac injury is common in critical cases of COVID-19."*
>
> **Rationale verification points** (quoted from paper §body):
> - Directional relationship: *"replacing higher with lower would cause the rationale to REFUTE the claim rather than SUPPORT it"*
> - Statistical significance: *"the system should interpret **p < 0.001** as an indication that the reported finding is statistically significant"*

---

## VERISCI Baseline (3-stage pipeline proposed alongside by the authors)

```
[Claim input]
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
│   binary classification of rationale sentences│
└──────────┬────────────────────────┘
           ▼
┌──────────────────────────────────┐
│ Step 3 — LABELPREDICTION          │
│   RoBERTa-large classifier        │
│   SUPPORTS / REFUTES / NOINFO     │
└──────────┬────────────────────────┘
           ▼
   [Verdict + rationale sentences]
```

**Domain adaptation experiment results (paper §6)**: Additional training on FEVER (Wikipedia) + general Wikipedia claims improves SciFact performance → "simple domain adaptation techniques substantially improve performance" (§Abstract).

---

## Main Evaluation Results (paper body Tables 3·4)

| Setting | Abstract Label-Only F1 | Abstract Label+Rationale F1 |
|---|---|---|
| Oracle Abstract (gold given) | ~89.7% | ~72.6% |
| Oracle Rationale (rationale given) | – | ~72.0% |
| **Open (TF-IDF retrieval)** | ~64.1% | **~46.4%** |

→ Large performance drop in the Open setting → retrieval is a major bottleneck for verification success.
→ Label+Rationale F1 is ~17%p lower than Label-Only F1 → identifying rationales is a harder task than label inference.

---

## COVID-19 Zero-Shot Verification Case (quoted from paper §body)

> *"We showcase the ability of our model to verify expert-written claims concerning the novel coronavirus COVID-19 against the newly-released **CORD-19 corpus** (Wang et al., 2020). Expert annotators judge retrieved evidence to be plausible for **23 of 36 claims**."*

→ Demonstrates zero-shot generalization potential in a real medical crisis. A model trained on SciFact can be immediately applied to a new domain (COVID-19).

---

## Key Contributions
1. Formalized the **Scientific Claim Verification** task (claim → abstract → label + rationale)
2. **Dataset of 1,409 expert-annotated claims** (natural claims based on citation sentences)
3. **VERISCI baseline** and demonstration of the effect of domain-adaptation training (FEVER pretraining → SciFact improvement)
4. Established a protocol for **simultaneous sentence-level + abstract-level F1 evaluation**

---

## Limitations
- **Small scale**: 1,409 claims, ~5,183 abstract corpus → extended by SciFact-Open (500K)
- **One-directional evaluation**: single (claim, abstract) pairs; contradiction/integration across multiple abstracts is not evaluated
- **Citation-sentence source bias**: being based on citation sentences, it may be biased toward review-style claims
- **Limits in causal/statistical interpretation**: VERISCI makes errors in resolving p-values, confidence intervals, and coreference
- **Sentence-level difficulty**: rationale identification is harder than abstract-level label inference

---

## Related Links
- **Paper (ACL Anthology)**: [2020.emnlp-main.609](https://aclanthology.org/2020.emnlp-main.609/)
- **arXiv**: [2004.14974](https://arxiv.org/abs/2004.14974)
- **DOI**: [10.18653/v1/2020.emnlp-main.609](https://doi.org/10.18653/v1/2020.emnlp-main.609)
- **DBLP**: [conf/emnlp/WaddenLLWZCH20](https://dblp.org/rec/conf/emnlp/WaddenLLWZCH20.html)
- **GitHub**: [allenai/scifact](https://github.com/allenai/scifact)
- **Extension**: **SciFact-Open** (Wadden et al., EMNLP Findings 2022) — open-domain evaluation with a 500K abstract pool
- **Follow-up work using this benchmark**: VerT5erini, ParagraphJoint, MultiVerS, OpenScholar (also used for citation F1 evaluation)
