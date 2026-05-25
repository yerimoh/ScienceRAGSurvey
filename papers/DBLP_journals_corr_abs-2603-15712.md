---
title: "LLM-Driven Discovery of High-Entropy Catalysts via Retrieval-Augmented Generation"
bib_key: "DBLP:journals/corr/abs-2603-15712"
year: 2026
domain: material
type: Method
venue: arXiv 2026
paper_link: https://arxiv.org/abs/2603.15712
---
# LLM-Driven Discovery of High-Entropy Catalysts via Retrieval-Augmented Generation

DBLP:journals/corr/abs-2603-15712 | 2026 | arXiv 2026 | Method | [material] | [paper](https://arxiv.org/abs/2603.15712)

**Retriever**: RAG over 50,000+ materials database (Materials Project, NOMAD, OC20)
**Eval Task**: CO2 reduction catalyst discovery (thermodynamic stability, cost, band gap, mechanical stability, limiting potential)
**Eval Metric**: Thermodynamic stability rate (%), limiting potential (V), cost ($/kg), volcano plot proximity
**Method Name**: HEA-RAG (LLM-RAG for High-Entropy Catalyst Discovery)
**Modality**: Text, Structured materials data

> arXiv 2026 | 2026 | Method | material
#### 📌 한 줄 요약
50,000개 이상의 기지(known) 재료 데이터베이스에 RAG로 접지된 GPT-4 기반 프레임워크로 250개 이상의 고엔트로피 합금(HEA) CO2 환원 촉매 후보를 생성하여 82% 열역학적 안정성과 IrO2 대비 25% 향상된 0.285V 제한 전위를 달성하였다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 재료 발견은 10-20년의 개발 주기를 요구하며 깊은 도메인 전문 지식이 필요함
- 기존 고처리량 스크리닝(HTS)은 넓은 화학 공간 탐색에 계산 비용이 과도함

**이 시스템이 필요한 이유**
- CO2 환원 효율 촉매 개발을 위한 화학 공간 탐색 가속화가 필요
- LLM이 재료 데이터베이스를 실시간으로 참조하며 다목적 제약(비용, 전도성, 안정성) 하에 후보를 생성하는 시스템 필요

#### 🔨 시스템 구성
Materials Project, NOMAD, Open Catalyst 2020 (OC20) 데이터셋을 통합한 50,000개 이상의 기지 재료 벡터 데이터베이스를 구축한다. GPT-4가 이 데이터베이스에서 RAG를 통해 화학 공간을 탐색하고, DFT(밀도범함수이론) 계산으로 후보 안정성을 검증한다. Volcano plot 분석으로 이론적 활성 최적점 근접 여부를 평가한다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 재료 데이터베이스 규모 | 50,000개 이상 기지 재료 |
| 생성된 촉매 후보 수 | 250개 이상 |
| 열역학적 안정성 비율 | 82% |
| 비용·전도성·기계 안정성 달성 | 68% (<$100/kg, band gap<0.1eV, B/G>1.75) |
| 최고 성능 합금 | Fe0.2Co0.2Ni0.2Ir0.1Ru0.3, 제한 전위 0.285V |
| IrO2 대비 개선 | 25% 향상 |
| 비용-성능 최적 합금 | Cr0.2Fe0.2Co0.3Ni0.2Mo0.1, $18/kg |
| Volcano plot 근접 비율 | 78% LLM 생성 촉매 |
| 계산 효율 | 기존 HTS 대비 200배 향상 |

#### ⚠️ 한계점
- DFT 검증 단계가 여전히 계산 집약적
- 고엔트로피 합금의 실제 합성 가능성은 검증되지 않은 경우 포함
- CO2 환원에 특화되어 다른 촉매 응용 분야로의 직접 전이 제한

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2603.15712](https://arxiv.org/abs/2603.15712)
