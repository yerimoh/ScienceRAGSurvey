---
title: "COSMIC: the Catalogue Of Somatic Mutations In Cancer"
bib_key: "DBLP:journals/nar/TateBJSBBBCCDFH19"
year: 2019
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gky1015
---
# COSMIC: the Catalogue Of Somatic Mutations In Cancer

DBLP:journals/nar/TateBJSBBBCCDFH19 | 2019 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gky1015)

**DB**: COSMIC (Catalogue Of Somatic Mutations In Cancer)
**DB size**: ~600만 코딩 변이 (v86, 2018.8); 1.4M 종양 샘플; 719개 암 유전자 센서스
**DB Open/Private**: Open (학술 무료) / 영리 기관 라이선스 필요
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: COSMIC 웹사이트 / REST API / FTP 다운로드

> Nucleic Acids Research | 2019 | dataset | medical
#### 📌 한 줄 요약
Wellcome Sanger Institute가 운영하는 암 체세포 돌연변이 카탈로그로, v86 기준 약 600만 개 코딩 돌연변이와 140만 개 종양 샘플, 719개 암 유전자 센서스, 10가지 암 Hallmarks 주석을 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 암 전장유전체·엑솜 분석 결과가 개별 논문에 분산되어 있었고 비교 가능한 형식으로 통합된 저장소가 없었다
- 어떤 유전자가 암 드라이버인지 근거 기반으로 분류한 권위 있는 목록이 부재했다
- 체세포 변이 외에도 융합 유전자, 복제수 변이, 메틸화 등 다양한 체세포 변화를 통합할 필요가 있었다

**이 시스템이 필요한 이유**
- 암 유전체 연구의 공통 참조 자원으로 돌연변이 스펙트럼, 서명(mutational signature), 드라이버 유전자를 체계적으로 기록해야 한다
- 신약 개발 및 임상 해석에서 체세포 돌연변이의 맥락(조직 유형, 암 종류)을 고려한 검색이 필요하다

#### 🔨 시스템 구성
COSMIC은 여러 데이터 섹션으로 구성된다.
- **Somatic Mutations**: 수동 큐레이션 논문 + 대규모 전장엑솜·게놈 연구의 체세포 변이
- **Cancer Gene Census (CGC)**: 암 유발 유전자 목록; Tier 1 (직접 증거)·Tier 2 (간접 증거) 구분; 10가지 암 Hallmarks 주석
- **COSMIC Signatures**: 체세포 돌연변이 패턴 서명 (SBS, DBS, ID 유형)
- **기타 변이 유형**: 유전자 융합(fusions), 복제수 변이(CNV), 유전자 발현 이상, 메틸화, 약물 내성 변이

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| COSMIC 웹사이트 | cancer.sanger.ac.uk/cosmic — 무료 검색·시각화 |
| FTP 다운로드 | 전체 데이터셋 파일; 학술 무료 등록 |
| REST API | 프로그래밍 쿼리; cosmic-cancer.org |
| 영리 라이선스 | 기업·상업 목적 별도 계약 |

#### 📤 제공 데이터 형식
- 체세포 변이 TSV/VCF 파일
- Cancer Gene Census TSV (Tier, Hallmarks, 암 종류)
- 돌연변이 서명 CSV (SBS/DBS/ID 행렬)
- 약물 내성 변이 테이블

#### 📊 주요 통계 (논문 기준, v86/2018년 8월)
| 항목 | 수치 |
|---|---|
| 코딩 변이 수 | **~6,000,000개** (5,977,977개) |
| 종양 샘플 수 | **~1,400,000개** (1,391,372개) |
| Cancer Gene Census 유전자 수 | **719개** |
| 큐레이션 논문 수 | **26,251편** |
| 대규모 WGS/WES 연구 수 | **457개** |
| 유전자 융합 수 | **19,368개** |
| 복제수 변이 수 | **1,179,545개** |
| 약물 내성 변이 수 | **360개 고유 대립형질** (24개 약물) |
| 암 Hallmarks 주석 | **10가지** |

#### ⚠️ 한계점
- 학술 무료지만 영리 기관 사용은 라이선스 비용 발생 — RAG 상업 배포 시 제약
- 수동 큐레이션 기반이므로 최신 연구 반영에 시차 존재
- 조직 유형별 커버리지 불균형: 유방암·대장암 과다 대표
- 체세포 변이 중심으로 생식세포(germline) 변이 해석은 ClinVar·OMIM 참조 필요

## 관련 정보
- **논문**: [Tate et al., Nucleic Acids Research 2019](https://doi.org/10.1093/nar/gky1015)
