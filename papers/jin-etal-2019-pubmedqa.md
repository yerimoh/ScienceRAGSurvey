---
title: "PubMedQA: A Dataset for Biomedical Research Question Answering"
bib_key: "jin-etal-2019-pubmedqa"
year: 2019
domain: medical
type: benchmark
venue: EMNLP-IJCNLP 2019
paper_link: https://aclanthology.org/D19-1259/
---
# PubMedQA: A Dataset for Biomedical Research Question Answering

jin-etal-2019-pubmedqa | 2019 | EMNLP-IJCNLP 2019 | benchmark | [medical] | [paper](https://aclanthology.org/D19-1259/)

**DB**: PubMedQA (biomedical research QA from PubMed abstracts)
**DB size**: 1k expert-annotated + 61.2k unlabeled + 211.3k artificially generated QA instances
**DB Open/Private**: Open (https://pubmedqa.github.io)
**Modality**: Text
**Retriever**: N/A (벤치마크)
**Eval Task**: Biomedical research question answering (Yes/No/Maybe)
**Eval Metric**: Accuracy
**Method Name**: PubMedQA

> EMNLP-IJCNLP 2019 | 2019 | benchmark | medical
#### 📌 한 줄 요약
PubMed 초록에서 수집한 1k 전문가 주석, 61.2k 미주석, 211.3k 인공 생성 QA 인스턴스로 구성된 생물의학 연구 질문 응답 벤치마크로, 정량적 내용을 포함한 추론이 필요한 최초의 QA 데이터셋이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 기존 생물의학 QA 데이터셋은 정량적 수치 추론(quantitative reasoning)이 필요하지 않았음
- PubMed 초록의 결론 부분을 활용한 체계적 QA 구성 방법론이 없었음

**이 시스템이 필요한 이유**
- 의학 연구에서 "~이 효과가 있는가?"와 같은 Yes/No/Maybe 형태의 질문에 답하는 시스템 평가 필요
- 임상 의사결정 지원을 위한 추론 능력 벤치마크 필요

#### 🔨 시스템 구성
각 PubMedQA 인스턴스는 (1) 연구 논문 제목 또는 파생 질문, (2) 결론을 제외한 초록 (컨텍스트), (3) 초록의 결론 (long answer), (4) Yes/No/Maybe 요약 답변으로 구성된다. 전문가 주석 1k 인스턴스는 생물의학 전문가가 직접 레이블링하였으며, 인공 생성 211.3k 인스턴스는 자동화 파이프라인으로 생성되었다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 전문가 주석 | 1,000개 |
| 미주석 | 61,200개 |
| 인공 생성 | 211,300개 |
| 최고 모델 성능 | BioBERT multi-phase fine-tuning: 68.1% |
| 인간 단일 성능 | 78.0% |
| 다수결 기준선 | 55.2% |

#### ⚠️ 한계점
- Yes/No/Maybe 3-class에 국한되어 개방형 답변 평가 불가
- 초록 기반이므로 전문 도메인 지식 없이 답하기 어려운 질문 포함
- 인공 생성 인스턴스의 품질이 전문가 주석에 비해 낮을 수 있음

## 관련 정보
- **논문**: [https://aclanthology.org/D19-1259/](https://aclanthology.org/D19-1259/)
- **데이터셋**: https://pubmedqa.github.io
