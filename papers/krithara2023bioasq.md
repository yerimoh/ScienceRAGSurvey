---
title: "BioASQ-QA: A manually curated corpus for Biomedical Question Answering"
bib_key: "krithara2023bioasq"
year: 2023
domain: medical, bio
type: benchmark
venue: Scientific Data (Nature)
paper_link: https://doi.org/10.1038/s41597-023-02068-4
---
# BioASQ-QA: A manually curated corpus for Biomedical Question Answering

> Scientific Data 2023 | Benchmark + Challenge Infrastructure | medical · bio

## TL;DR
The **cumulative QA dataset of the BioASQ Challenge Task B**, which has been run annually since 2012. Along with **4,721 questions** (as of 2022) authored directly by 21 biomedical experts (predominantly EU-based), it provides **relevant documents, snippets, ontology concepts, RDF triples, exact answers, and paragraph-level ideal answers** through an 8-step annotation protocol. It is the only biomedical benchmark that simultaneously evaluates IR + QA + multi-document summarization.

---

## How It Was Built (Construction Methodology)

```
BioASQ infrastructure = Expert team + Annotation tool + Assessment tool + Challenge

Step 0 — Expert team formation (2012~)
  └─ 21 experts (cardio, psychiatry, pharmacology, drug repositioning,
     genomics, proteomics, clinical IR, etc. — broad coverage)
  └─ 7 contributed most actively
  └─ Target of ~500 questions per person per year

Step 1 — Question formulation (start of the 8-step annotation)
  ┌──────────────────────────────────────────────┐
  │ Choose 1 of 4 question types:                 │
  │  · Yes/No                                    │
  │    e.g. "Do CpG islands colocalise with TSS?"│
  │  · Factoid (single-entity answer)            │
  │    e.g. "Which virus causes mononucleosis?"  │
  │  · List (list of entities)                   │
  │    e.g. "Which are the Raf kinase inhibitors?"│
  │  · Summary (needs a 1-paragraph summary)      │
  │    e.g. "How does dabigatran affect aPTT?"   │
  └──────────────────────────────────────────────┘
  ⚠ Guidelines: within a range where a PubMed query can retrieve 10–60 articles,
                 avoid controversial questions, must be biomedical domain

Step 2 — Relevant concept selection (including synonym/broader/narrower)

Step 3 — Information retrieval (PubMed advanced query)
   ↓ Various queries are possible (empirically, "many roads lead to Rome")

Step 4 — Selection of a sufficient article set
Step 5 — Text snippet extraction (full-sentence units, multiple articles allowed)
Step 6 — Query revision (repeat Steps 2-5; if no answer can be found, discard the question)

Step 7 — Exact answer
  · Yes/No → "yes" / "no"
  · Factoid → entity name + all synonyms
  · List → list of entities + synonyms of each element
  · Summary → blank (consolidated in Step 8)

Step 8 — Ideal answer (1-paragraph)
  Must be based on the snippets from Step 5 (no expert personal opinion),
  free to rephrase/shorten/order, written to be easy for other experts to read

[Post-challenge] Assessment phase:
  Experts review system answers to the questions they created,
  → any missing relevant docs/snippets are added to the gold dataset → dataset quality improves incrementally
```

---

## Data Sources (Drug-Target-Disease triangle)

| Axis | Resource | Scale |
|---|---|---|
| **Drugs** | **Jochem** (Joint Chemical Dictionary — integrates UMLS+MeSH+ChEBI+DrugBank+KEGG+HMDB+ChemIDplus) | — |
| **Targets** | **Gene Ontology** (cellular component / molecular function / biological process) | — |
|  | **UniProt SwissProt** (manual review) | >500k sequences |
| **Diseases** | **Disease Ontology** (integrated mapping of MeSH/ICD/NCI/SNOMED/OMIM) | ~8,000 diseases |
| **Documents** | **MEDLINE/PubMed** (abstracts only since BioASQ-4, 2016) | >34M citations |
| **Indexing** | **MeSH** (16 trees) | ~30,200 descriptors |
| ~~Linked Data~~ | ~~Linked Life Data~~ (10B statements) — *abandoned recent editions* | — |

---

## Cumulative Dataset Growth (BioASQ Challenge 1~10)

| Year | Challenge | Cumulative #questions | Avg #docs/Q | Avg #snippets/Q |
|---|---|---|---|---|
| 2012 | BioASQ-1 (proof-of-concept) | 10 | – | – |
| 2013 | BioASQ-2 | 310 | 14.28 | 18.71 |
| 2014 | BioASQ-3 | 810 | 13.45 | 13.30 |
| 2015 | BioASQ-4 | 1,307 | 13.00 | 17.86 |
| 2016 | BioASQ-5 | 1,799 | 11.86 | 20.38 |
| 2017 | BioASQ-6 | 2,251 | 12.01 | 14.76 |
| 2018 | BioASQ-7 | 2,747 | 11.14 | 13.91 |
| 2019 | BioASQ-8 | 3,243 | 10.15 | 12.92 |
| 2020 | BioASQ-9 | 3,742 | 9.43 | 12.33 |
| 2021 | BioASQ-10 | 4,234 | 9.22 | 12.24 |
| **2022** | **(current)** | **4,721** | **8.58** | **11.36** |

