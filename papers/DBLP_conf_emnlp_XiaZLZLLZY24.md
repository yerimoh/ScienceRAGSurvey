---
title: "RULE: Reliable Multimodal RAG for Factuality in Medical Vision Language Models"
bib_key: "DBLP:conf/emnlp/XiaZLZLLZY24"
year: 2024
domain: medical
type: Method
venue: EMNLP
paper_link: https://arxiv.org/abs/2407.05131
---
# RULE: Reliable Multimodal RAG for Medical VLMs
> EMNLP 2024 | Method | medical

## TL;DR
RULE is a multimodal RAG based on medical image-report retrieval that (1) calibrates the number of retrieved contexts via statistical risk control (Factuality Risk Control) to guarantee that the factuality risk stays below a user-specified upper bound, and (2) combines this with preference tuning (Knowledge-Balanced Preference Tuning) that reduces over-reliance on retrieval, improving the factual accuracy of Med-LVLMs by 47.4% on average.

## Architecture (RULE Architecture)
- **Multimodal retriever:** CLIP-style contrastive learning (ResNet-50 image + BioClinicalBERT text). Retrieves top-K reports by cosine similarity from the input image. The backbone Med-LVLM is LLaVA-Med-1.5 7B.
- **Calibrated context selection (FRC):** Calibrates the number of retrievals k via Learn-then-Test risk control — only k values for which the factuality risk FR(k) does not exceed the upper bound α are accepted (guaranteed with probability 1−δ). Statistically blocks the noise introduced by too many retrievals.
- **RAG-based preference fine-tuning (KBPT):** DPO-style LoRA preference learning that treats "over-reliance" samples — those answered correctly without retrieval but incorrectly after retrieval — as dispreferred.

## Pipeline (inference)
1. Input image and query → retriever retrieves top-K reports by cosine similarity.
2. Select k contexts calibrated by FRC.
3. Feed (query + selected reports + image) into LLaVA-Med tuned with KBPT.
4. Generate factuality-calibrated VQA answers or reports.

## Key results
Medical VQA accuracy (%): IU-Xray 75.47→**87.84**, MIMIC-CXR 75.79→**83.92**, Harvard-FairVLMed 63.03→**87.12**. Factual accuracy +47.4% on average, +14.46% over prior hallucination-mitigation methods, over-reliance error/ratio reduced by −42.9%/−47.3% respectively.

## Limitations
- Focused on factuality — safety, fairness, robustness, and privacy are left for future work.
- Retrieval quality may degrade for images outside the coverage of the retriever corpus (domain image-report pairs).

## Related links
- arXiv: 2407.05131 · EMNLP 2024 (Xia et al.)
- Code: https://github.com/richard-peng-xia/RULE
