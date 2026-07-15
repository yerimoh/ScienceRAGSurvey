---
title: "Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation"
bib_key: "DBLP:conf/naacl/SunZHX25"
year: 2025
domain: medical
type: Method
venue: NAACL
paper_link: https://arxiv.org/abs/2407.15268
---
# FactMM-RAG: Fact-Aware Multimodal RAG for Radiology Reports
> NAACL 2025 | Method | medical

## TL;DR
A RAG system that mines image-report pairs based on factual (entity-relation) agreement extracted with RadGraph to train a fact-aware multimodal retriever, and injects the retrieved reference reports as a condition into LLaVA to generate factually accurate chest radiology reports. It propagates fact-awareness all the way to the generator without diagnostic-label supervision or expert curation.

## Architecture (FactMM-RAG Architecture)
- **RadGraph fact-agreement pair mining:** (1) remove false negatives using the same symptom labels, (2) select positive pairs by applying a strict threshold δ to the entity/relation-based factual similarity.
- **Fact-aware multimodal retriever:** backbone MARVEL (based on T5-ANCE). Encodes query=image, document=(report, image) pairs, and performs InfoNCE contrastive learning (τ=0.01) with the mined factual positives.
- **Generator conditioning:** LLaVA-1.5 generates findings from the query X-ray + retrieved reference report + instruction prompt.

## Pipeline (inference)
1. Encode the query image with the trained MARVEL.
2. Retrieve the **top-1** reference report by cosine similarity from the training corpus (excluding self-retrieval and abnormal reports).
3. Input the image + reference report + prompt to LLaVA.
4. Autoregressively generate findings.

## Key results
Data: MIMIC-CXR (train 125,417 / val 991 / test 1,624), zero-shot CheXpert (1,000). Against SOTA retrievers, **up to +6.5% F1CheXbert and +2% F1RadGraph**. MIMIC-CXR: F1CheXbert 0.602 / F1RadGraph 0.257 / ROUGE-L 0.307 / BERTScore 0.561 (surpassing baselines such as Med-MARVEL and CLIP). Oracle upper bound F1CheXbert 0.992.

## Limitations
- Limited to chest radiology (generalization to brain scans and histopathology unverified).
- Evaluation metrics center on factual/textual similarity — no assessment of conciseness or human alignment.

## Related links
- arXiv: 2407.15268 · NAACL 2025 (Sun et al.)
- Code: https://github.com/cxcscmu/FactMM-RAG
