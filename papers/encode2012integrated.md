---
title: "An integrated encyclopedia of DNA elements in the human genome"
bib_key: "encode2012integrated"
year: 2012
domain: bio
type: dataset
venue: Nature
paper_link: https://doi.org/10.1038/nature11247
---
# An integrated encyclopedia of DNA elements in the human genome

encode2012integrated | 2012 | Nature | dataset | [bio] | [paper](https://doi.org/10.1038/nature11247)

**DB**: ENCODE (Encyclopedia of DNA Elements)
**DB size**: 인간 게놈의 거의 30억 염기 중 생화학적 기능이 할당된 영역 (논문 기준: 게놈의 80%에 생화학적 기능 할당)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ENCODE 데이터 포털 / UCSC Genome Browser

> Nature | 2012 | dataset | bio
#### 📌 한 줄 요약
ENCODE 프로젝트가 전사, 전사인자 결합, 염색질 구조, 히스톤 변형 영역을 체계적으로 지도화하여 인간 게놈의 80%에 생화학적 기능을 할당하고 유전자 조절 메커니즘에 관한 새로운 통찰을 제공했다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 인간 게놈의 거의 30억 염기 중 단백질 코딩 영역을 제외한 대다수의 기능이 알려져 있지 않았다
- 유전체 서열 변이와 인간 질환 사이의 연관성을 해석하기 위한 기능적 주석이 부족했다

**이 시스템이 필요한 이유**
- DNA 요소 백과사전 (ENCODE) 프로젝트를 통해 게놈 전체에 걸친 기능적 요소를 체계적으로 지도화
- 전사, 전사인자 결합, 염색질 구조, 히스톤 변형 영역의 생화학적 기능 할당
- 유전체 변이와 질환 사이의 통계적 대응관계 발견으로 변이 해석 지침 제공

#### 🔨 시스템 구성
ENCODE는 수십 개의 세포주에서 다양한 생화학적 실험(ChIP-seq, RNA-seq, DNase-seq, FAIRE-seq 등)을 수행하여 전사, 전사인자 결합 부위, 열린 염색질 영역, 히스톤 변형을 지도화했다. 새로 발견된 후보 조절 요소들이 서로 물리적으로 연결되어 있고 발현 유전자와 관련됨을 확인했다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| ENCODE 포털 | https://www.encodeproject.org — 실험 데이터 검색 및 다운로드 |
| UCSC Genome Browser | 게놈 브라우저 통합 시각화 |
| GEO/SRA | 원시 데이터 공개 저장소 |

#### 📤 제공 데이터 형식
- ChIP-seq, RNA-seq, DNase-seq 등 원시 및 처리 데이터
- BED, bigWig, FASTQ 형식
- 전사인자 결합 부위, 열린 염색질, 히스톤 변형 주석

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 게놈 기능 할당 비율 | **80%** (생화학적 기능 할당) |
| 인간 게놈 크기 | ~30억 염기 (nearly three billion bases) |
| 수행된 실험 유형 | 전사, 전사인자 결합, 염색질 구조, 히스톤 변형 |

#### ⚠️ 한계점
- 80% 게놈 기능 할당은 생화학적 활성 기반으로, 기능적 중요성(functional significance)과 동일하지 않다는 논쟁이 있었다
- 특정 세포주에 국한된 실험으로 모든 세포 유형과 조직 맥락을 포괄하지 못한다
- 조절 요소의 기능적 검증(인과 관계 증명)은 추가 실험이 필요하다

## 관련 정보
- **논문**: [An integrated encyclopedia of DNA elements in the human genome](https://doi.org/10.1038/nature11247)
