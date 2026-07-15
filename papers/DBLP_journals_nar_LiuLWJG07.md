---
title: "BindingDB: a web-accessible database of experimentally determined protein-ligand binding affinities"
bib_key: "DBLP:journals/nar/LiuLWJG07"
year: 2007
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkl999
---
# BindingDB: a web-accessible database of experimentally determined protein-ligand binding affinities

DBLP:journals/nar/LiuLWJG07 | 2007 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkl999)

**DB**: BindingDB (initial version)
**DB size**: ~20,000 binding affinity measurements, 110 protein targets, ~11,000 small-molecule ligands
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: BindingDB web interface (bindingdb.org)

> Nucleic Acids Research | 2007 | dataset | chem
#### 📌 TL;DR
BindingDB is a public database collecting experimentally determined protein-ligand binding affinities, providing ~20,000 binding data points extracted from the literature and centered on drug-target proteins.

#### 🎯 Background
**Limitations of existing infrastructure**
- Experimental protein-ligand binding affinity data was scattered across the literature, making it difficult to leverage for computational chemistry and drug discovery
- There was no integrated resource combining PDB structural data with quantitative binding affinity data
**Why this system is needed**
- A dataset of experimental binding data is needed to validate virtual screening methods
- To support SAR analysis for drug-target proteins

#### 🔨 Architecture
Binding affinity data for drug-target or candidate drug-target proteins is extracted from the scientific literature. It is linked to structural data in the PDB and to the literature in PubMed. It supports structure, substructure, and similarity search; protein sequence search; and affinity-range and molecular-weight search. Virtual screening tools are also included.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | bindingdb.org supports various search types |
| SDfile download | Download annotated SDF-format datasets |
| User compound DB | Virtual screening against uploaded compounds |

#### 📤 Data formats
- Annotated SDfile (compound structures + binding affinities)
- Protein sequence information
- PDB ID links
- PubMed ID links

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Binding affinity measurements | ~20,000 |
| Protein targets (including isoforms/variants) | 110 |
| Small-molecule ligands | ~11,000 |

#### ⚠️ Limitations
- As an initial version, data coverage is limited (drug-target focused)
- Manual extraction limits the pace of adding data

## Related links
- **Paper**: [BindingDB: a web-accessible database of experimentally determined protein-ligand binding affinities](https://doi.org/10.1093/nar/gkl999)
