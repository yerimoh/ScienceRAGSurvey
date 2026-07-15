---
title: "PubChem 2023 update"
bib_key: "kim2023pubchem"
year: 2023
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkac956
---
# PubChem 2023 update

kim2023pubchem | 2023 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkac956)

**DB**: PubChem (2022 update)
**DB size**: 120+ new data sources added (total record count not reported in the paper)
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PUG-REST, PUG-View API

> Nucleic Acids Research | 2023 | dataset | chem
#### 📌 TL;DR
A paper describing PubChem's 2022 update, explaining major expansions such as Google Patents integration, the addition of Cell Line and Taxonomy collections, and improvements to the bioassay data model.

#### 🎯 Background
**Limitations of the existing infrastructure**
- Integration between patent chemical data and PubChem was incomplete
- Access to chemical information by cell line and taxon was not systematically organized
**Why this system is needed**
- Integrating patent data (Google Patents) to greatly expand chemical space coverage
- Growing demand for a data standardization API feature (standardize) for AI model training

#### 🔨 Architecture
Integrates new data from 120+ data sources. Google Patents integration greatly expands the patent data collection. New Cell Line and Taxonomy data collections. Updated bioassay data model. Added target-centric download (by protein, gene, pathway, cell line, and taxon) to PUG-REST and PUG-View. Includes a large-scale update to PubChemRDF.

#### 📥 Access
| Method | Description |
|---|---|
| PUG-REST | Newly supports a chemical structure standardization option ('standardize') |
| PUG-View | Target-centric data download |
| Cell Line Collection | Fast access to chemical information for a specific cell line |
| Taxonomy Collection | Access to chemical information for a specific taxon |

#### 📤 Data formats
- SMILES, InChI, SDF
- JSON, XML
- RDF (PubChemRDF)

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| New data sources | 120+ (added over 2 years) |
| Included bioassay model | Updated (specific figures not reported in the paper) |

#### ⚠️ Limitations
- The paper is described mainly around update features and does not provide overall scale statistics such as total record count
- Data duplication and quality management challenges exist due to Google Patents integration

## Related links
- **Paper**: [PubChem 2023 update](https://doi.org/10.1093/nar/gkac956)
