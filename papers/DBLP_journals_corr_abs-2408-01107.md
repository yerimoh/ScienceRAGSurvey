---
title: "BioRAG: A RAG-LLM Framework for Biological Question Reasoning"
bib_key: "DBLP:journals/corr/abs-2408-01107"
year: 2024
domain: bio, medical
type: Method
venue: arXiv 2024
paper_link: https://arxiv.org/abs/2408.01107
---
# BioRAG: A RAG-LLM Framework for Biological Question Reasoning

> arXiv 2024 | 2024 | Method | bio · medical

## TL;DR
A 5-stage iterative RAG pipeline that indexes 22,371,343 PubMed abstracts and combines a MeSH classification model + a domain embedding + a self-evaluation loop + external search tools (10 external sources including 4 NCBI APIs for Gene/dbSNP/Protein/Genome plus a search engine). It outperforms all existing BioLLM and SciRAG systems such as GeneGPT, NewBing, BioMistral, and PMC-Llama across the 9 GeneTuring sub-tasks and 4 biomedical QA benchmarks.

## Background
**Limitations of existing approaches**
- Fine-tuned BioLLMs (BioMistral, PMC-Llama, etc.) hold only knowledge as of their training time → serious cutoff problems in the rapidly evolving field of life sciences
- A single RAG system (GeneGPT) is specialized only for specific API calls (Gene, dbSNP) and cannot perform multi-hop reasoning
- General search-engine-based RAG (NewBing) cannot access authoritative domain sources such as dbSNP and PubMed → "BIORAG and GeneGPT achieve 100% accuracy in the gene SNP association sub-task, as both of them have access to the dbSNP database. However, NewBing has no access to the dbSNP database, thus it gets 0% accuracy in this task." (paper p.7)

**Why this system is needed**
- Interdisciplinary research requires multi-layered knowledge spanning the molecule → cell → tissue → organism levels
- A closed-loop RAG capable of step-by-step reasoning + automatic switching to external search when information is insufficient is needed

## Construction Methodology
**Full 5-stage pipeline (paper Figure 2)**
```
[Input Question]
       │
       ▼
 ① Retriever Selection
   - Analyze the question type → the LLM decides which source is most suitable
   - Internal (PubMed local) vs External (Gene/dbSNP/Protein/Genome/Crossref/Wikimedia/biorxiv, etc.)
       │
       ▼
 ② Query Pre-processing
   - Rewrite the query + extract MeSH topic tags (MMeSH = Llama3-8B fine-tuned)
   - e.g.: "innate vs adaptive immunity" → MeSH: [Adaptive Immunity, Animals, ...]
       │
       ▼
 ③ Retriever Execution
   - Internal: MeSH SQL filter + embedding cosine ranking
   - External: NCBI Entrez API call / search engine call
       │
       ▼
 ④ Self-Evaluation (← core loop)
   - The LLM judges by itself "whether the retrieval results are sufficient for the answer"
   - If insufficient, return to ① and retry another source (up to 15 times)
       │
       ▼
 ⑤ Inference and Generation
   - Output the final answer + cited sources
```

### Core components
**Internal Source: PubMed 22M abstracts**
- Parsed the entire 2024 PubMed baseline
- Secured 22,371,343 high-quality abstract chunks after removing HTML/links/tables

**MMeSH (MeSH Classifier)**
- Llama3-8B fine-tuned with template: `"QUESTION: [.....] MeSH: [κ1, κ2, ...]"` (Figure 3)
- Generates SQL `filtered by: eq("MeSH", "Adaptive Immunity") or ...` from the predicted MeSH terms (Figure 4)
- After the first-pass filtering, ranks by embedding similarity

**Domain-Specific Embedding Model**
- AdamW, 2 epochs, domain-adapted on PubMed text
- Improved separability of biological technical terms compared to a general embedding

**External Sources (paper Table)**
- NCBI Gene / dbSNP / Genome / Protein (4 entities × Entrez API)
- biorxiv (preprints)
- Wikimedia (concept definitions)
- Crossref (citation network)
- Search engine (general web)

**Customized 5-Prompt Chain (paper Appendix)**
> "Prompt #1: To provide the most helpful and accurate response to the following Question: {Question}. You have been given descriptions..."
> "Prompt #2: Based on the RETRIEVAL METHODS you selected, and considering the Question and the Input Requirements..."
> "Prompt #4: Based on the RETRIEVAL RESULTS from the above steps, please evaluate whether the RESULTS support answering the..."
> "Prompt #5: Based on the RETRIEVAL RESULTS, perform a comprehensive reasoning and provide an answer to the Question."

## Input/Output
**Input**
- Biological question (free-form): nomenclature, genomic location, gene-disease association, functional analysis, protein-coding identification, multiple-choice biology/medicine questions

**Output**
- Natural language answer + (optional) cited sources
- For the 9 sub-tasks: gene symbol (e.g., "ARHGEF26"), location (chromosome band), Yes/No or MCQ answer

