---
title: "The Sloan Digital Sky Survey: Technical Summary"
bib_key: "york2000sloan"
year: 2000
domain: astronomy
type: dataset
venue: The Astronomical Journal
paper_link: https://arxiv.org/abs/astro-ph/0006396
---
# The Sloan Digital Sky Survey: Technical Summary

york2000sloan | 2000 | The Astronomical Journal | dataset | [astronomy] | [paper](https://arxiv.org/abs/astro-ph/0006396)

**DB**: Sloan Digital Sky Survey (SDSS) — imaging and spectroscopic sky survey
**DB size**: Survey goal: pi steradians (northern sky), ~1 million galaxy spectra, ~100,000 quasar spectra (York 2000 design spec; actual DR17 cumulative: hundreds of millions of objects)
**DB Open/Private**: Open
**Modality**: ['Image', 'Spectrum', 'Catalog']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: SDSS (2.5m telescope, Apache Point Observatory)

> The Astronomical Journal | 2000 | dataset | astronomy
#### TL;DR
An SDSS technical-summary paper describing the design specifications as of 2000. It images approximately pi steradians of the northern sky through 5 optical filters (ugriz) and aims to obtain spectra for roughly 1 million galaxies and 100,000 quasars. Across decades of SDSS data releases (DR1–DR17), hundreds of millions of objects have been cataloged, making it a core resource of K3 observational data in modern astronomy.

#### Background
**Limitations of existing infrastructure**
- Prior sky surveys relied on film-based photographic plates, making uniform photometric calibration and large-scale spectroscopy impossible
- Lack of systematic data on galaxy redshift distributions, large-scale structure, and quasar distributions

**Why this system is needed**
- Integrating photometric and spectroscopic data on the same telescope to measure luminosity and distance simultaneously
- Large-scale automated observation with a 5-band CCD imager (2048×2048 arrays) and multi-fiber spectrographs (640 simultaneous)
- Releasing calibrated digital catalogs for use in galaxy evolution, quasar studies, and Milky Way structure research

#### Architecture
A dedicated 2.5m telescope (Apache Point Observatory, New Mexico). 5 filters (u, g, r, i, z): g' ~23 mag depth. Two fiber spectrographs (320 fibers each): 3800–9200Å, R~2000. Data pipeline: automated real-time object extraction, photometric calibration, and spectral extraction. Includes the Photo pipeline (image processing and star–galaxy separation) and the Spectro pipeline (automated redshift measurement).

#### Access
| Method | Description |
|---|---|
| SkyServer | skyserver.sdss.org — web SQL query interface |
| CasJobs | large-volume batch queries |
| SciServer | cloud analysis environment |
| FITS files | das.sdss.org — direct download of raw images and spectra |

#### Data formats
- 5-band photometric catalog: position, magnitude, morphology parameters
- Spectroscopic catalog: redshift, classification (star/galaxy/quasar), spectra
- Image tiles (FITS format)
- CasJobs SQL-queryable schema

#### Key statistics
| Item | Value |
|---|---|
| Photometric target area | ~10,000 deg² (pi sr) |
| Spectroscopic target galaxies | ~1,000,000 |
| Spectroscopic target quasars | ~100,000 |
| DR17 cumulative spectra | ~4.9M spectra |
| Photometric depth | g' ~ 23 mag |
| Wavelength range (spectroscopy) | 3800–9200 Å |

#### Limitations
- The 2000 paper describes pre-completion design specifications, so actual achieved values require reference to subsequent DR papers
- Centered on high-latitude northern-sky regions, so the galactic plane and southern sky are not covered
- Provides only 5 optical bands (excluding infrared and UV); combining with subsequent WISE and GALEX data is required

## Related links
- **Paper**: [https://arxiv.org/abs/astro-ph/0006396](https://arxiv.org/abs/astro-ph/0006396)
- **Data portal**: [https://www.sdss.org](https://www.sdss.org)
