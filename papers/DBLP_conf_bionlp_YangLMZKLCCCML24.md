---
title: "KG-Rank: Enhancing Large Language Models for Medical QA with Knowledge Graphs and Ranking Techniques"
bib_key: "DBLP:conf/bionlp/YangLMZKLCCCML24"
year: 2024
domain: medical
type: Method
venue: BioNLP@ACL
paper_link: https://aclanthology.org/2024.bionlp-1.13/
---
# KG-Rank: Knowledge-Graph + Ranking for Long-form Medical QA
> BioNLP@ACL 2024 | Method | medical

## TL;DR
KG-Rank is a framework that extracts medical entities from a medical question, retrieves one-hop triples (facts) from UMLS, and then uses IR ranking/re-ranking techniques (similarity, Answer Expansion, MMR, MedCPT re-ranking) to select only the most relevant facts and inject them into an LLM, thereby improving the factuality and quality of long-form medical answers without fine-tuning.

## Architecture (KG-Rank Architecture)
1. **Medical NER:** The LLM extracts medical entities from the question via a prompt and maps them to UMLS entities.
2. **UMLS one-hop retrieval:** Collect one-hop relation triples (e_i', r, e_j') per entity (a single entity can have thousands of relations, so ranking is essential).
3. **Ranking/Re-ranking (core):** Align questions and triples using UmlsBERT embeddings. Four variants — Similarity / Answer Expansion (generate a pseudo answer, then retrieve with [Q,A]) / MMR (relevance + diversity, with the diversity penalty increasing as more items are selected) / Re-ranking (MedCPT cross-encoder).
4. **Long-form synthesis:** Inject the top triples plus a task prompt into the LLM to generate a free-text answer.

## Pipeline (inference)
1. Question → medical entity extraction → UMLS mapping.
2. one-hop triple retrieval.
3. Rank triples with Similarity/AE/MMR/Re-ranking.
4. Top triples + prompt → LLM long-form answer.

## Key results
Backbones include GPT-4 and others; datasets are ExpertQA-Bio/Med, LiveQA, and MedicationQA. On GPT-4, Zero-Shot→KG-Rank ROUGE-L: ExpertQA-Bio 23.00→**27.20**, ExpertQA-Med 25.45→**28.08**, MedicationQA 14.41→**16.19**; BERTScore also improves consistently. ROUGE-L improvements in general domains (Law/Business/Music/History) suggest extensibility.

## Limitations
- Physician evaluation of factuality is future work (not yet performed).
- Insufficient evaluation on medical-specialized base models.
- The ranking step increases additional computation time.

## Related links
- arXiv: 2403.05881 · BioNLP@ACL 2024 (Yang et al.)
- Code: https://github.com/YangRui525/KG-Rank · source UMLS, embeddings UmlsBERT, re-ranker MedCPT
