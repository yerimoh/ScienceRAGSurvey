---
title: "BioReader: a Retrieval-Enhanced Text-to-Text Transformer for Biomedical Literature"
bib_key: "DBLP:conf/emnlp/FrisoniMMV22"
year: 2022
domain: bio, medical
type: Method
venue: EMNLP
paper_link: https://aclanthology.org/2022.emnlp-main.390/
---
# BioReader: Retrieval-Enhanced T5 for Biomedical Literature
> EMNLP 2022 | Method | bio · medical

## TL;DR
BioReader is the first retrieval-enhanced text-to-text model for biomedical literature. It grafts RETRO's chunked cross-attention onto a T5 backbone and uses a frozen CONTRIEVER retriever to fetch relevant literature chunks in real time from a PubMed-based external datastore (about 60M tokens), augmenting the input. It casts every biomedical NLP task as a problem of "transforming text with the help of external knowledge," and outperforms several SOTA systems with up to 3x fewer parameters.

## Architecture (BioReader Architecture)
**Backbone (T5 + RETRO-blocks).** BioReader is a model that extends the T5 encoder–decoder. Unlike the GPT-based RETRO, it keeps the original T5 skeleton and, in the decoder, alternates RETRO-blocks with standard T5-blocks.
- The T5 encoder is kept as is.
- The RETRO-block combines fully-connected (FFW), self-attention (ATT), and chunked cross-attention (CCA): `RETRO(H,E) = FFW(CCA(ATT(H), E))`, while the standard block is `T5(H) = FFW(ATT(H))`.
- In T5-base (12 layers, d=768), RETRO-blocks are placed at the 9th and 12th layers (P={9,12}). At these points, the neighbor encoding and the input encoding are merged via CCA, replacing the encoder output.
- The final configuration has 229.5M parameters.

**Neural retrieval DB (Evidence Datastore).** It uses a retrieval pool that is different from the training corpus (advantageous for domain adaptation and knowledge updating). The datastore consists of about 200K English abstracts of randomized controlled trials (RCTs) derived from PubMed-RCT, amounting to roughly 60M tokens overall, centered on PubMed. Each value consists of two adjacent chunks [N, F] (neighbor + its continuation in the original abstract), and the key is the precomputed f(N).

**Retriever.** The mapping function f(·) is implemented with CONTRIEVER, a frozen, bi-directional encoder (a BERT-base-based dual-encoder trained unsupervised with MoCo contrastive learning), applying average pooling to the last-layer output.

**Chunked Cross-Attention (CCA) — neighbor fusion.** Unlike approaches that interpolate output probabilities or simply concatenate the input, BioReader encodes the input prompt and the neighbors separately and then assembles them via CCA.
- The input is split into chunks of size m=16 (n=512), and for each chunk C_u the top-k documents are retrieved with FAISS via dot product.
- The retrieved [N, F] are each of length 16 → neighbor tokens are encoded by the T5-encoder in a k×32 form.
- Each input chunk attends only to the neighbors of the preceding chunk, and a one-token overlap guarantees autoregression.

## Pipeline (inference)
1. **Input splitting:** The input is divided into chunks of size 16 (n=512).
2. **Retrieval:** Each chunk is encoded with the frozen CONTRIEVER, and top-k retrieval is performed from the datastore with FAISS → obtaining neighbor + continuation.
3. **Encoding:** The input prompt and the retrieved neighbors are encoded separately by the (same) T5 encoder.
4. **Fusion:** In the decoder's RETRO-blocks (P={9,12}), CCA merges the input and neighbor encodings, replacing the encoder output.
5. **Decoding:** Standard T5 greedy decoding. The first chunk is kept independent of neighbors. A task-specific prefix is prepended to the input to cast every task as text-to-text.

## Training / configuration (training)
- **Backbone initialization:** T5-blocks are initialized with SCIFIVE(PubMed)-base weights.
- **Parameter efficiency:** Following RETRO, the pre-trained weights are frozen and only the new CCA parameters (less than 5% of the total) are trained with span-mask. Therefore, when evaluated without retrieval, the original SCIFIVE performance is retained. CCA training uses only about 3% of the pre-training instances.
- **Fine-tuning:** Subsequently, all layers are fine-tuned on the target task (teacher forcing MLE), with multi-task training via task-specific prefixes.
- **Evaluation:** 18 datasets across 6 categories (NER, RE, NLI, DC, QA, OpenQA), most borrowed from BLURB.

## Key results
It outperforms the roughly 3x larger SCIFIVE-large (770M) on several tasks (BioReader 229.5M).

**QA / OpenQA — Exact Match**

| Model | #params | BioASQ4b | BioASQ5b | BioASQ6b | MedQA-USMLE |
|---|---|---|---|---|---|
| SCIFIVE-base | 220M | 60.80 | 59.53 | 55.56 | 34.57 |
| SCIFIVE-large | 770M | 62.98 | 61.67 | 61.74 | 35.12 |
| **BioReader** | **229.5M** | **64.13** | **62.02** | **62.18** | **42.96** |

It also sets new SOTA on NER/RE/DC with BC4CHEMD 92.81, Species-800 77.44, DDI 84.34, HoC(F1*) 87.78, and so on. A human evaluation by three experts also confirmed higher accuracy than automatic evaluation (inter-annotator Kendall 0.91). Adding COVID-19 RCT abstracts to the datastore lets it generate up-to-date answers without retraining (zero-shot datastore update).

## Limitations
- A chunk may hold only part of the evidence, which can induce incomplete or non-factual text, or repetition and contradiction.
- There is a risk that chunks are split across word/entity boundaries (especially risky in biomedicine).
- Only abstracts are used in the knowledge base → the datastore's topic coverage sets the performance ceiling (using full text is future work).
- High memory and FAISS index disk consumption; the backbone SCIFIVE may be undertrained, having been trained with limited resources.

## Related links
- ACL Anthology: https://aclanthology.org/2022.emnlp-main.390/ (EMNLP 2022, pp. 5770–5793)
- Code: https://github.com/disi-unibo-nlp
- Authors: Giacomo Frisoni, Miki Mizutani, Gianluca Moro, Lorenzo Valgimigli (University of Bologna)
