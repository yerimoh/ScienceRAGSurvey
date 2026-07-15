---
title: "MATLAB and Simulink"
bib_key: "matlabsimulink"
year: 1984
domain: general
type: dataset
venue: MathWorks (Commercial Software)
paper_link: https://www.mathworks.com
---
# MATLAB and Simulink

matlabsimulink | 1984 | MathWorks (Commercial Software) | dataset | [general] | [website](https://www.mathworks.com)

**DB**: MATLAB built-in numerical algorithm library, Simulink block-diagram library and parameter base (Aerospace, Control System, Signal Processing Toolbox, etc.)
**DB size**: N/A (licensed software, no public figures)
**DB Open/Private**: Subscription (commercial license; academic discounts available)
**Modality**: Tabular, Code
**Retriever**: N/A (K4 commercial computing environment — no directly queryable API)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: MATLAB / Simulink (MathWorks)

> MathWorks | 1984 | dataset | general
#### 📌 TL;DR
A numerical computing and simulation environment released by MathWorks in 1984 (MATLAB) / 1990 (Simulink), in which specialized knowledge from a wide range of engineering domains such as control engineering, signal processing, aerospace, and autonomous driving is encapsulated in the form of Toolboxes and used as an industrial and academic standard.

#### 🎯 Background
**Limitations of existing computing tools**
- Engineering computation in the 1970s-1980s required FORTRAN/BASIC coding, posing a high barrier for those without a mathematics background
- There was no standardized computation and visualization environment for control system design and signal processing algorithm verification

**The position of MATLAB/Simulink**
- MATLAB: the de facto standard for matrix-based numerical computation and data analysis (especially in the control and signal processing fields)
- Simulink: block-diagram-based dynamic system simulation; used from control systems, powertrain, and avionics design all the way to automatic code generation (AutoCode)

#### 🔨 Architecture
- **MATLAB Core**: function library for matrix operations, optimization, statistics, and machine learning
- **Simulink**: a block-diagram environment for modeling continuous/discrete systems + Stateflow (finite state machines)
- **Toolboxes**: more than 100, including Control System, Signal Processing, Aerospace, Robotics, Deep Learning, Phased Array
- **Embedded knowledge**: each Toolbox has domain-expert algorithm parameters and reference models built in

#### 📥 Access
| Method | Description |
|---|---|
| MATLAB interpreter | Interactive command window and script execution |
| Simulink GUI | Block-diagram-based model construction and simulation |
| MATLAB Engine API | Calling the MATLAB engine from Python/C/C++/Java |
| MATLAB Online | Cloud-based web environment |

#### 📤 Data formats
- Numerical arrays, structs, tables (.mat, .csv, Excel output)
- Simulink simulation results (.slx, .mat time-series data)
- Automatic code generation results (C/C++, HDL, PLC code)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| MATLAB initial release | 1984 |
| Simulink initial release | 1990 |
| Number of supported Toolboxes | more than 100 (domain-specific specialized libraries) |
| Public database size | Not public (commercial license) |

#### ⚠️ Limitations
- The algorithm parameters and reference data encapsulated in the Toolboxes cannot be directly accessed or queried by an external RAG system
- A transition to the Python (NumPy/SciPy) ecosystem is underway in some fields, but legacy code dependency in the control and aerospace fields remains strong
- License cost and platform lock-in are drawbacks compared to open-source alternatives

## Related links
- **Website**: [MathWorks MATLAB](https://www.mathworks.com/products/matlab.html) / [MathWorks Simulink](https://www.mathworks.com/products/simulink.html)
- **K4 classification**: Embedded in software — tacit knowledge of control, signal processing, and aerospace engineering is embedded in the Toolbox parameter base
