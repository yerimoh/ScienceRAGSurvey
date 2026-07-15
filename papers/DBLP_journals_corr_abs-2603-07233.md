---
notion_id: 355f2dcd-4912-8125-a0b1-edf649b6be58
title: Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation
bib_key: DBLP:journals/corr/abs-2603-07233
year: 2026
domain: bio
type: Method
venue: Gen2 @ ICLR
paper_link: https://arxiv.org/abs/2603.07233
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation

> Gen2 @ ICLR | 2026 | Method | bio

## TL;DR
PT-RAG, the first framework to apply RAG to predicting cellular responses to gene perturbation. Alongside the key finding that naive RAG actually degrades performance, it achieves improvements in distributional similarity metrics over STATE through GenePT embeddings plus a Gumbel-Softmax-based two-stage differentiable retrieval.

<details>
<summary>Background knowledge</summary>
**Perturbation** means "disturbance" or "perturbation," and its usage varies with context.
In its **general sense**, it refers to *deliberately touching a system from its original state to observe the change*.
---
**In biology (the context of this paper)**
It refers to *genetic manipulation* applied to a cell, such as turning a gene off (knockdown/knockout) or overexpressing it.
For example, "perturbing the BRCA1 gene" → suppressing BRCA1 to observe how the cell responds (how gene expression changes).
This paper uses a technique called **Perturb-seq**, which uses CRISPR to turn thousands of genes off one at a time while measuring the entire gene expression change of each cell all at once. Looking at the resulting data, learning "when I touched this gene, those genes responded like this" is the purpose of PT-RAG.
---
**In other fields**
- Physics: applying a small external stimulus to a system (perturbation theory)
- Machine learning: slightly modifying input data to see the model's response (adversarial perturbation, etc.)
In a word, it is the concept of **"touch it and see how it responds."**
</details>

## Research Background and Motivation
### Limitations of Existing Methods
- Existing perturbation prediction models such as GEARS, scGPT, and STATE generate expression profiles based only on cell state and perturbation identity, and **do not leverage knowledge across related perturbations**
- When simply applying RAG from the language domain (vanilla RAG), the perturbation domain has **no pre-defined similarity criteria**, so performance actually degrades
- In perturbation retrieval, relevance **depends heavily on cell type**, but existing methods do not account for this

### Why This Research Is Needed
- Because the effect of gene perturbation varies greatly by cell type even for the same gene, **cell-type-aware context retrieval** is essential
- Leveraging data from thousands of already-observed perturbation experiments in a RAG manner can improve generalization performance for predicting unseen perturbations
- Through a **differentiable retrieval mechanism**, the generation objective and the retrieval objective are jointly optimized end-to-end

## System Architecture

```
Input: (perturbation gene g, cell state c)
       │
       ▼
[Stage 1: GenePT embedding-based candidate retrieval]
  - Encode the input perturbation as a GenePT embedding
  - Retrieve K similar perturbation candidates in the training DB (cosine similarity)
       │
       ▼
[Stage 2: Gumbel-Softmax-based adaptive selection]
  - Conditioned on cell state + perturbation embedding
  - Make discrete selection differentiable via Straight-Through Gumbel-Softmax
  - Select the optimal subset (sparsity loss prevents mode collapse)
       │
       ▼
[Context Aggregation]
  - Aggregate the observed expression profiles of the selected perturbations
       │
       ▼
[Generator (STATE-based)]
  - Predict the post-perturbation expression distribution from context + input conditions
       │
       ▼
Output: predicted gene expression profile (2,000 HVGs)
```

## Detailed Description of Core Modules
### Stage 1: GenePT Embedding Candidate Retrieval
- **GenePT**: a gene embedding model trained on ChatGPT-generated gene functional description text
- Encode the input perturbation gene in the GenePT space, then retrieve the top-K candidate perturbations within the training data
- Based on semantic (functional similarity) — no learnable parameters

### Stage 2: Gumbel-Softmax Adaptive Selection
- Applies the **Straight-Through Gumbel-Softmax estimator** (Jang et al. 2017)
- Input: [cell state embedding; perturbation embedding]
- Output: discretely selects the optimal subset among the K candidates
- Adds a **sparsity loss**: prevents mode collapse in which all candidates are selected, inducing selection of only truly relevant context
- Overlap rate of selected perturbations across cell types is **19%** → quantitatively verifies the cell-type-aware property

### Context Aggregation
- Aggregates the observed scRNA-seq expression vectors of the selected perturbations
- Provided as the input context to the Generator (STATE)

### Generator (STATE backbone)
- Arc Institute's STATE: a Transformer-based multi-cell-type perturbation prediction model
- Trained with energy distance (an MMD-based distributional loss)
- Jointly optimized end-to-end with the PT-RAG context added

## Experiments and Evaluation
### Evaluation Dataset
| Item | Content |
|---|---|
| **Dataset** | Replogle-Nadig Perturb-seq (Replogle et al. 2022; Nadig et al. 2024) |
| **Cell lines** | K562, RPE1, Jurkat, HepG2 (4 human cell lines) |
| **Total cell count** | ~0.6M |
| **Number of perturbations** | 2,023 (test: 1,635) |
| **Number of features** | 2,000 HVGs |
| **Experimental method** | CRISPRi (CRISPR interference) single-gene knockdown |

### Main Results
| Method | W2 (↓) | Notes |
|---|---|---|
| **PT-RAG (proposed)** | improvement over STATE | best |
| STATE (baseline) | 646.1 | prior SOTA |
| Vanilla RAG | **1189.5** | actually the worst |
| GEARS | — | baseline |

- **Key finding**: Vanilla RAG degrades W2 by roughly 2x compared to the STATE baseline → empirically demonstrates the absolute necessity of domain-specific differentiable retrieval
- PT-RAG achieves meaningful improvement over STATE on the W1 and W2 distributional similarity metrics

## Key Contributions
1. **The first RAG framework for biological perturbation prediction**: extends language RAG to single-cell biology
2. **The failure of naive RAG is itself a key finding**: quantitatively demonstrates that, because the perturbation domain has no pre-defined similarity criteria, naive retrieval severely degrades performance
3. **Cell-type-aware differentiable retrieval**: a Gumbel-Softmax-based two-stage pipeline designed to learn the different optimal context for each cell type
4. **Distribution-level performance improvement**: improves over prior SOTA on distributional metrics such as W1 and W2

## Limitations
- **Single-dataset evaluation**: experiments only on the single Replogle-Nadig dataset — generalization to other Perturb-seq datasets is uncertain
- **Supports only single-gene perturbation**: combination perturbation is not validated
- **End-to-end training cost**: joint optimization of differentiable retrieval requires substantial compute resources
- **Dependence on text-based GenePT**: genes without functional descriptions may suffer degraded Stage 1 retrieval quality

## Related Work and Related Links
- **Paper link**: [https://arxiv.org/abs/2603.07233](https://arxiv.org/abs/2603.07233)
- **Code**: [https://github.com/difra100/PT-RAG_ICLR](https://github.com/difra100/PT-RAG_ICLR)
- **Venue**: ICLR 2026 Workshop — Generative AI in Genomics (Gen2)
- **Baseline models**: STATE (Adduri et al. 2025), GEARS (Roohani et al. 2024), scGPT
- **Datasets used**: Replogle et al. 2022 (Cell), Nadig et al. 2024
