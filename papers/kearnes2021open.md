---
title: "The Open Reaction Database"
bib_key: "kearnes2021open"
year: 2021
domain: chem
type: dataset
venue: Journal of the American Chemical Society
paper_link: https://doi.org/10.1021/jacs.1c09820
---
# The Open Reaction Database

kearnes2021open | 2021 | Journal of the American Chemical Society | dataset | [chem] | [paper](https://doi.org/10.1021/jacs.1c09820)

**DB**: ORD (Open Reaction Database)
**DB size**: 중앙화 저장소 (초기 공개 시 규모는 논문 미기재; GitHub 배포)
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ORD schema + GitHub 기반 중앙화 저장소

> Journal of the American Chemical Society | 2021 | dataset | chem
#### 📌 한 줄 요약
ORD는 저널 논문·특허·전자 실험 노트의 유기 반응 데이터를 구조화·공유하기 위한 오픈 액세스 스키마와 인프라로, 벤치 반응에서 자동화 고처리량 실험까지 지원한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 화학 반응 데이터가 저널·특허·전자 노트에 비구조화 형태로 저장되어 하류 AI 응용의 큰 장벽이었음
- 공유·재사용 가능한 반응 데이터 표준 포맷이 부재했음
**이 시스템이 필요한 이유**
- 일관된 데이터 표현으로 컴퓨터 지원 합성 계획, 반응 예측, 기타 예측 화학 과제의 수준 향상
- 산업계(Relay Therapeutics, Merck, Pfizer 등)와 학계의 공동 개방 데이터 생태계 구축

#### 🔨 시스템 구성
벤치 반응부터 자동화 고처리량 실험, 흐름 화학(flow chemistry)까지 지원하는 반응 데이터 스키마를 정의한다. 스키마, 지원 코드, 웹 기반 사용자 인터페이스 모두 GitHub에 공개. Relay Therapeutics, Merck, Pfizer, MIT, UCSF, Caltech 등 산학 공동 개발.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| GitHub | 데이터, 스키마, 코드 전체 공개 |
| 웹 인터페이스 | 데이터 탐색·기여 UI |

#### 📤 제공 데이터 형식
- Protocol Buffer (protobuf) 기반 ORD 스키마
- 반응물·시약·생성물 구조 (SMILES, InChI)
- 반응 조건 (온도, 용매, 촉매, 수율 등)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 수록 반응 규모 | 논문 미기재 (초기 공개 저장소 기반) |

#### ⚠️ 한계점
- 커뮤니티 기여 기반으로 초기 데이터 규모가 USPTO 코퍼스 대비 소규모
- 기여 데이터 품질 및 일관성은 기여자에 의존
- Protobuf 스키마에 대한 학습 곡선이 일부 사용자에게 장벽

## 관련 정보
- **논문**: [The Open Reaction Database](https://doi.org/10.1021/jacs.1c09820)
