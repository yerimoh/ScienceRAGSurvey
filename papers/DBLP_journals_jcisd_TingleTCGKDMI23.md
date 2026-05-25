---
title: "ZINC-22—A Free Multi-Billion-Scale Database of Tangible Compounds for Ligand Discovery"
bib_key: "DBLP:journals/jcisd/TingleTCGKDMI23"
year: 2023
domain: chem
type: dataset
venue: Journal of Chemical Information and Modeling
paper_link: https://doi.org/10.1021/acs.jcim.2c01253
---
# ZINC-22—A Free Multi-Billion-Scale Database of Tangible Compounds for Ligand Discovery

DBLP:journals/jcisd/TingleTCGKDMI23 | 2023 | Journal of Chemical Information and Modeling | dataset | [chem] | [paper](https://doi.org/10.1021/acs.jcim.2c01253)

**DB**: ZINC-22
**DB size**: 수십억 (tens of billions) 규모 make-on-demand 화합물
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CartBlanche (GUI), Globus, Amazon AWS, Oracle OCI

> Journal of Chemical Information and Modeling | 2023 | dataset | chem
#### 📌 한 줄 요약
ZINC-22는 수십억 규모의 make-on-demand 화합물 라이브러리를 기반으로 한 멀티-빌리언 스케일 리간드 발견 DB로, 규모에 비선형적으로 확장되는 유사도 검색 도구 CartBlanche와 함께 제공된다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 구매 가능 화학 공간이 수백억 분자 규모로 급격히 확장되어 기존 DB 조직 방식이 속도 저하 문제 발생
- 십억 단위 분자에서의 빠른 유사도 검색 도구가 없었음
**이 시스템이 필요한 이유**
- Make-on-demand 라이브러리의 분자 도킹에 필요한 형태(conformation), 전하, LogP, 용매화 에너지 등 신속 조회 필요
- 조 단위 분자 시대를 대비한 확장 가능한 DB 아키텍처 필요

#### 🔨 시스템 구성
Multi-billion scale make-on-demand 라이브러리에서 파생된 화합물 DB이다. CartBlanche GUI를 통해 유사 분자 검색이 가능하며, 분자 수에 비선형(sublinear) 확장되는 유사도 방법을 사용한다. 분자 다양성 분석 결과 DB 크기 증가에 따라 Bemis-Murcko scaffold도 log-linear하게 증가함. Amazon AWS, Oracle OCI 클라우드에서도 접근 가능.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| CartBlanche GUI | cartblanche22.docking.org 유사도 검색 |
| Globus | 대용량 데이터 전송 |
| Amazon AWS | 클라우드 접근 |
| Oracle OCI | 클라우드 접근 |

#### 📤 제공 데이터 형식
- 3D 형태 (conformations)
- 부분 원자 전하
- cLogP 값
- 용매화 에너지
- SMILES

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| DB 규모 | 수십억 (tens of billions) make-on-demand 화합물 |
| Scaffold 다양성 | DB 크기 100배 증가당 Bemis-Murcko scaffold log 증가 |

#### ⚠️ 한계점
- Make-on-demand 특성상 실제 합성 성공률은 화합물에 따라 다름
- 도킹 전 전처리에도 상당한 계산 자원이 필요
- 조 단위 규모 도달 시 현재 방법론의 한계 논의 필요

## 관련 정보
- **논문**: [ZINC-22 — A Free Multi-Billion-Scale Database of Tangible Compounds](https://doi.org/10.1021/acs.jcim.2c01253)
