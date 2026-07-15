---
title: "Reaxys"
bib_key: "reaxys"
year: 2009
domain: chem
type: dataset
venue: Elsevier (misc)
paper_link: https://www.reaxys.com
---
# Reaxys

reaxys | 2009 | Elsevier | dataset | [chem] | [paper](https://www.reaxys.com)

**DB**: Reaxys (Elsevier)
**DB size**: Subscription-based (no public figures reported)
**DB Open/Private**: Subscription
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Reaxys web platform

> Elsevier | 2009 | dataset | chem
#### 📌 TL;DR
Reaxys is a subscription-based chemical reaction, substance, and bioactivity DB operated by Elsevier. It integrates the Beilstein (organic chemistry) and Gmelin (inorganic and organometallic chemistry) DBs to support reaction search and synthetic route planning for synthetic chemists.

#### 🎯 Background
**Limitations of existing infrastructure**
- The Beilstein (organic) and Gmelin (inorganic) DBs were operated separately, making integrated access inconvenient
**Why this system is needed**
- A unified reaction-substance DB is needed for synthetic route planning (retrosynthesis)
- Alongside SciFinder, it serves as one of the two major commercial infrastructures for synthetic chemists

#### 🔨 Architecture
It integrates the Beilstein Database (organic chemistry reactions and substances), the Gmelin Database (inorganic and organometallic chemistry), and patent chemistry data. Launched in 2009 as the unified Reaxys brand. Enables integrated search across structures, reactions, and physicochemical properties.

#### 📥 Access
| Method | Description |
|---|---|
| Subscription platform | reaxys.com (institutional subscription required) |
| Structure search | Search based on compound and reaction structures |
| API | Reaxys API (provided under institutional agreements) |

#### 📤 Data formats
- Compound records (structures, physicochemical properties)
- Reaction records (reactants, products, conditions, yields, sources)
- Bioactivity data

#### 📊 Key statistics (per paper)
| Item | Figure |
|---|---|
| Launch | 2009 (Beilstein+Gmelin integration) |
| Data coverage | Subscription-based; no public figures released by Elsevier |

#### ⚠️ Limitations
- Being subscription-based, it is not directly accessible to open-science RAG systems
- Alongside SciFinder, it represents the open-closed gap in the chemistry field
- High cost limits access for small institutions

## Related links
- **Official page**: [Reaxys](https://www.reaxys.com)
