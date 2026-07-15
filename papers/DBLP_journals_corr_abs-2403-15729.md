---
title: "Towards a RAG-based Summarization Agent for the Electron-Ion Collider"
bib_key: "DBLP:journals/corr/abs-2403-15729"
year: 2024
domain: physics
type: Method
venue: arXiv 2024
paper_link: https://arxiv.org/abs/2403.15729
---
# Towards a RAG-based Summarization Agent for the Electron-Ion Collider (RAGS4EIC)

> arXiv:2403.15729 | 2024 | Method | physics
> AI4EIC — EIC Collaboration (1,400+ physicists, 38 countries)

## TL;DR
A LangChain-based RAG agent that indexes the vast institutional documents, papers, and data of the **EIC (Electron-Ion Collider)** collaboration — involving 1,400+ physicists from 38 countries — into a single vector DB, and generates **citation-rich, concise summaries** with an LLM (GPT-3.5). Achieves **Hallucination Frequency of 2% and Context Entity Recall of 98.7% in RAGAS score evaluation**.

## Background
**Limitations of existing approaches**
- In the EIC collaboration involving 1,400+ physicists from 38 countries, coordinating information curation across many working groups is difficult
- It is time-intensive for new collaborators and early-career scientists to understand the vast EIC data and documents
- The volume of documents a shift taker must review during experiments and data collection is overwhelming for beginners

**Why this system was needed**
- A virtual assistant that can be referenced instantly during shift work is needed
- To encourage collaborative participation and lower the entry barrier for new researchers
- To suppress LLM hallucination with citation-based responses, thereby securing reliability

## Construction Methodology

```
Step 1 — Knowledge base construction (Fig. 2)
  ┌─ Data sources : EIC-related wiki, run logs, PDFs, untagged materials
  ├─ Text extraction via OCR + DL models (figures/images have extraction limits)
  ├─ PDF Reader : PyPDF2 (figure loss occurs)
  ├─ LaTeX Reader : LatexSplitter
  └─ Chunking : LangChain RecursiveCharacterTextSplitter

Step 2 — Vectorization + indexing
  chunk → vector via Embedding model
  Store in VectorDB (cf. evolved to ChromaDB in the follow-up jat2026retrieval)

Step 3 — Online inference pipeline (Fig. 3)
  User question + (cosine sim or MMR) selection
       ↓
  decision chain (LLM judges whether KB reference is needed)
       ↓
  If needed, retrieve context + sources from VectorDB
       ↓
  fine-tuned prompt template + retrieved context + question
       ↓
  GPT-3.5-turbo-1106 (LLM) — response including citations
       ↓
  GitHub markdown formatted output (syntactic LLM)

Step 4 — LLM-assisted benchmark generation
  ┌─ Domains: hep.ph / nucl-ex / ph-acc
  ├─ An "annotator" selects arXiv papers + specifies claim count N
  ├─ GPT-4.0 generates (Question, Answer{claims, ideal_response, full_response})
  └─ annotator reviews, edits, and registers
  → AI4EIC2023_DATASETS (50 questions × up to 3 claims)

Step 5 — Evaluation (RAGAs framework)
  Standard metrics + RAGAs LLM-judge metrics (GPT-4)
```

## Input
- Vector DB: EIC institutional documents, arXiv papers, run logs, wikis, technical design reports
- User query: natural language (Streamlit web app: `rags4eic-ai4eic.streamlit.app`)
- Retrieval settings: cosine similarity / MMR, top-k=20

## Output (Answer format)
- GitHub-markdown format summary + arXiv citations
- inference trace tracked with LangSmith

## Example items (paper Section 5 evaluation + direct quotes from Appendix A)

### 📘 Benchmark dataset generation process (verbatim from the text)
> "The 'annotator' chooses an arXiv paper (with an option for a random, unexplored selection), the total questions to generate, and the claims per question. GPT-4.0 then processes the paper's contents using a template to produce formatted Question and Answer pairs."

### 📘 Dataset structure (each Q holds N "claims")
> "Each QA pair has a question with 'N' claims and a detailed json object which has detailed information about the answers. The json object contains the number of claims in the questions, the individual claims, ideal response to each of the individual claims, and a complete response involving all the claims."

### 📘 Domain scope
> "The dataset selected for this research encompasses a variety of disciplines, ranging from hep.ph to nucl-ex to ph-acc" *(arXiv categorical codes in physics)*

### 📘 Key limitation (direct quote from the authors)
> "The RAG Agent's ability to provide accurate responses to inquiries decreases significantly when dealing with questions that involve physics equations (including special LaTeX characters)."

> Example use case: In Appendix A, Fig. 4·5 visualize the "annotator" interface + inference flow. The main text does not quote specific Q text, and the 50 Q × 3 claim of AI4EIC2023_DATASETS are separately released in the GitHub code.

## Key evaluation results

**Standard Metrics (Table 2, 50Q × 3 claim)**

| Metric | Definition | Score |
|---|---|---|
| Claim Recognition Rate | answered claims / total claims | **96.4 ± 3.4%** |
| Claim Accuracy Rate | correctly answered claims / recognized | 88.9 ± 8.3% |
| Source Citation Frequency | source-cited queries / total | 85.3 ± 5.0% |
| **Hallucination Frequency** | hallucinations / total queries | **2 ± 2%** |

**RAGAs LLM-as-judge (Table 3, GPT-4 evaluation)**

| Metric | Score |
|---|---|
| Faithfulness (markdown rendering correctness) | 87.4 ± 5.5% |
| Context Relevancy | 61.4 ± 4.3% |
| **Context Entity Recall** | **98.7 ± 1.2%** |
| Answer Relevance | 77.2 ± 2.3% |
| Answer Correctness | 72.3 ± 2.4% |

## Limitations (stated by the authors)
- **Context Relevancy 61.4%**: due to fixed k=20 retrieval, much redundant information is included (pronounced when responses are short)
- **Weakness in handling physics equations**: accuracy clearly drops on questions containing LaTeX equations → better chunking strategy needed
- **Routing logic**: additional instruction-tuning needed for GitHub markdown rewriting
- **Reproducibility**: partially resolved with LangSmith trace, but limitations remain due to LLM stochasticity
- **Use of cloud-hosted external KB** → risk of external transmission of unpublished pre-release data (resolved with local deployment in the follow-up jat2026retrieval)

## Related links
- **Paper (arXiv)**: [https://arxiv.org/abs/2403.15729](https://arxiv.org/abs/2403.15729)
- **Web app**: [https://rags4eic-ai4eic.streamlit.app](https://rags4eic-ai4eic.streamlit.app)
- **Source code**: [https://github.com/ai4eic/EIC-RAG-Project](https://github.com/ai4eic/EIC-RAG-Project)
- **AI4EIC2023_DATASETS**: publicly available on GitHub (50Q × 3 claim)
- **Follow-up work**: jat2026retrieval (arXiv:2604.02259) — locally-deployed LLaMA-based extension
