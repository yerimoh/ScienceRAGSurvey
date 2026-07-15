---
title: "CardioRAG: A Retrieval-Augmented Generation Framework for Multimodal Chagas Disease Detection"
bib_key: "DBLP:journals/corr/abs-2510-01558"
year: 2025
domain: medical
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2510.01558
---
# CardioRAG: Retrieval-Augmented ECG Diagnosis
> arXiv 2025 | Method | medical

## TL;DR
CardioRAG is a RAG framework that, for 12-lead ECG-based Chagas disease detection, retrieves the most similar cases from a database of past patient ECG cases (VAE latent representations + extracted clinical features + diagnostic labels) using cosine similarity in latent space, and grounds them as structured context into an LLM to generate interpretable diagnoses. (K3 extension to physiological signals beyond imaging.)

## Architecture (CardioRAG Architecture)
- **VAE ECG latent representation:** An encoder with 4 residual blocks encodes the ECG into a 256-dimensional latent (L = L_recon + β·L_KL, β=0.1).
- **Past-case database:** Each case stores the VAE latent + demographics + clinical features (automatic RBBB/LAFB detection, V5 ventricular rate·RMSSD) + diagnostic label.
- **Retrieval → LLM grounding:** After retrieving candidates via cosine similarity in latent space, they are re-ranked by a composite score (S_VAE + w_age·S_age) to select top-k. The retrieved cases are converted into **structured text** (demographics·features·HRV·label) and fed into the LLM (the raw waveform is used only in the retrieval stage). LLM = DeepSeek-R1:1.5b.

## Pipeline (inference)
1. ECG preprocessing → automatic clinical feature extraction → VAE encoding into a 256-dimensional latent.
2. Latent similarity retrieval + composite-score re-ranking → top-k (optimal k=8) cases.
3. Combine the retrieved cases into the prompt as structured context.
4. The LLM outputs a binary diagnosis + confidence + clinical reasoning as JSON.

## Key Results
Data: SaMi-Trop (positive)·PTB-XL (negative)·CODE-15%. Test set of 100 patients (50 positive / 50 negative). Without RAG, recall 48.98% → **with RAG (k=8), recall 85.7~89.8%**. Optimal (P2 concise prompt, k=8): accuracy 58.59% / recall 87.76% / F1 0.68. k=16 degrades due to over-retrieval (inverted-U shape).

## Limitations
- accuracy 58~59% ceiling — a limitation of the small LLM; evaluation with a larger LLM is needed.
- The confidence scores of the small LLM are hard to trust.
- The datasets and splits used to construct the retrieval DB are insufficiently specified in the main text.

## Related links
- arXiv: 2510.01558 (Shen, Zhai, Tu, Shi; Imperial College London / Oxford)
