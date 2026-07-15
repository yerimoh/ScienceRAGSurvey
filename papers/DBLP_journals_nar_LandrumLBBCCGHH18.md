---
title: "ClinVar: improving access to variant interpretations and supporting evidence"
bib_key: "DBLP:journals/nar/LandrumLBBCCGHH18"
year: 2018
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkx1153
---
# ClinVar: improving access to variant interpretations and supporting evidence

DBLP:journals/nar/LandrumLBBCCGHH18 | 2018 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gkx1153)

**DB**: ClinVar (NCBI clinical variant interpretation archive)
**DB size**: 331,000+ variants; 500,000+ submission records; 800+ participating organizations
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ClinVar website / NCBI E-utilities (Entrez) API / FTP

> Nucleic Acids Research | 2018 | dataset | medical
#### 📌 TL;DR
A public archive of clinical variant interpretations operated by NCBI that, as of 2018, freely provides more than 330,000 variants and more than 500,000 submission records contributed by over 800 organizations across 60 countries.

#### 🎯 Background
**Limitations of existing infrastructure**
- Clinical genomics laboratories each kept variant interpretations in their own internal systems, making sharing and reuse impossible
- Existing databases such as HGMD and LOVD provided some data behind paywalls or registration restrictions
- When organizations interpreted the same variant differently, there was no mechanism to identify and resolve the discrepancies

**Why this system is needed**
- A variant interpretation repository that discloses the sources of evidence is needed for the reproducibility and transparency of clinical genomics interpretation
- A public infrastructure role linking variant interpretations to other clinical data (EHR, patient phenotypes) was required

#### 🔨 Architecture
ClinVar receives submissions of variant-disease clinical interpretations and aggregates and publishes them.
- **VCV (Variation in ClinVar)**: the top-level identifier that aggregates all submission records at the variant level (new in 2018)
- **RCV (Reference ClinVar Assertion)**: an aggregate record at the variant-disease pair level
- **Submission**: the unit of interpretation submitted by an individual organization; includes clinical significance (pathogenic/benign, etc.) plus evidence
- **Evidence types**: literature, family history, functional experiments, public databases

#### 📥 Access
| Method | Description |
|---|---|
| ClinVar website | ncbi.nlm.nih.gov/clinvar — free search |
| NCBI E-utilities | Entrez API — programmatic queries |
| FTP download | full dumps in XML/VCF formats; ftp.ncbi.nlm.nih.gov/pub/clinvar/ |

#### 📤 Data formats
- VCV XML (variant-level aggregate records)
- VCF files (using Variation ID instead of dbSNP rs numbers, improved in 2018)
- clinical significance labels + ACMG classification criteria
- HPO phenotype term links

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total variants | **331,000+** |
| Submission records | **500,000+** |
| Participating organizations | **800+** (60 countries) |
| Direct clinical testing laboratories | **76** |
| Large structural variants (>1kb) | **15,000+** |
| Somatic variants | approximately **3,000** |
| Daily web visitors | approximately **4,700** |

#### ⚠️ Limitations
- Interpretation discrepancies across organizations: conflicting pathogenic/benign interpretations exist for the same variant
- Submission quality variance: evidence levels and classification criteria differ across submitting organizations
- Inclusion of somatic variants is at an early stage (~3,000 as of 2018, negligible compared to germline variants)
- When used for RAG, the granularity of the clinical significance text labels may not match the query intent

## Related links
- **Paper**: [Landrum et al., Nucleic Acids Research 2018](https://doi.org/10.1093/nar/gkx1153)
