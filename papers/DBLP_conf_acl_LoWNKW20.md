---
notion_id: 355f2dcd-4912-8193-8028-d0ee8814f3e4
title: S2ORC - The Semantic Scholar Open Research Corpus
bib_key: DBLP:conf/acl/LoWNKW20
year: 2020
domain: bio, medical, physics
type: dataset
venue: ACL
paper_link: https://arxiv.org/abs/1911.02782
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# S2ORC: The Semantic Scholar Open Research Corpus

> arXiv | 2020 | dataset | bio · medical · physics

## 한 줄 요약
수백 곳의 학술 출판사와 디지털 아카이브에서 수집한 **8,110만 개**의 영어 학술 논문과 구조화된 전문(full text), 인라인 인용 네트워크를 제공하는 대규모 공개 기계가독형 학술 코퍼스.

## 연구 배경 및 동기
**기존 코퍼스의 한계**
- 기존 코퍼스는 소규모이거나 특정 도메인(AAN, PubMed Central 등)에 국한
- 구조화된 전문(full text) 및 인라인 인용 정보가 부족하여 텍스트 마이닝·인용 네트워크 분석에 활용 어려움

**이 연구가 필요한 이유**
- 범학문적으로 포괄적이고 기계가독성(machine-readable)이 높은 학술 데이터셋 필요
- 인라인 인용구, 표/그림 참조, 서지 정보까지 구조화하여 NLP 연구 지원

## 데이터 파이프라인
```
[MAG, arXiv, PubMed, Unpaywall 등 다양한 출처 수집]
      │
      ▼
[PDF/LaTeX 처리]
ScienceParse (PDF → 메타데이터·본문)
GROBID (PDF → XML: 초록, 섹션, 캡션, 인라인 인용구, 서지 정보)
      │
      ▼
[메타데이터 정규화]
가장 신뢰할 수 있는 출처 선정 → Canonical 데이터 구축
      │
      ▼
[필터링]
저자 없음, 100자 이하 텍스트 등 저품질 제거
      │
      ▼
[서지 링크 연결 (Bibliography Linking)]
자카드 지수(Jaccard) + Containment metric 조화 평균
→ 서지 항목 ↔ Paper cluster 고정밀 매핑
      │
      ▼
[Output: S2ORC]
81.1M 논문 / 380.5M 인용 링크
```

## 핵심 모듈 상세 설명
### 1. GROBID 파싱 및 후처리
- XML 결과물에서 초록, 섹션 헤더, 캡션, 인라인 인용구 분리
- 브래킷([2])이나 연도-이름 형태의 인용 스타일을 정규 표현식으로 보정

### 2. 서지 연결 (Bibliography Linking)
- 자카드 지수(Jaccard index)와 포함 지표(Containment metric)의 **조화 평균** 사용
- 서지 항목과 실제 논문 클러스터를 높은 정확도로 연결

### 3. 코퍼스 구성
| 구성 요소 | 규모 |
|---|---|
| 전체 논문 | 81.1M |
| 초록 포함 | 73.4M |
| PDF 포함 | 28.9M |
| GROBID full text | 8.1M |
| LaTeX full text | 1.5M |
| 인용 링크 | 380.5M |

## 실험 및 평가
**평가 방법**: S2ORC 텍스트로 처음부터 사전학습한 `S2ORC-SCIBERT`를 구축하여 기존 `SciBERT`와 성능 비교

**주요 결과 (F1)**
| 데이터셋 | 분야 | 태스크 | S2ORC-SCIBERT |
|---|---|---|---|
| BC5CDR | Biomed | NER | 90.41 ± 0.06 |
| GENIA | Biomed | DEP | 90.80 ± 0.19 |
| ChemProt | Biomed | REL | (본문 참조) |
| SciERC | CS | NER | 68.93 ± 0.19 |
| SciCite | Biomed & CS | CLS | 84.76 ± 0.37 |

## 핵심 기여
1. 8.1M개 오픈 액세스 논문 전문과 380.5M개 인용 네트워크를 포함한 **NLP 연구용 최대 규모 공개 학술 코퍼스** 배포
2. 텍스트 내 수식, 표, 그림이 인용된 위치(Inline References)까지 구조화하여 제공
3. 범학문적 커버리지: CS, 생의학, 물리, 수학 등 다양한 분야 포괄

## 한계점
- 동일 논문의 초안과 출판 버전을 하나의 Paper cluster로 묶는 과정에서 인용 맥락 불일치 발생 가능
- GROBID 파싱 에러 및 LaTeX 메타데이터 품질이 작성자 포맷에 따라 불균일
- 논문 클러스터링 시 모호성 존재

## 관련 정보
- **논문**: [https://arxiv.org/abs/1911.02782](https://arxiv.org/abs/1911.02782)
- **GitHub**: [https://github.com/allenai/s2orc/](https://github.com/allenai/s2orc/)
