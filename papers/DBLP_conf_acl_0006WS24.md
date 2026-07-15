---
title: "MindMap: Knowledge Graph Prompting Sparks Graph of Thoughts in Large Language Models"
bib_key: "DBLP:conf/acl/0006WS24"
year: 2024
domain: medical
type: Method
venue: ACL
paper_link: https://arxiv.org/abs/2308.09729
---
# MindMap: Knowledge Graph Prompting for Medical QA
> ACL 2024 | Method | medical

## TL;DR
MindMap is a KG-prompting framework that retrieves query-relevant evidence subgraphs from a curated clinical knowledge graph (disease-symptom-drug-test) and integrates them into natural-language reasoning paths ("graph of thoughts"), prompting the LLM to combine explicit KG knowledge with implicit knowledge and produce grounded answers together with a reasoning path (mind map).

## Architecture (MindMap Architecture)
- **Curated clinical KG:** EMCKG (English, 1,122 nodes / 5,802 triples / 6 relations) and CMCKG (Chinese, 62,282 nodes / 506,490 triples / 12 relations). Clinical flow of symptom→disease→test/drug.
- **Evidence subgraph retrieval (two complementary types):** query entity extraction with an LLM + KG node matching via BERT similarity → ① path-based (connecting query entities via ≤k hop paths), ② neighbor-based (expanding 1-hop neighbors of path nodes). Pruning via clustering and sampling.
- **Graph-of-thoughts:** the LLM converts and aggregates the entity chains of the retrieved subgraphs into natural language, integrating them into a single reasoning graph.
- **Prompt:** system instruction + question + evidence graph + graph-of-thought instruction + exemplars.

## Pipeline (inference)
1. **Evidence graph mining:** entity recognition (LLM+BERT) → path/neighbor subgraph retrieval.
2. **Aggregation:** integrate and refine the subgraphs into a single reasoning graph.
3. **Reasoning:** via the prompt, the LLM combines the graph with implicit knowledge → outputs (a) a summary answer, (b) the reasoning process, (c) a mind map (structured text).

## Key results
With GPT-3.5 as the backbone, it surpasses GPT-4 on some baselines. Datasets: GenMedGPT-5k, CMCQA, ExplainCPE.
- GenMedGPT-5k BERTScore F1: MindMap **0.7954** > KG Retriever 0.7868 > GPT-4 0.7786. In GPT-4-evaluated ranking, MindMap 1.87 vs GPT-4 4.18.
- Pairwise comparison (MindMap vs GPT-4 win rate): diversity/integrity 100%, drug recommendation 83%, diagnosis 73%.
- ExplainCPE accuracy 61.7%. Ablation: combining path+neighbor outperforms either alone.

## Limitations
- Performance depends on the completeness and accuracy of the curated clinical KG, with limited generalization to domains lacking a KG.
- Errors in entity recognition and matching can contaminate the subgraph.
- Evaluation relies on GPT-4 judges and BERTScore (potentially biased) and is limited to three medical datasets.

## Related links
- arXiv: 2308.09729 · ACL 2024 (Wen, Wang, Sun)
- Code: https://github.com/wyl-willing/MindMap
