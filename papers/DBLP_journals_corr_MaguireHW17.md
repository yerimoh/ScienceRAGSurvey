---
title: "HEPData: A Repository for High Energy Physics Data"
bib_key: "DBLP:journals/corr/MaguireHW17"
year: 2017
domain: physics
type: dataset
venue: Journal of Physics Conference Series (arXiv:1704.05473)
paper_link: https://arxiv.org/abs/1704.05473
---
# HEPData: A Repository for High Energy Physics Data

DBLP:journals/corr/MaguireHW17 | 2017 | Journal of Physics Conference Series | dataset | [physics] | [paper](https://arxiv.org/abs/1704.05473)

**DB**: HEPData — open-access repository for high-energy physics experimental data
**DB size**: Data points underlying several thousand publications (2017 기준); 현재 ~20,000+ 기록 (model knowledge)
**DB Open/Private**: Open
**Modality**: ['Table', 'Plot data', 'Numerical arrays']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: HEPData REST API / hepdata_lib (Python)

> Journal of Physics Conference Series | 2017 | dataset | physics
#### 한 줄 요약
더럼 고에너지물리 데이터베이스(HEPData)의 현대적 재구축을 기술한 논문. **40년 이상** 축적된 입자물리학 실험 논문의 수치 결과(산란 단면적, 분포, 상관 행렬)를 기계가독형 형식으로 보존하는 고에너지물리학 유일의 수치 데이터 아카이브. 2015년 이후 Invenio v3 기반으로 완전 재작성되어 hepdata.net에서 제공.

#### 개발/구축 배경
**기존 인프라의 한계**
- 1960년대 더럼 SPIRES/HEPData에서 시작된 레거시 플랫폼(hepdata.cedar.ac.uk)은 현대 기능 부재
- 논문의 수치 결과가 그림·PDF에만 존재하여 재분석·재사용 불가
- 데이터 포맷 표준화 없음 — 연구자들이 그림에서 수동으로 디지타이징

**이 시스템이 필요한 이유**
- LHC 실험(ATLAS, CMS, LHCb, ALICE)의 복잡한 측정 결과(다차원 분포, 공분산 행렬, 체계적 불확도)를 구조화 보존 필요
- 재해석(reinterpretation), 통계 결합, 모델 독립 한계 설정에 기계가독형 데이터 필수
- 고에너지물리학 커뮤니티 표준 데이터 공유 플랫폼 역할

#### 시스템 구성
Invenio v3 기반 디지털 라이브러리 프레임워크. 오픈소스(GitHub 공개). YAML/JSON 기반 HEPData 제출 형식. InspireHEP·arXiv·DOI 직접 연결. 그림별 데이터 테이블 구조 (x축, y축, 불확도, 단위 포함). ROOT·YODA·CSV·JSON 다운로드 지원.

#### 제공 데이터 유형
- **산란 단면적(cross-sections)**: 에너지별·각도별 미분 및 전체 단면적
- **분포(distributions)**: 불변 질량, 횡운동량, 위슬레이-변수 분포
- **상관 행렬(correlation matrices)**: 공분산·상관 행렬 (통계 결합용)
- **한계 곡선(exclusion limits)**: 초대칭·암흑 물질 탐색 결과
- **효율·수용도**: 분석별 선택 효율 및 기하학적 수용도

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| hepdata.net | 웹 탐색·다운로드·시각화 |
| HEPData REST API | JSON/YAML 반환 |
| hepdata_lib | Python 라이브러리 (제출·읽기) |
| ROOT/YODA 파일 | 직접 다운로드 |

#### 주요 통계 (2017 논문 기준 + model knowledge)
| 항목 | 수치 |
|---|---|
| 논문 수 (2017 기준) | **수천** 편 (several thousand publications) |
| 운영 기간 | **40년+** (1970년대 더럼 시작) |
| 현재 기록 수 | **~20,000+** 기록 (model knowledge, 2025) |
| 공개 소프트웨어 | GitHub (오픈소스) |
| 연결 시스템 | InspireHEP, arXiv, DOI |

#### 한계점
- 이전 레거시 논문의 데이터는 수동 입력 또는 디지타이징 필요 — 완전성 부족
- 그림에서 데이터를 추출하지 않은 논문은 HEPData에 미등록
- 복잡한 다차원 분포(e.g., 2D 변수 스캔)의 완전한 구조 표현 한계
- 현재 RAG 시스템에서 전혀 검색 코퍼스로 활용되지 않음 (survey K3 공백 지적)

## 관련 정보
- **논문**: [https://arxiv.org/abs/1704.05473](https://arxiv.org/abs/1704.05473)
- **HEPData**: [https://hepdata.net](https://hepdata.net)
