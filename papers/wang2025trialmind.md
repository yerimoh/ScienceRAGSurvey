---
title: "Accelerating clinical evidence synthesis with large language models"
bib_key: "wang2025trialmind"
year: 2025
domain: medical
type: Method
venue: npj Digital Medicine
paper_link: https://doi.org/10.1038/s41746-025-01840-7
---
# TrialMind: LLM Pipeline for Clinical Evidence Synthesis
> npj Digital Medicine 2025 | Method | medical

## TL;DR
TrialMind is a human-in-the-loop pipeline that uses an LLM to carry out the core stages of clinical evidence synthesis, namely literature search, screening, data extraction, and evidence synthesis. It is designed so that users can review and revise the intermediate outputs of each stage, thereby accelerating the systematic review workflow.

## Architecture (TrialMind Architecture)
The main backbone is GPT-4 (gpt-4-0125-preview). It decomposes evidence synthesis into four modules.
1. **Literature search:** Takes PICO elements as input, generates a Boolean query, and then searches PubMed.
2. **Literature screening:** Assesses and ranks the relevance of candidate studies according to eligibility criteria.
3. **Data extraction:** Extracts study characteristics and clinical outcome measures (linking to source-text locations).
4. **Evidence synthesis:** Standardizes the extracted results and integrates them into a meta-analysis and forest plot.

Throughout the pipeline, it combines In-Context Learning, RAG (augmenting the prompt with retrieved abstracts), and Chain-of-Thought. **Human-in-the-loop:** Users can edit eligibility criteria, verify the source-text locations of extracted data, and adjust the aggregation strategy, which blocks error propagation between stages.

## Pipeline (inference)
1. **Search:** PICO → generate a Boolean query via ICL, augment terms with RAG+CoT (identify → filter → expand) → submit to PubMed.
2. **Screening:** Generate eligibility criteria (editable) → evaluate candidates in parallel with −1/0/+1 per criterion and sum to rank them (targeting the top 2,000, with accompanying rationale).
3. **Extraction:** For general fields, extract value + location from the full document. For results: (i) identification (CoT) → (ii) numerical extraction → (iii) the LLM generates and runs Python code to produce standardized effect measures.
4. **Synthesis:** Aggregate the standardized numbers with the R 'meta' package to generate forest plots and pooled estimates.

## Key results
| Stage/metric | TrialMind | Comparison |
|---|---|---|
| Search Recall (average) | 0.782 | GPT-4 0.073 / Human 0.187 |
| Target capture within screening top 100 | >80% | — |
| Result extraction accuracy (Immunotherapy) | 0.70 | GPT-4 0.54 |
| Result extraction accuracy (Hyperthermia) | 0.84 | GPT-4 0.52 |
| Result extraction vs. best baseline | 1.50× median | — |

Human evaluation of evidence synthesis (win rate, 5 studies): 87.5/100/62.5/62.5/81.2%. User study: screening recall +71.4% and time −44.2%, extraction accuracy +23.5% and time −63.4%.

## Limitations
- Result extraction is the weakest link (inaccuracy/extraction failure/hallucination). Hallucination arises from confusion over definitions such as 'overall response' versus 'complete response'.
- The forest plots for standardization/synthesis are performed by human experts in R (assuming manual verification).
- Evaluation is limited to 4 cancer treatment domains.

## Related links
- arXiv: 2406.17755 · DOI: 10.1038/s41746-025-01840-7 (npj Digital Medicine 2025)
- Authors: Zifeng Wang, Lang Cao, Benjamin Danek, Qiao Jin, Zhiyong Lu, et al.
- Dataset TrialReviewBench: 100 systematic reviews across 4 cancer treatment domains + annotations for 2,220 clinical studies
