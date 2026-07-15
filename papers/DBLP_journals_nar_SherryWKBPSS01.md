---
title: "dbSNP: the NCBI database of genetic variation"
bib_key: "DBLP:journals/nar/SherryWKBPSS01"
year: 2001
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/29.1.308
---
# dbSNP: the NCBI database of genetic variation

DBLP:journals/nar/SherryWKBPSS01 | 2001 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/29.1.308)

**DB**: dbSNP (NCBI Database of Single Nucleotide Polymorphisms)
**DB size**: A general catalog of genome variation — a public database for designing large-scale association studies, gene mapping, and evolutionary biology
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NCBI web/FTP (http://www.ncbi.nlm.nih.gov/SNP)

> Nucleic Acids Research | 2001 | dataset | bio
#### 📌 TL;DR
A general catalog of genome variation built by NCBI, integrated with GenBank, PubMed, LocusLink, and Human Genome Project data, supporting the large-scale sample design required for association studies, gene mapping, and evolutionary biology research.

#### 🎯 Background
**Limitations of existing infrastructure**
- A general catalog of genome variation was needed to support the large-scale sample design required for association studies, gene mapping, and evolutionary biology (first proposed in a 1999 Genome Research paper)
- SNP data discovered in individual labs was scattered, making integrated access difficult

**Why this system is needed**
- Integrates diverse types of genome variation such as single nucleotide polymorphisms (SNPs), small insertions/deletions, and microsatellites into a single catalog
- Provides context by integrating with NCBI's GenBank, PubMed, LocusLink, and Human Genome Project data
- Freely provided to the research community through a public web interface and anonymous FTP

#### 🔨 Architecture
dbSNP is operated by NCBI and collects and integrates diverse types of genome variation. Submitted data is linked to GenBank, PubMed (literature), LocusLink (gene location), and Human Genome Project data. The full content is accessible through a web interface (http://www.ncbi.nlm.nih.gov/SNP) and anonymous FTP (ftp://ncbi.nlm.nih.gov/snp/).

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | http://www.ncbi.nlm.nih.gov/SNP — free browser search |
| Anonymous FTP | ftp://ncbi.nlm.nih.gov/snp/ — full download in various formats |

#### 📤 Data formats
- SNP submission data (various formats)
- Cross-references with GenBank/PubMed/LocusLink/Human Genome Project
- Chromosome location information

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Founding institution | NCBI (National Center for Biotechnology Information), NLM, NIH |
| Integrated data | GenBank, PubMed, LocusLink, Human Genome Project |
| Access method | Public web + anonymous FTP (free) |

#### ⚠️ Limitations
- As the 2001 founding paper, the number of variants included was initially very small compared to the present
- As a submission-based database, submission quality is inconsistent, so duplicate or erroneous entries may exist
- Initially focused on SNPs, but expansion to other variant types was carried out

## Related links
- **Paper**: [dbSNP: the NCBI database of genetic variation](https://doi.org/10.1093/nar/29.1.308)
