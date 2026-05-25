---
title: "ZINC 15 - Ligand Discovery for Everyone"
bib_key: "DBLP:journals/jcisd/SterlingI15"
year: 2015
domain: chem
type: dataset
venue: Journal of Chemical Information and Modeling
paper_link: https://doi.org/10.1021/acs.jcim.5b00559
---
# ZINC 15 - Ligand Discovery for Everyone

DBLP:journals/jcisd/SterlingI15 | 2015 | Journal of Chemical Information and Modeling | dataset | [chem] | [paper](https://doi.org/10.1021/acs.jcim.5b00559)

**DB**: ZINC15
**DB size**: 120M+ 구매 가능 drug-like 화합물
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ZINC15 web interface (zinc15.docking.org)

> Journal of Chemical Information and Modeling | 2015 | dataset | chem
#### 📌 한 줄 요약
ZINC15는 1억 2천만 개 이상의 구매 가능한 drug-like 화합물을 포함하며, 대사산물·약물·천연물 등 고가치 화합물과의 연결, 유전자 및 타겟 클래스별 접근, 비전문가 친화적 분석 도구를 통합하였다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 이전 ZINC 버전은 계산 전문가 중심이어서 생물학자가 활용하기 어려웠음
- 화합물-타겟 연결 및 생물학적 주석이 부족했음
**이 시스템이 필요한 이유**
- 비전문가도 리간드 발견에 활용 가능한 통합 플랫폼 필요
- 화합물을 유전자, 타겟 클래스, 생물학적 활성과 연결하는 주석 체계 구축

#### 🔨 시스템 구성
약 1억 2천만 개의 구매 가능 drug-like 화합물(4분의 1은 즉시 배송 가능)을 3D ready-to-dock 포맷으로 제공한다. 대사산물, 승인 약물, 천연물, 문헌 주석 화합물 등 고가치 화합물과 연결. 유전자 및 주요·부수 타겟 클래스별 접근 기능. 리간드 주석·구매 가능성·타겟·생물학 연결 도구 통합.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | zinc15.docking.org 검색·분석 |
| 서브셋 다운로드 | 유전자/타겟별, 성질별 필터링 후 다운로드 |
| 3D 포맷 | 모든 분자를 ready-to-dock 형태로 제공 |

#### 📤 제공 데이터 형식
- 3D 구조 (ready-to-dock, MOL2, SDF)
- SMILES
- 생물학적 활성 주석
- 타겟-화합물 매핑

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 구매 가능 drug-like 화합물 | 120M+ |
| 즉시 배송 가능 화합물 | ~25% (약 30M) |

#### ⚠️ 한계점
- 카탈로그 기반이므로 실제 구매 가능성은 지속적 업데이트 필요
- 일부 타겟-화합물 주석은 계산 예측에 기반

## 관련 정보
- **논문**: [ZINC 15 - Ligand Discovery for Everyone](https://doi.org/10.1021/acs.jcim.5b00559)
