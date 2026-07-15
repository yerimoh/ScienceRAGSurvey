---
notion_id: 355f2dcd-4912-8151-ac54-f3cf4d24cf83
title: PaperQA2 / LitQA2 - Language Agents Achieve Superhuman Synthesis of Scientific Knowledge
bib_key: DBLP:journals/corr/abs-2409-13740
year: 2024
domain: bio, medical
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2409.13740
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Language Agents Achieve Superhuman Synthesis of Scientific Knowledge

> arXiv | 2024 | Method | bio

## TL;DR
PaperQA2 is the first RAG agent system to achieve performance exceeding unrestricted human experts (PhDs / PhD students) across three real-world tasks: scientific literature search, summarization, and contradiction detection.

---
## Background and Motivation
**Limitations of existing methods**
- LLMs suffer from hallucination (confidently generating incorrect information), making it hard to meet the demands of scientific accuracy
- Existing scientific-literature benchmarks (PubMedQA, BioASQ, etc.) use only abstracts or fixed corpora, failing to reflect real research settings
- Most existing benchmarks do not compare directly against human performance, leaving their practical value unclear
- Simple RAG (Perplexity, Elicit, etc.) injects retrieved chunks into the context without transformation, causing a distracting-context problem

**Why this research is needed**
- Automating literature search, summarization, and contradiction detection in scientific research can dramatically improve researcher productivity
- With the explosion of literature, it has become impossible for humans to check the entire body of work one by one, creating a need for AI-based automated detection systems
- In particular, contradiction detection is a "many vs many" problem that can operate at a scale infeasible for humans

---
## Architecture

```
[User query]
     ↓
[PaperQA2 Agent (GPT-4-Turbo, ReAct pattern)]
     ├── Paper Search Tool
     │     Generate keywords + year range → search Semantic Scholar API
     │     → Grobid/PyMuPDF parsing → Hybrid embedding (dense+sparse)
     │     → store chunks (agent state)
     │
     ├── Citation Traversal Tool  ← NEW
     │     Traverse 1-hop citations/references of papers with RCS score ≥ 8
     │     → overlap fraction filtering → add up to 12 papers
     │
     ├── Gather Evidence Tool
     │     top-k (default 30) cosine-similarity search
     │     → RCS: LLM completion on each chunk
     │         → summary (200~400 tokens) + relevance score (0~10)
     │     → score-based reranking → store top summaries
     │
     └── Generate Answer Tool
           Top N (default 15) summaries → LLM final answer generation
           → output cited Wikipedia-style answer
```

**WikiCrow** (summarization-specialized): gene name → 4 PaperQA2 calls for each of the structure/function/interaction/clinical-significance sections + 1 overview LLM → synthesized with Python

**ContraCrow** (contradiction-detection-specialized): split paper into chunks → LLM claim extraction → quality filtering (≥8/10) → contradiction-detection query on each claim via PaperQA2 → output 11-point Likert score

---
## Key Module Details
### RCS (Reranking & Contextual Summarization)
| Item | Content |
|---|---|
| Input | top-k chunks (default 30) |
| Processing | LLM completion on each chunk: JSON output of summary + relevance score (0~10) |
| Output | contextual summaries reordered by score |
| Characteristics | high efficiency via parallel processing; injects source metadata (citation count, journal name) |
| Effect | significantly improves accuracy vs. No RCS (t=9.29, p<0.001) |

### Citation Traversal Tool
| Item | Content |
|---|---|
| Origin | starts from papers with RCS score ≥ 8 |
| Direction | both forward (future citers) and backward (past references) |
| API | Semantic Scholar + Crossref |
| Filter | overlap fraction α=1/3: keep only papers commonly cited by multiple source papers |
| Limit | up to 12 papers per call |
| Effect | significantly improves DOI recall (t=3.4, p=0.022) |

### Tool / DB Integration Table
| Tool | Role | Notes |
|---|---|---|
| Semantic Scholar API | Paper search and citation traversal | default 12 papers/search |
| Crossref API | Traversal of past references | complements Semantic Scholar |
| Grobid | Section/table/citation parsing | essential for WikiCrow; 44% token savings |
| PyMuPDF | Default PDF parsing | default for LitQA2 experiments |
| OpenAI Embeddings | Embedding generation | text-embedding-3-large |

---
## LitQA2 Benchmark Details (the closed-form QA benchmark built by this paper)

Along with the system (PaperQA2), this paper proposes the **LitQA2** benchmark. It is an extension of LitQA (the original PaperQA one, 47 questions), consisting of **248 multiple-choice (MCQ) biomedical questions**. The answers are based on facts that appear **only in the main body** of a paper and not in the abstract.

### Construction Methodology

```
Step 1 — Source-paper selection principle (quoted from the paper's §LitQA2 body)
  "LitQA2 questions are designed to have answers that appear in
   the main body of a paper, but not in the abstract, and ideally
   appear only once in the set of all scientific literature."
  → papers published after the training-data cut-off + facts that require main-body search

Step 2 — Staged release (quoted from the paper's §8.4 body)
  "LitQA2 was built up from LitQA (47 questions) in two stages
   of releases, first 100 questions (147), then an additional 101
   questions, adding to the original subset to make 248 total
   questions."
  ┌──────────────────────────┬────────────┐
  │ Stage                    │ Cumulative │
  ├──────────────────────────┼────────────┤
  │ Original LitQA           │         47 │
  │ + Stage 1 (development)  │        147 │
  │ + Stage 2 (held-out new) │        248 │
  └──────────────────────────┴────────────┘
  Stage 2 was newly written after the PaperQA2 engineering changes,
  verifying that PaperQA2 did not overfit to LitQA2.

Step 3 — Evaluation metrics (defined in the paper's §LitQA2 metric)
  · Accuracy = CorrectAll / All       (fraction of all questions answered correctly)
  · Precision = CorrectSure / AnsweredSure
    (fraction correct among those answered; leverages the "Insufficient information" option)
  The presence of the Insufficient-information option allows admitting ignorance → separates precision/accuracy

Step 4 — Automatic evaluation pipeline (quoted from the paper's §8.2 body)
  "LitQA2 was automatically evaluated using an evaluation LLM call
   (GPT-4-0613), which extracted the letter answer from PaperQA2's
   output."
  → match the extracted letter answer against the ideal answer; when "Insufficient information"
    is chosen, handle separately (scored as Correct for null answers)
```

