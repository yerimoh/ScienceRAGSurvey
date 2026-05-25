---
title: "PubMed: the bibliographic database"
bib_key: "canese2013pubmed"
year: 2013
domain: medical, bio
type: dataset
venue: The NCBI Handbook (2nd ed.)
paper_link: https://www.ncbi.nlm.nih.gov/books/NBK153387/
---
# PubMed: the bibliographic database

canese2013pubmed | 2013 | The NCBI Handbook (2nd ed.) | dataset | [medical, bio] | [paper](https://www.ncbi.nlm.nih.gov/books/NBK153387/)

**DB**: PubMed / MEDLINE bibliographic database
**DB size**: 22M+ citations (2013년 기준); MEDLINE 19M+
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PubMed / NCBI E-utilities API

> The NCBI Handbook (2nd ed.) | 2013 | dataset | medical, bio
#### 📌 한 줄 요약
NCBI(미국국립생물정보센터)가 무료로 운영하는 생의학 서지 데이터베이스. **2,200만 개 이상**의 인용 레코드를 제공하며, 핵심 구성 요소인 MEDLINE의 **1,900만 개 이상** 레코드에는 MeSH 통제 어휘로 색인이 부여된다. 1996년 실험적 공개 이후 하루 **350만 건 이상**의 검색이 이루어지는 전 세계 생의학 문헌의 표준 인프라.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- NLM(미국국립의학도서관)은 기존에 CD-ROM·다이얼업 서비스로만 제공되던 MEDLINE을 인터넷으로 무료 공개하고자 하였다
- 종래 서비스는 도서관 사서 중심 설계로 연구자 직접 활용에 부적합

**이 시스템이 필요한 이유**
- 1996년 1월 실험 서비스로 출발, 1997년 4월 정식 서비스로 전환
- 1997년 6월 26일 미 국회에서 무료 MEDLINE 공개를 공식 선언
- 1997년 6월 월 약 200만 건 수준이던 검색량이 2013년 기준 하루 350만 건 이상으로 급증

#### 🔨 시스템 구성
PubMed는 MEDLINE을 포함하면서 추가 레코드(in-process citations, 전 MEDLINE 수록 이전 레코드, OLDMEDLINE, out-of-scope 레코드, PubMed Central 연계 레코드)까지 제공하는 상위 데이터베이스. MeSH(Medical Subject Headings) 통제 어휘 시소러스로 색인되며, 계층 구조를 통해 상위 개념 검색 시 하위 개념이 자동 포함된다. 2012년 기준 추가 레코드의 **90% 이상**이 전자 방식으로 제출된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | pubmed.ncbi.nlm.nih.gov — 무료 브라우저 검색 |
| E-utilities API | Entrez Programming Utilities — 8개 서버 사이드 프로그램, 무료 |

#### 📤 제공 데이터 형식
- 인용 레코드: 제목, 저자, 저널, 출판 연도, PMID
- 초록 (대부분 레코드에 포함)
- MeSH 통제 어휘 색인 (MEDLINE 레코드)
- 전문 링크 (출판사 사이트 또는 PubMed Central)
- 2012년 기준 전자 제출 비율 90%+

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 전체 인용 레코드 | **22M+** (2013년 기준) |
| MEDLINE 레코드 | **19M+** (2013년 기준) |
| 일일 검색 횟수 | **3.5M+** (2013년 기준) |
| 연간 전자 제출 비율 | **90%+** (2012년) |
| 인프라 | Linux 서버 약 62대 (Intel Nehalem, 48-64GB RAM) |
| 네트워크 | 상용 인터넷 3Gbps + Internet2 20Gbps |

#### ⚠️ 한계점
- **전문(full text) 미포함**: 초록 표시 페이지에서 출판사 사이트나 PMC로의 링크만 제공
- **색인 지연**: 전자 제출되지 않는 저널의 경우 수작업 색인이 필요하여 처리 시간 증가
- **색인 범위의 선택성**: MEDLINE은 NLM이 선정한 저널만 대상; 범위 밖 주제(판구조론, 천체물리학 등)의 논문은 out-of-scope 상태로 MeSH 색인 없이 수록
- **검색 결과 표시 한계**: 한 번의 검색에서 표시할 수 있는 결과 수에 실질적 제한

## 관련 정보
- **논문**: [https://www.ncbi.nlm.nih.gov/books/n/handbook2e/PubMed/](https://www.ncbi.nlm.nih.gov/books/n/handbook2e/PubMed/)
