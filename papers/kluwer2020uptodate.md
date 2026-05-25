---
title: "UpToDate: evidence-based clinical decision support"
bib_key: "kluwer2020uptodate"
year: 2020
domain: medical
type: dataset
venue: Wolters Kluwer
paper_link: https://www.wolterskluwer.com/en/solutions/uptodate
---
# UpToDate: evidence-based clinical decision support

kluwer2020uptodate | 2020 | Wolters Kluwer | dataset | [medical] | [paper](https://www.wolterskluwer.com/en/solutions/uptodate)

**DB**: UpToDate (Wolters Kluwer 임상 의사 결정 지원 시스템)
**DB size**: 11,000개 이상 임상 토픽; 7,000명 이상 의사/전문가 저자·편집자
**DB Open/Private**: Subscription (유료 구독)
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: UpToDate 구독 웹 접근 / 병원·기관 라이선스

> Wolters Kluwer | 2020 | dataset | medical
#### 📌 한 줄 요약
Wolters Kluwer가 운영하는 구독 기반 임상 의사 결정 지원 시스템으로, 7,000명 이상의 전문가 저자·편집자가 작성·검토한 11,000개 이상의 임상 토픽과 근거 기반 권고를 제공하며, 전 세계 180개국 이상의 의사들이 진료 현장에서 사용한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 임상의가 진료 중 특정 질환의 진단·치료 프로토콜을 신속하게 조회할 단일 통합 참조 자원이 없었다
- PubMed 같은 원문 문헌 DB는 임상의가 직접 근거를 합성해야 해 시간이 과도하게 소요됐다
- 교과서는 업데이트 주기가 길어 최신 임상 지침을 반영하기 어려웠다

**이 시스템이 필요한 이유**
- '진료 현장(point of care)' 의사 결정을 위해 개별 문헌이 아닌 전문가가 합성한 근거 기반 권고문이 필요하다
- 의학 지식의 폭발적 증가로 개별 임상의가 모든 분야의 최신 증거를 추적하기 어렵다

#### 🔨 시스템 구성
UpToDate는 주제별 임상 토픽 아티클로 구성된다.
- **토픽 아티클**: 질환별 '배경', '역학', '진단', '치료', '후속 조치' 섹션으로 구성된 서사형 근거 합성
- **권고문(Recommendations)**: 각 토픽 내 GRADE 체계 기반 권고 강도(강함/약함) + 근거 등급(A/B/C)
- **Grading system**: UpToDate 자체 근거 수준 그레이딩 사용
- **업데이트 주기**: 연속 업데이트 (연간 최소 1회 전체 검토 + 주요 발견 시 즉시 반영)
- **참고문헌**: 각 토픽마다 수십~수백 건 1차 문헌 인용

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 구독 웹 접근 | uptodate.com — 기관·개인 구독 |
| EHR 통합 | Epic, Cerner 등 주요 EHR 내 UpToDate 위젯 |
| 모바일 앱 | iOS/Android 앱 — 구독자 오프라인 접근 |
| AlmanacQA | 라이선스 계약 하에 UpToDate 단편을 포함하는 연구용 QA 벤치마크 (유일한 공개 사례) |

#### 📤 제공 데이터 형식
- 임상 토픽 아티클 (서사형 텍스트 + 표·그림)
- 권고 요약 및 근거 등급 테이블
- 약물 정보 모듈 (별도 Lexicomp 통합)
- 의학 계산기 (용량 계산, 위험 점수 등)

#### 📊 주요 통계 (공식 자료 기준)
| 항목 | 수치 |
|---|---|
| 임상 토픽 수 | **11,000개 이상** |
| 저자·편집자 수 | **7,000명 이상** 의사·전문가 |
| 구독 국가 수 | **180개국 이상** |
| 접근 형태 | 구독 (Subscription) |
| 운영 기관 | Wolters Kluwer Health |

#### ⚠️ 한계점
- **유료 구독 장벽**: 모든 오픈 Scientific RAG 시스템이 접근할 수 없는 핵심 한계 — 논문에서 "open scientific RAG cannot reach"의 대표 사례
- 구독료가 고가여서 저소득 국가 의료 기관의 접근 제한
- AlmanacQA 외에 UpToDate 데이터를 활용한 공개 RAG 벤치마크 사실상 전무
- 자체 근거 등급 체계가 외부 GRADE 체계와 완전히 호환되지 않음

## 관련 정보
- **공식 사이트**: [UpToDate (Wolters Kluwer)](https://www.wolterskluwer.com/en/solutions/uptodate)
