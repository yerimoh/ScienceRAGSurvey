---
title: "BioRAGent: A Retrieval-Augmented Generation System for Showcasing Generative Query Expansion and Domain-Specific Search for Scientific Q&A"
bib_key: "DBLP:conf/ecir/AteiaK25"
year: 2025
domain: bio, medical
type: Method
venue: ECIR
paper_link: https://doi.org/10.1007/978-3-031-88720-8_1
---
# BioRAGent: Generative Query Expansion RAG for Biomedical Q&A
> ECIR 2025 | Method | bio · medical

## TL;DR
A biomedical RAG demo system that combines LLM-based generative query expansion with PubMed search (Elasticsearch/BM25). It exposes the retrieval process transparently (with editable expanded queries) and presents a conversational Q&A interface that attaches PubMed ID citations at the sentence level. It was built on the basis of the authors' participation in the BioASQ 2024 challenge.

## Architecture (BioRAGent Architecture)
It is a Gradio-based web application and consists of four components.
- **Generative query expansion (LLM):** The LLM generates, in a few-shot (3-shot) manner, an expanded query that includes synonyms and related terms for the original question. After execution, the user can inspect and modify the expanded query, making retrieval transparent and controllable.
- **Document retrieval & snippet extraction:** Elasticsearch is used as the search engine, with an index of PubMed articles (abstracts and titles) from a 2023 snapshot. It retrieves the top 50 articles using the default BM25, after which the LLM extracts relevant snippets in a few-shot manner and reranks them again in a few-shot manner according to their relevance to the question.
- **Answer generation:** It generates answers grounded in the retrieved snippets (in the two formats below).
- **User interface (conversational UI):** It displays a question input box and search button, an editable expanded-query box, two answer boxes (with and without citations), and a list of snippets with PubMed links.

The few-shot examples are drawn from the BioASQ training set, and for query expansion the examples are sampled based on the highest F1.

## Pipeline (inference)
1. The user enters a question → the LLM generates an expanded query in a 3-shot manner (editable by the user).
2. The expanded query is used to search Elasticsearch (BM25) → the top 50 PubMed articles are obtained.
3. The LLM extracts snippets in a few-shot manner → then reranks the snippets in a few-shot manner according to their relevance to the question.
4. Grounding on the snippets, two answers are generated:
   - **Short paragraph-style answer** — grounded in the retrieved information (this format was used in the BioASQ challenge).
   - **Paragraph-style answer with citations** — an inline citation in the form of a PubMed ID is attached to each sentence.
5. The UI displays the expanded query, the two answers (with/without citations), and a list of snippets with direct PubMed links.

## Evaluation / Setup
- In its participation in **BioASQ 2024 (the 12th BioASQ challenge)**, it showed competitive performance with both commercial and open-source LLMs and achieved several 1st and 2nd places (most competitive in the 12B question-answering Phase A+/Phase B). The evaluation/release of the RAG approach itself is based on the authors' prior work of participating in BioASQ 2024.
- LLM used: Google **Gemini 1.5 flash 002** (for reasons of speed and low cost).
- This paper is a **demo paper** that showcases the system and does not newly present separate quantitative figures.

## Limitations
- It is a demo system paper that does not newly present quantitative evaluation results (the performance evidence relies on the prior BioASQ 2024 participation).
- The fixed single LLM (Gemini 1.5 flash 002), the lack of built-in live evaluation/hallucination verification, and the static template configuration are current constraints (future plans include live prompt editing, hallucination detection, and support for multiple-LLM selection).
- It is limited to a single PubMed snapshot (2023) and does not use any separate dense retrieval beyond BM25 + LLM rerank.

## Related links
- arXiv: 2412.12358 (https://arxiv.org/abs/2412.12358)
- DOI: https://doi.org/10.1007/978-3-031-88720-8_1 (ECIR 2025)
- Demo: https://bioragent.samyateia.de/ · GitHub: https://github.com/SamyAteia/BioRAGent
- Authors: Samy Ateia, Udo Kruschwitz