> ⚠ Trend: the average number of docs/snippets gradually decreases — the Sufficient-set policy (from BioASQ-4) requires only the "minimal" evidence.

---

## Domain-Suitability Judgment Examples (paper Section 'Annotation process', verbatim)

> **Q1 (REJECTED):** *"Which are the differences between Hidden Markov Models (HMMs) and Artificial Neural Networks (ANNs)?"*
> · A general ML comparison — no explicit statement of direct biomedical application → rejected.
>
> **Q2 (ACCEPTED):** *"Which are the uses of Hidden Markov Models (HMMs) in gene prediction?"*
> · Explicitly states a biomedical application, "gene prediction" → accepted.

→ BioASQ only allows questions with a clear biomedical application, and avoids controversial medical debates or those without an answer.

## Retrieval-Step verbatim Examples (Tables 1-3 in paper)

### Step 3 PubMed Query (Q: "Do CpG islands colocalise with transcription start sites?")
> Extracted relevant terms: "CpG Island", "transcription start site", + synonym "Transcription Initiation Site"
> PubMed Advanced Query: `"CpG Island" AND "transcription start site"`
>
> Example of retrieved articles (Table 1):
> · *"Putative Zinc Finger Protein Binding Sites Are Over-Represented in the Boundaries of Methylation-Resistant CpG Islands in the Human Genome"*
> · *"CpG Islands: Starting Blocks for Replication and Transcription"*

### Step 5 Text Snippet Example (Table 2)
> *"A common explanation for the G+C rise that is seen here in the mammalian profile in the proximity of the TSS is the presence of CpG islands, ..."*

### Step 8 Ideal Answer (Table 3, verbatim)
> *"Yes. It is generally known that the presence of a CpG island around the TSS is related to the expression pattern of the gene. ..."*

## Actual Instance Example (JSON format)

```json
{
  "id": "52bf1b0a03868f1b06000009",
  "body": "Do CpG islands colocalise with transcription start sites?",
  "type": "yesno",
  "documents": [
    "https://www.ncbi.nlm.nih.gov/pubmed/838566", ...
  ],
  "snippets": [
    {"text": "A common explanation for the G+C rise that is seen
              here in the mammalian profile in the proximity of
              the TSS is the presence of CpG islands, ...",
     "document": "...", "beginSection": "abstract",
     "offsetInBeginSection": 122, "offsetInEndSection": 272}, ...
  ],
  "concepts": ["https://www.disease-ontology.org/api/metadata/DOID:893", ...],
  "triples": [{"s":"...","p":".../name","o":"Wilson_disease"}, ...],
  "ideal_answer": ["Yes. It is generally known that the presence
                    of a CpG island around the TSS is related to
                    the expression pattern of the gene. ..."],
  "exact_answer": "yes"
}
```

---

## Evaluation Metrics (Task B)

| Phase | Evaluation target | Metric |
|---|---|---|
| **Phase A** | Document retrieval | MAP, Mean Precision/Recall/F-measure |
|  | Snippet retrieval | MAP, Mean Precision/Recall/F-measure |
|  | Concept retrieval | (same) |
|  | RDF triple retrieval | (same) |
| **Phase B** | Exact answer (Yes/No) | **Macro F1** (official from BioASQ-6 / Accuracy reported alongside) |
|  | Exact answer (Factoid) | Mean Reciprocal Rank, Strict/Lenient Accuracy |
|  | Exact answer (List) | Mean F1 |
|  | Ideal answer | 1–5 manual scoring × 4 criteria (recall / precision / repetition / readability) |

---

## Limitations
- **English only** — no multilingual biomedical QA.
- **Updated once a year** — delayed reflection of the latest literature compared to an environment where 2 papers are registered to PubMed per minute.
- **Abstract only** (from BioASQ-4): full-text PMC is not used → cannot evaluate information beyond abstracts such as tables and figures.
- **Linked Life Data abandoned** → the RDF triple evaluation axis is effectively inactive.
- **Expert bias**: of the 21 experts, Europe dominates → possible lack of global clinical diversity.
- **Controversial-question avoidance policy**: medical debates without a clear answer are intentionally excluded → some real-world clinical decision-making scenarios are missing.

---

## Related links
- **Paper**: [Scientific Data 10:170 (2023)](https://doi.org/10.1038/s41597-023-02068-4)
- **Official site**: [bioasq.org](http://bioasq.org)
- **Data download**: [participants-area.bioasq.org](http://participants-area.bioasq.org)
- **Major follow-up work using this benchmark**:
  - MEDRAG/MIRAGE (Xiong et al., ACL 2024) — reformulates 618 BioASQ-Y/N questions into MC format
  - AlzheimerRAG (Lahiri & Hu, MAKE 2025) — used for cross-modal evaluation
  - Comparison target of PubMedQA (Jin et al., EMNLP-IJCNLP 2019)
