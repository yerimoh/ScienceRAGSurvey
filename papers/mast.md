---
title: "Mikulski Archive for Space Telescopes (MAST)"
bib_key: "mast"
year: 1997
domain: astronomy
type: dataset
venue: Space Telescope Science Institute (system reference)
paper_link: https://archive.stsci.edu
---
# Mikulski Archive for Space Telescopes (MAST)

mast | 1997 | Space Telescope Science Institute (system reference) | dataset | [astronomy] | [portal](https://archive.stsci.edu)

**DB**: MAST — unified NASA archive for UV/optical/NIR space telescope data
**DB size**: Petabyte-scale; hosts Hubble (~200 TB+), JWST (growing rapidly), Kepler/K2, TESS, Pan-STARRS (~1 PB DR2), GALEX, IUE, and others
**DB Open/Private**: Open (most missions; some proprietary periods)
**Modality**: ['Image', 'Spectrum', 'Light curve', 'Catalog']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: MAST Portal / MAST API (astroquery.mast)

> Space Telescope Science Institute (system reference) | 1997 | dataset | astronomy
#### TL;DR
An integrated NASA space telescope archive operated by the Space Telescope Science Institute (STScI) in the United States. It is a core infrastructure for astronomy K3 observational data, providing Hubble, JWST, TESS, Kepler, and Pan-STARRS data through a single portal. **Note that this is an institutional system reference item (`@misc`), not a formal academic paper.**

#### Background
**Limitations of existing infrastructure**
- In the 1980s–1990s, NASA space telescopes each operated separate archives → cross-mission data integration was impossible
- Long-term preservation and accessibility of early mission data such as IUE (1978) and HST (1990) needed to be secured

**Why this system is needed**
- As the science operations institution for HST, STScI naturally serves as the hub of the UV/optical archive
- A single portal enables cross-mission searches and the combination of multi-wavelength data for the same celestial object
- Designated as the official archive for JWST (2021–) data, it now manages the most cutting-edge data in astronomy

#### Architecture
MAST Portal (mast.stsci.edu): web-based search, visualization, and download. astroquery.mast: Python API. CAOM (Common Archive Observation Model): a uniform cross-mission metadata schema. DOI-based dataset citation support. Provides an AWS S3 cloud copy (MAST in the Cloud).

#### Hosted mission list
| Mission | Wavelength range | Main data types |
|---|---|---|
| Hubble Space Telescope (HST) | UV–optical–near-infrared | Images, spectra, time series |
| James Webb Space Telescope (JWST) | Near-infrared–mid-infrared | Images, spectra |
| TESS | Optical | Light curves, full-frame images |
| Kepler / K2 | Optical | Light curves (exoplanets) |
| Pan-STARRS (PS1) | Optical | Images, catalogs |
| GALEX | UV | Images, spectra |
| IUE (1978–1996) | UV | Spectra (legacy) |
| FUSE | Far-ultraviolet | Spectra |

#### Access
| Method | Description |
|---|---|
| MAST Portal | mast.stsci.edu — web GUI browsing and download |
| astroquery.mast | Python library, batch queries |
| MAST API (REST) | Returns JSON/VO Table |
| AWS S3 | s3://stpubdata/ — direct cloud access |

#### Key statistics (model knowledge)
| Item | Value |
|---|---|
| Operations start | 1997 (based on the IUE archive) |
| Hosted missions | 20+ |
| HST accumulated data | ~200 TB+ |
| Pan-STARRS DR2 | ~1 PB |
| JWST annual data production | ~50–100 TB/yr |
| Access | Public (after proprietary period elapses) |

#### Limitations
- Radio, X-ray, and gamma-ray missions are not hosted by MAST (separate NRAO, Chandra, Fermi archives)
- Some mission data have a proprietary period (12–18 months)
- Large datasets (TESS full-frame images, Pan-STARRS) are impractical to download locally — cloud analysis is required
- Data formats are non-uniform across missions (FITS-based but with differing extension structures)

## Related links
- **Portal**: [https://archive.stsci.edu](https://archive.stsci.edu)
- **MAST Portal**: [https://mast.stsci.edu](https://mast.stsci.edu)
