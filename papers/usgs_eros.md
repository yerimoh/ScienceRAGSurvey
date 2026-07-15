---
title: "USGS Earth Resources Observation and Science (EROS) Center"
bib_key: "usgs_eros"
year: 1973
domain: earth
type: dataset
venue: U.S. Geological Survey (system reference)
paper_link: https://www.usgs.gov/centers/eros
---
# USGS Earth Resources Observation and Science (EROS) Center

usgs_eros | 1973 | U.S. Geological Survey (system reference) | dataset | [earth] | [portal](https://www.usgs.gov/centers/eros)

**DB**: USGS EROS Center — Landsat and Earth observation archive
**DB size**: ~10 PB+ (complete Landsat 1–9 record + other satellite data); Landsat: 9 million+ scenes
**DB Open/Private**: Open (since the 2008 Landsat full open-data policy)
**Modality**: ['Satellite image', 'Multispectral', 'Thermal', 'Time series']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: EarthExplorer / USGS EROS Archive

> U.S. Geological Survey (system reference) | 1973 | dataset | earth
#### TL;DR
A USGS Earth-observation data archive established in 1973. It holds the **complete Landsat 1–9 record (over 50 years)** running from 1972 to the present, making it the world's longest continuous archive of land-surface satellite observation. Since the 2008 shift to a free open-data policy, it has been a core K3 resource for research on land-use change, deforestation, glacier retreat, and urban expansion. **Note that this is an institutional system reference entry (`@misc`), not a formal academic paper.**

#### Background
**Limitations of prior infrastructure**
- Before the 1960s, there were no digital means to record changes in the Earth's surface on a regular, uniform basis
- The launch of ERTS-1 (Earth Resources Technology Satellite, later Landsat 1) in 1972 created the need for a systematic archive

**Why this system is needed**
- Landsat repeatedly images the entire global surface on a 16-day revisit cycle → enabling time-series change detection
- The 2008 free release of Landsat (open archive) caused an explosive increase in use by researchers, governments, and NGOs worldwide
- Joint NASA–USGS operation guarantees the continuity of the Landsat satellites

#### Architecture
EROS Center (Sioux Falls, South Dakota): the primary data-processing and archive facility. EarthExplorer (earthexplorer.usgs.gov): web-based search, ordering, and download. ESPA (USGS EROS Science Processing Architecture): on-demand data processing.

Landsat band configuration:
- Landsat 1–5 (MSS/TM): 4–7 bands, 30–80 m resolution
- Landsat 7 (ETM+): 8 bands, 15 m panchromatic–30 m multispectral
- Landsat 8–9 (OLI/TIRS): 11 bands, 15–30 m (thermal infrared 100 m)

#### Access
| Method | Description |
|---|---|
| EarthExplorer | earthexplorer.usgs.gov — scene search and download |
| USGS M2M API | Machine-to-Machine API (JSON) |
| Google Earth Engine | Landsat collections integrated into GEE |
| AWS Open Data | s3://usgs-landsat/ — direct cloud access |

#### Data formats
- GeoTIFF (Landsat Collection 1/2 Surface Reflectance/Temperature)
- HDF (legacy)
- STACItem metadata (Collection 2 onward)
- Analysis Ready Data (ARD): tile-based, atmospheric correction completed

#### Key statistics (model knowledge)
| Item | Value |
|---|---|
| Landsat continuous observation period | **50 years+** (1972–present) |
| Total number of Landsat scenes | **~9,000,000** scenes+ |
| Satellite generations | **Landsat 1–9** (9 generations) |
| Spatial resolution | 15–80 m (by band and generation) |
| Revisit cycle | 16 days (single satellite), 8 days (Landsat 8+9 combined) |
| Free-release transition | 2008 |
| Established | 1973 |

#### Limitations
- The 16-day revisit cycle makes daily monitoring of rapid events (floods, fires) impossible (complemented by Sentinel-2's 8–10 day cycle)
- A high proportion of scenes are unusable due to cloud cover (affecting 40%+ in tropical regions)
- Low geometric-correction accuracy for early Landsat 1–4 data
- The 30 m resolution is insufficient for detailed urban analysis and individual farm-field monitoring

## Related links
- **Portal**: [https://www.usgs.gov/centers/eros](https://www.usgs.gov/centers/eros)
- **EarthExplorer**: [https://earthexplorer.usgs.gov](https://earthexplorer.usgs.gov)
