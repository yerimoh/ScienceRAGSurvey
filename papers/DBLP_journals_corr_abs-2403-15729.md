---
title: "Towards a RAG-based Summarization Agent for the Electron-Ion Collider"
bib_key: "DBLP:journals/corr/abs-2403-15729"
year: 2024
domain: physics
type: Method
venue: arXiv 2024
paper_link: https://arxiv.org/abs/2403.15729
---
# Towards a RAG-based Summarization Agent for the Electron-Ion Collider (RAGS4EIC)

DBLP:journals/corr/abs-2403-15729 | 2024 | arXiv 2024 | Method | [physics] | [paper](https://arxiv.org/abs/2403.15729)

**Retriever**: Dense vector retrieval (LangChain-based, EIC institutional documents)
**Eval Task**: EIC experiment information summarization and citation
**Eval Metric**: RAGAs (Retrieval-Augmented Generation Assessment) scoring
**Method Name**: RAGS4EIC (RAG-based Summarization AI for EIC)
**Modality**: Text (EIC documents, papers, data, institutional resources)

> arXiv 2024 | 2024 | Method | physics
#### 📌 한 줄 요약
전자-이온 충돌기(EIC) 실험 관련 문서·논문·데이터를 포괄한 벡터 데이터베이스를 구축하고, LLM으로 인용이 풍부한 요약을 생성하여 신규 협력자와 초기 경력 과학자의 대규모 EIC 기관 지식 접근을 지원하는 RAG 기반 요약 AI 에이전트이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 38개국 1,400명 이상 물리학자가 참여하는 EIC 협력체에서 방대한 기관 문서 탐색이 시간·노력 집약적
- 대규모 실험 협력에서 다수 워킹 그룹 간 정보 큐레이션 조율이 어려움

**이 시스템이 필요한 이유**
- 신규 협력자 및 초기 경력 과학자가 방대한 EIC 데이터셋·문서를 이해하는 데 드는 부담 경감 필요
- 협업적 참여를 장려하고 연구자 역량 강화를 위한 AI 기반 접근 도구 필요

#### 🔨 시스템 구성
2단계 접근법: (1) EIC 실험 정보 전체를 담은 포괄적 벡터 데이터베이스 쿼리, (2) LLM을 통해 사용자 쿼리와 검색된 데이터 기반으로 인용이 포함된 간결한 요약 생성. LangChain을 워크플로 기반으로 사용. 프롬프트 템플릿 기반 instruction-tuning으로 유연성·정확도 제공. Streamlit 웹 애플리케이션으로 배포.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 평가 방법 | RAGAs (RAG Assessment) 점수 |
| 지식 베이스 | EIC 실험 문서, 논문, 데이터 전체 |
| 배포 | Streamlit 웹 앱 (rags4eic-ai4eic.streamlit.app) |
| EIC 협력체 규모 | 1,400명+ 물리학자, 38개국 |

#### ⚠️ 한계점
- EIC 기관 문서에 특화되어 다른 실험 도메인으로의 직접 이전 제한
- 클라우드 호스팅 외부 지식 베이스 사용 → 데이터 프라이버시 우려 (후속 jat2026retrieval에서 로컬 배포로 해결)
- 미출판 사전 공개 데이터의 외부 전송 위험

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2403.15729](https://arxiv.org/abs/2403.15729)
- **웹 앱**: https://rags4eic-ai4eic.streamlit.app
- **소스코드**: https://github.com/ai4eic/EIC-RAG-Project
