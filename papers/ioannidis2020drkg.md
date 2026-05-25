---
title: "DRKG - Drug Repurposing Knowledge Graph for COVID-19"
bib_key: "ioannidis2020drkg"
year: 2020
domain: chem
type: dataset
venue: arXiv preprint
paper_link: https://arxiv.org/abs/2010.09600
---
# DRKG - Drug Repurposing Knowledge Graph for COVID-19

ioannidis2020drkg | 2020 | arXiv preprint | dataset | [chem] | [paper](https://arxiv.org/abs/2010.09600)

**DB**: DRKG (Drug Repurposing Knowledge Graph)
**DB size**: 97,238 엔티티, 5,874,261 트리플 (6개 기존 DB 통합)
**DB Open/Private**: Open
**Modality**: ['Structured', 'Network']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: DRKG (지식 그래프 완성 기반 약물 재목적화)

> arXiv preprint | 2020 | dataset | chem
#### 📌 한 줄 요약
DRKG는 COVID-19 약물 재목적화를 위해 DrugBank, Hetionet, GNBR, String, IntAct, DGIdb 등 6개 DB를 통합한 생물의학 지식 그래프로, 지식 그래프 임베딩 기반 후보 약물 발굴을 지원한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- COVID-19에 특화된 통합 약물 재목적화 지식 그래프가 없었음
- 기존 생물의학 DB들이 별도로 존재하여 교차 자원 분석이 어려웠음
**이 시스템이 필요한 이유**
- 팬데믹 대응을 위한 신속한 약물 후보 도출 필요
- 지식 그래프 완성(KGC) 방법으로 기존에 알려지지 않은 약물-타겟 관계 예측

#### 🔨 시스템 구성
DrugBank, Hetionet, GNBR, String, IntAct, DGIdb 등 6개 생물의학 DB를 통합한다. 엔티티 유형: 약물, 유전자, 질환, 화합물, 생물학적 과정, 해부학 구조, 세포 성분, 분자 기능 등. TransE, RotatE 등 KGE 모델로 약물 재목적화 후보 스코어링.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| GitHub | DRKG 그래프 데이터 및 임베딩 공개 |
| 직접 다운로드 | 노드·엣지 TSV 파일 |

#### 📤 제공 데이터 형식
- 지식 그래프 트리플 (head, relation, tail)
- KGE 임베딩 벡터
- 약물-타겟 예측 결과

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 엔티티 | 97,238 |
| 트리플 | 5,874,261 |
| 통합 DB | 6개 |

#### ⚠️ 한계점
- COVID-19 대응 목적으로 구축되어 다른 질환 영역은 커버리지 불균등
- 통합 과정에서 엔티티 정렬 오류 가능성
- 미심사(preprint) 논문 기반으로 방법론 검증이 제한적

## 관련 정보
- **논문**: [DRKG - Drug Repurposing Knowledge Graph for COVID-19](https://arxiv.org/abs/2010.09600)