### Actual LitQA2 Question Format (excerpt from the paper's Figure 2A body)

> "LitQA2 questions are MCQ with the option to refuse via 'Insufficient information to answer this question'. Each question has a single correct option, multiple incorrect distractors, and metadata indicating the source DOI."

LitQA2 questions are designed so that the answer appears in only **a single place** in the paper, so the model must perform accurate retrieval + reasoning rather than simple keyword matching.

### Key Evaluation Results (directly quoted from the paper's body Table + Figure 2B)

| System | LitQA2 Precision | LitQA2 Accuracy |
|---|---|---|
| **PaperQA2** | **85.2% ± 1.1%** | **66.0% ± 1.2%** |
| Human expert (PhD/PhD students, 9 people) | 73.8% ± 9.6% | 67.7% ± 11.9% |
| Perplexity Pro (GPT-4o) | 69.7% | – |
| Elicit | – | – |
| GPT-4-Turbo (no RAG) | 43.6% | – |
| Claude-Opus (no RAG) | 23.6% | – |
| PaperQA (old version) | 76.5% | 36.7% |

**Key findings (quoted from the paper's body)**
- PaperQA2 precision **exceeds human experts**: t(8.6)=3.49, p=0.0036 (statistically significant)
- "PaperQA2 outperforms other RAG systems on the LitQA2 benchmark in both precision and accuracy"
- No difference between Stage 1 (147) vs Stage 2 (101) results → no overfitting

### Significance of LitQA2

LitQA2 is a closed-form benchmark, yet it is designed to evaluate the **entire pipeline** of a RAG system (search → main-body extraction → reasoning → answering) at once:
- The answer is not in the abstract → retrieval must cover the entire main body
- The answer comes after the training-data cut-off → cannot be answered from parametric memory
- The "Insufficient information" option → also evaluates the prudence of admitting ignorance

---
## Experiments and Evaluation
### Evaluation Tasks and Datasets
| Task | Benchmark | Scale | Comparison target |
|---|---|---|---|
| Literature QA | LitQA2 (self-built) | 248 questions (MCQ) | 9 human experts |
| Scientific summarization | WikiCrow vs Wikipedia | 240 gene articles, 375 sentences evaluated | human-written Wikipedia |
| Contradiction detection | ContraDetect (self-built) | 93 biology papers, 3,180 claims | verified by 5 experts |

### Key Results
| System | Precision |
|---|---|
| **PaperQA2** | **85.2%** |
| Human experts | 73.8% |
| Perplexity Pro | 69.7% |
| GPT-4-Turbo (direct) | 43.6% |
| Claude-Opus (direct) | 23.6% |

| System | Precision (cited/supported fraction) |
|---|---|
| **WikiCrow** | **86.1%** |
| Wikipedia | 71.2% |

| Metric | Value |
|---|---|
| Average number of claims per paper | 35.16 ± 21.72 |
| Number of contradictions detected per paper | 2.34 ± 1.99 |
| Number of expert-verified contradictions | 1.64/paper (lower bound) |
| ContraDetect AUC | 0.842 |
| ContraDetect Precision | 88% |

---
## Key Contributions
- **First achievement of superhuman performance**: LitQA2 precision significantly exceeds unrestricted human experts (p=0.0036)
- **RCS technique**: after top-k retrieval, use an LLM to summarize + score each chunk to remove noisy chunks → substantial precision improvement
- **Citation Traversal tool**: leverages the citation graph via hierarchical indexing → significant recall improvement
- **WikiCrow**: automatically generates gene articles more accurate than human-written Wikipedia (reasoning errors 12 vs 26)
- **ContraCrow**: automatically detects an average of 1.64 verifiable contradictions per paper in biology literature
- **Rigorous human-comparison methodology**: comparison under identical conditions with PhD experts given full access to the internet and tools

---
## Limitations
- **Omission of closed-access papers**: due to licensing constraints, only open-access papers can be used → possibility of missing important results
- **ContraCrow overconfidence**: human-human agreement 75.5% vs ContraCrow-human agreement 60.4% → tendency toward excessive confidence
- **Cost**: $1~3 per query, $4.48 per WikiCrow article → cost burden at large-scale deployment
- **Degraded performance with small models**: using Llama3-70B or GPT-3.5-Turbo for RCS actually reduces accuracy → dependence on high-performance LLMs
- **Limits of abstract reasoning**: the LLM's own reasoning errors (hallucination) still exist (12 WikiCrow reasoning issues)

---
## Related Work and Related Links
- **Original paper**: [https://arxiv.org/abs/2409.13740](https://arxiv.org/abs/2409.13740)
- **GitHub**: [https://github.com/Future-House/paper-qa](https://github.com/Future-House/paper-qa) (paperqa open source)
- **WikiCrow generated articles**: [https://storage.googleapis.com/fh-public/wikicrow2/](https://storage.googleapis.com/fh-public/wikicrow2/)
- **Prior work**: PaperQA (arXiv 2312.07559), Lab-bench (arXiv 2407.10362)
- **Benchmarks built by this paper**: LitQA2 (248 MCQ), ContraDetect
