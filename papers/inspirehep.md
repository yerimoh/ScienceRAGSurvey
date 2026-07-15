---
title: "INSPIRE-HEP: The information system for high-energy physics"
bib_key: "inspirehep"
year: 2012
domain: physics
type: dataset
venue: INSPIRE Collaboration (system reference)
paper_link: https://inspirehep.net
---
# INSPIRE-HEP: The information system for high-energy physics

inspirehep | 2012 | INSPIRE Collaboration (system reference) | dataset | [physics] | [paper](https://inspirehep.net)

**DB**: INSPIRE-HEP high-energy physics literature database
**DB size**: ~1,858,514 records (as of May 2025, queried via INSPIRE API `/api/literature`)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: INSPIRE REST API

> INSPIRE Collaboration (system reference) | 2012 | dataset | physics
#### 📌 TL;DR
A literature information system dedicated to the physics community, holding **more than ~1.85 million** high-energy physics (HEP) documents. Originating from SPIRES in 1974, it is jointly operated by CERN, DESY, Fermilab, IHEP, and IN2P3, and provides integrated author disambiguation and arXiv fulltext search. **Note that this is an institutional system reference entry (`@misc`), not a formal academic paper.**

#### 🎯 Background
**Limitations of existing infrastructure**
- SPIRES (Stanford Physics Information REtrieval System) began at SLAC/DESY in 1974 — the standard bibliographic system for the HEP community for decades, but lacking modern features
- Features such as author disambiguation, fulltext search, and personalized author pages were not supported by the legacy system

**Why this system is needed**
- INSPIRE was built by combining "SPIRES's trusted curated content" with "the Invenio digital library technology developed at CERN"
- Operating institutions: CERN (Switzerland), DESY (Germany), Fermilab (USA), IHEP (China), IN2P3 (France)
- Partner institutions: arXiv.org, NASA-ADS, PDG (Particle Data Group), HEPDATA, HEP publishers

#### 🔨 Architecture
Provides queries over six entity types through the INSPIRE REST API: Literature, Authors, Institutions, Experiments, Conferences, and Jobs. Automatic harvesting and immediate indexing of arXiv hep-* categories. Includes indexing of internal technical notes from LHC experiments (ATLAS, CMS, LHCb, etc.). Author disambiguation: generation of high-quality author profiles and automatic author identification. Fulltext search and snippet display over the body text and figure captions of recent arXiv papers.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | inspirehep.net — free browser-based search |
| REST API | Per-entity endpoints such as `/api/literature` — free, with rate limits |

#### 📤 Data formats
- Literature: arXiv preprints, journal articles, report metadata
- Authors: disambiguated researcher profiles, h-index
- Institutions: affiliated-institution records
- Experiments: high-energy physics experiment information
- Conferences: list of HEP-field conferences
- Jobs: list of HEP-field positions

#### 📊 Key statistics (literature basis)
| Item | Value |
|---|---|
| Literature records | **~1,858,514** (as of May 2025) |
| Access | Free (public API, with rate limits) |
| Updates | Real-time (automatic arXiv harvesting) |
| Predecessor system | SPIRES (started at SLAC/DESY in 1974) |

#### ⚠️ Limitations
- **HEP-specialized scope**: Centered on high-energy physics; some astrophysics and nuclear physics are included, but the full range of physics is not covered
- **Partner changes**: SLAC withdrew as a partner in 2021 — instability in the long-term operational structure
- **Source limitation**: An `@misc` system reference entry rather than a formal academic paper — no peer-reviewed literature on the system's design and methodology
- **Limited historical records**: Among legacy records from the SPIRES era, some have uneven metadata quality
- **Future plans (mentioned in official documents)**: Expansion of the API for third parties, addition of historical content, and expanded user error-correction features

## Related links
- **Paper**: [https://inspirehep.net](https://inspirehep.net)
