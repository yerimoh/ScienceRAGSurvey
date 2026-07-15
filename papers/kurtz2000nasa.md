---
title: "The NASA Astrophysics Data System: Overview"
bib_key: "kurtz2000nasa"
year: 2000
domain: astronomy, physics
type: dataset
venue: Astronomy and Astrophysics Supplement Series
paper_link: https://arxiv.org/abs/astro-ph/0002104
---
# The NASA Astrophysics Data System: Overview

kurtz2000nasa | 2000 | Astronomy and Astrophysics Supplement Series | dataset | [astronomy, physics] | [paper](https://arxiv.org/abs/astro-ph/0002104)

**DB**: NASA Astrophysics Data System (ADS)
**DB size**: ~1.5M bibliographic/abstract records (as of the 2000 paper, summed across 4 services)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NASA ADS (bibcode-based search system)

> Astronomy and Astrophysics Supplement Series | 2000 | dataset | astronomy, physics
#### 📌 TL;DR
The NASA astronomy literature information system (ADS), launched in 1993. As of 2000, it held **about 1.5 million** bibliographic/abstract records and was organized into 4 services: astronomy (~85%), instrumentation, physics, and astronomy preprints. A core astronomy K1 infrastructure that was the first to implement a bibcode-based identification scheme and real-time cross-search between external data archives such as SIMBAD and NED.

#### 🎯 Background
**Limitations of existing infrastructure**
- The conventional NASA STI (Scientific and Technical Information) database was designed around library reference librarians, making it unsuitable for direct use by researchers
- Journals, preprints, and observational data archives were dispersed, making integrated search impossible
- The need for a natural-language-search-based astronomy abstract service was first raised at the 1987 Garching conference

**Why this system was needed**
- The 1991 Washington, D.C. conference ("On-Line Literature in Astronomy") established the concept of a network-based integrated information system
- The WWW-based Abstract Service was released in February 1993, after which the number of users quadrupled within 5 weeks (400 → 1,600 per month)
- In the summer of 1993, the first transatlantic real-time database cross-query connection with SIMBAD was established

#### 🔨 Architecture
ADS consists of 4 services (Astronomy, Instrumentation, Physics, Astronomy Preprints). It uses bibcode (Uniform Bibliographic Code, Schmitz et al. 1995)-based unique identifiers to hyperlink ADS ↔ SIMBAD ↔ electronic journals. In 1994, the AAS purchased a subset of the ISI Science Citation Index to provide citation data. Of ~1.73M hyperlinks, ~31% link to data sources external to ADS (SIMBAD, NED, CDS-Vizier, HEASARC, etc.). Electronic journal partners: ApJL, ApJ, ApJS, A&A, A&AS, AJ, PASP, MNRAS, New Astronomy, Nature, Science (as of 2000).

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | Author/title/abstract field search, natural-language topic search (entropy matching) |
| SIMBAD/NED linkage | Combined object-name queries (logical OR/AND) |
| Similar-paper search | "Find Similar Abstracts": uses an existing paper's abstract as the query |
| Mirror sites | Distributed services worldwide |

#### 📤 Data formats
- Bibliographic records: title, authors, journal, bibcode
- Abstracts (nearly complete coverage of major journals since 1975)
- Bitmaps (scanned images of back issues of major astronomy journals)
- Citation/reference data (AAS-ISI contract, covering January 1982 to September 1998)
- ~1.73M hyperlinks (including external data sources of ADS)

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| Total bibliographic/abstract records | **~1.5M** (as of 2000, summed across 4 services) |
| Astronomy-only abstracts | **~500,000 records** |
| Monthly queries | **~580,000** (as of March 1999) |
| Monthly users | **~20,000+** (as of March 1999) |
| Monthly abstract views | **~400,000** |
| Full-text article retrievals | **~110,000** / month |
| Hyperlinks | **~1.73M** |
| Annual queries | **~5M** |
| Query growth rate | doubling every 17 months (1996–1999) |
| Estimated ADS impact | equivalent to saving 333 FTE research staff per year |

#### ⚠️ Limitations
- **Incomplete citation data**: under the AAS-ISI contract, only citations among papers within ADS are included; citations to literature outside astronomy are missing
- **No keyword search (at the time)**: keyword queries were removed due to incompatibility between the old STI keyword scheme and journal keyword schemes (conversion work in progress)
- **Historical literature digitization incomplete**: literature before 1975 is not fully covered (AJ was the first case fully covered back to 1849, in January 1999)
- **Instrumentation/Physics services**: functionally less mature than the astronomy service
- **Future work (mentioned in the paper)**: expanding scans of old observatory reports and discontinued journals (in collaboration with the Harvard Preservation Project), integrating keyword schemes, expanding non-English-language abstracts

## Related links
- **Paper**: [https://arxiv.org/abs/astro-ph/0002104](https://arxiv.org/abs/astro-ph/0002104)
