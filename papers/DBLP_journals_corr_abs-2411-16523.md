---
title: "LaB-RAG: Label Boosted Retrieval Augmented Generation for Radiology Report Generation"
bib_key: "DBLP:journals/corr/abs-2411-16523"
year: 2024
domain: medical
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2411.16523
---
# LaB-RAG: Label-Boosted RAG for Radiology Report Generation
> arXiv 2024 | Method | medical

## TL;DR
LaB-RAG is a training-free RAG + in-context learning pipeline that generates radiology reports without fine-tuning a large model on the task. It predicts categorical labels from chest X-rays to filter retrieval candidates, retrieves 〈image-label-text〉 tuples from MIMIC-CXR via image embedding similarity, and then generates a report by presenting the retrieved reports as examples to a frozen general-purpose LLM.

## Architecture (LaB-RAG Architecture)
- **Label prediction:** On top of a frozen image embedding (BioViL-T for MIMIC-CXR), a lightweight logistic regression predicts 15 categorical labels, CheXpert 14 + Other (CheXbert is the superior labeler).
- **Label filter + image-similarity retrieval:** Rank by cosine similarity against the corpus (image-label-text tuples of the training split), then filter by predicted labels with either Exact (exact match) or Partial (re-rank by overlapping positive labels).
- **General-purpose LLM prompting:** Feed the retrieved example reports + predicted labels to a frozen Mistral-7B-Instruct (Naive/Simple/Verbose/Instruct prompts). The only thing trained is the label classifier.

## Pipeline (inference)
1. Encode the image → predict 15 labels.
2. Rank by image similarity against the corpus → Exact/Partial label filter.
3. Select the reports of the top k=5 tuples as in-context examples.
4. Feed the labels + example reports to the frozen Mistral-7B (greedy, temp 0) → generate the report.

## Key results
MIMIC-CXR Findings: **F1-CheXbert 0.466** (surpassing CXRMate 0.456 · RGRG 0.447 · retrieval baseline CXR-RePaiR 0.353), BLEU-4 0.265 / ROUGE-L 0.446 / BERTScore 0.815. Impression F1-CheXbert 0.484. However, **F1-RadGraph lags behind the fine-tuning baseline (CXRMate)**. CheXpert Plus Findings F1-CheXbert 0.507.

## Limitations
- Clinical label accuracy (F1-CheXbert) is strong, but some NLG metrics such as F1-RadGraph are inferior to the fine-tuning baseline.
- Performance depends on the quality of the label classifier and labeler, and on the size of the retrieval corpus.
- Evaluation is limited to chest X-ray report generation.

## Related links
- arXiv: 2411.16523 (Song, Subramanyam, Madejski, Grossman)
- Code: https://github.com/uc-cdis/label-boosted-RAG-for-RRG
