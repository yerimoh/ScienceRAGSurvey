---
title: "BindingDB in 2015: a public database for medicinal chemistry, computational chemistry and systems pharmacology"
bib_key: "gilson2016bindingdb"
year: 2016
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkv1072
---
# BindingDB in 2015: a public database for medicinal chemistry, computational chemistry and systems pharmacology

gilson2016bindingdb | 2016 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkv1072)

**DB**: BindingDB (2015 update)
**DB size**: 1M+ data entries (mostly based on literature and US patents)
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: BindingDB web interface + advanced cross-search

> Nucleic Acids Research | 2016 | dataset | chem
#### 📌 TL;DR
The 2015 update of BindingDB, which integrates more than one million protein-small molecule interaction data entries and bioactivity data from US patents, and strengthens target prediction and virtual screening tools.

#### 🎯 Background
**Limitations of existing infrastructure**
- The data scale had expanded greatly since 2007, but patent data had not been integrated
- Tools for systems pharmacology analysis were lacking
**Why this system is needed**
- The possibility of extracting large amounts of new binding data from US patents
- Demand for tools to predict the potential protein targets of compounds (polypharmacology)

#### 🔨 Architecture
It extracts protein-small molecule binding data from scientific papers and US patents. It provides advanced search tools (cross-search by text, chemical structure, protein sequence, and numeric affinity). It links with PDB, PubMed, ZINC, and pathway information. It includes target prediction and virtual screening tools. It provides congeneric series datasets.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | www.bindingdb.org advanced cross-search |
| Download | SDF, TSV format datasets |
| Programmatic | Web service API |
| Congeneric datasets | Special sets for validating drug design methods |

#### 📤 Data formats
- Protein-ligand binding affinity (Ki, IC50, Kd, EC50)
- Compound structures (SMILES, SDF)
- Protein sequence information
- Patent and literature source information

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| Data entries | 1M+ |

#### ⚠️ Limitations
- Patent data extraction carries the possibility of errors due to the difficulty of processing unstructured text
- Target prediction tools may be affected by training data bias

## Related links
- **Paper**: [BindingDB in 2015](https://doi.org/10.1093/nar/gkv1072)
