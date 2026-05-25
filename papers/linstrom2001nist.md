---
title: "The NIST Chemistry WebBook: A chemical data resource on the internet"
bib_key: "linstrom2001nist"
year: 2001
domain: chem
type: dataset
venue: Journal of Chemical & Engineering Data
paper_link: https://doi.org/10.1021/je000225m
---
# The NIST Chemistry WebBook: A chemical data resource on the internet

linstrom2001nist | 2001 | Journal of Chemical & Engineering Data | dataset | [chem] | [paper](https://doi.org/10.1021/je000225m)

**DB**: NIST Chemistry WebBook
**DB size**: 논문 미기재 (열화학 데이터 중심; 수만 화합물)
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NIST Chemistry WebBook (webbook.nist.gov)

> Journal of Chemical & Engineering Data | 2001 | dataset | chem
#### 📌 한 줄 요약
NIST Chemistry WebBook은 미국 NIST(국립표준기술연구소)가 제공하는 공개 화학 데이터 자원으로, 열화학·분광학 데이터 분야에서 독보적 깊이와 신뢰성을 가진다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 열화학, 분광학 등 물리화학 데이터가 여러 NIST 출판물에 분산되어 있었음
- 인터넷을 통한 신속하고 통합적인 데이터 접근이 불가능했음
**이 시스템이 필요한 이유**
- 화학 공학, 환경 과학, 재료 과학 연구자들이 표준 물리화학 성질을 즉시 조회할 수 있는 단일 자원 필요
- NIST의 신뢰성 있는 평가 데이터를 인터넷으로 광범위하게 배포

#### 🔨 시스템 구성
NIST-JANAF Thermochemical Tables, NIST Webbook Standard Reference Database 등 NIST의 기존 데이터 자원을 인터넷 접근 가능한 형태로 통합한다. 화합물명, 화학식, CAS 등록번호, InChI 등으로 검색 가능. 이름, 분자식, CAS 번호, 구조 검색 지원.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | webbook.nist.gov 직접 검색 |
| JSON API | NIST WebBook JSON API (화합물 데이터 조회) |

#### 📤 제공 데이터 형식
- 열화학 데이터 (ΔHf°, S°, Cp 등)
- 분광학 데이터 (IR, MS, NMR, UV-Vis)
- 열역학 상 전이 데이터
- 이온화 에너지 및 이온 에너지 데이터

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 출시 연도 | 1996년 (논문은 2001년 업데이트 기술) |
| 데이터 유형 | 열화학, 분광학, 상 전이, 이온화 에너지 등 |

#### ⚠️ 한계점
- 유기·무기 화합물 모두를 포함하나 drug-like 분자의 바이오활성 데이터는 없음
- 일부 오래된 데이터는 현대 계산 방법과 비교하면 정확도 제한
- 데이터 범위가 열화학·분광학 중심으로 특화

## 관련 정보
- **공식 페이지**: [NIST Chemistry WebBook](https://webbook.nist.gov)
- **논문**: [The NIST Chemistry WebBook](https://doi.org/10.1021/je000225m)
