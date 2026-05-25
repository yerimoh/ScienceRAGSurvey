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

> The NCBI Handbook (2nd ed.) | 2013 | dataset | medical · bio

## 한 줄 요약
NCBI(미국국립생물정보센터)가 무료로 운영하는 생의학 서지 데이터베이스. **2,200만 개 이상**의 인용 레코드를 제공하며, 핵심 구성 요소인 MEDLINE의 **1,900만 개 이상** 레코드에는 MeSH 통제 어휘로 색인이 부여된다. 1996년 실험적 공개 이후 하루 **350만 건 이상**의 검색이 이루어지는 전 세계 생의학 문헌의 표준 인프라.

## 연구 배경 및 동기
**생의학 문헌 접근의 필요성**
- NLM(미국국립의학도서관)은 기존에 CD-ROM·다이얼업 서비스로만 제공되던 MEDLINE을 인터넷으로 무료 공개하고자 하였다.
- 1996년 1월 실험 서비스로 출발, 1997년 4월 "실험적"이라는 표현을 삭제하고 정식 서비스로 전환하였다.
- 1997년 6월 26일 미 국회에서 무료 MEDLINE 공개를 공식 선언하였다.

**성장 배경**
- 1997년 6월 월 약 200만 건 수준이던 검색량이 2013년 기준 하루 350만 건 이상으로 급증하였다.
- 2012년 기준 PubMed에 추가된 인용 레코드의 **90% 이상**이 전자 방식으로 제출되었다.

## 핵심 기능

### PubMed와 MEDLINE의 구분
- **MEDLINE**: PubMed의 핵심 구성 요소. NLM이 선정한 학술지에 수록된 논문을 MeSH 어휘로 색인한 **1,900만 개 이상**의 레코드.
- **PubMed**: MEDLINE을 포함하면서 추가 레코드까지 제공하는 상위 데이터베이스. 총 **2,200만 개 이상**의 인용·초록 포함.

PubMed에서 MEDLINE 외에 포함되는 레코드는 다음과 같다:
- **In-process citations**: MeSH 색인 완료 전 임시 레코드
- **전 MEDLINE 수록 이전 레코드**: 해당 저널이 MEDLINE에 선정되기 이전 논문
- **OLDMEDLINE 레코드**: 현행 어휘로 아직 업데이트되지 않은 과거 레코드
- **Out-of-scope 레코드**: 판구조론, 천체물리학 등 생명과학 범위 외 주제를 다루는 일부 저널(주로 종합과학·종합화학 저널)의 논문
- **PubMed Central 연계 레코드**: PMC에 전문을 제출한 저널의 인용 레코드

### MeSH (Medical Subject Headings)
MeSH는 NLM이 개발한 통제 어휘 시소러스(Thesaurus)로, PubMed 인용 레코드의 색인에 사용된다. MeSH 번역 테이블에는 MeSH 용어 본체 외에 동의어 참조(entry terms), 소주제어(Subheadings), 출판 유형(Publication Types), 약리 작용(Pharmacological Actions), UMLS 파생 어휘 등이 포함된다. 계층 구조를 통해 상위 개념 검색 시 하위 개념이 자동으로 함께 검색된다.

### NCBI E-utilities API
"Entrez Programming Utilities(E-Utilities)"는 웹 인터페이스를 거치지 않고 프로그래밍 방식으로 PubMed를 검색·다운로드할 수 있게 해주는 여덟 개의 서버 사이드 프로그램 모음이다. 안정된 인터페이스를 제공하며 무료로 이용 가능하다.

## 데이터 규모 (2013년 기준)
| 항목 | 수치 |
|---|---|
| 전체 인용 레코드 | 22M+ |
| MEDLINE 레코드 | 19M+ |
| 일일 검색 횟수 | 3.5M+ |
| 연간 전자 제출 비율 | 90%+ (2012년) |
| 인프라 | Linux 서버 약 62대 (Intel Nehalem, 48-64GB RAM) |
| 네트워크 | 상용 인터넷 3Gbps + Internet2 20Gbps |

## 한계점
- **전문(full text) 미포함**: PubMed는 저널 논문의 전문을 직접 포함하지 않는다. 초록 표시 페이지에서 출판사 사이트나 PMC로의 링크를 제공할 뿐이다.
- **색인 지연**: 전자 제출되지 않는 저널의 경우 수작업 색인이 필요하여 처리 시간이 상당히 길어질 수 있다.
- **색인 범위의 선택성**: MEDLINE은 NLM이 선정한 저널만을 대상으로 하며, 범위 밖 주제(판구조론, 천체물리학 등)의 논문은 out-of-scope 상태로 MeSH 색인 없이 수록된다.
- **검색 결과 표시 한계**: 한 번의 검색에서 표시할 수 있는 결과 수에 실질적인 제한이 있다.

## 관련 정보
- **챕터 링크**: [https://www.ncbi.nlm.nih.gov/books/n/handbook2e/PubMed/](https://www.ncbi.nlm.nih.gov/books/n/handbook2e/PubMed/)
- **공식 사이트**: [https://pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov)
- **E-utilities 문서**: [https://www.ncbi.nlm.nih.gov/books/NBK25499/](https://www.ncbi.nlm.nih.gov/books/NBK25499/)

> **참고**: 챕터에 명시된 `paper_link`(NBK153387)는 실제로 BLAST 챕터를 가리키는 잘못된 URL이다. PubMed 챕터의 실제 URL은 `https://www.ncbi.nlm.nih.gov/books/n/handbook2e/PubMed/`이다.
