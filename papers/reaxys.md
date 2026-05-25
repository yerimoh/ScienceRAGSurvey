---
title: "Reaxys"
bib_key: "reaxys"
year: 2009
domain: chem
type: dataset
venue: Elsevier (misc)
paper_link: https://www.reaxys.com
---
# Reaxys

reaxys | 2009 | Elsevier | dataset | [chem] | [paper](https://www.reaxys.com)

**DB**: Reaxys (Elsevier)
**DB size**: 구독 기반 (공개적 수치 미기재)
**DB Open/Private**: Subscription
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Reaxys 웹 플랫폼

> Elsevier | 2009 | dataset | chem
#### 📌 한 줄 요약
Reaxys는 Elsevier가 운영하는 구독 기반 화학 반응·물질·바이오활성 DB로, Beilstein(유기화학)과 Gmelin(무기·금속유기화학) DB를 통합하여 합성 화학자의 반응 검색과 합성 경로 계획을 지원한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- Beilstein(유기)과 Gmelin(무기) DB가 별도로 운영되어 통합 접근이 불편했음
**이 시스템이 필요한 이유**
- 합성 경로 계획(retrosynthesis)을 위한 통합 반응-물질 DB 필요
- SciFinder와 함께 합성 화학자의 양대 상업 인프라 역할

#### 🔨 시스템 구성
Beilstein Database(유기 화학 반응·물질), Gmelin Database(무기·금속유기 화학), 특허 화학 데이터를 통합한다. 2009년 Reaxys 브랜드로 통합 출시. 구조, 반응, 물리화학적 성질 통합 검색 가능.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 구독 플랫폼 | reaxys.com (기관 구독 필요) |
| 구조 검색 | 화합물·반응 구조 기반 검색 |
| API | Reaxys API (기관 협약에 따라 제공) |

#### 📤 제공 데이터 형식
- 화합물 레코드 (구조, 물리화학적 성질)
- 반응 레코드 (반응물, 생성물, 조건, 수율, 출처)
- 바이오활성 데이터

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 출시 | 2009년 (Beilstein+Gmelin 통합) |
| 데이터 범위 | 구독 기반; Elsevier에서 공개적 수치 미발표 |

#### ⚠️ 한계점
- 구독 기반으로 오픈 과학 RAG 시스템이 직접 접근 불가
- SciFinder와 함께 화학 분야 오픈-클로즈드 격차를 대표하는 인프라
- 고비용으로 소규모 기관 접근 제한

## 관련 정보
- **공식 페이지**: [Reaxys](https://www.reaxys.com)
