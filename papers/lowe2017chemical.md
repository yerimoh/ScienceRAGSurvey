---
title: "Chemical reactions from US patents (1976-Sep2016)"
bib_key: "lowe2017chemical"
year: 2017
domain: chem
type: dataset
venue: figshare
paper_link: https://figshare.com/articles/dataset/Chemical_reactions_from_US_patents_1976-Sep2016_/5104873
---
# Chemical reactions from US patents (1976-Sep2016)

lowe2017chemical | 2017 | figshare | dataset | [chem] | [paper](https://figshare.com/articles/dataset/Chemical_reactions_from_US_patents_1976-Sep2016_/5104873)

**DB**: USPTO 화학 반응 데이터셋 (Lowe 2017)
**DB size**: 1976~2016년 9월 US 특허에서 추출한 화학 반응 (구체적 수치는 figshare 기재)
**DB Open/Private**: Open (CC0)
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: USPTO 반응 데이터셋 (텍스트 마이닝·구조 추출)

> figshare | 2017 | dataset | chem
#### 📌 한 줄 요약
1976년부터 2016년 9월까지의 US 특허에서 텍스트 마이닝으로 추출한 화학 반응 데이터셋으로, 컴퓨터 지원 합성 계획 및 반응 예측 모델의 표준 훈련 자원으로 광범위하게 활용된다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 화학 반응 데이터가 특허 전문에 비구조화 텍스트로 매립되어 있어 기계 학습에 활용 어려웠음
- 대규모 반응 예측 모델 훈련을 위한 공개 데이터셋이 부재했음
**이 시스템이 필요한 이유**
- 합성 경로 예측(retrosynthesis), 반응 조건 예측 등 계산 화학 모델 개발을 위한 대규모 반응 코퍼스 필요
- 특허는 저널보다 훨씬 많은 합성 반응 정보를 담고 있음

#### 🔨 시스템 구성
ChemDataExtractor, OSCAR4 등 텍스트 마이닝 도구로 US 특허 전문에서 반응물·시약·생성물 구조를 추출한다. SMILES 형식으로 반응을 인코딩. 반응 엔티티 인식 및 구조 파싱 파이프라인 포함.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| figshare 다운로드 | CC0 라이선스 공개 다운로드 |

#### 📤 제공 데이터 형식
- 반응 SMILES (반응물>시약>생성물)
- XML 형식 반응 데이터
- 특허 식별자 메타데이터

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 수록 기간 | 1976년 ~ 2016년 9월 |
| 데이터 출처 | US 특허 전문 |

#### ⚠️ 한계점
- 특허 텍스트 마이닝 기반이므로 구조 추출 오류 포함 가능
- 특허 기재 반응이 실제 최적 조건과 다를 수 있음
- 반응 수율, 순도 등 정량적 데이터 부재

## 관련 정보
- **논문**: [Chemical reactions from US patents (1976-Sep2016)](https://figshare.com/articles/dataset/Chemical_reactions_from_US_patents_1976-Sep2016_/5104873)
