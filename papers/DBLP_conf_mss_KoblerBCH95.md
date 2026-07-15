---
title: "Architecture and Design of Storage and Data Management for the NASA Earth Observing System Data and Information System (EOSDIS)"
bib_key: "DBLP:conf/mss/KoblerBCH95"
year: 1995
domain: earth
type: dataset
venue: IEEE Symposium on Mass Storage Systems (MSS 1995)
paper_link: https://doi.org/10.1109/MASS.1995.528217
---
# Architecture and Design of Storage and Data Management for the NASA EOSDIS

DBLP:conf/mss/KoblerBCH95 | 1995 | MSS 1995 | dataset | [earth] | [paper](https://doi.org/10.1109/MASS.1995.528217)

**DB**: NASA Earth Observing System Data and Information System (EOSDIS) / NASA Earthdata
**DB size**: Tens of PB scale (integrated archive of Earth observation satellite data; continuously accumulated since 1994)
**DB Open/Private**: Open (requires a NASA Earthdata account, free)
**Modality**: ['Satellite image', 'Gridded data', 'Time series', 'Tabular']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NASA Earthdata / EOSDIS (earthdata.nasa.gov)

> MSS 1995 | 1995 | dataset | earth
#### 📌 TL;DR
A 1995 paper describing the storage and data management architecture of EOSDIS, NASA's integrated archive of Earth observation satellite data. It explains the design of a distributed storage and distribution system for EOS satellite data covering land, atmosphere, ocean, and cryosphere, and serves as an early design document for the infrastructure that leads to today's NASA Earthdata portal.

#### 🎯 Background
**Limitations of existing infrastructure**
- Before the 1990s, NASA Earth observation data was managed by dispersed, individual mission teams, making integrated search and access impossible
- Absence of infrastructure for long-term preservation and distribution to scientists of terabyte- to petabyte-scale satellite data
- Need for a standardized data system to match the launch of the EOS satellite constellation such as Terra and Aqua

**Why this system is needed**
- To build an integrated Earth observation data archive covering the entire Earth system (land, atmosphere, ocean, cryosphere)
- Domain-specific specialized processing and distribution via a distributed network of DAACs (Distributed Active Archive Centers)
- Interoperability of multi-mission data through standard data formats (HDF-EOS) and metadata schemes

#### 🔨 Architecture
EOSDIS is a distributed network composed of 12 DAACs (Distributed Active Archive Centers). Each DAAC handles a domain-specific specialized processing role (e.g., NSIDC → cryosphere, SEDAC → socioeconomic-environmental, ORNL DAAC → carbon and ecology). Data standard: HDF-EOS (Hierarchical Data Format). EOSDIS Data Pool: public FTP/HTTP download. Earthdata Search (current): integrated metadata catalog search.

#### 📥 Access
| Method | Description |
|---|---|
| Earthdata Search | search.earthdata.nasa.gov — integrated metadata search and data ordering |
| Direct DAAC access | Each DAAC portal (NSIDC, LP DAAC, ORNL, GES DISC, etc.) |
| OPeNDAP | Remote partial access to gridded data |
| S3/Cloud | NASA Earthdata Cloud (AWS) — high-performance cloud analysis |

#### 📤 Data formats
- Satellite imagery: HDF-EOS, GeoTIFF, NetCDF
- Atmospheric data: AIRS, MODIS, MERRA-2 reanalysis
- Land data: MODIS vegetation, surface reflectance, fire
- Ocean data: SST, sea surface height, chlorophyll
- Cryosphere: sea ice extent, glaciers, snow cover

#### 📊 Key statistics (based on the paper/official sources)
| Item | Value |
|---|---|
| Archive size | **Tens of PB** (as of the 2020s) |
| Number of DAACs | **12** distributed archive centers |
| Paper publication | MSS 1995 (IEEE) — early system design document |
| Access | Public (free NASA Earthdata account registration) |
| Data coverage | Land · atmosphere · ocean · cryosphere in full |

#### ⚠️ Limitations
- As a 1995 paper, it differs substantially from the actual operational scale and functionality of current EOSDIS/Earthdata (a limitation as a reference)
- Data formats differ by domain, imposing preprocessing burden when integrating data across multiple DAACs
- High-resolution raw data reaches file sizes of several GB to tens of GB, making direct use for RAG difficult
- No known case of a scientific-domain RAG system using EOSDIS as a retrieval corpus

## Related links
- **Paper**: [doi:10.1109/MASS.1995.528217](https://doi.org/10.1109/MASS.1995.528217)
- **Current portal**: [NASA Earthdata](https://www.earthdata.nasa.gov)
