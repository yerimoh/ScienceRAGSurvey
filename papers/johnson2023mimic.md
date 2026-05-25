---
title: "MIMIC-IV, a freely accessible electronic health record dataset"
bib_key: "johnson2023mimic"
year: 2023
domain: medical
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/s41597-022-01899-x
---
# MIMIC-IV, a freely accessible electronic health record dataset

johnson2023mimic | 2023 | Scientific Data | dataset | [medical] | [paper](https://doi.org/10.1038/s41597-022-01899-x)

**DB**: MIMIC-IV (Medical Information Mart for Intensive Care IV)
**DB size**: 431,231 병원 입원; 180,733 고유 환자; ICU 입원 73,181건; 기간 2008–2019
**DB Open/Private**: Open (credentialed access via PhysioNet)
**Modality**: Text, Structured Table (EHR)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PhysioNet / MIMIC-IV portal

> Scientific Data | 2023 | dataset | medical

#### 📌 한 줄 요약
Beth Israel Deaconess Medical Center의 전자의무기록에서 추출한 2008–2019년 데이터를 기반으로, 환자 측정값·처방·진단·처치·치료·비식별 임상 노트를 포함하는 공개 EHR 데이터베이스.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- MIMIC-III는 2001–2012년 데이터로 노후화; 현대 임상 관행 반영 불가
- 기존 공개 데이터셋은 단일 모달리티(임상 관찰)에 한정
- 연구자 접근성 장벽이 높아 임상 연구 속도 저하

**이 시스템이 필요한 이유**
- 현대 디지털 의료 환경(2008–2019)을 반영하는 최신 EHR 데이터 필요
- 전자 의약품 투여 기록 등 새로운 정밀 디지털 정보원 통합
- 광범위한 연구 및 교육 활용을 위한 개방형 플랫폼 필요

#### 🔨 시스템 구성
BIDMC의 2008–2019년 EHR 데이터를 모듈화 구조로 제공. 병원 입원 431,231건(고유 환자 180,733명), ICU 입원 73,181건(고유 환자 50,920명)을 포함. 환자 측정값, 주문, 진단, 처치, 치료, 비식별 자유형식 임상 노트 제공. 병원 모듈과 ICU 모듈로 분리된 스키마 구조.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| PhysioNet 포털 | https://physionet.org/content/mimiciv/ — 자격 증명 후 무료 다운로드 |
| DOI | https://doi.org/10.1038/s41597-022-01899-x |

#### 📤 제공 데이터 형식
- 정형 테이블 (CSV): 활력징후, 검사 결과, 의약품, 처치 코드
- 비정형 텍스트: 비식별 임상 노트 (퇴원 요약, 방사선 보고서)
- ICD-10 진단/시술 코드 (MIMIC-III 대비 업그레이드)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 병원 입원 건수 | **431,231** |
| 고유 환자 수 (병원) | **180,733** |
| ICU 입원 건수 | **73,181** |
| 고유 환자 수 (ICU) | **50,920** |
| 데이터 기간 | **2008–2019** |
| 평균 연령 (병원) | **58.8세 (SD 19.2)** |
| 평균 연령 (ICU) | **64.7세 (SD 16.9)** |
| 여성 비율 (병원) | **52.2%** |

#### ⚠️ 한계점
- 단일 기관(BIDMC) 데이터로 일반화 제한
- 접근에 자격 증명 절차 필요
- 임상 노트는 비식별화로 일부 정보 손실

## 관련 정보
- **논문**: [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x)
