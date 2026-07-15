---
notion_id: 355f2dcd-4912-81dc-9b5b-ea1a837f8fd1
title: "SCIFACT-OPEN: Towards open-domain scientific claim verification"
bib_key: DBLP:conf/emnlp/WaddenLKCBWH22
year: 2022
domain: medical, bio
type: benchmark
venue: EMNLP (Findings)
paper_link: https://arxiv.org/abs/2210.13777
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# SCIFACT-OPEN: Towards open-domain scientific claim verification

> arXiv | 2022 | benchmark | medical, bio
## 📌 TL;DR
A large-scale open-domain test collection for evaluating scientific claim verification systems against a corpus of 500K research abstracts.
## 🎯 Background
**Limitations of existing benchmarks**
- Existing scientific claim verification systems have only been evaluated on small, artificial document sets (around 5K in scale) or in single-document settings, making it impossible to verify their scalability in real open-domain environments.
- When using a large-scale corpus, exhaustive manual annotation of all evidence documents is physically impossible, so a new benchmark that can address this is needed.
## 🔨 How It Was Built (Construction Methodology)
[image]
- **Step 1 (Corpus source selection and sampling)**: Filter high-quality papers from the S2ORC dataset that include a medical or biology field and have at least one incoming and outgoing citation. From 6.5M candidates, randomly sample 500K to construct the open-domain corpus.
- **Step 2 (Pooling via prediction models)**: Adopt a pooling strategy inspired by the TREC competition approach. Retrieve k=50 abstracts per claim using BM25 and the VerT5erini neural reranker. Then compute rankings based on the confidence scores of four state-of-the-art systems: VerT5erini, ParagraphJoint, MultiVerS, and MultiVerS10.
- **Step 3 (Annotation pool creation)**: Collect the top 250 (d=250) claim-abstract pair (CAP) predictions from each model, and create the final annotation pool from their union.
- **Step 4 (Expert quality verification and labeling)**: Three expert annotators with degrees in biology review the documents included in the pool and finally assign SUPPORTS, REFUTES, and NEI (Not Enough Info) labels.
## 📥 Input
<table header-row="true">
<tr>
<td>Item</td>
<td>Content</td>
</tr>
<tr>
<td>Input query</td>
<td>Scientific claim sentence</td>
</tr>
<tr>
<td>Corpus</td>
<td>500K S2ORC abstracts</td>
</tr>
<tr>
<td>Domain</td>
<td>Medical and biology</td>
</tr>
<tr>
<td>Number of claims</td>
<td>279</td>
</tr>
<tr>
<td>Source</td>
<td>Extended from claims extracted from SCIFACT-ORIG</td>
</tr>
</table>
**Provided fields**
<table header-row="true">
<tr>
<td>Field name</td>
<td>Description</td>
</tr>
<tr>
<td>Claim</td>
<td>Scientific claim sentence to be verified</td>
</tr>
<tr>
<td>Corpus</td>
<td>The full set of 500K abstract documents that must be searched to verify the claim</td>
</tr>
</table>
## 📤 Output (Answer format)
<table header-row="true">
<tr>
<td>Item</td>
<td>Content</td>
</tr>
<tr>
<td>Output form</td>
<td>Evidence abstracts that support (SUPPORTS) or refute (REFUTES) the claim + label</td>
</tr>
<tr>
<td>Evaluation metrics</td>
<td>Precision, Recall, F1, Average Precision</td>
</tr>
</table>
**List of benchmarked models**
<table header-row="true">
<tr>
<td>Model name</td>
<td>Base</td>
<td>Description</td>
</tr>
<tr>
<td>VerT5erini</td>
<td>T5-3B</td>
<td>Fact-checking pipeline that extracts at the sentence level and then uses a T5 model</td>
</tr>
<tr>
<td>ParagraphJoint</td>
<td>RoBERTa</td>
<td>512-token composition, multi-task learning that encodes the entire paragraph jointly</td>
</tr>
<tr>
<td>MultiVerS</td>
<td>Longformer</td>
<td>Uses Longformer to capture long-document context</td>
</tr>
<tr>
<td>ARSJoint</td>
<td>RoBERTa</td>
<td>Jointly predicts Abstract, Rationale, and Stance</td>
</tr>
</table>
## 💡 Example Items
**Supports example**
- **Claim**: Cancer risk is lower in individuals with a history of alcohol consumption. (Cancer risk is lower in individuals with a history of alcohol consumption)
- **Supporting Evidence**: Alcohol consumption was associated with a decreased risk of thyroid cancer. (Alcohol consumption was associated with a decreased risk of thyroid cancer)
**Refutes example**
- **Claim**: (Above same claim)
- **Refuting Evidence**: We found that the risk of cancer rises with increasing levels of alcohol consumption. (We found that the risk of cancer rises with increasing levels of alcohol consumption)
## 📊 Key Evaluation Results
**SCIFACT-OPEN setting (F1 Score)**
<table header-row="true">
<tr>
<td>Model</td>
<td>F1</td>
<td>Average Precision</td>
</tr>
<tr>
<td>VerT5erini</td>
<td>36.4</td>
<td>27.5</td>
</tr>
<tr>
<td>ParagraphJoint</td>
<td>46.5</td>
<td>40.5</td>
</tr>
<tr>
<td>MultiVerS</td>
<td>**52.4**</td>
<td>**44.9**</td>
</tr>
<tr>
<td>MultiVerS 10</td>
<td>51.3</td>
<td>43.4</td>
</tr>
<tr>
<td>ARSJoint</td>
<td>41.4</td>
<td>-</td>
</tr>
</table>
- Models that showed excellent performance on SCIFACT-ORIG saw their **F1 scores drop by 15-30 points** when applied to the open-domain setting, demonstrating a severe lack of generalization ability on large-scale corpora.
## ⚠️ Limitations
- During the data collection process, the initial retrieval relied only on a single information retrieval system (BM25 + VerT5erini).
- Compared to the traditional TREC competition, only a small number (4) of systems were used in the pooling process, leaving uncertainty that undiscovered evidence documents may remain within the corpus.
## 🔗 Related links
- Paper: [https://arxiv.org/abs/2210.13777](https://arxiv.org/abs/2210.13777)
- GitHub: [https://github.com/dwadden/scifact-open](https://github.com/dwadden/scifact-open)
- Paper using this benchmark: the original paper proposing SCIFACT-OPEN (arXiv 2022)
