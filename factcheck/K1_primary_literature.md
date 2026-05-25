# Fact-Check Report: §K1 General-purpose & Domain-specific literature (v2)
**Survey**: TPAMI Scientific RAG Survey, ver/2  
**Date**: 2026-05-25  
**Checker**: Claude Code (claude-sonnet-4-6)  
**Basis**: Actual paper full text read via web (not abstract-only). Source .md files at `/site/papers/`.

---

## §General-purpose literature (main.tex line 362–366)

### Survey text
> General-purpose corpora cover disciplines broadly enough that a single retrieval pipeline can serve more than one domain at once. Crossref~\cite{DBLP:journals/qss/HendricksTLF20} is the registry layer on which much of the rest is built, providing a free REST API of scholarly records keyed by DOI with reference linkage and **basic metadata**. OpenAlex~\cite{DBLP:journals/corr/abs-2205-01833} aggregates Crossref, PubMed~\cite{canese2013pubmed}, and institutional and disciplinary repositories into a single open entity graph of works, authors, venues, institutions, and concepts, accessible through a fully-open REST API. Semantic Scholar's S2ORC~\cite{DBLP:conf/acl/LoWNKW20} provides a unified bulk dataset of academic papers across all disciplines with parsed full text, structured citation linkage, and a single identifier space that maps across PubMed~\cite{canese2013pubmed}, arXiv, and other sources.

---

### Crossref — DBLP:journals/qss/HendricksTLF20

| Claim in text | Paper says (Hendricks et al. 2020) | Status |
|---|---|---|
| "free REST API" | `api.crossref.org` — free, no sign-up. Also OAI-PMH. | ✅ |
| "keyed by DOI" | DOI is the primary key for all records. | ✅ |
| "reference linkage" | Citation links are a core deposited metadata field. | ✅ |
| "**basic** metadata" | Paper reports: abstract, full-text links, funder info, license, citation links, correction/retraction notices, 13 content types. "Basic" is an **understatement**. | ⚠️ minor |
| "registry layer on which much of the rest is built" | OpenAlex, S2, etc. all ingest Crossref. Paper describes Crossref as scholarly metadata infrastructure. | ✅ |
| Record count (not stated in survey) | **106M+** records (paper figure), growing 11%/year. | — |

**Verdict**: ✅ Correct. "Basic metadata" is slightly understated — Crossref provides rich metadata including funding, licenses, and citation links — but not factually wrong for a high-level description.

---

### OpenAlex — DBLP:journals/corr/abs-2205-01833

| Claim in text | Paper says (Priem, Piwowar, Orr 2022) | Status |
|---|---|---|
| "aggregates Crossref, PubMed, and institutional and disciplinary repositories" | Paper lists: Crossref, PubMed, ORCID, ROR, MAG, Unpaywall, OpenCitations. "Institutional and disciplinary repositories" is a partial description. | ✅ acceptable |
| "single open entity graph" | Paper: five entity types in a connected graph. | ✅ |
| "works, authors, venues, institutions, and concepts" | Exact five types listed in paper: Works (209M), Authors (2,013M), Venues (124K), Institutions (109K), Concepts (65K). | ✅ |
| "fully-open REST API" | Paper: "All these are free and require no registration or permission. The REST API has no rate-limits." | ✅ |

**Verdict**: ✅ Correct (DataCite and "dozens of repositories" were removed in a prior fix; current text is accurate).

---

### S2ORC — DBLP:conf/acl/LoWNKW20

| Claim in text | Paper says (Lo et al. 2020) | Status |
|---|---|---|
| "unified bulk dataset across all disciplines" | 81.1M English-language papers from hundreds of publishers/archives. | ✅ |
| "parsed full text" | GROBID-parsed full text for 8.1M open-access papers; LaTeX source for 1.5M. | ✅ |
| "structured citation linkage" | Inline citation mentions linked to paper objects via biblio-linking pipeline. | ✅ |
| "maps across PubMed, arXiv, and other sources" | S2ORC IDs include: DOI, PubMed, PMC, arXiv, ACL Anthology — all confirmed in Table 3. | ✅ |

**Verdict**: ✅ All claims correct.

---

## §Domain-specific literature (main.tex line 367–373)

### Survey text
> PubMed~\cite{canese2013pubmed} and Europe PMC~\cite{europepmc2024} cover biomedicine, with PubMed indexing biomedical abstracts under the controlled MeSH vocabulary through the NCBI E-utilities API and Europe PMC adding open full text and integrated preprints over a RESTful API … Astronomy is indexed by the NASA Astrophysics Data System (ADS)~\cite{kurtz2000nasa}, which spans astronomy, planetary science, and parts of physics, and integrates direct links from papers to observational data archives and astronomical object databases through a unified bibliographic code system. High-energy physics is served by INSPIRE-HEP~\cite{inspirehep}, jointly operated by **CERN, DESY, Fermilab, SLAC, and IN2P3**, with an author-disambiguated bibliography that has been the field's canonical literature system since the SPIRES era of the 1970s. Geoscience is indexed by GeoRef~\cite{georef}, maintained by the American Geosciences Institute, covering geology, geophysics, hydrology, and paleontology.

---

### PubMed — canese2013pubmed

| Claim in text | Source says (Canese & Weis, NCBI Handbook 2013) | Status |
|---|---|---|
| "indexing biomedical abstracts" | 22M+ total citations; MEDLINE core: 19M+ records. | ✅ |
| "controlled MeSH vocabulary" | MeSH = NLM-developed thesaurus with entry terms, subheadings, pharmacological actions, UMLS terms. Hierarchical search (MeSH explosion). | ✅ |
| "NCBI E-utilities API" | Entrez Programming Utilities (E-utils) = 8 server-side programs for programmatic access; free, stable interface. | ✅ |

