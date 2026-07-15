---
notion_id: 355f2dcd-4912-81f0-8a5b-d3def3dd9529
title: Materials Dual-Source Knowledge Retrieval-Augmented Generation for Local Large Language Models in Photocatalysts
bib_key: DBLP:journals/jcisd/TakaharaYOKHTTKF25
year: 2025
domain: material, chem
type: Method
venue: J. Chem. Inf. Model.
paper_link: https://doi.org/10.1021/acs.jcim.5c01941
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Materials Dual-Source Knowledge Retrieval-Augmented Generation for Local Large Language Models in Photocatalysts

> J. Chem. Inf. Model. | 2025 | Method | material, chem

## TL;DR
A RAG framework (MDSK-RAG) that integrates CSV experimental data and PDF literature as dual sources, specializing a local LLM to the photocatalyst materials domain in a fully offline environment.

## Background and Motivation
- **Limitations of existing methods**: Cloud-based LLMs (e.g., GPT-4o) offer excellent performance, but in environments handling unpublished in-lab experimental data, external API use is not possible due to data confidentiality concerns. Existing RAG mainly handles only text literature, and lacks a method to integrate the lab's own CSV experimental data.
- **Why this research is needed**: A domain-specialized RAG system is needed that can simultaneously leverage confidential experimental records and scientific literature while enabling fully offline operation in a laboratory environment. There is a demand for a practical methodology that can rapidly boost the expertise of a local LLM without model retraining (fine-tuning).

## Architecture
```
[User query]
    |
    +---> [CSV Retriever] --> CSV-converted text DB (740 records) --> extract top-k relevant passages --> local LLM summary
    |
    +---> [PDF Retriever] --> PDF literature DB (20 papers)        --> extract top-k relevant passages --> local LLM summary
    |
    +---> [merge the two summaries + original query] --> local LLM (gemma-2-9b-it) --> final response generation
```

## Detailed Description of Core Modules
### 1. Dual-Database Construction
| Source | Content | Scale | Public availability |
|---|---|---|---|
| CSV experimental records | In-house metal sulfide photocatalyst experimental data | 740 records | Private |
| PDF scientific papers | Peer-reviewed scientific papers | 20 papers | Private |

### 2. CSV → Template-based Text Conversion
- Preprocesses structured CSV table data into natural-language template text so it becomes searchable via vector retrieval.
- Example: converted into the form `The hydrogen evolution rate of {material name} is {value} μmol/h, and the conditions are {conditions}.`

### 3. Dual Retriever
- A Retriever for the CSV-converted text and a Retriever for the PDFs are configured independently.
- Each returns top-k relevant passages via cosine-similarity-based vector retrieval.
- All computation is fully local (no-Internet).

### 4. Post-retrieval: Summarization and Merging
- The local LLM individually summarizes each retriever's results.
- The two summaries are merged (fusion) and, together with the original query, fed into the final generation LLM.

### 5. Generator (Local LLM)
| Model | Size | Hardware |
|---|---|---|
| gemma-2-9b-it (primary, quantized) | ~9B | Laptop GPU (16GB VRAM) |
| Qwen2.5-7B-Instruct | ~7B | Laptop GPU |
| gemma-2-27b-it | ~27B | Dedicated server (RTX 3090, 24GB VRAM) |

## Experiments and Evaluation
### Evaluation Tasks and Datasets
- **Photocatalyst Expert QA**: An in-house benchmark composed of 14 questions defined by domain experts.
- Question types: a mix of factual questions related to experimental conditions and reasoning/interpretation questions.

### Main Results
| Model | Condition | Cosine Similarity (median) | Expert 5-point rating (median) |
|---|---|---|---|
| gemma-2-9b-it | Without MDSK-RAG | 0.63 | 2 |
| gemma-2-9b-it | With MDSK-RAG | 0.71 (+12.70%) | 3 (+50.00%) |
| GPT-4o | Without MDSK-RAG (cloud) | 0.66 | — |

- Wilcoxon signed-rank test: W=14.0, p=1.34×10⁻² (statistically significant)
- gemma-2-9b-it with MDSK-RAG applied surpasses GPT-4o (without RAG) on the cosine similarity metric.

## Key Contributions
- Proposes a near-first offline materials-science RAG framework that integrates CSV (experimental records) and PDF (literature) dual sources.
- Strengthens the domain expertise of local small LLMs (<10B) without model retraining.
- Presents a practical solution that can leverage confidential experimental data without external leakage.
- Empirically demonstrates that a sub-10B local LLM + MDSK-RAG can outperform a high-performance cloud model (GPT-4o, without RAG) in a specific domain.

## Limitations
- In reasoning-type questions, incomplete context retrieval induces erroneous reasoning (a reasoning failure mode exists).
- Being specialized for the metal sulfide photocatalyst domain, applying it to other materials systems requires domain-specific adjustment.
- The evaluation benchmark is small at 14 questions (limited statistical power).
- Future work: proposals such as a hybrid symbolic approach and building a domain-specific knowledge graph.

## Related Work and Related Links
- **Paper link**: [https://doi.org/10.1021/acs.jcim.5c01941](https://doi.org/10.1021/acs.jcim.5c01941)
- **Related methodologies**: HoneyComb, G-RAG, TopoChat (materials-science RAG family)
- **Benchmark used**: Photocatalyst Expert QA (in-house, 14 questions)
