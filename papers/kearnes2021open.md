---
title: "The Open Reaction Database"
bib_key: "kearnes2021open"
year: 2021
domain: chem
type: dataset
venue: Journal of the American Chemical Society
paper_link: https://doi.org/10.1021/jacs.1c09820
---
# The Open Reaction Database

kearnes2021open | 2021 | Journal of the American Chemical Society | dataset | [chem] | [paper](https://doi.org/10.1021/jacs.1c09820)

**DB**: ORD (Open Reaction Database)
**DB size**: Centralized repository (the size at initial release is not reported in the paper; distributed via GitHub)
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ORD schema + GitHub-based centralized repository

> Journal of the American Chemical Society | 2021 | dataset | chem
#### 📌 TL;DR
ORD is an open-access schema and infrastructure for structuring and sharing organic reaction data from journal papers, patents, and electronic lab notebooks, supporting everything from bench reactions to automated high-throughput experimentation.

#### 🎯 Background
**Limitations of existing infrastructure**
- Chemical reaction data were stored in unstructured form across journals, patents, and electronic notebooks, posing a major barrier to downstream AI applications
- A standard, shareable, and reusable format for reaction data was lacking
**Why this system is needed**
- Consistent data representation raises the level of computer-aided synthesis planning, reaction prediction, and other predictive chemistry tasks
- Building a collaborative open-data ecosystem across industry (Relay Therapeutics, Merck, Pfizer, etc.) and academia

#### 🔨 Architecture
It defines a reaction data schema supporting everything from bench reactions to automated high-throughput experimentation and flow chemistry. The schema, supporting code, and web-based user interface are all released on GitHub. Jointly developed by industry and academia, including Relay Therapeutics, Merck, Pfizer, MIT, UCSF, and Caltech.

#### 📥 Access
| Method | Description |
|---|---|
| GitHub | Data, schema, and code fully open |
| Web interface | UI for exploring and contributing data |

#### 📤 Data formats
- ORD schema based on Protocol Buffer (protobuf)
- Reactant, reagent, and product structures (SMILES, InChI)
- Reaction conditions (temperature, solvent, catalyst, yield, etc.)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Size of included reactions | Not reported in the paper (based on the initial public repository) |

#### ⚠️ Limitations
- Being community-contribution based, the initial data size is small compared to the USPTO corpus
- The quality and consistency of contributed data depend on the contributors
- The learning curve for the Protobuf schema is a barrier for some users

## Related links
- **Paper**: [The Open Reaction Database](https://doi.org/10.1021/jacs.1c09820)
