---
title: "MIMIC-III, a freely accessible critical care database"
bib_key: "johnson2016mimic"
year: 2016
domain: medical
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/sdata.2016.35
---
# MIMIC-III, a freely accessible critical care database

johnson2016mimic | 2016 | Scientific Data | dataset | [medical] | [paper](https://doi.org/10.1038/sdata.2016.35)

**DB**: MIMIC-III (Medical Information Mart for Intensive Care III)
**DB size**: 53,423 distinct hospital admissions (adults, 2001–2012); 38,597 distinct adult patients; 7,870 neonates (2001–2008); 49,785 hospital admissions
**DB Open/Private**: Open (credentialed access via PhysioNet)
**Modality**: Text, Structured Table (EHR)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PhysioNet / MIMIC-III portal

> Scientific Data | 2016 | dataset | medical

#### 📌 한 줄 요약
Beth Israel Deaconess Medical Center의 중환자실 입원 데이터를 포함한 대규모 단일 기관 임상 데이터베이스로, 활력징후·의약품·검사 결과·영상 보고서·임상 기록 등을 자유롭게 접근 가능하게 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 임상 연구에 활용 가능한 공개 ICU 데이터베이스 부재
- 기존 데이터는 병원 내부 아카이브에 묶여 있어 연구 접근 불가
- 단편적 데이터셋은 규모가 작고 특정 연구 목적에 한정

**이 시스템이 필요한 이유**
- 학술·산업 연구, 품질 향상, 의학 교육을 위한 범용 플랫폼 필요
- ICU 환자의 임상 경과 및 치료 반응을 장기적으로 분석할 데이터 필요
- 재현 가능한 임상 연구를 위한 표준화된 개방형 데이터 필요

#### 🔨 시스템 구성
Beth Israel Deaconess Medical Center ICU의 2001–2012년 데이터를 통합한 단일 기관 EHR 데이터베이스. 성인 환자 53,423건의 중환자실 입원과 신생아 7,870건을 포함하며, 38,597명의 고유 성인 환자 데이터를 수록. 활력징후, 의약품, 검사 측정값, care provider 차트 기록, 체액 균형, 시술 코드, 진단 코드, 영상 보고서, 재원 기간, 생존 데이터 등을 포함. ICU 재원 기간 중앙값 2.1일. PhysioNet을 통해 자격 증명 후 무료 접근 가능.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| PhysioNet 포털 | https://physionet.org/content/mimiciii/ — 자격 증명 후 무료 다운로드 |
| DOI | https://doi.org/10.13026/C2XW26 |

#### 📤 제공 데이터 형식
- 정형 테이블 (CSV): 활력징후, 검사 결과, 의약품, 청구 코드
- 비정형 텍스트: 임상 노트, 영상 보고서, 퇴원 요약
- ICD-9 진단/시술 코드

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 성인 ICU 입원 건수 | **53,423** |
| 고유 성인 환자 수 | **38,597** |
| 병원 입원 건수 | **49,785** |
| 신생아 입원 건수 | **7,870** |
| 데이터 기간 (성인) | **2001–2012** |
| 성인 환자 중앙 연령 | **65.8세** |
| 남성 비율 | **55.9%** |
| 원내 사망률 | **11.5%** |
| ICU 재원 기간 중앙값 | **2.1일** |

#### ⚠️ 한계점
- 단일 기관(BIDMC) 데이터로 일반화 제한
- 접근에 자격 증명 절차 필요 (완전 개방 아님)
- ICD-9 코드 기반으로 최신 코딩 체계와 불일치

## 관련 정보
- **논문**: [MIMIC-III, a freely accessible critical care database](https://doi.org/10.1038/sdata.2016.35)
