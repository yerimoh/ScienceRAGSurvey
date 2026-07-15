---
title: "Online Mendelian Inheritance in Man (OMIM), a knowledgebase of human genes and genetic disorders"
bib_key: "hamosh2005online"
year: 2005
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gki033
---
# Online Mendelian Inheritance in Man (OMIM), a knowledgebase of human genes and genetic disorders

hamosh2005online | 2005 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gki033)

**DB**: OMIM (Online Mendelian Inheritance in Man)
**DB size**: 15,593 entries (as of September 2004); 9,816 genes, 5,777 phenotypes
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OMIM website / NCBI Entrez integrated search

> Nucleic Acids Research | 2005 | dataset | medical
#### 📌 TL;DR
An authoritative catalog of human genes and genetic disorders, maintained by the McKusick-Nathans Institute at Johns Hopkins University and distributed by NCBI, containing 15,593 entries and 12,715 allelic variants as of 2004.

#### 🎯 Background
**Limitations of existing infrastructure**
- It originates from Victor McKusick's 1966 print work "Mendelian Inheritance in Man (MIM)," but the print update cycle could not keep up with the rapidly growing volume of genetic discoveries
- Print and CD-ROM formats could not support daily literature updates or links to external DBs

**Why this system is needed**
- The genomic revolution meant new gene-disease associations were reported daily, making real-time online updates essential
- Clinicians and researchers needed to cross-search gene, phenotype, literature, and sequence DBs on a single platform

#### 🔨 Architecture
Each OMIM entry is identified by a unique six-digit MIM number and describes genes (star symbol), phenotypes, and gene-phenotype relationships.
- **MIM number scheme**: the leading digit distinguishes the entry type (1xxxx = autosomal dominant, 2xxxx = autosomal recessive, 3xxxx = X-linked, etc.)
- **Allelic Variant section**: clinically significant mutations listed within each entry (12,715 variants across 1,651 entries as of 2004)
- **Clinical Synopsis**: summary of clinical features by phenotype (more than 4,500)
- **Morbid Map**: alphabetically ordered list of gene-disease mappings

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | omim.org — free search; personal and non-profit use |
| NCBI Entrez | integrated search links across PubMed, Gene, and OMIM |
| FTP download | separate license required for commercial use |

#### 📤 Data formats
- Text entries by MIM number (gene descriptions, phenotypes, clinical synopses)
- Allelic variant lists (Allelic Variant section)
- Gene-phenotype mapping tables (Morbid Map)
- Cross-links to NCBI Gene, sequence DB, and PubMed

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total number of entries | **15,593** (as of September 2004) |
| Gene entries (molecular sequence confirmed) | **9,816** |
| Phenotype/disorder entries | **5,777** |
| Number of allelic variants | **12,715** (across 1,651 entries) |
| Number of clinical synopses | **more than 4,500** |
| Number of mapped disorders | **3,659** (distributed across 2,558 gene loci) |
| Disorders with confirmed molecular basis | **2,563** |
| Daily unique visitors | **about 8,500** |
| Daily number of queries | **about 100,000** |
| Monthly new entries/updates | about 70 new, about 600 updates |

#### ⚠️ Limitations
- Focused on Mendelian genetic disorders: coverage of complex (polygenic and environmental) disorders is limited
- Separate license negotiation required for commercial redistribution and use
- Text-centric narrative makes it difficult to use directly for structured queries (SPARQL, etc.)

## Related links
- **Paper**: [Hamosh et al., Nucleic Acids Research 2005](https://doi.org/10.1093/nar/gki033)
