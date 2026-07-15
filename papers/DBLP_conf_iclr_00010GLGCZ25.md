---
title: "KGARevion: An AI Agent for Knowledge-Intensive Biomedical QA"
bib_key: "DBLP:conf/iclr/00010GLGCZ25"
year: 2025
domain: medical, bio
type: Method
venue: ICLR
paper_link: https://arxiv.org/abs/2410.04660
---
# KGARevion: KG-Grounded Agent for Biomedical QA
> ICLR 2025 | Method | medical · bio

## TL;DR
KGARevion is a Generate→Review→Revise→Answer agent that first generates candidate triplets from the LLM's latent knowledge, then verifies and corrects them against a grounded biomedical knowledge graph (PrimeKG/OGB-biokg) before answering. It removes factually incorrect triplets and retains incomplete knowledge, raising the reliability of medical QA with KG-verified knowledge.

## Architecture (KGARevion Architecture)
- **Generate:** From the question, generate relevant candidate triplets using the LLM's latent knowledge (choice-aware for multiple-choice questions).
- **Review:** Verify each triplet against the KG — map entities via UMLS codes, align TransE structural embeddings with the relation description via attention+FFN, and output True/False through LoRA fine-tuning. Two soft-constraints: remove factually wrong triplets (Factually Wrong), retain incomplete knowledge (Incomplete).
- **Revise:** Regenerate and re-verify triplets judged False (up to k rounds).
- **Answer:** Generate the final answer from the set of verified True triplets.
- **KG used:** PrimeKG / OGB-biokg (biomedical KG), UMLS codes.

## Pipeline (inference)
1. Question → candidate triplet generation (Generate).
2. KG-grounded verification (Review) → remove factual errors, preserve incomplete ones.
3. Regenerate and re-verify the False set (Revise, ≤k rounds).
4. Generate the answer from the verified triplets (Answer).

## Key results
Evaluated on medical QA benchmarks (MMLU-Med, MedQA-US, PubMedQA*, BioASQ-Y/N, MedDDx Basic/Intermediate/Expert, AfriMed-QA). Improvements over baselines (direct LLM, general RAG, KG methods) on LLaMA3-8B · LLaMA3.1-8B (k=1) and open-ended (k=2). (For specific numbers, refer to the tables in the original paper — verified against the single HTML render.)

## Limitations
- Candidate triplet generation quality depends on the LLM's latent knowledge, and relations absent from the KG have limited verifiability.
- Performance is governed by KG (PrimeKG/biokg) coverage and UMLS mapping accuracy.
- LoRA training of the Review module and multiple rounds increase inference cost.

## Related links
- arXiv: 2410.04660 · ICLR 2025
- Code: https://github.com/mims-harvard/KGARevion
