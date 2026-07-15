---
title: "bioRxiv: the preprint server for biology"
bib_key: "sever2019biorxiv"
year: 2019
domain: bio
type: dataset
venue: bioRxiv (Cold Spring Harbor Laboratory)
paper_link: https://doi.org/10.1101/833400
---
# bioRxiv: the preprint server for biology

sever2019biorxiv | 2019 | bioRxiv (Cold Spring Harbor Laboratory) | dataset | [bio] | [paper](https://doi.org/10.1101/833400)

**DB**: bioRxiv preprint server
**DB size**: 310,000+ manuscripts (at time of paper writing)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: bioRxiv OAI-PMH / REST API

> bioRxiv (Cold Spring Harbor Laboratory) | 2019 | dataset | bio
#### 📌 TL;DR
A preprint server for the life sciences launched by Cold Spring Harbor Laboratory in 2013. It hosts more than 310,000 manuscripts as of the time of writing and accelerates scientific communication by making research immediately public before peer review.

#### 🎯 Background
**Limitations of existing infrastructure**
- The traditional scholarly publishing process delays the sharing of research findings due to peer-review periods lasting months to years
- Researchers had no venue for obtaining broad feedback at the draft stage
- Growing need for early disclosure to demonstrate research-funding productivity

**Why this system is needed**
- Immediate publication independent of journal submission and review, collecting feedback from a broad readership
- Ability to establish research priority ahead of formal publication
- Minimizes author burden through integration with journal policies (Easy Journal Transfer)

#### 🔨 Architecture
A non-profit open preprint repository operated by Cold Spring Harbor Laboratory (CSHL). Once an author submits, the full text is made public through the OAI-PMH interface after screening (for non-scientific content, plagiarism, etc.). It covers all fields of biology (evolutionary biology, genomics, computational biology, neuroscience, cell and developmental biology, etc.). Cold Spring Harbor Laboratory operates it together with the sister server medRxiv (clinical medicine). The Subject Category for each field is designated directly by the author.

#### 📥 Access
| Method | Description |
|---|---|
| OAI-PMH API | Supports batch harvesting of metadata and full text |
| Individual DOI | Each preprint is assigned a DOI in the 10.1101/XXXXXX format |
| RSS/Atom feed | Subscription to new preprints by field is available |
| Full-text PDF/HTML | Directly downloadable (open access) |

#### 📤 Data formats
- Full paper text (PDF and HTML)
- Structured metadata: title, authors, abstract, date, DOI, subject category
- Version history: multiple versions of the same preprint can be tracked
- Journal linkage: information on the final publishing journal (where available)

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| Total preprints hosted | **310,000+** (as of November 2019) |
| Monthly page views | **~10,000,000** |
| Service launch | **2013** |
| Operating institution | Cold Spring Harbor Laboratory (non-profit) |
| Early submission rate (before journal submission) | **30%** |
| Submission rate at time of journal submission | **55%** |

#### ⚠️ Limitations
- **No peer review**: Hosted papers have not undergone formal peer review, so there is no guarantee of scientific reliability
- **Quality variance**: Screening is at a basic level (filtering non-scientific content) and does not verify methodology or results
- **Multiple versions**: The same study exists in several versions, so tracking the latest version is necessary
- **Life-sciences only**: Other fields such as physics, chemistry, and earth science require separate servers (arXiv, ChemRxiv, EarthArXiv)

## Related links
- **Paper**: [https://doi.org/10.1101/833400](https://doi.org/10.1101/833400)
