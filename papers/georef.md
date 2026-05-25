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

> American Geosciences Institute | 2024 | dataset | earth

## 한 줄 요약
지질학, 지구물리학, 수문학, 고생물학 분야 **480만 개 이상**의 레코드를 보유하는 가장 포괄적인 지구과학 서지 데이터베이스. 1966년 AGI(American Geosciences Institute)가 설립하여 필드 전문가가 직접 큐레이션하는 K1 지구과학 인프라.

## 연구 배경 및 동기
**지구과학 문헌의 특수성**
- 지질학·지구물리학은 학술지 외에 정부 보고서, 학위논문, 지도·단면 자료가 핵심 자원
- 범용 학술 DB(Scopus, Web of Science)는 지구과학 회색 문헌 미흡
- 1966년부터 AGI 전문가 사서가 직접 색인 — 깊이 있는 전문 큐레이션

**이 데이터베이스가 중요한 이유**
- 지구과학 **가장 포괄적 서지 DB** — 지질 지도·암석 샘플 보고서까지 포함
- 지질학 RAG 시스템의 K1 코퍼스 기반

## 핵심 기능
| 기능 | 설명 |
|---|---|
| 전문 큐레이션 | AGI 사서가 직접 색인·주제어 부여 |
| 회색 문헌 포함 | 정부 보고서·학위논문·지질 지도 색인 |
| GeoRef 어휘 | 지구과학 통제 어휘(GeoRef Thesaurus) 적용 |
| 시계열 커버리지 | 1693년부터 현재까지 역사 문헌 포함 |
| EBSCO/ProQuest 연동 | 기관 구독을 통한 전문 링크 |

## 데이터 규모
- **총 레코드**: 4.8M+ (지구과학 전 분야)
- **연간 추가**: 약 100,000건
- **접근 방식**: EBSCO, ProQuest 등 제공 기관을 통한 구독 (일부 기관 무료)
- **갱신**: 월 단위 업데이트

## 활용 방법
```
[기관 구독 접근]
  → EBSCO GeoRef 인터페이스 → 키워드/통제어 검색
  → 제목, 저자, 초록, 지리 코드, 연대 정보 반환

[GeoRef Thesaurus 활용]
  → 통제 어휘로 계층적 주제 탐색
    (예: "igneous rocks" → "granite" → "granodiorite")

[회색 문헌 탐색]
  → Document Type 필터: Government Document, Map, Thesis
  → 출판된 학술지 외 보고서·지질도 검색

[RAG 파이프라인]
  → 지구과학 도메인 RAG의 K1 코퍼스 구성 시 활용
  → 기관 API/bulk export로 지역·주제별 레코드 수집
```

## 관련 정보
- **공식 사이트**: [https://www.americangeosciences.org/information/georef](https://www.americangeosciences.org/information/georef)
- **운영 기관**: American Geosciences Institute (AGI)
- **EBSCO 접근**: [https://www.ebsco.com/products/research-databases/georef](https://www.ebsco.com/products/research-databases/georef)
