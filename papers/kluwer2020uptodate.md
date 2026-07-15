---
title: "UpToDate: evidence-based clinical decision support"
bib_key: "kluwer2020uptodate"
year: 2020
domain: medical
type: dataset
venue: Wolters Kluwer
paper_link: https://www.wolterskluwer.com/en/solutions/uptodate
---
# UpToDate: evidence-based clinical decision support

kluwer2020uptodate | 2020 | Wolters Kluwer | dataset | [medical] | [paper](https://www.wolterskluwer.com/en/solutions/uptodate)

**DB**: UpToDate (Wolters Kluwer clinical decision support system)
**DB size**: 11,000+ clinical topics; 7,000+ physician/expert authors and editors
**DB Open/Private**: Subscription (paid subscription)
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: UpToDate subscription web access / hospital and institutional licensing

> Wolters Kluwer | 2020 | dataset | medical
#### 📌 TL;DR
A subscription-based clinical decision support system operated by Wolters Kluwer that provides 11,000+ clinical topics and evidence-based recommendations authored and reviewed by 7,000+ expert authors and editors, and is used at the point of care by physicians in 180+ countries worldwide.

#### 🎯 Background
**Limitations of existing infrastructure**
- Clinicians lacked a single integrated reference resource for rapidly looking up diagnostic and treatment protocols for a specific disease during patient care
- Primary literature databases such as PubMed required clinicians to synthesize the evidence themselves, which was excessively time-consuming
- Textbooks had long update cycles, making it difficult to reflect the latest clinical guidelines

**Why this system is needed**
- 'Point of care' decision-making requires expert-synthesized, evidence-based recommendations rather than individual pieces of literature
- The explosive growth of medical knowledge makes it difficult for individual clinicians to keep track of the latest evidence across all fields

#### 🔨 Architecture
UpToDate is composed of topic-based clinical topic articles.
- **Topic articles**: Narrative-style evidence syntheses organized by disease into 'background', 'epidemiology', 'diagnosis', 'treatment', and 'follow-up' sections
- **Recommendations**: GRADE-system-based recommendation strength (strong/weak) + evidence grade (A/B/C) within each topic
- **Grading system**: Uses UpToDate's own evidence-level grading
- **Update cycle**: Continuous updates (at least one full annual review + immediate incorporation upon major findings)
- **References**: Tens to hundreds of primary literature citations per topic

#### 📥 Access
| Method | Description |
|---|---|
| Subscription web access | uptodate.com — institutional and individual subscriptions |
| EHR integration | UpToDate widget within major EHRs such as Epic and Cerner |
| Mobile app | iOS/Android app — offline access for subscribers |
| AlmanacQA | A research QA benchmark that includes UpToDate excerpts under a licensing agreement (the only public case) |

#### 📤 Data formats
- Clinical topic articles (narrative-style text + tables and figures)
- Recommendation summaries and evidence-grade tables
- Drug information module (separate Lexicomp integration)
- Medical calculators (dose calculation, risk scores, etc.)

#### 📊 Key statistics (based on official materials)
| Item | Value |
|---|---|
| Number of clinical topics | **11,000+** |
| Number of authors and editors | **7,000+** physicians and experts |
| Number of subscribing countries | **180+** |
| Access type | Subscription |
| Operating organization | Wolters Kluwer Health |

#### ⚠️ Limitations
- **Paid subscription barrier**: A core limitation that no open Scientific RAG system can access — the representative example of "open scientific RAG cannot reach" in the paper
- Subscription fees are expensive, limiting access for healthcare institutions in low-income countries
- Public RAG benchmarks leveraging UpToDate data are virtually nonexistent apart from AlmanacQA
- The proprietary evidence-grading system is not fully compatible with the external GRADE system

## Related links
- **Official site**: [UpToDate (Wolters Kluwer)](https://www.wolterskluwer.com/en/solutions/uptodate)
