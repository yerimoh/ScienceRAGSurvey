---
title: "Repurposing non-pharmacological interventions for Alzheimer's disease through link prediction on biomedical literature"
bib_key: "xiao2024repurposing"
year: 2024
domain: medical
type: Method
venue: Scientific Reports
paper_link: https://doi.org/10.1038/s41598-024-59537-6
---
# Repurposing non-pharmacological interventions for Alzheimer's disease through link prediction on biomedical literature

xiao2024repurposing | 2024 | Scientific Reports | Method | [medical] | [paper](https://doi.org/10.1038/s41598-024-59537-6)

**Retriever**: Literature-based knowledge graph construction (biomedical literature retrieval)
**Eval Task**: Link prediction-based drug/intervention repurposing for Alzheimer's disease
**Eval Metric**: Downstream task accuracy (repurposing candidate validation)
**Method Name**: Literature-based link prediction for AD repurposing
**Modality**: Text (biomedical literature)

> Scientific Reports | 2024 | Method | medical
#### 📌 한 줄 요약
생물의학 문헌에서 구축한 지식 그래프의 링크 예측을 통해 알츠하이머병에 대한 비약리학적 중재법(non-pharmacological interventions) 후보를 재목적화(repurposing)하는 시스템으로, 문헌 검색 기반의 약한 검증(weakly-verified) 가설 생성 사례를 제시한다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 알츠하이머 약물 발굴은 높은 실패율과 긴 개발 기간으로 비약리학적 중재법 탐색이 부각
- 대규모 생물의학 문헌에 분산된 지식을 체계적으로 연결하는 시스템이 부재

**이 시스템이 필요한 이유**
- 기존 약물 재목적화 방법은 주로 약리학적 화합물에 집중; 비약리학적 중재(운동, 인지 훈련 등)에 대한 체계적 평가 필요
- 강한 외부 검증자(docking, 데이터베이스 직접 조회) 없이 문헌 유도 가설을 생성하는 평가 프레임워크 필요

#### 🔨 시스템 구성
생물의학 문헌에서 엔티티(질병, 중재법, 유전자, 생물학적 과정)와 관계를 추출하여 지식 그래프를 구축한다. 그래프 기반 링크 예측 모델을 통해 알츠하이머와 비약리학적 중재법 간의 잠재적 연결(후보 가설)을 생성한다. 평가는 기존 문헌 기반 근거와의 비교로 수행된다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 출판 저널 | Scientific Reports, vol.14, p.8693, 2024 |
| 평가 방식 | 다운스트림 태스크 정확도, 전문가 검증 |
| 검증 유형 | 약한 검증 (weak verification — 문헌 기반) |
| 적용 도메인 | 알츠하이머 비약리학적 중재법 재목적화 |

#### ⚠️ 한계점
- 강력한 외부 검증자(실험, DFT, 데이터베이스 직접 조회)가 없어 신규성과 타당성이 주요 평가 부담을 짐
- 문헌 품질 및 편향에 평가 결과가 민감
- 예측된 연결의 실험적 검증이 별도로 필요

## 관련 정보
- **논문**: [https://doi.org/10.1038/s41598-024-59537-6](https://doi.org/10.1038/s41598-024-59537-6)
- **PubMed**: https://pubmed.ncbi.nlm.nih.gov/38615044/
