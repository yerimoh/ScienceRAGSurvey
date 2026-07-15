---
title: "MIMIC-IV, a freely accessible electronic health record dataset"
bib_key: "johnson2023mimic"
year: 2023
domain: medical
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/s41597-022-01899-x
---
# MIMIC-IV, a freely accessible electronic health record dataset

johnson2023mimic | 2023 | Scientific Data | dataset | [medical] | [paper](https://doi.org/10.1038/s41597-022-01899-x)

**DB**: MIMIC-IV (Medical Information Mart for Intensive Care IV)
**DB size**: 431,231 hospital admissions; 180,733 unique patients; 73,181 ICU stays; period 2008–2019
**DB Open/Private**: Open (credentialed access via PhysioNet)
**Modality**: Text, Structured Table (EHR)
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PhysioNet / MIMIC-IV portal

> Scientific Data | 2023 | dataset | medical

#### 📌 TL;DR
A public EHR database built from electronic health records at Beth Israel Deaconess Medical Center covering 2008–2019, containing patient measurements, prescriptions, diagnoses, procedures, treatments, and de-identified clinical notes.

#### 🎯 Background
**Limitations of existing infrastructure**
- MIMIC-III uses 2001–2012 data and is outdated; it cannot reflect modern clinical practice
- Existing public datasets are limited to a single modality (clinical observations)
- High barriers to researcher access slow down clinical research

**Why this system is needed**
- A need for up-to-date EHR data reflecting the modern digital healthcare environment (2008–2019)
- Integration of new, precise digital information sources such as electronic medication administration records
- A need for an open platform for broad research and educational use

#### 🔨 Architecture
Provides BIDMC's 2008–2019 EHR data in a modular structure. Includes 431,231 hospital admissions (180,733 unique patients) and 73,181 ICU stays (50,920 unique patients). Provides patient measurements, orders, diagnoses, procedures, treatments, and de-identified free-text clinical notes. A schema structure separated into a hospital module and an ICU module.

#### 📥 Access
| Method | Description |
|---|---|
| PhysioNet portal | https://physionet.org/content/mimiciv/ — free download after credentialing |
| DOI | https://doi.org/10.1038/s41597-022-01899-x |

#### 📤 Data formats
- Structured tables (CSV): vital signs, lab results, medications, procedure codes
- Unstructured text: de-identified clinical notes (discharge summaries, radiology reports)
- ICD-10 diagnosis/procedure codes (an upgrade relative to MIMIC-III)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Hospital admissions | **431,231** |
| Unique patients (hospital) | **180,733** |
| ICU stays | **73,181** |
| Unique patients (ICU) | **50,920** |
| Data period | **2008–2019** |
| Mean age (hospital) | **58.8 years (SD 19.2)** |
| Mean age (ICU) | **64.7 years (SD 16.9)** |
| Proportion female (hospital) | **52.2%** |

#### ⚠️ Limitations
- Single-institution (BIDMC) data limits generalizability
- Access requires a credentialing process
- De-identification of clinical notes causes some information loss

## Related links
- **Paper**: [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x)
