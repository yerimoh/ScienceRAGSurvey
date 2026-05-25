---
title: "GeoRef: Comprehensive Geoscience Bibliography"
bib_key: "georef"
year: 2024
domain: earth
type: dataset
venue: American Geosciences Institute
paper_link: https://www.americangeosciences.org/information/georef
---
# GeoRef: Comprehensive Geoscience Bibliography

georef | 2024 | American Geosciences Institute | dataset | [earth] | [paper](https://www.americangeosciences.org/information/georef)

**DB**: GeoRef geoscience bibliographic database
**DB size**: 4.7M+ records (AGI 공식 사이트 기준; 연 ~100,000건 증가)
**DB Open/Private**: Subscription
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: GeoRef (EBSCO 구독 배포)

> American Geosciences Institute | 2024 | dataset | earth
#### 📌 한 줄 요약
지구과학 전 분야를 아우르는 가장 포괄적인 서지 데이터베이스. AGI(American Geosciences Institute)가 1966년 설립하여 운영하며, **470만 건 이상**의 레코드(연 약 10만 건 추가)를 44개 언어, 3,500종 이상의 저널과 보고서·지도·학위논문을 포함해 색인. 북미 지질학은 1666년, 전 세계 지질학은 1933년까지 소급 수록. **정식 학술 논문이 아닌 기관 데이터베이스 참고 항목(`@misc`)임에 유의.**

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 지구과학 분야 문헌이 저널·학위논문·정부 보고서·지질 지도 등 다양한 유형으로 분산
- 다언어(44개 언어) 지구과학 자료를 통합 탐색할 수 있는 전문 인프라 부재

**이 시스템이 필요한 이유**
- 1966년 AGI 설립 이후 지구과학 커뮤니티의 표준 문헌 정보 서비스로 자리잡음
- 훈련받은 지구과학자 편집자·색인자가 GeoRef Thesaurus 통제 어휘 직접 부여
- 북미 지질 1666년, 전 세계 지질 1933년까지 소급 수록하는 장기 시계열 제공

#### 🔨 시스템 구성
AGI(American Geosciences Institute, 버지니아주 알렉산드리아 소재)가 제작·관리하며 EBSCO 등 유통 기관을 통해 기관 구독 형태로 배포. AGI 지구과학자 편집자가 직접 색인·GeoRef Thesaurus 통제 어휘 부여로 전문 큐레이션. 수록 분야: 지질학 전반, 지구물리학, 수문학, 고생물학, 암석학, 광물학, 경제지질학, 환경·공학지질학, 해양지질학, 해양학. 수록 자료 유형: 저널 논문, 단행본, 지질 지도, 회의 논문, 보고서, 학위논문(미국·캐나다), USGS 간행물. 온라인 ISSN: 2573-1874.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 기관 구독 | EBSCO 등 유통 기관을 통한 구독 — 개인 무료 접근 불가 |
| API | 공개 무료 API 미제공 |

#### 📤 제공 데이터 형식
- 서지 정보: 제목, 저자, 출판연도, 저널/자료 유형
- 초록 (논문에 따라 다름)
- GeoRef Thesaurus 통제 어휘 (계층적 주제 탐색 가능)
- 회색 문헌: 학위논문(미국·캐나다 대학원), 지질 지도, 정부 보고서

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 레코드 | **4.7M+** (AGI 공식 사이트 기준) |
| 연간 증가 | **~100,000건** (월 6,000~9,000건) |
| 수록 저널 수 | **3,500종+** (44개 언어) |
| 소급 수록 범위 (북미) | **1666년~현재** |
| 소급 수록 범위 (전 세계) | **1933년~현재** |
| 갱신 주기 | 월 단위 |
| 접근 방식 | EBSCO 등 기관 구독 |

#### ⚠️ 한계점
- **구독 전용**: 무료 공개 API 미제공 — RAG 파이프라인 구축 시 기관 구독 계약 필수
- **전문 미포함**: 서지 정보(제목·저자·초록·통제어) 제공; 원문 자체는 별도 전문 링크 필요
- **회색 문헌 편향**: 비학술 보고서·지도 대량 포함으로 문헌 품질 편차 존재
- **1933년 이전 비북미 문헌 공백**: 전 세계 지질 커버리지는 1933년부터 시작; 유럽·아시아 19세기 지질 문헌 누락 가능
- **갱신 지연**: 월 단위 업데이트로 최신 arXiv 프리프린트 등 즉시 수록 불가

## 관련 정보
- **논문**: [https://www.americangeosciences.org/information/georef](https://www.americangeosciences.org/information/georef)
