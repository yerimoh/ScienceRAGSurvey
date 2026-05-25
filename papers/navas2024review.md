---
title: "Review of Particle Physics"
bib_key: "navas2024review"
year: 2024
domain: physics
type: dataset
venue: Physical Review D
paper_link: https://doi.org/10.1103/PhysRevD.110.030001
---
# Review of Particle Physics

navas2024review | 2024 | Physical Review D | dataset | [physics] | [paper](https://doi.org/10.1103/PhysRevD.110.030001)

**DB**: Review of Particle Physics (RPP) — Particle Data Group (PDG)
**DB size**: 2,717 new measurements from 869 papers (2024판 기준); 120개 리뷰 포함, 2권 구성
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PDG 데이터 접근: pdg.lbl.gov

> Physical Review D | 2024 | dataset | physics
#### 📌 한 줄 요약
입자데이터그룹(Particle Data Group)이 격년 발행하는 입자물리학의 표준 참조 편람으로, 게이지 보손·힉스 보손·렙톤·쿼크·중간자·중입자의 실측 특성을 평가·평균·요약하며, 고에너지물리학에서 가장 많이 인용되는 단일 참조 저작이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 입자물리학은 전 세계 수십 개 실험 그룹이 독립적으로 동일한 입자 특성을 측정하는 구조
- 개별 측정값들을 일관된 방식으로 평가·평균하는 중앙 집중 큐레이션 필요
- 가속기 실험 결과와 우주론·천체물리학 데이터를 통합하는 종합 참조 부재

**이 시스템이 필요한 이유**
- 측정 불확도를 포함한 표준 평균값 제공으로 전 세계 연구자의 공통 참조점 확보
- 가상 입자(초대칭 입자, 중성미자 질량, 암흑 물질) 탐색 결과도 통합 수록
- 이론 리뷰(힉스 보손 물리학, 초대칭, 대통일 이론, 중성미자 혼합 등)와 실험 데이터 병합 제공

#### 🔨 시스템 구성
PDG는 Lawrence Berkeley National Laboratory(LBNL)가 주도하고 전 세계 입자물리학자들이 참여하는 국제 협력체이다. 매 2년마다(홀수 연도) 최신 측정 데이터를 수집·평가하여 물리량의 세계 평균값과 오차를 산출한다. 2024판(Physical Review D 110, 030001)은 Summary Tables(제1권)와 Particle Listings 및 추가 리뷰(제2권)로 구성된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹사이트 | pdg.lbl.gov — 온라인 데이터 테이블, 입자 요약 |
| PDF/인쇄본 | Physical Review D 게재 (오픈 액세스) |
| 데이터 파일 | 구조화된 데이터 파일 다운로드 지원 |

#### 📤 제공 데이터 형식
- 입자 특성 요약 테이블 (질량, 수명, 붕괴 분기비, 자기 모멘트 등)
- 측정값 목록 (각 실험별 개별 측정값 + 가중 평균)
- 120개 이상의 리뷰 논문 (이론 및 실험 주제)
- 가속기·검출기 기술 개요
- 통계·확률 방법론 리뷰

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 2024판 신규 측정값 | **2,717** 건 (869편 논문 기반) |
| 수록 리뷰 수 | **120** 개 (대부분 업데이트) |
| 권 구성 | **2권** (제1권: Summary Tables + 97개 리뷰; 제2권: Particle Listings + 23개 리뷰) |
| 발행 주기 | 격년 (짝수 연도: 전자판 업데이트, 홀수 연도: 전체 출판) |
| 학술지 | Physical Review D vol.110, no.3 (2024) |

#### ⚠️ 한계점
- 큐레이션된 참조 편람으로서 1차 측정 논문이 아닌 2차 평균 데이터 제공
- 격년 발행 주기로 인해 최신 실험 결과 반영에 시간 지연 존재
- 평균 계산 방법론(PDG scaling factor 등)이 표준이지만 세부 측정별 맥락 손실 가능
- 텍스트 중심 RAG에서 수식·단위 혼재로 자동 파싱 어려움

## 관련 정보
- **논문**: [Review of Particle Physics (Phys. Rev. D 110, 030001, 2024)](https://doi.org/10.1103/PhysRevD.110.030001)
- **PDG 웹사이트**: [pdg.lbl.gov](https://pdg.lbl.gov)
