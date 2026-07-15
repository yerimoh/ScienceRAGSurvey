---
title: "GeoRef: Comprehensive Geoscience Bibliography"
bib_key: "georef"
year: 2024
domain: earth
type: dataset
venue: American Geosciences Institute
paper_link: https://www.americangeosciences.org/information/georef
---
# GeoRef: Comprehensive Geoscience Bibliography

georef | 2024 | American Geosciences Institute | dataset | [earth] | [paper](https://www.americangeosciences.org/information/georef)

**DB**: GeoRef geoscience bibliographic database
**DB size**: 4.7M+ records (per the official AGI site; growing ~100,000 records per year)
**DB Open/Private**: Subscription
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: GeoRef (distributed via EBSCO subscription)

> American Geosciences Institute | 2024 | dataset | earth
#### 📌 TL;DR
The most comprehensive bibliographic database spanning all fields of geoscience. Established and operated by AGI (American Geosciences Institute) in 1966, it indexes **more than 4.7 million** records (about 100,000 added per year), covering 44 languages and more than 3,500 journals as well as reports, maps, and theses. Coverage reaches back to 1666 for North American geology and to 1933 for worldwide geology. **Note that this is an institutional database reference entry (`@misc`), not a formal scholarly paper.**

#### 🎯 Background
**Limitations of existing infrastructure**
- Geoscience literature is scattered across diverse types such as journals, theses, government reports, and geologic maps
- Absence of specialized infrastructure for unified search of multilingual (44 languages) geoscience materials

**Why this system is needed**
- Since AGI's founding in 1966, it has become the standard literature-information service for the geoscience community
- Trained geoscientist editors and indexers directly assign GeoRef Thesaurus controlled vocabulary
- Provides a long time series with coverage reaching back to 1666 for North American geology and 1933 for worldwide geology

#### 🔨 Architecture
Produced and maintained by AGI (American Geosciences Institute, located in Alexandria, Virginia) and distributed as institutional subscriptions through distributors such as EBSCO. AGI geoscientist editors provide expert curation by directly indexing and assigning GeoRef Thesaurus controlled vocabulary. Fields covered: geology in general, geophysics, hydrology, paleontology, petrology, mineralogy, economic geology, environmental and engineering geology, marine geology, and oceanography. Material types covered: journal articles, monographs, geologic maps, conference papers, reports, theses (United States and Canada), and USGS publications. Online ISSN: 2573-1874.

#### 📥 Access
| Method | Description |
|---|---|
| Institutional subscription | Subscription through distributors such as EBSCO — no free individual access |
| API | No public free API provided |

#### 📤 Data formats
- Bibliographic information: title, author, publication year, journal/material type
- Abstract (varies by paper)
- GeoRef Thesaurus controlled vocabulary (enables hierarchical subject browsing)
- Grey literature: theses (U.S. and Canadian graduate schools), geologic maps, government reports

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total records | **4.7M+** (per the official AGI site) |
| Annual growth | **~100,000 records** (6,000–9,000 per month) |
| Number of journals covered | **3,500+** (44 languages) |
| Retrospective coverage range (North America) | **1666–present** |
| Retrospective coverage range (worldwide) | **1933–present** |
| Update cycle | Monthly |
| Access method | Institutional subscription (e.g., EBSCO) |

#### ⚠️ Limitations
- **Subscription-only**: No free public API — an institutional subscription contract is required when building a RAG pipeline
- **No full text**: Provides bibliographic information (title, author, abstract, controlled terms); the original text itself requires a separate full-text link
- **Grey-literature bias**: Large inclusion of non-scholarly reports and maps introduces variation in literature quality
- **Gap in pre-1933 non-North American literature**: Worldwide geology coverage begins in 1933; 19th-century European and Asian geology literature may be missing
- **Update lag**: Monthly updates mean the latest arXiv preprints and similar cannot be included immediately

## Related links
- **Paper**: [https://www.americangeosciences.org/information/georef](https://www.americangeosciences.org/information/georef)
