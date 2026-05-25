---
title: "BioASQ-QA: A manually curated corpus for Biomedical Question Answering"
bib_key: "krithara2023bioasq"
year: 2023
domain: medical, bio
type: benchmark
venue: Scientific Data
paper_link: https://doi.org/10.1038/s41597-023-02068-4
---
# BioASQ-QA: A manually curated corpus for Biomedical Question Answering

krithara2023bioasq | 2023 | Scientific Data | benchmark | [medical, bio] | [paper](https://doi.org/10.1038/s41597-023-02068-4)

**DB**: BioASQ QA benchmark (Task B)
**DB size**: 4,721 expert-annotated QA pairs (continuously extended since 2012)
**DB Open/Private**: Open
**Modality**: Text
**Retriever**: N/A (벤치마크)
**Eval Task**: Biomedical QA (exact answer + ideal summary answer)
**Eval Metric**: F1, MAP, MRR, ROUGE (ideal answers)
**Method Name**: BioASQ Challenge (Task A: MeSH indexing, Task B: QA)

> Scientific Data | 2023 | benchmark | medical · bio
#### 📌 한 줄 요약
생물의학 전문가가 2012년부터 연간 500여 개씩 직접 작성한 4,721개 질문-답변 쌍으로 구성된 BioASQ Task B 벤치마크로, exact answer와 paragraph-sized ideal answer를 모두 포함하는 복합 생물의학 QA 데이터셋이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 기존 QA 벤치마크는 실제 생물의학 전문가의 정보 니즈를 반영하지 못함
- exact answer 외에 요약형(ideal) answer를 포함한 벤치마크가 없었음

**이 시스템이 필요한 이유**
- PubMed에 분당 2편 이상 논문이 등록되는 환경에서 정확하고 빠른 생물의학 정보 접근 시스템이 필요
- IR, passage retrieval, NLG, multi-document summarization을 통합 평가하는 벤치마크 필요

#### 🔨 시스템 구성
BioASQ 인프라는 전문가 주석 도구, 시스템 평가 도구, 벤치마크 저장소, 평가 서비스를 포함한다. Task B에서 각 질문에 대해 관련 문서, 스니펫, 개념, RDF 트리플, exact answer(예: 질병명), ideal answer(단락형 요약)를 제공하도록 설계된다. 2012년부터 매년 챌린지를 운영하며 100개 이상의 기관이 참여하였다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 총 QA 쌍 | 4,721개 (2023년 기준) |
| 연간 신규 질문 | ~500개 (전문가 작성) |
| 참여 기관 수 | 전 세계 100개 이상 (모든 대륙) |
| 운영 기간 | 2012년~현재 |
| 질문 유형 | Yes/No, Factoid, List, Summary |

#### ⚠️ 한계점
- 영어 질문만 포함 (다국어 지원 없음)
- 연간 업데이트 주기로 인해 최신 문헌 반영에 시간 지연 존재
- Task A (MeSH 인덱싱)와 Task B (QA)가 분리되어 있어 통합 평가 어려움

## 관련 정보
- **논문**: [https://doi.org/10.1038/s41597-023-02068-4](https://doi.org/10.1038/s41597-023-02068-4)
- **공식 웹사이트**: http://bioasq.org
