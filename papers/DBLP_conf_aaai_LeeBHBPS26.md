---
title: "RAG-Enhanced Collaborative LLM Agents for Drug Discovery"
bib_key: "DBLP:conf/aaai/LeeBHBPS26"
year: 2026
domain: chem, medical
type: Method
venue: AAAI 2026
paper_link: https://doi.org/10.1609/aaai.v40i1.37020
---
# RAG-Enhanced Collaborative LLM Agents for Drug Discovery (CLADD)

DBLP:conf/aaai/LeeBHBPS26 | 2026 | AAAI 2026 | Method | [chem, medical] | [paper](https://doi.org/10.1609/aaai.v40i1.37020)

**Retriever**: RAG from biomedical knowledge bases (Drug Repurposing Hub, DrugBank, STITCH v5.0)
**Eval Task**: Drug-target interaction prediction, molecular property prediction (BBBP, Sider, ClinTox, BACE), property-specific molecular captioning
**Eval Metric**: Precision (top-5 protein prediction), AUROC
**Method Name**: CLADD (Collaborative LLM Agents for Drug Discovery)
**Modality**: Text, Molecular structures (SMILES)

> AAAI 2026 | 2026 | Method | chem · medical
#### 📌 한 줄 요약
도메인 특화 파인튜닝 없이 여러 LLM 에이전트가 협력하여 Drug Repurposing Hub, DrugBank, STITCH 등 생물의학 지식 베이스로부터 동적으로 검색하여 약물 발굴 태스크(drug-target interaction, 독성 분류)를 수행하는 RAG 기반 에이전틱 시스템이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 도메인 특화 LLM 파인튜닝은 비용이 높고, 새로운 실험 데이터의 빠른 통합이 어려움
- 실제 과학적 질문은 복잡하고 개방형이어서 정적 지식 검색만으로는 불충분함
- 생화학 데이터의 이종성(heterogeneity), 모호성, 다중 출처 통합이 RAG 적용의 주요 장애물

**이 시스템이 필요한 이유**
- 약물 발굴 태스크에서 지속적으로 생성되는 실험 데이터를 신속히 통합할 필요
- 제로샷 설정에서 일반 목적 LLM을 약물 발굴에 활용하는 유연한 프레임워크 필요

#### 🔨 시스템 구성
여러 LLM 에이전트가 협력하여 Drug Repurposing Hub, DrugBank (13,688 분자), STITCH v5.0으로부터 동적으로 정보를 검색하고, 쿼리 분자를 컨텍스트화하여 관련 증거를 통합한다. RAG 워크플로에서 생화학 데이터의 이종성과 모호성 문제를 해결하는 특수 처리 방법을 도입하였다. 파인튜닝 없이 제로샷 설정으로 동작한다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| Drug-target interaction 데이터셋 | Drug Repurposing Hub, DrugBank, STITCH v5.0 (총 13,688 분자) |
| Toxicity 데이터셋 | BBBP, Sider, ClinTox, BACE |
| BBBP AUROC | 72.28 (±1.04) — 최고 성능 |
| Sider AUROC | 66.42 (±1.31) — 최고 성능 |
| ClinTox AUROC | 93.80 (±2.30) — 최고 성능 |
| BACE AUROC | 77.74 (±3.15) |
| 비교 | GPT-4o, domain LLMs (MolT5, BioT5), GNN (GraphMVP, MoleculeSTM) 모두 능가 |

#### ⚠️ 한계점
- 외부 데이터베이스에 없는 분자("No Overlap" 시나리오)에서는 성능 일부 저하
- 여러 에이전트 협력으로 인한 추론 지연(latency) 증가
- 도메인 특화 파인튜닝 모델과의 격차가 일부 태스크에서 남아 있음

## 관련 정보
- **논문 (AAAI)**: [https://doi.org/10.1609/aaai.v40i1.37020](https://doi.org/10.1609/aaai.v40i1.37020)
- **arXiv preprint**: [https://arxiv.org/abs/2502.17506](https://arxiv.org/abs/2502.17506)
