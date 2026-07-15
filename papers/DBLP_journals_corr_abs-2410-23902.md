---
notion_id: 355f2dcd-4912-81ff-9980-de734a7c6161
title: Responsible Retrieval Augmented Generation for Climate Decision Making from Documents
bib_key: DBLP:journals/corr/abs-2410-23902
year: 2024
domain: earth
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2410.23902
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Responsible Retrieval Augmented Generation for Climate Decision Making from Documents

> arXiv | 2024 | Method | earth
## 📌 TL;DR
A paper that builds a responsible RAG system targeting climate law and policy documents, and releases a domain-specific 4-dimensional evaluation framework along with an expert human-annotated dataset.
## 🎯 Background and Motivation
**Limitations of existing methods**
- Climate law and policy documents are vast, technical, and written in multiple languages, making access to core information difficult
- General-purpose LLMs suffer from (1) hallucination and misinformation generation, (2) difficulty controlling output attributes, and (3) degraded performance in specialized domains
- Existing climate RAG apps (ChatClimate, ChatNetZero) either lack rigorous evaluation or are small-scale, and their UX does not link LLM-generated content back to the source text
- Research on legal-domain LLMs has clearly raised the need for fairness, transparency, and hallucination evaluation
**Why this research is needed**
- Climate decision support is a high-stakes AI application that directly affects human welfare
- Given that climate change disproportionately affects vulnerable populations and low- and middle-income countries, principles for responsible deployment are needed
- There is a lack of domain-specific generation policy guidelines and robust evaluation datasets
## 🏗️ Architecture
```javascript
[User Input]
    ↓
[Input Guardrails] → Filtering malicious/problematic queries (NeMo Guardrails, red-teaming)
    ↓
[Information Retrieval] → BM25 + Dense Retrieval hybrid
    ↓
[Answer Synthesis] → GPT-4/GPT-4o/Llama 3.1/Gemini-1.5-pro
    ↓
[Output Guardrails + Auto-Evaluators]
    - CPR policy compliance evaluation (Gemini-1.5-pro)
    - Faithfulness evaluation ensemble (Patronus Lynx + Gemini G-Eval + Vectara)
    - Formatting rule check
    - Response/no-response determination
    ↓
[UX Exposure] → Each evaluation result is transparently presented to the user
```
## 🔑 Detailed Description of Core Modules
**1. Database**
- Climate Policy Radar (CPR) DB: 6,000+ climate law and policy documents published by governments of all countries worldwide
- 550 documents sampled for evaluation (evenly distributed across World Bank Regions, stratified by translation status)
- Average of 80 pages, some over 1,000 pages, complex documents including tables, figures, and layouts
- Additional inclusion of IEA, IAEA, OSCE, WMO energy documents (for the RAG preference dataset)
**2. Retrieval Experiments**
| Method | Description |
| BM25 | Sparse retrieval baseline |
| Dense (4 types) | Open-source dense retrieval models standalone |
| Hybrid (4 types) | α·BM25 + dense (α=0.2) |

- Benchmarked with a total of 173,000 pairwise LLM judgments
- Recall as the top-priority metric (maximizing the proportion of relevant information passed to the LLM)
**3. Evaluation Framework 4 Dimensions**
| Dimension | Description | Evaluation Method |
| CPR generation policy compliance | Fairness, objectivity, faithfulness, avoiding human safety risks | Gemini-1.5-pro LLM-as-judge |
| Faithfulness | Generation grounded in provided context (hallucination detection) | Patronus Lynx + Gemini G-Eval + Vectara ensemble |
| Formatting | Markdown bullet-point + citation rules | regex/text rule-based |
| Response/no-response | Correct handling of unanswerable cases | Text search |

**4. Human Annotation**
- UNECE collaboration: 16 domain experts (UN, IRENA, WMO, various national governments)
- 3-week annotation sprint: labeling generated data for 800 documents
- Final dataset: 1,009 triples (query, retrieved passages, response), 15.6% policy violations
- Released on HuggingFace: [ClimatePolicyRadar/rag-climate-expert-eval](https://huggingface.co/datasets/ClimatePolicyRadar/rag-climate-expert-eval)
## 🧪 Experiments and Evaluation
**Retrieval Evaluation Results**
- Retrieval LLM Judge (GPT-4o based): F1 82.3% precision, 69.0% recall, 75.3% F1
- 194-question synthetic annotation dataset (2 expert annotators, 0-2 relevance scale)
- Limitations of the passage-ranking framing discovered: cases needing proximity signals for useful information, non-specific language, and document metadata
**Generation Evaluation Results (CPR policy compliance)**
| Model | Recall | Precision | F1 | Accuracy |
| GPT-4o | 0.987 | 0.343 | 0.509 | 0.708 |
| GPT-4 | 0.865 | 0.588 | 0.700 | 0.886 |
| Llama-3.1 | 0.487 | 0.854 | 0.620 | 0.908 |
| Gemini-1.5-pro | 0.961 | 0.542 | 0.693 | 0.869 |

- From a safe-deployment perspective, Recall is the top priority → Gemini-1.5-pro selected as the auto-evaluator
- Of 285 faithfulness violations, 100 (67.1%) overlapped with policy-violation True Positives
**Faithfulness Evaluator Ensemble**
- Vectara (NLU-based): low agreement with other models (different approach)
- Gemini↔GPT-4o: high agreement
- Patronus Lynx↔G-Eval Llama: pairwise F1 0.47 (fine-tuning produced large changes relative to the base model)
- Confirmed bias where an LLM prefers its own generations (self-preference bias)
- Final: Patronus Lynx + Gemini G-Eval + Vectara ensemble
## 💡 Key Contributions
- First proposal of a climate-domain-specific RAG generation policy and 4-dimensional evaluation framework
- Release of a human-annotated dataset built in collaboration with 16 UNECE experts (HuggingFace)
- Defense-in-depth UX design: transparently exposing each automatic evaluation result to the user
- Systematic comparison of open-source retrieval models vs BM25 hybrid
- Support for reproducibility in the climate/policy community through a live demo and released evaluation harness
## ⚠️ Limitations
- Current scope is single-document (multi-document extension incomplete)
- With a small policy-violation dataset, it is difficult to sufficiently validate the effect of prompt tuning
- Open-source dense models show limited performance compared to BM25 in certain settings
- Limitations of the passage-ranking framing itself (alternatives such as hierarchical and multi-hop retrieval proposed)
## 🔗 Related Research and Related Links
- **arXiv**: [https://arxiv.org/abs/2410.23902](https://arxiv.org/abs/2410.23902)
- **Live demo**: [https://queried.labs.climatepolicyradar.org/](https://queried.labs.climatepolicyradar.org/)
- **Dataset**: [https://huggingface.co/datasets/ClimatePolicyRadar/rag-climate-expert-eval](https://huggingface.co/datasets/ClimatePolicyRadar/rag-climate-expert-eval)
- **Annotation Guidebook**: [https://climatepolicyradar.notion.site/Annotation-Guidebook-for-Generative-AI-Data-Labelling](https://climatepolicyradar.notion.site/Annotation-Guidebook-for-Generative-AI-Data-Labelling)
- **Related research**: ChatClimate, ChatNetZero, ClimateGPT (prior work on climate-domain RAG)