**Verdict**: ✅ All claims correct.

---

### Europe PMC — europepmc2024

| Claim in text | Paper says (Rosonovski et al., NAR 2024, "Europe PMC in 2023") | Status |
|---|---|---|
| "open full text" | 42M+ abstracts; 9M+ full-text articles (open access). | ✅ |
| "integrated preprints" | 650K+ preprints from 31 preprint servers (bioRxiv 206K, Research Square 253K, medRxiv 45K, etc.). | ✅ |
| "over a RESTful API" | Articles RESTful API + Annotations API (DocMaps, Sciety integration). | ✅ |
| bib title "Europe PMC in 2024" | Actual title: **"Europe PMC in 2023"** — published NAR 2024. bib title is wrong by one year. | ⚠️ bib error (READ-ONLY) |

**Verdict**: ✅ Text claims all correct. Bib entry title error is a pre-existing issue in references.bib (read-only).

---

### NASA ADS — kurtz2000nasa

| Claim in text | Paper says (Kurtz et al., A&AS 2000) | Status |
|---|---|---|
| "spans astronomy, planetary science, and parts of physics" | 4 services: Astronomy (~85% of usage), Instrumentation, Physics, Preprints. Confirmed. | ✅ |
| "direct links from papers to observational data archives" | Links to HEASARC (high-energy), NED (extragalactic), CDS-Vizier (journal data tables), electronic journal pages. | ✅ |
| "astronomical object databases" | SIMBAD (CDS, Strasbourg) and NED (NASA/IPAC) linked directly from paper records. | ✅ |
| "unified bibliographic code system" | = **bibcode** (Uniform Bibliographic Code, Schmitz et al. 1995). Format: `YYYY+journal+vol+page+author`. Paper describes this extensively. | ✅ (correct paraphrase) |

**Verdict**: ✅ All claims correct and well-supported by the 2000 paper.

---

### INSPIRE-HEP — inspirehep

| Claim in text | Actual (INSPIRE official + arXiv:2505.03860) | Status |
|---|---|---|
| "CERN, DESY, Fermilab, **SLAC**, and IN2P3" | **SLAC ceased all activities in 2021**. SLAC should be removed. | ❌ |
| Missing: **IHEP** | IHEP (Institute of High Energy Physics, Beijing) is an active partner. Both bib note and arXiv:2505.03860 confirm IHEP. | ❌ omitted |
| "author-disambiguated bibliography" | Confirmed: author disambiguation is a core INSPIRE feature. | ✅ |
| "since the SPIRES era of the 1970s" | SPIRES collaboration began 1974 (SLAC/DESY). "1970s" is correct. | ✅ |
| "canonical literature system" | INSPIRE replaced SPIRES as HEP's primary system ~2012. | ✅ |

**Required fix** (survey text):
> "jointly operated by CERN, DESY, Fermilab, SLAC, and IN2P3"  
→ **"jointly operated by CERN, DESY, Fermilab, IHEP, and IN2P3"**

**Verdict**: ❌ Two errors: SLAC is outdated (left 2021); IHEP omitted.

---

### GeoRef — georef

| Claim in text | Source says (AGI official + EBSCO) | Status |
|---|---|---|
| "maintained by the American Geosciences Institute" | AGI, founded 1966. ✅ | ✅ |
| "covering geology, geophysics, hydrology, and paleontology" | Confirmed by AGI and EBSCO. Coverage also includes petrology, mineralogy, marine geology, oceanography — but the four named are correct. | ✅ |

**Verdict**: ✅ Correct (coverage is broader than listed, but what's listed is accurate).

---

### IPCC AR6 — lee2023climate

| Claim in text | Source says (IPCC 2023 AR6 SYR) | Status |
|---|---|---|
| "IPCC's assessment reports … authoritative synthesis documents the field treats as canonical" | AR6 Synthesis Report is the IPCC's definitive summary across WG I–III. Accurate characterization. | ✅ |

**Verdict**: ✅ Correct.

---

## Summary table

| Paper | Text claims | Verdict |
|---|---|---|
| Crossref | free REST API, DOI-keyed, reference linkage | ✅ ("basic metadata" minor understatement) |
| OpenAlex | 5 entity types, fully-open REST API, aggregates Crossref+PubMed+repos | ✅ |
| S2ORC | bulk dataset, parsed full text, citation linkage, PubMed+arXiv ID mapping | ✅ |
| PubMed | MeSH controlled vocab, E-utilities API | ✅ |
| Europe PMC | open full text, integrated preprints, RESTful API | ✅ (bib title error in read-only file) |
| NASA ADS | astronomy+planetary+physics, bibcode, data archive links | ✅ |
| INSPIRE-HEP | partner list | ❌ SLAC removed 2021; IHEP missing |
| GeoRef | AGI, 4 coverage domains | ✅ |
| IPCC AR6 | authoritative synthesis | ✅ |

---

## Only remaining fix required

**INSPIRE-HEP partner list in main.tex** (line 370):

| | Text |
|---|---|
| **Current** | "jointly operated by CERN, DESY, Fermilab, **SLAC**, and IN2P3" |
| **Correct** | "jointly operated by CERN, DESY, Fermilab, **IHEP**, and IN2P3" |

Source: arXiv:2505.03860 confirms SLAC exited 2021; bib note and INSPIRE official documentation include IHEP.
