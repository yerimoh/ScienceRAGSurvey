---
title: "bioRxiv: the preprint server for biology"
bib_key: "sever2019biorxiv"
year: 2019
domain: bio
type: dataset
venue: bioRxiv (Cold Spring Harbor Laboratory)
paper_link: https://doi.org/10.1101/833400
---
# bioRxiv: the preprint server for biology

sever2019biorxiv | 2019 | bioRxiv (Cold Spring Harbor Laboratory) | dataset | [bio] | [paper](https://doi.org/10.1101/833400)

**DB**: bioRxiv preprint server
**DB size**: 310,000+ manuscripts (논문 기재 시점)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: bioRxiv OAI-PMH / REST API

> bioRxiv (Cold Spring Harbor Laboratory) | 2019 | dataset | bio
#### 📌 한 줄 요약
Cold Spring Harbor Laboratory가 2013년 시작한 생명과학 분야 프리프린트 서버로, 논문 작성 시점 기준 31만 편 이상을 수록하며 피어리뷰 전에 연구를 즉시 공개함으로써 과학 커뮤니케이션을 가속화한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 전통적인 학술 출판 과정은 수개월~수년의 동료 심사 기간으로 인해 연구 성과 공유가 지연됨
- 연구자들은 초고 단계에서 광범위한 피드백을 받을 창구가 없었음
- 연구비 생산성 증빙을 위한 조기 공개 필요성 증가

**이 시스템이 필요한 이유**
- 논문 저널 제출·심사와 독립적으로 즉시 공개하여 광범위한 독자로부터 피드백 수집
- 연구 우선권을 공식 출판 이전에 확립 가능
- 저널 정책과의 통합(Easy Journal Transfer)으로 저자 부담 최소화

#### 🔨 시스템 구성
Cold Spring Harbor Laboratory(CSHL)가 운영하는 비영리 오픈 프리프린트 저장소. 저자가 제출하면 스크리닝(비과학적 내용·표절 등) 후 OAI-PMH 인터페이스를 통해 전문 공개. 생물학 전 분야(진화생물학, 유전체학, 전산생물학, 신경과학, 세포·발생생물학 등) 수록. 자매 서버 medRxiv(임상의학)와 함께 Cold Spring Harbor Laboratory 운영. 분야별 Subject Category는 저자가 직접 지정.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| OAI-PMH API | 메타데이터 및 전문 배치 수집 지원 |
| 개별 DOI | 각 프리프린트는 10.1101/XXXXXX 형식 DOI 부여 |
| RSS/Atom 피드 | 분야별 신규 프리프린트 구독 가능 |
| 전문 PDF/HTML | 직접 다운로드 가능 (오픈 액세스) |

#### 📤 제공 데이터 형식
- 논문 전문 (PDF 및 HTML)
- 구조화된 메타데이터: 제목, 저자, 초록, 날짜, DOI, subject category
- 버전 이력: 동일 프리프린트의 여러 버전 추적 가능
- 저널 연동 링크: 최종 게재 저널 정보 (가능한 경우)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 수록 프리프린트 | **310,000+** (2019년 11월 시점) |
| 월간 페이지뷰 | **약 10,000,000** |
| 서비스 시작 | **2013년** |
| 운영 기관 | Cold Spring Harbor Laboratory (비영리) |
| 조기 제출 비율 (저널 제출 전) | **30%** |
| 저널 제출 시점 제출 비율 | **55%** |

#### ⚠️ 한계점
- **피어리뷰 미완료**: 수록 논문은 정식 동료 심사를 거치지 않아 과학적 신뢰성 보장 없음
- **품질 편차**: 스크리닝은 기초적 수준(비과학적 내용 필터링)이며 방법론·결과 검증 없음
- **버전 다수**: 동일 연구가 여러 버전으로 존재하여 최신 버전 추적 필요
- **생명과학 한정**: 물리·화학·지구과학 등 타 분야는 별도 서버(arXiv, ChemRxiv, EarthArXiv) 이용 필요

## 관련 정보
- **논문**: [https://doi.org/10.1101/833400](https://doi.org/10.1101/833400)
