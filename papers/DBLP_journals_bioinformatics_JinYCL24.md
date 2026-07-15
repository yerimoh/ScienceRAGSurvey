---
title: "GeneGPT: augmenting large language models with domain tools for improved access to biomedical information"
bib_key: "DBLP:journals/bioinformatics/JinYCL24"
year: 2024
domain: bio, medical
type: Method
venue: Bioinformatics
paper_link: https://arxiv.org/abs/2304.09667
---
# GeneGPT: LLMs Calling NCBI Web APIs for Genomics QA
> Bioinformatics 2024 | Method | bio · medical

## TL;DR
GeneGPT teaches Codex (code-davinci-002) how to use the NCBI Web APIs (E-utils + BLAST) via in-context learning, and performs genomics QA by detecting and executing API calls during decoding and re-inserting their raw results into the generated text (augmented decoding). It achieves an average of 0.83 across the 9 GeneTuring tasks, substantially outperforming the previous best, New Bing (0.44).

## Architecture (GeneGPT Architecture)
- **NCBI Web APIs:** ① E-utils (`esearch`/`efetch`/`esummary`) — looks up identifiers and summaries from the `gene`/`snp`/`omim` DBs. ② BLAST URL API (`CMD=Put`→`Get`, `blastn`, `nt` DB) — sequence alignment.
- **In-context prompt (4 parts):** instruction + documentation (API syntax) + demonstration (4 examples solved with the NCBI APIs; URLs/results wrapped in `[ ]` and `->` used as the call indicator) + test question. (all used = full, only Dm.1+Dm.4 = slim)
- **Augmented decoding:** when a `->` token is encountered during generation, the last URL is extracted, the NCBI API is called, and the raw result is inserted into the text before generation resumes. On `\n\n` it terminates and extracts the text after "Answer:" as the answer.

## Pipeline (inference)
1. Build the prompt (instruction+doc+demo+question) and generate with Codex (temperature 0).
2. Detect `->` → extract URL → call E-utils/BLAST → insert result → resume.
3. Chain multiple APIs for a single question (esearch→efetch; BLAST Put→Get). Multi-hop (GeneHop) decomposes into subquestions with CoT.
4. `\n\n` → terminate → extract answer.

## Key results
GeneTuring (9 of the 12 tasks that are NCBI-related, 50 questions each):

| Model | Overall avg |
|---|---|
| GPT-3 (davinci-003) | 0.16 |
| ChatGPT | 0.12 |
| New Bing | 0.44 |
| **GeneGPT-slim** | **0.83** |

- Large improvement over the previous SOTA New Bing (0.44). On Sequence alignment (BLAST) all other models scored ~0.00, while GeneGPT scored 0.66.
- GeneHop (multi-hop, new) average: GeneGPT 0.50 vs New Bing 0.24.
- Ablation: API demonstration is more useful than documentation for in-context learning, with strong cross-task generalization.

## Limitations
- Uses automatic exact-match evaluation (whereas the comparison group used the manual evaluation of the original benchmark), so the criteria are not identical.
- Some questions cannot be answered from the NCBI DBs alone (E4 error), and there are argument errors (E2) and result-extraction failures (E3).
- Depends on Codex (8k context · code understanding) and requires access to NCBI servers.

## Related links
- arXiv: 2304.09667 · Bioinformatics 2024 (Jin, Yang, Chen, Lu; NCBI/NLM)
- Tools: NCBI E-utils (gene/snp/omim) + BLAST (blastn, nt)
