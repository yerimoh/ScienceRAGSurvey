---
title: "NOAA National Centers for Environmental Information (NCEI)"
bib_key: "noaa_ncei"
year: 2015
domain: earth, climate
type: dataset
venue: National Oceanic and Atmospheric Administration (system reference)
paper_link: https://www.ncei.noaa.gov
---
# NOAA National Centers for Environmental Information (NCEI)

noaa_ncei | 2015 | National Oceanic and Atmospheric Administration (system reference) | dataset | [earth, climate] | [portal](https://www.ncei.noaa.gov)

**DB**: NOAA NCEI — world's largest archive for weather, climate, and geophysical data
**DB size**: ~60 PB (archive + backup copy, per ncei.noaa.gov/about); ~20 TB newly ingested daily
**DB Open/Private**: Open (mostly public)
**Modality**: ['Time series', 'Satellite image', 'Gridded data', 'Station data']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NOAA NCEI portal / CDO (Climate Data Online) API

> National Oceanic and Atmospheric Administration (system reference) | 2015 | dataset | earth, climate
#### TL;DR
The world's largest weather and climate archive, launched in 2015 by consolidating NOAA's three data centers (NCDC, NGDC, NODC). It holds more than 100 PB of climate records (surface observations, satellite, ocean, geophysical) and publicly distributes dozens of core climate datasets such as GHCN, GSOD, and OISST. **Note that this is an institutional system reference entry (`@misc`), not a formal academic paper.**

#### Background
**Limitations of prior infrastructure**
- Within NOAA, weather (NCDC), geophysical (NGDC), and ocean (NODC) data were operated separately, making unified search impossible
- Long-term preservation was needed for weather observation records predating 1970s digitization
- Continuous, homogeneous time series spanning more than 100 years were needed for climate change monitoring

**Why this system is needed**
- A single authoritative source for Climate Normals, extreme-value records, and tracking of global temperature change
- Foundational data for the IPCC, the U.S. National Climate Assessment (NCA), and weather forecast model verification
- Supports climate-related decision-making in insurance, agriculture, energy, urban planning, and more

#### Architecture
NCEI is the consolidation of three predecessor agencies:
- **NCDC** (National Climatic Data Center, 1951~): weather and climate records
- **NGDC** (National Geophysical Data Center, 1964~): geomagnetic, seismic, and coastal data
- **NODC** (National Oceanographic Data Center, 1961~): ocean temperature, salinity, and currents

Major datasets: GHCN (Global Historical Climatology Network), GSOD (Global Surface Summary of Day), OISST (Optimum Interpolation SST), NSIDC-collaborated ice and snow cover, NEXRAD radar archive.

#### Access
| Method | Description |
|---|---|
| CDO (Climate Data Online) | ncei.noaa.gov/cdo-web/ — per-station data download |
| NCEI API | api.ncei.noaa.gov — RESTful JSON API |
| THREDDS/OPeNDAP | remote partial download of gridded data |
| S3 cloud | AWS Open Data — NOAA satellite and weather data |

#### Data formats
- Surface observations: CSV/JSON (GHCN-D, GSOD, ISD)
- Gridded data: NetCDF (OISST, reanalysis)
- Satellite imagery: GOES, AVHRR, VIIRS
- Geophysical: geomagnetic, seismic, and tsunami events
- Ocean: CTD (water temperature and salinity), waves, sea-level change

#### Key statistics (per ncei.noaa.gov/about)
| Item | Value |
|---|---|
| Total data held | **~60 PB** (archive + backup copy, confirmed at ncei.noaa.gov/about) |
| Daily new ingest | **~20 TB** |
| Number of GHCN-D stations | **~100,000**+ |
| Record period | **140+ years** (some beginning in the 1880s) |
| Established | 2015 (NCDC+NGDC+NODC consolidation) |
| Access | Public (free) |

#### Limitations
- The diversity of data formats and APIs makes building a consistent RAG pipeline difficult
- Quality control of historical station data is uneven (homogenization needed)
- Some high-resolution real-time data have commercial redistribution restrictions
- The archive's vast scale requires domain knowledge to navigate specific datasets

## Related links
- **Portal**: [https://www.ncei.noaa.gov](https://www.ncei.noaa.gov)
- **CDO**: [https://www.ncei.noaa.gov/cdo-web/](https://www.ncei.noaa.gov/cdo-web/)
