---
title: "MIMIC-III, a freely accessible critical care database"
bib_key: "johnson2016mimic"
year: 2016
domain: medical
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/sdata.2016.35
---
# MIMIC-III, a freely accessible critical care database

johnson2016mimic | 2016 | Scientific Data | dataset | [medical] | [paper](https://doi.org/10.1038/sdata.2016.35)

**DB**: MIMIC-III (Medical Information Mart for Intensive Care III)
**DB size**: 53,423 distinct hospital admissions (adults, 2001–2012); 38,597 distinct adult patients; 7,870 neonates (2001–2008); 49,785 hospital admissions
**DB Open/Private**: Open (credentialed access via PhysioNet)
**Modality**: Text, Structured Table (EHR)
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PhysioNet / MIMIC-III portal

> Scientific Data | 2016 | dataset | medical

#### 📌 TL;DR
A large-scale single-institution clinical database containing intensive care unit admission data from Beth Israel Deaconess Medical Center, providing freely accessible vital signs, medications, laboratory results, imaging reports, clinical notes, and more.

#### 🎯 Background
**Limitations of existing infrastructure**
- Absence of a public ICU database usable for clinical research
- Existing data is locked in hospital internal archives, inaccessible for research
- Fragmentary datasets are small in scale and limited to specific research purposes

**Why this system is needed**
- A general-purpose platform is needed for academic and industry research, quality improvement, and medical education
- Data is needed to analyze the clinical course and treatment response of ICU patients over the long term
- Standardized open data is needed for reproducible clinical research

#### 🔨 Architecture
A single-institution EHR database integrating 2001–2012 data from the Beth Israel Deaconess Medical Center ICU. It includes 53,423 ICU admissions of adult patients and 7,870 neonates, and records data on 38,597 distinct adult patients. It contains vital signs, medications, laboratory measurements, care provider chart records, fluid balance, procedure codes, diagnosis codes, imaging reports, length of stay, survival data, and more. The median ICU length of stay is 2.1 days. Free access is available through PhysioNet after credentialing.

#### 📥 Access
| Method | Description |
|---|---|
| PhysioNet portal | https://physionet.org/content/mimiciii/ — free download after credentialing |
| DOI | https://doi.org/10.13026/C2XW26 |

#### 📤 Data formats
- Structured tables (CSV): vital signs, laboratory results, medications, billing codes
- Unstructured text: clinical notes, imaging reports, discharge summaries
- ICD-9 diagnosis/procedure codes

#### 📊 Key statistics (per paper)
| Item | Value |
|---|---|
| Adult ICU admissions | **53,423** |
| Distinct adult patients | **38,597** |
| Hospital admissions | **49,785** |
| Neonatal admissions | **7,870** |
| Data period (adults) | **2001–2012** |
| Median adult patient age | **65.8 years** |
| Male proportion | **55.9%** |
| In-hospital mortality | **11.5%** |
| Median ICU length of stay | **2.1 days** |

#### ⚠️ Limitations
- Single-institution (BIDMC) data limits generalizability
- Access requires a credentialing process (not fully open)
- Based on ICD-9 codes, which are inconsistent with the latest coding systems

## Related links
- **Paper**: [MIMIC-III, a freely accessible critical care database](https://doi.org/10.1038/sdata.2016.35)
