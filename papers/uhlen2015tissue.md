---
title: "Tissue-based map of the human proteome"
bib_key: "uhlen2015tissue"
year: 2015
domain: medical, bio
type: dataset
venue: Science
paper_link: https://doi.org/10.1126/science.1260419
---
# Tissue-based map of the human proteome

uhlen2015tissue | 2015 | Science | dataset | [medical, bio] | [paper](https://doi.org/10.1126/science.1260419)

**DB**: Human Protein Atlas (HPA)
**DB size**: 32개 조직 및 장기; 추정 단백질 코딩 유전자 90% 이상 검출
**DB Open/Private**: Open (proteinatlas.org)
**Modality**: Image (면역조직화학), Genomic (전사체), Structured Table (단백질 발현 데이터)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Human Protein Atlas (proteinatlas.org)

> Science | 2015 | dataset | medical, bio

#### 📌 한 줄 요약
32개 인체 조직·장기에서 정량적 전사체학과 조직 마이크로어레이 기반 면역조직화학을 통합하여 단백질 공간 발현 지도를 단세포 수준까지 구축하고, 인간 단백질체의 90% 이상을 검출한 인터랙티브 웹 데이터베이스.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 조직 및 장기 수준의 단백질 공간적 위치 정보 부재
- 전사체 데이터만으로는 단백질 발현 패턴과 세포 내 위치 파악 불가
- 인간 분비체·막 단백질체·암 단백질체의 통합 자원 없음

**이 시스템이 필요한 이유**
- 인간 생물학 및 질환 이해를 위한 단백질 공간 발현 지도 필요
- 약물 표적, 바이오마커 발굴을 위한 통합 오믹스 플랫폼 필요

#### 🔨 시스템 구성
KTH Royal Institute of Technology(스웨덴) 주도 통합 오믹스 접근법. 32개 조직·장기에서 정량적 전사체학(mRNA) + 조직 마이크로어레이 기반 면역조직화학 통합. 단세포 수준의 단백질 공간 위치 파악. 인간 분비체, 막 단백질체, 약물 가능 단백질체, 암 단백질체, 대사 기능 탐색. 전체 데이터는 인터랙티브 웹 기반 데이터베이스(proteinatlas.org)로 통합 제공.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| Human Protein Atlas 포털 | https://www.proteinatlas.org — 무료 공개 접근 |
| DOI | https://doi.org/10.1126/science.1260419 |

#### 📤 제공 데이터 형식
- 면역조직화학 영상 (조직 마이크로어레이)
- RNA 발현 데이터 (TPM, 조직별)
- 단백질 발현 수준 (조직/세포 유형별)
- 항체 특이도 정보

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 분석 조직/장기 수 | **32개** |
| 검출된 단백질 코딩 유전자 비율 | **90% 이상** |

#### ⚠️ 한계점
- 항체 기반 검출법으로 교차 반응성 가능
- 단백질 발현량은 반정량적 수준
- 세포주 및 일부 희귀 조직 미포함

## 관련 정보
- **논문**: [Tissue-based map of the human proteome](https://doi.org/10.1126/science.1260419)
