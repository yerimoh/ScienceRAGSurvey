---
title: "Gaia Data Release 3: Summary of the Content and Survey Properties"
bib_key: "vallenari2023gaia"
year: 2023
domain: astronomy
type: dataset
venue: Astronomy & Astrophysics
paper_link: https://arxiv.org/abs/2208.00211
---
# Gaia Data Release 3: Summary of the Content and Survey Properties

vallenari2023gaia | 2023 | Astronomy & Astrophysics | dataset | [astronomy] | [paper](https://arxiv.org/abs/2208.00211)

**DB**: Gaia Data Release 3 (GDR3) — ESA Gaia astrometric/photometric/spectroscopic all-sky survey
**DB size**: ~1,500 million (1.5 billion) sources with positions, parallaxes, proper motions; ~470 million with astrophysical parameters; ~220 million BP/RP spectra
**DB Open/Private**: Open
**Modality**: ['Astrometry', 'Photometry', 'Spectrum', 'Catalog']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Gaia DR3 (ESA Gaia satellite, L2 orbit, launched 2013)

> Astronomy & Astrophysics | 2023 | dataset | astronomy
#### TL;DR
The third data release of the European Space Agency (ESA) Gaia satellite, a catalogue processing the first 34 months of mission observations. It provides astrometry, parallaxes, proper motions, and photometry for **about 1.5 billion sources**. One of the largest all-sky catalogues in the history of astronomy, including radial velocities for 33 million sources, 220 million BP/RP low-resolution spectra, and astrophysical parameters for 470 million sources.

#### Background
**Limitations of existing infrastructure**
- Hipparcos (1997) catalogue: revolutionary at the time with parallax measurements for 118,218 stars, but limited in scale and precision
- Ground-based astrometric catalogues: precision limited by atmospheric refraction and temperature variations, and unable to observe the whole sky uniformly

**Why this system is needed**
- Mapping the 3D structure of the Galaxy with microarcsecond (μas) precision parallaxes
- Providing a uniform astrometric reference frame (linked to the ICRF) by repeatedly scanning the whole sky with a single satellite
- Completing the 6D phase space (position + velocity) by including radial velocities and spectra

#### Architecture
Gaia satellite: L2 Lissajous orbit, two telescopes (fixed at an angle of 106.5°), SiC mirrors. Main camera: 106 CCDs (0.7 Giga-pixel). Scanning law: rotation every 5–6 hours, precession every 63.3 days. Data processing: Gaia Data Processing and Analysis Consortium (DPAC, 450+ people across 9 European countries).

- **Astrometry**: position, parallax, proper motion (G < 21 mag)
- **Photometry**: G, G_BP, G_RP 3-band
- **Spectroscopy**: RVS (radial velocity), BP/RP (low-resolution optical spectra)

#### Access
| Method | Description |
|---|---|
| Gaia Archive | gea.esac.esa.int — ADQL queries |
| CDS VizieR | vizier.cds.unistra.fr — catalogue lookup |
| Gaia DR3 direct download | ESA Science Data Centre |
| TAP service | standard IVOA TAP protocol |

#### Data formats
- Main source catalogue (position, parallax, proper motion, G/GBP/GRP photometry)
- Radial velocity catalogue (RVS, ~33M sources)
- BP/RP mean spectra (~220M sources)
- RVS mean spectra (~1M sources)
- Astrophysical parameters (Teff, logg, [Fe/H], etc., ~470M sources)
- Variable star catalogue (~10M, 24 types)
- Solar system objects (~150,000)
- Binary star orbital elements (~800,000 pairs)

#### Key statistics
| Item | Value |
|---|---|
| Total number of sources | **~1,500,000,000** (1.5 billion) |
| Radial velocity sources | **~33,000,000** |
| BP/RP spectra | **~220,000,000** |
| Astrophysical parameters | **~470,000,000** sources |
| Variable stars | **~10,000,000**, 24 types |
| Solar system objects | **~150,000** |
| Asteroid reflectance spectra | **~60,000** |
| Binary stars | **~800,000** pairs |
| Observation period (GDR3) | 34 months (early mission) |

#### Limitations
- GDR3 is based on the first 34 months of mission data, so it has lower precision and completeness than the final Gaia DR4/DR5
- Precision degrades for bright stars (G < 6) and in dense cluster regions due to saturation and crowding issues
- The resolution of BP/RP spectra is very low (R~50–100): detailed elemental abundances cannot be measured
- Radial velocity completeness is limited to G_RVS < 14 mag

## Related links
- **Paper**: [https://arxiv.org/abs/2208.00211](https://arxiv.org/abs/2208.00211)
- **Gaia Archive**: [https://gea.esac.esa.int/archive/](https://gea.esac.esa.int/archive/)
