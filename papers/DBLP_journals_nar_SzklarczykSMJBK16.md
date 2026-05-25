---
title: "STITCH 5: augmenting protein-chemical interaction networks with tissue and affinity data"
bib_key: "DBLP:journals/nar/SzklarczykSMJBK16"
year: 2016
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkv1277
---
# STITCH 5: augmenting protein-chemical interaction networks with tissue and affinity data

DBLP:journals/nar/SzklarczykSMJBK16 | 2016 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkv1277)

**DB**: STITCH 5 (Search Tool for Interacting Chemicals)
**DB size**: 430,000 화합물 통합, 다수 유기체 커버
**DB Open/Private**: Open
**Modality**: ['Structured', 'Network']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: STITCH web interface + API (stitch.embl.de)

> Nucleic Acids Research | 2016 | dataset | chem
#### 📌 한 줄 요약
STITCH 5는 다양한 DB·문헌·예측 방법의 단백질-화학물질 상호작용 정보를 43만 개 화합물에 대해 단일 네트워크로 통합하고, 조직 특이적 필터링 및 결합 친화도 네트워크 뷰를 신규 지원한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 단백질-화학물질 상호작용 정보가 여러 DB, 문헌, 예측 방법에 분산되어 통합 개요 파악이 어려웠음
- 조직 특이적 상호작용 필터링 기능이 없었음
**이 시스템이 필요한 이유**
- 약물의 다중 타겟 효과(polypharmacology) 및 부작용 예측을 위한 통합 네트워크 자원 필요
- 단백질 공간 발현 패턴을 고려한 상호작용 분석 필요

#### 🔨 시스템 구성
화학물질-단백질 상호작용을 DB, 실험 데이터, 텍스트 마이닝, 예측 방법에서 통합한다. Release 5에서 특정 조직의 단백질·화합물만 필터링하는 조직 특이적 기능 추가. 결합 친화도를 네트워크 뷰에서 직접 시각화하는 새 기능 제공. 전체 데이터 다운로드, 광범위한 API, 재설계된 웹 인터페이스 지원.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | stitch.embl.de 네트워크 검색·시각화 |
| 전체 다운로드 | 상호작용 네트워크 전체 다운로드 |
| API | 광범위한 프로그래밍 인터페이스 |

#### 📤 제공 데이터 형식
- 단백질-화합물 상호작용 네트워크 (점수 기반)
- 조직 특이적 필터링 데이터
- 결합 친화도 값

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 통합 화합물 | 430,000 |

#### ⚠️ 한계점
- 예측 기반 상호작용 포함으로 실험적 미검증 데이터 구분 주의 필요
- 조직 특이성 데이터의 완전성이 유기체·조직별로 편차 존재

## 관련 정보
- **논문**: [STITCH 5: augmenting protein-chemical interaction networks](https://doi.org/10.1093/nar/gkv1277)
