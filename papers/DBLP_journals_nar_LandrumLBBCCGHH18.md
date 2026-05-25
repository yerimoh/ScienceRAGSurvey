---
title: "ClinVar: improving access to variant interpretations and supporting evidence"
bib_key: "DBLP:journals/nar/LandrumLBBCCGHH18"
year: 2018
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkx1153
---
# ClinVar: improving access to variant interpretations and supporting evidence

DBLP:journals/nar/LandrumLBBCCGHH18 | 2018 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gkx1153)

**DB**: ClinVar (NCBI 임상 변이 해석 아카이브)
**DB size**: 331,000개 이상 변이; 500,000개 이상 제출 레코드; 800개 이상 기관 참여
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ClinVar 웹사이트 / NCBI E-utilities (Entrez) API / FTP

> Nucleic Acids Research | 2018 | dataset | medical
#### 📌 한 줄 요약
NCBI가 운영하는 임상 변이 해석 공개 아카이브로, 2018년 기준 60개국 800개 이상 기관이 제출한 33만 개 이상의 변이와 50만 건 이상의 제출 레코드를 무료로 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 임상 유전체 실험실들이 각자 내부 시스템에 변이 해석을 보관하여 공유·재사용이 불가능했다
- HGMD, LOVD 등 기존 DB는 일부 데이터를 유료 또는 등록 제한으로 제공했다
- 같은 변이에 대해 기관마다 해석이 다를 때 불일치를 파악하고 해결할 메커니즘이 없었다

**이 시스템이 필요한 이유**
- 임상 유전체 해석의 재현성·투명성을 위해 근거 출처를 공개하는 변이 해석 저장소가 필요하다
- 다른 임상 데이터(EHR, 환자 표현형)와 변이 해석을 연결하는 공공 인프라 역할이 요구됐다

#### 🔨 시스템 구성
ClinVar는 변이-질환 임상 해석을 제출받아 집계·공개한다.
- **VCV (Variation in ClinVar)**: 변이 단위로 모든 제출 레코드를 집계하는 최상위 식별자 (2018 신규)
- **RCV (Reference ClinVar Assertion)**: 변이-질환 쌍 단위 집계 레코드
- **Submission**: 개별 기관의 해석 제출 단위; 임상 유의성(pathogenic/benign 등) + 근거 포함
- **증거 유형**: 문헌, 가족 이력, 기능 실험, 공개 데이터베이스

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| ClinVar 웹사이트 | ncbi.nlm.nih.gov/clinvar — 무료 검색 |
| NCBI E-utilities | Entrez API — 프로그래밍 쿼리 |
| FTP 다운로드 | XML·VCF 포맷 전체 덤프; ftp.ncbi.nlm.nih.gov/pub/clinvar/ |

#### 📤 제공 데이터 형식
- VCV XML (변이 단위 집계 레코드)
- VCF 파일 (dbSNP rs 번호 대신 Variation ID 사용, 2018 개선)
- 임상 유의성 레이블 + ACMG 분류 기준
- HPO 표현형 용어 연결

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 총 변이 수 | **331,000개 이상** |
| 제출 레코드 수 | **500,000개 이상** |
| 참여 기관 수 | **800개 이상** (60개국) |
| 직접 임상 검사 실험실 | **76개** |
| 대형 구조 변이 (>1kb) | **15,000개 이상** |
| 소마틱(체세포) 변이 | 약 **3,000개** |
| 일일 웹 방문자 | 약 **4,700명** |

#### ⚠️ 한계점
- 기관 간 해석 불일치: 동일 변이에 대해 pathogenic/benign 상충 해석 존재
- 제출 품질 편차: 제출 기관마다 근거 수준과 분류 기준이 다름
- 소마틱 변이 포함 초기 단계 (2018 기준 ~3,000개로 생식세포 변이 대비 미미)
- RAG 활용 시 임상 유의성 텍스트 레이블의 세분화 정도가 쿼리 의도와 불일치할 수 있음

## 관련 정보
- **논문**: [Landrum et al., Nucleic Acids Research 2018](https://doi.org/10.1093/nar/gkx1153)
