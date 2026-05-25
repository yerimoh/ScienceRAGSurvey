---
title: "Alzheimer's Disease Neuroimaging Initiative (ADNI): clinical characterization"
bib_key: "petersen2010alzheimer"
year: 2010
domain: medical
type: dataset
venue: Neurology
paper_link: https://doi.org/10.1212/WNL.0b013e3181cb3e25
---
# Alzheimer's Disease Neuroimaging Initiative (ADNI): clinical characterization

petersen2010alzheimer | 2010 | Neurology | dataset | [medical] | [paper](https://doi.org/10.1212/WNL.0b013e3181cb3e25)

**DB**: ADNI (Alzheimer's Disease Neuroimaging Initiative)
**DB size**: 819명 등록 (정상 229명, MCI 398명, AD 192명)
**DB Open/Private**: Open (credentialed access via LONI)
**Modality**: Image (MRI, PET), Structured Table (CSF 바이오마커, 인지 평가)
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ADNI 포털 (adni.loni.usc.edu)

> Neurology | 2010 | dataset | medical

#### 📌 한 줄 요약
알츠하이머병 신경영상 이니셔티브(ADNI)의 임상적 특성화 논문으로, 정상 노화·경도 인지장애·알츠하이머병 코호트에서 신경영상 및 화학 바이오마커의 임상적 진행 지표를 평가한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 신경영상 측정값과 화학 바이오마커(CSF)의 임상적 유용성을 종단적으로 평가할 대규모 표준화 데이터 부재
- 알츠하이머병 임상 시험에서 바이오마커 활용을 위한 근거 데이터 미흡

**이 시스템이 필요한 이유**
- MCI와 AD 진행 예측을 위한 신경영상·CSF 바이오마커 통합 평가 필요
- 임상 시험 설계에 활용 가능한 표준화된 다기관 코호트 구축

#### 🔨 시스템 구성
북미 다기관 연구로 정상 인지(229명), 경도 인지장애(MCI, 398명), 경증 알츠하이머병(AD, 192명) 총 819명을 기준선 및 12개월 추적 관찰. MRI, FDG-PET, CSF Aβ-42/tau 측정, ADAS-Cog 등 표준 인지기능 검사 시행. MCI의 12개월 치매 전환율 16.5%/년. CSF Aβ-42가 세 그룹을 유의하게 구별하고 12개월 인지 변화를 예측.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| ADNI 포털 | https://adni.loni.usc.edu — 등록 및 데이터 사용 계약 후 접근 |
| LONI | Laboratory of Neuro Imaging, USC |

#### 📤 제공 데이터 형식
- MRI 뇌 영상 (T1-weighted, structural)
- PET 영상 (FDG-PET)
- CSF 바이오마커 (Aβ-42, total tau, p-tau)
- 표준화 인지기능 검사 점수 (ADAS-Cog, MMSE)
- 인구통계 및 임상 정보

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 등록 피험자 수 | **819명** |
| 정상 인지 피험자 | **229명** |
| MCI 피험자 | **398명** |
| AD 피험자 | **192명** |
| MCI 치매 전환율 | **16.5%/년** |
| 추적 기간 | **12개월** |
| MCI 항치매 치료 비율 | **약 50%** |

#### ⚠️ 한계점
- 기준선 특성 기술 논문으로 장기 종단 데이터 미포함
- MCI 피험자 약 50%가 항치매제 복용 — 바이오마커 해석 교란 가능
- 주로 백인·고학력·우편 코드 선택 편향 가능성

## 관련 정보
- **논문**: [Alzheimer's Disease Neuroimaging Initiative (ADNI): clinical characterization](https://doi.org/10.1212/WNL.0b013e3181cb3e25)
