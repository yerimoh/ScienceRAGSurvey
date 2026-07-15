---
title: "Large Language Model Integration for Knowledge Retrieval and Interaction for the DUNE Experiment"
bib_key: rafique2025large
year: 2025
domain: physics
type: Method
venue: arXiv (Lepton Photon 2025)
paper_link: https://arxiv.org/abs/2601.05278
---
# DUNE-GPT: LLM Integration for Knowledge Retrieval in the DUNE Experiment

> arXiv 2601.05278 | 2025 | Method | physics
> Rafique, Singh, Srinivas — Argonne National Laboratory (DUNE Collaboration)
> Presented at Lepton Photon 2025, Madison WI

## TL;DR
A RAG prototype system that retrieves DocDB, Indico, and internal wiki documents of the **Deep Underground Neutrino Experiment (DUNE)** on Fermilab/ALCF infrastructure (Aurora supercomputer + Argo + Ollama). Indexed with `multi-qa-mpnet-base-dot-v1` + FAISS, reporting **preliminary retrieval accuracy ~70%** across diverse query types. On-premise; accessible only to authenticated DUNE collaborators.

## Background
**Limitations of existing approaches**
- The DUNE collaboration stores documents across **multiple distributed platforms** such as DocDB (technical design reports/TDR, analysis notes), Indico (meetings/presentations), and internal wikis
- Finding information on reconstruction, simulation, data analysis, and detector operations is time-intensive for new collaborators
- Directly using commercial LLMs raises concerns about **data privacy, reproducibility, and network accessibility**
- Needs similar to chATLAS/MITRA of ATLAS/CMS

**Why DUNE-GPT was needed**
- As a "next-generation neutrino experiment," external transfer of unpublished data is prohibited
- Must operate within Fermilab compliance
- Requires a secure interface accessible only to authenticated DUNE collaborators

## How It Was Built (Construction Methodology)

```
Step 1 — Data source collection
  ┌─ DocDB : TDR, analysis notes, technical notes
  ├─ Indico : meeting presentation materials, meeting notes
  └─ internal wiki : DUNE operations documents
  Formats: PDF, DOCX, TXT, PNG, and various others
  Sensitive/restricted content is **excluded** per collaboration policy
  → only collaboration-wide accessible documents are processed

Step 2 — Preprocessing
  Metadata extraction (date, author, document type)
  token-level segmentation → embedding preparation

Step 3 — Embedding & Retrieval
  Embedding model: multi-qa-mpnet-base-dot-v1
                    (transformer encoder, scientific-text optimized)
  Vector DB: FAISS (Facebook AI Similarity Search)
  Similarity: cosine similarity

Step 4 — Response Generation (on-premise)
  LLM hosting:
  ┌─ Argonne (Argo)    : prototype development
  └─ Fermilab (Ollama) : final deployment infrastructure
  RAG: condition the LLM on retrieved snippets
       → minimize hallucination risk + grounded answer
  Returns: answer + citations to DUNE internal sources

Step 5 — Deployment
  Aurora supercomputer (ALCF) → migration to Fermilab in progress
  Python backend, lightweight web interface
  Accessible only to authenticated DUNE collaborators (Fermilab SSO integration planned)

Step 6 — Preliminary evaluation (Sec. 4)
  Detector specifics + reconstruction algorithms
    + physics analysis workflows
  Retrieval accuracy ~70% (preliminary, no quantitative IR metrics conducted)
```

## Input
- Natural language queries (web interface)
- Authenticated DUNE collaborator credentials

## Output
- Answers grounded in retrieved context + citations to DUNE internal sources
- top-3 retrieved references (displayed in Fig. 3 frontend)

## Example Questions (content stated in the paper body)

> This paper is a short 4-page proceedings, and **concrete verbatim Q/A examples are not included in the body**. However, it specifies the evaluation scope and interface of the system as follows:

### 📘 Evaluation query categories (verbatim from Sec. 4 body)
> "Initial benchmarks demonstrate that the RAG-based system retrieves relevant documentation with high accuracy (∼70%) across **diverse query types, including detector specifics, reconstruction algorithms, and physics analysis workflows**."

### 📘 Frontend example (Fig. 3 caption)
> "Frontend web interface showing a sample question, response, and the **top three retrieved references** used in response generation."
> *(the concrete question text is shown only in the figure and is not inline-cited in the body)*

### 📘 Data source scope
> "We extracted publicly accessible and internal DUNE documentation, including DUNE documents, presentations, meeting notes, technical design reports, and working group materials from DocDB and Indico."

### 📘 Security policy (Sec. 3 body)
> "all operations—including embedding generation and LLM inference—are performed within the DUNE internal computing environment. **Only authenticated DUNE collaborators will be able to use this tool.**"

> This paper is a system overview proceedings, and a quantitative evaluation + concrete Q/A case studies are planned for a follow-up paper.

## Key Results (Sec. 4 Preliminary)

| Item | Value |
|---|---|
| **Retrieval accuracy (preliminary)** | ~70% (across diverse query types) |
| Embedding model | `multi-qa-mpnet-base-dot-v1` |
| Vector DB | FAISS |
| Generation LLM | Argo (Argonne) + Ollama (Fermilab) |
| HW (prototype) | Aurora supercomputer (ALCF, Intel Gaudi) |
| HW (deploy) | Fermilab Ollama infrastructure |
| Processed formats | PDF, DOCX, TXT, PNG, etc. |

> **No comparison baseline**: no quantitative comparison against BM25 baselines such as MITRA (CMS, P@1=0.75 on semantic queries) or chATLAS (ATLAS, GPT-4o-mini API) was conducted. The authors explicitly note it is "preliminary."

## Limitations (stated by the authors)
- **Prototype stage** — before collaboration-wide deployment, systematic benchmarks are absent
- **Sensitive documents excluded**: controlled materials cannot be indexed per collaboration policy → incomplete knowledge coverage
- **No quantitative metrics**: no evaluation with IR metrics such as P@k, MRR, recall@k
- No quantitative comparison against baselines such as BM25
- Multi-modal content (plots, figures) not integrated — future work
- No optimization experiments on the retrieval-model and LLM combination
- Transferability beyond DUNE to LBL/SBN/external experiments not validated

## Related links
- **Paper**: [arXiv:2601.05278](https://arxiv.org/abs/2601.05278) (v2, 13 Jan 2026)
- **Presentation**: 32nd International Symposium on Lepton Photon Interactions at High Energies, Madison WI, Aug 25–29, 2025
- **Author affiliation**: Argonne National Laboratory (DUNE Collaboration)
- **Infrastructure**: Aurora (ALCF) + Argo + Fermilab Ollama
- **Similar systems**: chATLAS (ATLAS), MITRA (CMS), AI4EIC RAGS4EIC (EIC)
- **Grant**: U.S. DOE Office of HEP + multinational funding agencies