## Examples
### Example ① — Gene Alias Task (GeneTuring; paper Figure 6)
> **Query**: "What is the official gene symbol of SGEF?"
>
> **BioRAG execution log**
> > Thought: I can use the Gene tool to find the official gene symbol of SGEF.
> > Query Preprocessing → "SGEF"
> > Retriever Selection → Gene (NCBI)
> > Retriever Execution And Result:
> > "Official Symbol: ARHGEF26"
> > "Name: Rho guanine nucleotide exchange factor 26"
> > "Other Aliases: CSGEF, HMFN1864, SGEF"
> > Self-Evaluation: "The necessary information has been obtained to form an answer."
> > Inference and Generation: "The official gene symbol for SGEF is ARHGEF26."
>
> **NewBing comparison**: "The official gene symbol for SGEF is SGEF (Src homology 3 domain-containing Guanine nucleotide Exchange Factor)." → **wrong answer** (NewBing only retrieves a Wikipedia snippet)
>
> **GeneGPT comparison**: The Entrez API call succeeds but alias handling is inadequate

### Example ② — Multi-hop Gene-Disease Reasoning (Figure 7)
> **Query**: "What are genes related to B-cell immunodeficiency?"
>
> **BioRAG multi-stage execution**
> > Step 1: Retriever Selection = Gene → "Official Symbol: TOP2B, Other Aliases: BILU, TOPIIB, top2beta"
> > Self-Evaluation: "Use the PubMed tool to conduct further searches on genes and diseases." (first-pass result insufficient → jump to external)
> > Step 2: Retriever Selection = PubMed → "B cell development is a highly... Topoisomerase 2β (TOP2B) introduces..."
> > MeSH Mapping = Immunoglobulin G1 Fragments
> > Final answer: list of related genes such as TOP2B

### Example ③ — College Biology MCQ (Figure 5)
> **Question (litter size in rodents)** → BioRAG
> > Retriever Selection: PubMed Search → "Parental investment and litter size in rodents"
> > MeSH Mapping: Parental Behavior, Rodentia
> > Self-Evaluation: "Small litter sizes in rodents may be an adaptation to their specialized diet, requiring more parental investment."
> > Output: "Option B: High parental investment"

## Key Evaluation Results
**Table 1 — GeneTuring (9 sub-tasks, accuracy %)**
| Sub-task | GPT-3.5 | Llama-70B | BioMistral | GeneGPT | NewBing | **BioRAG** |
|---|---|---|---|---|---|---|
| Gene_alias | – | – | – | 98 | – | **100** |
| SNP_location | – | – | – | 100 | 0 | **100** |
| Gene_disease_association | – | – | – | 0 | 8 | **71** |
| Protein-coding genes | – | – | – | 40 | 80 | **100** |
| Gene_name_conversion | – | – | – | 66 | 32 | **71** |
| Functional analysis | 5 | 48 | 94 | 0 | 0 | **98** |
| Gene_alias (variant col) | – | – | – | – | – | **100** |

**Table 2 — Biological QA benchmarks (accuracy %)**
| Dataset | GPT-3.5 | Llama-70B | BioMistral | PMC-Llama | GeneGPT | NewBing | **BioRAG** |
|---|---|---|---|---|---|---|---|
| MedMCQA | 54 | 51 | 71 | 56 | 49 | 55 | **73** |
| Medical Genetics | 74 | 51 | 67 | 28 | 67 | 88 | **88** |
| College Biology | 73 | 75 | 88 | 30 | 67 | 71 | **90** |
| College Medicine | 65 | 61 | 70 | 23 | 51 | 78 | **78** |

**Key insights**
- BioRAG ties GeneGPT at 100% on API-dependent tasks such as nomenclature/genomic location
- On tasks that require reasoning, such as gene-disease association, GeneGPT(0%) > NewBing(8%) ≪ **BioRAG(71%)**

## Limitations
- The self-evaluation loop is fixed at a maximum of 15 iterations → risk of premature termination on deep multi-hop queries
- Very high cost of indexing 22M PubMed abstracts + Llama3-70B inference
- MeSH is not applicable to fields outside biomedicine (chemistry, materials, etc.)
- Dependence on external APIs → no defined fallback if NCBI/Crossref availability fails
- Prompt token cost explodes as the reasoning chain grows longer

## Related links
- **Paper (arXiv)**: [https://arxiv.org/abs/2408.01107](https://arxiv.org/abs/2408.01107)
- **Author affiliations**: Zhejiang University, OPPO Research, ETH Zürich
- **Benchmarks**: GeneTuring (Hou & Ji 2023), MedMCQA, MMLU subset (Medical Genetics, College Biology, College Medicine)
- **Base LLM**: Llama3-70B
- **K×O classification**: K1.O1 (PubMed literature) + K2.O1 (NCBI curated DB) — multi-source combination pattern
