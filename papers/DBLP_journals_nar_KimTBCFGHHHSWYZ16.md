---
title: "PubChem Substance and Compound databases"
bib_key: "DBLP:journals/nar/KimTBCFGHHHSWYZ16"
year: 2016
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkv951
---
# PubChem Substance and Compound databases

DBLP:journals/nar/KimTBCFGHHHSWYZ16 | 2016 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkv951)

**DB**: PubChem (Substance, Compound, BioAssay)
**DB size**: 157M+ substance descriptions, 60M unique structures, 1M+ bioassay descriptions (as of Sep 2015)
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PubChem REST API (PUG-REST, PUG-View)

> Nucleic Acids Research | 2016 | dataset | chem
#### 📌 TL;DR
A public chemical information repository operated by the US NIH that provides integrated compound, substance, and bioassay data including SMILES, InChI, and CAS identifiers.

#### 🎯 Background
**Limitations of existing infrastructure**
- Chemical substance information was scattered across multiple independent repositories, making integrated search difficult
- The connection between bioactivity data and chemical structure information was not systematically established
**Why this system is needed**
- As part of the NIH Molecular Libraries Roadmap Initiative, there was a need to secure public accessibility to chemical information
- Provides structure-based search, similarity search, and bioactivity lookup through a single interface

#### 🔨 Architecture
It consists of three interconnected databases (Substance, Compound, BioAssay). The Substance DB stores raw chemical information submitted by contributors, the Compound DB stores standardized unique structures, and the BioAssay DB stores experimental bioactivity data. A structure standardization pipeline automatically performs deduplication and SMILES/InChI conversion. Derived resources such as PubChem3D and PubChemRDF (RDF-format data) are also included.

#### 📥 Access
| Method | Description |
|---|---|
| PUG-REST API | RESTful API for searching and downloading by CID, SMILES, InChI, etc. |
| PUG-View | API for querying structured view data |
| FTP download | Provides full dumps in SDF, SMILES, XML, and ASN.1 formats |
| Web interface | pubchem.ncbi.nlm.nih.gov text/structure search |

#### 📤 Data formats
- SMILES (canonical and isomeric)
- InChI / InChIKey
- SDF (2D/3D structures)
- XML, ASN.1
- RDF (PubChemRDF)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Substance records | 157M+ (as of September 2015) |
| Unique compound structures | 60M |
| Bioassay descriptions | 1M+ |
| Protein targets | ~10,000 |
| Patent-compound links | 329M+ |

#### ⚠️ Limitations
- Wide variance in the quality of contributor-submitted data, with possible loss of some information during standardization
- API requests exceeding 3 per second are restricted due to concerns about server overload
- Large-scale requests (millions of records) require a batch-processing approach

## Related links
- **Paper**: [PubChem Substance and Compound databases](https://doi.org/10.1093/nar/gkv951)
