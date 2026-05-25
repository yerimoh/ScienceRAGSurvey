---
title: "CERN Open Data Portal"
bib_key: "cernopendata"
year: 2014
domain: physics
type: dataset
venue: CERN (system reference)
paper_link: https://opendata.cern.ch
---
# CERN Open Data Portal

cernopendata | 2014 | CERN (system reference) | dataset | [physics] | [portal](https://opendata.cern.ch)

**DB**: CERN Open Data Portal — LHC collision datasets from ATLAS, CMS, LHCb, ALICE
**DB size**: ~2 PB+ (CMS ~2 PB, ATLAS·LHCb·ALICE 추가); 약 3 PB 이상 (model knowledge)
**DB Open/Private**: Open (CC0 / CERN Open Data License)
**Modality**: ['Collision event data', 'Simulation', 'Software', 'Documentation']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CERN Open Data REST API / REANA

> CERN (system reference) | 2014 | dataset | physics
#### 한 줄 요약
2014년 CERN이 개설한 LHC 실험 공개 데이터 포털. ATLAS, CMS, LHCb, ALICE 실험의 실제 충돌 이벤트 데이터와 시뮬레이션, 분석 소프트웨어를 공개 배포. 재현 가능한 물리 분석과 교육 목적을 위해 설계된 고에너지물리학 K3 데이터 아카이브의 핵심 자원. **정식 학술 논문이 아닌 기관 시스템 참고 항목(`@misc`)임에 유의.**

#### 개발/구축 배경
**기존 인프라의 한계**
- LHC 실험 데이터는 내부 컴퓨팅 그리드(WLCG)에서만 접근 가능 — 외부 연구자·교육자 접근 불가
- 재현 가능성(reproducibility) 위기 대응: 발표된 결과의 기반 데이터 공개 필요
- 교육용 데이터셋과 실제 LHC 데이터 간 간극

**이 시스템이 필요한 이유**
- CERN 개방 접근(Open Access) 정책의 일환으로 공공 투자 연구의 데이터 공개
- 재해석(reinterpretation), 새로운 물리 모델 테스트, 머신러닝 개발에 실제 충돌 데이터 제공
- 고에너지물리학 외 커뮤니티(ML, 통계, 교육)의 LHC 데이터 활용 지원

#### 시스템 구성
- **실험별 데이터 컬렉션**: CMS (Run 1/2), ATLAS, LHCb, ALICE, LHCf, TOTEM
- **데이터 형식**: AOD/MiniAOD (CMS), xAOD (ATLAS), DST (LHCb), ESD (ALICE)
- **소프트웨어**: CMS CMSSW, ATLAS Analysis Release — Docker/REANA 통해 재현 가능 환경 제공
- **교육 데이터셋**: CMS Open Data for Education (단순화 포맷, Jupyter 기반)
- **메타데이터**: DOI 기반 인용, INSPIRE-HEP 연결

#### 제공 데이터 유형
- **충돌 이벤트 데이터**: proton-proton, Pb-Pb 충돌 (7, 8, 13 TeV)
- **시뮬레이션(MC)**: 신호·배경 이벤트 생성 샘플
- **소프트웨어**: 분석 프레임워크, ROOT 버전
- **파생 데이터**: 간단한 튜플 포맷 (교육용)
- **문서**: 분석 메모, 코드 예제

#### 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 포털 | opendata.cern.ch — 탐색·다운로드 |
| REST API | DOI 기반 레코드 조회 |
| REANA | 재현 가능 분석 플랫폼 |
| XRootD | CERN 스토리지에서 스트리밍 접근 |

#### 주요 통계 (model knowledge)
| 항목 | 수치 |
|---|---|
| 포털 개설 | 2014년 |
| CMS 공개 데이터 | **~2 PB** (Run 1/2) |
| 참여 실험 | **ATLAS, CMS, LHCb, ALICE** + LHCf, TOTEM |
| 레코드 수 | **3,500+** 데이터셋 레코드 (model knowledge) |
| 라이선스 | CC0 / CERN Open Data License |

#### 한계점
- 실제 충돌 데이터 분석을 위해 실험별 소프트웨어(CMSSW 등) 전문 지식 필요
- 데이터 볼륨이 PB 급으로 일반 인프라에서 전체 처리 불가
- Run 2/3 데이터의 공개는 분석 완료 후 수년 지연 (현재 Run 1/2 중심)
- 현재 과학 RAG 시스템에서 전혀 검색 코퍼스로 활용되지 않음 (survey K3 공백 지적)

## 관련 정보
- **포털**: [https://opendata.cern.ch](https://opendata.cern.ch)
- **교육 데이터셋**: [http://opendata.cern.ch/education](http://opendata.cern.ch/education)
